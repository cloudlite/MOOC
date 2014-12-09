__author__ = 'cloudlite'
# !/usr/bin/env python
# Simple debugger
# See instructions around lines 36

import sys
import readline

# Our buggy program
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out


# main program that runs the buggy program
def main():
    print remove_html_markup('xyz')
    print remove_html_markup('"<b>foo</b>"')
    print remove_html_markup("'<b>foo</b>'")

# globals
breakpoints = {14: True}
watchpoints = {'c': True}
stepping = False

"""
Our debug function
Improve and expand the debug function to accept a new command:
a delete command 'd <type> <argument>', where <type> is either b for breakpoint,
or w for watchpoint. The following argument should be either a number
for the breakpoint or a string for the watchpoint.
If there is mismatch between type and argument, you should print out
"Incorrect command".
In the case of "d b <argument>" you should delete that breakpoint from the
breakpoint dictionary, or print "No such breakpoint defined", repr(argument)
In case of watchpoint, you should delete the watchpoint if such variable exists,
or print: variable, "is not defined as watchpoint"
"""


def debug(command, my_locals):
    global stepping
    global breakpoints
    global watchpoints

    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None

    if command.startswith('s'):  # step
        stepping = True
        return True
    elif command.startswith('c'):  # continue
        stepping = False
        return True
    elif command.startswith('p'):  # print
        if not arg:
            print my_locals
        else:
            if my_locals.has_key(arg):
                var = repr(my_locals[arg])
                print arg + ' = ' + var
            else:
                print 'No such variable:', arg
    elif command.startswith('b'):  # breakpoint
        if arg and arg.isdigit():
            breakpoints[int(arg)] = True
        else:
            print 'You must supply a line number'
    elif command.startswith('w'):  # watch variable
        if arg:
            watchpoints[arg] = True
        else:
            print 'You must supply a variable name'
    elif command.startswith('d'):  # delete watch/break point
        # YOUR CODE HERE
        if not arg:
            print 'Incorrect command'
        else:
            args = command.split(' ')
            if len(args) != 3:
                print 'Incorrect command'
            else:
                if args[1] == 'b':
                    if breakpoints.has_key(int(args[2])):
                        del breakpoints[int(args[2])]
                        print 'Breakpoint', repr(args[2]), 'deleted'
                    else:
                        print 'No such breakpoint defined', repr(args[2])
                elif args[1] == 'w':
                    if watchpoints.has_key(args[2]):
                        del watchpoints[args[2]]
                        print 'Watchpoint', repr(args[2]), 'deleted'
                    else:
                        print repr(args[2]), "is not defined as watchpoint"

    elif command.startswith('q'):  # quit
        print "Exiting my-spyder..."
        sys.exit(0)
    else:
        print "No such command", repr(command)

    return False


commands = ["w out", "d w out", "w out", "b 12", "b", "d b 14", "b", "q"]


def input_command():
    # command = raw_input("(my-spyder) ")
    global commands
    command = commands.pop(0)
    return command


"""
Our traceit function
"""


def traceit(frame, event, trace_arg):
    global stepping

    if event == 'line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
            while not resume:
                command = input_command()
                resume = debug(command, frame.f_locals)
    return traceit

# Using the tracer
# sys.settrace(traceit)
# main()
#sys.settrace(None)

#Simple test
watchpoints = {'s': True}
print watchpoints
debug("d w s", {'s': 'xyz', 'tag': False})
print watchpoints
breakpoints = {8: True, 12: True, 20: True}
print breakpoints
debug("d b 12", {'s': 'xyz', 'tag': False})
print breakpoints
