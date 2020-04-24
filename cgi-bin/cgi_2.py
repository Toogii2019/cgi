#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import os
import datetime


default = "No Value Present"
script = os.environ.get('SCRIPT_NAME', __name__)
month = datetime.datetime.now().strftime('%B')
year = datetime.datetime.now().year
date = datetime.datetime.now().date
client_ip = os.environ.get('REMOTE_ADDR', 'eeee')

print("Content-Type: text/html")
print("")

body = """<html>
<head>
<title>Lab 1 - CGI experiments</title>
</head>
<body>
<p>Hey there, this page has been generated by {software}, running {script}</p>
<p>Today is {month} {date}, {year}.</p>
<p>This page was requested by IP Address {client_ip}</p>
</body>
</html>""".format(
    software=os.environ.get('SERVER_SOFTWARE', default),
    script=script,
    month=month,
    date=date,
    year=year,
    client_ip=client_ip
)
print(body)
