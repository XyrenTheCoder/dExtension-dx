import os, sys, platform, distro
from typing import Union
# extensions
import math
from aliases import *
from errors import *

class _general():
    def __init__(self):
        pass
    
    def getcwd():
        return os.getcwd()
    
    def argv(index: int):
        return sys.argv[index]
    
    def getname():
        return os.name
    
    def getos():
        if platform.system() == 'Linux':
            _name = distro.linux_distribution()
            _version = distro.distro_release_info()
        else:
            _name = platform.system()
            _version = platform.version()
        return ' '.join([_name, _version])

    def getpyver():
        return platform.python_version()

    def include(self):
        __import__(self)

    def out(*self):
        _s = str()
        for _i in self:
            _s += str(_i)
        print(_s)

    def assign(var: str, value):
        if var.startswith('_'):
            raise NameError("Variable name cannot start with '_'.")
        globals()[var] = value

#class _strings():
    def join(obj, sep: str):
        return sep.join(obj)
        
    def split(obj: str, sep: str, maxspt: int): 
        if maxspt < -1:
            raise ValueError('Max split value must be larger than or equal to -1.')
        else:
            return obj.split(sep, maxspt)

#class _tuple_lists_dicts():
    def append(tar: list, obj: str):
        tar.append(obj)

    def extend(tar: list, obj: Union[tuple, list, dict, set]):
        tar.extend(obj)

    def lpop(tar: list, index: int=None):
        if index == None:
            tar.pop()
        else:
            tar.pop(index)

    def dpop(tar: dict, key):
        tar.pop(key)
    
    def spop(tar: set):
        tar.pop()

    def count(tar: list, obj):
        return tar.count(obj)

    
    
    

    # python dextensible.py test.dx
    if __name__ == __file__:
        if not sys.argv[2].endswith('.dx'): raise FileExtensionError('Invalid file extension, file extension should be ".dx"')
        else:
            with open(sys.argv[2], 'r+') as _t:
                for _i in _t:
                    if _i == '\n' or _i.startswith('//'): pass
                    else:
                        print(_i); eval(_i)
    else: #testing session
        with open('test.dx', 'r+') as _t:
                for _i in _t:
                    if _i == '\n' or _i.startswith('//'): pass
                    else:
                        eval(_i)

