# OBD Simulator
--------------

OBD Simulator is an OBD-II compliant simulator adhering to the SAE standard J/1979 and ELM 327 command protocol.

### How It Came To Be
---------------------
I was looking to create an Android app that utilized OBD-II via an ELM 327 device. When I realized I would need a way to simulate the OBD interface, I searched high and low for something capable and found literally one OBD software simulator: OBDSim. This seemed perfect until I realized how much of a nightmare it is to work with serial ports in Java. After trying three seperate COM libraries, I knew a different solution was needed.

### About OBD-II
----------------
In order to get engine sensor specific data, two bytes are written to the OBD-II port (I call these "query bytes"), and up to eight bytes are returned. This is best demonstrated with an example. Say we
wish
 to get the Engine RPM. We would write 01 and 0C ("01 0C"), and would receive something akin to "41 0C 20 BC" back. The first two bytes, "41 0C" are the response code indicating the following bytes will describe the engine RPM's actual value. Therefore, "20 BC" are the two bytes representing the current Engine RPM. This query only returns two bytes, but queries can return as many as six bytes (plus the first two bytes for the response code, so a maximum eight). To calculate the ACTUAL value of the Engine RPM  from the bytes, a specific formula is needed (for Engine RPM it's ``((A*256)+B)/4``.

### What OBD Simulator Does
---------------------------
OBD Simulator creates a server instance at the specified address and port that accepts query bytes, processes them, and returns a random (but appropriate) response. Once you create an instance of OBD Simulator, all you need to do is open a socket at the correct address and port using your language of choice.

### How To Use It
-----------------
```
python.exe Program.py -address=localhost -port=1090 -shell
```
If the address and the port are not specified, the defaults "localhost" and "1090" will be used.
If -shell is passed, a seperate python instance wll be created with a shell connected to the OBD Simulator server instance's address and port.

Note that OBD Simulator is designed to take string reprsentations of bytes. If you wished to send 0x01 0x0C, conversion will be attempted to "01 0C". This is strictly to emulate ELM 327 device behavior.

### Project Status
------------------
Currently supports:
* Mode 01
* All PIDs up to 60

Planned:
* Modes 02, 03, 04, 07
* Logging
* User specified values
* Engine simulation