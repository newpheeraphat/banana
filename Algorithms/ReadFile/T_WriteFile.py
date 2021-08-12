import os
os.system('mkdir ~/Desktop/cs159')
f = os.path.expanduser("~/Desktop/cs159/testfile.txt")
file = open(f, "w")
file.close()
