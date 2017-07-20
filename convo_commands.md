================================================================================
Commands for MusicManager
================================================================================
~music.get_playlist()~
    Get playlist.

    Returns the list of songs in the playlist.

~music.load_music()~
    Load the songs that are in the resources/music folder.

    Loads the music from the resources/music folder

~music.next()~
    Play next song.

    Plays the next song in the list.

~music.pause()~
    Pause the now_playing song.

    Pauses the now_playing song.

~music.play()~
    Play next song.

    Plays the next song in the list of music, if no song is playing.

~music.play_song_name(song_name)~
    Play a song based on the song name.

    Search the playlist for the song name and then play it.

~music.previous()~
    Play previous song.

    Plays the previous song in the list.

~music.say_playlist()~

~music.shuffle()~
    Shuffle the list of music objects.

    shuffles the list of music objects, it does not reset current playing.

~music.stop()~
    Stop the song.

    Stops the song that is currently playing.

~music.fast()~
    Make this song faster.

    This will make the song play faster
    !Currently not implemented!

~music.slow()~
    Make this song slower.

    Will make the song play slower
    !Currently not implemented!

~music.speed(speed)~
    Change the speed of the song.

    This will change the speed of the song playing
    !Currently not implemented!

    speed -- the multiplier of the speed.  1 = normal

================================================================================
Commands for LedManager
================================================================================
~led.empty_commands()~
    Empty the commands list.

    empties the commands list

~led.restart()~
    Delete the led object and create a new one.

    This is an attempt to be able to stop a current command and start a new

~led.wait(duration)~
    Wait for a specified period of time.

    Cause this thread to sleep for a specified duration.

    duration -- amount of seconds to make this thread sleep.

~led.custom_color_name(color_name)~
    Change the color of the LED to the specified name color.

    Change the color fo the LED to the specified color value

    color_name -- valid color name or id using colour module

~led.custom_color_rgb(r, g, b)~
    Change the color to a custom color.

    Change the color of the LED to the specified color R G B values

    r -- int value of red
    g -- int value of green
    b -- int value of blue

~led.off()~
    Turn the led off.

    Turning the led off just sets the color to black.

~led.rainbow(wait_ms=1,iterations=1)~
    Make the LED go rainbow.

    The led will go between the different colors with a wait and iteration.

    wait_ms -- int miliseconds to wait between changes default=1
    iterations -- number of times to repeat the cycle default=1

~led.strobe()~
    Strobe the led.

    Turn the led on and off rapidly

================================================================================
Commands for ServoManager
================================================================================
~servo.angle(degrees)~
    Set the angle of the servo to a specific angle.

    degrees -- int value of degrees to be set at
               MUST BE BETWEEN 0 and 180
    map function is used to map the values into useful data for the servos
    we are using.  The out min and max may need to be changed for
    different servos.

~servo.down()~
    Point the arm down, use this to define the up angle
    angle depends on the orientation of the servo

    TODO: perhaps make this a constructor variable?

~servo.up()~
    Point the arm up, use this to define the up angle
    angle depends on the orientation of the servo

    TODO: perhaps make this a constructor variable?

~servo.wave(times=5)~
    Wave the arm.
    A wave is defined as going from the down position to the up position once

    times -- the number of times to wave, default = 5
