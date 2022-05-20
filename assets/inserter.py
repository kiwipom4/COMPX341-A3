import os
from tkinter import filedialog

for files in os.walk("."):
    for folder in files:
        for fileTS in folder:
            if "node_modules" not in  files[0]:
                if ".ts" in fileTS and ".tsx" not in fileTS and ".map" not in fileTS and os.path.isfile(os.path.join((""), (files[0] + "\\"), fileTS)):
                        print (os.path.join((""), (files[0] + "\\"), fileTS))
                        file = open(os.path.join((""), (files[0] + "\\"), fileTS), "r")
                        fileData = "//NAME: Jack Hayes\n//ID: 1545068\n" 
                        while file:
                            fileString = file.readline()
                            if fileString == "":
                                break
                            fileData += fileString 
                        fileWriter = open(os.path.join((""), (files[0] + "\\"), fileTS), "w")
                        fileWriter.write(fileData)
                        fileWriter.close()

                



