def get_worlds():
  return [
    {
      'name': 'Test world', # Name of the world
      'region_files_directory': '/home/jotalanusse/Desktop/snapshot-small/BCC Server/region/', # Directory of the world region files to be scanned
      'scans': [
        {
          'name': '30 seconds rule', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': './snapshot-small-test/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': './snapshot-small-test/heatmaps', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'plasma', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'gnuplot' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': True, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
  ]