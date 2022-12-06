# Path of Exile Rich Presence

Simple Path of Exile Rich Presence for Discord. Displays time from launch and current location (defults to "Main Menu" at startup and waits for location change).

![](examples/menu.png) | ![](examples/location.png)
:-:|:-:

# Running
1. Find the game installation folder. For Steam users the default is `C:\Program Files (x86)\Steam\steamapps\common\Path of Exile`, for non-Steam installations it should be in `C:\Program Files (x86)\Grinding Gear Games\Path of Exile`

2. Inside the game installation folder there should be a `logs` directory with a `Client.txt` file inside.

3. Make sure you have Python version at least 3.7 and install required libraries: `python -m pip install -r requirements.txt`

4. Run the presence by giving it a path to the `logs` directory: `python path-of-exile-rpc.py C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs`

5. To stop the presence, press `Ctrl` + `C`


## Notice
This was created and tested a long time ago, so don't expect everything to work.

Please check out these projects:
- [Exiled Presence](https://github.com/nibbydev/Exiled-Presence)
- [PathOfExileRPC](https://github.com/xKynn/PathOfExileRPC)


## Credits
- [Pypresence](https://pypi.org/project/pypresence/)
- [Path of Exile](https://www.pathofexile.com) ❤️
