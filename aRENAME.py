import os
folder_path = os.getcwd()
files = os.listdir(folder_path)
for file_name in files:
    new_filename =(file_name.replace("LoginCustomer", os.path.basename(folder_path)))
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_filename))
 
print("XONG")