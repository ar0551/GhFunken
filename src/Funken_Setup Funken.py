#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Description + license here
-
Provided by Funken 0.1
    Args:
        RUN: run me!!!
    Returns:
        log: log
"""

ghenv.Component.Name = "Funken_Setup Funken"
ghenv.Component.NickName = 'SetupFnk'
ghenv.Component.Message = 'VER 0.2.1'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass



import serial
import scriptcontext as sc
import time


def handle_funken_response(txt):
    
    if txt[0] != "<":
        return None
    
    for char in "<>\rn":
       txt = txt.replace(char, "")
    
    parsed = txt.split(":")
    
    device_id = int(parsed[1])
    comm_token = str(parsed[2])
    try:
        comm_val = str(parsed[3].strip("\n"))
    except:
        comm_val = None
    
    return device_id, comm_token, comm_val


## generic device connected to a serial port
class Device(object):
    
    def __init__(self, id):
        self.id = id
        self.tokens = {}
    
    def register_tokens(self, txt):
        
        parsed_tokens = txt.split(" ")
        
        for tok in parsed_tokens:
            if tok not in self.tokens:
                self.tokens[tok] = None

class SerialConnection(object):
    
    def __init__(self, port, baudrate):
        self.port = port
        self.ser = serial.Serial(port, baudrate)  # open serial port
        
        self.devices = {}
        self.devices_ids = []
    
    def register_devices(self):
        self.ser.write(b"GETID\n")
        time.sleep(0.1)
        while self.ser.in_waiting:
            response = self.ser.readline()
            parsed_response = handle_funken_response(response)
            if parsed_response is not None:
                if parsed_response[1] == "GETID":
                    if parsed_response[0] not in self.devices:
                        self.devices[parsed_response[0]] = Device(parsed_response[0])
                        self.devices_ids.append(parsed_response[0])
        
        time.sleep(0.1)
        for key in self.devices:
            self.ser.write(b"CLIST\n")
            time.sleep(0.1)
            while self.ser.in_waiting:
                response = self.ser.readline()
                parsed_response = handle_funken_response(response)
                if parsed_response is not None:
                    if parsed_response[1] == "CLIST":
                        if parsed_response[0] in self.devices:
                            self.devices[parsed_response[0]].register_tokens(parsed_response[2])


class Listener(object):
    
    def __init__(self, com_ports, baudrates = [230400]):
        self.com_ports = com_ports
        
        self.ser_conn = {}
        
        for i in xrange(len(self.com_ports)):
            #set baudrate
            baud = None
            if len(baudrates) == 1:
                baud = baudrates[0]
            else:
                baud = baudrates[i]
            #create serial connection
            self.ser_conn[self.com_ports[i]] = SerialConnection(self.com_ports[i], baud)
       
    def add_serial_connection(self, port, baudrate = 230400):
       if port in self.com_ports:
           self.ser_conn[port].ser.close()
       self.ser_conn[port] = SerialConnection(port, baudrate)
       self.com_ports.append(port)
    
    def send_command(self, comm_txt, port, id):
        self.ser_conn[port].ser.write(comm_txt)
        time.sleep(0.005)
    
    def get_response(self, comm_txt, token, port, id):
        self.ser_conn[port].ser.write(comm_txt)
        time.sleep(0.005)
        while self.ser_conn[port].ser.in_waiting:
            response = self.ser_conn[port].ser.readline()
            parsed_response = handle_funken_response(response)
            if parsed_response is not None:
                if parsed_response[1] == token:
                    return parsed_response[2]
        return None

log = []

if RUN:
    sc.sticky['Listener'] = Listener
    sc.sticky['SerialConnection'] = SerialConnection
    sc.sticky['Device'] = Device
    
    sc.sticky['main_listener'] = Listener([])
    log.append("ready to go...")
