


import music
import servo
import music



def main():
    """Main method creates a TJ bot and starts it along with the console_input.

    main method
    """

    line = "================================================================================"
    print(line)
    print("Commands for MusicManager")
    print(line)
    mm = music.MusicManager()

    for m in dir(mm):
        print(m)
        print(eval("mm"." + m + ".__doc__"))
        print(line)



    #dir(music)
    #dir(servo)
    #dir(music)


if __name__ == "__main__":
    main()
