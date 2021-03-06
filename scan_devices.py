#Copyright (c) 2017, alexandre barachant
#All rights reserved.
#Use of this source code is governed by a BSD-style license that can be  found in the LICENSE file.

import pygatt
from sys import platform

interface = None

if platform == "linux" or platform == "linux2":
    backend = 'gatt'
else:
    backend = 'bgapi'

if backend == 'gatt':
    interface = interface or 'hci0'
    adapter = pygatt.GATTToolBackend(interface)
else:
    adapter = pygatt.BGAPIBackend(serial_port=interface)

list_devices = adapter.scan(timeout=10.5)

for device in list_devices:
    print('Find device %s, MAC Address %s' % (device['name'], device['address']))
