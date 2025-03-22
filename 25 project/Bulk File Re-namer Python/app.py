import os

# 🔹 Yahan apne folder ka path likho
folder_path = r"C:\Users\YourName\Desktop\rename_files"

# 🔹 Yahan apna naya naam pattern likho
new_name = "file"

# Folder me jitni files hain, unko rename karne ka loop
for count, filename in enumerate(os.listdir(folder_path), start=1):
    file_ext = os.path.splitext(filename)[1]  # File ka extension (.txt, .jpg, etc.)
    new_filename = f"{new_name}_{count}{file_ext}"  # Naya naam banayenge
    
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)
    
    os.rename(old_path, new_path)  # File rename karenge

print("✅ All files have been renamed successfully!")
