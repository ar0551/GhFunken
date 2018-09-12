#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Write a digital value on a pin (mirrors the Arduino digitalWrite method).
-
Provided by Funken 0.3.0
    Args:
        PIN: The number of the pin where to write.
        VAL: The value to write. It can be either 0 (LOW) or 1 (HIGH).
        PORT: Serial port to send the message [Default is the first port available].
        ID: ID of the device [Default is the first device available].
    Returns:
        _COMM: Funken command.
        _PORT: Serial port where the message was sent (for daisy-chaining). 
        _ID: Device ID (for daisy-chaining). 
"""

ghenv.Component.Name = "Funken_Digital Write"
ghenv.Component.NickName = 'DigitalWrite'
ghenv.Component.Message = 'VER 0.3.0'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

import scriptcontext as sc
import Grasshopper as gh
import time

def main(pin, value, port, id):
    
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
    
    if value is None:
        value = 0
    
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
    
    comm = "DW " + str(PIN) + " " + str(value) + "\n"
    sc.sticky['pyFunken'].send_command(comm, port, id)
    return comm, port, id

result = main(PIN, VAL, PORT, ID)

if result is not None:
    _COMM = result[0]
    _PORT = result[1]
    _ID = result[2]
