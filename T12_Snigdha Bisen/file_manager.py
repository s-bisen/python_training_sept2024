import os
import shutil #module used for file operations like copy


class FileManager:
    # Displays all files in current directory
    def list_files(self):
        return [f for f in os.listdir('.') if os.path.isfile(f)]

    # Displaying all directories
    def list_dirs(self):

        return [d for d in os.listdir('.') if os.path.isdir(d)]

    # Display content of file
    def cat_file(self, filename):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error occured while reading file: {e}"

    def head_file(self, filename, lines=5):
        
        try:
            with open(filename, 'r') as f:
                return ''.join(f.readlines()[:lines])
        except Exception as e:
            return f"Error occured while reading file: {e}"

    def tail_file(self, filename, lines=5):
        
        try:
            with open(filename, 'r') as f:
                return ''.join(f.readlines()[-lines:])
        except Exception as e:
            return f"Error occured while reading file: {e}"

    def copy_file(self, src, dest):
        
        try:
            shutil.copy(src, dest)
            return f"Copied {src} to {dest}."
        except Exception as e:
            return f"Error occured while copying file: {e}"

    def remove_file(self, filename):
        
        try:
            os.remove(filename)
            return f"Removed file {filename}."
        except Exception as e:
            return f"Error occured while removing file: {e}"

    def empty_file(self, filename):
        
        try:
            open(filename, 'w').close()
            return f"Truncated file {filename}."
        except Exception as e:
            return f"Error occured while emptying file: {e}"
