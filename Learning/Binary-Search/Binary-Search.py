# Time complexity: O(log n)
def binarySearch(list, numToFind):
    leftIndex = 0
    rightIndex = len(list)- 1
    midIndex = 0
    
    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        
        if list[midIndex] == numToFind:
            return midIndex
        elif list[midIndex] <= numToFind:
            leftIndex = midIndex + 1
        else:
            rightIndex = midIndex - 1
    
    return -1


# Time complexity: O(n)
# def linearSearch(list, numToFind):
#     for i, num in enumerate(list):
#         if num == numToFind:
#             return i
    
#     return -1


if __name__ == "__main__":
    numberList = [2, 7, 16, 32, 75, 83, 90, 102, 105]
    numToFind = 16
    
    # index = linearSearch(numberList, numToFind)
    index = binarySearch(numberList, numToFind)

    print(f'The number {numToFind} is in the index {index}')
    