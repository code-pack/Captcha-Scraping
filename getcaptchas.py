"""
Basically we want an unlimited supply of captchas so keep reloading a webpage with captchas and saving the captcha.

use: python getcaptchas.py 0 10000   <-- start and end indexes

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import math
import os
import urllib

browser = webdriver.Firefox()
fout=open('captchaurls.txt','w')
for i in range(int(sys.argv[1]),int(sys.argv[2])) :
	#try :
	print i
	browser.get('https://www.wowhead.com/account=signup') # sorry wowhead.com
	#time.sleep(3)

	# get captcha image and save it to local directory
	imageurl = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "recaptcha_challenge_image"))).get_attribute('src')
	urllib.urlretrieve(imageurl, str(i)+".jpg")

		#fout.write( image.get_attribute('src')+'\n' )
	#except :
	#	print 'Error'