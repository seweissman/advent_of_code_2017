import re
from collections import defaultdict

with open("day20.input.txt") as f:
    pcount = 0
    min_n = None
    min_p = None
    for line in f.readlines():
        m = re.match(".*a=<(-?\d+),(-?\d+),(-?\d+)>.*", line)
        if m:
            ax = int(m.group(1))
            ay = int(m.group(2))
            az = int(m.group(3))
            n = abs(ax) + abs(ay) + abs(az)
            if min_n is None or n < min_n:
                min_n = n
                min_p = pcount
            print(ax, ay, az, n)
        else:
            raise ValueError("Not parsed: " + line)
        pcount += 1
    assert min_p == 258

# p=<-3787,-3683,3352>, v=<41,-25,-124>, a=<5,9,1>
def str_to_particle(s):
    m = re.match("p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>", line)
    if m:
        px = int(m.group(1))
        py = int(m.group(2))
        pz = int(m.group(3))
        p = (px, py, pz)

        vx = int(m.group(4))
        vy = int(m.group(5))
        vz = int(m.group(6))
        v = (vx, vy, vz)

        ax = int(m.group(7))
        ay = int(m.group(8))
        az = int(m.group(9))
        a = (ax, ay, az)

        return Particle(p, v, a)
    else:
        raise ValueError("Not parsed: " + line)


class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def move(self):
        self.v = (self.v[0] + self.a[0], self.v[1] + self.a[1], self.v[2] + self.a[2])
        self.p = (self.p[0] + self.v[0], self.p[1] + self.v[1], self.p[2] + self.v[2])

    def __str__(self):
        return "<Particle: " + str(self.p) + ">"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    particle_set = set()
    #particle_map = {}
    with open("day20.input.txt") as f:
        for line in f.readlines():
            line.strip()
            particle = str_to_particle(line)
            particle_set.add(particle)
            #particle_map[id(particle)] = particle
    #print(particle_set)
    for i in range(10000):
        location_map = defaultdict(list)
        for particle in particle_set:
            location_map[particle.p].append(particle)
            particle.move()

        col_count = 0
        for k in location_map:
            if len(location_map[k]) > 1:
                col_count += len(location_map[k])
                particle_set = particle_set - set(location_map[k])
                # print(location_map[k])
        if col_count > 0:
            print("Collisions:", col_count)
        print(len(particle_set))
