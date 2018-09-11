#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Description + license here
-
Provided by Funken 0.1
    Args:
        OPEN: Description...
        PORT: Description...
        LISTEN: Description...
    Returns:
        log: Description...
"""

ghenv.Component.Name = "Funken_Open Serial Port"
ghenv.Component.NickName = 'OpenPort'
ghenv.Component.Message = 'VER 0.3.0'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
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


def main(port, baud, open, register):
    
    check_data = True
    
    if len(port) == 0:
        check_data = False
        msg = "No serial port provided."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)
    
    if len(baud) == 0:
        baud = [57600]
        msg = "Baudrate set to Funken default: 57600"
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    elif len(baud) > 1 and len(baud) != len(port):
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
            for i in xrange(len(port)):
                if len(baud) == 1:
                    sc.sticky['pyFunken'].add_serial_connection(PORT[i], BAUD[0])
                else:
                    sc.sticky['pyFunken'].add_serial_connection(port[i], baud[i])
        
        if register:
            for conn in sc.sticky['pyFunken'].ser_conn:
                sc.sticky['pyFunken'].ser_conn[conn].register_devices()
                print sc.sticky['pyFunken'].ser_conn[conn].port, sc.sticky['pyFunken'].ser_conn[conn].devices
                for device in sc.sticky['pyFunken'].ser_conn[conn].devices:
                    print sc.sticky['pyFunken'].ser_conn[conn].devices[device].tokens

main(PORT, BAUD, OPEN, REG)