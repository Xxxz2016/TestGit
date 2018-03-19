# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 11:21
# @Author  : xxxz
# @File    : test3.py
# @Software: PyCharm

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return 'hello'

@app.route('/profile/<int:uid>/',methods=['GET','POST'])
def profile(uid):
    return render_template('profile.html',uid=uid)

if __name__ == '__main__':
    app.run(debug=True)