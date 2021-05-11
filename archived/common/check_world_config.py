from common.is_valid_directory import is_valid_directory
from common.create_directory import create_directory

def check_world_config(world):
  if not is_valid_directory(world['region_files_directory']): # Check if the regions folder is valid
    print(f'Invalid region files directory [{world["region_files_directory"]}]')
    exit(1) # TODO: Set the correct exit code
  
  for config in world['scans']: # Check each world's configuration
    print(f'Setting up scan [{config["name"]}]')
    
    if config['region_output']['enabled']: # Only check this if region output is enabled
      print('Region output is enabled for this scan')
      
      print('Checking region files output directory')
      if not is_valid_directory(config['region_output']['output_directory']): # Check if the directory is valid
        create_directory(config['region_output']['output_directory']) # If not try to create it
    else:
      print('Region output is not enabled for this scan')
    
    if config['map']['enabled']: # Only check this if map graphing is enabled
      print('Map graphing is enabled for this scan')
      
      print('Checking map files output directory')
      if not is_valid_directory(config['map']['output_directory']): # Check if the directory is valid
        create_directory(config['map']['output_directory']) # If not try to create it
    else:
      print('Map graphing is not enabled for this scan')
    
    # TODO: Check the rest of the configurations?