"""
Fetch the USB device.
"""
import usb.core

from .constants import USB_ID_PRODUCT, USB_ID_VENDOR
from . import asserts

# pylint: disable=no-member
def find():
    "Find the device, sanitize and return it"
    device = usb.core.find(idVendor=USB_ID_VENDOR, idProduct=USB_ID_PRODUCT)
    asserts.device(device)

    # We can't communicate with the device(s) if there are already drivers
    # attached to it.
    for configuration in device:
        for interface_index in range(configuration.bNumInterfaces):
            if device.is_kernel_driver_active(interface_index):
                device.detach_kernel_driver(interface_index)

    device.set_configuration() # Set the default configuration
    return device
