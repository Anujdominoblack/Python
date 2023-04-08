metallica="ride the lighting","metallica",1980
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
#another way
metallica2=("ride the lightning","meatlllica",1980)
print(metallica2)
print(metallica2[0])
print(metallica2[1])
print(metallica2[2])
#metallica[0]="rude"
print(metallica[0]) #this will throw an error as lists are immutable
#list() returns a list using the values present in the iterable
metallica3=list(metallica)
print(metallica3)