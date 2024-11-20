from ctypes import HRESULT, byref

from comtypes.automation import _midlSAFEARRAY
import comtypes.client


comtypes.client.GetModule((comtypes.GUID("{14B95319-AEF9-492A-A878-CA18FEB1F5BF}"), 1, 7))
import comtypes.gen.HeidenhainDNCLib as HeidenhainDNCLib


jhdaccess = comtypes.client.CreateObject(HeidenhainDNCLib.JHDataAccess, interface=HeidenhainDNCLib.IJHDataAccess4)
sa_type = _midlSAFEARRAY(HRESULT)
arr_lock = sa_type.create([])
arr_unlock = sa_type.create([])

jhdaccess.LockConfig(["Idents", "To", "Lock"], byref(arr_lock))  # first parameter is example
jhdaccess.LockConfig(["Idents", "To", "Unlock"], byref(arr_unlock))  # first parameter is example

print(arr_lock)
print(arr_unlock)
