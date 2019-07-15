#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Read a digital input pin (mirrors the Arduino digitalRead method).
-
Provided by Funken 0.3
    Args:
        PIN: The number of the pin from which to read.
        GET: True to read data.
        PORT: Serial port to send the message [Default is the first port available].
        ID: ID of the device [Default is the first device available].
    Returns:
        VAL: Read value.
        _COMM: Funken command.
        _PORT: Serial port where the message was sent (for daisy-chaining). 
        _ID: Device ID (for daisy-chaining). 
"""

ghenv.Component.Name = "Funken_Digital Read"
ghenv.Component.NickName = 'DigitalRead'
ghenv.Component.Message = 'VER 0.3.3'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "1 | Arduino"
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass

import scriptcontext as sc
import Grasshopper as gh
import time

def main(pin, get, port, id):
    
    if sc.sticky.has_key("pyFunken") == False:
        check_data = False
        msg = "No serial object available. Have you opened the serial port?"
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
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
    comm = "DR " + str(pin) + "\n"
    if get:
        response = sc.sticky['pyFunken'].get_response(comm, "DR", port, id)
        try:
            value = int(response.split(" ")[1])
        except:
            value = -1
        
    return value, comm, port, id

result = main(PIN, GET, PORT, ID)

if result is not None:
    VAL = result[0]
    _COMM = result[1]
    _PORT = result[2]
    _ID = result[3]
