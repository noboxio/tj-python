
import music

def main():
    s = music.Song("./resources/speech.wav")


print(s.process.communicate(input=b'p'))

print(s.process.communicate(input=b'p', timeout=.5))


s.process.stdin.write(b'p')
s.process.communicate()

if __name__ == "__main__":
    main()
