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
ghenv.Component.Message = 'VER 0.2.1'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass

import scriptcontext as sc
import serial
import time


if OPEN:
    for i in xrange(len(PORT)):
        if len(BAUD) == 0:
            sc.sticky['main_listener'].add_serial_connection(PORT[i])
        elif len(BAUD) == 1:
            sc.sticky['main_listener'].add_serial_connection(PORT[i], BAUD[0])
        elif len(BAUD) == len(PORT):
            sc.sticky['main_listener'].add_serial_connection(PORT[i], BAUD[i])
        else:
            print "wrong number of comports and baudrates"
    
    ## try communication
if REG:
    if 'main_listener' in sc.sticky:
        for conn in sc.sticky['main_listener'].ser_conn:
            sc.sticky['main_listener'].ser_conn[conn].register_devices()
            print sc.sticky['main_listener'].ser_conn[conn].port, sc.sticky['main_listener'].ser_conn[conn].devices
            for device in sc.sticky['main_listener'].ser_conn[conn].devices:
                print sc.sticky['main_listener'].ser_conn[conn].devices[device].tokens
     

"""
else:
    ## reset all connection
    pass
"""