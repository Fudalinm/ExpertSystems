import tkinter as tk
import time
import threading
import random
import queue as Queue
from subprocess import *
import threading
from logging.handlers import *
import time

class GuiPart(tk.Frame):
    def  __init__(self, master, queue, cmd):
        super().__init__(master, width = 500)
        self.grid()
        self.queue = queue
        self.cmd = cmd
        self.create_widgets()

        # Set up the GUI

    def create_widgets(self):
        self.textview = tk.Label(self)
        self.textview["text"] = "text"
        self.textview.grid(row=0, column=0)
        self.yes_button = tk.Button(self, height=1, width=2)
        self.yes_button["text"] = "Tak"
        self.yes_button["command"] = self.sendYes
        self.yes_button.grid(row=1, column=0)

        self.no_button = tk.Button(self, height=1, width=2)
        self.no_button["text"] = "Nie"
        self.no_button["command"] = self.sendNo
        self.no_button.grid(row=1, column=2)
    def sendYes(self):
        send_data(self.cmd,"tak.")
    def sendNo(self):
        send_data(self.cmd,"nie.")
    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize(  ):
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                if (msg not in ['Przycisnij cos aby wyjsc\n',"true.\n","false.\n", "","\n"]):
                    self.textview["text"] = msg
            except Queue.Empty:
                # just on general principles, although we don't
                # expect this branch to be taken in this case
                pass



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

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master

        # Create the queue
        self.queue = Queue.Queue(  )

        # Set up the GUI part

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1

        PROLOG_LOCALIZATION = "swipl"
        FILE_TO_LOAD = "[movie_choser]."
        MAIN_FUNCTION = "wykonaj."

        self.cmd = start_terminal([PROLOG_LOCALIZATION, FILE_TO_LOAD])
        self.gui = GuiPart(master, self.queue, self.cmd)

        send_data(self.cmd, FILE_TO_LOAD)
        send_data(self.cmd, MAIN_FUNCTION)
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()
        # start processes
        # read_thread = threading.Thread(target=read_data, args=(self.cmd,))
        err_thread = threading.Thread(target=read_err, args=(self.cmd,))
        send_thread = threading.Thread(target=send_thr, args=(self.cmd,))

        err_thread.start()
        send_thread.start()
        self.periodicCall(  )

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming(  )
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(200, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """
        while True:
            r = self.cmd.stdout.readline()
            self.queue.put(r)
            print(r)

    def endApplication(self):
        self.running = 0

rand = random.Random(  )
root = tk.Tk(  )

client = ThreadedClient(root)
root.mainloop(  )