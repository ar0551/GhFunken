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

ghenv.Component.Name = "Funken_CustomCommand"
ghenv.Component.NickName = 'CustomComm'
ghenv.Component.Message = 'VER 0.3.0'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

import scriptcontext as sc
import Grasshopper as gh
import time

def main(token, values, return_data, send_data, port, id):
    
    if sc.sticky.has_key("pyFunken") == False:
        check_data = False
        msg = "No serial object available. Have you opened the serial port?"
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)
        return
    
    if return_data is None:
        return_data = False
    
    if send_data is None:
        send_data = False
    
    if port is None:
        port = sc.sticky["pyFunken"].com_ports[0]
        msg = "No port provided. Port set to " + port
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    if id is None:
        id = sc.sticky['pyFunken'].ser_conn[port].devices_ids[0]
        msg = "No id provided. Id set to " + str(id)
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    response = None
    if send_data:
        
        comm = token
        for v in values:
            comm = comm + " " + str(v)
        comm = comm + "\n"
        
        if return_data:
            response = sc.sticky['pyFunken'].get_response(comm, token, port, id)
        else:
            sc.sticky['pyFunken'].send_command(comm, port, id)
    
    return response, port, id


result = main(TOKEN, VAL, RES, SEND, PORT, ID)

if result is not None:
    OUT_RAW = result[0]
    OUT = result[0].split(" ")
    _PORT = result[1]
    _ID = result[2]