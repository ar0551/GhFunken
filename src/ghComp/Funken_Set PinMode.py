#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Set pin mode (mirrors the Arduino pinMode method).
-
Provided by Funken 0.3
    Args:
        PIN: The number of the pin whose mode you wish to set.
        MODE: 0 for Input pins, 1 for Output pins.
        SET: True to set the pin.
        PORT: Serial port to send the message [Default is the first port available].
        ID: ID of the device [Default is the first device available].
    Returns:
        _COMM: Funken command.
        _PORT: Serial port where the message was sent (for daisy-chaining). 
        _ID: Device ID (for daisy-chaining). 
"""

ghenv.Component.Name = "Funken_Set PinMode"
ghenv.Component.NickName = 'PinMode'
ghenv.Component.Message = 'VER 0.3.3'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "1 | Arduino"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass

import scriptcontext as sc
import Grasshopper as gh

def main(pin, mode, set, port, id):
    
    check_data = True
    
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
    
    if mode is None:
        check_data = False
        msg = "No mode provided."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
        return
    
    if set is None:
        set = False
    
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
    
    if check_data:
        comm = "PM " + str(pin) + " " + str(mode) + "\n"
        if set:
            sc.sticky['pyFunken'].send_command(comm, port, id)
        
        return comm, port, id

result = main(PIN, MODE, SET, PORT, ID)

if result is not None:
    _COMM = result[0]
    _PORT = result[1]
    _ID = result[2]
