import socket
from multiprocessing import shared_memory

try:
    shm_a = shared_memory.SharedMemory(name='sck5556', create=True, size=1024)
except:
    shm_a = shared_memory.SharedMemory(name='sck5556')

sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
#sock.setblocking(0)

UDP_IP = ''
UDP_PORT = 5556

data = b"'9158.48985, a,a,a,a,a,a,a,a,a,a,a,a,a, 0, 0, 0'"

try:
    sock.bind((UDP_IP, UDP_PORT))
except:
    print("socket bind error. please check.")
    
print("Ctrl+C to close socket")
while(1):
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    except socket.error:
        print(socket.error)
        pass
    #print("received message: %s" % data)
    #received message sample: b'9158.48985, 3,   4.196,  5.700,  7.334, 4,   0.111, -0.288,  0.116, 5,   0.450,-48.000, -7.650, 81, 201.559,-39.178, 23.758'
    
    try:
        shm_a.buf[:(len(data)+1)] = data + b'\x00'
        #print(bytes(shm_a.buf[:]).split(b'\x00')[0])
    except KeyboardInterrupt:
        break

#print(data + b'test')

sock.shutdown(socket.SHUT_RDWR)
sock.close()

shm_a.close()
shm_a.unlink()

print("socket closed.")
