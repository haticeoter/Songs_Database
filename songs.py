import sqlite3

class Song():
    def __init__(self, song_name, singer, album, production_company, long):
        self.song_name = song_name
        self.singer = singer
        self.album = album
        self.production_company = production_company
        self.long = long

    def __str__(self):
        return "Name of the Song: {}\nSinger: {}\nAlbum: {}\nProduction Company: {}\nLong of the Song: {}".format(self.song_name, self.singer,self.album, self.production_company, self.long)


class Songs():
    def __init__(self):
        self.get_connect()

    def get_connect(self):
        self.connect = sqlite3.connect("songs.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS songs (Song_Name TEXT, Singer TEXT, Album TEXT, Production_Company TEXT, Song_Long INT)")
        self.connect.commit()


    def show_songs(self):
        self.cursor.execute("Select * From songs")
        songs = self.cursor.fetchall()
        if len(songs) == 0:
            print("There is no song yet.")
        else:
            for i in songs:
                song = Song(i[0],i[1],i[2],i[3],i[4])
                print(song)

    def add_songs(self, song):
        self.cursor.execute("INSERT INTO songs VALUES(?,?,?,?,?)",(song.song_name, song.singer, song.album, song.production_company, song.long))
        self.connect.commit()

    def delete_song(self,song):
        self.cursor.execute("Delete From songs where song_name = ?",(song,))
        self.connect.commit()

    def total_song_long(self):
        self.cursor.execute("SELECT Song_Long FROM songs")
        songs = self.cursor.fetchall()
        song_long = 0
        for song in songs:
            song_long += int(song[0])
        print(song_long)



