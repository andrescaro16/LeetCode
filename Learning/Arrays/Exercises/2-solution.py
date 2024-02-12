heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(1, f"The length of the list is: {len(heros)}")

# 2. Add 'black panther' at the end of this list
#heros.insert(len(heros), 'black panther')
heros.append('black panther')
print(2, f"'black panter' was added at the end of the list: {heros}")

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
hulkIndex = heros.index('hulk')
heros.insert(hulkIndex + 1, 'black panther')
print(3, f"The position of 'black panter' was corrected: {heros}")

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# heros = ['doctor strange' if hero in ["hulk", "thor", "captain america"] else hero for hero in heros]
heros[1:3] = ['doctor strange']
print(4, f"'hulk' and 'thor' were replaced by 'doctor strange': {heros}")


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
#print(dir(heros))
heros.sort()
print(5, f"'heros' list was sorted: {heros}")
