#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Checks for an input switching state.
-
Provided by Funken 0.3.0
    Args:
        VAL: Value to monitor
    Returns:
        TF: True when the value has switched from True to False
        FT: True when the value has switched from False to True
"""

ghenv.Component.Name = "Funken_State Change"
ghenv.Component.NickName = 'StateCh'
ghenv.Component.Message = 'VER 0.3.1'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "3 | Utilities"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass

import scriptcontext as sc
import Grasshopper as gh

check_data = True

if VAL is None:
    check_data = False
    msg = "No value provided"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
    
if check_data:
        
    if 'prev_value' not in globals():
        prev_value = False
    
    if VAL == True and prev_value != True:
        tf = True
        ft = False
    elif VAL == False and prev_value != False:
        ft = True
        tf = False
    else:
        tf = False
        ft = False
    
    prev_value = VAL
    
    TF = tf
    FT = ft