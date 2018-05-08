#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Description + license here
-
Provided by Funken 0.1
    Args:
        SCAN: Description...
    Returns:
        PORTS: Description...
"""

ghenv.Component.Name = "Funken_Scan Serial Ports"
ghenv.Component.NickName = 'ScanPorts'
ghenv.Component.Message = 'VER 0.2.1'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass


import scriptcontext as sc
import _winreg as winreg
import itertools


## https://eli.thegreenplace.net/2009/07/31/listing-all-serial-ports-on-windows-with-python/
def enumerate_serial_ports():
    """ Uses the Win32 registry to return an
        iterator of serial (COM) ports
        existing on this computer.
    """
    path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
    except WindowsError:
        return
        #raise IterationError
    ports = []
    for i in itertools.count():
        try:
            val = winreg.EnumValue(key, i)
            port_name = str(val[1])
            if port_name not in ports:
                ports.append(port_name)
        except EnvironmentError:
            break
    return ports

if SCAN:
    PORTS = enumerate_serial_ports()
