"""
Day 8: I Heard You Like Registers
"""

from collections import defaultdict
import re

INSTRUCTION_PATTERN = re.compile("([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) (>|<|>=|==|<=|!=) (-?[0-9]+)")
REGISTERS = defaultdict(int)

def execute(instruction_list, registers):
    """
    Executes a set of instructions and returns the highest
    register value seen
    """
    highest = None
    for instruction in instruction_list:
        # Check for highest val currently in registers
        if len(registers.values()) > 0:
            max_val = max(registers.values())
            if highest is None or max_val > highest:
                highest = max_val
        # Make sure we don't execute an empty instruction
        instruction = instruction.strip()
        if instruction == "":
            continue

        m = INSTRUCTION_PATTERN.search(instruction)
        op_register = m.group(1)
        op = "-" if m.group(2) == "dec" else "+"
        op_value = int(m.group(3))
        cond_register = m.group(4)
        cond = m.group(5)
        cond_value = m.group(6)
        # The condition to check to see if we evaluate op
        cond_eval_str = "{0} {1} {2}".format(registers[cond_register], cond, cond_value)
        # The op to evaluate if cond is true
        op_eval_str = "{0} {1} {2}".format(registers[op_register], op, op_value) 
        # Evaluate and execute
        if(eval(cond_eval_str)):
            op_eval = eval(op_eval_str)
            registers[op_register] = op_eval
    return highest

sample_instructions_str = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
sample_instructions = sample_instructions_str.split("\n")

highest = execute(sample_instructions, REGISTERS)
assert max(REGISTERS.values()) == 1
assert highest == 10


if __name__ == "__main__":
    REGISTERS = defaultdict(int)
    file_in = open("day8.input.txt")
    instructions = file_in.readlines()
    highest = execute(instructions, REGISTERS)
    print(max(REGISTERS.values()))
    print(highest)
