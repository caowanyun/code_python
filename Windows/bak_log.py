#!/usr/bin/env python
# -*- conding:utf8 -*-


import os
import sys
import time
import shutil
import socket
import zipfile
import datetime
import fileinput


####################################################################


Now = time.strftime('%H')
Today = datetime.date.today()
Sevendays = Today - datetime.timedelta(days=1)
Sevendaysago = Sevendays.strftime('%Y%m%d')
Sevenbaklogdir = 'd:\\back_log' + '\\' + '%s' % Sevendaysago + '\\' + '%s' % Now
File = open("d:\dir_name.txt", 'w')
Gamepath = open("d:\game_dir.txt", 'w')
Hostname = socket.gethostname()

if os.path.isdir('%s' % Sevenbaklogdir):
    pass
else:
    os.makedirs('%s' % Sevenbaklogdir)

####################################################################


def Isdir(dir_path):
    for name in os.listdir(dir_path):
        dirname = os.path.join(dir_path, name)
        if "gcd_games" in dirname:
            print >> Gamepath, dirname
            print "Game path is %s !!!" % dirname
            Disk,Father,Gamedir = dirname.split('\\')
            global Gamelogbakdir
            Gamelogbakdir = '%s' % Sevenbaklogdir + '\\' + '%s' % Gamedir
            print >> File, Gamelogbakdir
            print "Log backup path is %s !!!" % Gamelogbakdir
            Source = '%s' % dirname + '\\bin\\GameServer\\Exception'
            print "Game Source log path is %s !!!" % Source
            if os.path.isdir('%s' % Gamelogbakdir):
                pass
            else:
                os.makedirs('%s' % Gamelogbakdir)
                lname = "Exception_" + "%s" % Sevendaysago + '%s' % Now
                for file in os.listdir("%s" % Source):
                    if lname in file:
                        Sourcelog = "%s\%s" % (Source,file)
                        print Sourcelog
                        shutil.move("%s" % Sourcelog,"%s" % Gamelogbakdir)


def Ziplog(log_bakpath):
    Zipname = '%s' % log_bakpath + '%s' % Hostname + '_' + '%s' % Sevendaysago + '_' + '%s' % Now + '.zip'
    #print Zipname
    Zipfile = zipfile.ZipFile(Zipname, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(log_bakpath):
        for filename in filenames:
            Zipfile.write(os.path.join(dirpath, filename))
    Zipfile.close
    shutil.rmtree(log_bakpath)  #
    #print "D:\\game_package\\bin\\rsync.exe -avz /cygdrive/d/back_log/20160613  /cygdrive/d/back_log/20160615"



if __name__ == '__main__':
    Isdir("d:\game_package")
    File.close()
    Gamepath.close()
    Ziplog(Sevenbaklogdir)
    os.system("D:\\game_package\\bin\\rsync.exe -avz /cygdrive/d/back_log/20160613  /cygdrive/d/back_log/20160621")



####################################################################
