import os
import sys
import miniupnpc


# -- SET THESE --
TARGET_APP = ""
TARGET_PORT = 12345


if os.name == "nt":
        RUN_PREFIX = ".\\"
else:
        RUN_PREFIX = "./"

# For Pyinstaller
if getattr(sys, "frozen", False):
        os.chdir(os.path.dirname(sys.executable))
else:
        os.chdir(os.path.abspath(os.path.dirname(__file__)))

ip = input("Enter target IP address: ")

try:
        upnp = miniupnpc.UPnP()
        try: upnp.discover()
        except: pass
        upnp.selectigd()
        upnp.addportmapping(
                TARGET_PORT,
                "UDP",
                upnp.lanaddr,
                TARGET_PORT,
                "",
                ""
        )
        upnp.addportmapping(
                TARGET_PORT,
                "TCP",
                upnp.lanaddr,
                TARGET_PORT,
                "",
                ""
        )
except Exception as e:
        print("ERROR: " + str(e))

os.system(RUN_PREFIX+TARGET_APP+" "+upnp.externalipaddress()+" "+ip+" "+TARGET_PORT)
