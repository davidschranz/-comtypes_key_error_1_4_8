# -*- coding: mbcs -*-

from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import (
    _check_version, BSTR, CoClass, COMMETHOD, dispid, DISPMETHOD,
    GUID, helpstring, IUnknown
)
from ctypes import HRESULT
from comtypes.automation import _midlSAFEARRAY, VARIANT
from ctypes.wintypes import VARIANT_BOOL
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from comtypes import hints


_lcid = 0  # change this if required
typelib_path = 'C:\\PROGRA~1\\COMMON~1\\HEIDEN~1\\HEIDEN~1.DLL'
DNC_HANDLE = c_int

# values for enumeration 'DNC_DATAENTRY_PROPKIND'
DNC_DATAENTRY_PROPKIND_DATA = 0
DNC_DATAENTRY_PROPKIND_UNIT = 1
DNC_DATAENTRY_PROPKIND_UNITTEXT = 2
DNC_DATAENTRY_PROPKIND_LOWER_BOUND = 3
DNC_DATAENTRY_PROPKIND_UPPER_BOUND = 4
DNC_DATAENTRY_PROPKIND_DESCRIPTION = 5
DNC_DATAENTRY_PROPKIND_SUBSCRIBE_CAPABILITY = 6
DNC_DATAENTRY_PROPKIND_SAMPLE_CAPABILITY = 7
DNC_DATAENTRY_PROPKIND_DATAWIDTH = 8
DNC_DATAENTRY_PROPKIND_INITIALVALUE = 9
DNC_DATAENTRY_PROPKIND_LOCATION = 10
DNC_DATAENTRY_PROPKIND_BASE_ENTRY = 11
DNC_DATAENTRY_PROPKIND = c_int  # enum

# values for enumeration 'DNC_PLC_OPTION'
DNC_PLC_OPTION_NOSYNC = 0
DNC_PLC_OPTION = c_int  # enum

# values for enumeration 'DNC_STS_PROGRAM'
DNC_PRG_STS_IDLE = 0
DNC_PRG_STS_RUNNING = 1
DNC_PRG_STS_STOPPED = 2
DNC_PRG_STS_INTERRUPTED = 3
DNC_PRG_STS_FINISHED = 4
DNC_PRG_STS_ERROR = 5
DNC_PRG_STS_NOT_SELECTED = 6
DNC_STS_PROGRAM = c_int  # enum

# values for enumeration 'DNC_CONNECTION_PROPERTY'
DNC_CP_HOST = 0
DNC_CP_PORT = 1
DNC_CP_LSV_AUTODETECT = 2
DNC_CP_SPEED = 3
DNC_CP_DATABITS = 4
DNC_CP_STOPBITS = 5
DNC_CP_PARITY = 6
DNC_CP_CHECK_DTR = 7
DNC_CP_LSV_DELAY = 8
DNC_CP_LSV_RETRIES = 9
DNC_CP_LSV_OPTIONS = 10
DNC_CP_LSV_TX_TIMEOUT = 11
DNC_CP_LSV_RX_TIMEOUT = 12
DNC_CP_DIO_PROTOCOL = 13
DNC_CP_DIO_FLOWCTRL = 14
DNC_CP_DIO_LEADERLENGTH = 15
DNC_CP_SSH_IDENT = 16
DNC_CP_SSH_IDENT_PASSWORD = 17
DNC_CP_SSH_REMOTE_USER = 18
DNC_CP_SSH_REMOTE_HOST_KEY_FINGERPRINT = 19
DNC_CONNECTION_PROPERTY = c_int  # enum

# values for enumeration 'DNC_PROTOCOL'
DNC_PROT_DIO = 8
DNC_PROT_LSV2 = 1
DNC_PROT_TCPIP = 2
DNC_PROT_COM = 4
DNC_PROT_RPC = 5
DNC_PROT_TCPIP_SECURE = 12
DNC_PROT_RPC_SECURE = 15
DNC_PROTOCOL = c_int  # enum

# values for enumeration 'DNC_CNC_TYPE'
DNC_CNC_TYPE_ATEKM = 0
DNC_CNC_TYPE_ITNC = 1
DNC_CNC_TYPE_MILLPLUS = 2
DNC_CNC_TYPE_MILLPLUSIT = 3
DNC_CNC_TYPE_TURNPLUS = 4
DNC_CNC_TYPE_MILLPLUSIT_NCK = 5
DNC_CNC_TYPE_MANUALPLUS_NCK = 6
DNC_CNC_TYPE_ATEKM_NCK = 7
DNC_CNC_TYPE_TNC320_NCK = 8
DNC_CNC_TYPE_GRINDPLUS_NCK = 9
DNC_CNC_TYPE_TNC6xx_NCK = 10
DNC_CNC_TYPE_AR6000_NCK = 11
DNC_CNC_TYPE_CNCPILOT6xx_NCK = 12
DNC_CNC_TYPE_TNC128_NCK = 13
DNC_CNC_TYPE_GRINDPLUS640_NCK = 14
DNC_CNC_TYPE_TNC7_NCK = 15
DNC_CNC_TYPE = c_int  # enum

# values for enumeration 'DNC_TRIG_SAMPLE_MODE'
DNC_TRIG_SAMPLE_ON_CHANGE = 0
DNC_TRIG_SAMPLE_ON_TIMER = 1
DNC_TRIG_SAMPLE_ON_PLC = 2
DNC_TRIG_SAMPLE_ON_IPO = 3
DNC_TRIG_SAMPLE_ON_CCU = 4
DNC_TRIG_SAMPLE_MODE = c_int  # enum

# values for enumeration 'DNC_FEED_MODE'
FEED_MODE_NORMAL = 0
FEED_MODE_RAPID = 1
DNC_FEED_MODE = c_int  # enum

# values for enumeration 'DNC_SPINDLE_STATE'
DNC_SPINDLE_STATE_CW = 0
DNC_SPINDLE_STATE_CCW = 1
DNC_SPINDLE_STATE_STOPPED = 2
DNC_SPINDLE_STATE_POS_CTRL = 3
DNC_SPINDLE_STATE_TAPPING = 4
DNC_SPINDLE_STATE_RIGID_TAPPING = 5
DNC_SPINDLE_STATE = c_int  # enum

# values for enumeration 'DNC_POSSAMPLES_MOTION_TYPE'
DNC_POSSAMPLES_MOTION_COMPLEX = 0
DNC_POSSAMPLES_MOTION_LINEAR = 1
DNC_POSSAMPLES_MOTION_CIRCULAR = 2
DNC_POSSAMPLES_MOTION_SPLINE = 3
DNC_POSSAMPLES_MOTION_TYPE = c_int  # enum

# values for enumeration 'DNC_POSSAMPLES_LOGGING_TYPE'
DNC_POSSAMPLES_LOGGING_SAMPLED = 0
DNC_POSSAMPLES_LOGGING_ENDPOINTS = 1
DNC_POSSAMPLES_LOGGING_SAMPLED_WITH_BLOCK_END = 2
DNC_POSSAMPLES_LOGGING_NONLINEAR_SAMPLED_WITH_BLOCK_END = 3
DNC_POSSAMPLES_LOGGING_SAMPLED_WITH_AUX_AXES = 4
DNC_POSSAMPLES_LOGGING_ENDPOINTS_WITH_AUX_AXES = 5
DNC_POSSAMPLES_LOGGING_SAMPLED_WITH_BLOCK_END_WITH_AUX_AXES = 6
DNC_POSSAMPLES_LOGGING_NONLINEAR_SAMPLED_WITH_BLOCK_END_WITH_AUX_AXES = 7
DNC_POSSAMPLES_LOGGING_TYPE = c_int  # enum

# values for enumeration 'DNC_INTERFACE_OBJECT'
DNC_INTERFACE_JHAUTOMATIC = 0
DNC_INTERFACE_JHCONFIGURATION = 1
DNC_INTERFACE_JHERROR = 2
DNC_INTERFACE_JHPROCESSDATA = 3
DNC_INTERFACE_JHVERSION = 4
DNC_INTERFACE_JHFILESYSTEM = 5
DNC_INTERFACE_JHPLC = 6
DNC_INTERFACE_TNCTABLE = 7
DNC_INTERFACE_JHAXESPOSITIONSTREAMING = 8
DNC_INTERFACE_JHDATAACCESS = 9
DNC_INTERFACE_JHTEST = 10
DNC_INTERFACE_JHTRACE = 11
DNC_INTERFACE_JHVIRTUALMACHINE = 12
DNC_INTERFACE_JHDIAGNOSTICS = 13
DNC_INTERFACE_JHREMOTEERROR = 14
DNC_INTERFACE_OBJECT = c_int  # enum

# values for enumeration 'DNC_CONFIGURE_MODE'
DNC_CONFIGURE_MODE_ADD = 0
DNC_CONFIGURE_MODE_CHANGE = 1
DNC_CONFIGURE_MODE_REMOVE = 2
DNC_CONFIGURE_MODE_ALL = 3
DNC_CONFIGURE_MODE = c_int  # enum

# values for enumeration 'DNC_ERROR_GROUP'
DNC_EG_NONE = 0
DNC_EG_OPERATING = 1
DNC_EG_PROGRAMING = 2
DNC_EG_PLC = 3
DNC_EG_GENERAL = 4
DNC_EG_REMOTE = 5
DNC_EG_PYTHON = 6
DNC_ERROR_GROUP = c_int  # enum

# values for enumeration 'DNC_ERROR_CLASS'
DNC_EC_NONE = 0
DNC_EC_WARNING = 1
DNC_EC_FEEDHOLD = 2
DNC_EC_PROGRAMHOLD = 3
DNC_EC_PROGRAMABORT = 4
DNC_EC_EMERGENCY_STOP = 5
DNC_EC_RESET = 6
DNC_EC_INFO = 7
DNC_EC_ERROR = 8
DNC_EC_NOTE = 9
DNC_ERROR_CLASS = c_int  # enum

# values for enumeration 'DNC_ERROR_LOCATION'
DNC_ERROR_LOCATION_NONE = 0
DNC_ERROR_LOCATION_MACHINE = 1
DNC_ERROR_LOCATION_EDIT = 2
DNC_ERROR_LOCATION_OEM = 3
DNC_ERROR_LOCATION = c_int  # enum

# values for enumeration 'DNC_EVT_STATE'
DNC_EVT_STATE_HOST_NOT_AVAILABLE = 0
DNC_EVT_STATE_HOST_AVAILABLE = 1
DNC_EVT_STATE_WAIT_PERMISSION = 2
DNC_EVT_STATE_DNC_AVAILABLE = 3
DNC_EVT_STATE_MACHINE_BOOTED = 4
DNC_EVT_STATE_MACHINE_INITIALIZING = 5
DNC_EVT_STATE_MACHINE_AVAILABLE = 6
DNC_EVT_STATE_MACHINE_SHUTTING_DOWN = 7
DNC_EVT_STATE_DNC_STOPPED = 8
DNC_EVT_STATE_HOST_STOPPED = 9
DNC_EVT_STATE_CONNECTION_LOST = 10
DNC_EVT_STATE_PERMISSION_DENIED = 11
DNC_EVT_STATE = c_int  # enum

# values for enumeration 'DNC_TRIG_CONDITION'
DNC_TRIG_ON_COND_NONE = 0
DNC_TRIG_ON_COND_EQ = 1
DNC_TRIG_ON_COND_NEQ = 2
DNC_TRIG_ON_COND_LEQ = 3
DNC_TRIG_ON_COND_GEQ = 4
DNC_TRIG_ON_COND_LT = 5
DNC_TRIG_ON_COND_GT = 6
DNC_TRIG_ON_COND_INSIDE = 7
DNC_TRIG_ON_COND_OUTSIDE = 8
DNC_TRIG_CONDITION = c_int  # enum

# values for enumeration 'DNC_TRIG_MODE'
DNC_TRIG_MODE_NONE = 0
DNC_TRIG_ON_CHANGE = 1
DNC_TRIG_ON_CHANGE_DELTA = 2
DNC_TRIG_ON_RISE = 3
DNC_TRIG_ON_FALL = 4
DNC_TRIG_ON_CONDITION = 5
DNC_TRIG_ON_SUSTAINED_CONDITION = 6
DNC_TRIG_ALWAYS = 7
DNC_TRIG_MODE = c_int  # enum

# values for enumeration 'DNC_STATE'
DNC_STATE_NOT_INITIALIZED = 0
DNC_STATE_HOST_IS_NOT_AVAILABLE = 1
DNC_STATE_HOST_IS_AVAILABLE = 2
DNC_STATE_WAITING_PERMISSION = 3
DNC_STATE_DNC_IS_AVAILABLE = 4
DNC_STATE_MACHINE_IS_BOOTED = 5
DNC_STATE_MACHINE_IS_INITIALIZING = 6
DNC_STATE_MACHINE_IS_AVAILABLE = 7
DNC_STATE_MACHINE_IS_SHUTTING_DOWN = 8
DNC_STATE_DNC_IS_STOPPED = 9
DNC_STATE_HOST_IS_STOPPED = 10
DNC_STATE_NO_PERMISSION = 11
DNC_STATE = c_int  # enum

# values for enumeration 'DNC_ACCESS_MODE'
DNC_ACCESS_MODE_DEFAULT = 0
DNC_ACCESS_MODE_USR_PRIVATE = 1
DNC_ACCESS_MODE_OEM = 2
DNC_ACCESS_MODE_SYS = 3
DNC_ACCESS_MODE_INSPECT = 4
DNC_ACCESS_MODE_DIAGNOSTICS = 5
DNC_ACCESS_MODE_PLCDEBUG = 6
DNC_ACCESS_MODE_USR = 7
DNC_ACCESS_MODE_MONITOR = 8
DNC_ACCESS_MODE_DSP = 9
DNC_ACCESS_MODE_DNC = 10
DNC_ACCESS_MODE_SCOPE = 11
DNC_ACCESS_MODE_ALL = 12
DNC_ACCESS_MODE_AUTOMATIC = 13
DNC_ACCESS_MODE_PLC = 14
DNC_ACCESS_MODE_IPODATAACCESS = 15
DNC_ACCESS_MODE_OEM_ENCRYPTED = 16
DNC_ACCESS_MODE_NONE = 17
DNC_ACCESS_MODE_TESTUTILITY = 18
DNC_ACCESS_MODE_SENDKEY = 19
DNC_ACCESS_MODE_AXESPOSITIONSTREAMING = 20
DNC_ACCESS_MODE_SPLCDATAACCESS = 21
DNC_ACCESS_MODE_HWSDATAACCESS = 22
DNC_ACCESS_MODE_TABLEDATAACCESS = 23
DNC_ACCESS_MODE_PLCDATAACCESS = 24
DNC_ACCESS_MODE_GEODATAACCESS = 25
DNC_ACCESS_MODE_CFGDATAACCESS = 26
DNC_ACCESS_MODE_GEOSIMDATAACCESS = 27
DNC_ACCESS_MODE = c_int  # enum

# values for enumeration 'DNC_KEYACTION'
DNC_KEYACTION_DOWN_UP = 0
DNC_KEYACTION_DOWN = 1
DNC_KEYACTION_UP = 2
DNC_KEYACTION = c_int  # enum

# values for enumeration 'DNC_TRACE_VARIABLE_ID'
DNC_TRACE_VARIABLE_ID_NONE = 0
DNC_TRACE_VARIABLE_ID_AACT = 1
DNC_TRACE_VARIABLE_ID_ANOM = 2
DNC_TRACE_VARIABLE_ID_VACT = 3
DNC_TRACE_VARIABLE_ID_VNOM = 4
DNC_TRACE_VARIABLE_ID_FEED = 5
DNC_TRACE_VARIABLE_ID_BLOCK_NR = 6
DNC_TRACE_VARIABLE_ID_SACT = 7
DNC_TRACE_VARIABLE_ID_SNOM = 8
DNC_TRACE_VARIABLE_ID_SERR = 9
DNC_TRACE_VARIABLE_ID_SDIFF = 10
DNC_TRACE_VARIABLE_ID_CSI1 = 11
DNC_TRACE_VARIABLE_ID_CSI2 = 12
DNC_TRACE_VARIABLE_ID_JACT = 13
DNC_TRACE_VARIABLE_ID_JNOM = 14
DNC_TRACE_VARIABLE_ID_VNACT = 15
DNC_TRACE_VARIABLE_ID_VNNOM = 16
DNC_TRACE_VARIABLE_ID_ININT = 17
DNC_TRACE_VARIABLE_ID_INOM = 18
DNC_TRACE_VARIABLE_ID_PLC = 19
DNC_TRACE_VARIABLE_ID_ANALOG_OUT = 20
DNC_TRACE_VARIABLE_ID_IPODBG = 21
DNC_TRACE_VARIABLE_ID_CCDBG = 22
DNC_TRACE_VARIABLE_ID_IPOLOGIC = 23
DNC_TRACE_VARIABLE_ID = c_int  # enum

# values for enumeration 'DNC_TRACE_VARIABLE_TYPE'
DNC_TRACE_VARIABLE_TYPE_UNKNOWN = 0
DNC_TRACE_VARIABLE_TYPE_NORMAL = 1
DNC_TRACE_VARIABLE_TYPE_AXIS = 2
DNC_TRACE_VARIABLE_TYPE_CHANNEL = 3
DNC_TRACE_VARIABLE_TYPE_PATH = 4
DNC_TRACE_VARIABLE_TYPE = c_int  # enum

# values for enumeration 'DNC_PLC_ACTION'
DNC_PLC_ACTION_WRITE = 8192
DNC_PLC_ACTION = c_int  # enum

# values for enumeration 'DNC_TRACE_SOURCE_TYPE'
DNC_TRACE_SOURCE_TYPE_UNKNOWN = 0
DNC_TRACE_SOURCE_TYPE_IPO = 1
DNC_TRACE_SOURCE_TYPE_CCU = 2
DNC_TRACE_SOURCE_TYPE_PLC = 3
DNC_TRACE_SOURCE_TYPE = c_int  # enum

# values for enumeration 'DNC_HRESULT'
DNC_E_FAIL = -2147220991
DNC_E_ALL_CONNECTIONS_IN_USE = -2147220896
DNC_E_OPTION_NOT_AVAILABLE = -2147220895
DNC_E_DNC32FAILED = -2147220894
DNC_E_RPCFAILED = -2147220893
DNC_E_INVALID_PARAM = -2147220892
DNC_E_WRONG_MODE = -2147220891
DNC_E_NOT_POS_NOW = -2147220890
DNC_E_WRONG_OPERATE_MODE = -2147220889
DNC_E_OUT_OF_RANGE = -2147220888
DNC_E_NOT_INITIALISED = -2147220887
DNC_E_DNC_PROHIBITED = -2147220886
DNC_E_TOO_MANY_ELEMENTS = -2147220885
DNC_E_LIST_EMPTY = -2147220884
DNC_E_READ_ONLY = -2147220883
DNC_E_INVALID_DATA = -2147220882
DNC_E_NOT_ADVISED = -2147220881
DNC_E_MULTIPLE_OBJECTS = -2147220880
DNC_E_TRANSFER_ABORT = -2147220879
DNC_E_INVALID_PASSWORD = -2147220878
DNC_E_CANNOT_RESTORE_DEFAULT = -2147220877
DNC_E_MISSING_PARAM = -2147220876
DNC_E_UNABLE_TO_GET = -2147220875
DNC_E_UNABLE_TO_SET = -2147220874
DNC_E_UTC_TO_LOCAL = -2147220873
DNC_E_LOCAL_TO_UTC = -2147220872
DNC_E_STREAMING_ACTIVE = -2147220871
DNC_E_NO_STREAMING_ACTIVE = -2147220870
DNC_E_INVALID_AXIS = -2147220869
DNC_E_ITEM_NOT_FOUND = -2147220868
DNC_E_EXISTS = -2147220867
DNC_E_INVALID_CHANNEL = -2147220866
DNC_E_SUBSCRIPTION_ACTIVE = -2147220865
DNC_E_ITEM_DELETED = -2147220864
DNC_E_IN_USE = -2147220863
DNC_E_TIMEOUT = -2147220862
DNC_E_ECLIPSED = -2147220861
DNC_E_RECORD_NOT_FOUND = -2147220792
DNC_E_UNABLE_TO_INSERT = -2147220791
DNC_E_UNABLE_TO_DELETE = -2147220790
DNC_E_RECORD_LOCKED = -2147220789
DNC_E_SYNONYM_ACCESS = -2147220788
DNC_E_KEY_UNDEFINED = -2147220787
DNC_E_LOCKED = -2147220786
DNC_E_NOT_LOCKED = -2147220785
DNC_E_TRACING_ACTIVE = -2147220692
DNC_E_NO_TRACING_ACTIVE = -2147220691
DNC_E_NO_TRACE_DATA_AVAILABLE = -2147220690
DNC_E_NO_PROGRAM = -2147220391
DNC_E_PROGRAM_NOT_STARTED = -2147220390
DNC_E_NO_PROGRAM_ACTIVE = -2147220389
DNC_E_CANNOT_START_PROGRAM = -2147220388
DNC_E_CANNOT_LOAD_PROGRAM = -2147220387
DNC_E_ENDSWITCH_TRIPPED = -2147220386
DNC_E_COLLISION = -2147220385
DNC_E_HARD_DISK_FAIL = -2147220291
DNC_E_DISK_FULL = -2147220290
DNC_E_NO_DRIVE_ACCESS = -2147220289
DNC_E_DIR_NOT_EMPTY = -2147220288
DNC_E_DIR_EXISTS = -2147220287
DNC_E_DIR_NESTING = -2147220286
DNC_E_DIR_OVERFLOW = -2147220285
DNC_E_DIR_NOT_FOUND = -2147220284
DNC_E_FILE_EXISTS = -2147220283
DNC_E_FILE_LOCKED = -2147220282
DNC_E_FILE_FILENAME = -2147220281
DNC_E_FILE_NOT_FOUND = -2147220280
DNC_E_FILE_IN_USE = -2147220279
DNC_E_FILE_OVERFLOW = -2147220278
DNC_E_FILE_OPEN_FAILED = -2147220277
DNC_E_FILE_WRONG_MODE = -2147220276
DNC_E_DIR_LOCKED = -2147220275
DNC_E_FILE_REMOTE_NOT_FOUND = -2147220274
DNC_E_FILE_REMOTE_EXISTS = -2147220273
DNC_E_FILE_REMOTE_LOCKED = -2147220272
DNC_E_FILE_REMOTE_FILENAME = -2147220271
DNC_E_DIR_REMOTE_NOT_FOUND = -2147220270
DNC_E_DIR_REMOTE_LOCKED = -2147220269
DNC_E_DIR_REMOTE_EXISTS = -2147220268
DNC_E_REMOTE_READ_ONLY = -2147220267
DNC_E_FILE_LOCAL_OPEN_FAILED = -2147220266
DNC_E_FILE_CANNOT_OPEN = -2147220264
DNC32_E_STILL_CONN = -2147219791
DNC32_E_NOT_CONN = -2147219790
DNC32_E_NOT_HANDLE = -2147219789
DNC32_E_FAIL_HANDLE = -2147219788
DNC32_E_INIT = -2147219787
DNC32_E_NOT_PROT = -2147219786
DNC32_E_TRANS_FAIL = -2147219785
DNC32_E_RECV_FAIL = -2147219784
DNC32_E_RESERVED = -2147219783
DNC32_E_NOT_RES = -2147219782
DNC32_E_RECV_FRAME = -2147219781
DNC32_E_RECV_TIMEOUT = -2147219780
DNC32_E_VER_TOO_OLD = -2147219779
DNC32_E_VER_TOO_NEW = -2147219778
DNC32_E_TIMEOUT_VAL = -2147219777
DNC32_E_OPTION_VAL = -2147219776
DNC32_E_NO_ADDRESS = -2147219775
DNC32_E_NO_PORT = -2147219774
DNC32_E_PARITY = -2147219773
DNC32_E_FAIL_WINSOCK = -2147219772
DNC32_E_FAIL_LOOKUP = -2147219771
DNC32_E_FAIL_SOCKET = -2147219770
DNC32_E_FAIL_CONNECT = -2147219769
DNC32_E_FAIL_ACCEPT = -2147219768
DNC32_E_INVALID_PARAM = -2147219767
DNC32_E_NO_AUTODETECT = -2147219766
DNC32_E_LISTEN_FAIL = -2147219765
DNC32_E_CONNECT_LOST = -2147219764
DNC_E_HOST_REJECTED = -2147219763
DNC_E_CLIENT_REJECTED = -2147219762
DNC_HRESULT = c_int  # enum

# values for enumeration 'DNC_DATA_UNIT_SELECT'
DNC_DATA_UNIT_SELECT_INCH = 0
DNC_DATA_UNIT_SELECT_METRIC = 1
DNC_DATA_UNIT_SELECT = c_int  # enum

# values for enumeration 'DNC_MODE'
DNC_MODE_LOCAL = 0
DNC_MODE_REMOTE = 1
DNC_MODE = c_int  # enum

# values for enumeration 'DNC_EXEC_MODE'
DNC_EXEC_MANUAL = 0
DNC_EXEC_MDI = 1
DNC_EXEC_RPF = 2
DNC_EXEC_SINGLESTEP = 3
DNC_EXEC_AUTOMATIC = 4
DNC_EXEC_OTHER = 5
DNC_EXEC_SIMULO_TURBO_DEPRECATED = 6
DNC_EXEC_HANDWHEEL = 7
DNC_EXEC_MODE = c_int  # enum

# values for enumeration 'DNC_DATA_UNIT'
DNC_DATA_UNIT_NONE = 0
DNC_DATA_UNIT_OTHER = 1
DNC_DATA_UNIT_SECOND = 2
DNC_DATA_UNIT_METER = 3
DNC_DATA_UNIT_METER_PER_SEC = 4
DNC_DATA_UNIT_METER_PER_SEC2 = 5
DNC_DATA_UNIT_METER_PER_SEC3 = 6
DNC_DATA_UNIT_METER_PER_SEC4 = 7
DNC_DATA_UNIT_DEGREE = 8
DNC_DATA_UNIT_DEGREE_PER_SEC = 9
DNC_DATA_UNIT_DEGREE_PER_SEC2 = 10
DNC_DATA_UNIT_DEGREE_PER_SEC3 = 11
DNC_DATA_UNIT_DEGREE_PER_SEC4 = 12
DNC_DATA_UNIT_PER_MINUTE = 13
DNC_DATA_UNIT_MILLIMETER = 14
DNC_DATA_UNIT_MILLIMETER_PER_MINUTE = 15
DNC_DATA_UNIT_MILLIMETER_PER_SEC2 = 16
DNC_DATA_UNIT_MILLIMETER_PER_SEC3 = 17
DNC_DATA_UNIT_INCH = 18
DNC_DATA_UNIT_INCH_PER_MINUTE = 19
DNC_DATA_UNIT_DEGREES_PER_MINUTE = 20
DNC_DATA_UNIT_VOLT = 21
DNC_DATA_UNIT_AMPERE = 22
DNC_DATA_UNIT = c_int  # enum

# values for enumeration 'DNC_EVT_PROGRAM'
DNC_PRG_EVT_STARTED = 0
DNC_PRG_EVT_STOPPED = 1
DNC_PRG_EVT_FINISHED = 2
DNC_PRG_EVT_CANCELED = 3
DNC_PRG_EVT_INTERRUPTED = 4
DNC_PRG_EVT_COMPLETED = 5
DNC_PRG_EVT_ERROR = 6
DNC_PRG_EVT_ERROR_CLEARED = 7
DNC_PRG_EVT_SELECTED = 8
DNC_PRG_EVT_SELECT_CLEARED = 9
DNC_EVT_PROGRAM = c_int  # enum

# values for enumeration 'DNC_TRIG_INTERFACE'
DNC_TRIG_INTERFACE_CONDITION = 0
DNC_TRIG_INTERFACE_SAMPLING = 1
DNC_TRIG_INTERFACE = c_int  # enum

# values for enumeration 'DNC_TRIG_SEQUENCE'
DNC_TRIG_SEQUENCE_NONE = 0
DNC_TRIG_SEQUENCE_AND = 1
DNC_TRIG_SEQUENCE_OR = 2
DNC_TRIG_SEQUENCE_AND_THEN = 3
DNC_TRIG_SEQUENCE = c_int  # enum

# values for enumeration 'DNC_SW_TYPE'
DNC_SW_TYPE_MC = 0
DNC_SW_TYPE_CC = 1
DNC_SW_TYPE_PLC = 2
DNC_SW_TYPE_MP_UIMS = 3
DNC_SW_TYPE_MP_ADMS = 4
DNC_SW_TYPE_TNC_MODEL = 5
DNC_SW_TYPE_TNC_SG = 6
DNC_SW_TYPE_TNC_DSP1 = 7
DNC_SW_TYPE_TNC_DSP2 = 8
DNC_SW_TYPE_TNC_DSP3 = 9
DNC_SW_TYPE_TNC_DSPSG1 = 10
DNC_SW_TYPE_TNC_DSPSG2 = 11
DNC_SW_TYPE_TNC_DSPSG3 = 12
DNC_SW_TYPE_TNC_ICTL1 = 13
DNC_SW_TYPE_TNC_ICTL2 = 14
DNC_SW_TYPE_TNC_ICTL3 = 15
DNC_SW_TYPE_TNC_OPT = 16
DNC_SW_TYPE_TNC_OTHER = 17
DNC_SW_TYPE_UNKNOWN = 18
DNC_SW_TYPE_NCKERN = 19
DNC_SW_TYPE_FCL = 20
DNC_SW_TYPE_SPLC = 21
DNC_SW_TYPE_FS_MCU = 22
DNC_SW_TYPE_FS_CCU = 23
DNC_SW_TYPE = c_int  # enum

# values for enumeration 'DNC_FILE_OBSERVE'
DNC_FILE_OBSERVE_ADD = 0
DNC_FILE_OBSERVE_REMOVE = 1
DNC_FILE_OBSERVE_REMOVE_ALL = 2
DNC_FILE_OBSERVE = c_int  # enum

# values for enumeration 'DNC_ATTRIBUTE_TYPE'
DNC_ATTRIBUTE_READONLY = 0
DNC_ATTRIBUTE_HIDDEN = 1
DNC_ATTRIBUTE_DIR = 2
DNC_ATTRIBUTE_SYSTEM = 3
DNC_ATTRIBUTE_MODIFIED = 4
DNC_ATTRIBUTE_LOCKED = 5
DNC_ATTRIBUTE_TYPE = c_int  # enum

# values for enumeration 'DNC_PROGRAMBREAKCONDITION_KIND'
DNC_PROGRAMBREAKCONDITION_KIND_DEFAULT = 0
DNC_PROGRAMBREAKCONDITION_KIND_FORCE_OPTIONAL_STOP = 1
DNC_PROGRAMBREAKCONDITION_KIND_IGNORE_PROGRAMMED_STOP = 2
DNC_PROGRAMBREAKCONDITION_KIND_ON_LINE = 3
DNC_PROGRAMBREAKCONDITION_KIND = c_int  # enum

# values for enumeration 'DNC_AXISTYPE'
DNC_AXISTYPE_MAIN_LINEAR = 0
DNC_AXISTYPE_MAIN_ROTARY = 1
DNC_AXISTYPE_AUX_LINEAR = 2
DNC_AXISTYPE_AUX_ROTARY = 3
DNC_AXISTYPE_SPINDLE = 4
DNC_AXISTYPE = c_int  # enum

# values for enumeration 'DNC_PLC_SIZE'
DNC_PLC_SIZE_BIT = 256
DNC_PLC_SIZE_BYTE = 512
DNC_PLC_SIZE_WORD = 1024
DNC_PLC_SIZE = c_int  # enum

# values for enumeration 'DNC_PLC_TYPE'
DNC_PLC_TYPE_MARKER = 1
DNC_PLC_TYPE = c_int  # enum



class IJHDataEntryPropertyList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataEntryPropertyList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{3A9203D6-6576-4524-8A41-ACDF550E3F25}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHDataEntryProperty': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def _get_property(self, kind: hints.Incomplete) -> 'IJHDataEntryProperty': ...
        property = hints.named_property('property', _get_property)


class IJHDataEntryProperty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataEntryProperty Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{B2D90A79-D539-49EB-A049-F2526EF2F2D0}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_kind(self) -> hints.Incomplete: ...
        kind = hints.normal_property(_get_kind)
        def _get_bstrDescription(self) -> hints.Incomplete: ...
        bstrDescription = hints.normal_property(_get_bstrDescription)
        def _get_varValue(self) -> hints.Incomplete: ...
        def _set_varValue(self, pvarValue: hints.Incomplete) -> hints.Hresult: ...
        varValue = hints.normal_property(_get_varValue, _set_varValue)
        def _get_bIsReadOnly(self) -> hints.Incomplete: ...
        bIsReadOnly = hints.normal_property(_get_bIsReadOnly)
        def _get_varValueType(self) -> hints.Incomplete: ...
        varValueType = hints.normal_property(_get_varValueType)



IJHDataEntryPropertyList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHDataEntryProperty object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty)),
            'ppDataEntryProperty',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [dispid(10), helpstring('retrieve DataEntry object of given kind'), 'propget'],
        HRESULT,
        'property',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty)),
            'ppDataEntryProperty',
        )
    ),
]

################################################################
# code template for IJHDataEntryPropertyList implementation
# class IJHDataEntryPropertyList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHDataEntryProperty object on the specified index in the list'
#         #return ppDataEntryProperty
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#
#     @property
#     def property(self, kind):
#         'retrieve DataEntry object of given kind'
#         #return ppDataEntryProperty
#


class IJHError(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHError Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{920A7DE5-4C52-4FCF-999B-3432EEE1F680}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetFirstError(self, pErrorGroup: hints.Incomplete, plErrorNumber: hints.Incomplete, pErrorClass: hints.Incomplete, pbstrError: hints.Incomplete, plChannel: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetNextError(self, pErrorGroup: hints.Incomplete, plErrorNumber: hints.Incomplete, pErrorClass: hints.Incomplete, pbstrError: hints.Incomplete, plChannel: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def ClearAllErrors(self) -> hints.Hresult: ...
        def GetErrorDescription(self, lErrorNumber: hints.Incomplete, lChannel: hints.Incomplete) -> hints.Incomplete: ...


class IJHError2(IJHError):
    """IJHError2 Interface (deprecated)"""
    _case_insensitive_ = True
    _iid_ = GUID('{3D773231-F37E-452D-9165-B6C727023E80}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def RegisterRemoteError(self, pErrorEntry: hints.Incomplete) -> hints.Hresult: ...
        def UnRegisterRemoteError(self, pErrorEntry: hints.Incomplete) -> hints.Hresult: ...
        def SetRemoteError(self, pErrorEntry: hints.Incomplete) -> hints.Hresult: ...


class IJHError3(IJHError2):
    """IJHError3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{20349305-3B36-4AFF-A756-375FE80E3BE7}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetErrorList(self) -> 'IJHErrorEntry2List': ...


IJHError._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieving the first active error')],
        HRESULT,
        'GetFirstError',
        (['in', 'out'], POINTER(VARIANT), 'pErrorGroup'),
        (['in', 'out'], POINTER(VARIANT), 'plErrorNumber'),
        (['in', 'out'], POINTER(VARIANT), 'pErrorClass'),
        (['in', 'out'], POINTER(VARIANT), 'pbstrError'),
        (['in', 'out'], POINTER(VARIANT), 'plChannel')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Retrieving the following active errors')],
        HRESULT,
        'GetNextError',
        (['in', 'out'], POINTER(VARIANT), 'pErrorGroup'),
        (['in', 'out'], POINTER(VARIANT), 'plErrorNumber'),
        (['in', 'out'], POINTER(VARIANT), 'pErrorClass'),
        (['in', 'out'], POINTER(VARIANT), 'pbstrError'),
        (['in', 'out'], POINTER(VARIANT), 'plChannel')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Clearing all active errors')],
        HRESULT,
        'ClearAllErrors',
    ),
    COMMETHOD(
        [dispid(4), helpstring('Retrieving the long description of an error')],
        HRESULT,
        'GetErrorDescription',
        (['in'], c_int, 'lErrorNumber'),
        (['in'], c_int, 'lChannel'),
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorDescription')
    ),
]

################################################################
# code template for IJHError implementation
# class IJHError_Impl(object):
#     def GetFirstError(self):
#         'Retrieving the first active error'
#         #return pErrorGroup, plErrorNumber, pErrorClass, pbstrError, plChannel
#
#     def GetNextError(self):
#         'Retrieving the following active errors'
#         #return pErrorGroup, plErrorNumber, pErrorClass, pbstrError, plChannel
#
#     def ClearAllErrors(self):
#         'Clearing all active errors'
#         #return 
#
#     def GetErrorDescription(self, lErrorNumber, lChannel):
#         'Retrieving the long description of an error'
#         #return pbstrErrorDescription
#


class IJHErrorEntry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHErrorEntry Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E573A664-CD3A-47D8-B8B7-7B6A703B2A56}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Group(self) -> hints.Incomplete: ...
        def _set_Group(self, pGroup: hints.Incomplete) -> hints.Hresult: ...
        Group = hints.normal_property(_get_Group, _set_Group)
        def _get_Number(self) -> hints.Incomplete: ...
        def _set_Number(self, plNumber: hints.Incomplete) -> hints.Hresult: ...
        Number = hints.normal_property(_get_Number, _set_Number)
        def _get_Class(self) -> hints.Incomplete: ...
        def _set_Class(self, pClass: hints.Incomplete) -> hints.Hresult: ...
        Class = hints.normal_property(_get_Class, _set_Class)
        def _get_Channel(self) -> hints.Incomplete: ...
        def _set_Channel(self, pChannelId: hints.Incomplete) -> hints.Hresult: ...
        Channel = hints.normal_property(_get_Channel, _set_Channel)
        def _get_Text(self) -> hints.Incomplete: ...
        def _set_Text(self, pbstrErrorText: hints.Incomplete) -> hints.Hresult: ...
        Text = hints.normal_property(_get_Text, _set_Text)
        def _get_Description(self) -> hints.Incomplete: ...
        def _set_Description(self, pbstrErrorDescription: hints.Incomplete) -> hints.Hresult: ...
        Description = hints.normal_property(_get_Description, _set_Description)
        def _get_timeStamp(self) -> hints.Incomplete: ...
        timeStamp = hints.normal_property(_get_timeStamp)


IJHError2._methods_ = [
    COMMETHOD(
        [dispid(5), helpstring('Register a new error with the control')],
        HRESULT,
        'RegisterRemoteError',
        (['in'], POINTER(IJHErrorEntry), 'pErrorEntry')
    ),
    COMMETHOD(
        [dispid(6), helpstring('Unregister a remote error that has been registered with the control previously')],
        HRESULT,
        'UnRegisterRemoteError',
        (['in'], POINTER(IJHErrorEntry), 'pErrorEntry')
    ),
    COMMETHOD(
        [dispid(7), helpstring('Fire a remote error that has been registered with the control previously')],
        HRESULT,
        'SetRemoteError',
        (['in'], POINTER(IJHErrorEntry), 'pErrorEntry')
    ),
]

################################################################
# code template for IJHError2 implementation
# class IJHError2_Impl(object):
#     def RegisterRemoteError(self, pErrorEntry):
#         'Register a new error with the control'
#         #return 
#
#     def UnRegisterRemoteError(self, pErrorEntry):
#         'Unregister a remote error that has been registered with the control previously'
#         #return 
#
#     def SetRemoteError(self, pErrorEntry):
#         'Fire a remote error that has been registered with the control previously'
#         #return 
#


class IJHErrorEntry2List(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHErrorEntry2List Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6D835790-81FF-4572-82CF-C44EBEF3A1FC}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, index: hints.Incomplete) -> 'IJHErrorEntry2': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def _get_entry(self, errorHandle: hints.Incomplete) -> 'IJHErrorEntry2': ...
        entry = hints.named_property('entry', _get_entry)
        def AddItem(self, pIJHErrorEntry: hints.Incomplete) -> hints.Hresult: ...
        def RemoveItem(self, index: hints.Incomplete) -> hints.Hresult: ...
        def RemoveEntry(self, a_pIJHErrorEntry: hints.Incomplete) -> hints.Hresult: ...


IJHError3._methods_ = [
    COMMETHOD(
        [dispid(8), helpstring('Retrieve the list of active errors')],
        HRESULT,
        'GetErrorList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHErrorEntry2List)),
            'a_ppErrorList',
        )
    ),
]

################################################################
# code template for IJHError3 implementation
# class IJHError3_Impl(object):
#     def GetErrorList(self):
#         'Retrieve the list of active errors'
#         #return a_ppErrorList
#


class _IJHDataAccessEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHDataAccessEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{7B901BF2-FC47-4F2D-BE20-F6DBD33F1804}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnData(self, lSubscribeHandle: hints.Incomplete, timeStamp: hints.Incomplete, varData: hints.Incomplete) -> hints.Hresult: ...


class _IJHDataAccessEvents2(_IJHDataAccessEvents):
    """_IJHDataAccessEvents2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{7BF533F3-04F8-495F-AAC7-BDA46BBA5686}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnData2(self, subscriptionHandle: hints.Incomplete, timeStamp: hints.Incomplete, pChangeList: hints.Incomplete) -> hints.Hresult: ...


_IJHDataAccessEvents._methods_ = [
    COMMETHOD(
        [helpstring('This event is fired, if the subscribed data has changed on the control or the timer has expired')],
        HRESULT,
        'OnData',
        (['in'], c_int, 'lSubscribeHandle'),
        (['in'], c_double, 'timeStamp'),
        (['in'], VARIANT, 'varData')
    ),
]

################################################################
# code template for _IJHDataAccessEvents implementation
# class _IJHDataAccessEvents_Impl(object):
#     def OnData(self, lSubscribeHandle, timeStamp, varData):
#         'This event is fired, if the subscribed data has changed on the control or the timer has expired'
#         #return 
#


class IJHDataEntry2List(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataEntry2List Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{1234899F-99DE-4E92-92F1-F707C0534934}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHDataEntry2': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def AddItem(self, pNewChild: hints.Incomplete) -> hints.Hresult: ...
        def RemoveItem(self, index: hints.Incomplete) -> hints.Hresult: ...
        def _get_child(self, bstrChildIdent: hints.Incomplete) -> 'IJHDataEntry2': ...
        child = hints.named_property('child', _get_child)


_IJHDataAccessEvents2._methods_ = [
    COMMETHOD(
        [helpstring('This event is fired, if the subscribed data has changed on the control or the timer has expired')],
        HRESULT,
        'OnData2',
        (['in'], c_int, 'subscriptionHandle'),
        (['in'], c_double, 'timeStamp'),
        (['in'], POINTER(IJHDataEntry2List), 'pChangeList')
    ),
]

################################################################
# code template for _IJHDataAccessEvents2 implementation
# class _IJHDataAccessEvents2_Impl(object):
#     def OnData2(self, subscriptionHandle, timeStamp, pChangeList):
#         'This event is fired, if the subscribed data has changed on the control or the timer has expired'
#         #return 
#


class JHTraceVariable(CoClass):
    """JHTraceVariable Class"""
    _reg_clsid_ = GUID('{E4B28184-F3A1-4FF9-BE01-C1B6EA595F16}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHTraceVariable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceVariable Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{EEB5BB8B-F7D0-4746-B4CB-68093A6C4614}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Clone(self) -> 'IJHTraceVariable': ...
        def _get_VariableId(self) -> hints.Incomplete: ...
        VariableId = hints.normal_property(_get_VariableId)
        def _get_bstrVariableName(self) -> hints.Incomplete: ...
        bstrVariableName = hints.normal_property(_get_bstrVariableName)
        def _get_VariableType(self) -> hints.Incomplete: ...
        VariableType = hints.normal_property(_get_VariableType)
        def _get_SourceType(self) -> hints.Incomplete: ...
        SourceType = hints.normal_property(_get_SourceType)
        def _get_dMaxSamplingRateInMsec(self) -> hints.Incomplete: ...
        dMaxSamplingRateInMsec = hints.normal_property(_get_dMaxSamplingRateInMsec)
        def _get_bstrDimension(self) -> hints.Incomplete: ...
        def _set_bstrDimension(self, pbstrDimension: hints.Incomplete) -> hints.Hresult: ...
        bstrDimension = hints.normal_property(_get_bstrDimension, _set_bstrDimension)
        def _get_Dimension(self) -> hints.Incomplete: ...
        def _set_Dimension(self, pDimension: hints.Incomplete) -> hints.Hresult: ...
        Dimension = hints.normal_property(_get_Dimension, _set_Dimension)
        def _get_lAxisId(self) -> hints.Incomplete: ...
        lAxisId = hints.normal_property(_get_lAxisId)
        def _get_lChannelId(self) -> hints.Incomplete: ...
        lChannelId = hints.normal_property(_get_lChannelId)
        def _get_bstrPath(self) -> hints.Incomplete: ...
        bstrPath = hints.normal_property(_get_bstrPath)
        def _get_bPlcPrePgmNotPost(self) -> hints.Incomplete: ...
        bPlcPrePgmNotPost = hints.normal_property(_get_bPlcPrePgmNotPost)
        def _get_dSamplingRateInMsec(self) -> hints.Incomplete: ...
        dSamplingRateInMsec = hints.normal_property(_get_dSamplingRateInMsec)
        def SetTypeNormal(self, dSamplingRateInMsec: hints.Incomplete) -> hints.Hresult: ...
        def SetTypeAxis(self, dSamplingRateInMsec: hints.Incomplete, axisId: hints.Incomplete) -> hints.Hresult: ...
        def SetTypeChannel(self, dSamplingRateInMsec: hints.Incomplete, channelId: hints.Incomplete) -> hints.Hresult: ...
        def SetTypePath(self, dSamplingRateInMsec: hints.Incomplete, bstrPath: hints.Incomplete) -> hints.Hresult: ...
        def SetTypePlcPath(self, dSamplingRateInMsec: hints.Incomplete, bstrPath: hints.Incomplete, bPlcPrePgmNotPost: hints.Incomplete) -> hints.Hresult: ...


class IJHLoggingInternal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHLoggingInternal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{C334F96A-5DC1-4686-B6AB-4F308A79B1ED}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Output(self, bstrConnectionName: hints.Incomplete) -> hints.Hresult: ...


JHTraceVariable._com_interfaces_ = [IJHTraceVariable, IJHLoggingInternal]


class IJHConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHConnection Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{9A4222BC-CD66-49F9-BECA-91EFF53EFF68}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Clone(self) -> 'IJHConnection': ...
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHConnectionProperty': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def _get_ConnectionProperty(self, conProp: hints.Incomplete) -> 'IJHConnectionProperty': ...
        ConnectionProperty = hints.named_property('ConnectionProperty', _get_ConnectionProperty)
        def _get_name(self) -> hints.Incomplete: ...
        def _set_name(self, pbstrConnectionName: hints.Incomplete) -> hints.Hresult: ...
        name = hints.normal_property(_get_name, _set_name)
        def _get_protocol(self) -> hints.Incomplete: ...
        protocol = hints.normal_property(_get_protocol)
        def _get_cncType(self) -> hints.Incomplete: ...
        cncType = hints.normal_property(_get_cncType)


class IJHConnection2(IJHConnection):
    """IJHConnection2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{BCB5C2C2-45AF-4357-A4DB-2FDFE6638975}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Configure(self, cncType: hints.Incomplete, protocol: hints.Incomplete) -> hints.Hresult: ...
        def _get_propertyValue(self, conProp: hints.Incomplete) -> hints.Incomplete: ...
        def _set_propertyValue(self, conProp: hints.Incomplete, pPropertyValue: hints.Incomplete) -> hints.Hresult: ...
        propertyValue = hints.named_property('propertyValue', _get_propertyValue, _set_propertyValue)


class IJHConnectionProperty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHConnectionProperty Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{37EF3631-3F91-4679-AE17-FA9AB7231588}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_value(self) -> hints.Incomplete: ...
        def _set_value(self, pValue: hints.Incomplete) -> hints.Hresult: ...
        value = hints.normal_property(_get_value, _set_value)
        def _get_kind(self) -> hints.Incomplete: ...
        kind = hints.normal_property(_get_kind)



IJHConnection._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Create a new Connection object with the properties of the current one')],
        HRESULT,
        'Clone',
        (['out', 'retval'], POINTER(POINTER(IJHConnection)), 'ppClone')
    ),
    COMMETHOD(
        [dispid(0), helpstring('JHConnectionProperty object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        ([], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHConnectionProperty)),
            'ppIJHConnectionProperty',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('Retrieves an enumerator over the properties'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppNewEnum')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Number of JHConnectionProperty objects (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'plCount')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property ConnectionProperty'), 'propget'],
        HRESULT,
        'ConnectionProperty',
        (['in'], DNC_CONNECTION_PROPERTY, 'conProp'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHConnectionProperty)),
            'ppIJHConnectionProperty',
        )
    ),
    COMMETHOD(
        [dispid(6), helpstring('property name'), 'propget'],
        HRESULT,
        'name',
        (['out', 'retval'], POINTER(BSTR), 'pbstrConnectionName')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property name'), 'propput'],
        HRESULT,
        'name',
        (['in'], BSTR, 'pbstrConnectionName')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property protocol'), 'propget'],
        HRESULT,
        'protocol',
        (['out', 'retval'], POINTER(DNC_PROTOCOL), 'pProtocol')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property cncType'), 'propget'],
        HRESULT,
        'cncType',
        (['out', 'retval'], POINTER(DNC_CNC_TYPE), 'pCncType')
    ),
]

################################################################
# code template for IJHConnection implementation
# class IJHConnection_Impl(object):
#     def Clone(self):
#         'Create a new Connection object with the properties of the current one'
#         #return ppClone
#
#     @property
#     def Item(self, lIndex):
#         'JHConnectionProperty object on the specified index in the list'
#         #return ppIJHConnectionProperty
#
#     @property
#     def _NewEnum(self):
#         'Retrieves an enumerator over the properties'
#         #return ppNewEnum
#
#     @property
#     def Count(self):
#         'Number of JHConnectionProperty objects (0 to count -1)'
#         #return plCount
#
#     @property
#     def ConnectionProperty(self, conProp):
#         'property ConnectionProperty'
#         #return ppIJHConnectionProperty
#
#     def _get(self):
#         'property name'
#         #return pbstrConnectionName
#     def _set(self, pbstrConnectionName):
#         'property name'
#     name = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def protocol(self):
#         'property protocol'
#         #return pProtocol
#
#     @property
#     def cncType(self):
#         'property cncType'
#         #return pCncType
#

IJHConnection2._methods_ = [
    COMMETHOD(
        [dispid(9), helpstring('Configure an empty Connection object for given CNC type and protocol.')],
        HRESULT,
        'Configure',
        (['in'], DNC_CNC_TYPE, 'cncType'),
        (['in'], DNC_PROTOCOL, 'protocol')
    ),
    COMMETHOD(
        [dispid(10), helpstring('return the value of an existing property in the property list'), 'propget'],
        HRESULT,
        'propertyValue',
        (['in'], DNC_CONNECTION_PROPERTY, 'conProp'),
        (['out', 'retval'], POINTER(VARIANT), 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(10), helpstring('return the value of an existing property in the property list'), 'propput'],
        HRESULT,
        'propertyValue',
        (['in'], DNC_CONNECTION_PROPERTY, 'conProp'),
        (['in'], VARIANT, 'pPropertyValue')
    ),
]

################################################################
# code template for IJHConnection2 implementation
# class IJHConnection2_Impl(object):
#     def Configure(self, cncType, protocol):
#         'Configure an empty Connection object for given CNC type and protocol.'
#         #return 
#
#     def _get(self, conProp):
#         'return the value of an existing property in the property list'
#         #return pPropertyValue
#     def _set(self, conProp, pPropertyValue):
#         'return the value of an existing property in the property list'
#     propertyValue = property(_get, _set, doc = _set.__doc__)
#


class IJHTriggerSampling(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTriggerSampling Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{CCB26291-E1BA-4969-945A-720AB99F9310}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SampleOnChange(self, lMultiplier: hints.Incomplete, dMinRepeat: hints.Incomplete) -> hints.Hresult: ...
        def SampleOnTimer(self, dInterval: hints.Incomplete) -> hints.Hresult: ...
        def SampleOnPlc(self, lMultiplier: hints.Incomplete, dMinRepeat: hints.Incomplete) -> hints.Hresult: ...
        def SampleOnIpo(self, lMultiplier: hints.Incomplete, dMinRepeat: hints.Incomplete) -> hints.Hresult: ...
        def SampleOnCcu(self, lMultiplier: hints.Incomplete, dMinRepeat: hints.Incomplete) -> hints.Hresult: ...
        def _get_sampleMode(self) -> hints.Incomplete: ...
        sampleMode = hints.normal_property(_get_sampleMode)
        def _get_lSampleMultiplier(self) -> hints.Incomplete: ...
        lSampleMultiplier = hints.normal_property(_get_lSampleMultiplier)
        def _get_dSampleInterval(self) -> hints.Incomplete: ...
        dSampleInterval = hints.normal_property(_get_dSampleInterval)
        def _get_dSampleMinRepeatInterval(self) -> hints.Incomplete: ...
        dSampleMinRepeatInterval = hints.normal_property(_get_dSampleMinRepeatInterval)



IJHTriggerSampling._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method SampleOnChange')],
        HRESULT,
        'SampleOnChange',
        (['in'], c_int, 'lMultiplier'),
        (['in'], c_double, 'dMinRepeat')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method SampleOnTimer')],
        HRESULT,
        'SampleOnTimer',
        (['in'], c_double, 'dInterval')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method SampleOnPlc')],
        HRESULT,
        'SampleOnPlc',
        (['in'], c_int, 'lMultiplier'),
        (['in'], c_double, 'dMinRepeat')
    ),
    COMMETHOD(
        [dispid(4), helpstring('method SampleOnIpo')],
        HRESULT,
        'SampleOnIpo',
        (['in'], c_int, 'lMultiplier'),
        (['in'], c_double, 'dMinRepeat')
    ),
    COMMETHOD(
        [dispid(5), helpstring('method SampleOnCcu')],
        HRESULT,
        'SampleOnCcu',
        (['in'], c_int, 'lMultiplier'),
        (['in'], c_double, 'dMinRepeat')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property sampleMode'), 'propget'],
        HRESULT,
        'sampleMode',
        (['out', 'retval'], POINTER(DNC_TRIG_SAMPLE_MODE), 'pSampleMode')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property lSampleMultiplier'), 'propget'],
        HRESULT,
        'lSampleMultiplier',
        (['out', 'retval'], POINTER(c_int), 'plSampleMultiplier')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property dSampleInterval'), 'propget'],
        HRESULT,
        'dSampleInterval',
        (['out', 'retval'], POINTER(c_double), 'pdSampleInterval')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property dSampleMinRepeatInterval'), 'propget'],
        HRESULT,
        'dSampleMinRepeatInterval',
        (['out', 'retval'], POINTER(c_double), 'pdSampleMinRepeatInterval')
    ),
]

################################################################
# code template for IJHTriggerSampling implementation
# class IJHTriggerSampling_Impl(object):
#     def SampleOnChange(self, lMultiplier, dMinRepeat):
#         'method SampleOnChange'
#         #return 
#
#     def SampleOnTimer(self, dInterval):
#         'method SampleOnTimer'
#         #return 
#
#     def SampleOnPlc(self, lMultiplier, dMinRepeat):
#         'method SampleOnPlc'
#         #return 
#
#     def SampleOnIpo(self, lMultiplier, dMinRepeat):
#         'method SampleOnIpo'
#         #return 
#
#     def SampleOnCcu(self, lMultiplier, dMinRepeat):
#         'method SampleOnCcu'
#         #return 
#
#     @property
#     def sampleMode(self):
#         'property sampleMode'
#         #return pSampleMode
#
#     @property
#     def lSampleMultiplier(self):
#         'property lSampleMultiplier'
#         #return plSampleMultiplier
#
#     @property
#     def dSampleInterval(self):
#         'property dSampleInterval'
#         #return pdSampleInterval
#
#     @property
#     def dSampleMinRepeatInterval(self):
#         'property dSampleMinRepeatInterval'
#         #return pdSampleMinRepeatInterval
#


class JHDataEntryPropertyEnum(CoClass):
    """JHDataEntryPropertyEnum Class"""
    _reg_clsid_ = GUID('{52A01838-6A5C-4BBF-8D3E-1D505F39E8ED}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryPropertyEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class _DJHFileSystemEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHFileSystemEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{89E4E1C9-880F-41FF-8A1E-442AF64BFC57}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnFileTransferEnd(self, lTransferJobId: hints.Incomplete, hErrorCode: hints.Incomplete) -> hints.Incomplete: ...
        def OnFileTransferProgress(self, lTransferJobId: hints.Incomplete, lBytesCopied: hints.Incomplete, lBytesTotal: hints.Incomplete) -> hints.Incomplete: ...
        def OnFileChanged(self, bstrFileName: hints.Incomplete) -> hints.Incomplete: ...


_DJHFileSystemEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('method OnFileTransferEnd')],
        HRESULT,
        'OnFileTransferEnd',
        (['in'], c_int, 'lTransferJobId'),
        (['in'], c_int, 'hErrorCode')
    ),
    DISPMETHOD(
        [dispid(2), helpstring('method OnFileTransferProgress')],
        HRESULT,
        'OnFileTransferProgress',
        (['in'], c_int, 'lTransferJobId'),
        (['in'], c_int, 'lBytesCopied'),
        (['in'], c_int, 'lBytesTotal')
    ),
    DISPMETHOD(
        [dispid(3), helpstring('method OnFileChanged')],
        HRESULT,
        'OnFileChanged',
        (['in'], BSTR, 'bstrFileName')
    ),
]


class JHProgramPositionEnum(CoClass):
    """JHProgramPositionEnum Class"""
    _reg_clsid_ = GUID('{25BDF036-1D9D-45E8-B01B-D0852B7BBAFE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHProgramPositionEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHSoftwareVersion(CoClass):
    """JHSoftwareVersion Class"""
    _reg_clsid_ = GUID('{CC67877E-F737-4F11-995C-48BC1A21A3CB}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHSoftwareVersion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHSoftwareVersion Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{296F76EA-7902-450F-A4EF-07AC8BC6B20F}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_softwareType(self) -> hints.Incomplete: ...
        softwareType = hints.normal_property(_get_softwareType)
        def _get_bstrSoftwareType(self) -> hints.Incomplete: ...
        bstrSoftwareType = hints.normal_property(_get_bstrSoftwareType)
        def _get_bstrIdentNr(self) -> hints.Incomplete: ...
        bstrIdentNr = hints.normal_property(_get_bstrIdentNr)
        def _get_bstrDescription(self) -> hints.Incomplete: ...
        bstrDescription = hints.normal_property(_get_bstrDescription)


JHSoftwareVersion._com_interfaces_ = [IJHSoftwareVersion, IJHLoggingInternal]


class _DJHTraceEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHTraceEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{9DB07D6E-4171-4269-A4E1-21A209174E36}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnTraceDataAvailable(self) -> hints.Incomplete: ...
        def OnTracingAborted(self) -> hints.Incomplete: ...


_DJHTraceEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Fire event OnTraceDataAvailable')],
        HRESULT,
        'OnTraceDataAvailable',
    ),
    DISPMETHOD(
        [dispid(2), helpstring('Fire event OnTracingAborted')],
        HRESULT,
        'OnTracingAborted',
    ),
]


class JHDataEntryProperty2Enum(CoClass):
    """JHDataEntryProperty2Enum Class"""
    _reg_clsid_ = GUID('{679387F1-ECA7-4F35-9A77-FFF383AE7183}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryProperty2Enum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class IJHAxesPositionStreaming(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAxesPositionStreaming Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{ABAF25C2-9264-452B-86B1-310054F6B2CF}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SetNotificationSampleLimit(self, lSamples: hints.Incomplete) -> hints.Hresult: ...
        def SetNotificationTimeLimit(self, dTimeInSec: hints.Incomplete) -> hints.Hresult: ...
        def SetFilterTcpDelta(self, dDelta: hints.Incomplete) -> hints.Hresult: ...
        def SetFilterAxesDelta(self, pDeltaList: hints.Incomplete) -> hints.Hresult: ...
        def GetSampleRate(self) -> hints.Incomplete: ...
        def StartStreaming(self, lChannel: hints.Incomplete) -> hints.Hresult: ...
        def StopStreaming(self, lChannel: hints.Incomplete) -> hints.Hresult: ...
        def GetAxesPositionSamples(self, ppsaTimeStamp: hints.Incomplete, ppsaLineNr: hints.Incomplete, ppsaFeedMode: hints.Incomplete, ppsaSpindleState: hints.Incomplete, ppsaMotionType: hints.Incomplete, ppsaIsBlockEndpoint: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, 'IJHAxisPositionListList']: ...
        def SetLoggingType(self, loggingType: hints.Incomplete) -> hints.Hresult: ...


class IJHAxesPositionStreaming2(IJHAxesPositionStreaming):
    """IJHAxesPositionStreaming2 Interface (deprecated)"""
    _case_insensitive_ = True
    _iid_ = GUID('{75052454-2A53-4F6C-BB0D-78E9C60CF121}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def ActivateSimulationTurboMode(self, bActivate: hints.Incomplete) -> hints.Hresult: ...


class IJHAxisPositionList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAxisPositionList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E6CAA2D5-13A7-4723-B4CC-D166624AF36D}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHAxisPosition': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def AddItem(self, pAxisPosition: hints.Incomplete) -> hints.Hresult: ...




class IJHAxisPositionListList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAxisPositionListList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{92851968-560E-4FBE-90FF-4EE7DE5B0B43}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHAxisPositionList': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)



IJHAxesPositionStreaming._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Specify the maximum number of samples that will be buffered before a notification event is fired, and the data can be retrieved')],
        HRESULT,
        'SetNotificationSampleLimit',
        (['in'], c_int, 'lSamples')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Specify the desired maximum time before the next notification event is fired, even if the buffer is not filled yet')],
        HRESULT,
        'SetNotificationTimeLimit',
        (['in'], c_double, 'dTimeInSec')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Specify a maximum vector length (3D delta way) for the TCP movement for storing a sample')],
        HRESULT,
        'SetFilterTcpDelta',
        (['in'], c_double, 'dDelta')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Specify a list of maximum delta ways per machine axis, for storing a sample')],
        HRESULT,
        'SetFilterAxesDelta',
        (['in'], POINTER(IJHAxisPositionList), 'pDeltaList')
    ),
    COMMETHOD(
        [dispid(5), helpstring('Retrieve the minimal sample rate that can be used to store samples in the buffer')],
        HRESULT,
        'GetSampleRate',
        (['out', 'retval'], POINTER(c_double), 'pdSampleRateInSec')
    ),
    COMMETHOD(
        [dispid(6), helpstring('Start the axis position data streaming during the processing of a part program.')],
        HRESULT,
        'StartStreaming',
        (['in'], c_int, 'lChannel')
    ),
    COMMETHOD(
        [dispid(7), helpstring('Stop the streaming of given channel')],
        HRESULT,
        'StopStreaming',
        (['in'], c_int, 'lChannel')
    ),
    COMMETHOD(
        [dispid(8), helpstring('Retrieve a list of AxisPosition samples')],
        HRESULT,
        'GetAxesPositionSamples',
        (['in', 'out'], POINTER(_midlSAFEARRAY(c_double)), 'ppsaTimeStamp'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(c_int)), 'ppsaLineNr'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(DNC_FEED_MODE)), 'ppsaFeedMode'),
        (
            ['in', 'out'],
            POINTER(_midlSAFEARRAY(DNC_SPINDLE_STATE)),
            'ppsaSpindleState',
        ),
        (
            ['in', 'out'],
            POINTER(_midlSAFEARRAY(DNC_POSSAMPLES_MOTION_TYPE)),
            'ppsaMotionType',
        ),
        (
            ['in', 'out'],
            POINTER(_midlSAFEARRAY(VARIANT_BOOL)),
            'ppsaIsBlockEndpoint',
        ),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionListList)),
            'ppAxisPositionListList',
        )
    ),
    COMMETHOD(
        [dispid(9), helpstring('method SetLoggingType')],
        HRESULT,
        'SetLoggingType',
        (['in'], DNC_POSSAMPLES_LOGGING_TYPE, 'loggingType')
    ),
]

################################################################
# code template for IJHAxesPositionStreaming implementation
# class IJHAxesPositionStreaming_Impl(object):
#     def SetNotificationSampleLimit(self, lSamples):
#         'Specify the maximum number of samples that will be buffered before a notification event is fired, and the data can be retrieved'
#         #return 
#
#     def SetNotificationTimeLimit(self, dTimeInSec):
#         'Specify the desired maximum time before the next notification event is fired, even if the buffer is not filled yet'
#         #return 
#
#     def SetFilterTcpDelta(self, dDelta):
#         'Specify a maximum vector length (3D delta way) for the TCP movement for storing a sample'
#         #return 
#
#     def SetFilterAxesDelta(self, pDeltaList):
#         'Specify a list of maximum delta ways per machine axis, for storing a sample'
#         #return 
#
#     def GetSampleRate(self):
#         'Retrieve the minimal sample rate that can be used to store samples in the buffer'
#         #return pdSampleRateInSec
#
#     def StartStreaming(self, lChannel):
#         'Start the axis position data streaming during the processing of a part program.'
#         #return 
#
#     def StopStreaming(self, lChannel):
#         'Stop the streaming of given channel'
#         #return 
#
#     def GetAxesPositionSamples(self):
#         'Retrieve a list of AxisPosition samples'
#         #return ppsaTimeStamp, ppsaLineNr, ppsaFeedMode, ppsaSpindleState, ppsaMotionType, ppsaIsBlockEndpoint, ppAxisPositionListList
#
#     def SetLoggingType(self, loggingType):
#         'method SetLoggingType'
#         #return 
#

IJHAxesPositionStreaming2._methods_ = [
    COMMETHOD(
        [dispid(10), helpstring('deprecated method ActivateSimulationTurboMode, use @link IJHVirtualMachine'), 'hidden'],
        HRESULT,
        'ActivateSimulationTurboMode',
        (['in'], VARIANT_BOOL, 'bActivate')
    ),
]

################################################################
# code template for IJHAxesPositionStreaming2 implementation
# class IJHAxesPositionStreaming2_Impl(object):
#     def ActivateSimulationTurboMode(self, bActivate):
#         'deprecated method ActivateSimulationTurboMode, use @link IJHVirtualMachine'
#         #return 
#


class IJHMachine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHMachine Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{1CBC6C93-E45A-41D5-9FD6-5EF572A8E106}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Connect(self, bstrConnectionName: hints.Incomplete) -> hints.Hresult: ...
        def Disconnect(self) -> hints.Hresult: ...
        def GetInterface(self, requestedInterface: hints.Incomplete) -> hints.Incomplete: ...
        def ConfigureConnection(self, mode: hints.Incomplete, pbstrConnectionName: hints.Incomplete) -> hints.Incomplete: ...
        def ListConnections(self) -> 'IJHConnectionList': ...
        def _get_connected(self) -> hints.Incomplete: ...
        connected = hints.normal_property(_get_connected)
        def _get_currentMachine(self) -> hints.Incomplete: ...
        currentMachine = hints.normal_property(_get_currentMachine)




class IJHConnectionList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHConnectionList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{72E5D2A3-1CBE-451F-A777-800060355605}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def AddConnection(self, pNewConnection: hints.Incomplete) -> hints.Hresult: ...
        def RemoveConnection(self, lIndex: hints.Incomplete) -> hints.Hresult: ...
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHConnection': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def _get_Connection(self, bstrConnectionName: hints.Incomplete) -> 'IJHConnection': ...
        Connection = hints.named_property('Connection', _get_Connection)
        def NewConnection(self, newType: hints.Incomplete, newProtocol: hints.Incomplete) -> 'IJHConnection': ...


IJHMachine._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Make a connection to the selected CNC')],
        HRESULT,
        'Connect',
        (['in'], BSTR, 'bstrConnectionName')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Terminates the active connection')],
        HRESULT,
        'Disconnect',
    ),
    COMMETHOD(
        [dispid(3), helpstring('Retrieves a kind of interface that can be accessed')],
        HRESULT,
        'GetInterface',
        (['in'], DNC_INTERFACE_OBJECT, 'requestedInterface'),
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppDefaultInterface')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Starts a dialog for modifying connections')],
        HRESULT,
        'ConfigureConnection',
        (['in'], DNC_CONFIGURE_MODE, 'mode'),
        (['in', 'out'], POINTER(VARIANT), 'pbstrConnectionName')
    ),
    COMMETHOD(
        [dispid(5), helpstring('Retrieves the list of configured connections to machines')],
        HRESULT,
        'ListConnections',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHConnectionList)),
            'ppConnectionList',
        )
    ),
    COMMETHOD(
        [dispid(6), helpstring('Connection state property'), 'propget'],
        HRESULT,
        'connected',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pVal')
    ),
    COMMETHOD(
        [dispid(7), helpstring('The connection name of the CNC currently connected'), 'propget'],
        HRESULT,
        'currentMachine',
        (['out', 'retval'], POINTER(BSTR), 'pVal')
    ),
]

################################################################
# code template for IJHMachine implementation
# class IJHMachine_Impl(object):
#     def Connect(self, bstrConnectionName):
#         'Make a connection to the selected CNC'
#         #return 
#
#     def Disconnect(self):
#         'Terminates the active connection'
#         #return 
#
#     def GetInterface(self, requestedInterface):
#         'Retrieves a kind of interface that can be accessed'
#         #return ppDefaultInterface
#
#     def ConfigureConnection(self, mode):
#         'Starts a dialog for modifying connections'
#         #return pbstrConnectionName
#
#     def ListConnections(self):
#         'Retrieves the list of configured connections to machines'
#         #return ppConnectionList
#
#     @property
#     def connected(self):
#         'Connection state property'
#         #return pVal
#
#     @property
#     def currentMachine(self):
#         'The connection name of the CNC currently connected'
#         #return pVal
#


class JHTriggerList(CoClass):
    """JHTriggerList Class"""
    _reg_clsid_ = GUID('{D6B68DF0-08FE-44D4-AFAD-6BE495D29947}')
    _idlflags_ = ['hidden']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHTriggerList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTriggerList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{0F09D0A9-2A28-410F-80FE-3D82121694E0}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHTrigger': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def AddItem(self, pTrigger: hints.Incomplete) -> hints.Hresult: ...


JHTriggerList._com_interfaces_ = [IJHTriggerList, IJHLoggingInternal]


class _DJHDataAccessEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHDataAccessEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{5FF982C8-59D8-4F50-AF77-B7C71F4C5D06}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnData(self, lSubscribeHandle: hints.Incomplete, timeStamp: hints.Incomplete, varData: hints.Incomplete) -> hints.Incomplete: ...
        def OnData2(self, subscriptionHandle: hints.Incomplete, timeStamp: hints.Incomplete, pChangeList: hints.Incomplete) -> hints.Incomplete: ...


_DJHDataAccessEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('method OnData')],
        HRESULT,
        'OnData',
        (['in'], c_int, 'lSubscribeHandle'),
        (['in'], c_double, 'timeStamp'),
        (['in'], VARIANT, 'varData')
    ),
    DISPMETHOD(
        [dispid(2), helpstring('method OnData2')],
        HRESULT,
        'OnData2',
        (['in'], DNC_HANDLE, 'subscriptionHandle'),
        (['in'], c_double, 'timeStamp'),
        (['in'], POINTER(IJHDataEntry2List), 'pChangeList')
    ),
]


class IJHErrorEntry2(IJHErrorEntry):
    """IJHErrorEntry2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{0CE3D73D-8CBC-45BA-BAA1-E65BA7A67364}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Handle(self) -> hints.Incomplete: ...
        def _set_Handle(self, plHandle: hints.Incomplete) -> hints.Hresult: ...
        Handle = hints.normal_property(_get_Handle, _set_Handle)
        def _get_Location(self) -> hints.Incomplete: ...
        def _set_Location(self, a_pLocation: hints.Incomplete) -> hints.Hresult: ...
        Location = hints.normal_property(_get_Location, _set_Location)
        def _get_Cause(self) -> hints.Incomplete: ...
        def _set_Cause(self, pbstrErrorCause: hints.Incomplete) -> hints.Hresult: ...
        Cause = hints.normal_property(_get_Cause, _set_Cause)
        def _get_Action(self) -> hints.Incomplete: ...
        def _set_Action(self, pbstrErrorAction: hints.Incomplete) -> hints.Hresult: ...
        Action = hints.normal_property(_get_Action, _set_Action)
        def _get_Internals(self) -> hints.Incomplete: ...
        def _set_Internals(self, pbstrErrorInternals: hints.Incomplete) -> hints.Hresult: ...
        Internals = hints.normal_property(_get_Internals, _set_Internals)
        def _get_NumberAsText(self) -> hints.Incomplete: ...
        NumberAsText = hints.normal_property(_get_NumberAsText)
        def Clear(self) -> hints.Hresult: ...



IJHErrorEntry._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property group'), 'propget'],
        HRESULT,
        'Group',
        (['out', 'retval'], POINTER(DNC_ERROR_GROUP), 'pGroup')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property group'), 'propput'],
        HRESULT,
        'Group',
        (['in'], DNC_ERROR_GROUP, 'pGroup')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property number'), 'propget'],
        HRESULT,
        'Number',
        (['out', 'retval'], POINTER(c_int), 'plNumber')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property number'), 'propput'],
        HRESULT,
        'Number',
        (['in'], c_int, 'plNumber')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property class'), 'propget'],
        HRESULT,
        'Class',
        (['out', 'retval'], POINTER(DNC_ERROR_CLASS), 'pClass')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property class'), 'propput'],
        HRESULT,
        'Class',
        (['in'], DNC_ERROR_CLASS, 'pClass')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property channel'), 'propget'],
        HRESULT,
        'Channel',
        (['out', 'retval'], POINTER(c_int), 'pChannelId')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property channel'), 'propput'],
        HRESULT,
        'Channel',
        (['in'], c_int, 'pChannelId')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property errorText'), 'propget'],
        HRESULT,
        'Text',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorText')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property errorText'), 'propput'],
        HRESULT,
        'Text',
        (['in'], BSTR, 'pbstrErrorText')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property errorDescription'), 'propget'],
        HRESULT,
        'Description',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorDescription')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property errorDescription'), 'propput'],
        HRESULT,
        'Description',
        (['in'], BSTR, 'pbstrErrorDescription')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property TimeStamp'), 'propget'],
        HRESULT,
        'timeStamp',
        (['out', 'retval'], POINTER(c_double), 'pTimeStamp')
    ),
]

################################################################
# code template for IJHErrorEntry implementation
# class IJHErrorEntry_Impl(object):
#     def _get(self):
#         'property group'
#         #return pGroup
#     def _set(self, pGroup):
#         'property group'
#     Group = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property number'
#         #return plNumber
#     def _set(self, plNumber):
#         'property number'
#     Number = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property class'
#         #return pClass
#     def _set(self, pClass):
#         'property class'
#     Class = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property channel'
#         #return pChannelId
#     def _set(self, pChannelId):
#         'property channel'
#     Channel = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property errorText'
#         #return pbstrErrorText
#     def _set(self, pbstrErrorText):
#         'property errorText'
#     Text = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property errorDescription'
#         #return pbstrErrorDescription
#     def _set(self, pbstrErrorDescription):
#         'property errorDescription'
#     Description = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def timeStamp(self):
#         'property TimeStamp'
#         #return pTimeStamp
#

IJHErrorEntry2._methods_ = [
    COMMETHOD(
        [dispid(8), helpstring('property handle'), 'propget'],
        HRESULT,
        'Handle',
        (['out', 'retval'], POINTER(c_int), 'plHandle')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property handle'), 'propput'],
        HRESULT,
        'Handle',
        (['in'], c_int, 'plHandle')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property location'), 'propget'],
        HRESULT,
        'Location',
        (['out', 'retval'], POINTER(DNC_ERROR_LOCATION), 'a_pLocation')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property location'), 'propput'],
        HRESULT,
        'Location',
        (['in'], DNC_ERROR_LOCATION, 'a_pLocation')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property errorCause'), 'propget'],
        HRESULT,
        'Cause',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorCause')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property errorCause'), 'propput'],
        HRESULT,
        'Cause',
        (['in'], BSTR, 'pbstrErrorCause')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property errorAction'), 'propget'],
        HRESULT,
        'Action',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorAction')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property errorAction'), 'propput'],
        HRESULT,
        'Action',
        (['in'], BSTR, 'pbstrErrorAction')
    ),
    COMMETHOD(
        [dispid(12), helpstring('property errorInternals'), 'propget'],
        HRESULT,
        'Internals',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorInternals')
    ),
    COMMETHOD(
        [dispid(12), helpstring('property errorInternals'), 'propput'],
        HRESULT,
        'Internals',
        (['in'], BSTR, 'pbstrErrorInternals')
    ),
    COMMETHOD(
        [dispid(13), helpstring('property NumberAsText'), 'propget'],
        HRESULT,
        'NumberAsText',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorNumber')
    ),
    COMMETHOD(
        [dispid(14), helpstring('method Clear this error')],
        HRESULT,
        'Clear',
    ),
]

################################################################
# code template for IJHErrorEntry2 implementation
# class IJHErrorEntry2_Impl(object):
#     def _get(self):
#         'property handle'
#         #return plHandle
#     def _set(self, plHandle):
#         'property handle'
#     Handle = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property location'
#         #return a_pLocation
#     def _set(self, a_pLocation):
#         'property location'
#     Location = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property errorCause'
#         #return pbstrErrorCause
#     def _set(self, pbstrErrorCause):
#         'property errorCause'
#     Cause = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property errorAction'
#         #return pbstrErrorAction
#     def _set(self, pbstrErrorAction):
#         'property errorAction'
#     Action = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property errorInternals'
#         #return pbstrErrorInternals
#     def _set(self, pbstrErrorInternals):
#         'property errorInternals'
#     Internals = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def NumberAsText(self):
#         'property NumberAsText'
#         #return pbstrErrorNumber
#
#     def Clear(self):
#         'method Clear this error'
#         #return 
#


class IJHConnection3(IJHConnection2):
    """IJHConnection3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E4DD9EF8-4FA6-4929-B86A-520254CED8C8}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_bstrDefaultKeysDir(self) -> hints.Incomplete: ...
        bstrDefaultKeysDir = hints.normal_property(_get_bstrDefaultKeysDir)
        def GenerateKeyPairToProperties(self, bstrKeysDir: hints.Incomplete, mayOverwrite: hints.Incomplete, varbstrPrivateKeyPassword: hints.Incomplete = ...) -> hints.Hresult: ...
        def GenerateKeyPairToPropertiesEx(self, bstrKeysDir: hints.Incomplete, mayOverwrite: hints.Incomplete, bstrPrivateKeyPassword: hints.Incomplete, bstrPrivateKeyName: hints.Incomplete) -> hints.Hresult: ...
        def GenerateKeyPairFromProperties(self, mayOverwrite: hints.Incomplete) -> hints.Hresult: ...
        def GetHostKeyToProperty(self) -> hints.Hresult: ...
        def RegisterKeyFromProperties(self) -> hints.Hresult: ...


IJHConnection3._methods_ = [
    COMMETHOD(
        [dispid(11), helpstring('default SSH keys storage location'), 'propget'],
        HRESULT,
        'bstrDefaultKeysDir',
        (['out', 'retval'], POINTER(BSTR), 'pbstrDir')
    ),
    COMMETHOD(
        [dispid(12), helpstring('Create a new SSH key pair with preset name and store results')],
        HRESULT,
        'GenerateKeyPairToProperties',
        (['in'], BSTR, 'bstrKeysDir'),
        (['in'], c_int, 'mayOverwrite'),
        (['in', 'optional'], VARIANT, 'varbstrPrivateKeyPassword')
    ),
    COMMETHOD(
        [dispid(13), helpstring('Create a new SSH key pair and store results')],
        HRESULT,
        'GenerateKeyPairToPropertiesEx',
        (['in'], BSTR, 'bstrKeysDir'),
        (['in'], c_int, 'mayOverwrite'),
        (['in'], BSTR, 'bstrPrivateKeyPassword'),
        (['in'], BSTR, 'bstrPrivateKeyName')
    ),
    COMMETHOD(
        [dispid(14), helpstring('Create a new SSH key pair based on the actual properties')],
        HRESULT,
        'GenerateKeyPairFromProperties',
        (['in'], c_int, 'mayOverwrite')
    ),
    COMMETHOD(
        [dispid(15), helpstring('Read the host key from the remote host and store result')],
        HRESULT,
        'GetHostKeyToProperty',
    ),
    COMMETHOD(
        [dispid(16), helpstring('Transfer to and register the public key on the remote host for the defined user')],
        HRESULT,
        'RegisterKeyFromProperties',
    ),
]

################################################################
# code template for IJHConnection3 implementation
# class IJHConnection3_Impl(object):
#     @property
#     def bstrDefaultKeysDir(self):
#         'default SSH keys storage location'
#         #return pbstrDir
#
#     def GenerateKeyPairToProperties(self, bstrKeysDir, mayOverwrite, varbstrPrivateKeyPassword):
#         'Create a new SSH key pair with preset name and store results'
#         #return 
#
#     def GenerateKeyPairToPropertiesEx(self, bstrKeysDir, mayOverwrite, bstrPrivateKeyPassword, bstrPrivateKeyName):
#         'Create a new SSH key pair and store results'
#         #return 
#
#     def GenerateKeyPairFromProperties(self, mayOverwrite):
#         'Create a new SSH key pair based on the actual properties'
#         #return 
#
#     def GetHostKeyToProperty(self):
#         'Read the host key from the remote host and store result'
#         #return 
#
#     def RegisterKeyFromProperties(self):
#         'Transfer to and register the public key on the remote host for the defined user'
#         #return 
#


class JHTraceChannelList(CoClass):
    """JHTraceChannelList Class"""
    _reg_clsid_ = GUID('{F8AA9211-7A5A-4798-AD89-5965EB9BBF32}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHTraceChannelList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceChannelList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{68333118-17BC-4FFC-A237-8D718D138E51}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHTraceChannel': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def GetChannel(self, traceChannelId: hints.Incomplete) -> 'IJHTraceChannel': ...


JHTraceChannelList._com_interfaces_ = [IJHTraceChannelList, IJHLoggingInternal]

IJHErrorEntry2List._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHErrorEntry object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'index'),
        (['out', 'retval'], POINTER(POINTER(IJHErrorEntry2)), 'ppErrorEntry')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pNrOfElements')
    ),
    COMMETHOD(
        [dispid(2), helpstring('retrieve ErrorEntry object that matches the handle'), 'propget'],
        HRESULT,
        'entry',
        (['in'], c_int, 'errorHandle'),
        (['out', 'retval'], POINTER(POINTER(IJHErrorEntry2)), 'ppIJHErrorEntry')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method AddItem')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHErrorEntry2), 'pIJHErrorEntry')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Remove the JHErrorEntry at given index from the list.')],
        HRESULT,
        'RemoveItem',
        (['in'], c_int, 'index')
    ),
    COMMETHOD(
        [dispid(5), helpstring('Remove the given JHErrorEntry from the list.')],
        HRESULT,
        'RemoveEntry',
        (['in'], POINTER(IJHErrorEntry2), 'a_pIJHErrorEntry')
    ),
]

################################################################
# code template for IJHErrorEntry2List implementation
# class IJHErrorEntry2List_Impl(object):
#     @property
#     def Item(self, index):
#         'JHErrorEntry object on the specified index in the list'
#         #return ppErrorEntry
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pNrOfElements
#
#     @property
#     def entry(self, errorHandle):
#         'retrieve ErrorEntry object that matches the handle'
#         #return ppIJHErrorEntry
#
#     def AddItem(self, pIJHErrorEntry):
#         'method AddItem'
#         #return 
#
#     def RemoveItem(self, index):
#         'Remove the JHErrorEntry at given index from the list.'
#         #return 
#
#     def RemoveEntry(self, a_pIJHErrorEntry):
#         'Remove the given JHErrorEntry from the list.'
#         #return 
#


class TNCTable(CoClass):
    """TNCTable Class"""
    _reg_clsid_ = GUID('{FC757C15-56D6-43D3-9AD3-6451FB107EB1}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class ITNCTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """ITNCTable Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{5618A9C2-EF92-4C89-A3D2-69461FCC7653}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def DeleteRecord(self, bstrTableName: hints.Incomplete, bstrSQLQuery: hints.Incomplete) -> hints.Hresult: ...
        def GetTableInfo(self, bstrTableName: hints.Incomplete, bstrColumnTitles: hints.Incomplete, lColumnPos: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def ReceiveTableLines(self, bstrTableName: hints.Incomplete, bstrSQLQuery: hints.Incomplete, pbstrLines: hints.Incomplete) -> hints.Incomplete: ...
        def TransmitTablePart(self, bstrSourceFileName: hints.Incomplete, bstrDestTableName: hints.Incomplete) -> hints.Hresult: ...


TNCTable._com_interfaces_ = [ITNCTable]


class JHTriggerEnum(CoClass):
    """JHTriggerEnum Class"""
    _reg_clsid_ = GUID('{98D4BA75-D4A5-400D-800B-9E11F3E48DBE}')
    _idlflags_ = ['hidden']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTriggerEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class _IJHMachineEvents2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHMachineEvents2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F2BBDFA1-5448-4CA2-98ED-891FBD86D391}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnStateChanged(self, event: hints.Incomplete) -> hints.Hresult: ...


class _IJHMachineEvents2Internal(_IJHMachineEvents2):
    """_IJHMachineEvents2Internal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E528F03F-F6B0-4437-B962-6FD5E2E9BD1E}')
    _idlflags_ = ['hidden']



_IJHMachineEvents2._methods_ = [
    COMMETHOD(
        [helpstring('Connection state changed event')],
        HRESULT,
        'OnStateChanged',
        (['in'], DNC_EVT_STATE, 'event')
    ),
]

################################################################
# code template for _IJHMachineEvents2 implementation
# class _IJHMachineEvents2_Impl(object):
#     def OnStateChanged(self, event):
#         'Connection state changed event'
#         #return 
#

_IJHMachineEvents2Internal._methods_ = [
]

################################################################
# code template for _IJHMachineEvents2Internal implementation
# class _IJHMachineEvents2Internal_Impl(object):


class IJHErrorInternal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHErrorInternal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{969CB72E-46DD-4079-A739-754335A9DFCC}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _GetDescription(self, errorNumber: hints.Incomplete, errorChannel: hints.Incomplete, errorGroup: hints.Incomplete, errorClass: hints.Incomplete, errorTimeStamp: hints.Incomplete) -> hints.Incomplete: ...


class IJHErrorInternal2(IJHErrorInternal):
    """IJHErrorInternal2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{D3E8BDFE-2658-42B5-8646-610C72244A43}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _GetDescription2(self, errorHandle: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def _Clear(self, errorHandle: hints.Incomplete) -> hints.Hresult: ...


IJHErrorInternal._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieving the long description of an error')],
        HRESULT,
        '_GetDescription',
        (['in'], c_int, 'errorNumber'),
        (['in'], c_int, 'errorChannel'),
        (['in'], DNC_ERROR_GROUP, 'errorGroup'),
        (['in'], DNC_ERROR_CLASS, 'errorClass'),
        (['in'], c_double, 'errorTimeStamp'),
        (['out', 'retval'], POINTER(BSTR), 'pbstrDescription')
    ),
]

################################################################
# code template for IJHErrorInternal implementation
# class IJHErrorInternal_Impl(object):
#     def _GetDescription(self, errorNumber, errorChannel, errorGroup, errorClass, errorTimeStamp):
#         'Retrieving the long description of an error'
#         #return pbstrDescription
#

IJHErrorInternal2._methods_ = [
    COMMETHOD(
        [dispid(2), helpstring('Retrieving the detailed description of an error')],
        HRESULT,
        '_GetDescription2',
        (['in'], c_int, 'errorHandle'),
        (['out'], POINTER(BSTR), 'pbstrCause'),
        (['out'], POINTER(BSTR), 'pbstrAction'),
        (['out'], POINTER(BSTR), 'pbstrInternal')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Clear the error with given handle')],
        HRESULT,
        '_Clear',
        (['in'], c_int, 'errorHandle')
    ),
]

################################################################
# code template for IJHErrorInternal2 implementation
# class IJHErrorInternal2_Impl(object):
#     def _GetDescription2(self, errorHandle):
#         'Retrieving the detailed description of an error'
#         #return pbstrCause, pbstrAction, pbstrInternal
#
#     def _Clear(self, errorHandle):
#         'Clear the error with given handle'
#         #return 
#


class JHCutterLocationList(CoClass):
    """JHCutterLocationList Class"""
    _reg_clsid_ = GUID('{E98FCAA8-B0AD-4895-8762-D59300CE7A47}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHCutterLocationList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHCutterLocationList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{40604A5D-0DD2-482E-8DA6-F9F540E9AD91}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHCutterLocation': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


JHCutterLocationList._com_interfaces_ = [IJHCutterLocationList, IJHLoggingInternal]


class JHSoftwareVersionEnum(CoClass):
    """JHSoftwareVersionEnum Class"""
    _reg_clsid_ = GUID('{319BB74B-0C02-4787-BF6F-1FA63FD27FBB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHSoftwareVersionEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHAxisPositionListList(CoClass):
    """JHAxisPositionListList Class"""
    _reg_clsid_ = GUID('{B8269DE6-F56F-4D55-A09C-89CC84091153}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAxisPositionListList._com_interfaces_ = [IJHAxisPositionListList, IJHLoggingInternal]


class JHMachineInProcessEvents2(CoClass):
    """JHMachineInProcessEvents2 Class"""
    _reg_clsid_ = GUID('{AB41DF21-0C39-4D9E-A789-6EE01084BD9B}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IEventObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IEventObject Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{1DCA9382-A0B5-4BD4-9977-7703CCF1623B}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Init(self, pIUnknownOfCncObject: hints.Incomplete) -> hints.Hresult: ...
        def PutConnectionName(self, connectionName: hints.Incomplete) -> hints.Hresult: ...


class _DJHMachineEvents2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHMachineEvents2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{C42C8077-BA2F-44CA-8229-9FA5064185E7}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnStateChanged(self, event: hints.Incomplete) -> hints.Incomplete: ...


JHMachineInProcessEvents2._com_interfaces_ = [IEventObject]
JHMachineInProcessEvents2._outgoing_interfaces_ = [_DJHMachineEvents2, _IJHMachineEvents2]


class _IJHAxesPositionStreamingEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHAxesPositionStreamingEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{70676A76-4993-43F4-95AB-81363DDB6C6E}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnAxesPositionsAvailable(self) -> hints.Hresult: ...


_IJHAxesPositionStreamingEvents._methods_ = [
    COMMETHOD(
        [helpstring('This event is fired if one or more of the conditions of the StartStreaming method are true')],
        HRESULT,
        'OnAxesPositionsAvailable',
    ),
]

################################################################
# code template for _IJHAxesPositionStreamingEvents implementation
# class _IJHAxesPositionStreamingEvents_Impl(object):
#     def OnAxesPositionsAvailable(self):
#         'This event is fired if one or more of the conditions of the StartStreaming method are true'
#         #return 
#

IJHConnectionList._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Adds a new Connection object to the connection list')],
        HRESULT,
        'AddConnection',
        (['in'], POINTER(IJHConnection), 'pNewConnection')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Remove an existing Connection object from the connection list')],
        HRESULT,
        'RemoveConnection',
        (['in'], c_int, 'lIndex')
    ),
    COMMETHOD(
        [dispid(0), helpstring('returns the Connection object at the given index from the connection list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHConnection)), 'ppConnection')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('returns an enumeration object'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppNewEnum')
    ),
    COMMETHOD(
        [dispid(3), helpstring('returns the number of objects in the connection list'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'plCount')
    ),
    COMMETHOD(
        [dispid(5), helpstring('returns the Connection object with the given name from the connection list'), 'propget'],
        HRESULT,
        'Connection',
        (['in'], BSTR, 'bstrConnectionName'),
        (['out', 'retval'], POINTER(POINTER(IJHConnection)), 'ppConnection')
    ),
    COMMETHOD(
        [dispid(6), helpstring('method NewConnection')],
        HRESULT,
        'NewConnection',
        (['in'], DNC_CNC_TYPE, 'newType'),
        (['in'], DNC_PROTOCOL, 'newProtocol'),
        (['out', 'retval'], POINTER(POINTER(IJHConnection)), 'ppINewConnection')
    ),
]

################################################################
# code template for IJHConnectionList implementation
# class IJHConnectionList_Impl(object):
#     def AddConnection(self, pNewConnection):
#         'Adds a new Connection object to the connection list'
#         #return 
#
#     def RemoveConnection(self, lIndex):
#         'Remove an existing Connection object from the connection list'
#         #return 
#
#     @property
#     def Item(self, lIndex):
#         'returns the Connection object at the given index from the connection list'
#         #return ppConnection
#
#     @property
#     def _NewEnum(self):
#         'returns an enumeration object'
#         #return ppNewEnum
#
#     @property
#     def Count(self):
#         'returns the number of objects in the connection list'
#         #return plCount
#
#     @property
#     def Connection(self, bstrConnectionName):
#         'returns the Connection object with the given name from the connection list'
#         #return ppConnection
#
#     def NewConnection(self, newType, newProtocol):
#         'method NewConnection'
#         #return ppINewConnection
#


class JHTraceChannelEnum(CoClass):
    """JHTraceChannelEnum Class"""
    _reg_clsid_ = GUID('{ED77E667-83ED-4145-B95C-75270B9EE850}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceChannelEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHConfiguration(CoClass):
    """JHConfiguration Class"""
    _reg_clsid_ = GUID('{9B4FCE79-5395-4C03-BFB4-C1C327132FF8}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHConfiguration Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{7C52B717-7AA2-4C20-A3BC-C6DE77C34C26}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetAxesInfo(self) -> 'IJHAxisInfoList': ...
        def GetChannelInfo(self) -> 'IJHChannelInfoList': ...


JHConfiguration._com_interfaces_ = [IJHConfiguration]


class _DJHRemoteErrorEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHRemoteErrorEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{77F61218-C4AB-4FAC-BB65-59D84F4AD58B}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnRemoveRequest(self, pRemoteErrorEntry: hints.Incomplete) -> hints.Incomplete: ...


class IJHRemoteErrorEntry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHRemoteErrorEntry Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6CF60643-F645-475D-B9D2-9A6CCDA01AB9}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Number(self) -> hints.Incomplete: ...
        def _set_Number(self, plNumber: hints.Incomplete) -> hints.Hresult: ...
        Number = hints.normal_property(_get_Number, _set_Number)
        def _get_Class(self) -> hints.Incomplete: ...
        def _set_Class(self, pClass: hints.Incomplete) -> hints.Hresult: ...
        Class = hints.normal_property(_get_Class, _set_Class)
        def _get_Group(self) -> hints.Incomplete: ...
        def _set_Group(self, pGroup: hints.Incomplete) -> hints.Hresult: ...
        Group = hints.normal_property(_get_Group, _set_Group)
        def _get_Text(self) -> hints.Incomplete: ...
        def _set_Text(self, pbstrErrorText: hints.Incomplete) -> hints.Hresult: ...
        Text = hints.normal_property(_get_Text, _set_Text)
        def _get_Channel(self) -> hints.Incomplete: ...
        def _set_Channel(self, plChannelId: hints.Incomplete) -> hints.Hresult: ...
        Channel = hints.normal_property(_get_Channel, _set_Channel)
        def _get_SourceFile(self) -> hints.Incomplete: ...
        def _set_SourceFile(self, pbstrSourceFile: hints.Incomplete) -> hints.Hresult: ...
        SourceFile = hints.normal_property(_get_SourceFile, _set_SourceFile)
        def _get_SourceLineNr(self) -> hints.Incomplete: ...
        def _set_SourceLineNr(self, plSourceLineNr: hints.Incomplete) -> hints.Hresult: ...
        SourceLineNr = hints.normal_property(_get_SourceLineNr, _set_SourceLineNr)
        def _get_CallStack(self) -> hints.Incomplete: ...
        def _set_CallStack(self, pbstrCallStack: hints.Incomplete) -> hints.Hresult: ...
        CallStack = hints.normal_property(_get_CallStack, _set_CallStack)
        def _get_ClientShortName(self) -> hints.Incomplete: ...
        def _set_ClientShortName(self, pbstrClientShortName: hints.Incomplete) -> hints.Hresult: ...
        ClientShortName = hints.normal_property(_get_ClientShortName, _set_ClientShortName)
        def _get_ClientDescription(self) -> hints.Incomplete: ...
        def _set_ClientDescription(self, pbstrClientDescription: hints.Incomplete) -> hints.Hresult: ...
        ClientDescription = hints.normal_property(_get_ClientDescription, _set_ClientDescription)
        def _get_Cause(self) -> hints.Incomplete: ...
        def _set_Cause(self, pbstrCause: hints.Incomplete) -> hints.Hresult: ...
        Cause = hints.normal_property(_get_Cause, _set_Cause)
        def _get_Action(self) -> hints.Incomplete: ...
        def _set_Action(self, pbstrAction: hints.Incomplete) -> hints.Hresult: ...
        Action = hints.normal_property(_get_Action, _set_Action)
        def _get_Internals(self) -> hints.Incomplete: ...
        def _set_Internals(self, pbstrInternals: hints.Incomplete) -> hints.Hresult: ...
        Internals = hints.normal_property(_get_Internals, _set_Internals)
        def _get_HelpFile(self) -> hints.Incomplete: ...
        def _set_HelpFile(self, pbstrHelpFile: hints.Incomplete) -> hints.Hresult: ...
        HelpFile = hints.normal_property(_get_HelpFile, _set_HelpFile)
        def _get_HelpContextId(self) -> hints.Incomplete: ...
        def _set_HelpContextId(self, plHelpContextId: hints.Incomplete) -> hints.Hresult: ...
        HelpContextId = hints.normal_property(_get_HelpContextId, _set_HelpContextId)
        def Raise(self, varbWithRemoveAck: hints.Incomplete = ...) -> hints.Hresult: ...
        def Remove(self) -> hints.Hresult: ...


_DJHRemoteErrorEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Server requests clearance of remote error')],
        HRESULT,
        'OnRemoveRequest',
        (['in'], POINTER(IJHRemoteErrorEntry), 'pRemoteErrorEntry')
    ),
]


class IJHMachine2(IJHMachine):
    """IJHMachine2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{B43D20F9-C04C-4530-B36D-9014C35B39CA}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetState(self) -> hints.Incomplete: ...
        def ConnectRequest(self, bstrConnectionName: hints.Incomplete) -> hints.Hresult: ...
        def SetAccessMode(self, accessMode: hints.Incomplete, bstrPassword: hints.Incomplete) -> hints.Hresult: ...
        def GetVersionComInterface(self) -> hints.Incomplete: ...


class IJHMachine3(IJHMachine2):
    """IJHMachine3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{5748A4D4-59A9-4D6D-80E2-EE2286170E11}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def ConnectRequest2(self, bstrConnectionName: hints.Incomplete, varbstrClientName: hints.Incomplete = ..., varbstrClientGUID: hints.Incomplete = ...) -> hints.Hresult: ...
        def ConnectRequest3(self, pIConnection: hints.Incomplete, varbstrClientName: hints.Incomplete = ..., varbstrClientGUID: hints.Incomplete = ...) -> hints.Hresult: ...



IJHMachine2._methods_ = [
    COMMETHOD(
        [dispid(8), helpstring('The current connection state of the CNC')],
        HRESULT,
        'GetState',
        (['out', 'retval'], POINTER(DNC_STATE), 'pState')
    ),
    COMMETHOD(
        [dispid(9), helpstring('Make a connection to the selected CNC')],
        HRESULT,
        'ConnectRequest',
        (['in'], BSTR, 'bstrConnectionName')
    ),
    COMMETHOD(
        [dispid(10), helpstring('Set the interface to an extended access mode or back to default access.'), 'hidden'],
        HRESULT,
        'SetAccessMode',
        (['in'], DNC_ACCESS_MODE, 'accessMode'),
        (['in'], BSTR, 'bstrPassword')
    ),
    COMMETHOD(
        [dispid(11), helpstring('Retrieve the version of the HeidenhainDNC component (no connection required)')],
        HRESULT,
        'GetVersionComInterface',
        (['out', 'retval'], POINTER(BSTR), 'pbstrComInterfaceVersion')
    ),
]

################################################################
# code template for IJHMachine2 implementation
# class IJHMachine2_Impl(object):
#     def GetState(self):
#         'The current connection state of the CNC'
#         #return pState
#
#     def ConnectRequest(self, bstrConnectionName):
#         'Make a connection to the selected CNC'
#         #return 
#
#     def SetAccessMode(self, accessMode, bstrPassword):
#         'Set the interface to an extended access mode or back to default access.'
#         #return 
#
#     def GetVersionComInterface(self):
#         'Retrieve the version of the HeidenhainDNC component (no connection required)'
#         #return pbstrComInterfaceVersion
#

IJHMachine3._methods_ = [
    COMMETHOD(
        [dispid(12), helpstring('Request a pre-defined connection to the selected CNC')],
        HRESULT,
        'ConnectRequest2',
        (['in'], BSTR, 'bstrConnectionName'),
        (['in', 'optional'], VARIANT, 'varbstrClientName'),
        (['in', 'optional'], VARIANT, 'varbstrClientGUID')
    ),
    COMMETHOD(
        [dispid(13), helpstring('Request an ad-hoc connection to the selected CNC')],
        HRESULT,
        'ConnectRequest3',
        (['in'], POINTER(IJHConnection2), 'pIConnection'),
        (['in', 'optional'], VARIANT, 'varbstrClientName'),
        (['in', 'optional'], VARIANT, 'varbstrClientGUID')
    ),
]

################################################################
# code template for IJHMachine3 implementation
# class IJHMachine3_Impl(object):
#     def ConnectRequest2(self, bstrConnectionName, varbstrClientName, varbstrClientGUID):
#         'Request a pre-defined connection to the selected CNC'
#         #return 
#
#     def ConnectRequest3(self, pIConnection, varbstrClientName, varbstrClientGUID):
#         'Request an ad-hoc connection to the selected CNC'
#         #return 
#


class IJHSecureConnectionHelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHSecureConnectionHelper Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F93031DA-96F9-4A7F-8C38-A439557E4D00}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_bstrDefaultKeysDir(self) -> hints.Incomplete: ...
        bstrDefaultKeysDir = hints.normal_property(_get_bstrDefaultKeysDir)
        def _get_keyNameFromUserAtHost(self, bstrRemoteHost: hints.Incomplete, bstrRemoteUser: hints.Incomplete, protocol: hints.Incomplete) -> hints.Incomplete: ...
        keyNameFromUserAtHost = hints.named_property('keyNameFromUserAtHost', _get_keyNameFromUserAtHost)
        def _get_newRandomPassword(self, length: hints.Incomplete) -> hints.Incomplete: ...
        newRandomPassword = hints.named_property('newRandomPassword', _get_newRandomPassword)
        def GenerateKeyPair(self, bstrKeysDir: hints.Incomplete, bstrPrivateKeyName: hints.Incomplete, bstrPrivateKeyPassword: hints.Incomplete, mayOverwrite: hints.Incomplete, pbstrLogFile: hints.Incomplete) -> hints.Incomplete: ...
        def GetHostKey(self, bstrRemoteHost: hints.Incomplete, pbstrHostKeyFingerprint: hints.Incomplete, pbstrHostKeyRandomArt: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def RegisterKey(self, bstrRemoteHost: hints.Incomplete, bstrRemoteUser: hints.Incomplete, bstrPrivateKeyFilePath: hints.Incomplete) -> hints.Hresult: ...


class IJHSecureConnectionHelper2(IJHSecureConnectionHelper):
    """IJHSecureConnectionHelper2 Interface (deprecated)"""
    _case_insensitive_ = True
    _iid_ = GUID('{D2E77839-A235-4DD9-9DB9-62CD5F1B0A21}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def RegisterKey2(self, bstrRemoteHost: hints.Incomplete, bstrRemoteUser: hints.Incomplete, bstrRemoteUserPassword: hints.Incomplete, bstrPrivateKeyFilePath: hints.Incomplete) -> hints.Hresult: ...


class IJHSecureConnectionHelper3(IJHSecureConnectionHelper2):
    """IJHSecureConnectionHelper3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{85C76E21-DB1B-4E27-8176-0F594588B5B8}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def RegisterKey3(self, bstrRemoteHost: hints.Incomplete, bstrRemoteHostKeyFingerprint: hints.Incomplete, bstrRemoteUser: hints.Incomplete, bstrRemoteUserPassword: hints.Incomplete, bstrPrivateKeyFilePath: hints.Incomplete) -> hints.Hresult: ...


IJHSecureConnectionHelper._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('default SSH keys storage location'), 'propget'],
        HRESULT,
        'bstrDefaultKeysDir',
        (['out', 'retval'], POINTER(BSTR), 'pbstrDir')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Construct a private key name from user and host names'), 'propget'],
        HRESULT,
        'keyNameFromUserAtHost',
        (['in'], BSTR, 'bstrRemoteHost'),
        (['in'], BSTR, 'bstrRemoteUser'),
        (['in'], DNC_PROTOCOL, 'protocol'),
        (['out', 'retval'], POINTER(BSTR), 'pbstrPrivateKeyName')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Create a random password with given length'), 'propget'],
        HRESULT,
        'newRandomPassword',
        (['in'], c_int, 'length'),
        (['out', 'retval'], POINTER(BSTR), 'pbstrRandomPassword')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Create a new SSH key pair')],
        HRESULT,
        'GenerateKeyPair',
        (['in'], BSTR, 'bstrKeysDir'),
        (['in'], BSTR, 'bstrPrivateKeyName'),
        (['in'], BSTR, 'bstrPrivateKeyPassword'),
        (['in'], c_int, 'mayOverwrite'),
        (['in', 'out'], POINTER(BSTR), 'pbstrLogFile')
    ),
    COMMETHOD(
        [dispid(5), helpstring('Read the host key from the given remote host')],
        HRESULT,
        'GetHostKey',
        (['in'], BSTR, 'bstrRemoteHost'),
        (['in', 'out'], POINTER(BSTR), 'pbstrHostKeyFingerprint'),
        (['in', 'out'], POINTER(BSTR), 'pbstrHostKeyRandomArt')
    ),
    COMMETHOD(
        [dispid(6), helpstring('Transfer and register the given public key on the given remote host for the given user (deprecated)')],
        HRESULT,
        'RegisterKey',
        (['in'], BSTR, 'bstrRemoteHost'),
        (['in'], BSTR, 'bstrRemoteUser'),
        (['in'], BSTR, 'bstrPrivateKeyFilePath')
    ),
]

################################################################
# code template for IJHSecureConnectionHelper implementation
# class IJHSecureConnectionHelper_Impl(object):
#     @property
#     def bstrDefaultKeysDir(self):
#         'default SSH keys storage location'
#         #return pbstrDir
#
#     @property
#     def keyNameFromUserAtHost(self, bstrRemoteHost, bstrRemoteUser, protocol):
#         'Construct a private key name from user and host names'
#         #return pbstrPrivateKeyName
#
#     @property
#     def newRandomPassword(self, length):
#         'Create a random password with given length'
#         #return pbstrRandomPassword
#
#     def GenerateKeyPair(self, bstrKeysDir, bstrPrivateKeyName, bstrPrivateKeyPassword, mayOverwrite):
#         'Create a new SSH key pair'
#         #return pbstrLogFile
#
#     def GetHostKey(self, bstrRemoteHost):
#         'Read the host key from the given remote host'
#         #return pbstrHostKeyFingerprint, pbstrHostKeyRandomArt
#
#     def RegisterKey(self, bstrRemoteHost, bstrRemoteUser, bstrPrivateKeyFilePath):
#         'Transfer and register the given public key on the given remote host for the given user (deprecated)'
#         #return 
#

IJHSecureConnectionHelper2._methods_ = [
    COMMETHOD(
        [dispid(7), helpstring('Transfer and register the given public key on the given remote host for the given user')],
        HRESULT,
        'RegisterKey2',
        (['in'], BSTR, 'bstrRemoteHost'),
        (['in'], BSTR, 'bstrRemoteUser'),
        (['in'], BSTR, 'bstrRemoteUserPassword'),
        (['in'], BSTR, 'bstrPrivateKeyFilePath')
    ),
]

################################################################
# code template for IJHSecureConnectionHelper2 implementation
# class IJHSecureConnectionHelper2_Impl(object):
#     def RegisterKey2(self, bstrRemoteHost, bstrRemoteUser, bstrRemoteUserPassword, bstrPrivateKeyFilePath):
#         'Transfer and register the given public key on the given remote host for the given user'
#         #return 
#

IJHSecureConnectionHelper3._methods_ = [
    COMMETHOD(
        [dispid(8), helpstring('Transfer and register the given public key on the given remote host for the given user')],
        HRESULT,
        'RegisterKey3',
        (['in'], BSTR, 'bstrRemoteHost'),
        (['in'], BSTR, 'bstrRemoteHostKeyFingerprint'),
        (['in'], BSTR, 'bstrRemoteUser'),
        (['in'], BSTR, 'bstrRemoteUserPassword'),
        (['in'], BSTR, 'bstrPrivateKeyFilePath')
    ),
]

################################################################
# code template for IJHSecureConnectionHelper3 implementation
# class IJHSecureConnectionHelper3_Impl(object):
#     def RegisterKey3(self, bstrRemoteHost, bstrRemoteHostKeyFingerprint, bstrRemoteUser, bstrRemoteUserPassword, bstrPrivateKeyFilePath):
#         'Transfer and register the given public key on the given remote host for the given user'
#         #return 
#


class JHProgramPositionList(CoClass):
    """JHProgramPositionList Class"""
    _reg_clsid_ = GUID('{4A39F167-B929-4F7E-A2E0-2890DEDA26CA}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHProgramPositionList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHProgramPositionList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{3A3EDD9A-2A0C-4C8E-81B6-15D7183FFE37}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHProgramPosition': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


JHProgramPositionList._com_interfaces_ = [IJHProgramPositionList, IJHLoggingInternal]


class JHFileAttributes(CoClass):
    """JHFileAttributes Class"""
    _reg_clsid_ = GUID('{83D88391-26A5-4604-AC4A-A6C530C6E24E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHFileAttributes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHFileAttributes Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{8CBB96F6-6C3C-4412-A841-C664F0D81A71}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetAttributeName(self, attribute: hints.Incomplete) -> hints.Incomplete: ...
        def IsAttributeSet(self, attribute: hints.Incomplete) -> hints.Incomplete: ...
        def SetAttribute(self, attribute: hints.Incomplete) -> hints.Hresult: ...
        def ClearAttribute(self, attribute: hints.Incomplete) -> hints.Hresult: ...


JHFileAttributes._com_interfaces_ = [IJHFileAttributes, IJHLoggingInternal]


class JHAutomatic(CoClass):
    """JHAutomatic Class"""
    _reg_clsid_ = GUID('{F38CC671-EDB6-4328-9EDB-87F5765ECA14}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHAutomatic(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAutomatic Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{526BDD1B-0961-45FB-B417-A396A9E9DC4F}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def StartProgram0(self, bstrProgramName: hints.Incomplete) -> hints.Hresult: ...
        def GetProgramStatus(self) -> hints.Incomplete: ...
        def GetDncMode(self) -> hints.Incomplete: ...
        def ClearControl(self) -> hints.Hresult: ...
        def GetOverrideInfo(self, pFeed: hints.Incomplete, pSpeed: hints.Incomplete, pRapid: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetExecutionPoint(self, pSelectedProgram: hints.Incomplete) -> hints.Tuple[hints.Incomplete, 'IJHProgramPositionList']: ...
        def GetCutterLocation(self, lChannel: hints.Incomplete) -> 'IJHCutterLocationList': ...
        def SetOverrideFeed(self, lPercentage: hints.Incomplete) -> hints.Hresult: ...
        def SetOverrideRapid(self, lPercentage: hints.Incomplete) -> hints.Hresult: ...
        def SetOverrideSpeed(self, lPercentage: hints.Incomplete) -> hints.Hresult: ...
        def GetExecutionMode(self) -> hints.Incomplete: ...


class IJHAutomatic2(IJHAutomatic):
    """IJHAutomatic2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F7D0D8D6-CCDE-4A38-821B-7DA726DD40F2}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def StorePreset(self, lChannel: hints.Incomplete, lPresetEntry: hints.Incomplete, mcsPositions: hints.Incomplete, wcsPositions: hints.Incomplete, wcsRotations: hints.Incomplete) -> hints.Hresult: ...
        def SetExecutionMode(self, executionMode: hints.Incomplete) -> hints.Hresult: ...
        def StartProgram(self, bstrProgramName: hints.Incomplete, pBreakConditionList: hints.Incomplete = ...) -> hints.Hresult: ...


class IJHAutomatic3(IJHAutomatic2):
    """IJHAutomatic3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{AF749031-BA62-4834-AF0D-BFA3F063BD71}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SelectProgram(self, lChannel: hints.Incomplete, bstrProgramName: hints.Incomplete, varlStartBlockNumber: hints.Incomplete = ...) -> hints.Hresult: ...
        def StopProgram(self, lChannel: hints.Incomplete, bOnBlockEnd: hints.Incomplete) -> hints.Hresult: ...
        def CancelProgram(self, lChannel: hints.Incomplete) -> hints.Hresult: ...
        def GetMachinePositionsFromCutterPosition(self, lChannel: hints.Incomplete, pWcsPosition: hints.Incomplete, pToolToUse: hints.Incomplete) -> 'IJHAxisPositionListList': ...


class IJHAutomatic4(IJHAutomatic3):
    """IJHAutomatic4 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{DB4DB591-ADD3-4E44-86F8-1261404304B0}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def ImportToolUsageCSV(self, lChannel: hints.Incomplete, bstrToolUsageCSVName: hints.Incomplete) -> hints.Hresult: ...


class _DJHAutomaticEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHAutomaticEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{976C0711-57F4-40FB-9F60-8EE822E71289}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnProgramStatusChanged(self, programEvent: hints.Incomplete) -> hints.Incomplete: ...
        def OnDncModeChanged(self, newDncMode: hints.Incomplete) -> hints.Incomplete: ...
        def OnExecutionMessage(self, lChannel: hints.Incomplete, varNumericValue: hints.Incomplete, bstrValue: hints.Incomplete) -> hints.Incomplete: ...
        def OnProgramChanged(self, lChannel: hints.Incomplete, dTimeStamp: hints.Incomplete, bstrNewProgram: hints.Incomplete) -> hints.Incomplete: ...
        def OnToolChanged(self, lChannel: hints.Incomplete, pidToolOut: hints.Incomplete, pidToolIn: hints.Incomplete, dTimeStamp: hints.Incomplete) -> hints.Incomplete: ...
        def OnExecutionModeChanged(self, lChannel: hints.Incomplete, executionMode: hints.Incomplete) -> hints.Incomplete: ...


class _IJHAutomaticEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHAutomaticEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{41E1B1C0-D124-4C92-82EC-BAAFD560125A}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnProgramStatusChanged(self, programEvent: hints.Incomplete) -> hints.Hresult: ...
        def OnDncModeChanged(self, newDncMode: hints.Incomplete) -> hints.Hresult: ...


class _IJHAutomaticEvents2(_IJHAutomaticEvents):
    """_IJHAutomaticEvents2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{2540F084-655C-44B0-A151-67FF4FFC1DC9}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnExecutionMessage(self, lChannel: hints.Incomplete, varNumericValue: hints.Incomplete, bstrValue: hints.Incomplete) -> hints.Hresult: ...
        def OnProgramChanged(self, lChannel: hints.Incomplete, dTimeStamp: hints.Incomplete, bstrNewProgram: hints.Incomplete) -> hints.Hresult: ...
        def OnToolChanged(self, lChannel: hints.Incomplete, pidToolOut: hints.Incomplete, pidToolIn: hints.Incomplete, dTimeStamp: hints.Incomplete) -> hints.Hresult: ...


class _IJHAutomaticEvents3(_IJHAutomaticEvents2):
    """_IJHAutomaticEvents3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{F620BABE-3BCC-468D-BDB7-4508793B28AB}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnExecutionModeChanged(self, lChannel: hints.Incomplete, executionMode: hints.Incomplete) -> hints.Hresult: ...


JHAutomatic._com_interfaces_ = [IJHAutomatic4]
JHAutomatic._outgoing_interfaces_ = [_DJHAutomaticEvents, _IJHAutomaticEvents3]


class JHBreakCondition(CoClass):
    """JHBreakCondition Class"""
    _reg_clsid_ = GUID('{A132C7D4-38B0-4234-8DD6-42B20EE9359B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHBreakCondition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHBreakCondition Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{A1AED0B3-097C-41AE-B3F9-FA89E27238CB}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def BreakOnOptionalStop(self, bBreakOnOptionalStop: hints.Incomplete) -> hints.Hresult: ...
        def BreakOnProgrammedStop(self, bBreakOnProgrammedStop: hints.Incomplete) -> hints.Hresult: ...
        def BreakOnLineInFile(self, lLineNr: hints.Incomplete, lSkipCount: hints.Incomplete, bstrProgramFilename: hints.Incomplete = ...) -> hints.Hresult: ...
        def _get_bBreakOnOptionalStop(self) -> hints.Incomplete: ...
        bBreakOnOptionalStop = hints.normal_property(_get_bBreakOnOptionalStop)
        def _get_bBreakOnProgrammedStop(self) -> hints.Incomplete: ...
        bBreakOnProgrammedStop = hints.normal_property(_get_bBreakOnProgrammedStop)
        def _get_kind(self) -> hints.Incomplete: ...
        kind = hints.normal_property(_get_kind)
        def _get_bstrProgramFilename(self) -> hints.Incomplete: ...
        bstrProgramFilename = hints.normal_property(_get_bstrProgramFilename)
        def _get_lLineNr(self) -> hints.Incomplete: ...
        lLineNr = hints.normal_property(_get_lLineNr)
        def _get_lSkipCount(self) -> hints.Incomplete: ...
        lSkipCount = hints.normal_property(_get_lSkipCount)


JHBreakCondition._com_interfaces_ = [IJHBreakCondition, IJHLoggingInternal]


class JHTraceSampleList(CoClass):
    """JHTraceSampleList Class"""
    _reg_clsid_ = GUID('{24A447DC-B948-4AFD-829F-C06D1CA387F3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHTraceSampleList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceSampleList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{262E54F3-30FD-4208-A121-0415FC39230B}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHTraceSample': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def _get_lTraceChannelId(self) -> hints.Incomplete: ...
        lTraceChannelId = hints.normal_property(_get_lTraceChannelId)


JHTraceSampleList._com_interfaces_ = [IJHTraceSampleList, IJHLoggingInternal]


class IJHDataEntry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataEntry Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{C141C385-A752-4D06-8C19-F5D5CCDC9BE2}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_bIsNode(self) -> hints.Incomplete: ...
        bIsNode = hints.normal_property(_get_bIsNode)
        def _get_childList(self) -> 'IJHDataEntryList': ...
        childList = hints.normal_property(_get_childList)
        def _get_bstrFullName(self) -> hints.Incomplete: ...
        bstrFullName = hints.normal_property(_get_bstrFullName)
        def _get_bstrName(self) -> hints.Incomplete: ...
        bstrName = hints.normal_property(_get_bstrName)
        def _get_propertyList(self) -> 'IJHDataEntryPropertyList': ...
        propertyList = hints.normal_property(_get_propertyList)
        def Subscribe(self, pITriggerCondition: hints.Incomplete, pITriggerSampling: hints.Incomplete) -> hints.Incomplete: ...
        def UnSubscribe(self, lSubscribeHandle: hints.Incomplete) -> hints.Hresult: ...


class IJHDataEntry2(IJHDataEntry):
    """IJHDataEntry2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{88B02677-F095-4592-A36D-99DD02954317}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def Subscribe2(self) -> hints.Incomplete: ...
        def Subscribe2WithTrigger(self, pITriggerCondition: hints.Incomplete, pITriggerSampling: hints.Incomplete) -> hints.Incomplete: ...
        def _get_asString(self) -> hints.Incomplete: ...
        asString = hints.normal_property(_get_asString)
        def _get_unitSelect(self) -> hints.Incomplete: ...
        unitSelect = hints.normal_property(_get_unitSelect)
        def ReadPropertyValue(self, kind: hints.Incomplete) -> hints.Hresult: ...
        def WritePropertyValue(self, kind: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def GetPropertyValue(self, kind: hints.Incomplete) -> hints.Incomplete: ...
        def SetPropertyValue(self, kind: hints.Incomplete, propertyValue: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def _get_property(self, kind: hints.Incomplete = ...) -> 'IJHDataEntryProperty2': ...
        def _set_property(self, kind: hints.Incomplete = ..., **kwargs: hints.Any) -> hints.Hresult: ...
        property = hints.named_property('property', _get_property, _set_property)
        def _get_propertyList2(self) -> 'IJHDataEntryProperty2List': ...
        propertyList2 = hints.normal_property(_get_propertyList2)
        def GetPropertyList(self) -> 'IJHDataEntryProperty2List': ...
        def _get_propertyValue(self, kind: hints.Incomplete = ...) -> hints.Incomplete: ...
        def _set_propertyValue(self, kind: hints.Incomplete = ..., **kwargs: hints.Any) -> hints.Hresult: ...
        propertyValue = hints.named_property('propertyValue', _get_propertyValue, _set_propertyValue)
        def _get_child(self, bstrChildIdent: hints.Incomplete) -> 'IJHDataEntry2': ...
        child = hints.named_property('child', _get_child)
        def _get_childList2(self) -> 'IJHDataEntry2List': ...
        childList2 = hints.normal_property(_get_childList2)
        def add_child(self, bstrChildName: hints.Incomplete) -> 'IJHDataEntry2': ...
        def cloneTree(self) -> 'IJHDataEntry2': ...
        def ReadTreeValues(self, kind: hints.Incomplete) -> hints.Hresult: ...
        def WriteTreeValues(self, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def GetChildList(self) -> 'IJHDataEntry2List': ...


IJHDataEntry2List._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHDataEntry2 object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2)), 'ppDataEntry')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Add a new JHDataEntry2 item to the list.')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHDataEntry2), 'pNewChild')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Remove the JHDataEntry2 at given index from the list.')],
        HRESULT,
        'RemoveItem',
        (['in'], c_int, 'index')
    ),
    COMMETHOD(
        [dispid(4), helpstring('child'), 'propget'],
        HRESULT,
        'child',
        (['in'], BSTR, 'bstrChildIdent'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2)), 'ppDataEntry')
    ),
]

################################################################
# code template for IJHDataEntry2List implementation
# class IJHDataEntry2List_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHDataEntry2 object on the specified index in the list'
#         #return ppDataEntry
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#
#     def AddItem(self, pNewChild):
#         'Add a new JHDataEntry2 item to the list.'
#         #return 
#
#     def RemoveItem(self, index):
#         'Remove the JHDataEntry2 at given index from the list.'
#         #return 
#
#     @property
#     def child(self, bstrChildIdent):
#         'child'
#         #return ppDataEntry
#


class _IJHErrorEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHErrorEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{0FA1289F-60AC-4B52-B1AF-E3B9B355F2D8}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnError(self, errorGroup: hints.Incomplete, lErrorNumber: hints.Incomplete, errorClass: hints.Incomplete, bstrError: hints.Incomplete, lChannel: hints.Incomplete) -> hints.Hresult: ...
        def OnErrorCleared(self, lErrorNumber: hints.Incomplete, lChannel: hints.Incomplete) -> hints.Hresult: ...


class _IJHErrorEvents2(_IJHErrorEvents):
    """_IJHErrorEvents2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{FC0AB8A3-D32A-42F5-9FF1-8320EDF81E26}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnError2(self, a_pErrorEntry: hints.Incomplete) -> hints.Hresult: ...
        def OnErrorCleared2(self, a_pErrorEntry: hints.Incomplete) -> hints.Hresult: ...


_IJHErrorEvents._methods_ = [
    COMMETHOD(
        [helpstring('Signals the occurrence of an error')],
        HRESULT,
        'OnError',
        (['in'], DNC_ERROR_GROUP, 'errorGroup'),
        (['in'], c_int, 'lErrorNumber'),
        (['in'], DNC_ERROR_CLASS, 'errorClass'),
        (['in'], BSTR, 'bstrError'),
        (['in'], c_int, 'lChannel')
    ),
    COMMETHOD(
        [helpstring('Signals the clearence of an error')],
        HRESULT,
        'OnErrorCleared',
        (['in'], c_int, 'lErrorNumber'),
        (['in'], c_int, 'lChannel')
    ),
]

################################################################
# code template for _IJHErrorEvents implementation
# class _IJHErrorEvents_Impl(object):
#     def OnError(self, errorGroup, lErrorNumber, errorClass, bstrError, lChannel):
#         'Signals the occurrence of an error'
#         #return 
#
#     def OnErrorCleared(self, lErrorNumber, lChannel):
#         'Signals the clearence of an error'
#         #return 
#

_IJHErrorEvents2._methods_ = [
    COMMETHOD(
        [helpstring('Signals the occurrence of an error')],
        HRESULT,
        'OnError2',
        (['in'], POINTER(IJHErrorEntry2), 'a_pErrorEntry')
    ),
    COMMETHOD(
        [helpstring('Signals the clearence of an error')],
        HRESULT,
        'OnErrorCleared2',
        (['in'], POINTER(IJHErrorEntry2), 'a_pErrorEntry')
    ),
]

################################################################
# code template for _IJHErrorEvents2 implementation
# class _IJHErrorEvents2_Impl(object):
#     def OnError2(self, a_pErrorEntry):
#         'Signals the occurrence of an error'
#         #return 
#
#     def OnErrorCleared2(self, a_pErrorEntry):
#         'Signals the clearence of an error'
#         #return 
#


class JHError(CoClass):
    """JHError Class"""
    _reg_clsid_ = GUID('{3FB79E71-A6EB-4DAC-B212-FCEF8E86D7DA}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _DJHErrorEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_IEventObjectEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{114F372C-3BB4-4D37-8C08-C3194CB7E466}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnError(self, errorGroup: hints.Incomplete, lErrorNumber: hints.Incomplete, errorClass: hints.Incomplete, bstrError: hints.Incomplete, lChannel: hints.Incomplete) -> hints.Incomplete: ...
        def OnErrorCleared(self, lErrorNumber: hints.Incomplete, lChannel: hints.Incomplete) -> hints.Incomplete: ...
        def OnError2(self, pErrorEntry: hints.Incomplete) -> hints.Incomplete: ...
        def OnErrorCleared2(self, pErrorEntry: hints.Incomplete) -> hints.Incomplete: ...


JHError._com_interfaces_ = [IJHError3, IJHErrorInternal2]
JHError._outgoing_interfaces_ = [_DJHErrorEvents, _IJHErrorEvents2]


class JHProgramPosition(CoClass):
    """JHProgramPosition Class"""
    _reg_clsid_ = GUID('{D134ED57-29D7-4315-BF8C-5AA223CFC6FE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHProgramPosition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHProgramPosition Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6216D57D-678F-49DF-AD29-C00CC0C6AF62}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_programName(self) -> hints.Incomplete: ...
        programName = hints.normal_property(_get_programName)
        def _get_blockNumber(self) -> hints.Incomplete: ...
        blockNumber = hints.normal_property(_get_blockNumber)
        def _get_blockContent(self) -> hints.Incomplete: ...
        blockContent = hints.normal_property(_get_blockContent)


JHProgramPosition._com_interfaces_ = [IJHProgramPosition, IJHLoggingInternal]


class IJHTest(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTest Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{A7FF715B-1A3C-4F13-82C9-A39455F57105}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SendString(self, bstrString: hints.Incomplete) -> hints.Hresult: ...
        def SendKey(self, bstrWmKey: hints.Incomplete, bstrQualifiers: hints.Incomplete, keyAction: hints.Incomplete) -> hints.Hresult: ...
        def SetAccessMode(self, accessMode: hints.Incomplete, bstrPassword: hints.Incomplete) -> hints.Hresult: ...
        def StartPositionLogging(self, bstrFileName: hints.Incomplete) -> hints.Hresult: ...
        def StopPositionLogging(self) -> hints.Hresult: ...
        def StartUserLogging(self, bstrFileName: hints.Incomplete) -> hints.Hresult: ...
        def StopUserLogging(self) -> hints.Hresult: ...
        def StartUserLogPlayback(self) -> hints.Hresult: ...
        def StopUserLogPlayback(self) -> hints.Hresult: ...
        def WmKeyEventRaw(self, bstrWmKey: hints.Incomplete, bstrFuncKey: hints.Incomplete, bstrQualifiers: hints.Incomplete, code: hints.Incomplete, scanCode: hints.Incomplete, isDown: hints.Incomplete, isRepeat: hints.Incomplete, time: hints.Incomplete, mouseCoordX: hints.Incomplete, mouseCoordY: hints.Incomplete) -> hints.Hresult: ...
        def WmCharEventRaw(self, character: hints.Incomplete, bstrQualifiers: hints.Incomplete, isRepeat: hints.Incomplete, time: hints.Incomplete, mouseCoordX: hints.Incomplete, mouseCoordY: hints.Incomplete) -> hints.Hresult: ...
        def WmMouseEventRaw(self, bstrEventType: hints.Incomplete, bstrButton: hints.Incomplete, bstrQualifiers: hints.Incomplete, flags: hints.Incomplete, time: hints.Incomplete, mouseCoordX: hints.Incomplete, mouseCoordY: hints.Incomplete) -> hints.Hresult: ...
        def SendMouse(self, bstrAction: hints.Incomplete, bstrButton: hints.Incomplete, bstrQualifiers: hints.Incomplete, mouseCoordX: hints.Incomplete, mouseCoordY: hints.Incomplete) -> hints.Hresult: ...
        def MakeScreenShot(self, bstrFileName: hints.Incomplete, xOrigin: hints.Incomplete = ..., yOrigin: hints.Incomplete = ..., width: hints.Incomplete = ..., height: hints.Incomplete = ...) -> hints.Hresult: ...
        def GetAvailableKeys(self, ppsaVirtualKeys: hints.Incomplete, ppsaFunctionalKeys: hints.Incomplete, ppsaQualifiers: hints.Incomplete, ppsaActions: hints.Incomplete, ppsaButtons: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetGuiProcessState(self, bstrGuiProcessName: hints.Incomplete) -> hints.Incomplete: ...


IJHTest._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method SendString')],
        HRESULT,
        'SendString',
        (['in'], BSTR, 'bstrString')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method SendKey')],
        HRESULT,
        'SendKey',
        (['in'], BSTR, 'bstrWmKey'),
        (['in'], BSTR, 'bstrQualifiers'),
        (['in'], DNC_KEYACTION, 'keyAction')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method SetAccessMode')],
        HRESULT,
        'SetAccessMode',
        (['in'], DNC_ACCESS_MODE, 'accessMode'),
        (['in'], BSTR, 'bstrPassword')
    ),
    COMMETHOD(
        [dispid(4), helpstring('method StartPositionLogging')],
        HRESULT,
        'StartPositionLogging',
        (['in'], BSTR, 'bstrFileName')
    ),
    COMMETHOD(
        [dispid(5), helpstring('method StopPositionLogging')],
        HRESULT,
        'StopPositionLogging',
    ),
    COMMETHOD(
        [dispid(6), helpstring('method StartUserLogging')],
        HRESULT,
        'StartUserLogging',
        (['in'], BSTR, 'bstrFileName')
    ),
    COMMETHOD(
        [dispid(7), helpstring('method StopUserLogging')],
        HRESULT,
        'StopUserLogging',
    ),
    COMMETHOD(
        [dispid(8), helpstring('method StartUserLogPlayback')],
        HRESULT,
        'StartUserLogPlayback',
    ),
    COMMETHOD(
        [dispid(9), helpstring('method StopUserLogPlayback')],
        HRESULT,
        'StopUserLogPlayback',
    ),
    COMMETHOD(
        [dispid(10), helpstring('method WmKeyEventRaw')],
        HRESULT,
        'WmKeyEventRaw',
        (['in'], BSTR, 'bstrWmKey'),
        (['in'], BSTR, 'bstrFuncKey'),
        (['in'], BSTR, 'bstrQualifiers'),
        (['in'], c_ulong, 'code'),
        (['in'], c_ulong, 'scanCode'),
        (['in'], VARIANT_BOOL, 'isDown'),
        (['in'], VARIANT_BOOL, 'isRepeat'),
        (['in'], c_ulong, 'time'),
        (['in'], c_int, 'mouseCoordX'),
        (['in'], c_int, 'mouseCoordY')
    ),
    COMMETHOD(
        [dispid(11), helpstring('method WmCharEventRaw')],
        HRESULT,
        'WmCharEventRaw',
        (['in'], c_int, 'character'),
        (['in'], BSTR, 'bstrQualifiers'),
        (['in'], VARIANT_BOOL, 'isRepeat'),
        (['in'], c_ulong, 'time'),
        (['in'], c_int, 'mouseCoordX'),
        (['in'], c_int, 'mouseCoordY')
    ),
    COMMETHOD(
        [dispid(12), helpstring('method WmMouseEventRaw')],
        HRESULT,
        'WmMouseEventRaw',
        (['in'], BSTR, 'bstrEventType'),
        (['in'], BSTR, 'bstrButton'),
        (['in'], BSTR, 'bstrQualifiers'),
        (['in'], c_ulong, 'flags'),
        (['in'], c_ulong, 'time'),
        (['in'], c_int, 'mouseCoordX'),
        (['in'], c_int, 'mouseCoordY')
    ),
    COMMETHOD(
        [dispid(13), helpstring('method SendMouse')],
        HRESULT,
        'SendMouse',
        (['in'], BSTR, 'bstrAction'),
        (['in'], BSTR, 'bstrButton'),
        (['in'], BSTR, 'bstrQualifiers'),
        (['in'], c_int, 'mouseCoordX'),
        (['in'], c_int, 'mouseCoordY')
    ),
    COMMETHOD(
        [dispid(14), helpstring('method MakeScreenShot')],
        HRESULT,
        'MakeScreenShot',
        (['in'], BSTR, 'bstrFileName'),
        (['in', 'optional'], VARIANT, 'xOrigin'),
        (['in', 'optional'], VARIANT, 'yOrigin'),
        (['in', 'optional'], VARIANT, 'width'),
        (['in', 'optional'], VARIANT, 'height')
    ),
    COMMETHOD(
        [dispid(15), helpstring('method GetAvailableKeys')],
        HRESULT,
        'GetAvailableKeys',
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaVirtualKeys'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaFunctionalKeys'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaQualifiers'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaActions'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaButtons')
    ),
    COMMETHOD(
        [dispid(16), helpstring('method GetGuiProcessState')],
        HRESULT,
        'GetGuiProcessState',
        (['in'], BSTR, 'bstrGuiProcessName'),
        (['out', 'retval'], POINTER(BSTR), 'bstrNewState')
    ),
]

################################################################
# code template for IJHTest implementation
# class IJHTest_Impl(object):
#     def SendString(self, bstrString):
#         'method SendString'
#         #return 
#
#     def SendKey(self, bstrWmKey, bstrQualifiers, keyAction):
#         'method SendKey'
#         #return 
#
#     def SetAccessMode(self, accessMode, bstrPassword):
#         'method SetAccessMode'
#         #return 
#
#     def StartPositionLogging(self, bstrFileName):
#         'method StartPositionLogging'
#         #return 
#
#     def StopPositionLogging(self):
#         'method StopPositionLogging'
#         #return 
#
#     def StartUserLogging(self, bstrFileName):
#         'method StartUserLogging'
#         #return 
#
#     def StopUserLogging(self):
#         'method StopUserLogging'
#         #return 
#
#     def StartUserLogPlayback(self):
#         'method StartUserLogPlayback'
#         #return 
#
#     def StopUserLogPlayback(self):
#         'method StopUserLogPlayback'
#         #return 
#
#     def WmKeyEventRaw(self, bstrWmKey, bstrFuncKey, bstrQualifiers, code, scanCode, isDown, isRepeat, time, mouseCoordX, mouseCoordY):
#         'method WmKeyEventRaw'
#         #return 
#
#     def WmCharEventRaw(self, character, bstrQualifiers, isRepeat, time, mouseCoordX, mouseCoordY):
#         'method WmCharEventRaw'
#         #return 
#
#     def WmMouseEventRaw(self, bstrEventType, bstrButton, bstrQualifiers, flags, time, mouseCoordX, mouseCoordY):
#         'method WmMouseEventRaw'
#         #return 
#
#     def SendMouse(self, bstrAction, bstrButton, bstrQualifiers, mouseCoordX, mouseCoordY):
#         'method SendMouse'
#         #return 
#
#     def MakeScreenShot(self, bstrFileName, xOrigin, yOrigin, width, height):
#         'method MakeScreenShot'
#         #return 
#
#     def GetAvailableKeys(self):
#         'method GetAvailableKeys'
#         #return ppsaVirtualKeys, ppsaFunctionalKeys, ppsaQualifiers, ppsaActions, ppsaButtons
#
#     def GetGuiProcessState(self, bstrGuiProcessName):
#         'method GetGuiProcessState'
#         #return bstrNewState
#


class JHAxisPositionList(CoClass):
    """JHAxisPositionList Class"""
    _reg_clsid_ = GUID('{41911C16-915A-44AA-8F40-D7C595DA1EBC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAxisPositionList._com_interfaces_ = [IJHAxisPositionList, IJHLoggingInternal]


class JHVersion(CoClass):
    """JHVersion Class"""
    _reg_clsid_ = GUID('{9776BF54-59CE-4FAE-92A4-79A34853FAAC}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHVersion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHVersion Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{D157773C-4EA6-4E8B-8EA4-A6737EEA10A6}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetVersionNcSoftware(self) -> 'IJHSoftwareVersionList': ...
        def GetSik(self) -> hints.Incomplete: ...
        def GetVersionComInterface(self) -> hints.Incomplete: ...


JHVersion._com_interfaces_ = [IJHVersion]

IEventObject._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Store the control specific interface')],
        HRESULT,
        'Init',
        (['in'], POINTER(IUnknown), 'pIUnknownOfCncObject')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Sets the name of the current connection')],
        HRESULT,
        'PutConnectionName',
        ([], BSTR, 'connectionName')
    ),
]

################################################################
# code template for IEventObject implementation
# class IEventObject_Impl(object):
#     def Init(self, pIUnknownOfCncObject):
#         'Store the control specific interface'
#         #return 
#
#     def PutConnectionName(self, connectionName):
#         'Sets the name of the current connection'
#         #return 
#


class JHDirectoryEntryList(CoClass):
    """JHDirectoryEntryList Class"""
    _reg_clsid_ = GUID('{E7327C4D-9020-449E-AE79-D5CA2FC60399}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHDirectoryEntryList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDirectoryEntryList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{06DFEA67-B261-4D25-A8F0-0A97ED14E2FE}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHDirectoryEntry': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


JHDirectoryEntryList._com_interfaces_ = [IJHDirectoryEntryList, IJHLoggingInternal]


class JHDataAccessEvents(CoClass):
    """JHDataAccessEvents Class"""
    _reg_clsid_ = GUID('{97D5F510-06D3-46DB-A322-2AC8CE32A6C4}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataAccessEvents._com_interfaces_ = [IEventObject]
JHDataAccessEvents._outgoing_interfaces_ = [_DJHDataAccessEvents, _IJHDataAccessEvents2]


class JHBreakConditionList(CoClass):
    """JHBreakConditionList Class"""
    _reg_clsid_ = GUID('{6E846DAE-D525-4718-83E8-2DA2279BB1BC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHBreakConditionList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHBreakConditionList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E1677900-BAC3-41CF-8B44-7E01FE9AA20C}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHBreakCondition': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def AddItem(self, pBreakCondition: hints.Incomplete) -> hints.Hresult: ...
        def RemoveItem(self, lIndex: hints.Incomplete) -> hints.Hresult: ...


JHBreakConditionList._com_interfaces_ = [IJHBreakConditionList, IJHLoggingInternal]


class Library(object):
    """HeidenhainDnc 1.7 Type Library"""
    name = 'HeidenhainDNCLib'
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)




class _IJHTestEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHTestEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{87E9BF01-EC2A-4368-9615-720F95651409}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnRequestUnlockKeyboard(self) -> hints.Hresult: ...
        def OnGuiProcessStateChanged(self, bstrGuiProcessName: hints.Incomplete, bstrNewState: hints.Incomplete) -> hints.Hresult: ...
        def OnGuiProcessGotFocus(self, bstrGuiProcessName: hints.Incomplete) -> hints.Hresult: ...


_IJHTestEvents._methods_ = [
    COMMETHOD(
        [helpstring('Fire event OnRequestUnlockKeyboard')],
        HRESULT,
        'OnRequestUnlockKeyboard',
    ),
    COMMETHOD(
        [helpstring('Fire event OnGuiProcessStateChanged')],
        HRESULT,
        'OnGuiProcessStateChanged',
        (['in'], BSTR, 'bstrGuiProcessName'),
        (['in'], BSTR, 'bstrNewState')
    ),
    COMMETHOD(
        [helpstring('Fire event OnGuiProcessGotFocus')],
        HRESULT,
        'OnGuiProcessGotFocus',
        (['in'], BSTR, 'bstrGuiProcessName')
    ),
]

################################################################
# code template for _IJHTestEvents implementation
# class _IJHTestEvents_Impl(object):
#     def OnRequestUnlockKeyboard(self):
#         'Fire event OnRequestUnlockKeyboard'
#         #return 
#
#     def OnGuiProcessStateChanged(self, bstrGuiProcessName, bstrNewState):
#         'Fire event OnGuiProcessStateChanged'
#         #return 
#
#     def OnGuiProcessGotFocus(self, bstrGuiProcessName):
#         'Fire event OnGuiProcessGotFocus'
#         #return 
#


class JHTraceEvents(CoClass):
    """JHTraceEvents Class"""
    _reg_clsid_ = GUID('{5807308B-A006-4A11-BC11-EC045E31CD8F}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _IJHTraceEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHTraceEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{2BD4BC84-733A-47ED-9D99-355014E101C8}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnTraceDataAvailable(self) -> hints.Hresult: ...
        def OnTracingAborted(self) -> hints.Hresult: ...


JHTraceEvents._com_interfaces_ = [IEventObject]
JHTraceEvents._outgoing_interfaces_ = [_DJHTraceEvents, _IJHTraceEvents]


class JHTraceSampleEnum(CoClass):
    """JHTraceSampleEnum Class"""
    _reg_clsid_ = GUID('{205DFA6D-94E5-43F5-BD18-8A8DE37A3586}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceSampleEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHFileSystem(CoClass):
    """JHFileSystem Class"""
    _reg_clsid_ = GUID('{F1C0AD1A-FCD4-4654-B675-C1AF95AF4E90}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHFileSystem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHFileSystem Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{20143017-01FA-47B6-A6E0-906CA9529186}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetDiskSpace(self, bstrPath: hints.Incomplete, pdFreeSpace: hints.Incomplete, pdTotalSize: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def GetCurrentDirectory(self) -> hints.Incomplete: ...
        def GetFileSystemAttributes(self) -> 'IJHFileAttributes': ...
        def ReadDirectory(self, bstrFileName: hints.Incomplete, pAttributeSelection: hints.Incomplete, pAttributeState: hints.Incomplete) -> 'IJHDirectoryEntryList': ...
        def ChangeDirectory(self, bstrNewDir: hints.Incomplete) -> hints.Hresult: ...
        def MakeDirectory(self, bstrNewDir: hints.Incomplete) -> hints.Hresult: ...
        def DeleteDirectory(self, bstrDir: hints.Incomplete) -> hints.Hresult: ...
        def DeleteFile(self, bstrFileName: hints.Incomplete) -> hints.Hresult: ...
        def Rename(self, bstrOldFileName: hints.Incomplete, bstrNewFileName: hints.Incomplete) -> hints.Hresult: ...
        def CopyFile(self, bstrSourceFileName: hints.Incomplete, bstrDestFileName: hints.Incomplete) -> hints.Hresult: ...
        def PreviewFile(self, bstrFileName: hints.Incomplete, lNrLines: hints.Incomplete) -> hints.Incomplete: ...
        def ReceiveFile(self, bstrSourceFileName: hints.Incomplete, bstrDestFileName: hints.Incomplete) -> hints.Hresult: ...
        def StartReceiveFile(self, bstrSourceFileName: hints.Incomplete, bstrDestFileName: hints.Incomplete, bReportProgress: hints.Incomplete) -> hints.Incomplete: ...
        def TransmitFile(self, bstrSourceFileName: hints.Incomplete, bstrDestFileName: hints.Incomplete) -> hints.Hresult: ...
        def StartTransmitFile(self, bstrSourceFileName: hints.Incomplete, bstrDestFileName: hints.Incomplete, bReportProgress: hints.Incomplete) -> hints.Incomplete: ...
        def AbortFileTransfer(self, lTransferJobId: hints.Incomplete) -> hints.Hresult: ...
        def SetAttributes(self, bstrName: hints.Incomplete, pAttributes: hints.Incomplete) -> hints.Hresult: ...
        def GetAttributes(self, bstrName: hints.Incomplete) -> 'IJHFileAttributes': ...
        def SetFileTime(self, bstrFileName: hints.Incomplete, dateTime: hints.Incomplete) -> hints.Hresult: ...
        def GetFileTime(self, bstrFileName: hints.Incomplete) -> hints.Incomplete: ...
        def SetAccessMode(self, accessMode: hints.Incomplete, bstrPassword: hints.Incomplete) -> hints.Hresult: ...
        def ObserveFileChange(self, bstrFileName: hints.Incomplete, command: hints.Incomplete) -> hints.Hresult: ...


class _IJHFileSystemEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHFileSystemEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{712B7AFC-B5C8-4852-BE83-CA7B14A19133}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnFileTransferEnd(self, lTransferJobId: hints.Incomplete, hErrorCode: hints.Incomplete) -> hints.Hresult: ...
        def OnFileTransferProgress(self, lTransferJobId: hints.Incomplete, lBytesCopied: hints.Incomplete, lBytesTotal: hints.Incomplete) -> hints.Hresult: ...
        def OnFileChanged(self, bstrFileName: hints.Incomplete) -> hints.Hresult: ...


JHFileSystem._com_interfaces_ = [IJHFileSystem]
JHFileSystem._outgoing_interfaces_ = [_DJHFileSystemEvents, _IJHFileSystemEvents]


class JHAxesPositionStreaming(CoClass):
    """JHAxesPositionStreaming Class"""
    _reg_clsid_ = GUID('{2A8791A6-4D6A-4DFB-A331-CD6DC0F9386D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _DJHAxesPositionStreamingEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHAxesPositionStreamingEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{1DA2EA3A-F2A9-4CB2-A253-63151ECA13FA}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnAxesPositionsAvailable(self) -> hints.Incomplete: ...


JHAxesPositionStreaming._com_interfaces_ = [IJHAxesPositionStreaming2]
JHAxesPositionStreaming._outgoing_interfaces_ = [_DJHAxesPositionStreamingEvents, _IJHAxesPositionStreamingEvents]


class JHCutterLocationEnum(CoClass):
    """JHCutterLocationEnum Class"""
    _reg_clsid_ = GUID('{BF31D888-3803-4CA9-86A0-D80BB236ACC5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHCutterLocationEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class _DJHPlcEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHPlcEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{41719C98-9FFC-48EE-ACC9-4D80EC6D1F9D}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnPlcData(self, bstrPlcString: hints.Incomplete, ppsalPlcMarkers: hints.Incomplete, ppsalPlcDWords: hints.Incomplete) -> hints.Incomplete: ...


_DJHPlcEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('method OnPlcData')],
        HRESULT,
        'OnPlcData',
        (['in'], BSTR, 'bstrPlcString'),
        (['in'], POINTER(_midlSAFEARRAY(c_int)), 'ppsalPlcMarkers'),
        (['in'], POINTER(_midlSAFEARRAY(c_int)), 'ppsalPlcDWords')
    ),
]


class IJHProcessData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHProcessData Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{E04E196B-ADCD-435D-BC1F-7963DC27E6AC}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetNcUpTime(self, pHours: hints.Incomplete, pMinutes: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def GetMachineUpTime(self, pHours: hints.Incomplete, pMinutes: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def GetSpindleRunningTime(self, timerId: hints.Incomplete, pHours: hints.Incomplete, pMinutes: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...
        def GetMachineRunningTime(self, pHours: hints.Incomplete, pMinutes: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete]: ...


IJHProcessData._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieving the up-time of the NC')],
        HRESULT,
        'GetNcUpTime',
        (['in', 'out'], POINTER(VARIANT), 'pHours'),
        (['in', 'out'], POINTER(VARIANT), 'pMinutes')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Retrieving the up-time of the machine')],
        HRESULT,
        'GetMachineUpTime',
        (['in', 'out'], POINTER(VARIANT), 'pHours'),
        (['in', 'out'], POINTER(VARIANT), 'pMinutes')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Retrieving the operation time of the specified spindle')],
        HRESULT,
        'GetSpindleRunningTime',
        (['in'], c_int, 'timerId'),
        (['in', 'out'], POINTER(VARIANT), 'pHours'),
        (['in', 'out'], POINTER(VARIANT), 'pMinutes')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Retrieving the working time of the machine')],
        HRESULT,
        'GetMachineRunningTime',
        (['in', 'out'], POINTER(VARIANT), 'pHours'),
        (['in', 'out'], POINTER(VARIANT), 'pMinutes')
    ),
]

################################################################
# code template for IJHProcessData implementation
# class IJHProcessData_Impl(object):
#     def GetNcUpTime(self):
#         'Retrieving the up-time of the NC'
#         #return pHours, pMinutes
#
#     def GetMachineUpTime(self):
#         'Retrieving the up-time of the machine'
#         #return pHours, pMinutes
#
#     def GetSpindleRunningTime(self, timerId):
#         'Retrieving the operation time of the specified spindle'
#         #return pHours, pMinutes
#
#     def GetMachineRunningTime(self):
#         'Retrieving the working time of the machine'
#         #return pHours, pMinutes
#


class IJHDataEntryList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataEntryList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{42A5ECA9-BFF8-4C04-80BE-4E61BCA77577}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHDataEntry': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


class IJHTriggerCondition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTriggerCondition Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{D36ED203-F524-443F-9A24-E50473ED8CFD}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def TriggerAlways(self) -> hints.Hresult: ...
        def TriggerOnChange(self) -> hints.Hresult: ...
        def TriggerOnDeltaChange(self, varConditionDelta: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnLevel(self, levelCondition: hints.Incomplete, varConditionLevel: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnRange(self, rangeCondition: hints.Incomplete, varConditionLower: hints.Incomplete, varConditionUpper: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnSustainedLevelForDuration(self, levelCondition: hints.Incomplete, varConditionLevel: hints.Incomplete, durationCondition: hints.Incomplete, dDurationLevel: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnSustainedRangeForDuration(self, rangeCondition: hints.Incomplete, varConditionLower: hints.Incomplete, varConditionUpper: hints.Incomplete, durationCondition: hints.Incomplete, dDurationLevel: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnSustainedLevelForRange(self, levelCondition: hints.Incomplete, varConditionLevel: hints.Incomplete, durationCondition: hints.Incomplete, dDurationLower: hints.Incomplete, dDurationUpper: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnSustainedRangeForRange(self, rangeCondition: hints.Incomplete, varConditionLower: hints.Incomplete, varConditionUpper: hints.Incomplete, durationCondition: hints.Incomplete, dDurationLower: hints.Incomplete, dDurationUpper: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnRisingEdge(self) -> hints.Hresult: ...
        def TriggerOnRisingEdgeAndLevel(self, levelCondition: hints.Incomplete, varConditionLevel: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnRisingEdgeAndRange(self, rangeCondition: hints.Incomplete, varEdgeLower: hints.Incomplete, varEdgeUpper: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnFallingEdge(self) -> hints.Hresult: ...
        def TriggerOnFallingEdgeAndLevel(self, levelCondition: hints.Incomplete, varConditionLevel: hints.Incomplete) -> hints.Hresult: ...
        def TriggerOnFallingEdgeAndRange(self, rangeCondition: hints.Incomplete, varEdgeLower: hints.Incomplete, varEdgeUpper: hints.Incomplete) -> hints.Hresult: ...
        def _get_triggerMode(self) -> hints.Incomplete: ...
        triggerMode = hints.normal_property(_get_triggerMode)
        def _get_triggerCondition(self) -> hints.Incomplete: ...
        triggerCondition = hints.normal_property(_get_triggerCondition)
        def _get_varTriggerValueLower(self) -> hints.Incomplete: ...
        varTriggerValueLower = hints.normal_property(_get_varTriggerValueLower)
        def _get_varTriggerValueUpper(self) -> hints.Incomplete: ...
        varTriggerValueUpper = hints.normal_property(_get_varTriggerValueUpper)
        def _get_triggerDurationCondition(self) -> hints.Incomplete: ...
        triggerDurationCondition = hints.normal_property(_get_triggerDurationCondition)
        def _get_dTriggerDurationValueLower(self) -> hints.Incomplete: ...
        dTriggerDurationValueLower = hints.normal_property(_get_dTriggerDurationValueLower)
        def _get_dTriggerDurationValueUpper(self) -> hints.Incomplete: ...
        dTriggerDurationValueUpper = hints.normal_property(_get_dTriggerDurationValueUpper)


IJHDataEntry._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Test if this DataEntry is a node'), 'propget'],
        HRESULT,
        'bIsNode',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbIsNode')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property childList'), 'propget'],
        HRESULT,
        'childList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryList)),
            'ppDataEntryList',
        )
    ),
    COMMETHOD(
        [dispid(3), helpstring('property bstrFullName'), 'propget'],
        HRESULT,
        'bstrFullName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrFullName')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property bstrName'), 'propget'],
        HRESULT,
        'bstrName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrName')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property ppPropertyList'), 'propget'],
        HRESULT,
        'propertyList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryPropertyList)),
            'ppPropertyList',
        )
    ),
    COMMETHOD(
        [dispid(6), helpstring('Define a trigger condition for reporting events')],
        HRESULT,
        'Subscribe',
        (['in'], POINTER(IJHTriggerCondition), 'pITriggerCondition'),
        (['in'], POINTER(IJHTriggerSampling), 'pITriggerSampling'),
        (['out', 'retval'], POINTER(c_int), 'plSubscribeHandle')
    ),
    COMMETHOD(
        [dispid(7), helpstring('Disable a previous Subscribe')],
        HRESULT,
        'UnSubscribe',
        (['in'], c_int, 'lSubscribeHandle')
    ),
]

################################################################
# code template for IJHDataEntry implementation
# class IJHDataEntry_Impl(object):
#     @property
#     def bIsNode(self):
#         'Test if this DataEntry is a node'
#         #return pbIsNode
#
#     @property
#     def childList(self):
#         'property childList'
#         #return ppDataEntryList
#
#     @property
#     def bstrFullName(self):
#         'property bstrFullName'
#         #return pbstrFullName
#
#     @property
#     def bstrName(self):
#         'property bstrName'
#         #return pbstrName
#
#     @property
#     def propertyList(self):
#         'property ppPropertyList'
#         #return ppPropertyList
#
#     def Subscribe(self, pITriggerCondition, pITriggerSampling):
#         'Define a trigger condition for reporting events'
#         #return plSubscribeHandle
#
#     def UnSubscribe(self, lSubscribeHandle):
#         'Disable a previous Subscribe'
#         #return 
#


class IJHDataEntryProperty2(IJHDataEntryProperty):
    """IJHDataEntryProperty2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{BFBC4E34-9FE1-4E99-B2EE-87FA8CD05C25}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def ReadValue(self) -> hints.Hresult: ...
        def WriteValue(self, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def GetValue(self) -> hints.Incomplete: ...
        def SetValue(self, propertyValue: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def _get_value(self) -> hints.Incomplete: ...
        def _set_value(self, pvarValue: hints.Incomplete) -> hints.Hresult: ...
        value = hints.normal_property(_get_value, _set_value)
        def _get_asString(self) -> hints.Incomplete: ...
        asString = hints.normal_property(_get_asString)
        def _get_unitSelect(self) -> hints.Incomplete: ...
        unitSelect = hints.normal_property(_get_unitSelect)
        def _get_bstrFullName(self) -> hints.Incomplete: ...
        bstrFullName = hints.normal_property(_get_bstrFullName)
        def _get_bstrName(self) -> hints.Incomplete: ...
        bstrName = hints.normal_property(_get_bstrName)


class IJHDataEntryProperty2List(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataEntryPropertyList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{9314D6BE-512F-4DDE-8544-120C1A8C31C9}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHDataEntryProperty2': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def AddItem(self, pDataEntryProperty: hints.Incomplete) -> hints.Hresult: ...
        def _get_property(self, kind: hints.Incomplete) -> 'IJHDataEntryProperty2': ...
        property = hints.named_property('property', _get_property)
        def _get_propertyValue(self, kind: hints.Incomplete) -> hints.Incomplete: ...
        propertyValue = hints.named_property('propertyValue', _get_propertyValue)
        def ReadPropertyValue(self, kind: hints.Incomplete) -> hints.Hresult: ...
        def WritePropertyValue(self, kind: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def GetPropertyValue(self, kind: hints.Incomplete) -> hints.Incomplete: ...
        def SetPropertyValue(self, kind: hints.Incomplete, propertyValue: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...


IJHDataEntry2._methods_ = [
    COMMETHOD(
        [dispid(8), helpstring('Subscribe for events on this data entry')],
        HRESULT,
        'Subscribe2',
        (['out', 'retval'], POINTER(c_int), 'pSubscriptionHandle')
    ),
    COMMETHOD(
        [dispid(9), helpstring('Subscribe for events on this data entry, with specific trigger conditions')],
        HRESULT,
        'Subscribe2WithTrigger',
        (['in'], POINTER(IJHTriggerCondition), 'pITriggerCondition'),
        (['in'], POINTER(IJHTriggerSampling), 'pITriggerSampling'),
        (['out', 'retval'], POINTER(c_int), 'pSubscriptionHandle')
    ),
    COMMETHOD(
        [dispid(10), helpstring('return the asString setting'), 'propget'],
        HRESULT,
        'asString',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pAsString')
    ),
    COMMETHOD(
        [dispid(11), helpstring('return the unit select setting'), 'propget'],
        HRESULT,
        'unitSelect',
        (['out', 'retval'], POINTER(DNC_DATA_UNIT_SELECT), 'pUnit')
    ),
    COMMETHOD(
        [dispid(12), helpstring('read/update stored property value from server')],
        HRESULT,
        'ReadPropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind')
    ),
    COMMETHOD(
        [dispid(13), helpstring('write stored property value to server')],
        HRESULT,
        'WritePropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(14), helpstring('read/update stored property value from server and return it')],
        HRESULT,
        'GetPropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['out', 'retval'], POINTER(VARIANT), 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(15), helpstring('write/update given value to stored property value and write it to server')],
        HRESULT,
        'SetPropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['in'], VARIANT, 'propertyValue'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(16), helpstring('return reference to the selected stored property'), 'propget'],
        HRESULT,
        'property',
        (['in', 'optional'], DNC_DATAENTRY_PROPKIND, 'kind', 0),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty2)),
            'ppProperty',
        )
    ),
    COMMETHOD(
        [dispid(16), helpstring('return reference to the selected stored property'), 'propput'],
        HRESULT,
        'property',
        (['in', 'optional'], DNC_DATAENTRY_PROPKIND, 'kind', 0),
        (['in'], POINTER(IJHDataEntryProperty2), 'ppProperty')
    ),
    COMMETHOD(
        [dispid(17), helpstring('property ppPropertyList'), 'propget'],
        HRESULT,
        'propertyList2',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty2List)),
            'ppPropertyList',
        )
    ),
    COMMETHOD(
        [dispid(18), helpstring('Get all properties of this entry from the server')],
        HRESULT,
        'GetPropertyList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty2List)),
            'ppPropertyList',
        )
    ),
    COMMETHOD(
        [dispid(19), helpstring('return value of the selected stored property'), 'propget'],
        HRESULT,
        'propertyValue',
        (['in', 'optional'], DNC_DATAENTRY_PROPKIND, 'kind', 0),
        (['out', 'retval'], POINTER(VARIANT), 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(19), helpstring('return value of the selected stored property'), 'propput'],
        HRESULT,
        'propertyValue',
        (['in', 'optional'], DNC_DATAENTRY_PROPKIND, 'kind', 0),
        (['in'], VARIANT, 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(20), helpstring('return reference to the selected stored child entry'), 'propget'],
        HRESULT,
        'child',
        (['in'], BSTR, 'bstrChildIdent'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2)), 'ppChild')
    ),
    COMMETHOD(
        [dispid(21), helpstring('property childList'), 'propget'],
        HRESULT,
        'childList2',
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2List)), 'ppChildList')
    ),
    COMMETHOD(
        [dispid(22), helpstring('add a new empty child to the child list, and return its interface')],
        HRESULT,
        'add_child',
        (['in'], BSTR, 'bstrChildName'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2)), 'ppNewChild')
    ),
    COMMETHOD(
        [dispid(23), helpstring('create and return a deep-copy of the whole tree')],
        HRESULT,
        'cloneTree',
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2)), 'ppClonedTree')
    ),
    COMMETHOD(
        [dispid(24), helpstring('read/update stored property values for whole tree from server')],
        HRESULT,
        'ReadTreeValues',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind')
    ),
    COMMETHOD(
        [dispid(25), helpstring('write stored property value for whole tree to server')],
        HRESULT,
        'WriteTreeValues',
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(26), helpstring('Get all children of this entry from the server')],
        HRESULT,
        'GetChildList',
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2List)), 'ppChildList')
    ),
]

################################################################
# code template for IJHDataEntry2 implementation
# class IJHDataEntry2_Impl(object):
#     def Subscribe2(self):
#         'Subscribe for events on this data entry'
#         #return pSubscriptionHandle
#
#     def Subscribe2WithTrigger(self, pITriggerCondition, pITriggerSampling):
#         'Subscribe for events on this data entry, with specific trigger conditions'
#         #return pSubscriptionHandle
#
#     @property
#     def asString(self):
#         'return the asString setting'
#         #return pAsString
#
#     @property
#     def unitSelect(self):
#         'return the unit select setting'
#         #return pUnit
#
#     def ReadPropertyValue(self, kind):
#         'read/update stored property value from server'
#         #return 
#
#     def WritePropertyValue(self, kind, bWithFlush):
#         'write stored property value to server'
#         #return 
#
#     def GetPropertyValue(self, kind):
#         'read/update stored property value from server and return it'
#         #return pPropertyValue
#
#     def SetPropertyValue(self, kind, propertyValue, bWithFlush):
#         'write/update given value to stored property value and write it to server'
#         #return 
#
#     def _get(self, kind):
#         'return reference to the selected stored property'
#         #return ppProperty
#     def _set(self, kind, ppProperty):
#         'return reference to the selected stored property'
#     property = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def propertyList2(self):
#         'property ppPropertyList'
#         #return ppPropertyList
#
#     def GetPropertyList(self):
#         'Get all properties of this entry from the server'
#         #return ppPropertyList
#
#     def _get(self, kind):
#         'return value of the selected stored property'
#         #return pPropertyValue
#     def _set(self, kind, pPropertyValue):
#         'return value of the selected stored property'
#     propertyValue = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def child(self, bstrChildIdent):
#         'return reference to the selected stored child entry'
#         #return ppChild
#
#     @property
#     def childList2(self):
#         'property childList'
#         #return ppChildList
#
#     def add_child(self, bstrChildName):
#         'add a new empty child to the child list, and return its interface'
#         #return ppNewChild
#
#     def cloneTree(self):
#         'create and return a deep-copy of the whole tree'
#         #return ppClonedTree
#
#     def ReadTreeValues(self, kind):
#         'read/update stored property values for whole tree from server'
#         #return 
#
#     def WriteTreeValues(self, bWithFlush):
#         'write stored property value for whole tree to server'
#         #return 
#
#     def GetChildList(self):
#         'Get all children of this entry from the server'
#         #return ppChildList
#

IJHAutomatic._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method to start a NC program'), 'hidden'],
        HRESULT,
        'StartProgram0',
        (['in'], BSTR, 'bstrProgramName')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Retrieving the actual program status')],
        HRESULT,
        'GetProgramStatus',
        (['out', 'retval'], POINTER(DNC_STS_PROGRAM), 'pProgramStatus')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Retrieving the actual DNC mode')],
        HRESULT,
        'GetDncMode',
        (['out', 'retval'], POINTER(DNC_MODE), 'pDncMode')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Method to initiate a Clear Control on the CNC')],
        HRESULT,
        'ClearControl',
    ),
    COMMETHOD(
        [dispid(5), helpstring('Retrieving the override values')],
        HRESULT,
        'GetOverrideInfo',
        (['in', 'out'], POINTER(VARIANT), 'pFeed'),
        (['in', 'out'], POINTER(VARIANT), 'pSpeed'),
        (['in', 'out'], POINTER(VARIANT), 'pRapid')
    ),
    COMMETHOD(
        [dispid(6), helpstring('Retrieving the point of execution of the program in progress')],
        HRESULT,
        'GetExecutionPoint',
        (['in', 'out'], POINTER(VARIANT), 'pSelectedProgram'),
        (['out', 'retval'], POINTER(POINTER(IJHProgramPositionList)), 'ppList')
    ),
    COMMETHOD(
        [dispid(8), helpstring('Retrieving the current position of the tool (cutter) location')],
        HRESULT,
        'GetCutterLocation',
        (['in'], c_int, 'lChannel'),
        (['out', 'retval'], POINTER(POINTER(IJHCutterLocationList)), 'ppList')
    ),
    COMMETHOD(
        [dispid(9), helpstring('Sets a new value for the feed-override')],
        HRESULT,
        'SetOverrideFeed',
        (['in'], c_int, 'lPercentage')
    ),
    COMMETHOD(
        [dispid(10), helpstring('Sets a new value for the rapid-override')],
        HRESULT,
        'SetOverrideRapid',
        (['in'], c_int, 'lPercentage')
    ),
    COMMETHOD(
        [dispid(11), helpstring('Sets a new value for the speed-override')],
        HRESULT,
        'SetOverrideSpeed',
        (['in'], c_int, 'lPercentage')
    ),
    COMMETHOD(
        [dispid(12), helpstring('method GetExecutionMode')],
        HRESULT,
        'GetExecutionMode',
        (['out', 'retval'], POINTER(DNC_EXEC_MODE), 'pExecutionMode')
    ),
]

################################################################
# code template for IJHAutomatic implementation
# class IJHAutomatic_Impl(object):
#     def StartProgram0(self, bstrProgramName):
#         'method to start a NC program'
#         #return 
#
#     def GetProgramStatus(self):
#         'Retrieving the actual program status'
#         #return pProgramStatus
#
#     def GetDncMode(self):
#         'Retrieving the actual DNC mode'
#         #return pDncMode
#
#     def ClearControl(self):
#         'Method to initiate a Clear Control on the CNC'
#         #return 
#
#     def GetOverrideInfo(self):
#         'Retrieving the override values'
#         #return pFeed, pSpeed, pRapid
#
#     def GetExecutionPoint(self):
#         'Retrieving the point of execution of the program in progress'
#         #return pSelectedProgram, ppList
#
#     def GetCutterLocation(self, lChannel):
#         'Retrieving the current position of the tool (cutter) location'
#         #return ppList
#
#     def SetOverrideFeed(self, lPercentage):
#         'Sets a new value for the feed-override'
#         #return 
#
#     def SetOverrideRapid(self, lPercentage):
#         'Sets a new value for the rapid-override'
#         #return 
#
#     def SetOverrideSpeed(self, lPercentage):
#         'Sets a new value for the speed-override'
#         #return 
#
#     def GetExecutionMode(self):
#         'method GetExecutionMode'
#         #return pExecutionMode
#

IJHAutomatic2._methods_ = [
    COMMETHOD(
        [dispid(13), helpstring('Calculate and store the relation between the Workpiece Coordinate System (WCS) and the CNC Coordinate System (MCS)')],
        HRESULT,
        'StorePreset',
        (['in'], c_int, 'lChannel'),
        (['in'], c_int, 'lPresetEntry'),
        (['in'], POINTER(IJHAxisPositionList), 'mcsPositions'),
        (['in'], POINTER(IJHAxisPositionList), 'wcsPositions'),
        (['in'], POINTER(IJHAxisPositionList), 'wcsRotations')
    ),
    COMMETHOD(
        [dispid(14), helpstring('method SetExecutionMode')],
        HRESULT,
        'SetExecutionMode',
        (['in'], DNC_EXEC_MODE, 'executionMode')
    ),
    COMMETHOD(
        [dispid(15), helpstring('method StartProgram')],
        HRESULT,
        'StartProgram',
        (['in'], BSTR, 'bstrProgramName'),
        (['in', 'optional'], POINTER(VARIANT), 'pBreakConditionList')
    ),
]

################################################################
# code template for IJHAutomatic2 implementation
# class IJHAutomatic2_Impl(object):
#     def StorePreset(self, lChannel, lPresetEntry, mcsPositions, wcsPositions, wcsRotations):
#         'Calculate and store the relation between the Workpiece Coordinate System (WCS) and the CNC Coordinate System (MCS)'
#         #return 
#
#     def SetExecutionMode(self, executionMode):
#         'method SetExecutionMode'
#         #return 
#
#     def StartProgram(self, bstrProgramName, pBreakConditionList):
#         'method StartProgram'
#         #return 
#


class IJHCutterPosition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHCutterPosition Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{450D5A57-72FB-4FAD-8479-978C683ACC28}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_pCutterLocationList(self) -> 'IJHCutterLocation2List': ...
        def _set_pCutterLocationList(self, ppCutterLocationList: hints.Incomplete) -> hints.Hresult: ...
        pCutterLocationList = hints.normal_property(_get_pCutterLocationList, _set_pCutterLocationList)
        def _get_pCutterOrientation1(self) -> 'IJHAxisPositionList': ...
        def _set_pCutterOrientation1(self, ppCutterOrientation1: hints.Incomplete) -> hints.Hresult: ...
        pCutterOrientation1 = hints.normal_property(_get_pCutterOrientation1, _set_pCutterOrientation1)
        def _get_pCutterOrientation2(self) -> 'IJHAxisPositionList': ...
        def _set_pCutterOrientation2(self, ppCutterOrientation2: hints.Incomplete) -> hints.Hresult: ...
        pCutterOrientation2 = hints.normal_property(_get_pCutterOrientation2, _set_pCutterOrientation2)


class IJHToolId(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHToolId Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{B089A571-426E-4713-8F46-EEA9636427DA}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_lToolId(self) -> hints.Incomplete: ...
        def _set_lToolId(self, plToolId: hints.Incomplete) -> hints.Hresult: ...
        lToolId = hints.normal_property(_get_lToolId, _set_lToolId)
        def _get_lSpareToolId(self) -> hints.Incomplete: ...
        def _set_lSpareToolId(self, plSpareToolId: hints.Incomplete) -> hints.Hresult: ...
        lSpareToolId = hints.normal_property(_get_lSpareToolId, _set_lSpareToolId)
        def _get_lIndex(self) -> hints.Incomplete: ...
        def _set_lIndex(self, plIndex: hints.Incomplete) -> hints.Hresult: ...
        lIndex = hints.normal_property(_get_lIndex, _set_lIndex)


IJHAutomatic3._methods_ = [
    COMMETHOD(
        [dispid(16), helpstring('(Un)Select ((un)load) an NC program for execution')],
        HRESULT,
        'SelectProgram',
        (['in'], c_int, 'lChannel'),
        (['in'], BSTR, 'bstrProgramName'),
        (['in', 'optional'], VARIANT, 'varlStartBlockNumber')
    ),
    COMMETHOD(
        [dispid(17), helpstring('Stop the execution of an NC program')],
        HRESULT,
        'StopProgram',
        (['in'], c_int, 'lChannel'),
        (['in'], VARIANT_BOOL, 'bOnBlockEnd')
    ),
    COMMETHOD(
        [dispid(18), helpstring('Cancels the execution of a stopped NC program')],
        HRESULT,
        'CancelProgram',
        (['in'], c_int, 'lChannel')
    ),
    COMMETHOD(
        [dispid(19), helpstring('Convert a tool (tip) position in the Workpiece Coordinate System into a position in the Machine Coordinate System.'), 'hidden'],
        HRESULT,
        'GetMachinePositionsFromCutterPosition',
        (['in'], c_int, 'lChannel'),
        (['in'], POINTER(IJHCutterPosition), 'pWcsPosition'),
        (['in'], POINTER(IJHToolId), 'pToolToUse'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionListList)),
            'ppMcsPositionList',
        )
    ),
]

################################################################
# code template for IJHAutomatic3 implementation
# class IJHAutomatic3_Impl(object):
#     def SelectProgram(self, lChannel, bstrProgramName, varlStartBlockNumber):
#         '(Un)Select ((un)load) an NC program for execution'
#         #return 
#
#     def StopProgram(self, lChannel, bOnBlockEnd):
#         'Stop the execution of an NC program'
#         #return 
#
#     def CancelProgram(self, lChannel):
#         'Cancels the execution of a stopped NC program'
#         #return 
#
#     def GetMachinePositionsFromCutterPosition(self, lChannel, pWcsPosition, pToolToUse):
#         'Convert a tool (tip) position in the Workpiece Coordinate System into a position in the Machine Coordinate System.'
#         #return ppMcsPositionList
#

IJHAutomatic4._methods_ = [
    COMMETHOD(
        [dispid(20), helpstring('Create tool usage lists (.H.T.DEP) by importing a client supplied CSV file (without program simulation)')],
        HRESULT,
        'ImportToolUsageCSV',
        (['in'], c_int, 'lChannel'),
        (['in'], BSTR, 'bstrToolUsageCSVName')
    ),
]

################################################################
# code template for IJHAutomatic4 implementation
# class IJHAutomatic4_Impl(object):
#     def ImportToolUsageCSV(self, lChannel, bstrToolUsageCSVName):
#         'Create tool usage lists (.H.T.DEP) by importing a client supplied CSV file (without program simulation)'
#         #return 
#


class JHTestEvents(CoClass):
    """JHTestEvents Class"""
    _reg_clsid_ = GUID('{944A209D-9091-4CC2-9B8C-12F0DE94E59F}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _DJHTestEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHTestEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{EC2DFDA5-6CAA-4EE1-B117-AFBC11D1F501}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnRequestUnlockKeyboard(self) -> hints.Incomplete: ...
        def OnGuiProcessStateChanged(self, bstrGuiProcessName: hints.Incomplete, bstrNewState: hints.Incomplete) -> hints.Incomplete: ...
        def OnGuiProcessGotFocus(self, bstrGuiProcessName: hints.Incomplete) -> hints.Incomplete: ...


JHTestEvents._com_interfaces_ = [IEventObject]
JHTestEvents._outgoing_interfaces_ = [_DJHTestEvents, _IJHTestEvents]

IJHDataEntryProperty2List._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHDataEntryProperty2 object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty2)),
            'ppDataEntryProperty',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [dispid(2), helpstring('add new property to the list')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHDataEntryProperty2), 'pDataEntryProperty')
    ),
    COMMETHOD(
        [dispid(10), helpstring('retrieve property object of given kind'), 'propget'],
        HRESULT,
        'property',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDataEntryProperty2)),
            'ppDataEntryProperty',
        )
    ),
    COMMETHOD(
        [dispid(11), helpstring('retrieve property value of given kind'), 'propget'],
        HRESULT,
        'propertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['out', 'retval'], POINTER(VARIANT), 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(12), helpstring('read/update stored property value from server')],
        HRESULT,
        'ReadPropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind')
    ),
    COMMETHOD(
        [dispid(13), helpstring('write stored property value to server')],
        HRESULT,
        'WritePropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(14), helpstring('read/update stored property value from server and return it')],
        HRESULT,
        'GetPropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['out', 'retval'], POINTER(VARIANT), 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(15), helpstring('write/update given value to stored property value and write it to server')],
        HRESULT,
        'SetPropertyValue',
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['in'], VARIANT, 'propertyValue'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
]

################################################################
# code template for IJHDataEntryProperty2List implementation
# class IJHDataEntryProperty2List_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHDataEntryProperty2 object on the specified index in the list'
#         #return ppDataEntryProperty
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#
#     def AddItem(self, pDataEntryProperty):
#         'add new property to the list'
#         #return 
#
#     @property
#     def property(self, kind):
#         'retrieve property object of given kind'
#         #return ppDataEntryProperty
#
#     @property
#     def propertyValue(self, kind):
#         'retrieve property value of given kind'
#         #return pPropertyValue
#
#     def ReadPropertyValue(self, kind):
#         'read/update stored property value from server'
#         #return 
#
#     def WritePropertyValue(self, kind, bWithFlush):
#         'write stored property value to server'
#         #return 
#
#     def GetPropertyValue(self, kind):
#         'read/update stored property value from server and return it'
#         #return pPropertyValue
#
#     def SetPropertyValue(self, kind, propertyValue, bWithFlush):
#         'write/update given value to stored property value and write it to server'
#         #return 
#


class JHAxisPosition(CoClass):
    """JHAxisPosition Class"""
    _reg_clsid_ = GUID('{FD6628A6-CC5B-4BBC-BC48-6525BB0D3CEC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHAxisPosition(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAxisPosition Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{CC11EE72-FCBE-49DF-A1FB-C2BE8B7742DA}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_dPosition(self) -> hints.Incomplete: ...
        def _set_dPosition(self, pdPosition: hints.Incomplete) -> hints.Hresult: ...
        dPosition = hints.normal_property(_get_dPosition, _set_dPosition)
        def _get_lAxisId(self) -> hints.Incomplete: ...
        def _set_lAxisId(self, plAxisId: hints.Incomplete) -> hints.Hresult: ...
        lAxisId = hints.normal_property(_get_lAxisId, _set_lAxisId)


JHAxisPosition._com_interfaces_ = [IJHAxisPosition, IJHLoggingInternal]


class JHDiagnosticsEvents(CoClass):
    """JHDiagnosticsEvents Class"""
    _reg_clsid_ = GUID('{D6559CF2-1113-4B86-B77D-FA6D304A2D7A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _DJHDiagnosticsEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """_DJHDiagnosticsEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{D8ADD783-52CE-4A50-AECA-A5A6E3BE5A3D}')
    _idlflags_ = []
    _methods_ = []

    if TYPE_CHECKING:  # dispmembers
        def OnServiceFileCreated(self, result: hints.Incomplete) -> hints.Incomplete: ...


class _IJHDiagnosticsEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHDiagnosticsEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{342F1196-02DA-4126-A27E-EEA70F92085E}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnServiceFileCreated(self, result: hints.Incomplete) -> hints.Hresult: ...


JHDiagnosticsEvents._com_interfaces_ = [IEventObject]
JHDiagnosticsEvents._outgoing_interfaces_ = [_DJHDiagnosticsEvents, _IJHDiagnosticsEvents]


class JHRemoteErrorEvents(CoClass):
    """JHRemoteErrorEvents Class"""
    _reg_clsid_ = GUID('{EC5E42DD-8D58-41C0-9C28-F3876110BB28}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _IJHRemoteErrorEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHRemoteErrorEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{750585F1-59F3-425C-AEA0-97C1E971A9F0}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnRemoveRequest(self, pRemoteErrorEntry: hints.Incomplete) -> hints.Hresult: ...


JHRemoteErrorEvents._com_interfaces_ = [IEventObject]
JHRemoteErrorEvents._outgoing_interfaces_ = [_DJHRemoteErrorEvents, _IJHRemoteErrorEvents]


class IJHErrorEntryList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHErrorEntryList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{76C526D7-FC22-4837-8ADA-EA406D0FDA1E}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, index: hints.Incomplete) -> 'IJHErrorEntry': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


IJHErrorEntryList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHErrorEntry object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'index'),
        (['out', 'retval'], POINTER(POINTER(IJHErrorEntry)), 'ppErrorEntry')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pNrOfElements')
    ),
]

################################################################
# code template for IJHErrorEntryList implementation
# class IJHErrorEntryList_Impl(object):
#     @property
#     def Item(self, index):
#         'JHErrorEntry object on the specified index in the list'
#         #return ppErrorEntry
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pNrOfElements
#


class JHTraceSampleListList(CoClass):
    """JHTraceSampleListList Class"""
    _reg_clsid_ = GUID('{5F25867F-B93B-48A9-B6D7-2A5FB6EECE4F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHTraceSampleListList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceSampleListList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{C7977157-3D9C-4E01-A51C-573231CDE79B}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHTraceSampleList': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def GetSampleListByTraceChannelId(self, traceChannelId: hints.Incomplete) -> 'IJHTraceSampleList': ...


JHTraceSampleListList._com_interfaces_ = [IJHTraceSampleListList, IJHLoggingInternal]

_DJHDiagnosticsEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Signals service file is ready to be retrieved')],
        HRESULT,
        'OnServiceFileCreated',
        (['in'], HRESULT, 'result')
    ),
]


class JHCutterLocation2List(CoClass):
    """JHCutterLocation2List Class"""
    _reg_clsid_ = GUID('{FEB9D368-B78D-42BB-ABA0-F5C6EBCB336C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHCutterLocation2List(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHCutterLocation2List Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{681A39DC-EBD9-42E9-B2FE-527E72BC1E93}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHCutterLocation2': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def AddItem(self, pCutterLocation: hints.Incomplete) -> hints.Hresult: ...
        def RemoveItem(self, index: hints.Incomplete) -> hints.Hresult: ...


JHCutterLocation2List._com_interfaces_ = [IJHCutterLocation2List, IJHLoggingInternal]


class JHDirectoryEntry(CoClass):
    """JHDirectoryEntry Class"""
    _reg_clsid_ = GUID('{8B7D1EFA-A06C-4B5F-84D6-86AF51234D79}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHDirectoryEntry(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDirectoryEntry Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{30120162-005B-4F40-A38E-F1C6E26924DA}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_name(self) -> hints.Incomplete: ...
        name = hints.normal_property(_get_name)
        def _get_size(self) -> hints.Incomplete: ...
        size = hints.normal_property(_get_size)
        def _get_attributes(self) -> 'IJHFileAttributes': ...
        attributes = hints.normal_property(_get_attributes)
        def _get_dateTime(self) -> hints.Incomplete: ...
        dateTime = hints.normal_property(_get_dateTime)


JHDirectoryEntry._com_interfaces_ = [IJHDirectoryEntry, IJHLoggingInternal]


class IJHSoftwareVersionList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHSoftwareVersionList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{767579FC-1C6E-4FA8-B700-32BE11099021}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHSoftwareVersion': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


IJHVersion._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieving the versions of the used software')],
        HRESULT,
        'GetVersionNcSoftware',
        (['out', 'retval'], POINTER(POINTER(IJHSoftwareVersionList)), 'ppList')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Retrieving the System Identification Key')],
        HRESULT,
        'GetSik',
        (['out', 'retval'], POINTER(BSTR), 'pbstrSIK')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Retrieve the version of the HeidenhainDNC component')],
        HRESULT,
        'GetVersionComInterface',
        (['out', 'retval'], POINTER(BSTR), 'pbstrComInterfaceVersion')
    ),
]

################################################################
# code template for IJHVersion implementation
# class IJHVersion_Impl(object):
#     def GetVersionNcSoftware(self):
#         'Retrieving the versions of the used software'
#         #return ppList
#
#     def GetSik(self):
#         'Retrieving the System Identification Key'
#         #return pbstrSIK
#
#     def GetVersionComInterface(self):
#         'Retrieve the version of the HeidenhainDNC component'
#         #return pbstrComInterfaceVersion
#


class IJHTrace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTrace Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{CCBC9BFD-DEA3-4A33-BB92-46B80FE97A53}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetAvailableTraceChannels(self) -> 'IJHTraceChannelList': ...
        def GetAvailableTraceVariables(self) -> 'IJHTraceVariableList': ...
        def StartTracing(self) -> hints.Hresult: ...
        def GetTraceData(self) -> 'IJHTraceSampleListList': ...
        def StopTracing(self) -> hints.Hresult: ...


class IJHTraceVariableList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceVariableList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{2BC344E4-6F90-4F47-938D-9F185ECDEDB6}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHTraceVariable': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)
        def GetVariableById(self, traceVariableId: hints.Incomplete) -> 'IJHTraceVariable': ...
        def GetVariableByName(self, bstrTraceVariableName: hints.Incomplete) -> 'IJHTraceVariable': ...


IJHTrace._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method to retrieve the available trace channels')],
        HRESULT,
        'GetAvailableTraceChannels',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceChannelList)),
            'ppITraceChannelList',
        )
    ),
    COMMETHOD(
        [dispid(2), helpstring('method GetAvailableTraceVariables')],
        HRESULT,
        'GetAvailableTraceVariables',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceVariableList)),
            'ppITraceVariableList',
        )
    ),
    COMMETHOD(
        [dispid(3), helpstring('method StartTracing')],
        HRESULT,
        'StartTracing',
    ),
    COMMETHOD(
        [dispid(4), helpstring('method GetTraceData')],
        HRESULT,
        'GetTraceData',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceSampleListList)),
            'ppITraceSampleListList',
        )
    ),
    COMMETHOD(
        [dispid(5), helpstring('method StopTracing')],
        HRESULT,
        'StopTracing',
    ),
]

################################################################
# code template for IJHTrace implementation
# class IJHTrace_Impl(object):
#     def GetAvailableTraceChannels(self):
#         'method to retrieve the available trace channels'
#         #return ppITraceChannelList
#
#     def GetAvailableTraceVariables(self):
#         'method GetAvailableTraceVariables'
#         #return ppITraceVariableList
#
#     def StartTracing(self):
#         'method StartTracing'
#         #return 
#
#     def GetTraceData(self):
#         'method GetTraceData'
#         #return ppITraceSampleListList
#
#     def StopTracing(self):
#         'method StopTracing'
#         #return 
#


class JHAxisPositionEnum(CoClass):
    """JHAxisPositionEnum Class"""
    _reg_clsid_ = GUID('{2B60DE83-F8AC-4557-A8B5-73604F2684D1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAxisPositionEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHPlcEvents(CoClass):
    """JHPlcEvents Class"""
    _reg_clsid_ = GUID('{4F71BFD9-C957-480E-830E-04C5EC4DAE22}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class _IJHPlcEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    """_IJHPlcEvents Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{C54463C4-F918-4743-86CC-23D004848691}')
    _idlflags_ = []

    if TYPE_CHECKING:  # commembers
        def OnPlcData(self, bstrPlcString: hints.Incomplete, ppsalPlcMarkers: hints.Incomplete, ppsalPlcDWords: hints.Incomplete) -> hints.Hresult: ...


JHPlcEvents._com_interfaces_ = [IEventObject]
JHPlcEvents._outgoing_interfaces_ = [_DJHPlcEvents, _IJHPlcEvents]

IJHSoftwareVersionList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHSoftwareVersion object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHSoftwareVersion)),
            'ppSoftwareVersion',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHSoftwareVersionList implementation
# class IJHSoftwareVersionList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHSoftwareVersion object on the specified index in the list'
#         #return ppSoftwareVersion
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#


class IJHTrigger(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTrigger Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{127B2ED3-EA0E-4DFC-ADED-EF3F6C45DCD9}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetInterface(self, requestedInterface: hints.Incomplete) -> hints.Incomplete: ...
        def SetTriggerSequence(self, triggerSequence: hints.Incomplete) -> hints.Hresult: ...
        def SetTriggerSource(self, pIDataEntry: hints.Incomplete) -> hints.Hresult: ...
        def _get_triggerSequence(self) -> hints.Incomplete: ...
        triggerSequence = hints.normal_property(_get_triggerSequence)
        def _get_triggerSource(self) -> 'IJHDataEntry': ...
        triggerSource = hints.normal_property(_get_triggerSource)



IJHTrigger._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method GetInterface')],
        HRESULT,
        'GetInterface',
        (['in'], DNC_TRIG_INTERFACE, 'requestedInterface'),
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppInterface')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method SetTriggerSequence')],
        HRESULT,
        'SetTriggerSequence',
        (['in'], DNC_TRIG_SEQUENCE, 'triggerSequence')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method SetTriggerSource')],
        HRESULT,
        'SetTriggerSource',
        (['in'], POINTER(IJHDataEntry), 'pIDataEntry')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property triggerSequence'), 'propget'],
        HRESULT,
        'triggerSequence',
        (['out', 'retval'], POINTER(DNC_TRIG_SEQUENCE), 'pSequence')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property triggerSource'), 'propget'],
        HRESULT,
        'triggerSource',
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry)), 'ppIDataEntry')
    ),
]

################################################################
# code template for IJHTrigger implementation
# class IJHTrigger_Impl(object):
#     def GetInterface(self, requestedInterface):
#         'method GetInterface'
#         #return ppInterface
#
#     def SetTriggerSequence(self, triggerSequence):
#         'method SetTriggerSequence'
#         #return 
#
#     def SetTriggerSource(self, pIDataEntry):
#         'method SetTriggerSource'
#         #return 
#
#     @property
#     def triggerSequence(self):
#         'property triggerSequence'
#         #return pSequence
#
#     @property
#     def triggerSource(self):
#         'property triggerSource'
#         #return ppIDataEntry
#


class JHBreakConditionEnum(CoClass):
    """JHBreakConditionEnum Class"""
    _reg_clsid_ = GUID('{DE0BE30E-D14A-46FF-8F3D-472FBF1910F2}')
    _idlflags_ = ['hidden']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHBreakConditionEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class IJHTraceChannel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceChannel Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{6D5102B4-21B1-4658-8CE4-8CE00238B627}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_bEnabled(self) -> hints.Incomplete: ...
        def _set_bEnabled(self, pbEnabled: hints.Incomplete) -> hints.Hresult: ...
        bEnabled = hints.normal_property(_get_bEnabled, _set_bEnabled)
        def _get_lTraceChannelId(self) -> hints.Incomplete: ...
        lTraceChannelId = hints.normal_property(_get_lTraceChannelId)
        def _get_TraceVariable(self) -> 'IJHTraceVariable': ...
        TraceVariable = hints.normal_property(_get_TraceVariable)
        def SelectVariable(self, pTraceVariable: hints.Incomplete) -> hints.Hresult: ...


IJHTraceChannelList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('Property to retrieve a TraceChannel object (zero-based)'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHTraceChannel)), 'ppTraceChannel')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of elements (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'plNrOfChannels')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method GetChannel')],
        HRESULT,
        'GetChannel',
        (['in'], c_int, 'traceChannelId'),
        (['out', 'retval'], POINTER(POINTER(IJHTraceChannel)), 'ppTraceChannel')
    ),
]

################################################################
# code template for IJHTraceChannelList implementation
# class IJHTraceChannelList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'Property to retrieve a TraceChannel object (zero-based)'
#         #return ppTraceChannel
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of elements (0 to count -1)'
#         #return plNrOfChannels
#
#     def GetChannel(self, traceChannelId):
#         'method GetChannel'
#         #return ppTraceChannel
#

IJHSoftwareVersion._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property softwareType'), 'propget'],
        HRESULT,
        'softwareType',
        (['out', 'retval'], POINTER(DNC_SW_TYPE), 'pSoftwareType')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property Software Name'), 'propget'],
        HRESULT,
        'bstrSoftwareType',
        (['out', 'retval'], POINTER(BSTR), 'pbstrSoftwareType')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property bstrIdentNr'), 'propget'],
        HRESULT,
        'bstrIdentNr',
        (['out', 'retval'], POINTER(BSTR), 'pbstrIdentNumber')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property bstrDescription'), 'propget'],
        HRESULT,
        'bstrDescription',
        (['out', 'retval'], POINTER(BSTR), 'pbstrDescription')
    ),
]

################################################################
# code template for IJHSoftwareVersion implementation
# class IJHSoftwareVersion_Impl(object):
#     @property
#     def softwareType(self):
#         'property softwareType'
#         #return pSoftwareType
#
#     @property
#     def bstrSoftwareType(self):
#         'property Software Name'
#         #return pbstrSoftwareType
#
#     @property
#     def bstrIdentNr(self):
#         'property bstrIdentNr'
#         #return pbstrIdentNumber
#
#     @property
#     def bstrDescription(self):
#         'property bstrDescription'
#         #return pbstrDescription
#


class JHDataAccess(CoClass):
    """JHDataAccess Class"""
    _reg_clsid_ = GUID('{69B9E1AF-7530-41BF-BCCB-71828DD0D0EE}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHDataAccess(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataAccess Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{932CCA6F-11B3-470C-A399-5AED665A23A0}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetDataEntry(self, bstrDataSelection: hints.Incomplete) -> 'IJHDataEntry': ...


class IJHDataAccess2(IJHDataAccess):
    """IJHDataAccess2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{C195736F-EF3E-4152-83CE-63003E010FBD}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SetAccessMode(self, accessMode: hints.Incomplete, bstrPassword: hints.Incomplete) -> hints.Hresult: ...


class IJHDataAccess3(IJHDataAccess2):
    """IJHDataAccess3 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{FCCCC580-4A70-4C64-9579-6A4338E36CD4}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetDataEntry2(self, bstrDataSelection: hints.Incomplete, unitSelect: hints.Incomplete, asString: hints.Incomplete) -> 'IJHDataEntry2': ...
        def LockTable(self, bstrTableSelection: hints.Incomplete) -> hints.Incomplete: ...
        def UnlockTable(self, lockHandle: hints.Incomplete) -> hints.Hresult: ...


class IJHDataAccess4(IJHDataAccess3):
    """IJHDataAccess4 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{D5AC09FE-C9BD-4035-B02F-C7A61FEC97EE}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def AddDataEntry(self, bstrFullIdent: hints.Incomplete, varbstrStoragePath: hints.Incomplete = ...) -> hints.Hresult: ...
        def RemoveDataEntry(self, bstrFullIdent: hints.Incomplete) -> hints.Hresult: ...
        def LockConfig(self, bstrIdentsToLock: hints.Incomplete, ppsafLockResults: hints.Incomplete) -> hints.Incomplete: ...
        def UnlockConfig(self, bstrIdentsToUnlock: hints.Incomplete, ppsafUnlockResults: hints.Incomplete) -> hints.Incomplete: ...
        def SetPlcOption(self, plcOption: hints.Incomplete, bActivate: hints.Incomplete) -> hints.Hresult: ...


class IJHDataAccessInternal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDataAccessInternal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{B9DFE360-2ED0-4C05-AFCB-E3128371B507}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _AddBranches(self, pIParentEntry: hints.Incomplete, ppIChildList: hints.Incomplete) -> 'IJHDataEntryList': ...
        def _AddProperties(self, pIDataEntry: hints.Incomplete, ppIPropertyList: hints.Incomplete) -> 'IJHDataEntryPropertyList': ...
        def _Subscribe(self, pIDataEntry: hints.Incomplete, pITriggerCondition: hints.Incomplete, pITriggerSampling: hints.Incomplete) -> hints.Incomplete: ...
        def _get_propertyValue(self, bstrFullPathName: hints.Incomplete) -> hints.Incomplete: ...
        def _put_propertyValue(self, bstrFullPathName: hints.Incomplete, varNewPropertyVal: hints.Incomplete) -> hints.Hresult: ...
        def _UnSubscribe(self, lSubscribeHandle: hints.Incomplete) -> hints.Hresult: ...
        def _GetPropertyValue(self, bstrFullPathName: hints.Incomplete, kind: hints.Incomplete, unitSelect: hints.Incomplete, asString: hints.Incomplete) -> hints.Incomplete: ...
        def _GetPropertyValueList(self, pParentEntry: hints.Incomplete, kind: hints.Incomplete) -> 'IJHDataEntry2': ...
        def _Subscribe2(self, pParentEntry: hints.Incomplete, pITriggerCondition: hints.Incomplete, pITriggerSampling: hints.Incomplete) -> hints.Tuple[hints.Incomplete, 'IJHDataEntry2']: ...
        def _WriteTreeValues(self, pEntry: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def _WritePropertyValue(self, pProperty: hints.Incomplete, bWithFlush: hints.Incomplete) -> hints.Hresult: ...
        def _AddProperties2(self, a_pIJHDataEntry: hints.Incomplete, ppIJHDataEntryPropertyList: hints.Incomplete) -> 'IJHDataEntryProperty2List': ...
        def _AddBranches2(self, pIParentEntry: hints.Incomplete, ppIJHDataEntryList: hints.Incomplete) -> 'IJHDataEntry2List': ...


JHDataAccess._com_interfaces_ = [IJHDataAccess4, IJHDataAccessInternal]
JHDataAccess._outgoing_interfaces_ = [_DJHDataAccessEvents, _IJHDataAccessEvents2]


class JHCutterLocation(CoClass):
    """JHCutterLocation Class"""
    _reg_clsid_ = GUID('{768BB1F4-3200-46C6-AC86-BA255635E86E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHCutterLocation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHCutterLocation Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{396AE105-8166-4B34-B846-9255A8CBD3B4}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_bIsInch(self) -> hints.Incomplete: ...
        bIsInch = hints.normal_property(_get_bIsInch)
        def _get_dPosition(self) -> hints.Incomplete: ...
        dPosition = hints.normal_property(_get_dPosition)
        def _get_bstrCoordinateName(self) -> hints.Incomplete: ...
        bstrCoordinateName = hints.normal_property(_get_bstrCoordinateName)


class IJHCutterLocation2(IJHCutterLocation):
    """IJHCutterLocation2 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{8122A585-029F-4938-91FD-8CF1D5DA3AF0}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _set_bIsInch(self, rhs: hints.Incomplete) -> hints.Hresult: ...
        bIsInch = hints.normal_property(fset=_set_bIsInch)
        def _set_dPosition(self, rhs: hints.Incomplete) -> hints.Hresult: ...
        dPosition = hints.normal_property(fset=_set_dPosition)
        def _set_bstrCoordinateName(self, rhs: hints.Incomplete) -> hints.Hresult: ...
        bstrCoordinateName = hints.normal_property(fset=_set_bstrCoordinateName)


JHCutterLocation._com_interfaces_ = [IJHCutterLocation2, IJHLoggingInternal]


class JHDirectoryEntryEnum(CoClass):
    """JHDirectoryEntryEnum Class"""
    _reg_clsid_ = GUID('{873D762A-D1BE-4394-8A29-F3D228816ADF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDirectoryEntryEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHAxisPositionListEnum(CoClass):
    """JHAxisPositionListEnum Class"""
    _reg_clsid_ = GUID('{2F08C760-9BF6-49F2-B387-269ACEB81A71}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAxisPositionListEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

IJHTraceChannel._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property bEnabled'), 'propget'],
        HRESULT,
        'bEnabled',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbEnabled')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property bEnabled'), 'propput'],
        HRESULT,
        'bEnabled',
        (['in'], VARIANT_BOOL, 'pbEnabled')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property lTraceChannelId'), 'propget'],
        HRESULT,
        'lTraceChannelId',
        (['out', 'retval'], POINTER(c_int), 'plTraceChannelId')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property TraceVariable'), 'propget'],
        HRESULT,
        'TraceVariable',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceVariable)),
            'ppTraceVariable',
        )
    ),
    COMMETHOD(
        [dispid(4), helpstring('method SelectVariable')],
        HRESULT,
        'SelectVariable',
        (['in'], POINTER(IJHTraceVariable), 'pTraceVariable')
    ),
]

################################################################
# code template for IJHTraceChannel implementation
# class IJHTraceChannel_Impl(object):
#     def _get(self):
#         'property bEnabled'
#         #return pbEnabled
#     def _set(self, pbEnabled):
#         'property bEnabled'
#     bEnabled = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def lTraceChannelId(self):
#         'property lTraceChannelId'
#         #return plTraceChannelId
#
#     @property
#     def TraceVariable(self):
#         'property TraceVariable'
#         #return ppTraceVariable
#
#     def SelectVariable(self, pTraceVariable):
#         'method SelectVariable'
#         #return 
#


class JHVirtualMachine(CoClass):
    """IJHVirtualMachine Class"""
    _reg_clsid_ = GUID('{7CD1E2C6-8276-4A08-BD81-2054F408DD11}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHVirtualMachine(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHVirtualMachine Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{EFA34725-E9C9-46FB-B97A-4B3EAC8B9988}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def ActivateTurboMode(self, bActivate: hints.Incomplete) -> hints.Hresult: ...
        def SetTurboFactor(self, dAccelerationFactor: hints.Incomplete) -> hints.Hresult: ...
        def SetPosition(self, lChannel: hints.Incomplete, pMcsPositions: hints.Incomplete) -> 'IJHPositioningResult': ...
        def VerifyPosition(self, lChannel: hints.Incomplete, pMcsPositions: hints.Incomplete, pToolToUse: hints.Incomplete) -> 'IJHPositioningResult': ...
        def GetPosition(self, lChannel: hints.Incomplete) -> 'IJHAxisPositionList': ...


JHVirtualMachine._com_interfaces_ = [IJHVirtualMachine]


class JHTraceSampleListEnum(CoClass):
    """JHTraceSampleListEnum Class"""
    _reg_clsid_ = GUID('{0EFBA4D0-2980-48FA-AC7E-58A8949DC007}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceSampleListEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

_DJHAutomaticEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Signals a program status change')],
        HRESULT,
        'OnProgramStatusChanged',
        (['in'], DNC_EVT_PROGRAM, 'programEvent')
    ),
    DISPMETHOD(
        [dispid(2), helpstring('Signals the change of the DNC-mode')],
        HRESULT,
        'OnDncModeChanged',
        (['in'], DNC_MODE, 'newDncMode')
    ),
    DISPMETHOD(
        [dispid(3), helpstring('method OnExecutionMessage')],
        HRESULT,
        'OnExecutionMessage',
        (['in'], c_int, 'lChannel'),
        (['in'], VARIANT, 'varNumericValue'),
        (['in'], BSTR, 'bstrValue')
    ),
    DISPMETHOD(
        [dispid(4), helpstring('method OnProgramChanged')],
        HRESULT,
        'OnProgramChanged',
        (['in'], c_int, 'lChannel'),
        (['in'], c_double, 'dTimeStamp'),
        (['in'], BSTR, 'bstrNewProgram')
    ),
    DISPMETHOD(
        [dispid(5), helpstring('method OnToolChanged')],
        HRESULT,
        'OnToolChanged',
        (['in'], c_int, 'lChannel'),
        (['in'], POINTER(IJHToolId), 'pidToolOut'),
        (['in'], POINTER(IJHToolId), 'pidToolIn'),
        (['in'], c_double, 'dTimeStamp')
    ),
    DISPMETHOD(
        [dispid(6), helpstring('method OnExecutionModeChanged')],
        HRESULT,
        'OnExecutionModeChanged',
        (['in'], c_int, 'lChannel'),
        (['in'], DNC_EXEC_MODE, 'executionMode')
    ),
]


class JHErrorEvents(CoClass):
    """JHErrorEvents Class"""
    _reg_clsid_ = GUID('{7F18EDB0-B24E-4852-A76A-AB9AEFE0A7D8}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHErrorEvents._com_interfaces_ = [IEventObject]
JHErrorEvents._outgoing_interfaces_ = [_DJHErrorEvents, _IJHErrorEvents, _IJHErrorEvents2]


class JHDataEntryList(CoClass):
    """JHDataEntryList Class"""
    _reg_clsid_ = GUID('{03C779BC-9623-4486-9805-83EE9A0793F1}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryList._com_interfaces_ = [IJHDataEntryList, IJHLoggingInternal]


class JHAxesPositionStreamingEvents(CoClass):
    """JHAxesPositionStreamingEvents Class"""
    _reg_clsid_ = GUID('{107F2325-69B4-4180-B78C-FD76C0120D2A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAxesPositionStreamingEvents._com_interfaces_ = [IEventObject]
JHAxesPositionStreamingEvents._outgoing_interfaces_ = [_DJHAxesPositionStreamingEvents, _IJHAxesPositionStreamingEvents]

IJHTraceVariable._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Clone this object'), 'hidden'],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IJHTraceVariable)), 'ppClone')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property VariableId'), 'propget'],
        HRESULT,
        'VariableId',
        (['out', 'retval'], POINTER(DNC_TRACE_VARIABLE_ID), 'pVariableId')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property bstrVariableName'), 'propget'],
        HRESULT,
        'bstrVariableName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrVariableName')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property VariableType'), 'propget'],
        HRESULT,
        'VariableType',
        (['out', 'retval'], POINTER(DNC_TRACE_VARIABLE_TYPE), 'pVariableType')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property SourceType'), 'propget'],
        HRESULT,
        'SourceType',
        (['out', 'retval'], POINTER(DNC_TRACE_SOURCE_TYPE), 'pSourceType')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property dMaxSamplingRateInMsec'), 'propget'],
        HRESULT,
        'dMaxSamplingRateInMsec',
        (['out', 'retval'], POINTER(c_double), 'pdMaxSamplingRateInMsec')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property bstrDimension'), 'propget'],
        HRESULT,
        'bstrDimension',
        (['out', 'retval'], POINTER(BSTR), 'pbstrDimension')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property bstrDimension'), 'propput'],
        HRESULT,
        'bstrDimension',
        (['in'], BSTR, 'pbstrDimension')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property Dimension'), 'propget'],
        HRESULT,
        'Dimension',
        (['out', 'retval'], POINTER(DNC_DATA_UNIT), 'pDimension')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property Dimension'), 'propput'],
        HRESULT,
        'Dimension',
        (['in'], DNC_DATA_UNIT, 'pDimension')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property lAxisId'), 'propget'],
        HRESULT,
        'lAxisId',
        (['out', 'retval'], POINTER(c_int), 'plAxisId')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property lChannelId'), 'propget'],
        HRESULT,
        'lChannelId',
        (['out', 'retval'], POINTER(c_int), 'plChannelId')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property bstrPath'), 'propget'],
        HRESULT,
        'bstrPath',
        (['out', 'retval'], POINTER(BSTR), 'pbstrPath')
    ),
    COMMETHOD(
        [dispid(12), helpstring('property bPlcPrePgmNotPost'), 'propget'],
        HRESULT,
        'bPlcPrePgmNotPost',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbPlcPrePgmNotPost')
    ),
    COMMETHOD(
        [dispid(13), helpstring('property dSamplingRateInMsec'), 'propget'],
        HRESULT,
        'dSamplingRateInMsec',
        (['out', 'retval'], POINTER(c_double), 'pdSamplingRateInMsec')
    ),
    COMMETHOD(
        [dispid(14), helpstring('method SetTypeNormal')],
        HRESULT,
        'SetTypeNormal',
        (['in'], c_double, 'dSamplingRateInMsec')
    ),
    COMMETHOD(
        [dispid(15), helpstring('method SetTypeAxis')],
        HRESULT,
        'SetTypeAxis',
        (['in'], c_double, 'dSamplingRateInMsec'),
        (['in'], c_int, 'axisId')
    ),
    COMMETHOD(
        [dispid(16), helpstring('method SetTypeChannel')],
        HRESULT,
        'SetTypeChannel',
        (['in'], c_double, 'dSamplingRateInMsec'),
        (['in'], c_int, 'channelId')
    ),
    COMMETHOD(
        [dispid(17), helpstring('method SetTypePath')],
        HRESULT,
        'SetTypePath',
        (['in'], c_double, 'dSamplingRateInMsec'),
        (['in'], BSTR, 'bstrPath')
    ),
    COMMETHOD(
        [dispid(18), helpstring('method SetTypePlcPath')],
        HRESULT,
        'SetTypePlcPath',
        (['in'], c_double, 'dSamplingRateInMsec'),
        (['in'], BSTR, 'bstrPath'),
        (['in'], VARIANT_BOOL, 'bPlcPrePgmNotPost')
    ),
]

################################################################
# code template for IJHTraceVariable implementation
# class IJHTraceVariable_Impl(object):
#     def Clone(self):
#         'Clone this object'
#         #return ppClone
#
#     @property
#     def VariableId(self):
#         'property VariableId'
#         #return pVariableId
#
#     @property
#     def bstrVariableName(self):
#         'property bstrVariableName'
#         #return pbstrVariableName
#
#     @property
#     def VariableType(self):
#         'property VariableType'
#         #return pVariableType
#
#     @property
#     def SourceType(self):
#         'property SourceType'
#         #return pSourceType
#
#     @property
#     def dMaxSamplingRateInMsec(self):
#         'property dMaxSamplingRateInMsec'
#         #return pdMaxSamplingRateInMsec
#
#     def _get(self):
#         'property bstrDimension'
#         #return pbstrDimension
#     def _set(self, pbstrDimension):
#         'property bstrDimension'
#     bstrDimension = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Dimension'
#         #return pDimension
#     def _set(self, pDimension):
#         'property Dimension'
#     Dimension = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def lAxisId(self):
#         'property lAxisId'
#         #return plAxisId
#
#     @property
#     def lChannelId(self):
#         'property lChannelId'
#         #return plChannelId
#
#     @property
#     def bstrPath(self):
#         'property bstrPath'
#         #return pbstrPath
#
#     @property
#     def bPlcPrePgmNotPost(self):
#         'property bPlcPrePgmNotPost'
#         #return pbPlcPrePgmNotPost
#
#     @property
#     def dSamplingRateInMsec(self):
#         'property dSamplingRateInMsec'
#         #return pdSamplingRateInMsec
#
#     def SetTypeNormal(self, dSamplingRateInMsec):
#         'method SetTypeNormal'
#         #return 
#
#     def SetTypeAxis(self, dSamplingRateInMsec, axisId):
#         'method SetTypeAxis'
#         #return 
#
#     def SetTypeChannel(self, dSamplingRateInMsec, channelId):
#         'method SetTypeChannel'
#         #return 
#
#     def SetTypePath(self, dSamplingRateInMsec, bstrPath):
#         'method SetTypePath'
#         #return 
#
#     def SetTypePlcPath(self, dSamplingRateInMsec, bstrPath, bPlcPrePgmNotPost):
#         'method SetTypePlcPath'
#         #return 
#

IJHFileSystem._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieve the total and free space available on the server.')],
        HRESULT,
        'GetDiskSpace',
        (['in'], BSTR, 'bstrPath'),
        (['in', 'out'], POINTER(VARIANT), 'pdFreeSpace'),
        (['in', 'out'], POINTER(VARIANT), 'pdTotalSize')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Retrieve the current directory on the server.')],
        HRESULT,
        'GetCurrentDirectory',
        (['out', 'retval'], POINTER(BSTR), 'pbstrCurDir')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Retrieve file system information. Use this method once to retrieve the attribute definition.')],
        HRESULT,
        'GetFileSystemAttributes',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHFileAttributes)),
            'ppFileAttributes',
        )
    ),
    COMMETHOD(
        [dispid(4), helpstring('Read directory contents, optionally with filter.')],
        HRESULT,
        'ReadDirectory',
        (['in'], BSTR, 'bstrFileName'),
        (['in'], POINTER(IJHFileAttributes), 'pAttributeSelection'),
        (['in'], POINTER(IJHFileAttributes), 'pAttributeState'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDirectoryEntryList)),
            'ppDirEntryList',
        )
    ),
    COMMETHOD(
        [dispid(5), helpstring('Change the current directory on the server.')],
        HRESULT,
        'ChangeDirectory',
        (['in'], BSTR, 'bstrNewDir')
    ),
    COMMETHOD(
        [dispid(6), helpstring('Make a new directory on the server.')],
        HRESULT,
        'MakeDirectory',
        (['in'], BSTR, 'bstrNewDir')
    ),
    COMMETHOD(
        [dispid(7), helpstring('Delete an empty directory on the server.')],
        HRESULT,
        'DeleteDirectory',
        (['in'], BSTR, 'bstrDir')
    ),
    COMMETHOD(
        [dispid(8), helpstring('Delete a file on the server.')],
        HRESULT,
        'DeleteFile',
        (['in'], BSTR, 'bstrFileName')
    ),
    COMMETHOD(
        [dispid(9), helpstring('Rename a file or directory on the server.')],
        HRESULT,
        'Rename',
        (['in'], BSTR, 'bstrOldFileName'),
        (['in'], BSTR, 'bstrNewFileName')
    ),
    COMMETHOD(
        [dispid(10), helpstring('Copy a file on the server to a new file on the server (local copy!).')],
        HRESULT,
        'CopyFile',
        (['in'], BSTR, 'bstrSourceFileName'),
        (['in'], BSTR, 'bstrDestFileName')
    ),
    COMMETHOD(
        [dispid(11), helpstring('Retrieve the first lines of a file')],
        HRESULT,
        'PreviewFile',
        (['in'], BSTR, 'bstrFileName'),
        (['in'], c_int, 'lNrLines'),
        (['out', 'retval'], POINTER(BSTR), 'pbstrLines')
    ),
    COMMETHOD(
        [dispid(12), helpstring('Synchronous reception of a file from the server')],
        HRESULT,
        'ReceiveFile',
        (['in'], BSTR, 'bstrSourceFileName'),
        (['in'], BSTR, 'bstrDestFileName')
    ),
    COMMETHOD(
        [dispid(13), helpstring('Start a background reception of a file from the server.')],
        HRESULT,
        'StartReceiveFile',
        (['in'], BSTR, 'bstrSourceFileName'),
        (['in'], BSTR, 'bstrDestFileName'),
        (['in'], VARIANT_BOOL, 'bReportProgress'),
        (['out', 'retval'], POINTER(c_int), 'plTransferJobID')
    ),
    COMMETHOD(
        [dispid(14), helpstring('Synchronous transmission of a file to the server')],
        HRESULT,
        'TransmitFile',
        (['in'], BSTR, 'bstrSourceFileName'),
        (['in'], BSTR, 'bstrDestFileName')
    ),
    COMMETHOD(
        [dispid(15), helpstring('Start a background transmission of a file to the server.')],
        HRESULT,
        'StartTransmitFile',
        (['in'], BSTR, 'bstrSourceFileName'),
        (['in'], BSTR, 'bstrDestFileName'),
        (['in'], VARIANT_BOOL, 'bReportProgress'),
        (['out', 'retval'], POINTER(c_int), 'plTransferJobID')
    ),
    COMMETHOD(
        [dispid(16), helpstring('Abort a background file transfer.')],
        HRESULT,
        'AbortFileTransfer',
        (['in'], c_int, 'lTransferJobId')
    ),
    COMMETHOD(
        [dispid(17), helpstring('Set or reset the attribute(s) of a file')],
        HRESULT,
        'SetAttributes',
        (['in'], BSTR, 'bstrName'),
        (['in'], POINTER(IJHFileAttributes), 'pAttributes')
    ),
    COMMETHOD(
        [dispid(18), helpstring('Get the attributes of one or more files.')],
        HRESULT,
        'GetAttributes',
        (['in'], BSTR, 'bstrName'),
        (['out', 'retval'], POINTER(POINTER(IJHFileAttributes)), 'ppAttributes')
    ),
    COMMETHOD(
        [dispid(19), helpstring('Set the time and date of the specified file(s).')],
        HRESULT,
        'SetFileTime',
        (['in'], BSTR, 'bstrFileName'),
        (['in'], c_double, 'dateTime')
    ),
    COMMETHOD(
        [dispid(20), helpstring('Get the time and date of the specified file.')],
        HRESULT,
        'GetFileTime',
        (['in'], BSTR, 'bstrFileName'),
        (['out', 'retval'], POINTER(c_double), 'pDateTime')
    ),
    COMMETHOD(
        [dispid(21), helpstring('SetAccessMode.')],
        HRESULT,
        'SetAccessMode',
        (['in'], DNC_ACCESS_MODE, 'accessMode'),
        (['in'], BSTR, 'bstrPassword')
    ),
    COMMETHOD(
        [dispid(22), helpstring('Add or remove the specified file to the file change observe list ')],
        HRESULT,
        'ObserveFileChange',
        (['in'], BSTR, 'bstrFileName'),
        (['in'], DNC_FILE_OBSERVE, 'command')
    ),
]

################################################################
# code template for IJHFileSystem implementation
# class IJHFileSystem_Impl(object):
#     def GetDiskSpace(self, bstrPath):
#         'Retrieve the total and free space available on the server.'
#         #return pdFreeSpace, pdTotalSize
#
#     def GetCurrentDirectory(self):
#         'Retrieve the current directory on the server.'
#         #return pbstrCurDir
#
#     def GetFileSystemAttributes(self):
#         'Retrieve file system information. Use this method once to retrieve the attribute definition.'
#         #return ppFileAttributes
#
#     def ReadDirectory(self, bstrFileName, pAttributeSelection, pAttributeState):
#         'Read directory contents, optionally with filter.'
#         #return ppDirEntryList
#
#     def ChangeDirectory(self, bstrNewDir):
#         'Change the current directory on the server.'
#         #return 
#
#     def MakeDirectory(self, bstrNewDir):
#         'Make a new directory on the server.'
#         #return 
#
#     def DeleteDirectory(self, bstrDir):
#         'Delete an empty directory on the server.'
#         #return 
#
#     def DeleteFile(self, bstrFileName):
#         'Delete a file on the server.'
#         #return 
#
#     def Rename(self, bstrOldFileName, bstrNewFileName):
#         'Rename a file or directory on the server.'
#         #return 
#
#     def CopyFile(self, bstrSourceFileName, bstrDestFileName):
#         'Copy a file on the server to a new file on the server (local copy!).'
#         #return 
#
#     def PreviewFile(self, bstrFileName, lNrLines):
#         'Retrieve the first lines of a file'
#         #return pbstrLines
#
#     def ReceiveFile(self, bstrSourceFileName, bstrDestFileName):
#         'Synchronous reception of a file from the server'
#         #return 
#
#     def StartReceiveFile(self, bstrSourceFileName, bstrDestFileName, bReportProgress):
#         'Start a background reception of a file from the server.'
#         #return plTransferJobID
#
#     def TransmitFile(self, bstrSourceFileName, bstrDestFileName):
#         'Synchronous transmission of a file to the server'
#         #return 
#
#     def StartTransmitFile(self, bstrSourceFileName, bstrDestFileName, bReportProgress):
#         'Start a background transmission of a file to the server.'
#         #return plTransferJobID
#
#     def AbortFileTransfer(self, lTransferJobId):
#         'Abort a background file transfer.'
#         #return 
#
#     def SetAttributes(self, bstrName, pAttributes):
#         'Set or reset the attribute(s) of a file'
#         #return 
#
#     def GetAttributes(self, bstrName):
#         'Get the attributes of one or more files.'
#         #return ppAttributes
#
#     def SetFileTime(self, bstrFileName, dateTime):
#         'Set the time and date of the specified file(s).'
#         #return 
#
#     def GetFileTime(self, bstrFileName):
#         'Get the time and date of the specified file.'
#         #return pDateTime
#
#     def SetAccessMode(self, accessMode, bstrPassword):
#         'SetAccessMode.'
#         #return 
#
#     def ObserveFileChange(self, bstrFileName, command):
#         'Add or remove the specified file to the file change observe list '
#         #return 
#

IJHTriggerList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHTrigger object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHTrigger)), 'ppTrigger')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Add a new Trigger item to the list.')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHTrigger), 'pTrigger')
    ),
]

################################################################
# code template for IJHTriggerList implementation
# class IJHTriggerList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHTrigger object on the specified index in the list'
#         #return ppTrigger
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#
#     def AddItem(self, pTrigger):
#         'Add a new Trigger item to the list.'
#         #return 
#


class JHMachineEvents2(CoClass):
    """JHMachineEvents2 Class"""
    _reg_clsid_ = GUID('{A3A71930-EAD9-430B-9004-49D2F033CE78}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHMachineEvents2._outgoing_interfaces_ = [_DJHMachineEvents2, _IJHMachineEvents2]


class JHProcessData(CoClass):
    """JHProcessData Class"""
    _reg_clsid_ = GUID('{CC1D4B8B-2FAE-4CDC-86AD-1BECC516887D}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHProcessData._com_interfaces_ = [IJHProcessData]


class JHTraceVariableList(CoClass):
    """JHTraceVariableList Class"""
    _reg_clsid_ = GUID('{F0A5DBD6-1C88-417E-9B28-30756A2BFCDA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceVariableList._com_interfaces_ = [IJHTraceVariableList, IJHLoggingInternal]

IJHProgramPositionList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHProgramPosition object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHProgramPosition)),
            'ppProgramPosition',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHProgramPositionList implementation
# class IJHProgramPositionList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHProgramPosition object on the specified index in the list'
#         #return ppProgramPosition
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#

IJHToolId._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property lToolId'), 'propget'],
        HRESULT,
        'lToolId',
        (['out', 'retval'], POINTER(c_int), 'plToolId')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property lToolId'), 'propput'],
        HRESULT,
        'lToolId',
        (['in'], c_int, 'plToolId')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property lSpareToolId'), 'propget'],
        HRESULT,
        'lSpareToolId',
        (['out', 'retval'], POINTER(c_int), 'plSpareToolId')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property lSpareToolId'), 'propput'],
        HRESULT,
        'lSpareToolId',
        (['in'], c_int, 'plSpareToolId')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property lIndex'), 'propget'],
        HRESULT,
        'lIndex',
        (['out', 'retval'], POINTER(c_int), 'plIndex')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property lIndex'), 'propput'],
        HRESULT,
        'lIndex',
        (['in'], c_int, 'plIndex')
    ),
]

################################################################
# code template for IJHToolId implementation
# class IJHToolId_Impl(object):
#     def _get(self):
#         'property lToolId'
#         #return plToolId
#     def _set(self, plToolId):
#         'property lToolId'
#     lToolId = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property lSpareToolId'
#         #return plSpareToolId
#     def _set(self, plSpareToolId):
#         'property lSpareToolId'
#     lSpareToolId = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property lIndex'
#         #return plIndex
#     def _set(self, plIndex):
#         'property lIndex'
#     lIndex = property(_get, _set, doc = _set.__doc__)
#


class JHErrorEntry(CoClass):
    """JHErrorEntry Class"""
    _reg_clsid_ = GUID('{037ED973-BC89-4E5C-828B-CF7F67981EFB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHErrorEntry._com_interfaces_ = [IJHErrorEntry2, IJHLoggingInternal]

IJHProgramPosition._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property programName'), 'propget'],
        HRESULT,
        'programName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrProgamName')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property blockNumber'), 'propget'],
        HRESULT,
        'blockNumber',
        (['out', 'retval'], POINTER(c_int), 'plBlockNumber')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property blockContent'), 'propget'],
        HRESULT,
        'blockContent',
        (['out', 'retval'], POINTER(BSTR), 'pbstrBlockContent')
    ),
]

################################################################
# code template for IJHProgramPosition implementation
# class IJHProgramPosition_Impl(object):
#     @property
#     def programName(self):
#         'property programName'
#         #return pbstrProgamName
#
#     @property
#     def blockNumber(self):
#         'property blockNumber'
#         #return plBlockNumber
#
#     @property
#     def blockContent(self):
#         'property blockContent'
#         #return pbstrBlockContent
#


class JHMachineInProcess(CoClass):
    """JHMachineInProcess Class"""
    _reg_clsid_ = GUID('{BEB4B3C8-CCD6-4F37-97E6-21DD51BD2F23}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHMachine4(IJHMachine3):
    """IJHMachine4 Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{D3D5247D-59F7-48FD-BC23-F943DED02B22}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def ConnectRequest4(self, pIConnection: hints.Incomplete, varbstrClientName: hints.Incomplete = ..., varbstrClientGUID: hints.Incomplete = ...) -> hints.Hresult: ...


JHMachineInProcess._com_interfaces_ = [IJHMachine4, IJHConnection3, IJHSecureConnectionHelper3]
JHMachineInProcess._outgoing_interfaces_ = [_DJHMachineEvents2, _IJHMachineEvents2]

IJHCutterLocationList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHCutterLocation object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHCutterLocation)),
            'ppCutterLocation',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHCutterLocationList implementation
# class IJHCutterLocationList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHCutterLocation object on the specified index in the list'
#         #return ppCutterLocation
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#

IJHFileAttributes._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Gets the name of the specified attribute')],
        HRESULT,
        'GetAttributeName',
        (['in'], DNC_ATTRIBUTE_TYPE, 'attribute'),
        (['out', 'retval'], POINTER(BSTR), 'pbstrName')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Checks whether a specified Attribute is set')],
        HRESULT,
        'IsAttributeSet',
        (['in'], DNC_ATTRIBUTE_TYPE, 'attribute'),
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbIsSet')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Sets the specified Attribute')],
        HRESULT,
        'SetAttribute',
        (['in'], DNC_ATTRIBUTE_TYPE, 'attribute')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Clears the specified Attribute')],
        HRESULT,
        'ClearAttribute',
        (['in'], DNC_ATTRIBUTE_TYPE, 'attribute')
    ),
]

################################################################
# code template for IJHFileAttributes implementation
# class IJHFileAttributes_Impl(object):
#     def GetAttributeName(self, attribute):
#         'Gets the name of the specified attribute'
#         #return pbstrName
#
#     def IsAttributeSet(self, attribute):
#         'Checks whether a specified Attribute is set'
#         #return pbIsSet
#
#     def SetAttribute(self, attribute):
#         'Sets the specified Attribute'
#         #return 
#
#     def ClearAttribute(self, attribute):
#         'Clears the specified Attribute'
#         #return 
#

IJHTraceVariableList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('Property to retrieve a TraceVariable object (zero-based)'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceVariable)),
            'ppTraceVariable',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of elements (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'plNrOfVariables')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method GetVariableById')],
        HRESULT,
        'GetVariableById',
        (['in'], DNC_TRACE_VARIABLE_ID, 'traceVariableId'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceVariable)),
            'ppTraceVariable',
        )
    ),
    COMMETHOD(
        [dispid(3), helpstring('method GetVariableByName')],
        HRESULT,
        'GetVariableByName',
        (['in'], BSTR, 'bstrTraceVariableName'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceVariable)),
            'ppTraceVariable',
        )
    ),
]

################################################################
# code template for IJHTraceVariableList implementation
# class IJHTraceVariableList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'Property to retrieve a TraceVariable object (zero-based)'
#         #return ppTraceVariable
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of elements (0 to count -1)'
#         #return plNrOfVariables
#
#     def GetVariableById(self, traceVariableId):
#         'method GetVariableById'
#         #return ppTraceVariable
#
#     def GetVariableByName(self, bstrTraceVariableName):
#         'method GetVariableByName'
#         #return ppTraceVariable
#


class JHCutterLocation2Enum(CoClass):
    """JHCutterLocation2Enum Class"""
    _reg_clsid_ = GUID('{BC1721EF-F824-4C60-9FB4-2DE3E386E399}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHCutterLocation2Enum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

IJHCutterLocation._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property bIsInch'), 'propget'],
        HRESULT,
        'bIsInch',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbIsInch')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property dPosition'), 'propget'],
        HRESULT,
        'dPosition',
        (['out', 'retval'], POINTER(c_double), 'pdPosition')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property bstrCoordinateName'), 'propget'],
        HRESULT,
        'bstrCoordinateName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrCoordinateName')
    ),
]

################################################################
# code template for IJHCutterLocation implementation
# class IJHCutterLocation_Impl(object):
#     @property
#     def bIsInch(self):
#         'property bIsInch'
#         #return pbIsInch
#
#     @property
#     def dPosition(self):
#         'property dPosition'
#         #return pdPosition
#
#     @property
#     def bstrCoordinateName(self):
#         'property bstrCoordinateName'
#         #return pbstrCoordinateName
#

IJHTraceSampleListList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('Property to retrieve a JHTraceSampleList object (zero-based)'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceSampleList)),
            'ppTraceSampleList',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of elements (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'plNrOfSampleLists')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method GetSampleListByTraceChannelId')],
        HRESULT,
        'GetSampleListByTraceChannelId',
        (['in'], c_int, 'traceChannelId'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHTraceSampleList)),
            'ppTraceSampleList',
        )
    ),
]

################################################################
# code template for IJHTraceSampleListList implementation
# class IJHTraceSampleListList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'Property to retrieve a JHTraceSampleList object (zero-based)'
#         #return ppTraceSampleList
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of elements (0 to count -1)'
#         #return plNrOfSampleLists
#
#     def GetSampleListByTraceChannelId(self, traceChannelId):
#         'method GetSampleListByTraceChannelId'
#         #return ppTraceSampleList
#


class JHDataEntry2List(CoClass):
    """JHDataEntry2List Class"""
    _reg_clsid_ = GUID('{853B283E-DC5D-40AB-9B91-0F278F3722CA}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntry2List._com_interfaces_ = [IJHDataEntry2List, IJHLoggingInternal]

IJHBreakCondition._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method BreakOnOptionalStop')],
        HRESULT,
        'BreakOnOptionalStop',
        (['in'], VARIANT_BOOL, 'bBreakOnOptionalStop')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method BreakOnProgrammedStop')],
        HRESULT,
        'BreakOnProgrammedStop',
        (['in'], VARIANT_BOOL, 'bBreakOnProgrammedStop')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method BreakOnLineInFile')],
        HRESULT,
        'BreakOnLineInFile',
        (['in'], c_int, 'lLineNr'),
        (['in'], c_int, 'lSkipCount'),
        (['in', 'optional'], VARIANT, 'bstrProgramFilename')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property pbBreakOnOptionalStop'), 'propget'],
        HRESULT,
        'bBreakOnOptionalStop',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbBreakOnOptionalStop')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property bBreakOnProgrammedStop'), 'propget'],
        HRESULT,
        'bBreakOnProgrammedStop',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbBreakOnProgrammedStop')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property kind'), 'propget'],
        HRESULT,
        'kind',
        (['out', 'retval'], POINTER(DNC_PROGRAMBREAKCONDITION_KIND), 'pKind')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property bstrProgramFilename'), 'propget'],
        HRESULT,
        'bstrProgramFilename',
        (['out', 'retval'], POINTER(BSTR), 'pbstrProgramFilename')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property lLineNr'), 'propget'],
        HRESULT,
        'lLineNr',
        (['out', 'retval'], POINTER(c_int), 'plLineNr')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property lSkipCount'), 'propget'],
        HRESULT,
        'lSkipCount',
        (['out', 'retval'], POINTER(c_int), 'plSkipCount')
    ),
]

################################################################
# code template for IJHBreakCondition implementation
# class IJHBreakCondition_Impl(object):
#     def BreakOnOptionalStop(self, bBreakOnOptionalStop):
#         'method BreakOnOptionalStop'
#         #return 
#
#     def BreakOnProgrammedStop(self, bBreakOnProgrammedStop):
#         'method BreakOnProgrammedStop'
#         #return 
#
#     def BreakOnLineInFile(self, lLineNr, lSkipCount, bstrProgramFilename):
#         'method BreakOnLineInFile'
#         #return 
#
#     @property
#     def bBreakOnOptionalStop(self):
#         'property pbBreakOnOptionalStop'
#         #return pbBreakOnOptionalStop
#
#     @property
#     def bBreakOnProgrammedStop(self):
#         'property bBreakOnProgrammedStop'
#         #return pbBreakOnProgrammedStop
#
#     @property
#     def kind(self):
#         'property kind'
#         #return pKind
#
#     @property
#     def bstrProgramFilename(self):
#         'property bstrProgramFilename'
#         #return pbstrProgramFilename
#
#     @property
#     def lLineNr(self):
#         'property lLineNr'
#         #return plLineNr
#
#     @property
#     def lSkipCount(self):
#         'property lSkipCount'
#         #return plSkipCount
#


class IJHTraceSample(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceSample Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{4EA9A978-C41F-4416-9C6C-B40594A242A8}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_timeStamp(self) -> hints.Incomplete: ...
        timeStamp = hints.normal_property(_get_timeStamp)
        def _get_value(self) -> hints.Incomplete: ...
        value = hints.normal_property(_get_value)


IJHTraceSampleList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('Property to retrieve a TraceSample object (zero-based)'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHTraceSample)), 'ppTraceSample')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of elements (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'plNrOfSamples')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property lTraceChannelId'), 'propget'],
        HRESULT,
        'lTraceChannelId',
        (['out', 'retval'], POINTER(c_int), 'plTraceChannelId')
    ),
]

################################################################
# code template for IJHTraceSampleList implementation
# class IJHTraceSampleList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'Property to retrieve a TraceSample object (zero-based)'
#         #return ppTraceSample
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of elements (0 to count -1)'
#         #return plNrOfSamples
#
#     @property
#     def lTraceChannelId(self):
#         'property lTraceChannelId'
#         #return plTraceChannelId
#

IJHDirectoryEntryList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHDirectoryEntry object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHDirectoryEntry)),
            'ppDirectoryEntry',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHDirectoryEntryList implementation
# class IJHDirectoryEntryList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHDirectoryEntry object on the specified index in the list'
#         #return ppDirectoryEntry
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#

IJHAxisPositionList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHAxisPosition object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHAxisPosition)), 'ppAxisPosition')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Add a new AxisPosition item to the list.')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHAxisPosition), 'pAxisPosition')
    ),
]

################################################################
# code template for IJHAxisPositionList implementation
# class IJHAxisPositionList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHAxisPosition object on the specified index in the list'
#         #return ppAxisPosition
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#
#     def AddItem(self, pAxisPosition):
#         'Add a new AxisPosition item to the list.'
#         #return 
#

IJHDirectoryEntry._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property name'), 'propget'],
        HRESULT,
        'name',
        (['out', 'retval'], POINTER(BSTR), 'pbstrName')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property size'), 'propget'],
        HRESULT,
        'size',
        (['out', 'retval'], POINTER(c_double), 'plSize')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property attributes'), 'propget'],
        HRESULT,
        'attributes',
        (['out', 'retval'], POINTER(POINTER(IJHFileAttributes)), 'ppAttributes')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property dateTime'), 'propget'],
        HRESULT,
        'dateTime',
        (['out', 'retval'], POINTER(c_double), 'pDateTime')
    ),
]

################################################################
# code template for IJHDirectoryEntry implementation
# class IJHDirectoryEntry_Impl(object):
#     @property
#     def name(self):
#         'property name'
#         #return pbstrName
#
#     @property
#     def size(self):
#         'property size'
#         #return plSize
#
#     @property
#     def attributes(self):
#         'property attributes'
#         #return ppAttributes
#
#     @property
#     def dateTime(self):
#         'property dateTime'
#         #return pDateTime
#

IJHConnectionProperty._methods_ = [
    COMMETHOD(
        [dispid(2), helpstring('property value'), 'propget'],
        HRESULT,
        'value',
        (['out', 'retval'], POINTER(VARIANT), 'pValue')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property value'), 'propput'],
        HRESULT,
        'value',
        (['in'], VARIANT, 'pValue')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property kind'), 'propget'],
        HRESULT,
        'kind',
        (
            ['out', 'retval'],
            POINTER(DNC_CONNECTION_PROPERTY),
            'pConnectionProperty',
        )
    ),
]

################################################################
# code template for IJHConnectionProperty implementation
# class IJHConnectionProperty_Impl(object):
#     def _get(self):
#         'property value'
#         #return pValue
#     def _set(self, pValue):
#         'property value'
#     value = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def kind(self):
#         'property kind'
#         #return pConnectionProperty
#

IJHTraceSample._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property TimeStamp'), 'propget'],
        HRESULT,
        'timeStamp',
        (['out', 'retval'], POINTER(c_double), 'pTimeStamp')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property Value'), 'propget'],
        HRESULT,
        'value',
        (['out', 'retval'], POINTER(VARIANT), 'pvarValue')
    ),
]

################################################################
# code template for IJHTraceSample implementation
# class IJHTraceSample_Impl(object):
#     @property
#     def timeStamp(self):
#         'property TimeStamp'
#         #return pTimeStamp
#
#     @property
#     def value(self):
#         'property Value'
#         #return pvarValue
#


class JHAxisInfoList(CoClass):
    """JHAxisInfoList Class"""
    _reg_clsid_ = GUID('{875356CA-D5F6-410F-A1E0-288FCDDCBA5F}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHAxisInfoList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAxisInfoList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{B80B9FE0-28A5-41E5-84FC-0F07973FE71D}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHAxisInfo': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


JHAxisInfoList._com_interfaces_ = [IJHAxisInfoList, IJHLoggingInternal]

IJHBreakConditionList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHBreakCondition object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHBreakCondition)),
            'ppBreakCondition',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pNrOfElements')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method AddItem')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHBreakCondition), 'pBreakCondition')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method RemoveItem')],
        HRESULT,
        'RemoveItem',
        (['in'], c_int, 'lIndex')
    ),
]

################################################################
# code template for IJHBreakConditionList implementation
# class IJHBreakConditionList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHBreakCondition object on the specified index in the list'
#         #return ppBreakCondition
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pNrOfElements
#
#     def AddItem(self, pBreakCondition):
#         'method AddItem'
#         #return 
#
#     def RemoveItem(self, lIndex):
#         'method RemoveItem'
#         #return 
#


class JHTraceVariableEnum(CoClass):
    """JHTraceVariableEnum Class"""
    _reg_clsid_ = GUID('{1BD12CDE-2CCD-4A53-B948-2AAA62C04113}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceVariableEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHErrorEntryEnum(CoClass):
    """JHErrorEntryEnum Class"""
    _reg_clsid_ = GUID('{B353246E-9334-4A97-A512-61F7A678ADCC}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHErrorEntryEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

IJHAxisPosition._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property dPosition'), 'propget'],
        HRESULT,
        'dPosition',
        (['out', 'retval'], POINTER(c_double), 'pdPosition')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property dPosition'), 'propput'],
        HRESULT,
        'dPosition',
        (['in'], c_double, 'pdPosition')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property lAxisId'), 'propget'],
        HRESULT,
        'lAxisId',
        (['out', 'retval'], POINTER(c_int), 'plAxisId')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property lAxisId'), 'propput'],
        HRESULT,
        'lAxisId',
        (['in'], c_int, 'plAxisId')
    ),
]

################################################################
# code template for IJHAxisPosition implementation
# class IJHAxisPosition_Impl(object):
#     def _get(self):
#         'property dPosition'
#         #return pdPosition
#     def _set(self, pdPosition):
#         'property dPosition'
#     dPosition = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property lAxisId'
#         #return plAxisId
#     def _set(self, plAxisId):
#         'property lAxisId'
#     lAxisId = property(_get, _set, doc = _set.__doc__)
#


class JHDiagnostics(CoClass):
    _reg_clsid_ = GUID('{B6223804-6295-499C-BB03-F5341D4A90BE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHDiagnostics(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHDiagnostics Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{A01733C5-C1EA-4929-B5DF-A6F751F88E61}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SetAccessMode(self, accessMode: hints.Incomplete, bstrPassword: hints.Incomplete) -> hints.Hresult: ...
        def StartCreateServiceFile(self, bstrFileName: hints.Incomplete) -> hints.Hresult: ...
        def GetAvailableKeys(self, ppsaVirtualKeys: hints.Incomplete, ppsaFunctionalKeys: hints.Incomplete, ppsaQualifiers: hints.Incomplete, ppsaActions: hints.Incomplete, ppsaButtons: hints.Incomplete) -> hints.Tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def SendKey(self, bstrWmKey: hints.Incomplete, bstrQualifiers: hints.Incomplete, keyAction: hints.Incomplete) -> hints.Hresult: ...
        def SendString(self, bstrString: hints.Incomplete) -> hints.Hresult: ...
        def MakeScreenShot(self, bstrFileName: hints.Incomplete, xOrigin: hints.Incomplete = ..., yOrigin: hints.Incomplete = ..., width: hints.Incomplete = ..., height: hints.Incomplete = ...) -> hints.Hresult: ...


JHDiagnostics._com_interfaces_ = [IJHDiagnostics]
JHDiagnostics._outgoing_interfaces_ = [_DJHDiagnosticsEvents, _IJHDiagnosticsEvents]

_DJHErrorEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Signals the occurrence of an error')],
        HRESULT,
        'OnError',
        (['in'], DNC_ERROR_GROUP, 'errorGroup'),
        (['in'], c_int, 'lErrorNumber'),
        (['in'], DNC_ERROR_CLASS, 'errorClass'),
        (['in'], BSTR, 'bstrError'),
        (['in'], c_int, 'lChannel')
    ),
    DISPMETHOD(
        [dispid(2), helpstring('Signals the clearence of an error')],
        HRESULT,
        'OnErrorCleared',
        (['in'], c_int, 'lErrorNumber'),
        (['in'], c_int, 'lChannel')
    ),
    DISPMETHOD(
        [dispid(3), helpstring('Signals the occurrence of an error')],
        HRESULT,
        'OnError2',
        (['in'], POINTER(IJHErrorEntry2), 'pErrorEntry')
    ),
    DISPMETHOD(
        [dispid(4), helpstring('Signals the clearence of an error')],
        HRESULT,
        'OnErrorCleared2',
        (['in'], POINTER(IJHErrorEntry2), 'pErrorEntry')
    ),
]


class IJHTraceInternal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHTraceInternal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{8BE60E3F-10BC-4673-8BA8-2431BAF32FB3}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SwitchChannelState(self, traceChannelId: hints.Incomplete, bActive: hints.Incomplete) -> hints.Hresult: ...
        def SelectVariable(self, traceChannelId: hints.Incomplete, pTraceVariable: hints.Incomplete) -> hints.Hresult: ...


IJHTraceInternal._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method SwitchChannelState')],
        HRESULT,
        'SwitchChannelState',
        (['in'], c_int, 'traceChannelId'),
        (['in'], VARIANT_BOOL, 'bActive')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method SelectVariable')],
        HRESULT,
        'SelectVariable',
        (['in'], c_int, 'traceChannelId'),
        (['in'], POINTER(IJHTraceVariable), 'pTraceVariable')
    ),
]

################################################################
# code template for IJHTraceInternal implementation
# class IJHTraceInternal_Impl(object):
#     def SwitchChannelState(self, traceChannelId, bActive):
#         'method SwitchChannelState'
#         #return 
#
#     def SelectVariable(self, traceChannelId, pTraceVariable):
#         'method SelectVariable'
#         #return 
#


class JHTest(CoClass):
    """JHTest Class"""
    _reg_clsid_ = GUID('{7857AFE9-1A4A-47AF-9E18-0E423F3C4E00}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTest._com_interfaces_ = [IJHTest]
JHTest._outgoing_interfaces_ = [_DJHTestEvents, _IJHTestEvents]


class JHDataEntry(CoClass):
    """JHDataEntry Class"""
    _reg_clsid_ = GUID('{63B3FA0A-238D-4275-8295-60C0014508A1}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntry._com_interfaces_ = [IJHDataEntry2, IJHLoggingInternal]


class JHCutterPosition(CoClass):
    """JHCutterPosition Class"""
    _reg_clsid_ = GUID('{FD9ABBAA-66C0-4D70-A4C8-90A047C4D522}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHCutterPosition._com_interfaces_ = [IJHCutterPosition]

IJHCutterPosition._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property pCutterLocationList'), 'propget'],
        HRESULT,
        'pCutterLocationList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHCutterLocation2List)),
            'ppCutterLocationList',
        )
    ),
    COMMETHOD(
        [dispid(1), helpstring('property pCutterLocationList'), 'propput'],
        HRESULT,
        'pCutterLocationList',
        (['in'], POINTER(IJHCutterLocation2List), 'ppCutterLocationList')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property pCutterOrientation1'), 'propget'],
        HRESULT,
        'pCutterOrientation1',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionList)),
            'ppCutterOrientation1',
        )
    ),
    COMMETHOD(
        [dispid(2), helpstring('property pCutterOrientation1'), 'propput'],
        HRESULT,
        'pCutterOrientation1',
        (['in'], POINTER(IJHAxisPositionList), 'ppCutterOrientation1')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property pCutterOrientation2'), 'propget'],
        HRESULT,
        'pCutterOrientation2',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionList)),
            'ppCutterOrientation2',
        )
    ),
    COMMETHOD(
        [dispid(3), helpstring('property pCutterOrientation2'), 'propput'],
        HRESULT,
        'pCutterOrientation2',
        (['in'], POINTER(IJHAxisPositionList), 'ppCutterOrientation2')
    ),
]

################################################################
# code template for IJHCutterPosition implementation
# class IJHCutterPosition_Impl(object):
#     def _get(self):
#         'property pCutterLocationList'
#         #return ppCutterLocationList
#     def _set(self, ppCutterLocationList):
#         'property pCutterLocationList'
#     pCutterLocationList = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property pCutterOrientation1'
#         #return ppCutterOrientation1
#     def _set(self, ppCutterOrientation1):
#         'property pCutterOrientation1'
#     pCutterOrientation1 = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property pCutterOrientation2'
#         #return ppCutterOrientation2
#     def _set(self, ppCutterOrientation2):
#         'property pCutterOrientation2'
#     pCutterOrientation2 = property(_get, _set, doc = _set.__doc__)
#

_IJHFileSystemEvents._methods_ = [
    COMMETHOD(
        [helpstring('method OnFileTransferEnd')],
        HRESULT,
        'OnFileTransferEnd',
        (['in'], c_int, 'lTransferJobId'),
        (['in'], c_int, 'hErrorCode')
    ),
    COMMETHOD(
        [helpstring('method OnFileTransferProgress')],
        HRESULT,
        'OnFileTransferProgress',
        (['in'], c_int, 'lTransferJobId'),
        (['in'], c_int, 'lBytesCopied'),
        (['in'], c_int, 'lBytesTotal')
    ),
    COMMETHOD(
        [helpstring('method OnFileChanged')],
        HRESULT,
        'OnFileChanged',
        (['in'], BSTR, 'bstrFileName')
    ),
]

################################################################
# code template for _IJHFileSystemEvents implementation
# class _IJHFileSystemEvents_Impl(object):
#     def OnFileTransferEnd(self, lTransferJobId, hErrorCode):
#         'method OnFileTransferEnd'
#         #return 
#
#     def OnFileTransferProgress(self, lTransferJobId, lBytesCopied, lBytesTotal):
#         'method OnFileTransferProgress'
#         #return 
#
#     def OnFileChanged(self, bstrFileName):
#         'method OnFileChanged'
#         #return 
#


class JHErrorEntry2Enum(CoClass):
    """JHErrorEntry2Enum Class"""
    _reg_clsid_ = GUID('{FF7F5EC2-8664-49B9-9114-D618281D1FC9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHErrorEntry2Enum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

_IJHTraceEvents._methods_ = [
    COMMETHOD(
        [helpstring('New trace data is available')],
        HRESULT,
        'OnTraceDataAvailable',
    ),
    COMMETHOD(
        [helpstring('Active tracing has been aborted by the server')],
        HRESULT,
        'OnTracingAborted',
    ),
]

################################################################
# code template for _IJHTraceEvents implementation
# class _IJHTraceEvents_Impl(object):
#     def OnTraceDataAvailable(self):
#         'New trace data is available'
#         #return 
#
#     def OnTracingAborted(self):
#         'Active tracing has been aborted by the server'
#         #return 
#


class JHTraceChannel(CoClass):
    """JHTraceChannel Class"""
    _reg_clsid_ = GUID('{2B4BCAF3-BBF4-45D8-AE05-E131974616E5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceChannel._com_interfaces_ = [IJHTraceChannel, IJHLoggingInternal]

IJHCutterLocation2List._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHCutterLocation object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHCutterLocation2)),
            'ppCutterLocation',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Add a new CutterLocation item to the list.')],
        HRESULT,
        'AddItem',
        (['in'], POINTER(IJHCutterLocation2), 'pCutterLocation')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Remove the CutterLocation at given index from the list.')],
        HRESULT,
        'RemoveItem',
        (['in'], c_int, 'index')
    ),
]

################################################################
# code template for IJHCutterLocation2List implementation
# class IJHCutterLocation2List_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHCutterLocation object on the specified index in the list'
#         #return ppCutterLocation
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#
#     def AddItem(self, pCutterLocation):
#         'Add a new CutterLocation item to the list.'
#         #return 
#
#     def RemoveItem(self, index):
#         'Remove the CutterLocation at given index from the list.'
#         #return 
#

ITNCTable._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method DeleteRecord')],
        HRESULT,
        'DeleteRecord',
        (['in'], BSTR, 'bstrTableName'),
        (['in'], BSTR, 'bstrSQLQuery')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method GetTableInfo')],
        HRESULT,
        'GetTableInfo',
        (['in'], BSTR, 'bstrTableName'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'bstrColumnTitles'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(c_int)), 'lColumnPos')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method ReceiveTableLines')],
        HRESULT,
        'ReceiveTableLines',
        (['in'], BSTR, 'bstrTableName'),
        (['in'], BSTR, 'bstrSQLQuery'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'pbstrLines')
    ),
    COMMETHOD(
        [dispid(4), helpstring('method TransmitTablePart')],
        HRESULT,
        'TransmitTablePart',
        (['in'], BSTR, 'bstrSourceFileName'),
        (['in'], BSTR, 'bstrDestTableName')
    ),
]

################################################################
# code template for ITNCTable implementation
# class ITNCTable_Impl(object):
#     def DeleteRecord(self, bstrTableName, bstrSQLQuery):
#         'method DeleteRecord'
#         #return 
#
#     def GetTableInfo(self, bstrTableName):
#         'method GetTableInfo'
#         #return bstrColumnTitles, lColumnPos
#
#     def ReceiveTableLines(self, bstrTableName, bstrSQLQuery):
#         'method ReceiveTableLines'
#         #return pbstrLines
#
#     def TransmitTablePart(self, bstrSourceFileName, bstrDestTableName):
#         'method TransmitTablePart'
#         #return 
#


class JHTrace(CoClass):
    """JHTrace Class"""
    _reg_clsid_ = GUID('{E6290E90-847D-4068-956F-3F4C8BF3B69B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTrace._com_interfaces_ = [IJHTrace, IJHTraceInternal]
JHTrace._outgoing_interfaces_ = [_DJHTraceEvents, _IJHTraceEvents]


class JHAxisInfo(CoClass):
    """JHAxisInfo Class"""
    _reg_clsid_ = GUID('{127FF4EE-0000-497C-B304-D76521359430}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHAxisInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHAxisInfo Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{7C28E6E8-BE27-4D02-B9A2-1314B08E7EA1}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_lAxisId(self) -> hints.Incomplete: ...
        lAxisId = hints.normal_property(_get_lAxisId)
        def _get_axisType(self) -> hints.Incomplete: ...
        axisType = hints.normal_property(_get_axisType)
        def _get_bstrAxisName(self) -> hints.Incomplete: ...
        bstrAxisName = hints.normal_property(_get_bstrAxisName)


JHAxisInfo._com_interfaces_ = [IJHAxisInfo, IJHLoggingInternal]

IJHCutterLocation2._methods_ = [
    COMMETHOD(
        [dispid(4), helpstring('property bIsInch'), 'propput'],
        HRESULT,
        'bIsInch',
        (['in'], VARIANT_BOOL, 'rhs')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property dPosition'), 'propput'],
        HRESULT,
        'dPosition',
        (['in'], c_double, 'rhs')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property bstrCoordinateName'), 'propput'],
        HRESULT,
        'bstrCoordinateName',
        (['in'], BSTR, 'rhs')
    ),
]

################################################################
# code template for IJHCutterLocation2 implementation
# class IJHCutterLocation2_Impl(object):
#     def _set(self, rhs):
#         'property bIsInch'
#     bIsInch = property(fset = _set, doc = _set.__doc__)
#
#     def _set(self, rhs):
#         'property dPosition'
#     dPosition = property(fset = _set, doc = _set.__doc__)
#
#     def _set(self, rhs):
#         'property bstrCoordinateName'
#     bstrCoordinateName = property(fset = _set, doc = _set.__doc__)
#


class JHDataEntryEnum(CoClass):
    """JHDataEntryEnum Class"""
    _reg_clsid_ = GUID('{C60A549C-AB4E-41B9-9688-E1EB31F810FD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

IJHAxisPositionListList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHAxisPositionList object on the specified index of the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionList)),
            'ppAxisPositionList',
        )
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHAxisPositionListList implementation
# class IJHAxisPositionListList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHAxisPositionList object on the specified index of the list'
#         #return ppAxisPositionList
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#


class JHPositioningResult(CoClass):
    """JHPositioningResult Class"""
    _reg_clsid_ = GUID('{93544229-39EC-4083-BA84-C02CE8F1B3B0}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHPositioningResult(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHPositioningResult Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{07D18E9C-674D-4870-BB12-3253D49ED955}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_bEndSwitchTripped(self) -> hints.Incomplete: ...
        bEndSwitchTripped = hints.normal_property(_get_bEndSwitchTripped)
        def _get_bCollision(self) -> hints.Incomplete: ...
        bCollision = hints.normal_property(_get_bCollision)
        def _get_pSwEndSwitchViolationList(self) -> 'IJHAxisPositionList': ...
        pSwEndSwitchViolationList = hints.normal_property(_get_pSwEndSwitchViolationList)


JHPositioningResult._com_interfaces_ = [IJHPositioningResult]

IJHRemoteErrorEntry._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property number'), 'propget'],
        HRESULT,
        'Number',
        (['out', 'retval'], POINTER(c_int), 'plNumber')
    ),
    COMMETHOD(
        [dispid(1), helpstring('property number'), 'propput'],
        HRESULT,
        'Number',
        (['in'], c_int, 'plNumber')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property class'), 'propget'],
        HRESULT,
        'Class',
        (['out', 'retval'], POINTER(DNC_ERROR_CLASS), 'pClass')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property class'), 'propput'],
        HRESULT,
        'Class',
        (['in'], DNC_ERROR_CLASS, 'pClass')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property group'), 'propget'],
        HRESULT,
        'Group',
        (['out', 'retval'], POINTER(DNC_ERROR_GROUP), 'pGroup')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property group'), 'propput'],
        HRESULT,
        'Group',
        (['in'], DNC_ERROR_GROUP, 'pGroup')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property errorText'), 'propget'],
        HRESULT,
        'Text',
        (['out', 'retval'], POINTER(BSTR), 'pbstrErrorText')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property errorText'), 'propput'],
        HRESULT,
        'Text',
        (['in'], BSTR, 'pbstrErrorText')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property channel'), 'propget'],
        HRESULT,
        'Channel',
        (['out', 'retval'], POINTER(c_int), 'plChannelId')
    ),
    COMMETHOD(
        [dispid(6), helpstring('property channel'), 'propput'],
        HRESULT,
        'Channel',
        (['in'], c_int, 'plChannelId')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property sourceFile'), 'propget'],
        HRESULT,
        'SourceFile',
        (['out', 'retval'], POINTER(BSTR), 'pbstrSourceFile')
    ),
    COMMETHOD(
        [dispid(7), helpstring('property sourceFile'), 'propput'],
        HRESULT,
        'SourceFile',
        (['in'], BSTR, 'pbstrSourceFile')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property source line number'), 'propget'],
        HRESULT,
        'SourceLineNr',
        (['out', 'retval'], POINTER(c_int), 'plSourceLineNr')
    ),
    COMMETHOD(
        [dispid(8), helpstring('property source line number'), 'propput'],
        HRESULT,
        'SourceLineNr',
        (['in'], c_int, 'plSourceLineNr')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property call stack'), 'propget'],
        HRESULT,
        'CallStack',
        (['out', 'retval'], POINTER(BSTR), 'pbstrCallStack')
    ),
    COMMETHOD(
        [dispid(9), helpstring('property call stack'), 'propput'],
        HRESULT,
        'CallStack',
        (['in'], BSTR, 'pbstrCallStack')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property client short name'), 'propget'],
        HRESULT,
        'ClientShortName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrClientShortName')
    ),
    COMMETHOD(
        [dispid(10), helpstring('property client short name'), 'propput'],
        HRESULT,
        'ClientShortName',
        (['in'], BSTR, 'pbstrClientShortName')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property client description'), 'propget'],
        HRESULT,
        'ClientDescription',
        (['out', 'retval'], POINTER(BSTR), 'pbstrClientDescription')
    ),
    COMMETHOD(
        [dispid(11), helpstring('property client description'), 'propput'],
        HRESULT,
        'ClientDescription',
        (['in'], BSTR, 'pbstrClientDescription')
    ),
    COMMETHOD(
        [dispid(12), helpstring('property cause'), 'propget'],
        HRESULT,
        'Cause',
        (['out', 'retval'], POINTER(BSTR), 'pbstrCause')
    ),
    COMMETHOD(
        [dispid(12), helpstring('property cause'), 'propput'],
        HRESULT,
        'Cause',
        (['in'], BSTR, 'pbstrCause')
    ),
    COMMETHOD(
        [dispid(13), helpstring('property Action'), 'propget'],
        HRESULT,
        'Action',
        (['out', 'retval'], POINTER(BSTR), 'pbstrAction')
    ),
    COMMETHOD(
        [dispid(13), helpstring('property Action'), 'propput'],
        HRESULT,
        'Action',
        (['in'], BSTR, 'pbstrAction')
    ),
    COMMETHOD(
        [dispid(14), helpstring('property Internals'), 'propget'],
        HRESULT,
        'Internals',
        (['out', 'retval'], POINTER(BSTR), 'pbstrInternals')
    ),
    COMMETHOD(
        [dispid(14), helpstring('property Internals'), 'propput'],
        HRESULT,
        'Internals',
        (['in'], BSTR, 'pbstrInternals')
    ),
    COMMETHOD(
        [dispid(15), helpstring('property help file'), 'propget'],
        HRESULT,
        'HelpFile',
        (['out', 'retval'], POINTER(BSTR), 'pbstrHelpFile')
    ),
    COMMETHOD(
        [dispid(15), helpstring('property help file'), 'propput'],
        HRESULT,
        'HelpFile',
        (['in'], BSTR, 'pbstrHelpFile')
    ),
    COMMETHOD(
        [dispid(16), helpstring('property help context ID'), 'propget'],
        HRESULT,
        'HelpContextId',
        (['out', 'retval'], POINTER(c_int), 'plHelpContextId')
    ),
    COMMETHOD(
        [dispid(16), helpstring('property help context ID'), 'propput'],
        HRESULT,
        'HelpContextId',
        (['in'], c_int, 'plHelpContextId')
    ),
    COMMETHOD(
        [dispid(17), helpstring('method Raise this error on server')],
        HRESULT,
        'Raise',
        (['in', 'optional'], VARIANT, 'varbWithRemoveAck')
    ),
    COMMETHOD(
        [dispid(18), helpstring('method Remove this error on server')],
        HRESULT,
        'Remove',
    ),
]

################################################################
# code template for IJHRemoteErrorEntry implementation
# class IJHRemoteErrorEntry_Impl(object):
#     def _get(self):
#         'property number'
#         #return plNumber
#     def _set(self, plNumber):
#         'property number'
#     Number = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property class'
#         #return pClass
#     def _set(self, pClass):
#         'property class'
#     Class = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property group'
#         #return pGroup
#     def _set(self, pGroup):
#         'property group'
#     Group = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property errorText'
#         #return pbstrErrorText
#     def _set(self, pbstrErrorText):
#         'property errorText'
#     Text = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property channel'
#         #return plChannelId
#     def _set(self, plChannelId):
#         'property channel'
#     Channel = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property sourceFile'
#         #return pbstrSourceFile
#     def _set(self, pbstrSourceFile):
#         'property sourceFile'
#     SourceFile = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property source line number'
#         #return plSourceLineNr
#     def _set(self, plSourceLineNr):
#         'property source line number'
#     SourceLineNr = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property call stack'
#         #return pbstrCallStack
#     def _set(self, pbstrCallStack):
#         'property call stack'
#     CallStack = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property client short name'
#         #return pbstrClientShortName
#     def _set(self, pbstrClientShortName):
#         'property client short name'
#     ClientShortName = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property client description'
#         #return pbstrClientDescription
#     def _set(self, pbstrClientDescription):
#         'property client description'
#     ClientDescription = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property cause'
#         #return pbstrCause
#     def _set(self, pbstrCause):
#         'property cause'
#     Cause = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Action'
#         #return pbstrAction
#     def _set(self, pbstrAction):
#         'property Action'
#     Action = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property Internals'
#         #return pbstrInternals
#     def _set(self, pbstrInternals):
#         'property Internals'
#     Internals = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property help file'
#         #return pbstrHelpFile
#     def _set(self, pbstrHelpFile):
#         'property help file'
#     HelpFile = property(_get, _set, doc = _set.__doc__)
#
#     def _get(self):
#         'property help context ID'
#         #return plHelpContextId
#     def _set(self, plHelpContextId):
#         'property help context ID'
#     HelpContextId = property(_get, _set, doc = _set.__doc__)
#
#     def Raise(self, varbWithRemoveAck):
#         'method Raise this error on server'
#         #return 
#
#     def Remove(self):
#         'method Remove this error on server'
#         #return 
#

IJHVirtualMachine._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('increase the CNC program execution speed')],
        HRESULT,
        'ActivateTurboMode',
        (['in'], VARIANT_BOOL, 'bActivate')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Set the acceleration factor for the CNC program execution speed')],
        HRESULT,
        'SetTurboFactor',
        (['in'], c_double, 'dAccelerationFactor')
    ),
    COMMETHOD(
        [dispid(3), helpstring('Set machine axes to the given position immediately'), 'hidden'],
        HRESULT,
        'SetPosition',
        (['in'], c_int, 'lChannel'),
        (['in'], POINTER(IJHAxisPositionList), 'pMcsPositions'),
        (['out', 'retval'], POINTER(POINTER(IJHPositioningResult)), 'ppResult')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Verify the given position can be reached')],
        HRESULT,
        'VerifyPosition',
        (['in'], c_int, 'lChannel'),
        (['in'], POINTER(IJHAxisPositionList), 'pMcsPositions'),
        (['in'], POINTER(IJHToolId), 'pToolToUse'),
        (['out', 'retval'], POINTER(POINTER(IJHPositioningResult)), 'ppResult')
    ),
    COMMETHOD(
        [dispid(5), helpstring('Return the actual axis positions in the MCS')],
        HRESULT,
        'GetPosition',
        (['in'], c_int, 'lChannel'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionList)),
            'ppMcsPositionList',
        )
    ),
]

################################################################
# code template for IJHVirtualMachine implementation
# class IJHVirtualMachine_Impl(object):
#     def ActivateTurboMode(self, bActivate):
#         'increase the CNC program execution speed'
#         #return 
#
#     def SetTurboFactor(self, dAccelerationFactor):
#         'Set the acceleration factor for the CNC program execution speed'
#         #return 
#
#     def SetPosition(self, lChannel, pMcsPositions):
#         'Set machine axes to the given position immediately'
#         #return ppResult
#
#     def VerifyPosition(self, lChannel, pMcsPositions, pToolToUse):
#         'Verify the given position can be reached'
#         #return ppResult
#
#     def GetPosition(self, lChannel):
#         'Return the actual axis positions in the MCS'
#         #return ppMcsPositionList
#


class IJHPlc(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHPlc Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{9350EF31-0B81-4517-A7D8-DB355F48ECD2}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def SetPlcData(self, bstrPlcString: hints.Incomplete, lPlcMarkers: hints.Incomplete, lPlcDWords: hints.Incomplete) -> hints.Hresult: ...


IJHPlc._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method SetPlcData')],
        HRESULT,
        'SetPlcData',
        (['in'], BSTR, 'bstrPlcString'),
        (['in'], POINTER(_midlSAFEARRAY(c_int)), 'lPlcMarkers'),
        (['in'], POINTER(_midlSAFEARRAY(c_int)), 'lPlcDWords')
    ),
]

################################################################
# code template for IJHPlc implementation
# class IJHPlc_Impl(object):
#     def SetPlcData(self, bstrPlcString, lPlcMarkers, lPlcDWords):
#         'method SetPlcData'
#         #return 
#


class JHDataEntry2Enum(CoClass):
    """JHDataEntry2Enum Class"""
    _reg_clsid_ = GUID('{FBF102DD-0AEF-4B12-A9B0-BF3C6F8B7181}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntry2Enum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHErrorEntryList(CoClass):
    """JHErrorEntryList Class"""
    _reg_clsid_ = GUID('{E0279A07-A5FB-408A-9B33-70E66AA03E56}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHErrorEntryList._com_interfaces_ = [IJHErrorEntryList, IJHLoggingInternal]


class JHToolId0(CoClass):
    """JHToolId Class"""
    _reg_clsid_ = GUID('{71DEC7F2-4EF3-4A38-8DA1-216F1D0A8AFB}')
    _idlflags_ = ['hidden']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHToolId0._com_interfaces_ = [IJHToolId, IJHLoggingInternal]

_IJHAutomaticEvents._methods_ = [
    COMMETHOD(
        [helpstring('Signals a program status change')],
        HRESULT,
        'OnProgramStatusChanged',
        (['in'], DNC_EVT_PROGRAM, 'programEvent')
    ),
    COMMETHOD(
        [helpstring('Signals the change of the DNC-mode')],
        HRESULT,
        'OnDncModeChanged',
        (['in'], DNC_MODE, 'newDncMode')
    ),
]

################################################################
# code template for _IJHAutomaticEvents implementation
# class _IJHAutomaticEvents_Impl(object):
#     def OnProgramStatusChanged(self, programEvent):
#         'Signals a program status change'
#         #return 
#
#     def OnDncModeChanged(self, newDncMode):
#         'Signals the change of the DNC-mode'
#         #return 
#

_IJHAutomaticEvents2._methods_ = [
    COMMETHOD(
        [helpstring('This event is fired by the NC on a specific part program command')],
        HRESULT,
        'OnExecutionMessage',
        (['in'], c_int, 'lChannel'),
        (['in'], VARIANT, 'varNumericValue'),
        (['in'], BSTR, 'bstrValue')
    ),
    COMMETHOD(
        [helpstring('method OnProgramChanged')],
        HRESULT,
        'OnProgramChanged',
        (['in'], c_int, 'lChannel'),
        (['in'], c_double, 'dTimeStamp'),
        (['in'], BSTR, 'bstrNewProgram')
    ),
    COMMETHOD(
        [helpstring('method OnToolChanged')],
        HRESULT,
        'OnToolChanged',
        (['in'], c_int, 'lChannel'),
        (['in'], POINTER(IJHToolId), 'pidToolOut'),
        (['in'], POINTER(IJHToolId), 'pidToolIn'),
        (['in'], c_double, 'dTimeStamp')
    ),
]

################################################################
# code template for _IJHAutomaticEvents2 implementation
# class _IJHAutomaticEvents2_Impl(object):
#     def OnExecutionMessage(self, lChannel, varNumericValue, bstrValue):
#         'This event is fired by the NC on a specific part program command'
#         #return 
#
#     def OnProgramChanged(self, lChannel, dTimeStamp, bstrNewProgram):
#         'method OnProgramChanged'
#         #return 
#
#     def OnToolChanged(self, lChannel, pidToolOut, pidToolIn, dTimeStamp):
#         'method OnToolChanged'
#         #return 
#

_IJHAutomaticEvents3._methods_ = [
    COMMETHOD(
        [helpstring('This event is fired by the NC on a specific part program command')],
        HRESULT,
        'OnExecutionModeChanged',
        (['in'], c_int, 'lChannel'),
        (['in'], DNC_EXEC_MODE, 'executionMode')
    ),
]

################################################################
# code template for _IJHAutomaticEvents3 implementation
# class _IJHAutomaticEvents3_Impl(object):
#     def OnExecutionModeChanged(self, lChannel, executionMode):
#         'This event is fired by the NC on a specific part program command'
#         #return 
#


class IJHRemoteErrorEntryInternal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHRemoteErrorEntryInternal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{5BEF2706-7769-49C5-BB9F-93C5B144460B}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _AcknowledgeRemoveRequest(self, bAllow: hints.Incomplete) -> hints.Hresult: ...


IJHRemoteErrorEntryInternal._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method _AcknowledgeRemoveRequest')],
        HRESULT,
        '_AcknowledgeRemoveRequest',
        (['in'], VARIANT_BOOL, 'bAllow')
    ),
]

################################################################
# code template for IJHRemoteErrorEntryInternal implementation
# class IJHRemoteErrorEntryInternal_Impl(object):
#     def _AcknowledgeRemoveRequest(self, bAllow):
#         'method _AcknowledgeRemoveRequest'
#         #return 
#

IJHDataEntryProperty._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property kind'), 'propget'],
        HRESULT,
        'kind',
        (['out', 'retval'], POINTER(DNC_DATAENTRY_PROPKIND), 'pKind')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property bstrDescription'), 'propget'],
        HRESULT,
        'bstrDescription',
        (['out', 'retval'], POINTER(BSTR), 'pbstrDescription')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property varValue'), 'propget'],
        HRESULT,
        'varValue',
        (['out', 'retval'], POINTER(VARIANT), 'pvarValue')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property varValue'), 'propput'],
        HRESULT,
        'varValue',
        (['in'], VARIANT, 'pvarValue')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property bIsReadOnly'), 'propget'],
        HRESULT,
        'bIsReadOnly',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbIsReadOnly')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property varValueType'), 'propget'],
        HRESULT,
        'varValueType',
        (['out', 'retval'], POINTER(VARIANT), 'pvarValueType')
    ),
]

################################################################
# code template for IJHDataEntryProperty implementation
# class IJHDataEntryProperty_Impl(object):
#     @property
#     def kind(self):
#         'property kind'
#         #return pKind
#
#     @property
#     def bstrDescription(self):
#         'property bstrDescription'
#         #return pbstrDescription
#
#     def _get(self):
#         'property varValue'
#         #return pvarValue
#     def _set(self, pvarValue):
#         'property varValue'
#     varValue = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def bIsReadOnly(self):
#         'property bIsReadOnly'
#         #return pbIsReadOnly
#
#     @property
#     def varValueType(self):
#         'property varValueType'
#         #return pvarValueType
#


class JHAxisInfoEnum(CoClass):
    """JHAxisInfoEnum Class"""
    _reg_clsid_ = GUID('{F722D8DD-B502-46EF-B7A2-CC7F8C555367}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAxisInfoEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]


class JHToolId(CoClass):
    """JHToolId Class"""
    _reg_clsid_ = GUID('{8BB961F4-134B-4DB8-8E4C-0D09D09B38A7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHToolId._com_interfaces_ = [IJHToolId, IJHLoggingInternal]

_IJHPlcEvents._methods_ = [
    COMMETHOD(
        [helpstring('method OnPlcData')],
        HRESULT,
        'OnPlcData',
        (['in'], BSTR, 'bstrPlcString'),
        (['in'], POINTER(_midlSAFEARRAY(c_int)), 'ppsalPlcMarkers'),
        (['in'], POINTER(_midlSAFEARRAY(c_int)), 'ppsalPlcDWords')
    ),
]

################################################################
# code template for _IJHPlcEvents implementation
# class _IJHPlcEvents_Impl(object):
#     def OnPlcData(self, bstrPlcString, ppsalPlcMarkers, ppsalPlcDWords):
#         'method OnPlcData'
#         #return 
#

IJHPositioningResult._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property bEndSwitchTripped'), 'propget'],
        HRESULT,
        'bEndSwitchTripped',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbEndSwitchTripped')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property bCollision'), 'propget'],
        HRESULT,
        'bCollision',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pbCollision')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property pSwEndSwitchViolationList'), 'propget'],
        HRESULT,
        'pSwEndSwitchViolationList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisPositionList)),
            'ppSwEndSwitchViolationList',
        )
    ),
]

################################################################
# code template for IJHPositioningResult implementation
# class IJHPositioningResult_Impl(object):
#     @property
#     def bEndSwitchTripped(self):
#         'property bEndSwitchTripped'
#         #return pbEndSwitchTripped
#
#     @property
#     def bCollision(self):
#         'property bCollision'
#         #return pbCollision
#
#     @property
#     def pSwEndSwitchViolationList(self):
#         'property pSwEndSwitchViolationList'
#         #return ppSwEndSwitchViolationList
#

IJHDataEntryList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHDataEntry object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry)), 'ppDataEntry')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHDataEntryList implementation
# class IJHDataEntryList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHDataEntry object on the specified index in the list'
#         #return ppDataEntry
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#


class JHRemoteErrorEntry(CoClass):
    """JHRemoteErrorEntry Class"""
    _reg_clsid_ = GUID('{361CAB13-130E-448D-A48E-B5A81E7967F1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHRemoteErrorEntry._com_interfaces_ = [IJHRemoteErrorEntry, IJHRemoteErrorEntryInternal, IJHLoggingInternal]


class JHChannelInfoList(CoClass):
    """JHChannelInfoList Class"""
    _reg_clsid_ = GUID('{2BBE14AC-13CF-4E3C-90C0-2F6BD3A48C81}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHChannelInfoList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHChannelInfoList Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{A16C6578-4AC7-4060-A633-4ED91F0A528C}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_Item(self, lIndex: hints.Incomplete) -> 'IJHChannelInfo': ...
        Item = hints.named_property('Item', _get_Item)
        __call__ = hints.to_dunder_call(Item)
        __getitem__ = hints.to_dunder_getitem(Item)
        __setitem__ = hints.to_dunder_setitem(Item)
        def _get__NewEnum(self) -> hints.Incomplete: ...
        _NewEnum = hints.normal_property(_get__NewEnum)
        __iter__ = hints.to_dunder_iter(_NewEnum)
        def _get_Count(self) -> hints.Incomplete: ...
        Count = hints.normal_property(_get_Count)
        __len__ = hints.to_dunder_len(Count)


JHChannelInfoList._com_interfaces_ = [IJHChannelInfoList, IJHLoggingInternal]

IJHDiagnostics._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method SetAccessMode')],
        HRESULT,
        'SetAccessMode',
        (['in'], DNC_ACCESS_MODE, 'accessMode'),
        (['in'], BSTR, 'bstrPassword')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Activate the creation of a service file on the control')],
        HRESULT,
        'StartCreateServiceFile',
        (['in'], BSTR, 'bstrFileName')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method GetAvailableKeys'), 'hidden'],
        HRESULT,
        'GetAvailableKeys',
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaVirtualKeys'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaFunctionalKeys'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaQualifiers'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaActions'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(BSTR)), 'ppsaButtons')
    ),
    COMMETHOD(
        [dispid(4), helpstring('method SendKey'), 'hidden'],
        HRESULT,
        'SendKey',
        (['in'], BSTR, 'bstrWmKey'),
        (['in'], BSTR, 'bstrQualifiers'),
        (['in'], DNC_KEYACTION, 'keyAction')
    ),
    COMMETHOD(
        [dispid(5), helpstring('method SendString'), 'hidden'],
        HRESULT,
        'SendString',
        (['in'], BSTR, 'bstrString')
    ),
    COMMETHOD(
        [dispid(6), helpstring('method MakeScreenShot')],
        HRESULT,
        'MakeScreenShot',
        (['in'], BSTR, 'bstrFileName'),
        (['in', 'optional'], VARIANT, 'xOrigin'),
        (['in', 'optional'], VARIANT, 'yOrigin'),
        (['in', 'optional'], VARIANT, 'width'),
        (['in', 'optional'], VARIANT, 'height')
    ),
]

################################################################
# code template for IJHDiagnostics implementation
# class IJHDiagnostics_Impl(object):
#     def SetAccessMode(self, accessMode, bstrPassword):
#         'method SetAccessMode'
#         #return 
#
#     def StartCreateServiceFile(self, bstrFileName):
#         'Activate the creation of a service file on the control'
#         #return 
#
#     def GetAvailableKeys(self):
#         'method GetAvailableKeys'
#         #return ppsaVirtualKeys, ppsaFunctionalKeys, ppsaQualifiers, ppsaActions, ppsaButtons
#
#     def SendKey(self, bstrWmKey, bstrQualifiers, keyAction):
#         'method SendKey'
#         #return 
#
#     def SendString(self, bstrString):
#         'method SendString'
#         #return 
#
#     def MakeScreenShot(self, bstrFileName, xOrigin, yOrigin, width, height):
#         'method MakeScreenShot'
#         #return 
#


class JHPlc(CoClass):
    """JHPlc Class"""
    _reg_clsid_ = GUID('{DEAEB205-9C89-47D2-833E-039F830190FD}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHPlc._com_interfaces_ = [IJHPlc]
JHPlc._outgoing_interfaces_ = [_DJHPlcEvents, _IJHPlcEvents]


class JHRemoteError(CoClass):
    _reg_clsid_ = GUID('{57887C3F-FFD8-45FA-8197-6B473369AB8B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHRemoteError(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHRemoteError Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{36CEE569-A706-42A0-ABA2-D5B2F51486E9}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def CreateEntry(self, errorNumber: hints.Incomplete, errorClass: hints.Incomplete, bstrErrorString: hints.Incomplete) -> 'IJHRemoteErrorEntry': ...


class IJHRemoteErrorInternal(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHRemoteErrorInternal Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{3F289040-2237-4793-9290-14699981A0CB}')
    _idlflags_ = ['hidden', 'dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _Raise(self, pParent: hints.Incomplete, varbWithRemoveAck: hints.Incomplete) -> hints.Incomplete: ...
        def _Remove(self, lHandle: hints.Incomplete) -> hints.Hresult: ...
        def _AcknowledgeRemoveRequest(self, lRaisedErrorHandle: hints.Incomplete, bAllow: hints.Incomplete) -> hints.Hresult: ...


JHRemoteError._com_interfaces_ = [IJHRemoteError, IJHRemoteErrorInternal]
JHRemoteError._outgoing_interfaces_ = [_DJHRemoteErrorEvents, _IJHRemoteErrorEvents]


class JHDataEntryPropertyList(CoClass):
    """JHDataEntryPropertyList Class"""
    _reg_clsid_ = GUID('{6668C91E-60E4-407E-B12E-4B8CAA734355}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryPropertyList._com_interfaces_ = [IJHDataEntryPropertyList, IJHLoggingInternal]


class JHAutomaticEvents(CoClass):
    """JHAutomaticEvents Class"""
    _reg_clsid_ = GUID('{CF4E5482-182E-4A69-952E-44704324C84F}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHAutomaticEvents._com_interfaces_ = [IEventObject]
JHAutomaticEvents._outgoing_interfaces_ = [_DJHAutomaticEvents, _IJHAutomaticEvents3]


class JHErrorEntry2List(CoClass):
    """JHErrorEntry2List Class"""
    _reg_clsid_ = GUID('{0AA1E6D1-0322-445F-9A60-9009AB76BFB1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHErrorEntry2List._com_interfaces_ = [IJHErrorEntry2List, IJHLoggingInternal]

IJHConfiguration._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieving a list of all available axes')],
        HRESULT,
        'GetAxesInfo',
        (['out', 'retval'], POINTER(POINTER(IJHAxisInfoList)), 'ppList')
    ),
    COMMETHOD(
        [dispid(2), helpstring('Retrieving info about the NC channels of the NC')],
        HRESULT,
        'GetChannelInfo',
        (['out', 'retval'], POINTER(POINTER(IJHChannelInfoList)), 'ppList')
    ),
]

################################################################
# code template for IJHConfiguration implementation
# class IJHConfiguration_Impl(object):
#     def GetAxesInfo(self):
#         'Retrieving a list of all available axes'
#         #return ppList
#
#     def GetChannelInfo(self):
#         'Retrieving info about the NC channels of the NC'
#         #return ppList
#

IJHDataAccess._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Retrieve the DataEntry object that is selected by the path qualifier')],
        HRESULT,
        'GetDataEntry',
        (['in'], BSTR, 'bstrDataSelection'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry)), 'ppDataEntry')
    ),
]

################################################################
# code template for IJHDataAccess implementation
# class IJHDataAccess_Impl(object):
#     def GetDataEntry(self, bstrDataSelection):
#         'Retrieve the DataEntry object that is selected by the path qualifier'
#         #return ppDataEntry
#

IJHDataAccess2._methods_ = [
    COMMETHOD(
        [dispid(2), helpstring('Sets the data access interface to an extended access mode')],
        HRESULT,
        'SetAccessMode',
        (['in'], DNC_ACCESS_MODE, 'accessMode'),
        (['in'], BSTR, 'bstrPassword')
    ),
]

################################################################
# code template for IJHDataAccess2 implementation
# class IJHDataAccess2_Impl(object):
#     def SetAccessMode(self, accessMode, bstrPassword):
#         'Sets the data access interface to an extended access mode'
#         #return 
#

IJHDataAccess3._methods_ = [
    COMMETHOD(
        [dispid(3), helpstring('Retrieve the DataEntry object that is selected by the path qualifier')],
        HRESULT,
        'GetDataEntry2',
        (['in'], BSTR, 'bstrDataSelection'),
        (['in'], DNC_DATA_UNIT_SELECT, 'unitSelect'),
        (['in'], VARIANT_BOOL, 'asString'),
        (['out', 'retval'], POINTER(POINTER(IJHDataEntry2)), 'ppDataEntry')
    ),
    COMMETHOD(
        [dispid(4), helpstring('Lock the given table for exclusive access')],
        HRESULT,
        'LockTable',
        (['in'], BSTR, 'bstrTableSelection'),
        (['out', 'retval'], POINTER(c_int), 'pLockHandle')
    ),
    COMMETHOD(
        [dispid(5), helpstring('Release the previously locked table')],
        HRESULT,
        'UnlockTable',
        (['in'], c_int, 'lockHandle')
    ),
]

################################################################
# code template for IJHDataAccess3 implementation
# class IJHDataAccess3_Impl(object):
#     def GetDataEntry2(self, bstrDataSelection, unitSelect, asString):
#         'Retrieve the DataEntry object that is selected by the path qualifier'
#         #return ppDataEntry
#
#     def LockTable(self, bstrTableSelection):
#         'Lock the given table for exclusive access'
#         #return pLockHandle
#
#     def UnlockTable(self, lockHandle):
#         'Release the previously locked table'
#         #return 
#

IJHDataAccess4._methods_ = [
    COMMETHOD(
        [dispid(6)],
        HRESULT,
        'AddDataEntry',
        (['in'], BSTR, 'bstrFullIdent'),
        (['in', 'optional'], VARIANT, 'varbstrStoragePath')
    ),
    COMMETHOD(
        [dispid(7)],
        HRESULT,
        'RemoveDataEntry',
        (['in'], BSTR, 'bstrFullIdent')
    ),
    COMMETHOD(
        [dispid(8), 'hidden'],
        HRESULT,
        'LockConfig',
        (['in'], _midlSAFEARRAY(BSTR), 'bstrIdentsToLock'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(HRESULT)), 'ppsafLockResults')
    ),
    COMMETHOD(
        [dispid(9), 'hidden'],
        HRESULT,
        'UnlockConfig',
        (['in'], _midlSAFEARRAY(BSTR), 'bstrIdentsToUnlock'),
        (['in', 'out'], POINTER(_midlSAFEARRAY(HRESULT)), 'ppsafUnlockResults')
    ),
    COMMETHOD(
        [dispid(10)],
        HRESULT,
        'SetPlcOption',
        (['in'], DNC_PLC_OPTION, 'plcOption'),
        (['in'], VARIANT_BOOL, 'bActivate')
    ),
]

################################################################
# code template for IJHDataAccess4 implementation
# class IJHDataAccess4_Impl(object):
#     def AddDataEntry(self, bstrFullIdent, varbstrStoragePath):
#         '-no docstring-'
#         #return 
#
#     def RemoveDataEntry(self, bstrFullIdent):
#         '-no docstring-'
#         #return 
#
#     def LockConfig(self, bstrIdentsToLock):
#         '-no docstring-'
#         #return ppsafLockResults
#
#     def UnlockConfig(self, bstrIdentsToUnlock):
#         '-no docstring-'
#         #return ppsafUnlockResults
#
#     def SetPlcOption(self, plcOption, bActivate):
#         '-no docstring-'
#         #return 
#

_IJHDiagnosticsEvents._methods_ = [
    COMMETHOD(
        [helpstring('Service file has been created event')],
        HRESULT,
        'OnServiceFileCreated',
        (['in'], HRESULT, 'result')
    ),
]

################################################################
# code template for _IJHDiagnosticsEvents implementation
# class _IJHDiagnosticsEvents_Impl(object):
#     def OnServiceFileCreated(self, result):
#         'Service file has been created event'
#         #return 
#

IJHAxisInfoList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHAxisInfo object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHAxisInfo)), 'ppAxisInfo')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHAxisInfoList implementation
# class IJHAxisInfoList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHAxisInfo object on the specified index in the list'
#         #return ppAxisInfo
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#

IJHRemoteError._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Create a new remote error entry object')],
        HRESULT,
        'CreateEntry',
        (['in'], c_int, 'errorNumber'),
        (['in'], DNC_ERROR_CLASS, 'errorClass'),
        (['in'], BSTR, 'bstrErrorString'),
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHRemoteErrorEntry)),
            'ppRemoteErrorEntry',
        )
    ),
]

################################################################
# code template for IJHRemoteError implementation
# class IJHRemoteError_Impl(object):
#     def CreateEntry(self, errorNumber, errorClass, bstrErrorString):
#         'Create a new remote error entry object'
#         #return ppRemoteErrorEntry
#


class JHTrigger(CoClass):
    """JHTrigger Class"""
    _reg_clsid_ = GUID('{B19505D6-024A-454C-B5EE-5657F0D66CA1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTrigger._com_interfaces_ = [IJHTrigger, IJHTriggerCondition, IJHTriggerSampling, IJHLoggingInternal]

IJHTriggerCondition._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method TriggerAlways')],
        HRESULT,
        'TriggerAlways',
    ),
    COMMETHOD(
        [dispid(2), helpstring('method TriggerOnChange')],
        HRESULT,
        'TriggerOnChange',
    ),
    COMMETHOD(
        [dispid(3), helpstring('method TriggerOnDeltaChange')],
        HRESULT,
        'TriggerOnDeltaChange',
        (['in'], VARIANT, 'varConditionDelta')
    ),
    COMMETHOD(
        [dispid(4), helpstring('method TriggerOnLevel')],
        HRESULT,
        'TriggerOnLevel',
        (['in'], DNC_TRIG_CONDITION, 'levelCondition'),
        (['in'], VARIANT, 'varConditionLevel')
    ),
    COMMETHOD(
        [dispid(5), helpstring('method TriggerOnRange')],
        HRESULT,
        'TriggerOnRange',
        (['in'], DNC_TRIG_CONDITION, 'rangeCondition'),
        (['in'], VARIANT, 'varConditionLower'),
        (['in'], VARIANT, 'varConditionUpper')
    ),
    COMMETHOD(
        [dispid(6), helpstring('method TriggerOnSustainedLevelForDuration')],
        HRESULT,
        'TriggerOnSustainedLevelForDuration',
        (['in'], DNC_TRIG_CONDITION, 'levelCondition'),
        (['in'], VARIANT, 'varConditionLevel'),
        (['in'], DNC_TRIG_CONDITION, 'durationCondition'),
        (['in'], c_double, 'dDurationLevel')
    ),
    COMMETHOD(
        [dispid(7), helpstring('method TriggerOnSustainedRangeForDuration')],
        HRESULT,
        'TriggerOnSustainedRangeForDuration',
        (['in'], DNC_TRIG_CONDITION, 'rangeCondition'),
        (['in'], VARIANT, 'varConditionLower'),
        (['in'], VARIANT, 'varConditionUpper'),
        (['in'], DNC_TRIG_CONDITION, 'durationCondition'),
        (['in'], c_double, 'dDurationLevel')
    ),
    COMMETHOD(
        [dispid(8), helpstring('method TriggerOnSustainedLevelForRange')],
        HRESULT,
        'TriggerOnSustainedLevelForRange',
        (['in'], DNC_TRIG_CONDITION, 'levelCondition'),
        (['in'], VARIANT, 'varConditionLevel'),
        (['in'], DNC_TRIG_CONDITION, 'durationCondition'),
        (['in'], c_double, 'dDurationLower'),
        (['in'], c_double, 'dDurationUpper')
    ),
    COMMETHOD(
        [dispid(9), helpstring('method TriggerOnSustainedRangeForRange')],
        HRESULT,
        'TriggerOnSustainedRangeForRange',
        (['in'], DNC_TRIG_CONDITION, 'rangeCondition'),
        (['in'], VARIANT, 'varConditionLower'),
        (['in'], VARIANT, 'varConditionUpper'),
        (['in'], DNC_TRIG_CONDITION, 'durationCondition'),
        (['in'], c_double, 'dDurationLower'),
        (['in'], c_double, 'dDurationUpper')
    ),
    COMMETHOD(
        [dispid(10), helpstring('method TriggerOnRisingEdge')],
        HRESULT,
        'TriggerOnRisingEdge',
    ),
    COMMETHOD(
        [dispid(11), helpstring('method TriggerOnRisingEdgeAndLevel')],
        HRESULT,
        'TriggerOnRisingEdgeAndLevel',
        (['in'], DNC_TRIG_CONDITION, 'levelCondition'),
        (['in'], VARIANT, 'varConditionLevel')
    ),
    COMMETHOD(
        [dispid(12), helpstring('method TriggerOnRisingEdgeAndRange')],
        HRESULT,
        'TriggerOnRisingEdgeAndRange',
        (['in'], DNC_TRIG_CONDITION, 'rangeCondition'),
        (['in'], VARIANT, 'varEdgeLower'),
        (['in'], VARIANT, 'varEdgeUpper')
    ),
    COMMETHOD(
        [dispid(13), helpstring('method TriggeronFallingEdge')],
        HRESULT,
        'TriggerOnFallingEdge',
    ),
    COMMETHOD(
        [dispid(14), helpstring('method TriggerOnFallingEdgeAndLevel')],
        HRESULT,
        'TriggerOnFallingEdgeAndLevel',
        (['in'], DNC_TRIG_CONDITION, 'levelCondition'),
        (['in'], VARIANT, 'varConditionLevel')
    ),
    COMMETHOD(
        [dispid(15), helpstring('method TriggerOnFallingEdgeAndRange')],
        HRESULT,
        'TriggerOnFallingEdgeAndRange',
        (['in'], DNC_TRIG_CONDITION, 'rangeCondition'),
        (['in'], VARIANT, 'varEdgeLower'),
        (['in'], VARIANT, 'varEdgeUpper')
    ),
    COMMETHOD(
        [dispid(16), helpstring('property triggerMode'), 'propget'],
        HRESULT,
        'triggerMode',
        (['out', 'retval'], POINTER(DNC_TRIG_MODE), 'pMode')
    ),
    COMMETHOD(
        [dispid(17), helpstring('property triggerCondition'), 'propget'],
        HRESULT,
        'triggerCondition',
        (['out', 'retval'], POINTER(DNC_TRIG_CONDITION), 'pTriggerCondition')
    ),
    COMMETHOD(
        [dispid(18), helpstring('property varTriggerValueLower'), 'propget'],
        HRESULT,
        'varTriggerValueLower',
        (['out', 'retval'], POINTER(VARIANT), 'pvarValueLower')
    ),
    COMMETHOD(
        [dispid(19), helpstring('property varTriggerValueUpper'), 'propget'],
        HRESULT,
        'varTriggerValueUpper',
        (['out', 'retval'], POINTER(VARIANT), 'pvarValueUpper')
    ),
    COMMETHOD(
        [dispid(20), helpstring('property triggerDurationCondition'), 'propget'],
        HRESULT,
        'triggerDurationCondition',
        (['out', 'retval'], POINTER(DNC_TRIG_CONDITION), 'pDurationCondition')
    ),
    COMMETHOD(
        [dispid(21), helpstring('property dTriggerDurationValueLower'), 'propget'],
        HRESULT,
        'dTriggerDurationValueLower',
        (['out', 'retval'], POINTER(c_double), 'pdValueLower')
    ),
    COMMETHOD(
        [dispid(22), helpstring('property dTriggerDurationValueUpper'), 'propget'],
        HRESULT,
        'dTriggerDurationValueUpper',
        (['out', 'retval'], POINTER(c_double), 'pdValueUpper')
    ),
]

################################################################
# code template for IJHTriggerCondition implementation
# class IJHTriggerCondition_Impl(object):
#     def TriggerAlways(self):
#         'method TriggerAlways'
#         #return 
#
#     def TriggerOnChange(self):
#         'method TriggerOnChange'
#         #return 
#
#     def TriggerOnDeltaChange(self, varConditionDelta):
#         'method TriggerOnDeltaChange'
#         #return 
#
#     def TriggerOnLevel(self, levelCondition, varConditionLevel):
#         'method TriggerOnLevel'
#         #return 
#
#     def TriggerOnRange(self, rangeCondition, varConditionLower, varConditionUpper):
#         'method TriggerOnRange'
#         #return 
#
#     def TriggerOnSustainedLevelForDuration(self, levelCondition, varConditionLevel, durationCondition, dDurationLevel):
#         'method TriggerOnSustainedLevelForDuration'
#         #return 
#
#     def TriggerOnSustainedRangeForDuration(self, rangeCondition, varConditionLower, varConditionUpper, durationCondition, dDurationLevel):
#         'method TriggerOnSustainedRangeForDuration'
#         #return 
#
#     def TriggerOnSustainedLevelForRange(self, levelCondition, varConditionLevel, durationCondition, dDurationLower, dDurationUpper):
#         'method TriggerOnSustainedLevelForRange'
#         #return 
#
#     def TriggerOnSustainedRangeForRange(self, rangeCondition, varConditionLower, varConditionUpper, durationCondition, dDurationLower, dDurationUpper):
#         'method TriggerOnSustainedRangeForRange'
#         #return 
#
#     def TriggerOnRisingEdge(self):
#         'method TriggerOnRisingEdge'
#         #return 
#
#     def TriggerOnRisingEdgeAndLevel(self, levelCondition, varConditionLevel):
#         'method TriggerOnRisingEdgeAndLevel'
#         #return 
#
#     def TriggerOnRisingEdgeAndRange(self, rangeCondition, varEdgeLower, varEdgeUpper):
#         'method TriggerOnRisingEdgeAndRange'
#         #return 
#
#     def TriggerOnFallingEdge(self):
#         'method TriggeronFallingEdge'
#         #return 
#
#     def TriggerOnFallingEdgeAndLevel(self, levelCondition, varConditionLevel):
#         'method TriggerOnFallingEdgeAndLevel'
#         #return 
#
#     def TriggerOnFallingEdgeAndRange(self, rangeCondition, varEdgeLower, varEdgeUpper):
#         'method TriggerOnFallingEdgeAndRange'
#         #return 
#
#     @property
#     def triggerMode(self):
#         'property triggerMode'
#         #return pMode
#
#     @property
#     def triggerCondition(self):
#         'property triggerCondition'
#         #return pTriggerCondition
#
#     @property
#     def varTriggerValueLower(self):
#         'property varTriggerValueLower'
#         #return pvarValueLower
#
#     @property
#     def varTriggerValueUpper(self):
#         'property varTriggerValueUpper'
#         #return pvarValueUpper
#
#     @property
#     def triggerDurationCondition(self):
#         'property triggerDurationCondition'
#         #return pDurationCondition
#
#     @property
#     def dTriggerDurationValueLower(self):
#         'property dTriggerDurationValueLower'
#         #return pdValueLower
#
#     @property
#     def dTriggerDurationValueUpper(self):
#         'property dTriggerDurationValueUpper'
#         #return pdValueUpper
#


class JHChannelInfo(CoClass):
    """JHChannelInfo Class"""
    _reg_clsid_ = GUID('{DFB3989C-33BA-4327-8C51-CBC14B523967}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


class IJHChannelInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    """IJHChannelInfo Interface"""
    _case_insensitive_ = True
    _iid_ = GUID('{DD9CCD8B-204D-44B0-A881-95E9CC8A2D25}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def _get_lChannelId(self) -> hints.Incomplete: ...
        lChannelId = hints.normal_property(_get_lChannelId)
        def _get_pAxisInfoList(self) -> 'IJHAxisInfoList': ...
        pAxisInfoList = hints.normal_property(_get_pAxisInfoList)


JHChannelInfo._com_interfaces_ = [IJHChannelInfo, IJHLoggingInternal]

_DJHMachineEvents2._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Fire event OnStateChanged')],
        HRESULT,
        'OnStateChanged',
        (['in'], DNC_EVT_STATE, 'event')
    ),
]


class JHDataEntryProperty2List(CoClass):
    """JHDataEntryProperty2List Class"""
    _reg_clsid_ = GUID('{7C5D3295-109F-455C-90CA-9E1F3B9FAB3C}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryProperty2List._com_interfaces_ = [IJHDataEntryProperty2List, IJHLoggingInternal]

IJHAxisInfo._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property lAxisId'), 'propget'],
        HRESULT,
        'lAxisId',
        (['out', 'retval'], POINTER(c_int), 'pAxisID')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property axisType'), 'propget'],
        HRESULT,
        'axisType',
        (['out', 'retval'], POINTER(DNC_AXISTYPE), 'pAxisType')
    ),
    COMMETHOD(
        [dispid(3), helpstring('property bstrAxisName'), 'propget'],
        HRESULT,
        'bstrAxisName',
        (['out', 'retval'], POINTER(BSTR), 'pbstrAxisName')
    ),
]

################################################################
# code template for IJHAxisInfo implementation
# class IJHAxisInfo_Impl(object):
#     @property
#     def lAxisId(self):
#         'property lAxisId'
#         #return pAxisID
#
#     @property
#     def axisType(self):
#         'property axisType'
#         #return pAxisType
#
#     @property
#     def bstrAxisName(self):
#         'property bstrAxisName'
#         #return pbstrAxisName
#

IJHRemoteErrorInternal._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method _Raise')],
        HRESULT,
        '_Raise',
        (['in'], POINTER(IJHRemoteErrorEntry), 'pParent'),
        (['in'], VARIANT, 'varbWithRemoveAck'),
        (['out', 'retval'], POINTER(c_int), 'plHandle')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method _Remove')],
        HRESULT,
        '_Remove',
        (['in'], c_int, 'lHandle')
    ),
    COMMETHOD(
        [dispid(3), helpstring('method _AcknowledgeRemoveRequest')],
        HRESULT,
        '_AcknowledgeRemoveRequest',
        (['in'], c_int, 'lRaisedErrorHandle'),
        (['in'], VARIANT_BOOL, 'bAllow')
    ),
]

################################################################
# code template for IJHRemoteErrorInternal implementation
# class IJHRemoteErrorInternal_Impl(object):
#     def _Raise(self, pParent, varbWithRemoveAck):
#         'method _Raise'
#         #return plHandle
#
#     def _Remove(self, lHandle):
#         'method _Remove'
#         #return 
#
#     def _AcknowledgeRemoveRequest(self, lRaisedErrorHandle, bAllow):
#         'method _AcknowledgeRemoveRequest'
#         #return 
#


class JHTraceSample(CoClass):
    """JHTraceSample Class"""
    _reg_clsid_ = GUID('{7669C5F4-E7A8-4B7C-9988-AF9D3E07952F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHTraceSample._com_interfaces_ = [IJHTraceSample, IJHLoggingInternal]


class JHMachine(CoClass):
    """JHMachine Class"""
    _reg_clsid_ = GUID('{8FA3D2F7-51B3-4E5F-BCC6-D2F7D7FCA7C1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHMachine._com_interfaces_ = [IJHMachine4, _IJHMachineEvents2Internal, IJHConnection3, IJHSecureConnectionHelper3]
JHMachine._outgoing_interfaces_ = [_DJHMachineEvents2, _IJHMachineEvents2]

_IJHRemoteErrorEvents._methods_ = [
    COMMETHOD(
        [helpstring('Server requests clearance of remote error')],
        HRESULT,
        'OnRemoveRequest',
        (['in'], POINTER(IJHRemoteErrorEntry), 'pRemoteErrorEntry')
    ),
]

################################################################
# code template for _IJHRemoteErrorEvents implementation
# class _IJHRemoteErrorEvents_Impl(object):
#     def OnRemoveRequest(self, pRemoteErrorEntry):
#         'Server requests clearance of remote error'
#         #return 
#


class JHFileSystemEvents(CoClass):
    """JHFileSystemEvents Class"""
    _reg_clsid_ = GUID('{6663C824-03EA-4FF8-BCA5-0FDF250B28A9}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHFileSystemEvents._com_interfaces_ = [IEventObject]
JHFileSystemEvents._outgoing_interfaces_ = [_DJHFileSystemEvents, _IJHFileSystemEvents]

IJHLoggingInternal._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('Write data in Windows Event Log'), 'hidden'],
        HRESULT,
        'Output',
        (['in'], BSTR, 'bstrConnectionName')
    ),
]

################################################################
# code template for IJHLoggingInternal implementation
# class IJHLoggingInternal_Impl(object):
#     def Output(self, bstrConnectionName):
#         'Write data in Windows Event Log'
#         #return 
#

IJHChannelInfoList._methods_ = [
    COMMETHOD(
        [dispid(0), helpstring('JHChannelInfo object on the specified index in the list'), 'propget'],
        HRESULT,
        'Item',
        (['in'], c_int, 'lIndex'),
        (['out', 'retval'], POINTER(POINTER(IJHChannelInfo)), 'ppChannelInfo')
    ),
    COMMETHOD(
        [dispid(-4), helpstring('property _NewEnum'), 'restricted', 'propget'],
        HRESULT,
        '_NewEnum',
        (['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppUnk')
    ),
    COMMETHOD(
        [dispid(1), helpstring('Number of items (0 to count -1)'), 'propget'],
        HRESULT,
        'Count',
        (['out', 'retval'], POINTER(c_int), 'pCount')
    ),
]

################################################################
# code template for IJHChannelInfoList implementation
# class IJHChannelInfoList_Impl(object):
#     @property
#     def Item(self, lIndex):
#         'JHChannelInfo object on the specified index in the list'
#         #return ppChannelInfo
#
#     @property
#     def _NewEnum(self):
#         'property _NewEnum'
#         #return ppUnk
#
#     @property
#     def Count(self):
#         'Number of items (0 to count -1)'
#         #return pCount
#


class JHChannelInfoEnum(CoClass):
    """JHChannelInfoEnum Class"""
    _reg_clsid_ = GUID('{CD9585DF-C94F-41DD-829A-B3C4A4DFB8E5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHChannelInfoEnum._com_interfaces_ = [comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT]

IJHChannelInfo._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('property lChannelId'), 'propget'],
        HRESULT,
        'lChannelId',
        (['out', 'retval'], POINTER(c_int), 'plChannelId')
    ),
    COMMETHOD(
        [dispid(2), helpstring('property pAxisInfoList'), 'propget'],
        HRESULT,
        'pAxisInfoList',
        (
            ['out', 'retval'],
            POINTER(POINTER(IJHAxisInfoList)),
            'ppIJHAXisInfoList',
        )
    ),
]

################################################################
# code template for IJHChannelInfo implementation
# class IJHChannelInfo_Impl(object):
#     @property
#     def lChannelId(self):
#         'property lChannelId'
#         #return plChannelId
#
#     @property
#     def pAxisInfoList(self):
#         'property pAxisInfoList'
#         #return ppIJHAXisInfoList
#

_DJHAxesPositionStreamingEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('method OnAxesPositionsAvailable')],
        HRESULT,
        'OnAxesPositionsAvailable',
    ),
]

IJHMachine4._methods_ = [
    COMMETHOD(
        [dispid(14), helpstring('Request an ad-hoc connection to the selected CNC')],
        HRESULT,
        'ConnectRequest4',
        (['in'], POINTER(IJHConnection3), 'pIConnection'),
        (['in', 'optional'], VARIANT, 'varbstrClientName'),
        (['in', 'optional'], VARIANT, 'varbstrClientGUID')
    ),
]

################################################################
# code template for IJHMachine4 implementation
# class IJHMachine4_Impl(object):
#     def ConnectRequest4(self, pIConnection, varbstrClientName, varbstrClientGUID):
#         'Request an ad-hoc connection to the selected CNC'
#         #return 
#


class JHDataEntryProperty(CoClass):
    """JHDataEntryProperty Class"""
    _reg_clsid_ = GUID('{5AF81AC1-9BF6-4BA7-8D61-4EFEAF72C085}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHDataEntryProperty._com_interfaces_ = [IJHDataEntryProperty2, IJHLoggingInternal]

_DJHTestEvents._disp_methods_ = [
    DISPMETHOD(
        [dispid(1), helpstring('Fire event OnRequestUnlockKeyboard')],
        HRESULT,
        'OnRequestUnlockKeyboard',
    ),
    DISPMETHOD(
        [dispid(2), helpstring('Fire event OnGuiProcessStateChanged')],
        HRESULT,
        'OnGuiProcessStateChanged',
        (['in'], BSTR, 'bstrGuiProcessName'),
        (['in'], BSTR, 'bstrNewState')
    ),
    DISPMETHOD(
        [dispid(3), helpstring('Fire event OnGuiProcessGotFocus')],
        HRESULT,
        'OnGuiProcessGotFocus',
        (['in'], BSTR, 'bstrGuiProcessName')
    ),
]

IJHDataEntryProperty2._methods_ = [
    COMMETHOD(
        [dispid(6), helpstring('read/update stored value from server')],
        HRESULT,
        'ReadValue',
    ),
    COMMETHOD(
        [dispid(7), helpstring('write stored property value to server')],
        HRESULT,
        'WriteValue',
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(8), helpstring('read/update stored value from server and return it')],
        HRESULT,
        'GetValue',
        (['out', 'retval'], POINTER(VARIANT), 'pPropertyValue')
    ),
    COMMETHOD(
        [dispid(9), helpstring('write/update given value to stored  value and write it to server')],
        HRESULT,
        'SetValue',
        (['in'], VARIANT, 'propertyValue'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(10), helpstring('return stored property varValue'), 'propget'],
        HRESULT,
        'value',
        (['out', 'retval'], POINTER(VARIANT), 'pvarValue')
    ),
    COMMETHOD(
        [dispid(10), helpstring('return stored property varValue'), 'propput'],
        HRESULT,
        'value',
        (['in'], VARIANT, 'pvarValue')
    ),
    COMMETHOD(
        [dispid(11), helpstring('return the asString setting'), 'propget'],
        HRESULT,
        'asString',
        (['out', 'retval'], POINTER(VARIANT_BOOL), 'pAsString')
    ),
    COMMETHOD(
        [dispid(12), helpstring('return the unit select setting'), 'propget'],
        HRESULT,
        'unitSelect',
        (['out', 'retval'], POINTER(DNC_DATA_UNIT_SELECT), 'pUnit')
    ),
    COMMETHOD(
        [dispid(13), helpstring('return the unit select setting'), 'propget'],
        HRESULT,
        'bstrFullName',
        (['out', 'retval'], POINTER(BSTR), 'a_pbstrFullName')
    ),
    COMMETHOD(
        [dispid(14), helpstring('return the unit select setting'), 'propget'],
        HRESULT,
        'bstrName',
        (['out', 'retval'], POINTER(BSTR), 'a_pbstrName')
    ),
]

################################################################
# code template for IJHDataEntryProperty2 implementation
# class IJHDataEntryProperty2_Impl(object):
#     def ReadValue(self):
#         'read/update stored value from server'
#         #return 
#
#     def WriteValue(self, bWithFlush):
#         'write stored property value to server'
#         #return 
#
#     def GetValue(self):
#         'read/update stored value from server and return it'
#         #return pPropertyValue
#
#     def SetValue(self, propertyValue, bWithFlush):
#         'write/update given value to stored  value and write it to server'
#         #return 
#
#     def _get(self):
#         'return stored property varValue'
#         #return pvarValue
#     def _set(self, pvarValue):
#         'return stored property varValue'
#     value = property(_get, _set, doc = _set.__doc__)
#
#     @property
#     def asString(self):
#         'return the asString setting'
#         #return pAsString
#
#     @property
#     def unitSelect(self):
#         'return the unit select setting'
#         #return pUnit
#
#     @property
#     def bstrFullName(self):
#         'return the unit select setting'
#         #return a_pbstrFullName
#
#     @property
#     def bstrName(self):
#         'return the unit select setting'
#         #return a_pbstrName
#

IJHDataAccessInternal._methods_ = [
    COMMETHOD(
        [dispid(1), helpstring('method AddBranches')],
        HRESULT,
        '_AddBranches',
        (['in'], POINTER(IJHDataEntry), 'pIParentEntry'),
        (['in', 'out'], POINTER(POINTER(IJHDataEntryList)), 'ppIChildList')
    ),
    COMMETHOD(
        [dispid(2), helpstring('method AddProperties')],
        HRESULT,
        '_AddProperties',
        (['in'], POINTER(IJHDataEntry), 'pIDataEntry'),
        (
            ['in', 'out'],
            POINTER(POINTER(IJHDataEntryPropertyList)),
            'ppIPropertyList',
        )
    ),
    COMMETHOD(
        [dispid(3), helpstring('method Subscribe')],
        HRESULT,
        '_Subscribe',
        (['in'], POINTER(IJHDataEntry), 'pIDataEntry'),
        (['in'], POINTER(IJHTriggerCondition), 'pITriggerCondition'),
        (['in'], POINTER(IJHTriggerSampling), 'pITriggerSampling'),
        (['out', 'retval'], POINTER(c_int), 'plSubscribeHandle')
    ),
    COMMETHOD(
        [dispid(4), helpstring('property propertyValue')],
        HRESULT,
        '_get_propertyValue',
        (['in'], BSTR, 'bstrFullPathName'),
        (['out', 'retval'], POINTER(VARIANT), 'pvarPropertyValue')
    ),
    COMMETHOD(
        [dispid(5), helpstring('property propertyValue')],
        HRESULT,
        '_put_propertyValue',
        (['in'], BSTR, 'bstrFullPathName'),
        (['in'], VARIANT, 'varNewPropertyVal')
    ),
    COMMETHOD(
        [dispid(6), helpstring('method UnSubscribe')],
        HRESULT,
        '_UnSubscribe',
        (['in'], c_int, 'lSubscribeHandle')
    ),
    COMMETHOD(
        [dispid(7), helpstring('method GetPropertyValue')],
        HRESULT,
        '_GetPropertyValue',
        (['in'], BSTR, 'bstrFullPathName'),
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['in'], DNC_DATA_UNIT_SELECT, 'unitSelect'),
        (['in'], VARIANT_BOOL, 'asString'),
        (['out', 'retval'], POINTER(VARIANT), 'pVarServerValue')
    ),
    COMMETHOD(
        [dispid(8), helpstring('method GetPropertyValueList')],
        HRESULT,
        '_GetPropertyValueList',
        (['in'], POINTER(IJHDataEntry2), 'pParentEntry'),
        (['in'], DNC_DATAENTRY_PROPKIND, 'kind'),
        (['out'], POINTER(POINTER(IJHDataEntry2)), 'ppNewDataEntry')
    ),
    COMMETHOD(
        [dispid(9), helpstring('method Subscribe2')],
        HRESULT,
        '_Subscribe2',
        (['in'], POINTER(IJHDataEntry2), 'pParentEntry'),
        (['in'], POINTER(IJHTriggerCondition), 'pITriggerCondition'),
        (['in'], POINTER(IJHTriggerSampling), 'pITriggerSampling'),
        (['out'], POINTER(c_int), 'plSubscribeHandle'),
        (['out'], POINTER(POINTER(IJHDataEntry2)), 'ppSubscribedDataEntry')
    ),
    COMMETHOD(
        [dispid(10), helpstring('write DATA property of this entry and all its children')],
        HRESULT,
        '_WriteTreeValues',
        (['in'], POINTER(IJHDataEntry2), 'pEntry'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(11), helpstring('write DATA property of given DataEntry to the server')],
        HRESULT,
        '_WritePropertyValue',
        (['in'], POINTER(IJHDataEntryProperty2), 'pProperty'),
        (['in'], VARIANT_BOOL, 'bWithFlush')
    ),
    COMMETHOD(
        [dispid(12), helpstring('method AddProperties2')],
        HRESULT,
        '_AddProperties2',
        (['in'], POINTER(IJHDataEntry2), 'a_pIJHDataEntry'),
        (
            ['in', 'out'],
            POINTER(POINTER(IJHDataEntryProperty2List)),
            'ppIJHDataEntryPropertyList',
        )
    ),
    COMMETHOD(
        [dispid(13), helpstring('method AddBranches2')],
        HRESULT,
        '_AddBranches2',
        (['in'], POINTER(IJHDataEntry2), 'pIParentEntry'),
        (
            ['in', 'out'],
            POINTER(POINTER(IJHDataEntry2List)),
            'ppIJHDataEntryList',
        )
    ),
]

################################################################
# code template for IJHDataAccessInternal implementation
# class IJHDataAccessInternal_Impl(object):
#     def _AddBranches(self, pIParentEntry):
#         'method AddBranches'
#         #return ppIChildList
#
#     def _AddProperties(self, pIDataEntry):
#         'method AddProperties'
#         #return ppIPropertyList
#
#     def _Subscribe(self, pIDataEntry, pITriggerCondition, pITriggerSampling):
#         'method Subscribe'
#         #return plSubscribeHandle
#
#     def _get_propertyValue(self, bstrFullPathName):
#         'property propertyValue'
#         #return pvarPropertyValue
#
#     def _put_propertyValue(self, bstrFullPathName, varNewPropertyVal):
#         'property propertyValue'
#         #return 
#
#     def _UnSubscribe(self, lSubscribeHandle):
#         'method UnSubscribe'
#         #return 
#
#     def _GetPropertyValue(self, bstrFullPathName, kind, unitSelect, asString):
#         'method GetPropertyValue'
#         #return pVarServerValue
#
#     def _GetPropertyValueList(self, pParentEntry, kind):
#         'method GetPropertyValueList'
#         #return ppNewDataEntry
#
#     def _Subscribe2(self, pParentEntry, pITriggerCondition, pITriggerSampling):
#         'method Subscribe2'
#         #return plSubscribeHandle, ppSubscribedDataEntry
#
#     def _WriteTreeValues(self, pEntry, bWithFlush):
#         'write DATA property of this entry and all its children'
#         #return 
#
#     def _WritePropertyValue(self, pProperty, bWithFlush):
#         'write DATA property of given DataEntry to the server'
#         #return 
#
#     def _AddProperties2(self, a_pIJHDataEntry):
#         'method AddProperties2'
#         #return ppIJHDataEntryPropertyList
#
#     def _AddBranches2(self, pIParentEntry):
#         'method AddBranches2'
#         #return ppIJHDataEntryList
#


class JHSoftwareVersionList(CoClass):
    """JHSoftwareVersionList Class"""
    _reg_clsid_ = GUID('{C607E43A-2372-44B0-988F-F032A3751EA6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{14B95319-AEF9-492A-A878-CA18FEB1F5BF}', 1, 7)


JHSoftwareVersionList._com_interfaces_ = [IJHSoftwareVersionList, IJHLoggingInternal]

__all__ = [
    'DNC_EXEC_MDI', 'DNC_CP_DIO_LEADERLENGTH',
    'DNC_E_INVALID_PASSWORD', 'DNC_CP_SSH_IDENT',
    'DNC_ACCESS_MODE_USR', 'DNC_TRIG_ON_CONDITION',
    'DNC_CNC_TYPE_TNC128_NCK', '_IJHDataAccessEvents',
    'DNC_KEYACTION_DOWN', 'DNC_DATA_UNIT_AMPERE', 'IJHVirtualMachine',
    'DNC_EVT_STATE_HOST_STOPPED', 'JHTest',
    'DNC_POSSAMPLES_LOGGING_NONLINEAR_SAMPLED_WITH_BLOCK_END',
    'DNC_CNC_TYPE_AR6000_NCK', 'DNC_TRIG_SAMPLE_ON_CHANGE',
    '_DJHTestEvents', 'JHTraceSampleEnum', 'DNC_PRG_EVT_SELECTED',
    'DNC_CP_LSV_DELAY', 'DNC_ACCESS_MODE_SCOPE',
    'DNC_PRG_STS_INTERRUPTED', 'DNC_INTERFACE_JHDATAACCESS',
    'JHDirectoryEntryEnum', 'DNC_TRACE_VARIABLE_ID_VNOM',
    'JHErrorEntryEnum', 'IJHAxisPositionList',
    'DNC_SPINDLE_STATE_TAPPING', 'DNC_INTERFACE_JHVIRTUALMACHINE',
    'DNC_E_DIR_NOT_FOUND', 'DNC_CNC_TYPE_MANUALPLUS_NCK',
    'DNC_TRACE_VARIABLE_ID_JNOM', 'DNC_CONNECTION_PROPERTY',
    'DNC_E_DIR_REMOTE_LOCKED', 'DNC_ACCESS_MODE_AUTOMATIC',
    'IJHAutomatic4', 'JHVersion', 'DNC_EXEC_OTHER',
    'DNC32_E_FAIL_HANDLE', 'DNC32_E_NO_AUTODETECT',
    'DNC_TRIG_SEQUENCE_AND_THEN', 'DNC_SW_TYPE_TNC_OTHER',
    'DNC_ATTRIBUTE_TYPE', 'DNC_STATE_MACHINE_IS_INITIALIZING',
    'JHFileAttributes', 'IEventObject', 'DNC_TRIG_SAMPLE_ON_IPO',
    'DNC_SW_TYPE_FS_MCU', 'DNC_E_DIR_NOT_EMPTY', 'DNC_E_DIR_NESTING',
    'DNC_KEYACTION_DOWN_UP', 'DNC_EVT_STATE_HOST_AVAILABLE',
    'IJHRemoteErrorEntry', 'DNC_ATTRIBUTE_LOCKED',
    'DNC_POSSAMPLES_LOGGING_NONLINEAR_SAMPLED_WITH_BLOCK_END_WITH_AUX_AXES',
    'DNC_INTERFACE_JHREMOTEERROR',
    'DNC_DATAENTRY_PROPKIND_UPPER_BOUND',
    'DNC_CNC_TYPE_GRINDPLUS640_NCK', 'IJHAxesPositionStreaming2',
    'DNC_PRG_STS_NOT_SELECTED', '_IJHMachineEvents2',
    'JHTraceChannel', 'DNC_ERROR_CLASS', 'IJHAutomatic2',
    'IJHLoggingInternal', 'IJHConnection',
    'DNC_DATAENTRY_PROPKIND_BASE_ENTRY',
    'DNC_EVT_STATE_MACHINE_AVAILABLE', 'DNC_SW_TYPE_TNC_OPT',
    'DNC_ACCESS_MODE_HWSDATAACCESS', 'DNC_TRIG_ON_RISE',
    '_IJHAxesPositionStreamingEvents', 'JHTraceSample',
    'DNC_ACCESS_MODE_DSP', 'DNC_TRIG_ON_COND_LEQ',
    'DNC_DATA_UNIT_METER_PER_SEC3', 'DNC_E_FILE_REMOTE_LOCKED',
    'DNC_POSSAMPLES_MOTION_LINEAR', 'IJHTriggerList', 'IJHAutomatic3',
    'DNC_CP_LSV_TX_TIMEOUT', 'DNC_ACCESS_MODE_USR_PRIVATE',
    'DNC_DATA_UNIT', 'DNC_SW_TYPE_SPLC', 'JHBreakCondition',
    'DNC_E_FILE_FILENAME', 'DNC_PRG_EVT_CANCELED',
    'DNC32_E_NOT_HANDLE', 'DNC_E_UTC_TO_LOCAL',
    'DNC_E_NO_TRACING_ACTIVE', 'DNC_HANDLE',
    'DNC_E_CANNOT_RESTORE_DEFAULT', 'DNC_E_UNABLE_TO_INSERT',
    'DNC32_E_TIMEOUT_VAL', 'DNC_EXEC_HANDWHEEL',
    'DNC_POSSAMPLES_LOGGING_SAMPLED', 'DNC_ACCESS_MODE_CFGDATAACCESS',
    'DNC_ACCESS_MODE_GEOSIMDATAACCESS', 'DNC_SW_TYPE_FCL',
    'DNC_TRIG_ON_COND_GEQ', 'DNC_E_DIR_REMOTE_NOT_FOUND',
    'DNC_PROT_RPC', 'DNC_TRIG_ON_FALL', 'DNC_PRG_STS_ERROR',
    'DNC_TRACE_VARIABLE_ID_IPODBG', 'DNC_CNC_TYPE_MILLPLUSIT',
    'DNC_KEYACTION_UP', 'DNC_E_INVALID_CHANNEL', 'DNC32_E_NO_PORT',
    'JHDataEntryProperty2Enum', 'DNC_DATA_UNIT_NONE',
    'DNC_E_DIR_LOCKED', 'DNC_TRACE_VARIABLE_ID_ININT',
    'DNC_ACCESS_MODE_SPLCDATAACCESS', 'DNC_E_DNC32FAILED', 'IJHPlc',
    'DNC_TRACE_VARIABLE_ID_INOM', 'DNC_E_FILE_REMOTE_EXISTS',
    'JHAutomaticEvents', 'DNC_EXEC_MANUAL', 'DNC_CNC_TYPE_TNC7_NCK',
    'DNC_TRIG_INTERFACE_CONDITION', 'DNC_EVT_STATE_WAIT_PERMISSION',
    'IJHDirectoryEntryList', 'DNC_E_ALL_CONNECTIONS_IN_USE',
    'DNC_E_TOO_MANY_ELEMENTS', 'IJHDirectoryEntry',
    'DNC_SW_TYPE_TNC_ICTL3', 'DNC_POSSAMPLES_LOGGING_TYPE',
    'IJHDataAccess2', 'DNC_TRACE_VARIABLE_ID_JACT',
    'DNC_E_INVALID_AXIS', 'DNC_TRACE_VARIABLE_ID', 'DNC_EXEC_MODE',
    'DNC32_E_LISTEN_FAIL', 'DNC_EVT_STATE_MACHINE_BOOTED',
    'DNC_EC_NONE', 'DNC_DATA_UNIT_METER_PER_SEC', 'IJHDiagnostics',
    'JHConfiguration', 'DNC_ACCESS_MODE_PLCDATAACCESS',
    'IJHRemoteErrorEntryInternal', 'DNC_SW_TYPE_PLC', 'DNC_EC_NOTE',
    'DNC32_E_NOT_CONN', 'DNC_E_CLIENT_REJECTED',
    'DNC_TRIG_SEQUENCE_NONE', 'JHTraceVariableList',
    'DNC_E_DIR_EXISTS', 'DNC_DATA_UNIT_MILLIMETER_PER_MINUTE',
    'DNC_SW_TYPE_TNC_SG', 'JHDataEntry2Enum', 'DNC32_E_RESERVED',
    'IJHTraceChannel', 'DNC_PLC_ACTION_WRITE', 'DNC_TRIG_ON_COND_LT',
    'DNC_STS_PROGRAM', '_DJHMachineEvents2', 'DNC_EG_OPERATING',
    'IJHSecureConnectionHelper2', 'IJHSecureConnectionHelper3',
    'DNC_ERROR_LOCATION', 'DNC32_E_FAIL_WINSOCK',
    'IJHDataAccessInternal', 'DNC_EG_PROGRAMING', 'DNC_EVT_STATE',
    'DNC_DATA_UNIT_MILLIMETER_PER_SEC3', 'DNC32_E_RECV_FRAME',
    'IJHErrorEntryList', 'IJHTraceSampleList', 'DNC_PROT_TCPIP',
    'DNC_DATAENTRY_PROPKIND_SAMPLE_CAPABILITY',
    'DNC_DATA_UNIT_DEGREE_PER_SEC3', 'DNC_SW_TYPE_MP_ADMS',
    'DNC_PROT_DIO', 'DNC_TRACE_VARIABLE_ID_VNNOM',
    'DNC_ACCESS_MODE_OEM', 'DNC_TRIG_ON_COND_NONE', 'JHPlcEvents',
    'DNC_TRACE_VARIABLE_ID_VACT', 'TNCTable',
    'DNC_TRACE_VARIABLE_ID_VNACT', 'DNC32_E_FAIL_SOCKET',
    'JHAxisInfoEnum', 'DNC_ACCESS_MODE_NONE', 'IJHTraceChannelList',
    'DNC_E_INVALID_DATA', 'DNC_ACCESS_MODE_DIAGNOSTICS',
    'IJHDataEntryProperty2', 'DNC_E_HARD_DISK_FAIL',
    'DNC_PRG_EVT_COMPLETED', 'JHPositioningResult',
    'DNC_ACCESS_MODE_SYS', 'DNC_SW_TYPE', 'DNC_E_NOT_ADVISED',
    'DNC_CNC_TYPE_TNC320_NCK', 'DNC_TRIG_ON_CHANGE_DELTA',
    'DNC_TRACE_VARIABLE_ID_SACT', 'IJHProgramPositionList',
    'JHFileSystemEvents', '_IJHTestEvents', 'DNC_AXISTYPE_AUX_ROTARY',
    '_IJHMachineEvents2Internal', 'DNC_E_WRONG_OPERATE_MODE',
    'DNC_EXEC_SINGLESTEP', '_DJHDiagnosticsEvents', 'DNC_HRESULT',
    'DNC_E_MULTIPLE_OBJECTS', 'DNC32_E_PARITY', 'JHMachineInProcess',
    'DNC_CNC_TYPE', 'IJHCutterLocation', 'DNC_PROTOCOL',
    'JHTestEvents', 'IJHError3', 'IJHDataEntryProperty',
    'DNC_TRIG_ON_CHANGE', 'DNC_SW_TYPE_TNC_DSP1',
    '_DJHAxesPositionStreamingEvents', 'JHMachineInProcessEvents2',
    'DNC_STATE_HOST_IS_AVAILABLE', '_DJHDataAccessEvents', 'Library',
    'DNC_PLC_SIZE_WORD', 'DNC_E_NO_TRACE_DATA_AVAILABLE',
    '_IJHPlcEvents', 'DNC_TRACE_VARIABLE_ID_NONE', 'DNC_PROT_LSV2',
    '_DJHFileSystemEvents', 'IJHTraceInternal', 'IJHVersion',
    'DNC_EC_INFO', 'DNC_CP_SPEED', 'IJHErrorInternal',
    'DNC_E_FILE_OVERFLOW', 'DNC_CNC_TYPE_ITNC',
    'DNC_ACCESS_MODE_GEODATAACCESS', 'DNC_STATE_WAITING_PERMISSION',
    'DNC_E_PROGRAM_NOT_STARTED', 'DNC_DATA_UNIT_METER_PER_SEC4',
    'DNC_DATA_UNIT_INCH_PER_MINUTE', 'JHCutterLocationList',
    'DNC_PRG_EVT_FINISHED', 'DNC_TRACE_VARIABLE_TYPE_AXIS',
    'DNC_TRACE_VARIABLE_TYPE_PATH', 'DNC_ACCESS_MODE_PLCDEBUG',
    'DNC_TRACE_VARIABLE_ID_BLOCK_NR', 'DNC_E_ITEM_DELETED',
    'DNC_SW_TYPE_TNC_DSP3', 'DNC_ACCESS_MODE_SENDKEY',
    'DNC_ERROR_LOCATION_NONE', 'DNC_SW_TYPE_TNC_DSP2',
    'IJHCutterPosition', 'DNC_E_NO_PROGRAM', 'DNC_TRIG_ALWAYS',
    'DNC_CNC_TYPE_TURNPLUS', 'DNC_PRG_EVT_SELECT_CLEARED',
    'DNC_STATE_MACHINE_IS_AVAILABLE', 'DNC_INTERFACE_TNCTABLE',
    'DNC_E_MISSING_PARAM', 'DNC_CP_SSH_IDENT_PASSWORD',
    'DNC_TRACE_VARIABLE_ID_SDIFF', 'DNC_EG_PLC', 'DNC32_E_OPTION_VAL',
    'JHTrigger', 'DNC_E_OPTION_NOT_AVAILABLE', 'DNC_E_FILE_EXISTS',
    'JHProgramPositionList', 'DNC_DATA_UNIT_MILLIMETER',
    'IJHFileAttributes', 'JHToolId', 'DNC_PRG_EVT_ERROR_CLEARED',
    'DNC_PLC_SIZE', 'DNC_SW_TYPE_UNKNOWN',
    'DNC_INTERFACE_JHCONFIGURATION', 'DNC_E_COLLISION',
    'DNC_CP_SSH_REMOTE_HOST_KEY_FINGERPRINT', 'JHPlc',
    'DNC_E_NO_DRIVE_ACCESS', 'JHErrorEntry', 'IJHDataAccess3',
    'DNC_MODE_REMOTE', 'DNC_CP_LSV_RX_TIMEOUT',
    'IJHTraceVariableList', 'DNC32_E_STILL_CONN', 'DNC_EC_ERROR',
    'DNC_AXISTYPE_AUX_LINEAR', 'JHFileSystem',
    'DNC_E_FILE_REMOTE_FILENAME', 'DNC_DATA_UNIT_OTHER',
    'JHSoftwareVersion', 'JHDirectoryEntryList', 'DNC_PLC_SIZE_BIT',
    'DNC_ERROR_LOCATION_EDIT', 'DNC_E_RECORD_NOT_FOUND',
    'DNC_CP_PORT', 'JHCutterLocation', 'DNC_SW_TYPE_FS_CCU',
    'DNC_AXISTYPE_SPINDLE', 'JHTrace', 'DNC32_E_FAIL_CONNECT',
    'DNC_TRIG_ON_COND_GT', 'DNC_STATE_DNC_IS_AVAILABLE',
    'DNC_PLC_TYPE', 'DNC_PRG_STS_FINISHED', 'IJHToolId',
    'IJHChannelInfoList', 'IJHError', 'DNC_SW_TYPE_TNC_DSPSG2',
    'DNC_TRACE_VARIABLE_ID_PLC', 'DNC_EC_EMERGENCY_STOP',
    'DNC_TRIG_SAMPLE_MODE', 'IJHTraceVariable',
    'DNC_DATAENTRY_PROPKIND_DATAWIDTH', 'DNC_SPINDLE_STATE_CW',
    'DNC_ATTRIBUTE_READONLY', 'IJHTrigger', 'DNC_EC_PROGRAMABORT',
    'IJHTriggerCondition', '_IJHDiagnosticsEvents',
    'DNC32_E_VER_TOO_OLD', 'DNC_FILE_OBSERVE_REMOVE',
    'IJHAxesPositionStreaming', 'JHRemoteErrorEvents',
    'DNC_PROGRAMBREAKCONDITION_KIND_IGNORE_PROGRAMMED_STOP',
    'JHAxisPositionEnum', 'DNC_E_IN_USE',
    'DNC_STATE_HOST_IS_NOT_AVAILABLE', 'DNC_ATTRIBUTE_SYSTEM',
    'IJHError2', 'DNC_TRIG_ON_COND_INSIDE',
    'DNC_E_CANNOT_LOAD_PROGRAM', 'IJHAxisPosition',
    'DNC_E_NO_PROGRAM_ACTIVE', 'DNC_DATAENTRY_PROPKIND_DATA',
    'JHDataEntry', 'DNC_PRG_STS_RUNNING', '_IJHErrorEvents',
    'DNC_TRACE_VARIABLE_ID_CSI1', 'DNC_TRIG_MODE',
    'DNC32_E_INVALID_PARAM', 'DNC_E_ECLIPSED', 'DNC_SPINDLE_STATE',
    'DNC_DATA_UNIT_SECOND', 'IJHBreakConditionList',
    'DNC_ATTRIBUTE_DIR', 'IJHMachine2', 'DNC_INTERFACE_JHERROR',
    'DNC_TRIG_ON_COND_EQ', 'DNC_ERROR_LOCATION_OEM',
    '_IJHErrorEvents2', 'DNC_TRIG_INTERFACE_SAMPLING',
    'DNC_PROGRAMBREAKCONDITION_KIND', 'DNC_SW_TYPE_TNC_DSPSG1',
    'DNC_TRIG_SAMPLE_ON_PLC', 'DNC_SW_TYPE_TNC_ICTL2',
    'DNC_PRG_STS_STOPPED', 'DNC_CNC_TYPE_CNCPILOT6xx_NCK',
    'DNC32_E_FAIL_LOOKUP', 'IJHDataEntryProperty2List',
    'DNC_AXISTYPE', 'DNC_EC_FEEDHOLD', 'DNC_CONFIGURE_MODE_ADD',
    'IJHRemoteError', '_DJHAutomaticEvents',
    'DNC_DATAENTRY_PROPKIND_INITIALVALUE', 'DNC_TRIG_INTERFACE',
    'DNC_ATTRIBUTE_HIDDEN', 'DNC_SW_TYPE_MC', 'DNC_DATA_UNIT_SELECT',
    'DNC_DATA_UNIT_DEGREE_PER_SEC2',
    'DNC_DATAENTRY_PROPKIND_UNITTEXT',
    'DNC_DATA_UNIT_MILLIMETER_PER_SEC2', 'JHTraceSampleListList',
    'DNC_CP_LSV_OPTIONS',
    'DNC_POSSAMPLES_LOGGING_SAMPLED_WITH_AUX_AXES',
    'DNC_POSSAMPLES_LOGGING_ENDPOINTS_WITH_AUX_AXES',
    'DNC_E_FILE_IN_USE', 'DNC_EVT_PROGRAM', 'JHRemoteErrorEntry',
    'DNC_EG_NONE', 'JHTraceSampleList', 'DNC_PROT_COM',
    'DNC_TRIG_CONDITION', 'JHAxisPosition',
    'DNC_EVT_STATE_DNC_AVAILABLE', 'IJHProgramPosition',
    'JHDataAccess', 'DNC_EG_PYTHON', 'DNC_PRG_STS_IDLE',
    'DNC_PLC_OPTION_NOSYNC', 'IJHConnectionProperty',
    'IJHCutterLocation2List', 'DNC_ACCESS_MODE_TABLEDATAACCESS',
    'DNC_TRACE_VARIABLE_ID_AACT', 'JHBreakConditionEnum',
    'DNC_STATE_NOT_INITIALIZED', 'DNC_FILE_OBSERVE', 'JHError',
    'DNC32_E_TRANS_FAIL', 'DNC_INTERFACE_JHFILESYSTEM',
    'DNC_PRG_EVT_STOPPED', 'DNC_SW_TYPE_TNC_MODEL', 'IJHConnection3',
    'IJHProcessData', 'DNC_FILE_OBSERVE_REMOVE_ALL',
    'IJHRemoteErrorInternal', 'DNC_AXISTYPE_MAIN_LINEAR',
    'DNC_EVT_STATE_CONNECTION_LOST', 'DNC_TRACE_VARIABLE_ID_SERR',
    'DNC_POSSAMPLES_MOTION_SPLINE',
    'DNC_POSSAMPLES_LOGGING_SAMPLED_WITH_BLOCK_END_WITH_AUX_AXES',
    'DNC_PROGRAMBREAKCONDITION_KIND_DEFAULT', 'DNC_E_READ_ONLY',
    'DNC_CNC_TYPE_TNC6xx_NCK', 'JHDataEntryProperty',
    'FEED_MODE_NORMAL', 'DNC_CP_LSV_AUTODETECT',
    'DNC_TRACE_SOURCE_TYPE', 'DNC_SW_TYPE_TNC_DSPSG3',
    'DNC_PROGRAMBREAKCONDITION_KIND_FORCE_OPTIONAL_STOP',
    'JHCutterPosition', 'DNC_TRACE_VARIABLE_TYPE_UNKNOWN',
    'DNC32_E_NO_ADDRESS', 'DNC_PROT_RPC_SECURE', 'JHDataEntry2List',
    'JHDataEntryPropertyEnum', 'DNC_DATAENTRY_PROPKIND_UNIT',
    'DNC_E_FILE_CANNOT_OPEN', 'DNC_E_NOT_POS_NOW', 'IJHFileSystem',
    'DNC_TRIG_SAMPLE_ON_TIMER', 'IJHDataEntryPropertyList',
    'ITNCTable', 'IJHConfiguration', 'DNC_E_LOCKED',
    'FEED_MODE_RAPID', 'DNC_TRIG_ON_SUSTAINED_CONDITION',
    'DNC_E_WRONG_MODE', 'DNC32_E_NOT_RES', '_IJHDataAccessEvents2',
    'IJHTriggerSampling', 'DNC_DATA_UNIT_DEGREE',
    'DNC_AXISTYPE_MAIN_ROTARY', 'DNC_SW_TYPE_CC',
    'DNC_STATE_MACHINE_IS_SHUTTING_DOWN',
    'DNC_ACCESS_MODE_OEM_ENCRYPTED', 'JHCutterLocation2List',
    '_IJHFileSystemEvents', 'DNC_FEED_MODE', 'DNC_E_ITEM_NOT_FOUND',
    'DNC_ACCESS_MODE_PLC', 'DNC_E_EXISTS', 'DNC_E_FILE_LOCKED',
    'DNC_SPINDLE_STATE_RIGID_TAPPING', 'DNC_E_RPCFAILED',
    'DNC_EXEC_RPF', 'DNC_TRACE_SOURCE_TYPE_PLC', 'JHAutomatic',
    'DNC_STATE_NO_PERMISSION', 'DNC_TRACE_VARIABLE_ID_FEED',
    'DNC_MODE', 'DNC_CNC_TYPE_ATEKM_NCK', 'DNC_E_SUBSCRIPTION_ACTIVE',
    'IJHErrorEntry2', 'IJHDataEntryList',
    'DNC_EVT_STATE_MACHINE_SHUTTING_DOWN', 'IJHAxisPositionListList',
    '_DJHPlcEvents', 'DNC_E_NO_STREAMING_ACTIVE',
    'IJHCutterLocationList', '_IJHTraceEvents', 'IJHErrorEntry',
    'DNC_ATTRIBUTE_MODIFIED', 'JHAxisPositionListEnum',
    'DNC_ACCESS_MODE_TESTUTILITY', 'DNC_ACCESS_MODE_ALL',
    'DNC_TRIG_SEQUENCE_AND', 'IJHMachine4', 'DNC_E_SYNONYM_ACCESS',
    'DNC_SPINDLE_STATE_STOPPED', 'DNC_TRIG_ON_COND_NEQ',
    'DNC_E_TRACING_ACTIVE', 'JHProcessData',
    'DNC_CNC_TYPE_MILLPLUSIT_NCK', 'DNC_E_ENDSWITCH_TRIPPED',
    '_IJHAutomaticEvents', 'DNC_INTERFACE_OBJECT',
    'DNC_E_DIR_REMOTE_EXISTS', 'DNC_ERROR_GROUP', 'JHAxisInfo',
    'DNC_EC_WARNING', 'DNC_PRG_EVT_ERROR', 'DNC_E_NOT_INITIALISED',
    'DNC_SPINDLE_STATE_POS_CTRL', 'DNC_ERROR_LOCATION_MACHINE',
    'DNC_POSSAMPLES_MOTION_TYPE',
    'DNC_PROGRAMBREAKCONDITION_KIND_ON_LINE', 'JHTraceChannelEnum',
    'DNC_CNC_TYPE_MILLPLUS', 'DNC_PLC_ACTION', 'DNC_E_DISK_FULL',
    'DNC_PRG_EVT_INTERRUPTED', 'JHTraceSampleListEnum',
    '_DJHErrorEvents', 'JHAxesPositionStreamingEvents',
    'DNC_SW_TYPE_TNC_ICTL1', 'IJHPositioningResult',
    '_DJHRemoteErrorEvents', 'JHDataEntryList',
    'DNC_TRACE_VARIABLE_ID_ANALOG_OUT', 'DNC_TRIG_ON_COND_OUTSIDE',
    'DNC32_E_RECV_FAIL', 'DNC_ACCESS_MODE_AXESPOSITIONSTREAMING',
    'DNC32_E_CONNECT_LOST', 'DNC_CONFIGURE_MODE_REMOVE',
    'DNC_CONFIGURE_MODE_ALL', 'DNC_EVT_STATE_HOST_NOT_AVAILABLE',
    'JHTriggerEnum', 'DNC_DATA_UNIT_PER_MINUTE',
    'IJHSecureConnectionHelper', 'IJHDataAccess4', 'DNC_CP_STOPBITS',
    'DNC_E_FILE_REMOTE_NOT_FOUND', 'DNC_SW_TYPE_NCKERN',
    'JHDataEntryPropertyList', 'DNC_E_REMOTE_READ_ONLY',
    'JHAxisPositionList', 'JHTraceEvents', 'IJHTraceSampleListList',
    'DNC_E_FILE_LOCAL_OPEN_FAILED', 'DNC32_E_INIT',
    'DNC_DATA_UNIT_METER', 'IJHMachine', 'DNC_E_LOCAL_TO_UTC',
    'DNC_KEYACTION', 'JHCutterLocationEnum',
    'DNC_POSSAMPLES_MOTION_COMPLEX', 'DNC_EG_GENERAL',
    'IJHChannelInfo', 'JHAxesPositionStreaming', 'JHTriggerList',
    'IJHDataEntry', 'DNC_E_OUT_OF_RANGE', 'DNC_INTERFACE_JHTRACE',
    'DNC_E_DIR_OVERFLOW', 'JHTraceVariableEnum', 'JHTraceVariable',
    'JHMachine', 'DNC_E_TRANSFER_ABORT', 'DNC_TRACE_SOURCE_TYPE_CCU',
    'DNC_EVT_STATE_MACHINE_INITIALIZING', 'IJHDataEntry2List',
    'DNC32_E_VER_TOO_NEW',
    'DNC_POSSAMPLES_LOGGING_SAMPLED_WITH_BLOCK_END', 'IJHConnection2',
    'DNC_E_KEY_UNDEFINED', 'JHDataEntryEnum', 'DNC_PRG_EVT_STARTED',
    'DNC_INTERFACE_JHPROCESSDATA', 'IJHTrace', 'DNC_EC_PROGRAMHOLD',
    'JHBreakConditionList', 'JHDataEntryProperty2List',
    'DNC_TRACE_VARIABLE_TYPE_NORMAL', 'DNC_ACCESS_MODE_IPODATAACCESS',
    'DNC_PLC_OPTION', 'IJHMachine3',
    'DNC_DATAENTRY_PROPKIND_SUBSCRIBE_CAPABILITY',
    'DNC_CNC_TYPE_ATEKM', 'DNC_SPINDLE_STATE_CCW',
    'DNC_INTERFACE_JHPLC', 'DNC_EG_REMOTE', 'DNC_CP_SSH_REMOTE_USER',
    'DNC_EXEC_AUTOMATIC', 'DNC_POSSAMPLES_MOTION_CIRCULAR',
    'DNC_EC_RESET', 'DNC_TRACE_SOURCE_TYPE_IPO',
    'JHDiagnosticsEvents', 'DNC_FILE_OBSERVE_ADD',
    'DNC_E_HOST_REJECTED', 'JHChannelInfoEnum', 'IJHDataAccess',
    'DNC_INTERFACE_JHAXESPOSITIONSTREAMING', 'DNC_E_UNABLE_TO_DELETE',
    'JHCutterLocation2Enum', 'IJHTest', 'DNC_STATE',
    'DNC_TRACE_VARIABLE_ID_ANOM', 'DNC_E_RECORD_LOCKED',
    'DNC_DATA_UNIT_INCH', 'DNC_TRIG_MODE_NONE',
    'DNC_ACCESS_MODE_DEFAULT', 'JHToolId0', 'DNC_E_FAIL',
    'JHVirtualMachine', 'JHProgramPositionEnum', 'IJHAxisInfo',
    'DNC_TRACE_VARIABLE_TYPE', 'IJHCutterLocation2',
    'DNC_ACCESS_MODE', 'DNC_ACCESS_MODE_INSPECT',
    'IJHSoftwareVersionList', 'DNC32_E_FAIL_ACCEPT', 'typelib_path',
    'DNC_CONFIGURE_MODE', 'DNC_CP_DIO_FLOWCTRL',
    'DNC_INTERFACE_JHVERSION', 'DNC_TRIG_SAMPLE_ON_CCU',
    'DNC_E_INVALID_PARAM', 'JHChannelInfoList',
    'DNC_POSSAMPLES_LOGGING_ENDPOINTS', 'DNC_EVT_STATE_DNC_STOPPED',
    'IJHTraceSample', 'JHDiagnostics', 'IJHConnectionList',
    'DNC_CP_DATABITS', 'DNC32_E_RECV_TIMEOUT',
    'DNC_PROT_TCPIP_SECURE', 'DNC_CNC_TYPE_GRINDPLUS_NCK',
    'DNC_TRACE_VARIABLE_ID_CCDBG', 'DNC_DATA_UNIT_SELECT_INCH',
    'DNC_DATA_UNIT_DEGREES_PER_MINUTE', 'JHErrorEntry2List',
    'DNC_E_STREAMING_ACTIVE', 'DNC_INTERFACE_JHAUTOMATIC',
    'DNC_E_NOT_LOCKED', 'DNC_INTERFACE_JHDIAGNOSTICS',
    'JHDirectoryEntry', 'JHTraceChannelList', '_IJHRemoteErrorEvents',
    'IJHAutomatic', 'DNC_DATAENTRY_PROPKIND_DESCRIPTION',
    'DNC_E_CANNOT_START_PROGRAM', 'JHProgramPosition',
    'DNC_DATA_UNIT_DEGREE_PER_SEC4', 'DNC_ACCESS_MODE_DNC',
    '_DJHTraceEvents', 'DNC_STATE_HOST_IS_STOPPED',
    'DNC_EVT_STATE_PERMISSION_DENIED', 'DNC_CP_HOST',
    'DNC_DATA_UNIT_METER_PER_SEC2', 'DNC_CP_PARITY',
    'JHSoftwareVersionList', 'DNC_DATAENTRY_PROPKIND_LOCATION',
    'DNC_TRACE_VARIABLE_ID_SNOM', 'DNC_PLC_SIZE_BYTE',
    'DNC_E_FILE_NOT_FOUND', 'DNC_E_UNABLE_TO_SET',
    'DNC_DATA_UNIT_VOLT', 'DNC_TRIG_SEQUENCE_OR', 'DNC_CP_CHECK_DTR',
    'JHDataAccessEvents', 'DNC_MODE_LOCAL', 'JHChannelInfo',
    'JHErrorEntry2Enum', 'DNC_ACCESS_MODE_MONITOR',
    'DNC_TRACE_SOURCE_TYPE_UNKNOWN', 'JHAxisPositionListList',
    'DNC_DATA_UNIT_DEGREE_PER_SEC', 'JHMachineEvents2',
    '_IJHAutomaticEvents3', 'DNC_CP_LSV_RETRIES',
    'JHSoftwareVersionEnum', 'DNC_E_DNC_PROHIBITED',
    'DNC_E_UNABLE_TO_GET', 'DNC_E_TIMEOUT', 'DNC_E_LIST_EMPTY',
    'DNC_DATA_UNIT_SELECT_METRIC', 'DNC_CONFIGURE_MODE_CHANGE',
    'IJHErrorInternal2', 'IJHErrorEntry2List',
    'DNC_TRACE_VARIABLE_TYPE_CHANNEL', 'IJHBreakCondition',
    'DNC_CP_DIO_PROTOCOL', 'DNC_TRACE_VARIABLE_ID_IPOLOGIC',
    'IJHAxisInfoList', '_IJHAutomaticEvents2',
    'DNC_E_FILE_WRONG_MODE', 'IJHDataEntry2',
    'DNC_STATE_DNC_IS_STOPPED', 'DNC_EXEC_SIMULO_TURBO_DEPRECATED',
    'JHAxisInfoList', 'DNC_PLC_TYPE_MARKER',
    'DNC_TRACE_VARIABLE_ID_CSI2', 'DNC32_E_NOT_PROT',
    'DNC_DATAENTRY_PROPKIND', 'DNC_TRIG_SEQUENCE',
    'DNC_INTERFACE_JHTEST', 'DNC_STATE_MACHINE_IS_BOOTED',
    'DNC_DATAENTRY_PROPKIND_LOWER_BOUND', 'IJHSoftwareVersion',
    'DNC_SW_TYPE_MP_UIMS', 'JHRemoteError', 'JHErrorEvents',
    'JHErrorEntryList', 'DNC_E_FILE_OPEN_FAILED'
]

_check_version('1.4.8', 1723030128.000000)

