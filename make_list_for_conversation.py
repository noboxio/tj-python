


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
        print("music." + m)
        details = eval("pydoc.render_doc(mm." + m + ")")
        details.replace("\n",'',2)
        print(thin_line)



    #dir(music)
    #dir(servo)
    #dir(music)


if __name__ == "__main__":
    main()
