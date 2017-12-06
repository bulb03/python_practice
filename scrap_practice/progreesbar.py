import time
import sys

toolbar_width = 40
n = 0
# setup toolbar
sys.stdout.write(str(n)+"%/100%")
sys.stdout.flush()
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    n+=1
    sys.stdout.write("-")
    sys.stdout.flush()
	sys.stdout.write(str(n)+"%/100%")
	sys.stdout.flush()

sys.stdout.write("\n")