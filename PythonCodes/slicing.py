data='XBOX 360 | 150 | NEW'
product=data[:data.index('|')]
print(product)

new_data=data[data.index('|')+1:]
price=new_data[:new_data.index('|')]
print(price)

condition=new_data[new_data.index('|')+1:]
print(condition)
