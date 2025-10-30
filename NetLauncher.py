import os
import tkinter as tk
import miniupnpc


# -- SET THESE --
TARGET_APP = ""
TARGET_PORT = 12345


if os.name == "nt":
        RUN_PREFIX = ".\\"
else:
        RUN_PREFIX = "./"

os.chdir(os.path.abspath(os.path.dirname(__file__))) # For Pyinstaller executable

root = tk.Tk()
root.title("Enter IP address")
root.eval("tk::PlaceWindow . center")

ip = tk.StringVar()
tk.Entry(root, textvariable=ip).pack()

def on_connect_button_pressed():
        try:
                upnp = miniupnpc.UPnP()
                upnp.discover()
                upnp.selectigd()
                upnp.addportmapping(
                        TARGET_PORT,
                        "UDP",
                        upnp.lanaddr,
                        TARGET_PORT,
                        "",
                        ""
                )
        except Exception:
                pass

        os.system(RUN_PREFIX+TARGET_APP+" "+ip.get()+" "+TARGET_PORT)
tk.Button(root, text="Connect", command=on_connect_button_pressed).pack()

root.mainloop()