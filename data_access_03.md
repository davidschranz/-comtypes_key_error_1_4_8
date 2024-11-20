Exception running data_access_03.py
```
Traceback (most recent call last):
  File "C:\tools\PyCharm\plugins\python-ce\helpers\pydev\pydevd.py", line 1570, in _exec
    pydev_imports.execfile(file, globals, locals)  # execute the script
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\tools\PyCharm\plugins\python-ce\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\data_access_03.py", line 26, in <module>
    arr_lock = sa_type.create([])
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\safearray.py", line 144, in create
    raise MemoryError()
MemoryError
```
