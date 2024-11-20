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

del ijhdataentry
del jhdaccess
del jhdataaccess

ijhmachine.Disconnect()
del ijhmachine
del jhmachine
