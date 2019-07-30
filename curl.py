# -*- coding: utf-8 -*-
# 
# 2019.07.30 박충렬 (crpark@gamevilcom2us.com, yeoli128@gmail.com)
#
# curl-with-resolved-ipaddr for Promotion Server Developers
#

import pycurl
import json
from urllib.parse import urlencode
from io import BytesIO

# Sample: https://jsonplaceholder.typicode.com/posts

protocol		= 'http://'
targetDomain	= 'jsonplaceholder.typicode.com'
uri				= '/posts'
destIP			= '172.64.129.28'
destPort		= '443'


data = u"""
{
    "hello": "world"
}
"""



buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, targetDomain + uri)
c.setopt(c.POST, True)
c.setopt(c.SSL_VERIFYPEER, False)
c.setopt(pycurl.HTTPHEADER, [
	'Content-type: Application/json;charset=utf-8',
	'Authorization: Basic YmVhdDpiZWF0X2FwcDswZWU4YTg0NjhmMmVjYjUzMzY2ZGM0MTA4NzUzZxxxxxxx'
])
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.RESOLVE, [targetDomain + ':' + destPort + ':' + destIP])
#data = json.dumps(data)
c.setopt(c.POSTFIELDS, data.encode('utf8'))

c.perform()
print('- Status: %d' % c.getinfo(c.RESPONSE_CODE))
print('- Total Time: %f' % c.getinfo(c.TOTAL_TIME))
print('- Primary IP: %s Port: %d' % (c.getinfo(c.PRIMARY_IP), c.getinfo(c.PRIMARY_PORT)))
c.close()

body = buffer.getvalue()
print('- Result Body')
print(body.decode('cp949')) # ko

