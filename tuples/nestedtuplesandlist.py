albums=[("welcome to my nightmres","alice cooper",1975),
        ("bad comapny","bad company",1980),
        ("night flight","bigile",1960),
        ("more mayhem","emilda may",2011),
        ("ride the lighting","metallica",1999),
        ]


#unpaccking the tuple
for album in albums:

    name,artist,year=album
    print("album {} artist {} year {}".format(name,artist,year))

#another way of unpacking

for name,artist,years in albums:
     print(name,artist,years)