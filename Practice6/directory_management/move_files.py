import shutil

# copy file
shutil.copy("test.txt", "ata-ana/test_copy.txt")

# move file
shutil.move("test.txt", "ata-ana/test_moved.txt")

print("Copy and move completed")