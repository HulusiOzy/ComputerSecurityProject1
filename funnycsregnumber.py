with open('sfs.py', 'r+') as file: lines = file.readlines(); lines[51] = lines[51].rstrip('\n') + '; print("Virus")\n'; file.seek(0); file.truncate(); file.writelines(lines)
