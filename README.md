pbLuaConnect
======
This is a collection of simple python scripts to provide easy cross-platform access to a Lego Mindstorms NXT robot running the modified firmware [pbLua](https://github.com/7HAL32/pbLua).

Prerequisites
------
1. Make sure to have a flashed NXT brick running pbLua connected to your computer via USB (at the moment Bluetooth is not supported). Therefore follow the instructions provided in the [pbLua repository](https://github.com/7HAL32/pbLua).

2. In order to communicate with the brick make sure to have the respective drivers installed.
    * For macOS and Windows [official Lego NXT Fantom drivers](http://cache.lego.com/r/www/r/mindstorms/-/media/franchises/mindstorms%202014/downloads/firmware%20and%20software/nxt%20software/nxt%20fantom%20drivers%20v120.zip?l.r2=-964392510) are available.

    * On Linux the package [libusb](http://libusb.org) is needed.
```
sudo apt-get install libusb
```

3. The provided scripts were written in Python 3.
    So please check if python already lives on your system.
```
python3 --version
```
If the output looks something like `Python 3.x.x`, you're good to go. Otherwise you'll need to install Python. There are official downloads with setup instructions available [on their website](https://www.python.org/downloads/).

  Users on Unix-like systems are lucky, as they can use a package-manager instead to install Python.

    Linux
  ```
  sudo apt-get install python3
  ```
  macOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
```
brew install python3
```

Usage
------
The main script *run.py* is a wrapper for all other scripts and functions in this repository. It can be used to establish a connection with your brick, transmit a lua script, run it and show you any results.

There is an easy shorthand command that takes care of everything.
```
./run.py your_cool_script.lua
```

```
./run.py -r
```
