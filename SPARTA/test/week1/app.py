from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import json_util

client = MongoClient('mongodb+srv://sparta:test@cluster0.mgovdoc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1
    doc = {
        'num':count,  #버킷 등록 시, db에서 특정 버킷을 찾기 위해 'num' 이라는 고유 값 부여
        'bucket' :bucket_receive,
        'done' : 0   #'done' key값을 추가 해 각 버킷의 완료 상태 구분(0 = 미완료, 1 = 완료)
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'result': all_buckets})


@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    done_receive = request.form['done_give']
    db.bucket.update_one({'done': int(done_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '완료🎉'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
    
    
    
    