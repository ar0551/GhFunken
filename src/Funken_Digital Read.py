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

ghenv.Component.Name = "Funken_Digital Read"
ghenv.Component.NickName = 'DigitalRead'
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
        port = sc.sticky["pyFunken"].com_ports[0]
        msg = "No port provided. Port set to " + port
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    if id is None:
        id = sc.sticky['pyFunken'].ser_conn[port].devices_ids[0]
        msg = "No id provided. Id set to " + str(id)
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    value = None
    if get:
        comm = "DR " + str(pin) + "\n"
        response = sc.sticky['pyFunken'].get_response(comm, "DR", port, id)
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
