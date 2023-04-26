a = {
    'Hello': 'Bonjour',
    'Dog': 'Chienne',
    'Cat': 'Chatte',
    'Computer': 'Ordinateur'
}


def add_item():
    global voc
    english = input('Which word do u wanna add: ')
    french = input('What is a translation: ')
    a.update({
        english: french
    })
    print(a)


def delete_item():
    global a
    del_item = input('What do u wanna delete: ')
    b = a.__delitem__(del_item)
    print(a)


def find_item():
    global a
    fi_item = input('What do u wanna find: ')
    g = a.get(fi_item)
    print(g)


def change_item():
    global a
    old_item = input('What do u wanna change: ')
    new_item = input('New item: ')
    a[old_item] = new_item
    print(a)
