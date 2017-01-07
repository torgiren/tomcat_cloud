import dbus
import subprocess
import os
import sys
import time

SYSTEMD_BUSNAME = 'org.freedesktop.systemd1'
SYSTEMD_PATH = '/org/freedesktop/systemd1'
SYSTEMD_MANAGER_INTERFACE = 'org.freedesktop.systemd1.Manager'
SYSTEMD_UNIT_INTERFACE = 'org.freedesktop.systemd1.Unit'

bus = dbus.SystemBus()

systemd_object = bus.get_object(SYSTEMD_BUSNAME, SYSTEMD_PATH)
systemd_manager = dbus.Interface(systemd_object, SYSTEMD_MANAGER_INTERFACE)

unit = systemd_manager.GetUnit('httpd.service')
unit_object = bus.get_object(SYSTEMD_BUSNAME, unit)

systemd_manager.StopUnit('httpd.service', 'replace')

