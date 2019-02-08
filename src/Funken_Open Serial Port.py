#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Open a serial port and register avaialble Funken devices.
-
Provided by Funken 0.3
    Args:
        
        PORT: Serial port to open.
        BAUD: Communication baudrate [Funken default: 57600].
        OPEN: True to open the port for communication.
        REG: Register devices to access available Funken commands.
    Returns:
        LOG: Information about connected devices.
"""

ghenv.Component.Name = "Funken_Open Serial Port"
ghenv.Component.NickName = 'OpenPort'
ghenv.Component.Message = 'VER 0.3.2'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass


import sys
import scriptcontext as sc
import Grasshopper as gh
import time

## add Funken install directory to system path
ghcompfolder = gh.Folders.DefaultAssemblyFolder
fnk_path = ghcompfolder + "GhFunken"
if fnk_path not in sys.path:
    sys.path.append(fnk_path)
try:
    import funken
except:
    msg = "Cannot import Funken. Is the funken.py module installed in " + fnk_path + "?"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)


def main(ports, bauds, open, register):
    
    check_data = True
    
    if len(ports) == 0:
        check_data = False
        msg = "No serial port provided."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
    
    if len(bauds) == 0:
        bauds = [57600]
    
    elif len(bauds) > 1 and len(bauds) != len(ports):
        check_data = False
        msg = "Wrong number of comports and baudrates."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)
    
    if open is None:
        open = False
    
    if register is None:
        register = False
    
    if check_data:
        
        if sc.sticky.has_key("log") == False:
            sc.sticky["log"] = ""
        
        if sc.sticky.has_key("pyFunken") == False:
            sc.sticky['pyFunken'] = funken.PyFunken([],[])
        
        if open:
            sc.sticky["log"] = ""
            for i in xrange(len(ports)):
                baud = None
                if len(bauds) == 1:
                    baud = bauds[0]
                else:
                    baud = bauds[i]
                try:
                    sc.sticky['pyFunken'].add_serial_connection(ports[i], baud)
                    sc.sticky["log"] = sc.sticky["log"] + str(ports[i]) + ":\n" + "No Funken device registered\n"
                    sc.sticky["log"] = sc.sticky["log"] + "---\n"
                except:
                    sc.sticky["log"] = sc.sticky["log"] + str(ports[i]) + ":\n" + "Could not open the serial port\n"
                    sc.sticky["log"] = sc.sticky["log"] + "---\n"
                
        
        if register:
            sc.sticky["log"] = ""
            for port in ports:
                try:
                    sc.sticky['pyFunken'].ser_conn[port].register_devices()
                    sc.sticky["log"] = sc.sticky["log"] + str(sc.sticky['pyFunken'].ser_conn[port].port) + ":\n"
                    if len(sc.sticky['pyFunken'].ser_conn[port].devices) > 0:
                        for device in sc.sticky['pyFunken'].ser_conn[port].devices:
                            sc.sticky["log"] = sc.sticky["log"] + str(device) + ":" + str(sc.sticky['pyFunken'].ser_conn[port].devices[device].tokens.keys()) + "\n"
                    else:
                        sc.sticky["log"] = sc.sticky["log"] + "No Funken device available\n"
                except:
                    sc.sticky["log"] = sc.sticky["log"] + str(port) + ":\n" + "Could not open the serial port\n"
                    
                sc.sticky["log"] = sc.sticky["log"] + "---\n"
    
    return sc.sticky["log"]

LOG = main(PORT, BAUD, OPEN, REG)