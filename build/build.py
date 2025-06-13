"""Python file to convert project into a exe"""

import os
import sys
try:
    os.system("auto-py-to-exe")
except:
    os.system("pip install auto-py-to-exe")
    os.system("auto-py-to-exe")
