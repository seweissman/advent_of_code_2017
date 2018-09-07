class LinkedList:
    def __init__(self, n):
        self.val = n
        self.nxt = self
        self.prv = self

    def __str__(self):
        s = "["
        curr = self
        while True:
            s += str(curr.val) + " "
            curr = curr.nxt
            if curr == self:
                break
        s += "]"
        return s

def spinlock(step, num_spins):
    buffer = LinkedList(0)
    curr_pos = buffer
    curr_val = 0
    for c in range(num_spins):
        # print(str(buffer))
        if c % 100000 == 0:
            print("c =", c)
        curr_val += 1
        spin_pos = curr_pos
        for p in range(step):
            spin_pos = spin_pos.nxt
        # print("spin_pos =", spin_pos)
        new_node = LinkedList(curr_val)
        new_node.prv = spin_pos
        new_node.nxt = spin_pos.nxt
        spin_pos.nxt = new_node
        curr_pos = new_node
    return curr_pos

# Rewriting above with linkedlist means every round is O(step)
# but still not fast enough. BUT, zero never moves, so we can
# just keep track of the number after zero, which is much quicker
def spinlock0(step, num_spins):
    buffer_len = 1
    curr_pos = 0
    num_after_zero = 1
    curr_num = 0
    for c in range(num_spins):
        if c % 100000 == 0:
            print("c =", c)
        curr_num += 1
        spin_pos = (curr_pos + step) % buffer_len
        # print(curr_pos, spin_pos, num_after_zero)

        # We are changing the number after zero
        if spin_pos == 0:
            num_after_zero = curr_num
        buffer_len += 1
        curr_pos = (spin_pos + 1) % buffer_len
    return num_after_zero

assert spinlock(3, 2017).nxt.val == 638

def node_after_zero(ll):
    curr = ll
    while curr.val != 0:
        curr = curr.nxt
    return curr.nxt

if __name__ == "__main__":
    ll = spinlock(337, 2017)
    print(ll.nxt.val)
    after_zero = node_after_zero(ll)
    assert after_zero.prv.val == 0
    print(after_zero.val)
    assert spinlock0(337, 2017) == after_zero.val
    print(spinlock0(337, 50000000))

