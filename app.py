#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post


@post('/schedule')
def schedule():
	scheduleURL = 'https://docs.google.com/spreadsheets/d/1GD__Yyx8GZ6vsqo7E4pxqoitooOr5LgLomVAL8gBFH8/edit'
	return scheduleURL

if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
	run(host='0.0.0.0', port=port)
