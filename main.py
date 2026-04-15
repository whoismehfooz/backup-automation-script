import shutil
import datetime


source = input('Enter folder path to backup: ')
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
destination = f'backups/backup_copy_{timestamp}'

shutil.copytree(source,destination)


print('Backup created Successfully....💞')
print(f'File saved at: {destination}')