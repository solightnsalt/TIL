from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mgovdoc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# all_users = list(db.users.find({},{'_id':False}))
# # {'_id':False} 이거 안쓰면 id값 붙어나옴

# for i in all_users:
#     print(i['name'], '(', i['age'],')')

db.users.update_one({'name':'영수'},{'$set':{'age':50}})
db.users.delete_one({'name':'영희'})

