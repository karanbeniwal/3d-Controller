# 3d-Controller

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

3d-Controller is a use case where a 3d object gets it's rotational values from a smartphone's sensors.

- It receives data over the network using UDP connection
- IPC used : shared_memory
- 3d library used: ratcave

## Guide

### 1. Install the requirements:

```sh
$ cd /to/project/directory/
$ pip install -r requirements.txt
```

### 2. Open UDP Server:

```sh
$ python UDP_server.py
```
* make sure UDP Port 5556 is open in the firewall

### 3. Run the 3d-viewer, in a new separate shell/cmd prompt:

```sh
$ python 3d_view.py
```
* You can reset the roational values to a default pose by pressing key "R" in the 3d-view window.

### 4. Stream the sensor data to 3d-view:

You can control the 3d object in two ways:

#### 4.1 The APP method:
(Using an app that broadcast phone's sensor info to 3d-view)
	
Install the following android app:
https://play.google.com/store/apps/details?id=de.lorenz_fenster.sensorstreamgps

* both the smartphone and target system should be on same network.

1. Set the PC's IP Address as "Target IP Address" in the app
2. Set the port as 5556
3. "Sensor Update Frequency", leave it as "Medium"
4. Select "UDP Stream"
5. Check "Run in Backgroud" if you want to let the sensor signals pass through even when the app is not active.
6. Goto tab "Toggle Sensors">>Check "Orientation", and also Check "Include User-Checked Sensor Data in Stream"
7. Back to tab "Preferences">>"Switch Stream">>ON
8. Start rotating the phone as see the model being rotated in same way.

If you don't want to connect a smartphone, there's an emulator you can use with this.

#### 4.2 The emulator method:
(Using an emulator provided within)

Run the emulator python script, in a separat new shell/cmd prompt
```sh
$ python UDP_tx_emulator.py
```
Use the following keys to send related sensor data:
UP-DOWN 	: Rotate X-axis
RIGHT-LEFT 	: Rotate Y-axis

