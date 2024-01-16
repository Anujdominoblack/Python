watches = {
        '1':'patek phillips',
        '2' : 'tissot',
        '3' : 'audemars piguet',
         '4' : 'rolex '
}


for key in watches:  # for itertaing over a list of elements
    print(key,watches[key],sep=" ,")

# now we will change value and we will do it by using key positon

watches['2'] = 'omega'

for key in watches:
    print(key,watches[key],sep=" ,")