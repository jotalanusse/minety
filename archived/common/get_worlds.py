def get_worlds():
  return [
    ##############################################################################################################################
    ######################################################### [SEASON 2] #########################################################
    ##############################################################################################################################
    {
      'name': 'BCC Season 2 - overworld', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-2/original/Lelo_world_2.0/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/overworld/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/overworld/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    {
      'name': 'BCC Season 2 - nether', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-2/original/Lelo_world_2.0/DIM-1/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/nether/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/nether/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-2/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    ##############################################################################################################################
    ######################################################### [SEASON 3] #########################################################
    ##############################################################################################################################
    {
      'name': 'BCC Season 3 - overworld', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-3/original/BCC Server/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/overworld/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/overworld/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    {
      'name': 'BCC Season 3 - nether', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-3/original/BCC Server/DIM-1/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/nether/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/nether/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    {
      'name': 'BCC Season 3 - end', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-3/original/BCC Server/DIM1/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/end/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/end/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/end/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-3/end/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    ##############################################################################################################################
    ######################################################### [SEASON 4] #########################################################
    ##############################################################################################################################                           
    {
      'name': 'BCC Season 4 - overworld', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-4/original/BCC Server/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/overworld/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/overworld/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    {
      'name': 'BCC Season 4 - nether', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-4/original/BCC Server_nether/DIM-1/region', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/nether/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/nether/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    {
      'name': 'BCC Season 4 - end', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-4/original/BCC Server_the_end/DIM1/region', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/end/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/end/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/end/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-4/end/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    ##############################################################################################################################
    ######################################################### [SEASON 5] #########################################################
    ##############################################################################################################################                           
    {
      'name': 'BCC Season 5 - overworld', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-5/original/world/region/', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/overworld/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/overworld/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/overworld/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
    {
      'name': 'BCC Season 5 - nether', # Name of the world
      'region_files_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/servers/season-5/original/world/DIM-1/region', # Directory of the world region files to be scanned
      'scans': [
                {
          'name': '5 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 5, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/nether/seconds-5/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-5.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        },
        {
          'name': '30 seconds scan', # Name of the scan
          'scan_all_chunks': True, # When enabled, the script will check all the chunks even if the region is already marked as important (the only good thing about this is you get to see an awesome world map)
          'inhabited_ticks_threshold': 20 * 30, # How many ticks a chunk has to be inhabited for so that it is considered as an important chunk
          'region_output': {
            'enabled': True, # When disabled, no files will be copied to the output
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/nether/seconds-30/', # Output directory for the processed region files
          },
          'map': {
            'enabled': True, # Is a map going to be graphed or not
            'scale_factor': 1.0, # How large the map image output will be (if value is 1.0 one chunk = one pixel)
            'file_name': 'heatmap-30.png', # Filename of the map file
            'output_directory': '/media/jotalanusse/windows-drive/Servers/Minecraft/backup/clean/season-5/nether/heatmaps/', # Output directory for the generated heatmaps
            'colors': {
              'default': [0, 0, 0], # Default color for the map
              'regions': {
                'inhabited_colormap': 'jet', # Colormap used when a region is inhabited
                'non_inhabited_colormap': 'PRGn' # Colormap used when a region is not inhabited
              }
            },
            'realtime_graph': {
              'enabled': False, # When enabled, the script will show a real time window showing the map being graphed once the region scanning process is finished
              'max_size': 1000, # If you are using a small screen you can modify this value to be able to fit the whole map graph in your screen
              'update_interval': 1 #  How many chunk renders to skip before displaying the updated graph again
            }
          },
        }
      ]
    },
  ]