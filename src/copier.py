import os
import shutil

#Recursively explore the src dir and return a list of directories and files to copy. The list of dirs will not include the src dir while the files will.
def explore_src(src, dest, cp):
    if os.path.exists(src) == False:
        print(f"Filepath does not exist: {src}")
        return
    
    if os.path.exists(dest) == True:
        shutil.rmtree(dest)
        os.mkdir(dest)
    
    for dir in os.listdir(src):
        if os.path.isfile(src + "/" + dir):
            shutil.copy(src +'/' + dir, dest +'/' + dir)
        else:
            os.mkdir(dest + "/" + dir)
            explore_src(src + "/" + dir, dest + "/" + dir, cp)
    
    return

    
