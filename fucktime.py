import os
import random

time = "{].{}"
date = "{}/{}/{}"



while True:
	os.system("time " + time.format(str(random.randint(0, 23)), str(random.randint(0,59))))
	os.system("date " + date.format(str(random.randint(2000, 2077)), str(random.randint(1,12)), str(random.randint(1,29))))
