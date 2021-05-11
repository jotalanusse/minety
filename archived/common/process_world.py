from multiprocessing import Pool

from .get_region_files import get_region_files
from .parse_region import parse_region
from .scan_region import scan_region
from .copy_file import copy_file
from .graph_map import graph_map

# Process world and it's region files
def process_world(world):
  print(f'Processing world [{world["name"]}]')
  
  region_files = get_region_files(world['region_files_directory']) # Get all region files from the region files directory for this world
  
  regions_pool_instance = Pool() # Start a new multiprocessing pool to parse regions
  regions_pool = regions_pool_instance.map_async(parse_region, region_files) # Use multiprocessing to parse all the region files and return a list of regions
  regions = regions_pool.get() # Wait for the pool to finish and retreive the regions
  regions_pool_instance.close() # Close the pool
  
  for config in world['scans']: # For each configuration process the regions
    print(f'Starting scan [{config["name"]}]')
    
    region_scans = [] # Store all the region scans
    
    for region in regions: # Process each region
      region_scan = scan_region(region, config['inhabited_ticks_threshold'], config['scan_all_chunks']) # Scan the region with the provided configuration
      
      if region_scan['is_inhabited']: # Here we check if the region is inhabited or not
        if config['region_output']['enabled']: # Check if the region output is enabled
          copy_file(region_scan['region']['file'], config['region_output']['output_directory']) # Copy the region to the output directory
      
      region_scans.append(region_scan) # Add the region scan to the list
    
    print(f'Scan [{config["name"]}] completed')
    
    if config['map']['enabled']: # Only render map if it is enabled in the configuration
      map_graph = graph_map(region_scans, config['map']) # Graph the map and return the image