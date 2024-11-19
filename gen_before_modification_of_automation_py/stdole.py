from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    EXCEPINFO, OLE_YPOS_HIMETRIC, OLE_XSIZE_HIMETRIC, Default,
    OLE_HANDLE, FONTBOLD, StdPicture, GUID, FONTNAME,
    OLE_YSIZE_CONTAINER, DISPMETHOD, FontEvents, IFontEventsDisp,
    OLE_YSIZE_PIXELS, OLE_XPOS_HIMETRIC, OLE_XSIZE_PIXELS, Font,
    OLE_CANCELBOOL, Unchecked, OLE_YSIZE_HIMETRIC, VARIANT_BOOL,
    IFontDisp, Library, FONTITALIC, StdFont, dispid, OLE_XPOS_PIXELS,
    OLE_YPOS_PIXELS, FONTSTRIKETHROUGH, IUnknown, BSTR,
    OLE_XPOS_CONTAINER, OLE_COLOR, Picture, OLE_YPOS_CONTAINER, _lcid,
    Checked, IPicture, DISPPROPERTY, COMMETHOD, Gray, IFont,
    IPictureDisp, _check_version, Color, DISPPARAMS, VgaColor,
    OLE_XSIZE_CONTAINER, FONTUNDERSCORE, IDispatch, IEnumVARIANT,
    OLE_OPTEXCLUSIVE, Monochrome, CoClass, OLE_ENABLEDEFAULTBOOL,
    typelib_path, HRESULT, FONTSIZE
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'LoadPictureConstants', 'IFontDisp', 'Library', 'FONTITALIC',
    'OLE_YPOS_HIMETRIC', 'OLE_XSIZE_HIMETRIC', 'Default', 'StdFont',
    'OLE_HANDLE', 'FONTBOLD', 'OLE_XPOS_PIXELS', 'StdPicture',
    'OLE_YPOS_PIXELS', 'FONTSTRIKETHROUGH', 'OLE_XPOS_CONTAINER',
    'OLE_COLOR', 'FONTNAME', 'OLE_YPOS_CONTAINER', 'Picture',
    'Checked', 'IPicture', 'Gray', 'IFont', 'IPictureDisp',
    'OLE_YSIZE_CONTAINER', 'OLE_TRISTATE', 'Color', 'FontEvents',
    'IFontEventsDisp', 'VgaColor', 'OLE_YSIZE_PIXELS',
    'FONTUNDERSCORE', 'OLE_XSIZE_CONTAINER', 'OLE_XPOS_HIMETRIC',
    'OLE_XSIZE_PIXELS', 'OLE_OPTEXCLUSIVE', 'Font', 'OLE_CANCELBOOL',
    'Unchecked', 'Monochrome', 'OLE_ENABLEDEFAULTBOOL',
    'typelib_path', 'FONTSIZE', 'OLE_YSIZE_HIMETRIC'
]

