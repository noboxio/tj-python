# TROUBLESHOOTING

## `ErrorNo 9981` : Input Overflow
In `streaming.py`, change the default rate value in the `__init__` constructor from `48000` to `44100`.

## Make sure package `websocket` is not installed.
If getting errors about WebSocketApp, pip3 uninstall `websocket-client` package and reinstall.

## Speaker not working
Check connections.  Right-click on the Audio icon in the upper right and make sure it is set to Analog and not HDMI.

## Conversation not responding
Make sure the name of the robot is not capitalized
