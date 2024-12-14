unsortedList1 = []
unsortedList2 = []
with open('input.txt') as f:
    for line in f:
        unsortedList1.append(int(line.split()[0]))
        unsortedList2.append(int(line.split()[1]))
f.close()

sortedList1 = sorted(unsortedList1)
sortedList2 = sorted(unsortedList2)

totalDistance = 0
similarityScore = 0
for x in range(len(sortedList1)):
    totalDistance = totalDistance + abs(sortedList1[x]-sortedList2[x])
    totalFound = 0
    for y in range(len(sortedList1)):
        if sortedList1[x] == sortedList2[y]:
            totalFound = totalFound + 1
    similarityScore = totalFound * sortedList1[x] + similarityScore



print(totalDistance)
print(similarityScore)
    