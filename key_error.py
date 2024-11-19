import comtypes.client
comtypes.client.GetModule((comtypes.GUID("{14B95319-AEF9-492A-A878-CA18FEB1F5BF}"), 1, 7))
import comtypes.gen.HeidenhainDNCLib as HeidenhainDNCLib

comtypes.CoInitializeEx()
jhmachine = comtypes.client.CreateObject("HeidenhainDnc.JHMachineInProcess")
ijhmachine = jhmachine.QueryInterface(HeidenhainDNCLib.IJHMachine4)
version = ijhmachine.GetVersionComInterface()
print(f"VersionComInterface {version}")

ijhmachine.Release()
