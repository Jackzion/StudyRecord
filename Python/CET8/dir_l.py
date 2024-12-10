import os,time

def dir_l(path='.'):
    entries = os.listdir(path)
    for entry in entries:
        full_path = os.path.join(path,entry)
        stat_info = os.stat(full_path)
        
        permissions = stat_info.st_mode
        size = stat_info.st_size
        last_modify = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(stat_info.st_mtime))
        print(f'{permissions} {size} {last_modify} {entry}')

dir_l()