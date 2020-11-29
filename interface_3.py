from subprocess import *
# import threading
from logging.handlers import *
import sys
import time

def cmd_as_bytes(s):
    return s


def start_terminal(prolog):
    return Popen(prolog, stdout=PIPE, stdin=PIPE, stderr=PIPE,  shell=True,universal_newlines=True)


def send_data(p, data):
    print('S: ' + data + '\n')
    p.stdin.write(cmd_as_bytes(data + '\n'))
    p.stdin.flush()



def read_data(p):
    while True:
        print("xD1")
        r = p.stdout.read(1)
        # r = r.decode('utf-8')
        print('Out :' + r)



def read_err(p):
    while True:
        print("xD2")
        r = p.stderr.readline()
        # r=r.decode('utf-8')
        print('Err: ' + r)


def send_thr(p):
    while True:
        x = input()
        send_data(p,x)



if __name__ == "__main__":
    PROLOG_LOCALIZATION = ["python", "echo.py"]


    cmd = start_terminal(PROLOG_LOCALIZATION)

    # start processes
    read_thread = threading.Thread(target=read_data, args=(cmd,))
    err_thread = threading.Thread(target=read_err, args=(cmd,))
    send_thread  = threading.Thread(target=send_thr,args=(cmd,))

    read_thread.start()
    err_thread.start()
    send_thread.start()


    send_thread.join()
