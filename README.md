# Path of Exile Rich Presence

Simple Path of Exile Rich Presence for Discord. Displays time from launch and current location (defults to "Main Menu" at startup and waits for location change).

![](https://i.imgur.com/5priaBA.png) | ![](https://i.imgur.com/ChNhmHm.png)
:-:|:-:

# Running
1. Find your logs directory (should be located in your game directory and contain a `Client.txt` file)

2. Make sure you have python3 and all required libraries installed:
    `python3 -m pip install -r requirements.txt`

3. Open a terminal

4. Run the presence by giving it a path to your logs directory:
    `python path-of-exile-rpc.py C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs`

5. To stop the program press `Control` + `C`


## Notice
This app is still very WIP, so unresponsive updates of your presence can be expected (skipping location changes). If you have any suggestion or changes to commit to this project, please contact me on Discord (@Predator#4682) or open a [Github issue](https://github.com/Stefankar1000/path-of-exile-rpc/issues).

## Credits
- [Pypresence](https://pypi.org/project/pypresence/)
- [Path of Exile](https://www.pathofexile.com) for being an awesome game ❤️
