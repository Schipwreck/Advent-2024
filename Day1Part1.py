import numpy as np
groups =[]
with open('Day1.txt', 'r') as file:
    for line in file:
        lists = line.strip().split()

        if len(lists) == 2:
            list1 = int(lists[0])
            list2 = int(lists[1])
            groups.append((list1,list2))

        
firstNum = [group[0] for group in groups]
secondNum = [group[1] for group in groups]

firstNum.sort()
secondNum.sort()



Total = 0
for x in range(len(firstNum)):
    difference = abs(firstNum[x] - secondNum[x])
    
    Total = Total + difference
    

Similarity = 0
for num in firstNum:
    repeatNum = secondNum.count(num)
    Similarity += num * repeatNum
    print(Similarity)
    
