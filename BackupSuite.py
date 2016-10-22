#manage user requests
#1. full backup (completely recreates the origin folder tree into the target folder)
#2. partial backup (a differencial backup to be regularly run, checks for new files & modifications, diferent hash)
#3. compress (like a tar gz, with or without password)
#4. restore (recreates the backup folder tree into the target folder)
import sys
import os 
import datetime
import shutil
import hashlib
import filecmp
import fullbackup
import partialbackup
import compress
import restore

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if len(sys.argv) != 4:
    print "Error in argument list"
    print "Expected 4 args: $> BackupSuite.py exec_mode src_path dst_path"
    
    print "Argument 0> BackupSuite.py : this script"
    print "Argument 1> exec_mode : execution mode (FullBackup; PartialBackup; Compress; Restore)"
    print "Argument 2> src_path : Source folder to backup"
    print "Argument 3> dst_path : Target for backup"
    sys.exit(-1)

src = sys.argv[2] + os.sep 
dst = sys.argv[3] +  os.sep 


if sys.argv[1] == "fullbackup" or sys.argv[1]=="FullBackup" or sys.argv[1] =="full" or sys.argv[1]== "Full":
    fullbackup.ProcessTree(src, dst)
elif sys.argv[1] == "partialbackup" or sys.argv[1]=="PartialBackup" or sys.argv[1]=="partial" or sys.argv[1] == "Partial":
    partialbackup.ProcessTree(src, dst)

sys.exit(0)
