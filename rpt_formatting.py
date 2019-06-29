import re
import string

def reformat_file(original_file, file_copy):
    with open(original_file, 'r') as rf:
        with open(file_copy, 'r+') as wf:
            #for line in rf:
            #   wf.write(line)

            for line in rf:
                if '&' in line:
                    #splits all items by comma
                    full_item = line.split(',')

                    #splits items within comma, just gives 'first name'
                    first_name_only = [i.split('_')[0] for i in full_item]

                    #splits items within comma, just gives 'full name'
                    full_name_only = [i.split('(')[0] for i in full_item]

                    #splits items within comma, just gives value in parentheses
                    parenth_value = [i.split('(')[-1].split(')')[0] for i in full_item]
                    print(parenth_value)

                if '*' in line:
                    #splits all items from line 6 since line 6 starts with a '*'
                    value_items = line.split(',')

                    #put together each respective item from each respective list
                    for fname, parenth, full, value in zip(first_name_only, parenth_value, full_name_only, value_items):
                        wf.write('{0},{1},{2},{3}\n'.format(fname, parenth, full, value))

def main():
    original_file = '/dir/file.rpt' #path of original file
    
    file_copy = '/dir/file_copy.rpt' #path of copy file

    reformat_file(original_file, file_copy)
    
if __name__ == '__main__':
    main()    