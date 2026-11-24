import socket
import json
import random
from datetime import datetime, date

def varint(number):
    if number < 128:
        return bytes([number])
    else:
        bytes1=number % 128 + 128
        bytes2=number // 128
        return bytes([bytes1, bytes2])

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(("0.0.0.0", 25565))
while True:
 ss.listen(5)
 
 conection, direction = ss.accept()
 datos = conection.recv(1024)
 print(datos)
 
 if len(datos) == datos[0] + 1:
  datos2 = conection.recv(1024)
  print(datos2)
 


 if datos[datos[0]] == 1:
  number=random.randint(1, 4)
  phantom={
      "version": {"name": "26.3", "protocol": 777},
      "players": {
          "max": 2,
          "online": 28,
          "sample": [
    {"name": "§cEnds Feb 28", "id": "00000000-0000-0000-0000-000000000001"}
]
      },
      "description": {
          "text": "§f{Phantom} §8Build creative projects for 50 hours, then fly to an escape room hackathon in Philadel..."
      },
      "favicon": "data:image/png;base64,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",
      "enforcesSecureChat": False
  }
  hackcraft={
        "version": {"name": "26.3", "protocol": 777},
        "players": {
            "max": 12,
            "online": 31,
            "sample": [
      {"name": "§cEnds Dec 31", "id": "00000000-0000-0000-0000-000000000001"}
  ]
        },
        "description": {
    "text": "",
    "extra": [
        {"text": "{Hack", "color": "dark_green"},
        {"text": "Craft} ", "color": "#986a44"},
        {"text": "Create a Minecraft mod, earn a free game and server hosting!", "color": "dark_gray"}
    ]
},
        "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDI2LTExLTIzVDE0OjIxOjE5KzAwOjAwpH4maAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNi0xMS0yM1QxNDoyMToxNSswMDowMDTLbcMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjYtMTEtMjNUMTQ6MjE6MTUrMDA6MDBFltV/AAAACXBIWXMAAAPYAAAD2AFuR2M1AAADAFBMVEUAAABQOSc4JxpLNSQzIxhHMyNZQCxALB4xIhdLNiUpJyk9Kx1JNCQ6KBxFMSE2JhpVPSpVPClXPipDLh9POCZROihkSDFgRS9XjDS7sa49LB6+tLECAQFTPClHMiJCLyBUOygEAwNONyZALR8pHBNcQi1DMCE9LR80JRlZPytoSzRXPyx3VjtSOygsHxU/LB5MNyZpTDQQDQvOwr9dQy66sK1ShDE8KhxuTzbLwL1ThzFPhC0HBgUMCQhzmk07Kh0gHx9rTTVRhi59WT5FOCFLPCUmJSZOgS1CLR4vIBZXizRFMCBMSUhNNiVBMCJiRzDPxMF2nFDAtbJdkzkmGhLVycbBtrPRxsNDNiBulEjCuLXHvLlxl0sgFw/ZzcpajzZkmEHJvrvQxcJojkG3rapajThFLx9VfTNYjjXFurdglT1VijJOTEuyqabUyMXEubYZGBhckDnWysdRT05HbSdQeS9pn0Z0UzmCXUBmSTOwpqNMdStWhzVIOiMzJhxBLyC5r6wjISI3NDO1q6hqkUN5n1JXijVDMSWupaJBPTyto6BJRkRjlkJIMSFHMCE2KR8qKSpxUTgWFRQSERFHeiUaEgxLfSpKcSlVUlIdHBmfl5QvLS1ohENkmkE4NjZgkj29s7BEdySXj41JRCVPS0dyj0ymnZtFQkE5ODlagjcyMDBSPS1fhz6QiIZ5cnBti0hDZSVORyheW1smIxKHYUNZhTU+OzpqZGNkiz88OTiAeXZlYF6Gf32HgH40UiB0bmxLPilFOiZxa2kpPhlaVlNcWFaDfHlvaWiEfXs7XSUrKBZcWVczJBlbkDhFMiI9Kx1DLyBDLyBDLyA+LB46Khw0JRk6KRw8Kx1XjTQ9LB5WjDI1JRpZPytckTpaiDdFMSFgkTxIMyNHNSNbkDlajzdglT1gkTxUPililT9BLyBolkNCMCE9LB47Kh01JRlYjjRMgSo+LB5cQS1cQS1MeSlnlkNhlj5Qhi02JhpJfidMNyYyIxlFeiM7Kh1DeCBHcEzsx81TAAABAHRSTlP///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8pCqXrPHUM3UL4ClXd9Oum9tKk9nXrtUL1pjzFVdLrKfy10sUpxevcVbUptd5C+SnSxaYApVAE3QAAAYxpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0n77u/JyBpZD0nVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkJz8+Cjx4OnhtcG1ldGEgeG1sbnM6eD0nYWRvYmU6bnM6bWV0YS8nIHg6eG1wdGs9J0ltYWdlOjpFeGlmVG9vbCAxMi45OCc+CjxyZGY6UkRGIHhtbG5zOnJkZj0naHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyc+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczpwZGY9J2h0dHA6Ly9ucy5hZG9iZS5jb20vcGRmLzEuMy8nPgogIDxwZGY6UHJvZHVjZXI+T25saW5lLUNvbnZlcnQ8L3BkZjpQcm9kdWNlcj4KIDwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSdyJz8+uaFLMAAACyxJREFUWMNklnlQk2cexx8ICQl5CTkh0ZwgWZIQDeEKIVFAAsFEgqjchyIBBETOxXAMKgoiyhTlkMOKoFC1ntu11qPaa89hu7udnXGd6rrr0U7/aafbdmd3drb7e56XuJ3uZyaT50me3+f9/p687wPo+xWWXz598eXDR8+9Umnd1vr6rdaMDGvl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",
        "enforcesSecureChat": False
    }
  jamegam={
          "version": {"name": "26.3", "protocol": 777},
          "players": {
              "max": 12,
              "online": 18,
              "sample": [
        {"name": "§cEnds Dec 18", "id": "00000000-0000-0000-0000-000000000001"}
    ]
          },
          "description": {
      "text": "§7{jame gam} §8a community of teenagers who enter game jams together. build a game, get prizes",
  },
          "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAE2ElEQVR4Xu2bTUhVQRTHz2xzUWF7000FRrWqiNYFlYpBUVBQVKsioyiSlhFmWkpBUJZQRNCHpRXUKsJFX4SFmLR57xn0ISXlI4s2TszzzeU4ztz5uJ++13/53r1z5/zuOWdmzswlUOYiZW5/PAAopT/CAE0ImR9GO1ihegCltF7RwfuK323VwG4ghPTa3qhS2ABoWB3zEyEktH4HaohSOgAAy02M3ly3weQyqXbt2Qsb6wov31NYEJwBUCp/20EMNdHdvkf4suWEkHcm94UaAtj4bCYDR5oOBOmDtQQIbwkhK6wbKcraA7Dxhw/uh1w26/rsQBIgOIeEFQBK6TkAaGI9v3r5EvQ/ewr5fD6QIa7asKke6hsbobJyAW+igxByyLY9WwBelo861k3U1nEeqmtqAiVGJwBBjZ9TUQHXb97ytdH0GQurq6G980KhLZeRITIAzEV3793nayTWjm1b4PfEhPcTj3EdiNQBEJMTEzbiaPMJWLlq9TTjVUbytli+efRAPvlLPQCZcWII6ABwya77DyBtOUDMzCYewOYTH0dGYHJy0nvb2LCxse+QH89LJ1ypA8CE84AJACZVEuRzjlTlADGxyYRHATEJ1tYuhZ3bt0rvw2IgUzUKMPGpsK5jcSj2iRAGwJTkWoAJA3CZBDFZTYS4kl4NinmmYIhjkcQVgLcoYhm6t6dHmaSikDDL/AYAN1wWQs4eIIaCSVIMU4nWA8QwCFoQOb1+ndfm0OgoXBt4q2WFACRTEcIeoAKwpqoK6pYs1hqj0rHHT5T/lQUAJhWExAGYjAJBPSC1ACil9wCmNii6uy5BNpuBocHBGe5akgAopXMB4CezduLXLzhx/GhhESNTTADWAkCBPiFk3CXhWM0DsOvrpsIxAfAU6UQIV4NNx/woATDJKk8uELQeIO4A6d48V9QAuHA9oBgKWpuwtBfbuD1WXAC4sEfYeIIvgOK+/jz+ENO3zxQ3AKHOyBL1RUJIsy4xKgEU9/oL+/ojuRx8/foFWk+d1LUXewhgCRXnBwBwRXeWwA+AtwvkV5ZWKW4PkIWCSU6QAnCN+yRzAJZNPpgGALs9k03MY+EVXhD5LYj8ZLNzrASgM549RFUSixqASbFU3JpTjQxOADjhJAFw6eoRunCwBoDP68wGANgTZF5gDQATnQ0AmHifrQDIkqBux4crjhwgyi9nGQPgUp0Aw/J74KwHwKSDoBslopRsJagatq2SoInSsDWGa4LFPmtLyUbDoIk4ADb8nD3TAp8/fTK5LVQJAD4AwCIAXwjK8rl2OSwKH49tb22BXDYTKwRh/e8ZVuyXVH4HKa0BiPlBNxEJW6k4KitLklEmxVQeli5CkJ4WNz30xGV7vU3FRyenEMCilC7DCchkQiLKFECYhnMlBeAn+/xFN6TaLGtdFSqAh333obvrsrQvwvLUCIAY+6n3AAv3NwLApJvJBVWoHmAIoIEXKnUhUDIAhFguXwBiDOMFl3hQkqskQsBvPc4hlASAly+ez9g8wZsVsizOAbx5/QqGh9/DvTu3vbcvHq1P6yhQCwD9AFNbaOxNYqEvQwqZX8zaePuNQeg42+Zdgu79AwB/U/3prK6A4vf2dPeyD7UIIZ1BhzyZAg+DwrRY+umsieuKG7HeVNXxBKip/gEHPURu4XstNwAAABBkZUJHNjQxNTJBODYwMTI0MjAzNbLqoqoAAAAASUVORK5CYII=",
          "enforcesSecureChat": False
      }
  threeam={
            "version": {"name": "26.3", "protocol": 777},
            "players": {
                "max": 11,
                "online": 25,
                "sample": [
          {"name": "§cEnds Nov 25", "id": "00000000-0000-0000-0000-000000000001"}
      ]
            },
            "description": {
        "text": "§e{3 am} §8Pick something dark themed to build. A moody website, a cursed little tool, a game, or whatever...",
    },
            "favicon": "data:image/png;base64,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",
            "enforcesSecureChat": False
        }


  
  today = date.today() # 23/11/2026
  if today > date(2027, 2, 28):
   phantom={
         "version": {"name": "§cEnded", "protocol": -1},
         "players": {
             "max": 2,
             "online": 28,
             "sample": [
       {"name": "§cEnded Feb 28", "id": "00000000-0000-0000-0000-000000000001"}
   ]
         },
         "description": {
             "text": "§f{Phantom} §8Build creative projects for 50 hours, then fly to an escape room hackathon in Philadel..."
         },
         "favicon": "data:image/png;base64,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",
         "enforcesSecureChat": False
     }
  if today > date(2026, 12, 31):
    hackcraft={
        "version": {"name": "§cEnded", "protocol": -1},
        "players": {
            "max": 12,
            "online": 31,
            "sample": [
      {"name": "§cEnded Dec 31", "id": "00000000-0000-0000-0000-000000000001"}
  ]
        },
        "description": {
    "text": "",
    "extra": [
        {"text": "{Hack", "color": "dark_green"},
        {"text": "Craft} ", "color": "#986a44"},
        {"text": "Create a Minecraft mod, earn a free game and server hosting!", "color": "dark_gray"}
    ]
},
        "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDI2LTExLTIzVDE0OjIxOjE5KzAwOjAwpH4maAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNi0xMS0yM1QxNDoyMToxNSswMDowMDTLbcMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjYtMTEtMjNUMTQ6MjE6MTUrMDA6MDBFltV/AAAACXBIWXMAAAPYAAAD2AFuR2M1AAADAFBMVEUAAABQOSc4JxpLNSQzIxhHMyNZQCxALB4xIhdLNiUpJyk9Kx1JNCQ6KBxFMSE2JhpVPSpVPClXPipDLh9POCZROihkSDFgRS9XjDS7sa49LB6+tLECAQFTPClHMiJCLyBUOygEAwNONyZALR8pHBNcQi1DMCE9LR80JRlZPytoSzRXPyx3VjtSOygsHxU/LB5MNyZpTDQQDQvOwr9dQy66sK1ShDE8KhxuTzbLwL1ThzFPhC0HBgUMCQhzmk07Kh0gHx9rTTVRhi59WT5FOCFLPCUmJSZOgS1CLR4vIBZXizRFMCBMSUhNNiVBMCJiRzDPxMF2nFDAtbJdkzkmGhLVycbBtrPRxsNDNiBulEjCuLXHvLlxl0sgFw/ZzcpajzZkmEHJvrvQxcJojkG3rapajThFLx9VfTNYjjXFurdglT1VijJOTEuyqabUyMXEubYZGBhckDnWysdRT05HbSdQeS9pn0Z0UzmCXUBmSTOwpqNMdStWhzVIOiMzJhxBLyC5r6wjISI3NDO1q6hqkUN5n1JXijVDMSWupaJBPTyto6BJRkRjlkJIMSFHMCE2KR8qKSpxUTgWFRQSERFHeiUaEgxLfSpKcSlVUlIdHBmfl5QvLS1ohENkmkE4NjZgkj29s7BEdySXj41JRCVPS0dyj0ymnZtFQkE5ODlagjcyMDBSPS1fhz6QiIZ5cnBti0hDZSVORyheW1smIxKHYUNZhTU+OzpqZGNkiz88OTiAeXZlYF6Gf32HgH40UiB0bmxLPilFOiZxa2kpPhlaVlNcWFaDfHlvaWiEfXs7XSUrKBZcWVczJBlbkDhFMiI9Kx1DLyBDLyBDLyA+LB46Khw0JRk6KRw8Kx1XjTQ9LB5WjDI1JRpZPytckTpaiDdFMSFgkTxIMyNHNSNbkDlajzdglT1gkTxUPililT9BLyBolkNCMCE9LB47Kh01JRlYjjRMgSo+LB5cQS1cQS1MeSlnlkNhlj5Qhi02JhpJfidMNyYyIxlFeiM7Kh1DeCBHcEzsx81TAAABAHRSTlP///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8pCqXrPHUM3UL4ClXd9Oum9tKk9nXrtUL1pjzFVdLrKfy10sUpxevcVbUptd5C+SnSxaYApVAE3QAAAYxpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0n77u/JyBpZD0nVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkJz8+Cjx4OnhtcG1ldGEgeG1sbnM6eD0nYWRvYmU6bnM6bWV0YS8nIHg6eG1wdGs9J0ltYWdlOjpFeGlmVG9vbCAxMi45OCc+CjxyZGY6UkRGIHhtbG5zOnJkZj0naHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyc+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczpwZGY9J2h0dHA6Ly9ucy5hZG9iZS5jb20vcGRmLzEuMy8nPgogIDxwZGY6UHJvZHVjZXI+T25saW5lLUNvbnZlcnQ8L3BkZjpQcm9kdWNlcj4KIDwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSdyJz8+uaFLMAAACyxJREFUWMNklnlQk2cexx8ICQl5CTkh0ZwgWZIQDeEKIVFAAsFEgqjchyIBBETOxXAMKgoiyhTlkMOKoFC1ntu11qPaa89hu7udnXGd6rrr0U7/aafbdmd3drb7e56XuJ3uZyaT50me3+f9/p687wPo+xWWXz598eXDR8+9Umnd1vr6rdaMDGvl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",
        "enforcesSecureChat": False
    }
  if today > date(2026, 12, 18):
      jamegam={
               "version": {"name": "§cEnded", "protocol": -1},
               "players": {
                   "max": 12,
                   "online": 18,
                   "sample": [
             {"name": "§cEnded Dec 18", "id": "00000000-0000-0000-0000-000000000001"}
         ]
               },
               "description": {
           "text": "§7{jame gam} §8a community of teenagers who enter game jams together. build a game, get prizes",
       },
               "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAE2ElEQVR4Xu2bTUhVQRTHz2xzUWF7000FRrWqiNYFlYpBUVBQVKsioyiSlhFmWkpBUJZQRNCHpRXUKsJFX4SFmLR57xn0ISXlI4s2TszzzeU4ztz5uJ++13/53r1z5/zuOWdmzswlUOYiZW5/PAAopT/CAE0ImR9GO1ihegCltF7RwfuK323VwG4ghPTa3qhS2ABoWB3zEyEktH4HaohSOgAAy02M3ly3weQyqXbt2Qsb6wov31NYEJwBUCp/20EMNdHdvkf4suWEkHcm94UaAtj4bCYDR5oOBOmDtQQIbwkhK6wbKcraA7Dxhw/uh1w26/rsQBIgOIeEFQBK6TkAaGI9v3r5EvQ/ewr5fD6QIa7asKke6hsbobJyAW+igxByyLY9WwBelo861k3U1nEeqmtqAiVGJwBBjZ9TUQHXb97ytdH0GQurq6G980KhLZeRITIAzEV3793nayTWjm1b4PfEhPcTj3EdiNQBEJMTEzbiaPMJWLlq9TTjVUbytli+efRAPvlLPQCZcWII6ABwya77DyBtOUDMzCYewOYTH0dGYHJy0nvb2LCxse+QH89LJ1ypA8CE84AJACZVEuRzjlTlADGxyYRHATEJ1tYuhZ3bt0rvw2IgUzUKMPGpsK5jcSj2iRAGwJTkWoAJA3CZBDFZTYS4kl4NinmmYIhjkcQVgLcoYhm6t6dHmaSikDDL/AYAN1wWQs4eIIaCSVIMU4nWA8QwCFoQOb1+ndfm0OgoXBt4q2WFACRTEcIeoAKwpqoK6pYs1hqj0rHHT5T/lQUAJhWExAGYjAJBPSC1ACil9wCmNii6uy5BNpuBocHBGe5akgAopXMB4CezduLXLzhx/GhhESNTTADWAkCBPiFk3CXhWM0DsOvrpsIxAfAU6UQIV4NNx/woATDJKk8uELQeIO4A6d48V9QAuHA9oBgKWpuwtBfbuD1WXAC4sEfYeIIvgOK+/jz+ENO3zxQ3AKHOyBL1RUJIsy4xKgEU9/oL+/ojuRx8/foFWk+d1LUXewhgCRXnBwBwRXeWwA+AtwvkV5ZWKW4PkIWCSU6QAnCN+yRzAJZNPpgGALs9k03MY+EVXhD5LYj8ZLNzrASgM549RFUSixqASbFU3JpTjQxOADjhJAFw6eoRunCwBoDP68wGANgTZF5gDQATnQ0AmHifrQDIkqBux4crjhwgyi9nGQPgUp0Aw/J74KwHwKSDoBslopRsJagatq2SoInSsDWGa4LFPmtLyUbDoIk4ADb8nD3TAp8/fTK5LVQJAD4AwCIAXwjK8rl2OSwKH49tb22BXDYTKwRh/e8ZVuyXVH4HKa0BiPlBNxEJW6k4KitLklEmxVQeli5CkJ4WNz30xGV7vU3FRyenEMCilC7DCchkQiLKFECYhnMlBeAn+/xFN6TaLGtdFSqAh333obvrsrQvwvLUCIAY+6n3AAv3NwLApJvJBVWoHmAIoIEXKnUhUDIAhFguXwBiDOMFl3hQkqskQsBvPc4hlASAly+ez9g8wZsVsizOAbx5/QqGh9/DvTu3vbcvHq1P6yhQCwD9AFNbaOxNYqEvQwqZX8zaePuNQeg42+Zdgu79AwB/U/3prK6A4vf2dPeyD7UIIZ1BhzyZAg+DwrRY+umsieuKG7HeVNXxBKip/gEHPURu4XstNwAAABBkZUJHNjQxNTJBODYwMTI0MjAzNbLqoqoAAAAASUVORK5CYII=",
               "enforcesSecureChat": False
           } 
  if today > date(2026, 11, 25):
     threeam={
                 "version": {"name": "§cEnded", "protocol": -1},
                 "players": {
                     "max": 11,
                     "online": 25,
                     "sample": [
               {"name": "§cEnded Nov 25", "id": "00000000-0000-0000-0000-000000000001"}
           ]
                 },
                 "description": {
             "text": "§e{3 am} §8Pick something dark themed to build. A moody website, a cursed little tool, a game, or whatever...",
         },
                 "favicon": "data:image/png;base64,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",
                 "enforcesSecureChat": False
             }
  if number == 1:
     jeison=phantom
  elif number == 2:
     jeison=hackcraft   
  elif number == 3:
     jeison=jamegam
  elif number == 4:
     jeison=threeam   
  text = json.dumps(jeison).encode("utf8")
  print(text)
  
  textwithleng = varint(len(text)) +text
  pack = b"\x00" + textwithleng
  response = varint(len(pack)) + pack
  conection.send(response)
  datos3 = conection.recv(1024)
  print(datos3)
  conection.send(datos3)
 else:
    jeison = {"text": "§7Check out all ysws available at\n§f§nhttps://hackclub.com/programs\n\n§c§lHack Club <3"}
    text = json.dumps(jeison).encode("utf8")
    print(text)
    textwithleng = varint(len(text)) + text
    pack = b"\x00" + textwithleng
    response = varint(len(pack)) + pack
    conection.send(response)

 conection.close()
