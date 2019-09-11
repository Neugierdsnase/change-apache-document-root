from sys import argv
from os import fdopen, remove
from tempfile import mkstemp
from shutil import move
import subprocess

from config import apache_config_file_path

new_folder = argv[1]

# Create temp file
fh, abs_path = mkstemp()
with fdopen(fh, "w") as new_file:
    with open(apache_config_file_path) as old_file:
        for line in old_file:
            if not "DocumentRoot" in line:
                new_file.write(line)
            else:
                new_file.write(f"\tDocumentRoot /var/www/{new_folder}/\n")
# Remove original file
remove(apache_config_file_path)
# Move new file
move(abs_path, apache_config_file_path)

subprocess.run(["sudo", "systemctl", "restart", "apache2.service"])
