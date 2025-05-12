#file
f=open("newfile.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

k=open("ayush.txt","w")
k.write("I AM PYTHONE DEVELOPER")
k.close()

k=open("ayush.txt","r")
print(k.read())
k.close()

f=open("newfile.txt","a")
f.write("\n I like python ---- HURRAH!!!")
f.close()

f=open("newfile.txt","r")
print(f.read())
f.close()