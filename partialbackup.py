import sys
import os 
import datetime
import shutil
import hashlib
import filecmp

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def ProcessFile(src_start_path, dst_start_path, partial_path, filename):
    src_file = os.path.join(src_start_path, partial_path, filename)
    dst_file = os.path.join(dst_start_path, partial_path, filename)
    print ("SRC FILE: " + src_file)
    print ("DST FILE: " + dst_file)

    if not os.path.isfile(dst_file):
        shutil.copy2(src_file,dst_file)
    else:
        #src_time= os.path.getmtime(src_file)
        #dst_time= os.path.getmtime(dst_file)
        #if (src_time > dst_file):
        # shutil.copy2(src_file,dst_file)
        #if ((src_time < dst_file) or (src_time == dst_file)):
        #    src_md5 = md5(src_file)
        #    dst_md5 = md5(dst_file)
        #    if (src_md5 != dst_md5):
        #        shutil.copy2(src_file,dst_file)
        if not filecmp.cmp(src_file, dst_file, shallow=False):
            shutil.copy2(src_file,dst_file)

def ProcessFolder(src_start_path, dst_start_path, partial_path):
    src_folder = os.path.join(src_start_path, partial_path)
    dst_folder = os.path.join(dst_start_path, partial_path)
    print ("SRC FOLDER: " + src_folder)
    print ("DST FOLDER: " + dst_folder)

    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    directories = []
    filenames = []
    for element in os.listdir( src_folder ):
        if (os.path.isfile(os.path.join(src_folder, element)) ):
            filenames.append(element)
        elif( os.path.isdir(os.path.join(src_folder, element)) ):
            directories.append(element)

    for filename in filenames:
        ProcessFile(src_start_path, dst_start_path, partial_path, filename)
    for directory in directories:
        ProcessFolder(src_start_path, dst_start_path, os.path.join(partial_path, directory))

def ProcessTree(src_start_path, dst_start_path):
    ProcessFolder(src_start_path, dst_start_path, '')

