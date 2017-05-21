# python-lanbox

Python Interface for LanBox controllers

```python
 import lanbox
 host = '192.168.1.77'
 port = 777
 password = '777'
 box = lanbox.Lanbox(host, port, password)
 box.runCueList(1)

 channels = box.getChannels()
 duration = 10.2  # seconds
 box.fadeTo(channels, duration)
```
