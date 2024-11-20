from ctypes import HRESULT, byref

from comtypes.automation import _midlSAFEARRAY

import comtypes.client
comtypes.client.GetModule((comtypes.GUID("{14B95319-AEF9-492A-A878-CA18FEB1F5BF}"), 1, 7))
import comtypes.gen.HeidenhainDNCLib as HeidenhainDNCLib

jhmachine = comtypes.client.CreateObject("HeidenhainDnc.JHMachineInProcess")
ijhmachine = jhmachine.QueryInterface(HeidenhainDNCLib.IJHMachine4)

name = jhmachine.ConfigureConnection(HeidenhainDNCLib.DNC_CONFIGURE_MODE_ALL)
ijhmachine.Connect(name)

jhdataaccess = ijhmachine.GetInterface(HeidenhainDNCLib.DNC_INTERFACE_JHDATAACCESS)
jhdaccess = jhdataaccess.QueryInterface(HeidenhainDNCLib.IJHDataAccess4)

entry = r"\PLC\program\symbol\global\Axes[0].DG_ref_position"
jhdaccess.SetAccessMode(HeidenhainDNCLib.DNC_ACCESS_MODE_PLCDATAACCESS, '807667')
ijhdataentry = jhdaccess.GetDataEntry2(entry, HeidenhainDNCLib.DNC_DATA_UNIT_SELECT_METRIC, True)
value = ijhdataentry.GetPropertyValue(HeidenhainDNCLib.DNC_DATAENTRY_PROPKIND_DATA)
print(value)

# jhdaccess = comtypes.client.CreateObject(HeidenhainDNCLib.JHDataAccess, interface=HeidenhainDNCLib.IJHDataAccess4)
sa_type = _midlSAFEARRAY(HRESULT)
arr_lock = sa_type.create([])
arr_unlock = sa_type.create([])

jhdaccess.LockConfig(["Idents", "To", "Lock"], byref(arr_lock))  # first parameter is example
jhdaccess.UnlockConfig(["Idents", "To", "Unlock"], byref(arr_unlock))  # first parameter is example

print(arr_lock)
print(arr_unlock)

del ijhdataentry
del jhdaccess
del jhdataaccess

ijhmachine.Disconnect()
del ijhmachine
del jhmachine
