


import music
import servo
import music

import pydoc
import re

def main():
    """Main method creates a TJ bot and starts it along with the console_input.

    main method
    """

    thick_line = "================================================================================"
    thin_line =  "--------------------------------------------------------------------------------"
    dash_line =  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    print(thick_line)
    print("Commands for MusicManager")
    print(thick_line)

    mm = music.MusicManager()

    for m in dir(mm):
        details = eval("pydoc.render_doc(mm." + m + ")")
        details = fix_line(details)
        out = "music." + details
        print(out)

    ss = music.Song("./resources/output.wav")

    for s in dir(ss):
        details = eval("pydoc.render_doc(ss." + s + ")")
        details = fix_line(details)
        out = "music." + details
        print(out)


    print(thick_line)
    print("Commands for LedManager")
    print(thick_line)

    lm = led.LedManager()
    for m in dir(lm):
        details = eval("pydoc.render_doc(lm." + m + ")")
        details = fix_line(details)
        out = "led." + details
        print(out)


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
