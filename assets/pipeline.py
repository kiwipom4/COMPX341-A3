from re import T
import sys
import os
import subprocess

if len(sys.argv) != 2:
    print("No commit message. Usage: 'python pipeline.py [COMMIT MESSAGE]'")
    exit()  
subprocess.run('npm install', shell=True)
subprocess.run('npm run build > output.txt', shell=True)
file = open("output.txt", "r")
for line in file:
    if line == "Failed to compile.\n":
        print("ERROR HAS BEEN FOUND")
        exit()
#subprocess.run('npm run start', shell=True)
subprocess.run('cd ../', shell=True)
subprocess.run('git add -u', shell=True)
commitString = 'git commit -m ', sys.argv[1]
subprocess.run(["git", "commit", "-m", sys.argv[1]], shell=True)
subprocess.run('git push', shell=True)


    