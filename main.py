import socket
import json

def varint(number):
    if number < 128:
        return bytes([number])
    else:
        bytes1=number % 128 + 128
        bytes2=number // 128
        return bytes([bytes1, bytes2])

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.bind(("0.0.0.0", 25565))
while True:
 ss.listen(5)
 
 conection, direction = ss.accept()
 datos = conection.recv(1024)
 print(datos)
 
 datos2 = conection.recv(1024)
 print(datos2)
 
 jeison={
     "version": {
         "name": "26.3",
         "protocol": 777
     },
     "players": {
         "max": 20,
         "online": 0,
         "sample": [
         ]
     },
     "description": {
         "text": "Hello, world!"
     },
     "favicon": "data:image/png;base64,<data>",
     "enforcesSecureChat": False
 }
 
 text = json.dumps(jeison).encode("utf8")
 print(text)
 
 textwithleng = varint(len(text)) +text
 pack = b"\x00" + textwithleng
 response = varint(len(pack)) + pack

 conection.send(response)
 datos3 = conection.recv(1024)
 print(datos3)
 conection.send(datos3)
 conection.close()
