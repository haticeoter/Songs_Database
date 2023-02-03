from songs import *
print("""***********************************

Welcome to the Songs Program.

Operations;

1. Show the Songs

2. Add a Song

3. Delete a Song

4. Show the Total Long of Songs

Type "E" to exit.
***********************************""")

song = Songs()

while True:
    operation = input("Which operation would you like to do:")

    if (operation == "E"):
        print("Program is terminated.....")
        break
    elif (operation == "1"):
        song.show_songs()
    elif (operation == "2"):
        song_name = input("Song Name:")
        singer = input("Singer:")
        album = input("Album:")
        production_company = input("Production Company:")
        long = input("Long of the Song:")

        new_song = Song(song_name, singer, album, production_company, long)
        song.add_songs(new_song)
        print("Song added")

    elif (operation == "3"):
        name = input("Which song would you like to delete ?")
        song.delete_song(name)
        print("Song deleted")
    elif (operation == "4"):
        song.total_song_long()
    else:
        print("Invalid Operation...")

