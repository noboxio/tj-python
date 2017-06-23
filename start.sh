# start.sh: kill all threads before we start the program.

sudo kill -9 `pidof python3`
python3 tjbot.py
