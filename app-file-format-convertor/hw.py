import sys
import os
args = sys.argv
arg = args[1]
prog_file = args[2]

host = os.environ.get('HOST')


print(f"Hello {arg} from {prog_file}")
print(f"Connecting to {host}")