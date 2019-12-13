# Path of Exile RPC
This is still a very simple app, that I got working in a few hours. It displays your current location and time that the RPC client has been running.

I am planning to add more stuff, but I'm still not sure how to get some info, such as character and league name, character class and so on.

All info is gathered from client logs (logs/Client.txt).

![Presence running in Idle](https://i.imgur.com/VuxjL8A.png)


# Running
1. Find your logs directory (should be located in your game directory and contain a `Client.txt` file)

2. Make sure you have python3 and all required libraries installed:
    `python3 -m pip install -r requirements.txt`

3. Open a terminal

4. Run the presence:
    `python path-of-exile-rpc.py C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs`

5. To stop the program press `Control` + `C`


# Notice
This app is still very WIP, so unresponsive updates of your presence can be expected. If you have any suggestion or changes to commit, please contact me on Discord (@Predator#4682) or make a Github issue/pull request.