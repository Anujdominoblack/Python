vehicles = {'dream' : 'Hondaa 250T',
             'roadster' : 'BMW R1100',
             'er5' : 'kawasaki er5',
              'cannan' : 'bombardier cannan',
              'viragao' : 'yamaha xv250',
               'ten' : 'yamcha xt650' ,
               'jimmy' : 'suzuki jimmny 1.5',
               'fiesta' : 'ford fiesta 1.4'}


for key in vehicles:  # we will iterate over vehicles and only keys will be presented
    print(key)

# now to get value along with keys

for key1 in vehicles:
    print(key1 ,vehicles[key1])
