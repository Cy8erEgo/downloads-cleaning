#!/usr/bin/python3 

import zipfile
import shutil 
import os

path = '/Users/Anon/Downloads'
os.chdir(path)

for filename in os.listdir():
    if filename.endswith('.torrent'): 
        os.unlink(filename) 
        print('%s is deleted' % filename)
    elif filename.endswith('.dmg'):
        os.unlink(filename)
        print('%s is deleted' % filename)
    elif filename.endswith('.zip'):
        try:
            zipf = zipfile.ZipFile(filename)
            zipf.extractall(filename[:-4])
            os.unlink(filename)
            print('%s was extracted' % filename)
        except zipfile.BadZipFile:
            pass
