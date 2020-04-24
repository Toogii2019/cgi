#!/usr/bin/env python
import cgi
import cgitb
from functools import reduce

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')
try:
    total = sum(map(int, operands))
    body = "your total is: {}".format(total)
except (ValueError, TypeError):
    print(operands)
    body = "Unable to calculate a sum: Please provide integer as operands"

print("Content-type: text/plain")
print()
print(body)
