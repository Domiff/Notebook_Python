import os


class Directory:    
    
    def make_directory(self, name_path):
        if not os.path.exists(name_path):
            return os.makedirs(name_path)
