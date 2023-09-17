#!/usr/bin/python3

# Number = '2,147,483,647'
Number = '20'
Number = int(Number.replace(",",""))
# print(Number)


print("binary of Number = ", bin(Number)[2:])
def solution():
    count = 0
    largest = 0
    start = 0
    end = 1
    N = list(bin(Number)[2:])
    print("N = ", N)
    for end in range(len(N)):
        if N[start] == '1':
            if N[end] == '1':
                print("::", end, N[end])
                start = end
            else:
                count = end - start
            if largest < count and N[end] == '1':
                    largest = count
    print("largest = ", largest)

solution()








