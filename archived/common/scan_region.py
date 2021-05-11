# Check if a chunk has been inhabited for x ticks or more based on a threshold
def is_chunk_inhabited(chunk, inhabited_ticks_threshold):
  # print(f'Processing chunk [{chunk.data["x_pos"]}, {chunk.data['zPos']}] for inhabited ticks')
  
  inhabited_ticks = chunk['inhabited_ticks']
  return inhabited_ticks >= inhabited_ticks_threshold # Return true the total inhabited ticks are higher than the threshold check, or false otherwise


# Scan a region with the given parameters
def scan_region(region, inhabited_ticks_threshold, scan_all_chunks):
  # print(f'Scanning region [{path.basename(region_file)}]') # TODO: Show the name of the region being scanned
  
  region_scan = {
    'region': region, # Save the region corresponding to the scan
    'is_inhabited': False, # Here we store if the region is inhabited or not
    'inhabited_ticks_threshold': inhabited_ticks_threshold, # Store the threshold used for the scan
    'scan_all_chunks': scan_all_chunks, # Store if all chunks where scanned or not
    'chunk_scans': [] # Here we store the individual scan for each chunk
  }
  
  chunks = region['chunks']
  
  # Scan all the region chunks with the input parameters
  for chunk in chunks:
    chunk_scan = {
      'chunk': chunk, # Save the chunk corresponding to the scan
      'is_inhabited': False, # Here we store if the chunk is inhabited or not
    }
          
    if is_chunk_inhabited(chunk, inhabited_ticks_threshold): # Check if the chunk is inhabited or not
      chunk_scan['is_inhabited'] = True
      region_scan['is_inhabited'] = True # If one chunk is inhabited, the the region is inhabited
      
      if not scan_all_chunks: # If the scan_all_chunks parameter is not enabled we can return that the region scan on the first encounter with an inhabited chunk
        region_scan['chunk_scans'].append(chunk_scan) # Add the first inhabited chunk scan to the list before returning the region scan
        return region_scan # Return the uncompleted (not a full scan) region scan
    
    region_scan['chunk_scans'].append(chunk_scan) # Add the chunk scan to the list
    
  return region_scan