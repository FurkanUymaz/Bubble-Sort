from ds import *

def bubble_sort( theSeq ):
    if(isinstance(theSeq, list)):
        n = len( theSeq )
        for i in range( n - 1 ):
            for j in range( n-(i+1) ):
                if (theSeq[j] > theSeq[j + 1]):
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
            #print(theSeq)
        return theSeq

    
    
    elif isinstance(theSeq, LinkedList):
            if theSeq.num_items < 2:
                return theSeq  

            for i in range(theSeq.num_items - 1):
                node = theSeq.head
                while node and node.next:
                    if node.data > node.next.data:
                        temp = node.data
                        node.data = node.next.data
                        node.next.data = temp
                    node = node.next
            return theSeq
