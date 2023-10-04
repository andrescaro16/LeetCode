def anyFunc(arr, num):
    return True


# -------------------- TESTS ----------------------
test = []

# num is in the middle
test.append({
    'input': {
        'arr': [1, 3, 5, 3, 8],
        'num': 5
    },
    'output': 2
})

# num is at the beginning
test.append({
    'input': {
        'arr': [2, 3, 5, 3, 8],
        'num': 2
    },
    'output': 0
})

# num is duplicated
test.append({
    'input': {
        'arr': [2, 3, 5, 5, 5, 3, 8],
        'num': 5
    },
    'output': 2
})


print(test)
result = anyFunc(test[0]['input']['arr'], test[0]['input']['num'])