import sys
from datetime import datetime

args = sys.argv

cat = sys.argv[1]

title = sys.argv[2]

date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

today = str(datetime.today().strftime("%Y-%m-%d"))

template = "---\n\
layout: post\n\
title:  \"" + title+ "\" \n\
date:  " + date + "\n\
categories: " + cat + "\n\
---"

print template
path = '_posts/'
filename = today+'-'+title+'.markdown'
f = open(path+filename,'w')
f.write(template)
f.close()
print "New post template created at " + path + filename+ "."
