#
# Информация о системе: Реализуйте программу, которая выводит информацию о системе (например, операционная система, архитектура процессора).
#

import platform # pip install platform
import psutil # pip install psutil
import getpass # pip install getpass
import socket # pip install socket
import cpuinfo # pip install py-cpuinfo

my_system = platform.uname()

nics = psutil.net_if_addrs()
mac_address = nics["Ethernet"][0].address



print(f"OS System: {platform.platform()} {my_system.release}")
print(f"Machine: {my_system.machine}")
print(f"Computer Name: {my_system.node}")
print(f"User Name: {getpass.getuser()}")  # Имя пользователя
print(f"MAC adress: {mac_address}")  # MAC адрес
print(f"IP adress: {socket.gethostbyname(socket.getfqdn())}")

print(f"Processor: {cpuinfo.get_cpu_info()["brand_raw"]}")  # WARNING: for CPUINFO need little time :'(
print(f"RAM Total: {psutil.virtual_memory().total / (1024.0**3):.2f} GB") # :.2f - оставяем только 2 последние цифры

print(f"Used RAM Now: {(psutil.virtual_memory().used / (1024.0**3)):.2f} GB {psutil.virtual_memory().percent} %")

print("Deal!")
