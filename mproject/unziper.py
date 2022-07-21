from zipfile import ZipFile

def ext(path):
    file_name = path
    expath=""
    for x in file_name:
        if( x == '.'):
            break
        expath+=x
    try:
        with ZipFile(file_name, 'r') as zip:
            zip.extractall(expath)
    except:
        print(" some think went rong ")

path=input("Enter path of ziped file : ")
ext(path)
print("Extraction is Sucesfull ")