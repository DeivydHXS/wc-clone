import sys

arg_list = sys.argv
arg_list_len = len(arg_list)

VERSION = 'Word Count Clone v0.5'

HELP =f'''
{VERSION}

Commands:
python main.py -v
    Print the version of wcc

python main.py -h help
    Print instructions for use wcc

python main.py 'textfile.ext'
    Print the number of bytes, lines and words in a file

python main.py -c 'textfile.ext'
    Print the number of bytes in a file

python main.py -l 'textfile.ext'
    Print the number of lines in a file

python main.py -w 'textfile.ext'
    Print the number of words in a file

python main.py -m 'textfile.ext'
    Print the number of characters in a file

'''

def getFile(filename, mode = 'rb'):
    text = ''
    try:
        with open(filename, mode) as f:
            text = f.read()
    except:
        print(f'File \'{filename}\' does not exist')
        exit()
    return text

if arg_list_len < 2 or arg_list_len > 3:
    print('wcc -h to help')
elif arg_list_len == 2:
    match arg_list[1]:
        case '-v':
            print(VERSION)
        case '-h':
            print(HELP)
        case _:
            filename = arg_list[1]
            btext = getFile(filename)
            text = btext.decode("utf-8")
            print(len(text.splitlines()), len(text.split()), len(btext), filename)
else:
    filename = arg_list[2]
    match arg_list[1]:
        case '-c':
            btext = getFile(filename)
            print(len(btext), filename)
        case '-l':
            btext = getFile(filename)
            text = btext.decode("utf-8")
            print(len(text.splitlines()), filename)
        case '-w':
            btext = getFile(filename)
            text = btext.decode("utf-8")
            print(len(text.split()), filename)
        case '-m':
            btext = getFile(filename)
            text = btext.decode("utf-8")
            print(len(text), filename)
        case _:
            print('wcc -h to help')