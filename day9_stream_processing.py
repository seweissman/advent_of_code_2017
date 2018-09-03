"""
Day 9: Stream Processing
"""

import enum

def remove_ignored(stream):
    stream_out = ""
    ignore_next = False
    for s in stream:
        if ignore_next:
            ignore_next = False
            continue
        if s == "!":
            ignore_next = True
        else:
            ignore_next = False
            stream_out += s
    return stream_out


assert remove_ignored("<{!>}>") == "<{}>"
assert remove_ignored("{{<!>},{<!>},{<!>},{<a>}}") == "{{<},{<},{<},{<a>}}"


class State(enum.Enum):
    BEGIN = 1
    GROUP = 2
    GARBAGE = 3
    IGNORE = 4


def process_stream(stream):
    curr_state = State.BEGIN
    state_stack = []
    group_count = 0
    garbage_count = 0
    score = 0
    count = 0
    for s in stream:
        #print(s,curr_state,state_stack,group_count,score)
        if s == "{":
            if curr_state == State.BEGIN:
                state_stack.append(curr_state)
                curr_state = State.GROUP
                group_count += 1
            elif curr_state == State.GROUP:
                state_stack.append(curr_state)
                curr_state = State.GROUP
                group_count += 1
            elif curr_state == State.GARBAGE:
                garbage_count += 1
                pass
            elif curr_state == State.IGNORE:
                curr_state = state_stack.pop()
        elif s == "}":
            if curr_state == State.BEGIN:
                raise ValueError("Close group seen outside group {}".format(count))
            elif curr_state == State.GROUP:
                curr_state = state_stack.pop()
                score += group_count
                group_count -= 1
            elif curr_state == State.GARBAGE:
                garbage_count += 1
                pass
            elif curr_state == State.IGNORE:
                curr_state = state_stack.pop()
                pass
        elif s == "<":
            if curr_state == State.BEGIN:
                state_stack.append(curr_state)
                curr_state = State.GARBAGE
            elif curr_state == State.GROUP:
                state_stack.append(curr_state)
                curr_state = State.GARBAGE
            elif curr_state == State.GARBAGE:
                garbage_count += 1
                pass
            elif curr_state == State.IGNORE:
                curr_state = state_stack.pop()
        elif s == ">":
            if curr_state == State.BEGIN:
                raise ValueError("Garbage close seen outside group {}".format(count))
            elif curr_state == State.GROUP:
                raise ValueError("Garbage close seen without open {}".format(count))
            elif curr_state == State.GARBAGE:
                curr_state = state_stack.pop()
            elif curr_state == State.IGNORE:
                curr_state = state_stack.pop()
        elif s == "!":
            if curr_state == State.BEGIN:
                raise ValueError("Ignore seen outside group {}".format(count))
            elif curr_state == State.IGNORE:
                curr_state = state_stack.pop()
            else:
                state_stack.append(curr_state)
                curr_state = State.IGNORE
        else:
            if curr_state == State.BEGIN:
                raise ValueError("Random characters seen {}".format(count))
            elif curr_state == State.IGNORE:
                curr_state = state_stack.pop()
            elif curr_state == State.GARBAGE:
                garbage_count += 1
            else:
                pass
        count += 1
    return (score, garbage_count)


score, garbage_count = process_stream("{}")
assert score == 1
score, garbage_count = process_stream("{{{}}}")
assert score == 6
score, garbage_count = process_stream("{{},{}}")
assert score == 5
score, garbage_count = process_stream("{{{},{},{{}}}}")
assert score == 16
score, garbage_count = process_stream("{<a>,<a>,<a>,<a>}")
assert score == 1
score, garbage_count = process_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}")
assert score == 9
score, garbage_count = process_stream("{{<!!>},{<!!>},{<!!>},{<!!>}}")
assert score == 9
score, garbage_count = process_stream("{{<a!>},{<a!>},{<a!>},{<ab>}}")
assert score == 3

score, garbage_count = process_stream("<>")
assert garbage_count == 0
score, garbage_count = process_stream("<random characters>")
assert garbage_count == 17
score, garbage_count = process_stream("<<<<>")
assert garbage_count == 3
score, garbage_count = process_stream("<{!>}>")
assert garbage_count == 2
score, garbage_count = process_stream("<!!>")
assert garbage_count == 0
score, garbage_count = process_stream("<!!!>>")
assert garbage_count == 0
score, garbage_count = process_stream('<{o"i!a,<{i<a>')
assert garbage_count == 10

if __name__ == "__main__":
    with open("day9.input.txt") as f:
        INPUT = f.read()
    print(process_stream(INPUT.strip()))
            
