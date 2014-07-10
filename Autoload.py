import sys,imp
from os import path,listdir
class Autoload:
	"""docstring for Autoload
		* change  Libdirectory to global value
	"""
	
	def __init__(self, arg):
		super(Autoload, self).__init__()
		self.arg = arg
		self.loadLibrary(arg)
	
	def loadLibrary(self,DirtoAppend=''):

		Libdirectory = "/library"+DirtoAppend
		DirectoryPath = path
		DirectoryList = listdir("."+Libdirectory)	
		sys.path.insert(0, DirectoryPath.dirname(__file__)+Libdirectory)

		for directory in DirectoryList:
			DirectoryUrl = DirectoryPath.dirname(__file__)+Libdirectory+"/"+directory;
			directory_ = directory.replace(".py","")


			#Delete or fix this
			if '__pycache__'== directory_ :
				continue

			print("trying to load "+directory_)
			#directory
			if DirectoryPath.isdir(DirectoryUrl):
				print(directory_ + "is a directory")
				sys.path.insert(0, DirectoryUrl)
				self.loadLibrary("/"+directory_)

			#not directory
			else:				
				print(directory_ + "is not a directory")
				if imp.find_module(directory_):
					print(directory +" found.")
					fp, pathname, description = imp.find_module(directory_)
					imp.load_module(directory_, fp, pathname, description)
					from directory_ import directory_
					print( directory_ + " loaded.")					
		#	x=__import__('Controller',["*"])
		pass

	def loadModules():

		pass		
