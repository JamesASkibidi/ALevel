import random

library_length = 5


def shuffler(library, artits):

    shuffled = []
    for i in library:
        
        
        shuffled.append(i)

    random.shuffle(shuffled)

    count =0

    for i in shuffled:
        count+=1

        tag = "#EXTINF:" + str(count) + ", " + artists[i] + " - " + i
        
        with open("data structures/playlist/queue.m3u" , "a") as f:

            f.write(tag +"\n" +
                library[i] + "\n")



    


    




library = {
    
    'Song 2 ' : '/playlist/library/Song2.mp3',
    'Soul to squeeze' : '/playlist/library/Soul_To_Squeeze.mp3',
    'Johnny B. Goode' : '/playlist/library/Johnny_B_Goode.mp3',
    'Hurt' : '/playlist/library/Hurt.mp3',
    'Tunnel Of Love' : '/playlist/library/Tunel_Of_Love.mp3',
}

artists = {
    'Song 2 ' : 'Blur',
    'Soul to squeeze' : 'Red Hot Chilli Peppers',
    'Johnny B. Goode' : 'Benny Goodman',
    'Hurt' : 'Jonny Cash',
    'Tunnel Of Love' : 'Dire Straits',
}


f = open("data structures/playlist/queue.m3u", "x")

with open("data structures/playlist/queue.m3u" , "a") as f:

    f.write("#EXTM3U"+"\n" + "\n")

shuffler(library, artists)

# shuffled_library = random.shuffle(library)

# print(library)

# print(shuffled_library)



# queue = []
# head = -1
# tail = -1
# count=0

# NowPlaying = None