import sys

arg_list = sys.argv
arg_list_len = len(arg_list)
# print(arg_list)
# print(arg_list_len)

VERSION = 'Word Count Clone v0.2'

HELP =f'''
{VERSION}

Commands:
wcc -v
    Print the version of wcc

wcc -h help
    Print instructions for use wcc

wcc -c 'textfile.ext'
    Print the number of bytes in a file

wcc -l 'textfile.ext'
    Print the number of lines in a file

wcc -m 'textfile.ext'
    Print the number of words in a file

wcc 'textfile.ext'
    Print the number of bytes, lines and words in a file

'''

if arg_list_len > 1:
    if arg_list[1] == '-v':
        print(VERSION)
    elif arg_list[1] == '-h':
        print(HELP)
    elif arg_list[1] == '-c':
        filename = arg_list[2]
        text = ''
        with open(filename, 'rb') as f:
            text = f.read()
        print(len(text), filename)
    elif arg_list[1] == '-l':
        print('Not implemented yet')
    elif arg_list[1] == '-m':
        print('Not implemented yet')
