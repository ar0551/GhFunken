#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Scan for available serial ports.
-
Provided by Funken 0.3.0
    Args:
        SCAN: True to scan for available serial ports.
    Returns:
        PORTS: Available serial ports.
"""

ghenv.Component.Name = "Funken_Scan Serial Ports"
ghenv.Component.NickName = 'ScanPorts'
ghenv.Component.Message = 'VER 0.3.2'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass

import platform
import Grasshopper as gh


## https://eli.thegreenplace.net/2009/07/31/listing-all-serial-ports-on-windows-with-python/
def enumerate_serial_ports_win():
    """ Uses the Win32 registry to return an
        iterator of serial (COM) ports
        existing on this computer.
    """
    
    import _winreg as winreg
    import itertools
    
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

## missing reference link 
## !!! NOT TESTED !!!
def enumerate_serial_ports_mac():
    import glob
    ports = glob.glob("/dev/tty.*")
    return ports


if SCAN:
    os_name = platform.system()
    
    if os_name == "Windows":
        PORTS = enumerate_serial_ports_win()
    elif os_name == "Darwin":
        PORTS = enumerate_serial_ports_mac()
    else:
        msg = "Your operative system is currently not supported by Funken.\n You might try to write the name of the serial port manually to the OpenPort component."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)

