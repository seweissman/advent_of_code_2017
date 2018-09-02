"""
Day 8: I Heard You Like Registers
"""

from collections import defaultdict
import re

INSTRUCTION_PATTERN = re.compile("([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) (>|<|>=|==|<=|!=) (-?[0-9]+)")
REGISTERS = defaultdict(int)


def execute(instruction_list):
    highest = None
    for instruction in instruction_list:
        if len(REGISTERS.values()) > 0:
            max_val = max(REGISTERS.values())
            if highest is None or max_val > highest:
                highest = max_val
        instruction = instruction.strip()
        if instruction == "":
            continue
        print("Instruction:", instruction)
        m = INSTRUCTION_PATTERN.search(instruction)
        op_register = m.group(1)
        op = "-" if m.group(2) == "dec" else "+"
        op_value = int(m.group(3))
        cond_register = m.group(4)
        cond = m.group(5)
        cond_value = m.group(6)
        cond_eval_str = "REGISTERS['{0}'] {1} {2}".format(cond_register, cond, cond_value)
        op_eval_str = "REGISTERS['{0}'] {1}= {2}".format(op_register, op, op_value) 
        if(eval(cond_eval_str)):
            exec(op_eval_str)
    return highest

sample_instructions_str = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
sample_instructions = sample_instructions_str.split("\n")

execute(sample_instructions)
assert max(REGISTERS.values()) == 1



if __name__ == "__main__":
    REGISTERS = defaultdict(int)
    file_in = open("day8.input.txt")
    instructions = file_in.readlines()
    highest = execute(instructions)
    print(max(REGISTERS.values()))
    print(highest)
