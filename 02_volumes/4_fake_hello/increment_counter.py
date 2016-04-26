import os
import time
from atomicfile import AtomicFile


COUNTER_PATH = os.getenv('COUNTER_PATH', '/tmp/counter.txt')
INCREMENT = os.getenv('INCREMENT', "1")
WAIT = os.getenv('WAIT_TIME', 3)


def add_visit(number=1):
    counter = 0
    try:
        with open(COUNTER_PATH, "r") as f:
            counter = int(f.read())
    except:
        pass

    counter += number

    with AtomicFile(COUNTER_PATH, "w") as f:
        f.write(str(counter))
        f.close()

if __name__ == "__main__":
    try:
        while True:
            time.sleep(WAIT)
            add_visit(int(INCREMENT))

    except KeyboardInterrupt:
        print('See you soon!')
