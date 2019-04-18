import fcntl
import sys
import termios
import os

def simulate_terminal(t,cmd):


    with open(t, 'w') as fd:
        for c in (cmd+'\n'):
            fcntl.ioctl(fd, termios.TIOCSTI, c)   # the TIOCSTI ioctl call simulates input, it inserts the command as bytes into the input queue of the terminal http://man7.org/linux/man-pages/man4/tty_ioctl.4.html


