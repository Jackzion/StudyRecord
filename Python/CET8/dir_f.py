import os

def dir_f(search_text=''):
    entries = os.listdir()
    return list(filter(lambda filename : filename.__contains__(search_text) , entries))

def dir_find(path='.',search_text=''):
    result = []
    if os.path.isdir(path):
        entries = os.listdir(path)
        # 此层查找
        filter_files = filter(lambda filename : filename.__contains__(search_text) , entries)
        result += (list(map(lambda f : os.path.join(path,f),filter_files)))
        for entry in entries:
            full_path = os.path.join(path,entry)
            if os.path.isdir(full_path):
                # 进入下一层
                result += dir_find(path=full_path,search_text=search_text)
    else: 
        raise NotADirectoryError("not a directory")
    return result
print(dir_find(search_text='.json'))
print(dir_find(search_text='CET'))