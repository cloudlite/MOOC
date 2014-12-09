__author__ = 'cloudlite'

# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which
# should be 10
#
# Your test function should run assertion checks and throw an
# AssertionError for each of the 5 incorrect Queues. Pressing
# submit will tell you how many you successfully catch so far.


# from queue_test import *
import Queue


class my_queue:
    def __init__(self, maxsize):
        self.queue = Queue.Queue(maxsize)

    def enqueue(self, val):
        try:
            self.queue.put(val)
            return True
        except Queue.Full:
            return False

    def dequeue(self):
        if not self.empty():
            return self.queue.get()
        else:
            return None

    def empty(self):
        return self.queue.empty()

    def full(self):
        return self.queue.full()


def test():
    ###Your code here.
    q = Queue(1)

    is_empty = q.empty()
    assert is_empty

    succeeded = q.enqueue(10)
    assert succeeded

    fail_enqueue = q.enqueue(2)
    assert fail_enqueue == False

    is_full = q.full()
    assert is_full

    is_empty = q.empty()
    assert is_empty == False

    value = q.dequeue()
    assert value == 10

    is_full = q.full()
    assert is_full == False

    fail_dequeue = q.dequeue()
    assert fail_dequeue is None

    is_empty = q.empty()
    assert is_empty == False


def test2():
    # works for 15, but not 16
    b = Queue(16)
    for i in range(16):
        p = b.enqueue(i)
        assert p

    # finds one bug
    q = Queue(1)
    value = q.dequeue()
    assert value == None

    #gets 3 bugs
    s = q.enqueue(-1)
    is_empty = q.empty()
    value = q.dequeue()
    assert value == -1


test()