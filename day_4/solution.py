from collections import defaultdict

def get_minute(line):
    words = line.split()
    time = words[1][:-1]
    return int(time.split(':')[1])

def get_most_frequent(d):
    most_frequent = None
    for k,v in d.items():
     if most_frequent is None or v > d[most_frequent]:
         most_frequent = k
    return most_frequent

def parse_text_input():
    text_input = open('input.txt', "r")
    lines = []

    for line in text_input:
        lines.append(line.rstrip())

    lines.sort()
    return lines

def part_1():
    lines = parse_text_input()
    guard_sleep_sched = defaultdict(list)

    guard = None
    asleep = None

    for line in lines:
        minute = get_minute(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = minute
        elif 'wakes up' in line:
            for i in range(asleep, minute):
                guard_sleep_sched[guard].append(i)


    worst_guard = None
    most_slept = 0

    for guard, minutes_slept in guard_sleep_sched.items():
        if len(minutes_slept) > most_slept:
            most_slept = len(minutes_slept)
            worst_guard = guard


    minute_count = {}
    for minute in guard_sleep_sched[worst_guard]:
        minute_count[minute] = minute_count.get(minute, 0) + 1


    most_slept_minute = None
    most_slept_count = 0

    for minute, count in minute_count.items():
        if count > most_slept_count:
            most_slept_minute = minute
            most_slept_count = count

    return most_slept_minute * worst_guard


def part_2():
    lines = parse_text_input()
    guard_sleep_sched = defaultdict(int)

    guard = None
    asleep = None

    for line in lines:
        minute = get_minute(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = minute
        elif 'wakes up' in line:
            for i in range(asleep, minute):
                guard_sleep_sched[(guard, i)] += 1

    guard_id, sleep_minute = get_most_frequent(guard_sleep_sched)
    return guard_id * sleep_minute



