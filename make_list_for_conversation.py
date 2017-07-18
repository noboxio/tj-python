


import music
import servo
import led

import pydoc
import re

def main():
    """Main method creates a TJ bot and starts it along with the console_input.

    main method
    """

    F = open("convo_commands.txt", "w")

    thick_line = "================================================================================"
    thin_line =  "--------------------------------------------------------------------------------"
    dash_line =  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    F.write(thick_line)
    F.write("Commands for MusicManager")
    F.write(thick_line)

    mm = music.MusicManager()

    for m in dir(mm):
        details = eval("pydoc.render_doc(mm." + m + ")")
        details = fix_line(details)
        out = "music." + details
        F.write(out)

    ss = music.Song("./resources/output.wav")

    for s in dir(ss):
        details = eval("pydoc.render_doc(ss." + s + ")")
        details = fix_line(details)
        out = "music." + details
        F.write(out)


    F.write(thick_line)
    F.write("Commands for LedManager")
    F.write(thick_line)

    lm = led.LedManager()
    for m in dir(lm):
        details = eval("pydoc.render_doc(lm." + m + ")")
        details = fix_line(details)
        out = "led." + details
        F.write(out)


    lm = led.NeoPixel()
    for m in dir(lm):
        details = eval("pydoc.render_doc(lm." + m + ")")
        details = fix_line(details)
        out = "led." + details
        F.write(out)

    F.write(thick_line)
    F.write("Commands for ServoManager")
    F.write(thick_line)

    lm = servo.ServoManager()
    for m in dir(lm):
        details = eval("pydoc.render_doc(lm." + m + ")")
        details = fix_line(details)
        out = "servo." + details
        F.write(out)

    se = servo.Servo()
    for m in dir(se):
        details = eval("pydoc.render_doc(se." + m + ")")
        details = fix_line(details)
        out = "servo." + details
        F.write(out)
#something else

def fix_line(line):
    lin = line.split("\n")
    out = ""
    for i in range(2, len(lin)):
        out = out + lin[i] + "\n"
    return out
    #dir(music)
    #dir(servo)
    #dir(music)


if __name__ == "__main__":
    main()
