# Time complexity: O(n^2)
# Space complexity: O(1)
def getIndex(arr, target):
    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if(arr[i] + arr[j] == target):
                result.append(i)
                result.append(j)
                return result
            
    return [-1, -1]



# Tests
arr = [2,7,11,15]
target = 9

print(getIndex(arr, target))
