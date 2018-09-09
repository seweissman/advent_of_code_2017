from enum import Enum
import re

# Kind of a mess but it does the job
class Walker:
    class Dir(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dir = self.Dir.DOWN
        self.letters = []
        self.steps = 1

    def get_value(self, diagram, direction):
        row = None
        col = None
        if direction == self.Dir.UP and self.row > 0:
            row = self.row - 1
            col = self.col
        if direction == self.Dir.DOWN and self.row < len(diagram) - 1:
            row = self.row + 1
            col = self.col
        if direction == self.Dir.LEFT and self.col > 0:
            row = self.row
            col = self.col - 1
        if direction == self.Dir.RIGHT and self.col < len(diagram[self.row]) - 1:
            row = self.row
            col = self.col + 1

        if row is None:
            return None
        if diagram[row][col] == " ":
            return None
        return diagram[row][col]

    def step(self, diagram):
        """
        Step to the next square in the diagram. Returns false if we are
        at the end, otherwise true.
        """

        # Advance walker to new space in its current direction
        if self.dir == self.Dir.UP:
            next_row = self.row - 1
            next_col = self.col
        if self.dir == self.Dir.DOWN:
            next_row = self.row + 1
            next_col = self.col
        if self.dir == self.Dir.LEFT:
            next_row = self.row
            next_col = self.col - 1
        if self.dir == self.Dir.RIGHT:
            next_row = self.row
            next_col = self.col + 1
        if next_row < 0 or next_row > len(diagram) - 1:
            return False
        if next_col < 0 or next_col > len(diagram[0]) - 1:
            return False

        self.row = next_row
        self.col = next_col

        # Now deal with the letter in the new space
        c = diagram[self.row][self.col]

        # print(self.row, self.col, self.dir, c)
        # End case
        if c == " ":
            return False
        self.steps += 1
        # Turn case
        if c == "+":
            self.change_direction(diagram)

        # letter case
        m = re.match("([A-Z])", c)
        if m:
            letter = m.group(1)
            self.letters.append(letter)
        return True

    def change_direction(self, diagram):
        if self.dir in [self.Dir.UP, self.Dir.DOWN]:
            possible_next_dirs = set([self.Dir.LEFT, self.Dir.RIGHT])
        else:
            possible_next_dirs = set([self.Dir.UP, self.Dir.DOWN])
        for d in possible_next_dirs:
            v = self.get_value(diagram, d)
            if v is not None:
                self.dir = d

def run_diagram(diagram):
    # find start
    start = 0
    c = diagram[0][start]
    while c != "|":
        start += 1
        c = diagram[0][start]
    
    walker = Walker(0, start)

    not_at_end = True
    while not_at_end:
        not_at_end = walker.step(diagram)
    return ("".join(walker.letters), walker.steps)
        
test_input = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """

test_diagram = test_input.split("\n")
assert run_diagram(test_diagram) == ("ABCDEF",38)

if __name__ == "__main__":
    with open("day19.input.txt") as f:
        diagram_str = f.read()
    diagram = diagram_str.split("\n")
    print([len(l) for l in diagram])
    print(run_diagram(diagram))
