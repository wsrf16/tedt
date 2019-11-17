import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "he:p:", ["help", "env=", "port="])
for name, value in opts:
    if name in ("-h", "--help"):
        print("help:正确的使用方法是.......")
    if name in ("-e", "--env"):
        print('env 是:', value)
    if name in ("-p", "--port"):
        print('port 端口是:', value)
