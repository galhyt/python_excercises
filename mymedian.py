import pandas as pd

def median_val(arr):
    ser = pd.Series(arr)
    expectedval = ser.median()

    medianval = None
    last_numberoccr = None
    medianoccr = int(len(ser)/2)
    for i in range(len(ser)):
        if medianval != None:
            if ser[i] < medianval:
                if last_numberoccr > medianoccr:
                    continue
            elif ser[i] > medianval:
                if last_numberoccr < medianoccr:
                    continue
            else:
                continue

        medianval = ser[i]
        last_numberoccr = len(ser[medianval < ser])
        if last_numberoccr == medianoccr:
            break

    
    return "result: %s  expected: %s" % (medianval, expectedval)