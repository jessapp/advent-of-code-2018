from collections import defaultdict

def get_minute(line):
    words = line.split()
    time = words[1][:-1]
    return int(time.split(':')[1])

def get_best(d):
    best = None
    for k,v in d.items():
     if best is None or v > d[best]:
         best = k
    return best

def get_worst(d):
    worst = None
    for k, v in d.items():
        if worst is None or v < d[worst]:
            worst = k
    return worst 


def part_1():
    text_input = open('input.txt', "r")
    lines = []

    for line in text_input:
        lines.append(line.rstrip())

    lines.sort()
    guard_sleep_sched = defaultdict(int)
    guard_sleep_count = defaultdict(int)

    guard = None
    asleep = None

    for line in lines:
        minute = get_minute(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = minute
            print("falls asleep at", asleep)
        elif 'wakes up' in line:
            for i in range(asleep, minute):
                guard_sleep_sched[(guard, i)] += 1
                guard_sleep_count[guard] += 1

    worst_guard = get_worst(guard_sleep_count)

    most_slept_min = None
    most_slept_count = 0

    for k, v in guard_sleep_sched.items():
        guard_id, minute = k
        if guard_id == worst_guard:
            print(k)
            if v > most_slept_count:
                most_slept_min = minute
                most_slept_count = v

    return worst_guard * most_slept_min
