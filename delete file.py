#delete a file

import os
if os.path.exists("filehandling.txt"):
    os.remove("filehandling.txt")
    print("\nFile deleted successfully.")
else:
    print("\nFile not found.")