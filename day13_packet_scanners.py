from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1


class Layer:
    def __init__(self, scanned, scan_range, scan_pos):
        self.scanned = scanned
        self.scan_range = scan_range
        self.scan_pos = scan_pos
        self.scan_dir = Direction.DOWN


    def advance(self):
        if self.scanned:
            if self.scan_dir == Direction.DOWN:
                if self.scan_pos < self.scan_range - 1:
                    self.scan_pos += 1
                else:
                    self.scan_dir = Direction.UP
                    self.scan_pos -= 1
            else:
                if self.scan_dir == Direction.UP:
                    if self.scan_pos > 0:
                        self.scan_pos -= 1
                    else:
                        self.scan_dir = Direction.DOWN
                        self.scan_pos += 1
    def __str__(self):
        if self.scanned:
            return "Scanning: {}/{}".format(self.scan_pos, self.scan_range)
        else:
            return "Empty"

    def reset(self):
        if self.scanned:
            self.scan_dir = Direction.DOWN
            self.scan_pos = 0

    def __repr__(self):
        return self.__str__()

def parse_firewall(s):
    s = s.strip()
    lines = s.split("\n")

    i = 0
    firewall = []
    for line in lines:
        depth, scan_range  = line.split(": ")

        depth = int(depth)
        scan_range = int(scan_range)

        while i < depth:
            layer = Layer(False, None, None)
            firewall.append(layer)
            i += 1
        layer = Layer(True, scan_range, 0)
        firewall.append(layer)
        i += 1
    return firewall

input = """0: 3
1: 2
4: 4
6: 4"""

test_firewall = parse_firewall(input)

def advance_firewall(firewall):
    for layer in firewall:
        layer.advance()

def print_firewall(firewall, t=-1):
    f_str = ""
    for i,layer in enumerate(firewall):
        if i == t:
            f_str += " *" + str(layer)
        else:
            f_str += "  " + str(layer)
    print(f_str)

def reset_firewall(firewall):
    for layer in firewall:
        layer.reset()

def run_firewall(firewall, delay = 0):
    trip_severity = 0
    t = 0
    while t - delay < len(firewall):
        # print_firewall(firewall, t)
        if t >= delay:
            layer = firewall[t - delay]
            # If there is a scanner at the top of the layer as your 
            # packet enters it, you are caught.        
            if layer.scan_pos == 0:
                severity = (t - delay) * layer.scan_range
                trip_severity += severity
        advance_firewall(firewall)
        t += 1
    return trip_severity

def delay_firewall(firewall):
    """ 
    Calculate how long we have to delay in order to
    get through firewall
    """
    delay = 0
    # We just brute force this until we find a delay that works
    while True:
        i = 0
        while i < len(firewall):
            layer = firewall[i]
            # If we get caught at 0, break out of the loop and try the
            # next delay
            if layer.scanned and (delay + i) % ((layer.scan_range-1)*2) == 0:
                break
            i += 1
        # Check if we got to the end of the firewall
        if i == len(firewall):
            return delay
        delay += 1

assert run_firewall(test_firewall) == 24
reset_firewall(test_firewall)
assert run_firewall(test_firewall, delay=10) == 0
reset_firewall(test_firewall)
assert delay_firewall(test_firewall) == 10

if __name__ == "__main__":
    with open("day13.input.txt") as f:
        input = f.read().strip()

    firewall = parse_firewall(input)
    print(run_firewall(firewall))

    reset_firewall(firewall)
    print(delay_firewall(firewall))
    
    
# x x x .. x
# x x x    x
# x   x    x
# x        x
# x

