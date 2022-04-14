import sys


def main():
    #...TODO...
    size = int(sys.argv[1])
    print ("FIFO", FIFO(size,pages), "page faults.")
    print ("LRU", LRU(size,pages), "page faults.")
    print ("OPT", OPT(size,pages), "page faults.")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()


def FIFO(size, pages):
    return 0

def LRU(size, pages):
    return 0

def OPT(size, pages):
    return 0