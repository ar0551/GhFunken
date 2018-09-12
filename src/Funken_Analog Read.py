#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Description + license here
-
Provided by Funken 0.1
    Args:
        PIN: Description...
        VAL: Description...
        PORT: Description...
    Returns:
        VAL_OUT: Description...
"""

ghenv.Component.Name = "Funken_Analog Read"
ghenv.Component.NickName = 'AnalogRead'
ghenv.Component.Message = 'VER 0.3.0'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

import scriptcontext as sc
import Grasshopper as gh
import time

def main(pin, get, port, id):
    
    if sc.sticky.has_key("pyFunken") == False:
        check_data = False
        msg = "No serial object available. Have you opened the serial port?"
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)
        return
    
    if pin is None:
        check_data = False
        msg = "No pin provided."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
        return
    
    if get is None:
        get = False
    
    if port is None:
        if len(sc.sticky["pyFunken"].com_ports) == 0:
            msg = "No serial connection available. Did you connect open the serial port?"
            ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
            return
        else:
            port = sc.sticky["pyFunken"].com_ports[0]
    
    if id is None:
        if len(sc.sticky['pyFunken'].ser_conn[port].devices_ids) == 0:
            msg = "No device available. Did you connect an Arduino-compatible device and registered it?"
            ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
            return
        else:
            id = sc.sticky['pyFunken'].ser_conn[port].devices_ids[0]
    
    value = None
    if get:
        comm = "AR " + str(pin) + "\n"
        response = sc.sticky['pyFunken'].get_response(comm, "AR", port, id)
        try:
            value = int(response.split(" ")[1])
        except:
            value = -1
        
    return value, port, id

result = main(PIN, GET, PORT, ID)

if result is not None:
    VAL = result[0]
    _PORT = result[1]
    _ID = result[2]
