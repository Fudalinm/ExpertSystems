from subprocess import *
import threading
from logging.handlers import *
import time


def cmd_as_bytes(s):
    return s


def start_terminal(p):
    return Popen(p, bufsize=0, stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True, shell=True)


def send_data(p, data):
    print('S: ' + data + '\n')
    p.stdin.write(cmd_as_bytes(data + '\n'))
    p.stdin.flush()


def read_data(p):
    while True:
        r = p.stdout.readline()
        print('Out :' + r)


def read_err(p):
    while True:
        # p.stderr.flush()
        r = p.stderr.readline()
        print('Err: ' + r)


def send_thr(p):
    while True:
        x = input('>>')
        send_data(p, x)


if __name__ == "__main__":
    PROLOG_LOCALIZATION = "swipl"
    FILE_TO_LOAD = "movie_choser.pl"
    MAIN_FUNCTION = "wykonaj."

    cmd = start_terminal([PROLOG_LOCALIZATION, FILE_TO_LOAD])

    send_data(cmd, FILE_TO_LOAD)
    send_data(cmd,MAIN_FUNCTION)

    # start processes
    read_thread = threading.Thread(target=read_data, args=(cmd,))
    err_thread = threading.Thread(target=read_err, args=(cmd,))
    send_thread = threading.Thread(target=send_thr, args=(cmd,))

    read_thread.start()
    err_thread.start()
    send_thread.start()


    read_thread.join()
    err_thread.join()
