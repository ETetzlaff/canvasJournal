#!/usr/bin/python
import requests
import json
import sys


cak = open("Canvas/apikey", "r")
canvasAPIkey = cak.read(100)
cak.close()
if canvasAPIkey[-1] == '\n': canvasAPIkey = canvasAPIkey[:-1]

headers = dict()
headers['Authorization'] = "Bearer " + canvasAPIkey


url = 'https://weber.instructure.com/api/v1/courses'
print (url)
#print (headers)

r = requests.get(url, headers=headers)
print ('Status Code from group request:', r.status_code)

assn = json.loads(r.text)

for item in assn:
    print item['course_code'] + ':' + str(item['id'])

#print (assn)

for i in assn:
  if 'use_rubric_for_grading' in i:
    print ('<' + str(i['name']) + '> use_rubric_for_grading: ' + str(i['use_rubric_for_grading']))
