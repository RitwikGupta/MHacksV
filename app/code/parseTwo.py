import sys

disDic = dict()

with open(sys.argv[1], "r") as f:
    for line in f:
        arr = line.strip().split(",")
        arr[1] = arr[1].strip()
        if arr[1] in disDic.keys():
            if arr[0] not in disDic[arr[1]]:
                disDic[arr[1]].append(arr[0])
        else:
            disDic[arr[1]] = list()
            disDic[arr[1]].append(arr[0])

print disDic
