import difflib
import sys
from common import file
from common import code


def do():
    try:
        textfile1 = 'D:/1.txt'
        textfile2 = 'D:/2.txt'
    except Exception as e:
        print("Error:" + str(2))
        print("Usge: difflib.py file1 file2")
        sys.exit()

    if textfile1 == "" or textfile2 == "":
        print("usege :difflib.py file1 file2")
        sys.exit()
    diff = file.html_diff(textfile1, textfile2)
    print(diff)
    file.write(diff, 'diff.html')

    print(1)

    return 1





