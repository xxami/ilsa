
import sys

class Ilsa():

    def __init__(self):
        pass

    def assembler(self):
        pass


def usage():
    print('useage: ilsa.py file.ils')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        Ilsa(sys.argv).assemble()
    else:
        usage()
