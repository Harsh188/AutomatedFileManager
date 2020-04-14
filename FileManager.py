'''
Project Name: Automated File Manager
Author: Harshith MohanKumar
Date: 4/11/2020
Description: This project aims to automate the process of organizing files which are downloaded
	from the internet.
'''

import os
from pathlib import Path
from datetime import datetime

DIRECTORIES = {
		"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp"],
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd"],
        "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  ".pptx"],
        "PDF": [".pdf"],
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
        "OTHER": [".html5", ".html", ".htm", ".xhtml", ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                 ".dmg", ".rar", ".xar", ".zip", ".py", ".xml", ".exe", ".sh"]
}

def cleanUp(path):
	'''
	This method cleans up the downloads folder by removing old files.
	Parameter: string directory path
	Return: None
	'''
	
	# First lets make sure that we are in the correct directory
	os.chdir(path)
	# Scan all of the documents in the current directory
	file = os.scandir(path)
	print('\n')
	# Loop through all the documents
	for f in file:
		print(f.name)
		# If the file is a directory then recursively call cleanUp
		if (f.is_dir()):
			cleanUp(f.path)
		# Otherwise perform operations to check how old the file is
		else:
			# Get the timestamp of the file
			timestamp = os.path.getmtime(f.path)
			# Get the datetime of the current time period
			cur_dt_obj = datetime.now()
			# Get the datetime of the file
			dt_obj = datetime.fromtimestamp(timestamp)
			# Compute the difference in time
			timeDiff = cur_dt_obj-dt_obj
			if(timeDiff.days>15):
				os.remove(f.name)
				print("File Removed!")


def renameFile(dir,ext):
	'''
	This is a helper function which will rename the file numerically according
	to the number of existing files in directory.
	Parameter: String directory name
	Return: String file name
	'''
	os.chdir('/Users/harshithmohankumar/Downloads/'+dir)
	file = [f for f in os.scandir() if f.is_file()]
	print(len(file))
	return 'File#'+str(len(file))+ext

def get_key(val):
	'''
	This is a helper function which returns the keyvalue of a dictionary which 
	contains the value passed in.
	Parameters: String value [dictonary item]
	Return: String key [dictonary key]
	'''
	for key, value in DIRECTORIES.items():
		if val in value:
			return key 
	return "OTHER"

def fileManager():
	""" 
	This method organizes all of the files in the download folder.
	Return: None
	Parameters: None 
	"""

	# First we change the working directory to the Downloads folder
	downloadsPath = '/Users/harshithmohankumar/Downloads'
	os.chdir(downloadsPath)
	# Next we will get all of the files in the directory to organize
	file = [f for f in os.scandir() if f.is_file()]
	# Now loop through all the files and organize them
	for f in file:
		fileName = f.name
		# Obtain the extension of the file
		i = fileName.rfind('.')
		ext = fileName[i:].lower()
		# Match the extension to the according directory
		toFile = get_key(ext)
		# Now move the file to that directory
		if Path(toFile).exists():
			full_path = os.path.join(downloadsPath,fileName)
			fileName = renameFile(toFile,ext)
			os.chdir(downloadsPath)
			to_path = os.path.join(downloadsPath,toFile,fileName)
			os.rename(full_path,to_path)

if __name__ == '__main__':
	cleanUp('/Users/harshithmohankumar/Downloads')
	# fileManager()
