# Obtener modelo PLC
from cpppo.server.enip.get_attribute import proxy_simple
host = "192.168.1.2"
x = proxy_simple(host).read([('@1/1/7','SSTRING')])
for i in x:
    print (i)

from cpppo.server.enip.get_attribute import proxy_simple
host = "192.168.1.2"
x, = proxy_simple(host).read("OFF")
print(x)

import sys
import time
from cpppo.server.enip.get_attribute import proxy_simple

product_name, = proxy_simple("192.168.1.2").read([('@1/1/7', 'SSTRING')])
print(product_name)


data2, = proxy_simple("192.168.1.2").read([('@196/0/100', 'INT')])
var2 = data2
if var2 == [4]:
    print('CPU in execution mode')
elif var2 == [2]:
    print('CPU in monitoring mode')
elif var2 == [1]:
    print('CPU in stop mode')
else:
    pass


via = proxy_simple('192.168.1.2')
with via:
    result, = via.read([('@0x7F/1/1=(SINT)1','@0x7F/1/1')],1)
    print(result)

import sys
import time
from cpppo.server.enip.get_attribute import proxy_simple

for j in range(1,200):
    for i in range(1, 200):
        try:
            product_name = proxy_simple("192.168.1.2").read([('@{}/{}'.format(j,i), 'INT')])

        except:
            product_name = proxy_simple("192.168.1.2").read([('@{}/{}'.format(j,i), 'SSTRING')])

for j in range(1,200):
    for i in range(1,200):
        print('1:', j, ' 2:', i, '  ', product_name)

# FINS
import fins.udp
import time

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.1.2', 9600)
fins_instance.dest_node_add = 1
fins_instance.srce_node_add = 195

x = int(input('Number of times: '))
#print(fins_instance.cpu_unit_status_read())

for i in range(x):
    fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD, b'\x00\x64\x00', b'\x00\xff', 1)
    mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD, b'\x00\x64\x00')
    print(mem_area)


import time
import fins.udp

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.1.2')
fins_instance.dest_node_add=14
fins_instance.srce_node_add=249

for i in range(1):
    mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().,b'\x00\x64\x00')
    #mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x64\x00')
    time.sleep(1)
    mem_area = int.from_bytes(mem_area,'big')
    mem_area = bin(mem_area)
    print(mem_area)

import time
import fins.udp
fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.1.2')
fins_instance.dest_node_add=14  #30
fins_instance.srce_node_add=249  #238
mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().DATA_MEMORY_WORD,b'\x00\x64\x00')

# APHYT
from aphyt import omron

try:
    eip_instance = omron.n_series.NSeriesEIP()
    eip_instance.connect_explicit('192.168.1.2')
    eip_instance.register_session()
    eip_instance.update_variable_dictionary()
    print('Conexión exitosa')

except:
    print('Error: ')
    
a = eip_instance.read_variable('ON')
#print("PRUEBA: " + a)
#reply = eip_instance.write_variable('PRUEBA', True)
#reply = eip_instance.read_variable('TestBoolFalse')
#print("TestBoolFalse: " + str(reply))
#reply = eip_instance.write_variable('TestBoolFalse', False)
#reply = eip_instance.read_variable('TestBoolFalse')
#print("TestBoolFalse: " + str(reply))

#eip_instance.close_explicit()

# EASY MODBUS
import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient('192.168.1.2', 9600)
modbus_client.connect()

#The first argument is the starting address, the second argument is the quantity.
coils = modbus_client.read_coils(0, 110)                          #Read coils 1 and 2 from server 
print(coils)
#discrete_inputs = modbus_client.read_discreteinputs(10, 10)     #Read discrete inputs 11 to 20 from server 
#print(discrete_inputs)
#input_registers = modbus_client.read_inputregisters(0, 5)      #Read input registers 1 to 10 from server 
#print(input_registers)
#holding_registers = modbus_client.read_holdingregisters(0, 5)   #Read holding registers 1 to 5 from server 
#print(holding_registers)
modbus_client.close()

import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient('192.168.1.2', 9600)
modbus_client.connect()

#The first argument is the starting registers, the second argument is the quantity.
register_values = modbus_client.read_holdingregisters(0, 5)
print("Value of Register 1: " + str(register_values[0]))
print("Value of Register 2: " + str(register_values[1])) 
print("Value of Register 3: " + str(register_values[2]))
print("Value of Register 4: " + str(register_values[3])) 
print("Value of Register 5: " + str(register_values[4]))

# ESCRIBIR REGISTROS
a = 115
modbus_client.write_single_register(0, a)   # Write value "115" to Holding Register 1

import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient('192.168.1.2', 9600)
modbus_client.connect()

#The first argument is the starting registers, the second argument is the quantity.
register_values = modbus_client.read_holdingregisters(0, 5)
print("Value of Register #1:" + str(register_values[0]))
print("Value of Register #2:" + str(register_values[1])) 
print("Value of Register #3:" + str(register_values[2]))
print("Value of Register #4:" + str(register_values[3])) 
print("Value of Register #5:" + str(register_values[4]))

# ESCRIBIR REGISTROS
modbus_client.write_holdingregisters(0, 5)   # Write value "115" to Holding Register 1 

# LEER DATOS PLC
import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient("192.168.1.2", 9600)
modbus_client.connect()

#The first argument is the starting address, the second argument is the quantity.
coils = modbus_client.read_coils(2, 50)                    # Lee salidas digitales del PLC 
print(coils)
modbus_client.close()

# LEER DATOS PLC
import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient("192.168.1.2", 9600)
modbus_client.connect()

holding_registers = modbus_client.read_holdingregisters(1, 5)       # Lee registros de retención del PLC 
for i in holding_registers:
    print(i)
modbus_client.close()

# LEER DATOS PLC
import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient("192.168.1.2", 9600)
modbus_client.connect()

input_registers = modbus_client.read_inputregisters(1, 10)     # Lee registros digitales del PLC 
for i in input_registers:
    print(i)
modbus_client.close()

# LEER DATOS PLC
import easymodbus.modbusClient

#create an instance of a Modbus-TCP class (Server IP-Address and Port) and connect
modbus_client = easymodbus.modbusClient.ModbusClient("192.168.1.2", 9600)
modbus_client.connect()

discreteInputs = modbus_client.read_discreteinputs(2, 15)        # Lee entradas digitales del PLC 
print(discreteInputs)
modbus_client.close()

# ESCRIBIR DATOS PLC
import easymodbus.modbusClient
modbusclient = easymodbus.modbusClient.ModbusClient("192.168.1.2", 9600)
modbusclient.connect()

try:
    modbusclient.write_single_coil(5,True)
    print('Ok')
except:
    print('Nel')

modbusclient.close()