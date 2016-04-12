#
# check referer tool
#
#!/usr/bin/python

import urllib2
import sys

opener=urllib2.build_opener()
ref = open('/Users/saeoshi/ref.txt')
line = ref.readlines()
url = "http://hogehoge.com/01/fe/e9/j/o064004801317141126182.jpg"

for x in line :
        try:
            y =  x.strip("\n")
            opener.addheaders=[('Referer','http://%s' % y)]
            print opener.addheaders
            f = opener.open(url)

        except IOError:
            print 'An match Referer' , y
