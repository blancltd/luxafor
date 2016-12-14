# Python API for Luxafor
Python 3 API Interface for Luxafor

On udev systems you may want to do this so you don't have to run as root:
```shell
echo '"ACTION=="add", SUBSYSTEM=="usb", ATTRS{idProduct}=="f372", ATTRS{idVendor}=="04d8", MODE:="666"' > /etc/udev/rules.d/10-luxafor.rules
``` 

# Quickstart
Assuming the current user is allowed to access the device:
```python
import luxafor

API = luxafor.API()
API.mode_colour(luxafor.COLOUR_RED)
```
You may want to read the help() text for API class and perhaps list the contents
in luxafor.constants .