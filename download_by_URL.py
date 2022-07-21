from urllib.request import urlretrieve

URL = ''
location = ""
name = ""
formate = 0

print("Enter URL : ")
URL=input()
print("Enter Location ( path to folder ) : ")
location =input()
print("Enter Name for the file : ")
name =input()
print("Enter '1' for Image (jpg) \n\t '2' for video (mp4) \n\t : ")
formate = input()
if (formate==1):
    urlretrieve(URL, location +"\\"+name+"_urld.jpg" )
else:
    urlretrieve(URL, location + "\\" + name + "_urld.mp4")