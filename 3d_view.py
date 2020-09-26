import pyglet
from pyglet.window import key
import ratcave as rc
from rx import UDPmod
from multiprocessing import shared_memory

#settings

fps = 25
recv_ip = '' #all IPs of server machine
recv_udp_port = 5556

#--------------------------------------------------

#check if shared_memory exists

try:
    shm_b = shared_memory.SharedMemory('sck5556')
except:
    print("socket is not open.")
    exit()

#oUDP = UDPmod(recv_ip, recv_udp_port)

# assign key handler to newly created windows from pyglet
window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# import sample mesh collection file from ratcave repo
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# import monkey mesh
monkey = obj_reader.get_mesh("Monkey", position=(0, 0, -1.5), scale=.6)

# load monkey mesh in ratcave scene
scene = rc.Scene(meshes=[monkey])
scene.bgColor = 1, 0, 0
reset_adj = [0,0,0]
ornt = [0,0,0]

# Functions to Run in Event Loop
def rotate_meshes(dt):
    #get orientation from UDP stream
    #ornt = oUDP.get_orient()
    
    #get socket data from shm_a
    data = bytes(shm_b.buf[:]).split(b'\x00')[0]
    recvarr = data.decode("utf-8").split(",")
    if len(recvarr) > 6:
        ornt[0] = float(recvarr[-3])
        ornt[1] = float(recvarr[-2])
        ornt[2] = float(recvarr[-1][:-1])
    
    
    monkey.rotation.x = -(int(ornt[1]) - reset_adj[1])
    monkey.rotation.y = -(int(ornt[0]) - reset_adj[0])
    monkey.rotation.z = int(ornt[2]) - reset_adj[2]
    #print(ornt)
    if keys[key.R]: #reset orientation
        reset_adj[0] = int(ornt[0])
        reset_adj[1] = int(ornt[1])
        reset_adj[2] = int(ornt[2])
        #print(reset_adj)
    #print(ornt)
#pyglet.clock.schedule_interval(rotate_meshes, (1/fps))
pyglet.clock.schedule(rotate_meshes)

@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()

@window.event
def on_close():
    #oUDP.close_socket()
    shm_b.close()
    print('shared_memory closed')

pyglet.app.run()
