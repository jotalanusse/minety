import numpy as np
import matplotlib as mpl
import cv2
from os import path


# Graph a world map based on a list of region scans
def graph_map(region_scans, map_config): # By accepting the list of region scans instead of a list of chunks, we can do really interesting things
  pass
  # print(f'Graphing map with a total of [{len(region_scans)}] regions => [{len(region_scans) * 1024)}] chunks')

  # for region
  
  # # Set the position variables as high/low as possible so the script can set the correct values when comparing with the real positions
  # min_x_pos = 9999999999999
  # min_z_pos = 9999999999999
  # max_x_pos = -9999999999999
  # max_z_pos = -9999999999999
  
  # # Do the same for the inhabited ticks
  # max_inhabited_ticks = -9999999999999
  
  # # Iterate all of the regions
  # for region_scan in region_scans:
  #   chunk_scans = region_scan['chunk_scans']
    
  #   # Check every chunk in the chunk graphs list for the highest/lowest values
  #   for chunk_scan in chunk_scans:
  #     chunk = chunk_scan['chunk']
      
  #     x_pos = chunk['x_pos']
  #     z_pos = chunk['z_pos']
  #     inhabited_ticks = chunk['inhabited_ticks']
      
  #     # Search for the minimum position for X and Z
  #     min_x_pos = min(min_x_pos, x_pos)
  #     min_z_pos = min(min_z_pos, z_pos)

  #     # Search for the maximum position for X and Z
  #     max_x_pos = max(max_x_pos, x_pos)
  #     max_z_pos = max(max_z_pos, z_pos)
      
  #     # Search for the maximum inhabited ticks
  #     max_inhabited_ticks = max(max_inhabited_ticks, inhabited_ticks)

  # # Position offsets to be used while graphing the map
  # x_pos_offset = 0
  # z_pos_offset = 0 
  
  # # Here we take the minimum positions of X and Z and use them to calculate the offset
  # if min_x_pos < 0:
  #   x_pos_offset += abs(min_x_pos)
  # elif min_x_pos > 0:
  #   x_pos_offset += -min_x_pos
    
  # if min_z_pos < 0:
  #     z_pos_offset += abs(min_z_pos)
  # elif min_z_pos > 0:
  #   z_pos_offset += -min_z_pos
  
  # # Now we have our canvas size and we can create the map
  # map = np.zeros((1 + max_x_pos + x_pos_offset, 1 + max_z_pos + z_pos_offset, 3), np.uint8) # I don't really fucking know why we have to add one pixel more for the canvas to be the correct size, but it works
  # map[:] = default_map_color # Set the base color for the map
  
  # graphing_index = 0 # Graphing index used to know when to show an updated graph to the user

  # # Iterate all of the regions
  # for region_scan in region_scans:
  #   region = region_scan['region']
  #   chunks = region['chunks']
  #   is_inhabited = region_scan['is_inhabited']
    
  #   # Do the coloring shenanigans per region
  #   colormap_reference = non_inhabited_region_colormap # Set the default region colormap (non inhabited)
  #   if is_inhabited:
  #     colormap_reference = inhabited_region_colormap # In case the region is habited change the colormap
      
  #   colormap = mpl.pyplot.get_cmap(colormap_reference)  # Get the specified colormap
  #   normalized_max_inhabited_ticks = mpl.colors.LogNorm(1, max_inhabited_ticks) # Normalize the max inhabited ticks for a better heatmap
  #   scalar_map = mpl.cm.ScalarMappable(norm = normalized_max_inhabited_ticks, cmap = colormap) # Generate a scalar mapping for the colormap given the inhabited ticks
    
  #   # Check every chunk in the chunk graphs list for the highest/lowest values
  #   for chunk in chunks:
  #     x_pos = chunk['x_pos']
  #     z_pos = chunk['z_pos']
  #     inhabited_ticks = chunk['inhabited_ticks']
      
  #     # Get the X and Z positions of the chunk after we add the offset
  #     final_chunk_x_pos = x_pos + x_pos_offset
  #     final_chunk_z_pos = z_pos + z_pos_offset

  #     rgba_color = scalar_map.to_rgba(inhabited_ticks + 1) # Get the corresponding color given the total inhabited ticks
  #     bgr_color = (rgba_color[2] * 255, rgba_color[1] * 255, rgba_color[0] * 255) # Convert the RGBA format to BGR # TODO: Find a better way of converting the color
      
  #     map[final_chunk_x_pos, final_chunk_z_pos] = bgr_color # Set the color on the map
      
  #     # Allow the user to see the map graph in real time
  #     if real_time_graph_enabled: # If the user decided to watch the map graph in real time
  #       if graphing_index % real_time_graph_update_interval == 0: # We skip updating the map graph until we encounter a valid graphing index
  #         height, width, channels = map.shape # Get the size of the map
  #         largest_axis = max(height, width) # Find the largest axis
          
  #         scale_factor = (real_time_graph_max_size / largest_axis) # Determine a scale factor to resize the map
          
  #         # Resize both axis
  #         final_width = round(width * scale_factor)
  #         final_height = round(height * scale_factor)
          
  #         small_map = cv2.resize(map, (final_width, final_height)) # Create small map form the given measurements
          
  #         cv2.imshow('World Map', small_map) # Show the small map
  #         cv2.waitKey(1) # Wait 1 ms before continuing
        
  #     graphing_index += 1 # Do I need to explain this 3: Super-Electric Boogaloo
    
  # height, width, channels = map.shape # Get the size of the map
  
  # # Resize both axis
  # final_width = round(width * map_scale_factor)
  # final_height = round(height * map_scale_factor)
  
  # final_map = cv2.resize(map, (final_width, final_height)) # Scale the map to match the defined scale factor
  
  # map_output = path.join(map_output_directory ,map_file_name) # Create the complete output directory path based on the map name and the output directory
  # cv2.imwrite(map_output, final_map) # Write the final map with the provided name
  
  # print(f'Map [{map_file_name}] saved to directory [{map_output_directory}]');