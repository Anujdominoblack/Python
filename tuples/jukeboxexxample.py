albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
SONG_LIST=3
SONG_TITLE_INDEX=1
while True:
    print("please choose your album")
    for index,(title,artist,year,songs) in enumerate(albums):
        print(index+1,title)
    choice=int(input())
    if 1<=choice<=5:
        song_list=albums[choice-1][SONG_LIST]

    else:
        break;
    print("choose your song")
    for index,(track,song) in enumerate(song_list):
        print("{} :{}".format(index+1,song))
    song_choice=int(input())
    if 1<=song_choice<=len(song_list):
        title=song_list[song_choice-1][SONG_TITLE_INDEX]
    else:
        break
    print("playing {}".format(title))

