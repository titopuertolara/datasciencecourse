import shutil
import os

path='/home/andres/Downloads/images_dms/ImageAssistant_Batch_Image_Downloader/www.google.com/drowsiness_driver_-_Búsqueda_de_Google'

file_list=os.listdir(path)

for f in file_list:
	
	name=f.split('.')[0]
	ext=f.split('.')[1]
	new_name=name+'_driver.'+ext
	os.rename(path+'/'+f,path+'/'+new_name)
	print(path+'/'+f,path+'/'+new_name)
	
