print('ENTER total numbers you want to register')
num = int(input())                                #number of enteries
print('ENTER your name then space then number you want to register')

phone_book = {}                                   #empty phone book dictionary

for count in range(0, num):
    print('your ',count+1,' registery')
    entry = str(input()).split(" ")
    name = entry[0]
    number = int(entry[1])
    phone_book[name] = number

for count in range(0, num):
    print('you want to search for ?')
    name = str(input())
    if name in phone_book:
        number = phone_book[name]
        print(name + "=" + str(number))
    else:
        print("Not found")
