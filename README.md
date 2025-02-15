# Word Count Clone
A simple word count clone 

# How to use

Word Count Clone v0.6

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

You can also use something like cat program to pass data to the program, like the following:

cat textfile.ext | python main.py