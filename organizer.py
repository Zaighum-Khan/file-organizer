import os
import shutil 

def get_extension(fileName):
    result = os.path.splitext(fileName)
    return result[1].lower()

def get_files(folder):
    return os.listdir(folder)

def get_destination(ext):
    if ext in ['.pdf' , '.docx' , '.txt']:
        dest = 'Documents'
    elif ext in ['.jpg' , '.png' , '.gif']:
        dest = 'Images'
    elif ext in ['.mp4' , '.mov' , '.mkv' , '.avi']:
        dest = 'Videos'
    elif ext in ['.mp3' , '.wav' , '.ogg' , '.m4a']:
        dest = 'Audios'
    elif ext in ['.zip' , '.rar']:
        dest = 'Archives'
    else:
        dest = 'Others'
    return dest

def move_file(file, dest):
    os.makedirs(dest, exist_ok=True)
    shutil.move(file, dest)
    print('Successful Action!')
    
def organize(folder):
    files = get_files(folder)
    
    for file in files:
        if not os.path.isfile(os.path.join(folder , file)) or file == os.path.basename(__file__):
            continue
        ext = get_extension(file)
        dest = get_destination(ext)
        move_file(os.path.join(folder , file) , os.path.join(folder , dest))
        
    print('Organization Successful!')
    
    
def main_menu():
    while True:
        service = input('1. Organize Folder\n2. Exit\n Enter your choice: ')
        if service == '1':
            while True:
                folder = input('Enter Folder Path (or Enter 0 to go back): ')
                if folder == '0':
                    break
                else:
                    confirm = input('Do you want to proceed with this Folder? (Y for yes): ').lower()
                    if confirm == 'y':
                        organize(folder)
                        os.system('clear')
                        break
                    else:
                        continue
        elif service == '2':
            print('GoodBye!')
            return
        else:
            print('Invalid Input! Exiting...')
            return
        
main_menu()