import socket

host = input("Digite um IP/Host: ")
ports = []
all_ports = [*range(0, 1025)]
#The * is an unpacking character for the argument of the function (range(), in this case)


def make_decision():
    option = int(input("Please, choose an option:\n1 - Specify the ports you want to scan\n2 - Use the default ports (0 - 1024)\n"))
    if option == 1:
        return 1
    else:
        return 2
    
def default_ports_scanner(host = host, ports = all_ports):
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((host, port))
        if code == 0:
            print(port, " is open!")

def specified_ports_scanner(host = host, ports = ports):
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((host, port))
        if code == 0:
            print(port, " is open!")


def main():
    type_of_scan = make_decision()
    if type_of_scan == 1:
        specified_ports_scanner()
    else:
        default_ports_scanner()

main()
