##Goal of the project
##Modify the file to append ; print("Virus") at line52
##Read the docx for more info

def modify_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    #Didnt add a check for this because only 1 case
    lines[51] = lines[51].rstrip('\n') + '; print("Virus")\n'

    with open(filename, 'w') as file:
        file.writelines(lines)

if __name__ == '__main__':
    modify_file('sfs.py')
