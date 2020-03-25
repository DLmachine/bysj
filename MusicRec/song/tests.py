# import pymongo
 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["NetCloudMusic"]
# mycol = mydb["PlaylistInfo"]

# data=mycol.find_one({"playlist_id":'3115062936'})
# print(data)

for i in range(3):
	data=input()
	lis=[i for i in data]
	print(lis)