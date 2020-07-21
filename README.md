# L2PING flood attack

This repo contains a simple script to run `l2ping` on a bunch of processes to try and flood a bluetooth device and force it to disconnect.
It works quite well.

# Example
To run this rudimentary l2ping flood attack on a device with MAC address FC:58:FA:83:FA:2D on 150 processes, type this command:
```
$ python l2ping-flood.py FC:58:FA:83:FA:2D -p 150
```

**NOTE: You'll likely have to run this with sudo**

A couple different fun things to try out:

- Pair you bluetooth headphones to your computer and start listening to music.
Then run this script with different numbers of processes and you'll hear how the bluetooth connection is being flooded and the music starts breaking up.
- This one will work on Ubuntu. Like above, pair your bluetooth headphones to your computer. Run `bluetoothctl` in one terminal. Then run lsping-flood.py.
Watch the terminal where you're running `bluetoothctl` to see if you can force the headphones to disconnect.

# Usage

To view usage, run `python l2ping-flood.py -h`:

```
usage: l2ping-flood.py [-h] [-p PROCESSES] mac

positional arguments:
  mac                   MAC address of device to smash

optional arguments:
  -h, --help            show this help message and exit
  -p PROCESSES, --processes PROCESSES
                        Number of process to run l2ping on. Default is 100
```
