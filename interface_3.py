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
    def __init__(self, master, queue, cmd):
        self.scale = 2
        master.minsize(width=650 * self.scale, height=100 * self.scale)
        master.maxsize(width=650 * self.scale, height=100 * self.scale)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        super().__init__(master, width=650 * self.scale)
        self.grid()
        self.grid_columnconfigure(0, weight=1)
        self.queue = queue
        self.cmd = cmd
        self.create_widgets()

        # Set up the GUI

    def create_widgets(self):
        f_textviw = ('Courier', self.scale * 15, 'bold')
        f_button = (f_textviw[0], int(f_textviw[1] / 2), 'bold')
        self.textview = tk.Label(self, font=f_textviw,width=21*self.scale)
        self.textview["text"] = "text"
        self.textview.grid(row=0, column=1)

        self.yes_button = tk.Button(self, height=self.scale * 1, width=self.scale * 4)
        self.yes_button["text"] = "Tak"
        self.yes_button['font'] = f_button
        self.yes_button["command"] = self.sendYes
        self.yes_button.grid(row=1, column=0)

        self.no_button = tk.Button(self, height=self.scale * 1, width=self.scale * 4)
        self.no_button["text"] = "Nie"
        self.no_button['font'] = f_button
        self.no_button["command"] = self.sendNo
        self.no_button.grid(row=1, column=2)

        self.restart_button = tk.Button(self, height=self.scale * 1, width=self.scale * 8)
        self.restart_button["text"] = "Restart"
        self.restart_button['font'] = f_button
        self.restart_button["command"] = self.restart
        self.restart_button.grid(row=1, column=1)
        self.restart_button["state"] = tk.DISABLED

    def sendYes(self):
        send_data(self.cmd, "tak.")

    def sendNo(self):
        send_data(self.cmd, "nie.")

    def restart(self):
        self.no_button['state'] = tk.NORMAL
        self.yes_button['state'] = tk.NORMAL
        self.restart_button['state'] = tk.DISABLED
        self.textview.config(fg='BLACK')
        send_data(self.cmd, "wykonaj.")

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple test, print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                msg = msg.replace('_', ' ')
                if msg not in ['Przycisnij cos aby wyjsc\n', "true.\n", "false.\n", "", "\n"]:
                    msg = msg.replace(' (t/n)', '')
                    msg = msg[0].upper() + msg[1:]
                    self.textview["text"] = msg
                if "Polecanym filmem moze byc" in msg or "Nie jestem w stanie poleci" in msg:
                    self.no_button['state'] = tk.DISABLED
                    self.yes_button['state'] = tk.DISABLED
                    self.restart_button['state'] = tk.NORMAL


                    if "Polecanym filmem moze byc" in msg:
                        self.textview.config(fg='GREEN')
                        # change color to green
                    else:
                        self.textview.config(fg='RED')
                        # change color to red

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
        self.queue = Queue.Queue()

        # Set up the GUI part

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1

        PROLOG_LOCALIZATION = "swipl"
        FILE_TO_LOAD = "movie_choser.pl"
        MAIN_FUNCTION = "wykonaj."

        self.cmd = start_terminal([PROLOG_LOCALIZATION, FILE_TO_LOAD])
        self.gui = GuiPart(master, self.queue, self.cmd)

        # send_data(self.cmd, FILE_TO_LOAD) # you DO NOT NEED to do this (you should not) look at start terminal it already loads file
        send_data(self.cmd, MAIN_FUNCTION)
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()
        # start processes
        # read_thread = threading.Thread(target=read_data, args=(self.cmd,))
        err_thread = threading.Thread(target=read_err, args=(self.cmd,))
        send_thread = threading.Thread(target=send_thr, args=(self.cmd,))

        err_thread.start()
        send_thread.start()
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
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


rand = random.Random()
root = tk.Tk()

client = ThreadedClient(root)
root.mainloop()
