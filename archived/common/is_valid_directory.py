from os import path

# Check if a directory exists and if it's valid
def is_valid_directory(directory):
  if not path.exists(directory): # If the directory is not present
    print(f'Cannot find directory [{directory}]')
    return False
  
  if not path.isdir(directory): # If the 'directory' is not actually a directory (file, etc.)
    print(f'The provided directory is not valid [{directory}]')
    return False
  
  print(f'Directory is valid [{directory}]') # Good old directory
  return True