file=open("r1.txt","w")
print("hi")
file.close()
file=open("r1.txt","r")
print(file.read())
file.close()
file=open("r1.txt","w")
file.write("vandana")
file.close()
file=open("r1.txt","a")
file.write("welcome")
file.close()