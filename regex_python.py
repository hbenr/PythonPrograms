"""Extracting numbers from text file.

Two line version of this program:
import re
print sum([int(num) for num in re.findall('[0-9]+', open('regex_sum_206625.txt', 'r').read())])
"""
import re

def main():
    """Main function."""

    with open('regex_sum_206625.txt', 'r') as file_handler:
        temp_lst = re.findall('[0-9]+', file_handler.read())  
        print sum([int(num) for num in temp_lst])

if __name__ == '__main__':
    main()
