"""Windows DPAPI protected, per-user PS5 connection settings."""
import os
import json
import ctypes
from ctypes import wintypes
from pathlib import Path

def config_path():
    base=os.environ.get('LOCALAPPDATA')
    if not base or os.name!='nt':
        return None
    return Path(base)/'Y2JBThemeCreator'/'connection.dat'

class DATA_BLOB(ctypes.Structure):
    _fields_=[('cbData',wintypes.DWORD),('pbData',ctypes.POINTER(ctypes.c_byte))]

def _blob(data):
    buf=ctypes.create_string_buffer(data)
    return DATA_BLOB(len(data),ctypes.cast(buf,ctypes.POINTER(ctypes.c_byte))),buf

def _crypt(data, decrypt=False):
    if os.name!='nt': raise OSError('Windows DPAPI required')
    crypt32=ctypes.WinDLL('crypt32',use_last_error=True)
    kernel32=ctypes.WinDLL('kernel32',use_last_error=True)
    src,buf=_blob(data)
    out=DATA_BLOB()
    fn=crypt32.CryptUnprotectData if decrypt else crypt32.CryptProtectData
    fn.restype=wintypes.BOOL
    if decrypt:
        ok=fn(ctypes.byref(src),None,None,None,None,0,ctypes.byref(out))
    else:
        ok=fn(ctypes.byref(src),'Y2JB Theme Creator',None,None,None,0,ctypes.byref(out))
    if not ok: raise ctypes.WinError(ctypes.get_last_error())
    try: return ctypes.string_at(out.pbData,out.cbData)
    finally: kernel32.LocalFree(ctypes.cast(out.pbData,ctypes.c_void_p))

def load_connection():
    path=config_path()
    if not path or not path.is_file(): return {}
    try:
        data=json.loads(_crypt(path.read_bytes(),True).decode('utf-8'))
        return data if isinstance(data,dict) else {}
    except (OSError,ValueError,UnicodeError):
        return {}

def save_connection(host,port):
    import ipaddress
    host=str(ipaddress.ip_address(host.strip()))
    port=int(port)
    if not 1<=port<=65535: raise ValueError('Invalid port')
    path=config_path()
    if path is None: return
    path.parent.mkdir(parents=True,exist_ok=True)
    encrypted=_crypt(json.dumps({'host':host,'port':port}).encode('utf-8'))
    temp=path.with_suffix('.tmp')
    try:
        temp.write_bytes(encrypted)
        os.replace(temp,path)
    finally:
        if temp.exists(): temp.unlink()
