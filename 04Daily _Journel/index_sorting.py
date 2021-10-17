
items = ["red", "blue", "pink", "purple", "orange"]

for item in items:
    print("the item is {}" .format(item))

# other way using indexing to print the items. and also here we r unpacking a tuple.
for (idx, item) in enumerate(items):
    print(" {} {}" .format(idx+1, item)) #add 1 in index for correct index numbering.



