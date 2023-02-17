import os

def format_filename(cur_hour_minute):
	t = cur_hour_minute.replace(" ", "_")
	return t + ".json"

def format_path(filename, directory_name):
	# dirname will get the parent directory.  There are two here since we have to go to backend/ instead of just utils/
	# https://stackoverflow.com/questions/2817264/how-to-get-the-parent-dir-location
	dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	dir_path += "/" + directory_name
	# Create the file directories if they don't exist

	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
		
	return dir_path + "/" + filename
