#!/usr/bin/env python3

import webbrowser
import time
 
count = 0
while count < 24:
     webbrowser.open('https://www.ysense.com/surveys')
     time.sleep(3600)
     count += 1
