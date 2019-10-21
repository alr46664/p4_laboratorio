#!/usr/bin/python
import httplib
import sys
import re

if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print 'USAGE: http_client.py PORTA RECURSO'
    sys.exit(1)

port = int(sys.argv[1])
site = sys.argv[2]

site = site.split('://')
if len (site) < 2:
    site = site[0]
else:
    site = site[1]
site = site.split('/')
conn = httplib.HTTPConnection(site[0], port)    
conn.request("GET", '/' + '/'.join(site[1:]))
r1 = conn.getresponse()
print 'HTTP GET', '/'.join(site)
print r1.status, r1.reason
data1 = re.sub(r'[\n\t]', '', r1.read())
print data1[:100],'\n'
conn.close()