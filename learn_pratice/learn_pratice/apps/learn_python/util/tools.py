
import os

def del_file(path, types, excepts):
	ls = os.listdir(path)
	for i in ls:
		del_path = os.path.join(path, i)
		if os.path.isdir(del_path):
			del_file(del_path, types, excepts)
		else:
			file_type = del_path.split('.')[-1]
			if file_type in types and del_path not in excepts:
				print(del_path)
				os.remove(del_path)


types = ['exe', 'zip']
path = ''
excepts = [
	'',
]
# del_file(path, types, excepts)