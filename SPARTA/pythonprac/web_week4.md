# 웹 크롤링

soup.select_one('카피 셀렉터')
여러개 가지고 올 때는 select로 가져와서 for문 돌리기
title.text
title['href']

## mongoDB

library dnspython & pymongo 필요

pymongo로 db 연결 
기본코드 
```python
from pymongo import MongoClient
client = MongoClient('여기에 URL 입력')
db = client.dbsparta
```

```python
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
```
 