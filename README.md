# comtypes_key_error_1_4_8
https://github.com/enthought/comtypes/issues/668

Steps to reproduce:\
Install HeidenhainDNC.msi\
Run key_error.py

Exception occurs in line 
```python
comtypes.client.GetModule((comtypes.GUID("{14B95319-AEF9-492A-A878-CA18FEB1F5BF}"), 1, 7))
```

Can fix it with modification of automation.py (line 951)
```python
_ctype_to_vartype: Dict[Type[_CData], int] = {
    HRESULT: VT_HRESULT,  # used for HeidenhainDNC.dll
    c_byte: VT_I1,
    c_ubyte: VT_UI1,
    c_short: VT_I2,
    c_ushort: VT_UI2,
    c_long: VT_I4,
    c_ulong: VT_UI4,
    c_float: VT_R4,
    c_double: VT_R8,
    c_longlong: VT_I8,
    c_ulonglong: VT_UI8,
    VARIANT_BOOL: VT_BOOL,
    BSTR: VT_BSTR,
    VARIANT: VT_VARIANT,
    # SAFEARRAY(VARIANT *)
    #
    # It is unlear to me if this is allowed or not.  Apparently there
    # are typelibs that define such an argument type, but it may be
    # that these are buggy.
    #
    # Point is that SafeArrayCreateEx(VT_VARIANT|VT_BYREF, ..) fails.
    # The MSDN docs for SafeArrayCreate() have a notice that neither
    # VT_ARRAY not VT_BYREF may be set, this notice is missing however
    # for SafeArrayCreateEx().
    #
    # We have this code here to make sure that comtypes can import
    # such a typelib, although calling ths method will fail because
    # such an array cannot be created.
    POINTER(VARIANT): VT_BYREF | VT_VARIANT,
    # This is needed to import Esri ArcObjects (esriSystem.olb).
    POINTER(BSTR): VT_BYREF | VT_BSTR,
    # These are not yet implemented:
    # POINTER(IUnknown): VT_UNKNOWN,
    # POINTER(IDispatch): VT_DISPATCH,
}
```

Exception before modification of automation.py
```
import sys; print('Python %s on %s' % (sys.version, sys.platform))
D:\Projects\github\comtypes_key_error_1_4_8\.venv\Scripts\python.exe -X pycache_prefix=C:\Users\s91281\AppData\Local\JetBrains\PyCharm2024.3\cpython-cache C:/tools/PyCharm/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --port 29781 --file D:\Projects\github\comtypes_key_error_1_4_8\key_error.py 
Traceback (most recent call last):
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\safearray.py", line 66, in _midlSAFEARRAY
    return POINTER(_safearray_type_cache[itemtype])  # type: ignore
                   ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: <class 'ctypes.HRESULT'>
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\safearray.py", line 87, in _make_safearray_type
    vartype = _ctype_to_vartype[itemtype]
              ~~~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: <class 'ctypes.HRESULT'>
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "C:\tools\PyCharm\plugins\python-ce\helpers\pydev\pydevd.py", line 1570, in _exec
    pydev_imports.execfile(file, globals, locals)  # execute the script
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\tools\PyCharm\plugins\python-ce\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\key_error.py", line 2, in <module>
    comtypes.client.GetModule((comtypes.GUID("{14B95319-AEF9-492A-A878-CA18FEB1F5BF}"), 1, 7))
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\client\_generate.py", line 128, in GetModule
    return ModuleGenerator(tlib, pathname).generate()
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\client\_generate.py", line 245, in generate
    return [_create_module(name, code) for (name, code) in codebases][-1]
            ~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\client\_generate.py", line 217, in _create_module
    return _my_import(modulename)
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\client\_generate.py", line 27, in _my_import
    return importlib.import_module(fullname)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\s91281\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1022, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\gen\_14B95319_AEF9_492A_A878_CA18FEB1F5BF_0_1_7.py", line 2157, in <module>
    (['in', 'out'], POINTER(_midlSAFEARRAY(HRESULT)), 'ppsafLockResults')
                            ~~~~~~~~~~~~~~^^^^^^^^^
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\safearray.py", line 68, in _midlSAFEARRAY
    sa_type = _make_safearray_type(itemtype)
  File "D:\Projects\github\comtypes_key_error_1_4_8\.venv\Lib\site-packages\comtypes\safearray.py", line 107, in _make_safearray_type
    raise TypeError(itemtype)
TypeError: <class 'ctypes.HRESULT'>
python-BaseException
```