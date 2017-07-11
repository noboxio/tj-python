











from multiprocessing import Process
import time




class lled():
        def __init__(self, text):
            self.text = text

        def s(self):
            print(self.text)

        def gogo(self):
            while True:
                self.s()
                time.sleep(1)

def __main__():

    l = lled("message here")

    param = "gogo"
    cmd =  "l." + param
    print(cmd)

    p = Process(target=eval(cmd))

    #exec("p = Process(target=l.gogo)")

    p.start()

if __name__ == '__main__':
        __main__()
