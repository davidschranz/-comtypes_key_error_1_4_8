"""
This code does only work together with a heidenhain control
The IJHMachine4 needs to be connected to be able to get the IJHDataAccess4 interface

Disconnect will fail if not all interfaces queried from IJHMachine4 are released.
comtypes will call Release itself once the object is deleted

The method LockConfig is not (yet) documented.
I do not know how the bstrIdentsToLock would have to lock like.
bstrIdentsToLock = ["\\PLC\\memory\\M\\0"]
ppsafLockResults = jjhdataaccess.LockConfig(bstrIdentsToLock)
Returns _ctypes.COMError: (-2147024809, 'The parameter is incorrect.', (None, None, None, 0, None))

Wrapping the HeidenhainDNCLib will fail (comtypes.client.GetModule) if VT_HRESULT does not exit.

_ctype_to_vartype.update not necessary if using https://github.com/davidschranz/comtypes.git
"""
# from comtypes.automation import _ctype_to_vartype, HRESULT, VT_HRESULT
# _ctype_to_vartype.update({HRESULT: VT_HRESULT})

import comtypes.client
comtypes.client.GetModule((comtypes.GUID("{14B95319-AEF9-492A-A878-CA18FEB1F5BF}"), 1, 7))
import comtypes.gen.HeidenhainDNCLib as HeidenhainDNCLib

jhmachine = comtypes.client.CreateObject("HeidenhainDnc.JHMachineInProcess")
ijhmachine = jhmachine.QueryInterface(HeidenhainDNCLib.IJHMachine4)
name = ijhmachine.ConfigureConnection(HeidenhainDNCLib.DNC_CONFIGURE_MODE_ALL)
ijhmachine.Connect(name)

jhdataaccess = ijhmachine.GetInterface(HeidenhainDNCLib.DNC_INTERFACE_JHDATAACCESS)
jjhdataaccess = jhdataaccess.QueryInterface(HeidenhainDNCLib.IJHDataAccess4)
jjhdataaccess.SetAccessMode(HeidenhainDNCLib.DNC_ACCESS_MODE_PLCDATAACCESS, '807667')

entry = r"\PLC\memory\M\0"
ijhdataentry = jjhdataaccess.GetDataEntry2(entry, HeidenhainDNCLib.DNC_DATA_UNIT_SELECT_METRIC, False)
value = ijhdataentry.GetPropertyValue(HeidenhainDNCLib.DNC_DATAENTRY_PROPKIND_DATA)
# ijhdataentry.SetPropertyValue(HeidenhainDNCLib.DNC_DATAENTRY_PROPKIND_DATA, not(value), False)
print(value)

del ijhdataentry
del jjhdataaccess
del jhdataaccess

ijhmachine.Disconnect()
del ijhmachine
del jhmachine
