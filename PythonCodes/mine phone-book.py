def give_number(name,dicto):
    for key in dicto:
        if key==name:
            print(str(key)+'='+str(dicto[key]))
            break
    else :
            print("Not found.")

number_of_enteries=int(input())

temp_phone_book=[]

for count in range(number_of_enteries):
    temp_phone_book.append(input())

phone_book={}

for count in range(number_of_enteries):
    phone_book[temp_phone_book[count][:temp_phone_book[count].index(' ')]] = temp_phone_book[count][temp_phone_book[count].index(' ')+1:]

query_list=[]

while(5<6):
    entry=input()
    query_list.append(entry)
    if len(entry)==0:
        break

for count in range(len(query_list)-1):
    give_number(query_list[count],phone_book)
