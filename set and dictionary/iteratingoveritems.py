vehicles = {
          'dream' : 'honda 250t' ,
          'roadster' : 'BMW r1100',
          'er5' : 'kawasaki er5',
          'cannan' : 'bombardier ',
          'virago ' : 'yamaha xv250',
          'tenn' : 'yamaha xt500',
          'jimmny' : 'suzuki jimmny 1.5',
          'fiesta' : 'ford fiesta 1.4'
}

for key,value in vehicles.items():  # it returns a tuple and we are doing a tuple unpacking  it is similar to enumerate
    print(key,value,sep=" ,")   #first assigned value gives key and second returns the value