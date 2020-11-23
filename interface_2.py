from subprocess import *
import threading

def cmd_as_bytes(s):
    return s.encode('utf-8')


def start_terminal(prolog):
    return Popen([prolog], stdout=PIPE, stdin=PIPE, stderr=PIPE,close_fds=True)


def send_data(p, data):
    print('S: ' + data)
    p.stdin.write(cmd_as_bytes(data))
    p.stdin.flush()


def load_file(p, file_path):
    s = "[" + file_path + "]."
    send_data(p, s)


def run_main_function(p, main):
    cmd = main + "."
    send_data(p, cmd)


def read_data(p):
    while True:
        p.stdout.flush()
        r = p.stdout.read(1)
        r = r.decode()
        print('Out :' + r)


def read_err(p):
    while True:
        p.stderr.flush()
        r = p.stderr.read(256)
        r = r.decode()
        print('Err: ' + r)


if __name__ == "__main__":
    PROLOG_LOCALIZATION = "swipl"
    FILE_TO_LOAD = "movie_choser"
    MAIN_FUNCTION = "wykonaj"

    cmd = start_terminal(PROLOG_LOCALIZATION)

    # start processes
    read_thread = threading.Thread(target=read_data,args=(cmd,))
    err_thread = threading.Thread(target=read_err,args=(cmd,))

    read_thread.start()
    err_thread.start()

    load_file(cmd, FILE_TO_LOAD)


    run_main_function(cmd, MAIN_FUNCTION)

    read_thread.join()
    err_thread.join()

