#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post
from flask_slack import Slack

slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

@post('/schedule')

@slack.command('your_command', token='hMj5SZXTCJJUqO4FnUoE1Jgd', team_id='T0001', methods=['POST'])
def your_method(**kwargs):
    text = kwargs.get('text')
    return slack.response(text)


def schedule():
	scheduleURL = 'https://docs.google.com/spreadsheets/d/1GD__Yyx8GZ6vsqo7E4pxqoitooOr5LgLomVAL8gBFH8/edit'
	return slack.response(scheduleURL)

if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
	run(host='0.0.0.0', port=port)
