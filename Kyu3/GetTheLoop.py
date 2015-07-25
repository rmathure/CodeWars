__author__ = 'rohanmathure'


'''
Description:

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.

Image and video hosting by TinyPic
# Use the `next' attribute to get the following node

node.next
'''


def loop_size(node):
    nodePtr1=node
    nodePtr2=node
    cnt=0
    if node is None:
        return cnt
    while True:
        nodePtr1=nodePtr1.next
        nodePtr2=nodePtr2.next.next
        if nodePtr1==nodePtr2:
            break
    nodePtr1=node
    while not nodePtr1==nodePtr2:
        nodePtr1=nodePtr1.next
        nodePtr2=nodePtr2.next
    while True:
        nodePtr2=nodePtr2.next
        cnt+=1
        if nodePtr1 == nodePtr2:
            break
    return cnt

class Node(object):
    next = None
