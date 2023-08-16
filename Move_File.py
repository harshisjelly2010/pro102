import os
import shutil

source = "sourec"
destination = "C:/Users/harsh/OneDrive/Desktop/Harsh/byjus future school/Document_Files"

list_of_files = os.listdir(source)
print(list_of_files)

for i in list_of_files:
  file1 ,extension =   os.path.splitext(i)


  if extension in ['.txt', '.pdf', '.doc', '.docx']:
    path1 = source + "/" + i
    path2 = destination + "/" + "Document_Folder"
    path3 = destination + "/" + "Document_Folder" + "/" + i

    if os.path.exists(path2):
      # Move from path1 ---> path3
      shutil.move(path1, path3)

    else:
      os.makedirs(path2)
      shutil.move(path1, path3)