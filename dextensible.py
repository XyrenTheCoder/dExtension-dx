import os, math
from typing import Union

T = True
F = False

class FileExtensionError(Exception): pass

class _main():
    def __init__(self):
        pass
    
    def getcwd():
        return os.getcwd()

    def include(self):
        __import__(self)

    def out(*self):
        _s = str()
        for _i in self:
            _s += str(_i)
        print(_s)

    def assign(var: str, value):
        if var.startswith('_'): raise NameError("Variable name cannot start with '_'.")
        globals()[var] = value

    def append(obj: str, tar: list):
        tar.append(obj)

    def extend(objs: list, tar: Union[tuple, list, dict, set]):
        tar.extend(objs)



    if __name__ != __file__:
        _f = input(f'{os.getcwd()} @-> ')
        #_f = 'text.dx' #test
        if not _f.endswith('.dx'): raise FileExtensionError('Invalid file extension, file extension should be ".dx"')
        with open(_f, 'r+') as _t:
            for _i in _t:
                if _i == '\n' or _i.startswith('//'): pass
                else: print(_i); eval(_i)

