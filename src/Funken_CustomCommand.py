#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Send custom Funken commands.
-
Provided by Funken 0.3.0
    Args:
        TOKEN: Command identification token.
        VAL: Command parameters.
        RES: True if the command is expecting a response.
        SEND: True to send the command.
        PORT: Serial port to send the message [Default is the first port available].
        ID: ID of the device [Default is the first device available].
    Returns:
        OUT: Parsed command output (as list).
        OUT_RAW: Raw command output (as string).
        _COMM: Funken command.
        _PORT: Serial port where the message was sent (for daisy-chaining). 
        _ID: Device ID (for daisy-chaining). 
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
    
    response = None
    comm = token
    for v in values:
        comm = comm + " " + str(v)
    comm = comm + "\n"
    if send_data:
        if return_data:
            response = sc.sticky['pyFunken'].get_response(comm, token, port, id)
        else:
            sc.sticky['pyFunken'].send_command(comm, port, id)
    
    return response, comm, port, id


result = main(TOKEN, VAL, RES, SEND, PORT, ID)

if result is not None:
    OUT_RAW = result[0]
    OUT = result[0].split(" ")
    _COMM = result[1]
    _PORT = result[2]
    _ID = result[3]