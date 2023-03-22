with open("file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("i am fine")
myfile.close()    