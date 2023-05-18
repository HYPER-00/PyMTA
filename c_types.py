"""PyMTA C-Types (included from ctypes library)"""

from ctypes import (
    c_int  as int,
    c_uint as uint,
    c_int8 as int8,
    c_uint8 as uint8,
    c_int16 as int16,
    c_uint16 as uint16,
    c_int32 as int32,
    c_uint32 as uint32,
    c_int64 as int64,
    c_uint64 as uint64,
    c_short as short,
    c_ushort as ushort,
    c_long as long,
    c_ulong as ulong,
    c_longlong as longlong,
    c_ulonglong as ulonglong,
    c_double as double,
    c_size_t as size_t,
    c_ssize_t as ssize_t,
    c_bool as bool,
    c_byte as byte,
    c_ubyte as ubyte,
    c_char as char,
    c_char_p as charptr,
    c_wchar as wchar,
    c_wchar_p as wcharptr,
    c_float as float,
    c_longdouble as longdouble,
    c_void_p as voidptr,
    pointer as ptr,
    sizeof as sizeof,
    wintypes
)