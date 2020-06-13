from PIL import Image
import os
import glob
import string

PATH = os.getcwd()

for filepath in glob.iglob("**/*.ppm*", recursive=True):
        im = Image.open(filepath)
        filepath2=filepath[:-4]
        filepath2= ''.join(ch for ch in filepath2)
        filepath2= filepath2+".png"
    
        
        im.save(filepath2)
