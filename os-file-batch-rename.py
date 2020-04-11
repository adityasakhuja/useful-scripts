# Import os library to parse through directories and files
import os
# Import regex library to search precisely
import re

# Go to the directory you want to sort
os.chdir('/Users/adityasakhuja/Dropbox/Dev/Tools/Video')

report = open('report.txt', 'w')

toReport = 'Working in ' + os.getcwd() + '\n'
report.write(toReport)

# Loop through all the files in the directory
for f in os.listdir():
	# Write your own logic using basic string, regex and file operations
	# In my case, I wanted to take a bunch of asset files named like this:
	# videohive-19903359-modern-parallax-timeline-slideshow-file-and-license.zip
	# and turn it into the format I use to organise my files which looks like this:
	# Video - Modern Parallax Timeline Slideshow.zip
	# You can follow the logic easily as I have broken it down in easy steps

	# Grab all the zip files
	if f.endswith('.zip'):

		toReport = 'Working on file ' + f + '\n'
		report.write(toReport)

		# Split the name from the extension
		f_fullname, f_ext = os.path.splitext(f)

		# Recognise the type of file it is - Video, Audio, Web, etc
		search_type = re.search(r'-', f_fullname)
		f_type = f_fullname[:search_type.start()]
		if f_type == 'videohive':
			f_type = 'Video'

		toReport = 'File is of type: ' + f_type + '\n'
		report.write(toReport)

		# Remove the initial 'videohive-19903359-' part from the name
		search_name = re.search(r'\d-', f_fullname)
		if search_name != None:
			f_name = f_fullname[search_name.end():]
		
		# Remove the latter half containing '-file-and-license'
		search_extras = re.search(r'-file|--file', f_name)
		if search_extras != None:
			f_name = f_name[:search_extras.start()]
		else:
			f_name = f_name

		# Title case for capitalisation of each word
		f_name = str.title(f_name)
		# Remove the hyphens in the name
		f_name = f_name.split('-')
		
		# To create the new file name, I want to,
		# Add the type of file, and then the name separated by a hyphen
		f_newname = f_type + " -"
		# Add all the words in the name separated by single whitespace
		for word in f_name:
			f_newname = f_newname + " " + word
		# Add the extention at the end
		f_newname = f_newname + f_ext
		# Finally, rename the files
		os.rename(f, f_newname)

		toReport = 'File renamed to ' + f_newname + '\n' + '\n'
		report.write(toReport)

report.close()