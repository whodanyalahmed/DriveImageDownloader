import tkinter as tk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import pandas as pd
import csv
import time
from selenium import webdriver
import time
from openpyxl import *
import time
import requests
from bs4 import BeautifulSoup
import random
import urllib.request
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import load_workbook
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from selenium.webdriver.common.action_chains import ActionChains
import re
import pandas as pd
import time
from openpyxl import *
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import numpy as np


column = 2
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
driver = webdriver.Chrome("I://clients//chromedriver.exe", options=options)
driver.maximize_window()
counter = 1
driver.get('https://developersales.co/normanton-park/price-list?fbclid=IwAR1hEuR6OQ46sac9-sjBzdDd_sSEIgZqyEpVxYlIGjtXi_I6jG_QOPCQtLo')
driver.implicitly_wait(10)
driver.find_element_by_xpath(
    '//html/body/div[3]/div/div/div[1]/button').click()
time.sleep(2)

while True:
    try:
        element = driver.find_element_by_xpath(
            # '//html/body/div').click()
            # /html/body/div/div[2]/div[2]/div[2]
            "//html/body/div/div[2]/div[2]/div[2]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("window.scrollTo(0, 500);")
        print('scrolling...')
    except Exception as e:
        print("error occured - " + str(e))
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
