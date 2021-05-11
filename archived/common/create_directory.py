import os

# Create a new directory
def create_directory(directory):
  try:
    os.makedirs(directory) # Try to create the directory for the user
  except:
      print(f'Failed creating output directory: {directory}') # Fuck you OS, let me create a directory
      exit(1) # TODO: Add the correct exit code
  else:
      print(f'Output directory created successfully: {directory}') # I love you OS, thanks for creating my directory