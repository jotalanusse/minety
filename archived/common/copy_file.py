import shutil


# Copy a region file to the output folder
def copy_file(region_file, output_region_directory):
  # print(f'Copying [{region_file}] to output directory')
  
  try:
    shutil.copy2(region_file, output_region_directory) # Copy the file
  except:
    print(f'Error while copying file [{region_file}] to output directory')