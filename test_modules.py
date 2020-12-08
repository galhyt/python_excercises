import sys

def main():
    if len(sys.argv) == 1:
        print("No arguments sent. Exit!")
        return
    
    option = sys.argv[1] 
    arrindex = 2
    func = None

    if option == "--median":
        from mymedian import median_val as func
    elif option == "--qsort":
        from myqsort import qsort as func

    if func== None:
        return

    print(func([int(i) for i in sys.argv[arrindex:]]))

if __name__ == '__main__':
    main()
