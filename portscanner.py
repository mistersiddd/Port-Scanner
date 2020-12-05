import socket


target=input('Enter the IP address to be scanned:')
port_range=input('Enter the range of port to be scanned (EG 80-8080) ')

lowerbound=int(port_range.split('-')[0])
upperbound=int(port_range.split('-')[1])
print ('Scanning IP address ',target,' from port ',lowerbound,' to port ',upperbound)

for port in range (lowerbound,upperbound):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    success_flag=s.connect_ex((target, port))
    if(success_flag == 0):
        print('Port ',port,'is open')
    else:
        print('Port ',port,'is closed')
    s.close()