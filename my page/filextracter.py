from zipfile import ZipFile

def ext(path):
    file_name = path
    try:
        with ZipFile(file_name, 'r') as zip:
            zip.extractall()
    except:
        print(" some think went rong ")