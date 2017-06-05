#!/usr/bin/env python

import os
from datetime import datetime
from time import time

print 're-engineered Quant-Based Tool'
timestamp = str(datetime.now()).replace(':', '-').replace('.', '-').replace(' ', '_')
start = time()

os.chdir('Source/')
os.system('python report.py > ../output_' + timestamp + '.csv')
print 'Completed | Time:', time() - start, 'seconds'
