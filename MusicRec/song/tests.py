from MusicRec.MusicRec.settings import SongInfo

data=SongInfo.find_one({'song_id':'1427664555'})
print(data)