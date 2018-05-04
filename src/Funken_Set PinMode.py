#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Description + license here
-
Provided by Funken 0.1
    Args:
        PIN: Description...
        MODE: Description...
        SET: Description...
        PORT: Description...
    Returns:
        log: Description...
"""

ghenv.Component.Name = "Funken_Set PinMode"
ghenv.Component.NickName = 'PinMode'
ghenv.Component.Message = 'VER 0.2.0'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "3"
except: pass

import scriptcontext as sc
import time


if SET:
    
    if PORT is None:
        PORT = sc.sticky['main_listener'].com_ports[0]
    
    if ID is None:
        ID = 1
    
    comm = "PM " + str(PIN) + " " + str(MODE) + "\n"
    sc.sticky['main_listener'].send_command(comm, PORT, ID)
    if MODE == 0:
        comm_act = "DW " + str(PIN) + " 1\n"
        sc.sticky['main_listener'].send_command(comm, PORT, ID)