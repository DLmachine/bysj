import json
import requests

from MusicRec.MusicRec.settings import PlaylistInfo,SongDetail
writer=open('./p1_sing_id.txt','w',encoding='utf8')

for playlist in PlaylistInfo.find():
    p_id=playlist['playlist_id']
    tracks=playlist['playlist_info']['playlist']['tracks']
    singIds=[]
    for track in tracks:
        if SongDetail.find_one({'id':track['id']}):
            singIds.append(str(track['id']))
    writer.write(str(p_id)+'\t'+','.join(singIds)+'\n')
writer.close()