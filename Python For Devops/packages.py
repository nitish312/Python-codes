import os, shutil

print(os.getcwd())

total, used, free = shutil.disk_usage("/")

print(f"Total Disk Space is {total // (2**30)} GBs")
print(f"Used Disk Space is {used // (2**30)} GBs")
print(f"Free Disk Space is {free // (2**30)} GBs")