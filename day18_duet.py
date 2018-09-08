from collections import defaultdict

class Machine:
    def __init__(self, program):
        self.registers = defaultdict(int)
        self.last_sound = None
        self.instruction_pointer = 0
        self.program = program

    def execute_program(self):
        success = True
        while success:
            success = self.execute_instruction()
            print(dict(self.registers))

    def execute_instruction(self):
        inst = self.program[self.instruction_pointer]
        print(inst)
        if (self.instruction_pointer >= len(self.program) or
            self.instruction_pointer < 0):
            return False
        inst_parts = inst.split(" ")
        op = inst_parts[0]
        x = inst_parts[1]
        if len(inst_parts) > 2:
            y = inst_parts[2]
            try:
                y = int(y)
            except ValueError:
                y = self.registers[y]

        if op == "snd":
            self.last_sound = self.registers[x]
            self.instruction_pointer += 1
        if op == "set":
            self.registers[x] = y
            self.instruction_pointer += 1
        if op == "add":
            self.registers[x] = self.registers[x] + y
            self.instruction_pointer += 1
        if op == "mul":
            self.registers[x] = self.registers[x] * y
            self.instruction_pointer += 1
        if op == "mod":
            self.registers[x] = self.registers[x] % y
            self.instruction_pointer += 1
        if op == "rcv":
            if self.registers[x] != 0:
                return False
            self.instruction_pointer += 1
        if op == "jgz":
            if self.registers[x] > 0:
                self.instruction_pointer += y
            else:
                self.instruction_pointer += 1
        return True

    
test_program_str = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

test_program = test_program_str.split("\n")
test_machine = Machine(test_program)
test_machine.execute_program()
assert test_machine.last_sound == 4

if __name__ == "__main__":
    with open("day18.input.txt") as f:
        program_str = f.read().strip()
    program = program_str.split("\n")
    machine = Machine(program)
    machine.execute_program()
    print(machine.last_sound)
