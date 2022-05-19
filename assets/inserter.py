import os


for files in os.walk("."):
    for folder in files:
        for fileTS in folder:
            if ".ts" in fileTS and ".tsx" not in fileTS and ".map" not in fileTS:

                #print (os.path.join((""), (files[0] + "\\"), fileTS))
                file = open(os.path.join((""), (files[0] + "\\"), fileTS), "r")
                fileData = "//NAME: Jack Hayes\n//ID: 1545068\n" 
                for fileOut in file:
                   fileData += fileOut
                fileWriter = open(os.path.join((""), (files[0] + "\\"), fileTS), "w")
                fileWriter.write(fileData)


