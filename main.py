import os
from selenium import webdriver
import random

interface = 'wlp58s0'
url       = ''
name      = ''
os.system(f'sudo ifconfig {interface} down')
os.system(f'sudo macchanger -r {interface}')
os.system(f'sudo ifconfig {interface} up')

d = webdriver.Chrome()
d.get(url)

num   = random.randint(0, 99999)
email = f'test{num}@gmail.com'

d.find_element_by_name('email').send_keys(email)
d.find_element_by_name('name').send_keys(name)

# d.find_elements_by_class_name('reject')[0].click()
d.close()