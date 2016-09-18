from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
#from builtins import *
from lxml import html
import requests
from scipy import stats
import numpy as np
import json
import matplotlib.pyplot as plt

def getData():

	page = requests.get('https://vr-arthritis-5ddd7.firebaseio.com/.json')
	tree = html.fromstring(page.content)

	print(page.content)



