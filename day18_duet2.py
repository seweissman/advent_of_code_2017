from collections import defaultdict, deque
from enum import Enum

class Machine:
    
    class State(Enum):
        EXECUTING = 0
        WAITING = 1
        SENDING = 2
        DONE = 3

    def __init__(self, program, program_id):
        self.send_count = 0
        self.registers = defaultdict(int)
        self.registers["p"] = program_id
        self.program_id = program_id
        self.receive_queue = deque([])
        self.last_sent = None
        self.instruction_pointer = 0
        self.program = program

    def execute_program(self):
        state = self.State.EXECUTING
        while state != self.State.DONE:
            state = self.execute_instruction()
            if state == self.State.WAITING or state == self.State.SENDING or state == self.State.DONE:
                yield state

    def execute_instruction(self):
        if (self.instruction_pointer >= len(self.program) or
            self.instruction_pointer < 0):
            return self.State.DONE
        inst = self.program[self.instruction_pointer]

        inst_parts = inst.split(" ")
        op = inst_parts[0]
        x = inst_parts[1]
        y = None
        if len(inst_parts) > 2:
            y = inst_parts[2]
            try:
                y = int(y)
            except ValueError:
                y = self.registers[y]
        print(self.program_id, dict(self.registers))
        print(self.program_id, inst, ":", op, x, y)
        print(self.program_id, self.receive_queue)
        if op == "snd":
            try:
                x = int(x)
            except ValueError:
                x = self.registers[x]
            self.last_sent = x
            self.instruction_pointer += 1
            self.send_count += 1
            return self.State.SENDING
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
            if len(self.receive_queue) > 0:
                self.registers[x] = self.receive_queue.pop()
                self.instruction_pointer += 1
            else:
                return self.State.WAITING
        if op == "jgz":
            try:
                x = int(x)
            except ValueError:
                x = self.registers[x]
            if x > 0:
                self.instruction_pointer += y
            else:
                self.instruction_pointer += 1
        return self.State.EXECUTING

    def receive(self,v):
        self.receive_queue.appendleft(v)

def run_machines(machine0, machine1):
    while True:
        state0 = next(machine0.execute_program())
        if state0 == Machine.State.SENDING:
            machine1.receive(machine0.last_sent)
        state1 = next(machine1.execute_program())
        if state1 == Machine.State.SENDING:
            machine0.receive(machine1.last_sent)
        if state0 == Machine.State.WAITING and state1 == Machine.State.WAITING:
            break


test_program_str = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

test_program = test_program_str.split("\n")
test_machine0 = Machine(test_program, 0)
test_machine1 = Machine(test_program, 1)
# run_machines(test_machine0, test_machine1)

if __name__ == "__main__":
    with open("day18.input.txt") as f:
        program_str = f.read().strip()
    program = program_str.split("\n")
    machine0 = Machine(program, 0)
    machine1 = Machine(program, 1)
    run_machines(machine0, machine1)
    print(machine1.send_count)
