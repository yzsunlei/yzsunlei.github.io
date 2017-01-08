#!/usr/bin/env python
# coding=utf-8
# Split up a URL of the form http://www.something.com

url = raw_input('Please enter the URL: ')
domain = url[11:-4]  # start index 11 to -4

print "Domain name: " + domain
