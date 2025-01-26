import sys

arg_list = sys.argv
arg_list_len = len(arg_list)

VERSION = 'Word Count Clone v0.3'

HELP =f'''
{VERSION}

Commands:
wcc -v
    Print the version of wcc

wcc -h help
    Print instructions for use wcc

wcc 'textfile.ext'
    Print the number of bytes, lines and words in a file

wcc -c 'textfile.ext'
    Print the number of bytes in a file

wcc -l 'textfile.ext'
    Print the number of lines in a file

wcc -m 'textfile.ext'
    Print the number of words in a file

'''

if arg_list_len < 2 or arg_list_len > 3:
    print('wcc -h to help')
elif arg_list_len == 2:
    match arg_list[1]:
        case '-v':
            print(VERSION)
        case '-h':
            print(HELP)
        case _:
            print('Not implemented yet')
else:
    match arg_list[1]:
        case '-c':
            filename = arg_list[2]
            text = ''
            with open(filename, 'rb') as f:
                text = f.read()
            print(len(text), filename)
        case '-l':
            filename = arg_list[2]
            text = ''
            with open(filename, 'r') as f:
                text = f.read()
            print(len(text.splitlines()), filename)
        case '-m':
            print('Not implemented yet')
        case _:
            print('Not implemented yet')                