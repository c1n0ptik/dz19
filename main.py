from vocabulary import add_item, delete_item, change_item, find_item
from vocabulary import voc

print(voc())
print('')

while True:
    options = int(input("1 - add, 2 - delete, 3 - find, 4 - change, 5 - stop: "))

    if options == 1:
        add_item()

    elif options == 2:
        delete_item()

    elif options == 3:
        find_item()

    elif options == 4:
        change_item()

    elif options == 5:
        break
