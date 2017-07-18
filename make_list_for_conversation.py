


import music
import servo
import music

import pydoc


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
        print("music."m)
        print(eval("pydoc.render_doc(mm." + m + ".__doc__"))
        print(thin_line)



    #dir(music)
    #dir(servo)
    #dir(music)


if __name__ == "__main__":
    main()
