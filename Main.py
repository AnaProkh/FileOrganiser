import patoolib
import os
import logging
from send2trash import send2trash

logging.getLogger("patool").setLevel(logging.WARNING)

#path = "C://Users//nasti//Downloads//Telegram Desktop"
path = "C:\\Users\\nasti\\Assets"
zip_list = []

obj = os.scandir(path)

for entry in obj:
    if entry.is_file() and (entry.name.endswith(".zip") or entry.name.endswith(".rar")):
        zip_list.append(entry.path)



print(f"Current directory: {path}\nFound {len(zip_list)} zip files")
user_answer = input("Would you like to unzip all of them? (y/n) ")

if user_answer == "y":
    for file in zip_list:
        target_path = file[:-4]
        patoolib.extract_archive(file, outdir=target_path, verbosity=-1)

    print("All done!")

    user_answer = input("Would you like to clean up the folder and remove any zip files? (y/n) ")
    if user_answer == "y":
        send2trash(zip_list)

