# we will create dictionary

vehicles = {'dream': 'honda 250T',
            'roadster':'BMW r100',
            'er5':'kawasaki',
            'cannan':'bombarder',
            'virago':'yamaha xt650',
            'jimmy':'sizuki jimmny 1.5',
            'fiesta':'ford fiesta 1.4'}

my_car = vehicles['fiesta']
print(my_car)

commuter=vehicles['virago']
print(commuter)

dream_car = vehicles['dream']
print(dream_car)


#using the get method if we will use get method it will return none if key does not exist

learner = vehicles.get('er5')
print(learner)  #it returns the value

# to get the none value

learner2 = vehicles.get('cool')
print(learner2)