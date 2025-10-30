Customizable cross-platform general-purpose launcher program which asks the user for an IP then attempts UPnP mapping of provided IP and internally-configured port, then launches internally-configured target application with provided IP and internally-configured port as command-line arguments 

# Usage
1) `pip install miniupnpc pyinstaller`
2) In `P2PLauncher.py`: Set `TARGET_APP` to the relative path of the networked app you want to launch
3) In `P2PLauncher.py`: Set `TARGET_PORT` to the port you wish to forward and use in your target app
4) `pyinstaller -F P2PLauncher.py`
(Output executable is in `dist/`)
