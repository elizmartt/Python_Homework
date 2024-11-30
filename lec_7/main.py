import os
answer="yes"
while answer.lower()=="yes":

 filename = input("Write the file name that you want to create or access: ")
 command=input("What do you want to do with that file read/write/delete:")
 match command:
    case "read":
        try:
         f=open(filename,"r")
         print(f"the file {filename} contents: ",f.read())
         f.close()
        except FileExistsError:
         print("Sorry the file don't exist,try creating it before reading")
    case "write":
        text=input(f"Write the text you want to write in file {filename}:")
        if os.path.exists(filename):
            f=open(filename,"a")
            f.write(text)
            f.close()
            f=open(filename,"r")
            print(f.read())
        else:
            f=open(filename,"x")
            f.write(text)
            f.close()
            f=open(filename,"r")
            print(f.read())
            f.close()
    case "delete":
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print(f"File do not exist try another one")
 answer = input("Do you want to continue?(yes/no)")