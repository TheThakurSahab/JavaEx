items = [34,66,23,43,12,98,56,33,63]
def find_items(item, itemList):
    for i in range(0, len(items)):
        if item == itemList[i]:
            return i
    return None

print(find_items(56, items))
print(find_items(200, items))