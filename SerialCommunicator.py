import serial
import time

lenght = {'s': 3,
			'u': 0,
			'd': 0 }

def get_connection(port):
	ser = serial.Serial(port, timeout=1) 
	return ser 

def send(ser, message, mes_len):
	ser.write(message)
	time.sleep(0.1)
	if mes_len != 0:
		data = ser.read(mes_len)	
		result = data.decode()
		result = result.strip() # удаление невид симв 
		print(result)

if __name__ == '__main__':
	ser = get_connection("COM8")
	while True:
		inp = input('enter command:')
		lenght = lenght.get(inp, 17)
		send(ser, inp.encode(), lenght)