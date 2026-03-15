#4 Copy and back up files using shutil
#5 Delete files safely
import shutil
shutil.copy("text.txt", "firstcopy.txt")

import os
os.remove("firstcopy.txt")





