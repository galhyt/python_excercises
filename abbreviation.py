import numpy as np


def abbreviation(a: str, b: str):
    def __compare__(a: str, b):
        if len(a) < len(b) or len(np.where(a.isupper())) > len(np.where(b.isupper())):
            return False

        if a[0].isupper():
            if a[0] != b[0]:
                return False
            else:
                if len(b) == 1:
                    if len(a) == 1:
                        return True
                    if not a[1:].islower():
                        return False
                    else:
                        return True
                elif len(a) == 1:
                    return False

                return __compare__(a[1:], b[1:])
        else:
            if a[0].upper() != b[0].upper():
                if len(a) == 1:
                    # No more characters in a to match b's
                    return False
                return __compare__(a[1:], b)
            else:
                # First character of each string match
                if len(b) == 1:
                    if len(a) == 1:
                        return True
                    if not a[1:].islower():
                        return __compare__(a[1:], b)
                    else:
                        # We can remove all remaining characters from a
                        return True
                elif len(a) == 1:
                    return False
                return True if __compare__(a[1:], b[1:]) else __compare__(a[1:], b)

    return 'YES' if __compare__(a,b) else 'NO'

# print(abbreviation('bBccC', 'BBC'))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('input1_abbreviation.txt', 'r') as file:
        q = int(file.readline())

        for q_itr in range(q):
            a = file.readline()

            b = file.readline()

            result = abbreviation(a, b)

            print(result + '\n')
