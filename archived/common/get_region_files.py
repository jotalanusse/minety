
import glob
from os import path


# Search for all the available region files in the given directory
def get_region_files(directory):
  print(f'Searching for region files in directory [{directory}]')
  
  region_files =  glob.glob(path.join(directory, '*.mca')) # Get all the region files in the given directory
  
  print(f'A total of [{len(region_files)}] region files where found')
  
  return region_files