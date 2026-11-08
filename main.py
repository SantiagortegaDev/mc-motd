import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(("0.0.0.0", 25565))

serversocket.listen(5)

conexion, direccion = serversocket.accept()
datos = conexion.recv(1024)
print(datos)

datos2 = conexion.recv(1024)
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
    "enforcesSecureChat": false
}
