Exception running data_access_01.py
Line jhdaccess = comtypes.client.CreateObject(HeidenhainDNCLib.JHDataAccess, interface=HeidenhainDNCLib.IJHDataAccess4)

```
D:\Projects\github\comtypes_key_error_1_4_8\.venv\Scripts\python.exe -X pycache_prefix=C:\Users\s91281\AppData\Local\JetBrains\PyCharm2024.3\cpython-cache C:/tools/PyCharm/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --port 29781 --file D:\Projects\github\comtypes_key_error_1_4_8\data_access_01.py 
Traceback (most recent call last):
  File "C:\tools\PyCharm\plugins\python-ce\helpers\pydev\pydevd.py", line 1570, in _exec
    pydev_imports.execfile(file, globals, locals)  # execute the script
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\tools\PyCharm\plugins\python-ce\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\data_access_01.py", line 11, in <module>
    jhdaccess = comtypes.client.CreateObject(HeidenhainDNCLib.JHDataAccess, interface=HeidenhainDNCLib.IJHDataAccess4)
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\client\__init__.py", line 267, in CreateObject
    obj = comtypes.CoCreateInstance(clsid, clsctx=clsctx, interface=interface)
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\_post_coinit\misc.py", line 137, in CoCreateInstance
    _ole32.CoCreateInstance(byref(clsid), punkouter, clsctx, byref(iid), byref(p))
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "_ctypes/callproc.c", line 1032, in GetResult
OSError: [WinError -2147221231] ClassFactory cannot supply requested class

Process finished with exit code 1
```
