## Write a Python program to print all positive numbers in a range.
for i in range(2):
    Arr = list(map(int, input("Input: list "+str(i + 1)+" =").strip("[]").split(",")))
    l = []
    for i in Arr:
        if i > 0:
            l.append(i)
    print("Output: "+str(l))
    
    
## Desired output would be like this sir/madam

##Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
##Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
