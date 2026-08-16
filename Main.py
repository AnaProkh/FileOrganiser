import patoolib
import os
import logging
from send2trash import send2trash, TrashPermissionError

logging.getLogger("patool").setLevel(logging.WARNING)

#path = "C://Users//nasti//Downloads//Telegram Desktop"
path = "C:\\Users\\nasti\\Assets\\"
zip_list = []

try:
    obj = os.scandir(path)
except FileNotFoundError:
    print("The specified directory does not exist.")
    exit()
except PermissionError:
    print("You don't have permission to access this directory.")
    exit()

for entry in obj:
    if entry.is_file() and (entry.name.endswith(".zip") or entry.name.endswith(".rar")):
        zip_list.append(entry.name)

if len(zip_list) == 0:
    print("No zip files found in this directory.")
    exit()


print(f"Current directory: {path}\nFound {len(zip_list)} zip files")
user_answer = input("Would you like to unzip all of them? (y/n) ")

if user_answer == "y":
    for file in zip_list:
        target_path = path+file[:-4]
        patoolib.extract_archive(path+file, outdir=target_path, verbosity=-1)

    print("All done!")

    user_answer = input("Would you like to clean up the folder and remove any zip files? (y/n) ")
    if user_answer == "y":
        for file in zip_list:
            try:
                send2trash(path+file)
            except TrashPermissionError as e:
                print(f"Could not remove {file}: {e}")
            except OSError as e:
                print(f"Could not remove {file}: {e}")

