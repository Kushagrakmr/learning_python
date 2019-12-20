import pdb

first = "First"
second = "Second"

pdb.set_trace()

result = first + second
third = "Third"

pdb.set_trace()

result += third
print(result)
