# RSSI Quality Check in Python
Some simple RSSI quality checker written in Python 2.7 and to be made work with Ncurses + Python 3 eventually.


### Info:
Insert random bullshit info here I guess?

Nothing special to be planned for this, just a little side project as I learn to code better in Python and get to grips with it more. I may make better use out of this script I have conjured up piecing together what information I have learned thus far.

main purpose of this python script is to check currently connected RSSI signal quality of Wi-Fi you're currently connected to like so in the following preview image...


[![RSSi Quality Checker in Python][1]][1]

  [1]: https://i.stack.imgur.com/Di8wd.png
  
Clone the repo to your local directory:

```BASH
git clone https://github.com/Alkaris/RSSI-Python.git
```

run the script:
```PYTHON
python ./rssi_quality.py
```
give the script `chmod +x` execute permission and you can just run `./rssi_quality.py` without extra commands.
  
sounds easy right? hahaha I wish... my code will be bit of a mess, but take gander at it yourself and you decide. currently works as is in Python 2.3, need to do more work with it so it can work with Python 3.x, and implement a little Ncurses with it, maybe not as something like my other side test project [[here]](https://github.com/Alkaris/Roofox.py). I need to figure out stuff with the network interface card names becuase they're different from system to system, and I want to make it work across systems without needing to modify the script to match the interface names.
