#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Simple counter
-
Provided by Funken 0.3
    Args:
        ADD: True to add a step to the counter
        STEP: step size
        RESET: True to reset the counter to 0
    Returns:
        C: Current counter value
"""

ghenv.Component.Name = "Funken_Counter"
ghenv.Component.NickName = 'Count'
ghenv.Component.Message = 'VER 0.3.2'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "3 | Utilities"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass

import scriptcontext as sc
import Grasshopper as gh

check_data = True

if ADD is None:
    ADD = False

if STEP is None:
    STEP = 1

if RESET is None:
    RESET = False

if check_data:
    
    if 'counter' not in globals() or RESET:
        counter = 0
    
    if ADD:
        counter += STEP
    
    C = counter