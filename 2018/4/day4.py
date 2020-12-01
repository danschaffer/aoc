import datetime
results = {}

def sort_lines():
    data = {}
    for line in open('./day4-input.txt').read().split('\n'):
        fields = line.split(' ')
        year = int(fields[0][1:5])
        month = int(fields[0][6:8])
        day = int(fields[0][9:11])
        hour = int(fields[1][0:2])
        minute = int(fields[1][3:5])
        index = datetime.datetime(year, month, day, hour, minute).toordinal()
        print(f"{index} {line}")
        data[index] = line
    sorted_lines = []
    for dt in sorted(data.keys()):
        sorted_lines += [data[dt]]
    open('day4-input-sorted.txt', 'w').write("\n".join(sorted_lines))

def process1():
    ct = 0
    start = -1

    for line in open('./day4-input-sorted.txt').read().split('\n'):
        tokens = line.split(' ')
        if len(tokens)<4:
            continue
        minute = int(tokens[2][3:5])
        action = tokens[3]

        if action == "Guard":
            guard = int(tokens[4][1:])
        if guard not in results:
            results[guard] = {'schedule': [0 for n in range(60)]}
        if action == "falls" and start == -1:
            start = minute
        if action == "wakes" and start > -1:
            for n in range(start, minute):
                results[guard]['schedule'][n] += 1
            start = -1
    for key in results.keys():
        results[key]['max'] = max(results[key]['schedule'])
        results[key]['sum'] = sum(results[key]['schedule'])
    data = sorted(results.items(), key=lambda x: x[1]['sum'], reverse=True)
    index = results[data[0][0]]['schedule'].index(data[0][1]['max'])
    print(data[0])
    print(f"answer: {data[0][0] * index}")

def process2():
    ct = 0
    start = -1

    for line in open('./day4-input-sorted.txt').read().split('\n'):
        tokens = line.split(' ')
        if len(tokens)<4:
            continue
        minute = int(tokens[2][3:5])
        action = tokens[3]

        if action == "Guard":
            guard = int(tokens[4][1:])
        if guard not in results:
            results[guard] = {'schedule': [0 for n in range(60)]}
        if action == "falls" and start == -1:
            start = minute
        if action == "wakes" and start > -1:
            for n in range(start, minute):
                results[guard]['schedule'][n] += 1
            start = -1
    for key in results.keys():
        results[key]['max'] = max(results[key]['schedule'])
        results[key]['sum'] = sum(results[key]['schedule'])
    data = sorted(results.items(), key=lambda x: x[1]['max'], reverse=True)
    index = results[data[0][0]]['schedule'].index(data[0][1]['max'])
    print(data[0])
    print(f"answer: {data[0][0] * index}")

#sort_lines()
#process1()
process2()
