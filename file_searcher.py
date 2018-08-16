import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:e:s:f:h',
        ['input', 'exclude', 'start', 'finish', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-i', '--input'):
        input_file = arg
    elif opt in ('-e', '--exclude'):
        exclude = arg
    elif opt in ('-s', '--start'):
        start_date = arg
    elif opt in ('-f', '--finish'):
        finish_date = arg
    else:
        usage()
        sys.exit(2)

print("%s %s %s %s" % (input_file, exclude, start_date, finish_date))