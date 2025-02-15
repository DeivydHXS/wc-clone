import sys

class WordCount():
    def __init__(self):
        self.args = sys.argv
        self.args_len = len(self.args)
        self.std = sys.stdin
        
        self.available_options = ['-v','-h','-l','-w','-m']
        self.VERSION = 'Word Count Clone v1.0'
        self.HELP =f'''
        {self.VERSION}

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

    def getFile(self, filename, mode = 'rb'):
        text = ''
        try:
            with open(filename, mode) as f:
                text = f.read()
        except:
            print(f'File \'{filename}\' does not exist')
            exit(69)
        return text

    def choose(self, filename='', text='', option=''):
            try:
                # Just for piped data
                text = text.encode('utf-8')
            except:
                pass
            result = []
            match option:
                    case '-c':
                        result.append((len(text)))
                    case '-l':
                        result.append((len(text.splitlines())))
                    case '-w':
                        result.append((len(text.split())))
                    case '-m':
                        result.append((len(text)))
                    case '-v':
                        result.append(self.VERSION)
                    case '-h':
                        result.append(self.HELP)
                    case _:
                        result.append((len(text.splitlines())))
                        result.append((len(text.split())))
                        result.append((len(text)))
            
            if filename:
                result.append(filename)
            
            return ' '.join((str(e) for e in result))

    def isAvailableOption(self, option):
        if option in self.available_options:
            return True

        return False

    def run(self):
        if self.args_len == 1:
            if not self.std.isatty():
                # cat filename | wcc
                return self.choose(text=self.std.read())
            
            print('python main.py -h to help')
            exit(69)

        elif self.args_len == 2:
            if not self.std.isatty():
                # cat filename | wcc -option
                return self.choose(text=self.std.read(), option=self.args[1])
            else:
                filename_or_option = self.args[1]
                if self.isAvailableOption(filename_or_option):
                    # wcc -option
                    return self.choose(option=filename_or_option)

                # wcc filename
                return self.choose(filename=filename_or_option, text=self.getFile(filename_or_option))
        elif self.args_len == 3:
            if not self.std.isatty():
                print('python main.py -h to help')
                exit(69)
            else:
                option = self.args[1]
                filename = self.args[2]
                return self.choose(filename=filename, text=self.getFile(filename), option=option)
