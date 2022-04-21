"""
Talifhani Mulaudzi
MLDTAL001

CSC3002F - OS1 Assignment
"""


from random import randint
import sys
from queue import Queue
from collections import deque
from operator import itemgetter
import pandas as pd


# A method for determining the number of page faults using the FIFO page replacement algorithm
def FIFO(size, pages):
    
    """
    Check if the current page is in the set or not
    A python set is used to store the pages that are currently in memory.
    """
    s = set()
    """
    Python Queue works in a FIFO maner, therefore it's used to store 
    the pages in order of insertion into memory.
    """
    queue = Queue()
    page_faults = 0 # Variable to store all the page faults in FIFO
    for i in range(len(pages)): #loop through each page
       # If there are fewer items in the set than the frame size
        if len(s) < size: # if the set is not full
            # If the current page is not present in the set
            if pages[i] not in s:
                s.add(pages[i]) #add it to the set and increment the page faults variable.
                page_faults += 1
                queue.put(pages[i]) #Store the current page in the queue
        
        #If there is no space in the set, apply page replacement
        # using FIFO by removing the first element from the queue an from the set 
        else:
            # If the current page not present
            if pages[i] not in s:
                #Delete the first page
                first = queue.queue[0]
                queue.get()
                s.remove(first) # Delete from the set
                s.add(pages[i]) # put the current page into the set
                queue.put(pages[i])  # put the current page into the queue
                page_faults += 1 # increment faults

    return page_faults #return the FIFO page faults



"""
A method for determining the number of page 
faults using the LRU page replacement algorithm
"""
def LRU(size, pages):

    n = len(pages) #Number of frames

    # "-1" is used to represent an empty frame
    frame = ["-1"]*size 
    time_used = [0]*size
    time = 0
    #store the pages_in_frame
    pages_in_frame = pd.DataFrame(index=range(0,size))
    page_faults = 0    
    for i in range(0,n): # loop through all pages.
        if (frame.count("-1") > 0): # Check if there are pages in the frame.
            #Put the current page into the set  
            if (pages[i] not in frame): # If page not in memory
                frame[frame.index("-1")] = pages[i]
                page_faults += 1
                pages_in_frame[time] = frame 
        # If frame is full, apply page replacement using LRU algorithm.
        else: 
            if (pages[i] not in frame): # determine if the current page is not present in the set.   
                index = max(enumerate(time_used), key=itemgetter(1))[0]
                frame[index] = pages[i] # Replace the least recently used page with the current page.
                time_used[index] = 0
                page_faults += 1 # Increment faults
               # pages_in_frame[time] = frame # insert into the frame
            else:
                time_used[frame.index(pages[i])] = 0
               
        time_used = [t+170 for t in time_used]
        time += 1
    return page_faults


# A method for determining the number of page faults using the Optimal page replacement algorithm
def OPT(size, pages):

    n = len(pages) # Frame size
    # "-1" is used to represent an empty frame
    frame = ["-1"]*size 
    queue = deque() # store all pages in a queue

    for page in pages:
        queue.append(page) # Add each page into the creted queue

    time = 0
    #store the pages_in_frame
    pages_in_frame = pd.DataFrame(index=range(0,size)) 
    page_faults = 0 # Variable to hold the page faults
    for i in range(0,n): # loop through all pages.
        if (frame.count("-1") > 0): # Check if there are pages in the frame.
             #Put the current page into the set 
            if (pages[i] not in frame): 
                frame[frame.index("-1")] = pages[i]
                page_faults += 1
                pages_in_frame[time] = frame

        # If frame is full, apply page replacement using the OPT algorithm.
        else: 
            if (pages[i] not in frame):  # determine if the current page is not present in the set. 
                time_to_use = [1000]*size
                for j in range(len(frame)):
                    if frame[j] in queue:
                        time_to_use[j] = queue.index(frame[j])
                index = max(enumerate(time_to_use), key=itemgetter(1))[0]
                frame[index] = pages[i] # Replace the least recently used page with the current page.
                page_faults += 1  # Increment faults
                
        time += 1
        queue.popleft()
    return page_faults
    #print("Faults = "+ str(page_faults))

def main():
    #...TODO...
    size = int(sys.argv[1]) # get the frame size from the first parameter.
    # pages = "85625354235326256856234213754315"
    pages = ""
    for i in range(32): #generate 32 random numbers from 0 to 9 inclusively
        pages += str(randint(0,9)) # Add the random numbers to the pages string.

    # print(pages)

    print ("FIFO", FIFO(size,pages), "page faults.") #Print the page faults for FIFO
    print ("LRU", LRU(size,pages), "page faults.")  #Print the page faults for LRU
    print ("OPT", OPT(size,pages), "page faults.")  #Print the page faults for OPT
if __name__ == "__main__":
    if len(sys.argv) != 2: # Check if there are 2 parameters
        print("Usage: python paging.py [number of pages]") 
    else:
        main()