from socket import AF_INET, SOCK_DGRAM, socket

socket_instance = socket(AF_INET, SOCK_DGRAM)

socket_instance.connect(('8.8.8.8', 80))
machine_ip = socket_instance.getsockname()[0]

print(machine_ip)
