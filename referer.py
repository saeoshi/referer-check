#
# check referer tool
#
#!/usr/bin/python

import urllib2
import sys

opener=urllib2.build_opener()
ref = open('/Users/saeoshi/ref.txt')
line = ref.readlines()
#url = "http://stat.ameba.jp/user_images/20130905/11/ab-anna06/74/d6/j/o0300040012673355938.jpg"
url = "http://stat.profile.ameba.jp/profile_images/20110928/01/fe/e9/j/o064004801317141126182.jpg"

for x in line :
        try:
            y =  x.strip("\n")
            opener.addheaders=[('Referer','http://%s' % y)]
            print opener.addheaders
            f = opener.open(url)

        except IOError:
            print 'An match Referer' , y
