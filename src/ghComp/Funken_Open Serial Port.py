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
        REG: Register devices to access available Funken commands. Sometimes the connection takes some time to be established, so you might need to press this button 2-3 times.
    Returns:
        LOG: Information about connected devices.
"""

ghenv.Component.Name = "Funken_Open Serial Port"
ghenv.Component.NickName = 'OpenPort'
ghenv.Component.Message = 'VER 0.3.3'
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


def main(ports, bauds, open, register, log):
    
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
        
        if sc.sticky.has_key("pyFunken") == False:
            sc.sticky['pyFunken'] = funken.PyFunken([],[])
        
        if open:
            log = ""
            for i in xrange(len(ports)):
                if ports[i] is not None:
                    baud = None
                    if len(bauds) == 1:
                        baud = bauds[0]
                    else:
                        baud = bauds[i]
                    try:
                        sc.sticky['pyFunken'].add_serial_connection(ports[i], baud)
                        log = log + str(ports[i]) + ":\n" + "No Funken device registered\n"
                        log = log + "---\n"
                    except:
                        log = log + str(ports[i]) + ":\n" + "Could not open the serial port\n"
                        log = log + "---\n"
        
        if register:
            log = ""
            for port in ports:
                try:
                    sc.sticky['pyFunken'].ser_conn[port].register_devices()
                    log = log + str(sc.sticky['pyFunken'].ser_conn[port].port) + ":\n"
                    if len(sc.sticky['pyFunken'].ser_conn[port].devices) > 0:
                        for device in sc.sticky['pyFunken'].ser_conn[port].devices:
                            log = log + str(device) + ":" + str(sc.sticky['pyFunken'].ser_conn[port].devices[device].tokens.keys()) + "\n"
                    else:
                        log = log + "No Funken device available\n"
                
                except:
                    log = log + str(port) + ":\n" + "Could not open the serial port\n"
                    
                log = log + "---\n"
    
    ## test if available serial ports are still active
    if sc.sticky.has_key("pyFunken"):
        
        ## remove port names if no longer in use
        for port in sc.sticky['pyFunken'].com_ports:
            if sc.sticky['pyFunken'].ser_conn.has_key(port) == False:
                sc.sticky['pyFunken'].com_ports =  filter(lambda a: a != port, sc.sticky['pyFunken'].com_ports)
        
        ## remove serial connections if no longer available
        removed_keys = []
        for port in sc.sticky['pyFunken'].ser_conn:
            for device in sc.sticky['pyFunken'].ser_conn[port].devices:
                try:
                    sc.sticky['pyFunken'].send_command("TEST", port, device)
                except:
                    removed_keys.append(port)
                    if port in sc.sticky['pyFunken'].com_ports:
                        sc.sticky['pyFunken'].com_ports.remove(port) 
                    break
        for key in removed_keys:
            sc.sticky['pyFunken'].ser_conn.pop(key)
    
    return log


if 'logger' not in globals():
    logger = ""

logger = main(PORT, BAUD, OPEN, REG, logger)
LOG = logger