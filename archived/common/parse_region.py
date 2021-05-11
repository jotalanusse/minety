from os import path
import anvil


from .create_chunk import create_chunk


# Parse a region file into a region
def parse_region(region_file):
  print(f'Parsing region [{path.basename(region_file)}]')
  
  region_object = anvil.Region.from_file(region_file) # Create a region object from the region file
  
  region = {
    'file': region_file, # Get the file corresponding to the region
    # TODO: Get the name of the region
    'size': path.getsize(region_file), # Get the size in bytes of the region
    'chunks': [] # Here we store all the chunks for the region
  }
  
  # The region is represented in a grid of 32x32 chunks
  for i in range(32):
    for o in range(32):
      try:
        chunk_object = region_object.get_chunk(i, o) # Create a chunk object based on the relative coordinates of the region
        chunk = create_chunk(chunk_object) # Create a chunk from the chunk object
        region['chunks'].append(chunk) # Add the chunk to region chunks list
      except Exception as e:
        pass # Propably the error is raised because the chunk in the current index does not exist
      
  return region