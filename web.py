#!/usr/bin/python
#coding:utf-8

from flask import Flask, request
from flask import jsonify
import random
import random_resource

str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
task_name_list = ['任务' + str(i) for i in range(1, 50)]
img_list = ['http://img0.imgtn.bdimg.com/it/u=2995055718,2800286614&fm=23&gp=0.jpg',
            'http://www.qqxoo.com/uploads/allimg/170504/13595245N-22.jpg',
            'http://img3.duitang.com/uploads/item/201503/11/20150311125532_BKrdG.jpeg',
            'http://www.qqxoo.com/uploads/allimg/170504/14002KQ4-1.jpg',
            'http://www.qqxoo.com/uploads/allimg/170504/1359524093-17.jpg',]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '雷猴!'

@app.route('/challenge/chinese/sign/user_sign_flag.json')
def sign_flag():
    return jsonify({
        'msgCode': 301,
        'data': {
            'sign_flag': '0',
            'sign_count': '1212',
            'current_time': '0000000',
            'star_total': '8',
            'ucoin': '7',
            'kit': '1',
        }
    })

@app.route('/challenge/chinese/sign/awards.json')
def sign_award():
    return jsonify({
        'msgCode': 301,
        'data': [
            {'date': '2017-05-25',
             'award': {
                 'id': '1',
                 'ucoin': '2',
                 'kit': '1',
             }
             },
            {'date': '2017-05-29',
             'award': {
                 'id': '2',
                 'ucoin': '3',
                 'kit': '3',
             }
             }
        ]
    })

@app.route('/challenge/chinese/sign/sign_datas.json')
def sign_date():
    return jsonify({
        'msgCode': 301,
        'data': {
            'sign_dates': ['2017-05-02', '2017-05-03', '2017-05-10'],
            'get_award_dates': ['2017-05-05'],
            'day_poems': [{
                'day': '2017-05-21',
                'peom': {}
            }]
        }
    })

@app.route('/challenge/chinese/sign/signed.json')
def sign_signed():
    return jsonify({
        'msgCode': 301
    })

@app.route('/challenge/chinese/sign/get_award.json')
def sign_get_award():
    return jsonify({
        'msgCode': 301
    })
@app.route('/challenge/chinese/question/tollgate_count.json')
def tollgate_count():
    return jsonify({
        'msgCode': 301,
        'data': {
            'level_total': 100,
            'user_level': 10,
        }
    })

@app.route('/challenge/chinese/question/passedLevel.json')
def passed_level():
    return jsonify({
        'msgCode': 301,
        'data': [
            {'level': 1, 'star': 2},
            {'level': 2, 'star': 1},
            {'level': 3, 'star': 3},
            {'level': 4, 'star': 2},
            {'level': 5, 'star': 3},
            {'level': 6, 'star': 2},
            {'level': 7, 'star': 2},
            {'level': 8, 'star': 0},
            {'level': 9, 'star': 2},
            {'level': 10, 'star': 2},
            {'level': 11, 'star': 3},
            {'level': 12, 'star': 2},
            {'level': 13, 'star': 2},
            {'level': 14, 'star': 1},
            {'level': 15, 'star': 2},
            {'level': 16, 'star': 3},
            {'level': 17, 'star': 2},
            {'level': 18, 'star': 2},
        ]
    })

# 每日任务
@app.route('/challenge/chinese/daily_task/tasks.json')
def daily_task():
    task_id = request.args.get('task_id')
    data = {}
    if task_id is None:
        data = random_dialy_tasks(3)
    else:
        data = {
            'ucoin': str(random.randint(1, 10)),
            'kit': str(random.randint(1, 5)),
        }
    return success_json(data)

def random_dialy_tasks(count):
    result = []
    for i in range(0, count):
        task = {
            'task_id': random.randint(1, 100),
            'task_name': random.choice(task_name_list),
            'task_content': {'full_start_count': str(random.randint(1, 5)), 'sign': str(random.randint(1, 3)),
                      'tollgate_clear_count': str(random.randint(1, 5)), 'prop_times': str(random.randint(1, 11)),
                      'ucoin_cost': str(random.randint(1, 21))},
            'award': {'id': str(random.randint(1, 111)), 'ucoin': str(random.randint(1, 11)),
                             'kit': str(random.randint(1, 5))},
        }
        for key in random.sample(task['task_content'].keys(), 4):
            task['task_content'][key] = '-1'
        result.append(task)
    return result

# 排行榜
@app.route('/challenge/chinese/rank/grade_rank.json')
def grade_rank():
    grade = request.args.get('grade')
    print(request.args)
    if grade:
        return jsonify({
            'msgCode': 301,
            'data': random_grade_rank(5),
        })
    else:
        return jsonify({
            'msgCode': 223,
            'data': {'reason': '无效的参数'}
        })

@app.route('/challenge/chinese/rank/rank.json')
def top_rank():
    data = random_grade_rank(5)
    return success_json(data)

@app.route('/challenge/chinese/rank/my_rank.json')
def my_rank():
    data = [
        {'type': '1', 'rank': 311, 'head_url': random.choice(img_list), 'name': random.choice(random_resource.names), 'star_count': '55', 'sign_count': '21', 'tollgate_count': '17'},
        {'type': '2', 'rank': 621, 'head_url': random.choice(img_list), 'name': random.choice(random_resource.names), 'star_count': '55', 'sign_count': '21', 'tollgate_count': '17'},
        ]
    return success_json(data)

def random_grade_rank(count):
    random_grade_ranks = []
    for i in range(0, count):
        random_rank = {'rank': str(i + 1), 'head_url': random.choice(img_list), 'name': random.choice(random_resource.names), 'star_count': str(random.randint(1, 1000)), 'sign_count': str(random.randint(1, 1000)), 'tollgate_count': str(random.randint(1, 200))}
        random_grade_ranks.append(random_rank)
    return random_grade_ranks

def success_json(data):
    return jsonify({
        'msgCode': 301,
        'data': data
    })

def error_para_json():
    return jsonify({
        'msgCode': 223,
        'data': {}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
