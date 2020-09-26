import socket

class UDPmod:

    orient = [0, 0, 0, 0] #x, y, z, has_err
    sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
    sock.setblocking(0)
    
    def __init__(self, rx_ip, rx_udp_port):
        UDP_IP = rx_ip #'' #"192.168.43.75"
        UDP_PORT = rx_udp_port #5556
        try:
            self.sock.bind((UDP_IP, UDP_PORT))
        except:
            print("socket bind error. please check.")
        
    def get_orient(self):
        try:
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            self.orient[3] = 0
        except socket.error:
            #pass dummy data in case of error
            data = b"'9158.48985, a,a,a,a,a,a,a,a,a,a,a,a,a, 0, 0, 0'"
            self.orient[3] = 1
            pass
        #print("received message: %s" % data)
        #received message sample: b'9158.48985, 3,   4.196,  5.700,  7.334, 4,   0.111, -0.288,  0.116, 5,   0.450,-48.000, -7.650, 81, 201.559,-39.178, 23.758'
        recvarr = data.decode("utf-8").split(",")
        if len(recvarr) > 6:
            self.orient[0] = float(recvarr[-3])
            self.orient[1] = float(recvarr[-2])
            self.orient[2] = float(recvarr[-1][:-1])
        #print("converted orientation set:%s" % orient)
        #print(data)
        return(self.orient)
    
    def close_socket(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        print("socket closed.")
