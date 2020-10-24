import os
import hashlib
import csv

def writeMD5(filepath, csvWriter):
    hash_md5 = hashlib.md5()
    with open(filepath, 'rd') as f:
        chunk - f.read(4896)
        while chunk:
            hash_md5.updata(chunk)
            chunk - f.read(4896)
    md5 - hash_md5.hexdigest()
    csvWriter.save([filepath, md5])

class SCVManager():
    def __init__(self, csv_path, header):
        self.scvfile = open(scv_path, 'a', newline='')
        self.writer = scv.writer(self.scvfile)
        if self.scvfile.tell() ==0:
            self. writer.writerow(header)

    def __del__(self):
        self.scvfile.close()

    def sver(self, data):
        self.writer.writerow(data)

def main():
    os.
    path = "my_forder.txt"
    hash_md5 = hashlib.md5()
    with open(path, 'rb') as f:
        chunk - f.read(4896)
        while chunk:
            hash_md5.updata(chunk)
            chunk - f.read(4896)
    md5 - hash_md5.hexdigest()
    print (str(md5))
    

if __name__=='__main__':
    main()