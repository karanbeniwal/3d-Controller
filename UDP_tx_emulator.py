import pyglet
from pyglet.window import key
import socket

#settings

send_to_ip = '127.0.0.1' #send UDP data to self
send_to_port = 5556

#--------------------------------------------------

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# create pyglet window with assigned keys handler
window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

rot = [0,0,0]

def send_keypress(dt):
    if keys[key.UP]:
        rot[0] += 1 
    if keys[key.DOWN]:
        rot[0] -= 1
    if keys[key.LEFT]:
        rot[1] += 1
    if keys[key.RIGHT]:
        rot[1] -= 1
    
    #prepare dummy stream as per the app specifications, based on key press data
    data = b"'9158.48985, a,a,a,a,a,a,a,a,a,a,a,a,a, " + str(rot[1]).encode("utf-8") + b", " + str(rot[0]).encode("utf-8") + b", " + str(rot[2]).encode("utf-8") + b"'"
    
    sock.sendto(data, (send_to_ip, send_to_port))
    #print(data)
    #print(dt)
pyglet.clock.schedule(send_keypress)

@window.event
def on_close():
    print("emulator closed.")

pyglet.app.run()
