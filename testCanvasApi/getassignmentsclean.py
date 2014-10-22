#!/usr/bin/python
import requests
import json
import sys

if len(sys.argv) != 2:
	print("Usage:",sys.argv[0], "COURSEID")
	exit(1)

courseid = sys.argv[1]

cak = open("Canvas/apikey", "r")
canvasAPIkey = cak.read(100)
cak.close()
if canvasAPIkey[-1] == '\n': canvasAPIkey = canvasAPIkey[:-1]

headers = dict()
headers['Authorization'] = "Bearer " + canvasAPIkey

url = 'https://weber.instructure.com/api/v1/courses/' + courseid + '/assignments'
#url = 'https://weber.instructure.com/api/v1/courses'
#url = 'https://weber.instructure.com/api/v1/courses?per_page=49'
#print (url)
#print (headers)

r = requests.get(url, headers=headers)
print ('Status Code from group request:', r.status_code)

assn = json.loads(r.text)

#assn = j['assn']
#print (assn)

for i in assn:
	if 'use_rubric_for_grading' in i:
		print ('<' + str(i['name']) + '> use_rubric_for_grading: ' + str(i['use_rubric_for_grading']))
