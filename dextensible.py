import os, sys, platform, distro, math
from typing import Union

T = True
F = False

class FileExtensionError(Exception): pass

class _main():
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
        if var.startswith('_'): raise NameError("Variable name cannot start with '_'.")
        globals()[var] = value

    def append(obj: str, tar: list):
        tar.append(obj)

    def extend(objs: list, tar: Union[tuple, list, dict, set]):
        tar.extend(objs)

    def join(obj, sep: str):
        return sep.join(obj)
        

    # python dextensible.py test.dx
    if __name__ == __file__:
        if not sys.argv[2].endswith('.dx'): raise FileExtensionError('Invalid file extension, file extension should be ".dx"')
        else:
            with open(sys.argv[2], 'r+') as _t:
                for _i in _t:
                    if _i == '\n' or _i.startswith('//'): pass
                    else: print(_i); eval(_i)
    else: #testing session
        with open('test.dx', 'r+') as _t:
                for _i in _t:
                    if _i == '\n' or _i.startswith('//'): pass
                    else: print(_i); eval(_i)

