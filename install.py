import os
import glob
import shutil

original_directory = os.path.dirname(os.path.realpath(__file__))
apcupsd_directory = '/etc/apcupsd'
backup_scripts_directory = 'backup_scripts'

# Create folder to save original scripts
backup_directory = '{}/{}'.format(apcupsd_directory, backup_scripts_directory)
if not os.path.exists(backup_directory):
    os.mkdir(backup_directory)

# Backup all existing scripts in apcupsd directory
for script in glob.glob('{}/scripts/*'.format(original_directory)):
    script_directory = '{}/{}'.format(apcupsd_directory, script)
    if os.path.exists(script_directory):
        shutil.move(script_directory, '{}/{}'.format(backup_scripts_directory, script))

# If backup directory is empty, delete it
if len(os.listdir(backup_directory)) == 0:
    os.rmdir(backup_directory)

# Move all scripts from scripts directory to apcupsd directory
for script in glob.glob('{}/scripts/*'.format(original_directory)):
    shutil.move(script, apcupsd_directory)
