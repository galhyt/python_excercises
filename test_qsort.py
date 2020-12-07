import sys
from myqsort import qsort as quicksort

def main():
    print(sys.argv)
    print(quicksort([int(i) for i in sys.argv[1:]]))

if __name__ == '__main__':
    main()