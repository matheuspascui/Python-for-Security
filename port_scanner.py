import socket

host = input("Digite um IP/Host: ")
ports = [21,22,23,25,53,80,111,135,139,443,445,3306,8080,9090]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((host, port))
    if code == 0:
        print(port, " is open!")


