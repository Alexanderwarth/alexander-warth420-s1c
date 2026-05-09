




def findmax(numlist):

    largest = numlist[0]
    for num in numlist:
        if num > largest:
            largest = num
    return largest

myMax = findmax([5, 2, 121, 6, 2])
print("max: ", myMax)