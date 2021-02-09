#!/usr/bin/env python
import os
import shutil
  
def move_files(src_root, dest_root):
 
    dest_photo = os.path.join(dest_root,'Photo')
    dest_music = os.path.join(dest_root,'Music')
    dest_other = os.path.join(dest_root,'Documents')
 
    for root, dirs, files in os.walk(src_root):
        for _file in files:
 
            file_path = os.path.join(src_root, _file)
 
            if os.path.isfile(file_path):
 
                ext = os.path.splitext(_file.lower())[-1]
 
                if ext in ['.mov','.jpg','.png','.mp4']:
                    dest = os.path.join(dest_photo,_file)
                    shutil.copyfile(file_path,dest)
                    os.remove(file_path)
                elif ext in ['.mp3','.ogg','.flac']:
                    dest = os.path.join(dest_music,_file)
                    shutil.copyfile(file_path,dest)
                    os.remove(file_path)
                else:
                    dest = os.path.join(dest_other,_file)
                    shutil.copyfile(file_path,dest)
                    os.remove(file_path)
                     
if __name__ == "__main__":
     
    base_src = '/mnt/storage/MEGASync/'
    base_dest = '/mnt/storage'
     
    move_files(base_src, base_dest)

    #https://www.darkartistry.com/2018/12/using-linux-with-iphone-the-easy-way/