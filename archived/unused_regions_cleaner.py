from common import get_worlds, check_world_config, process_world

def main():
  print('################################################')
  print('#########  UNUSED REGIONS CLEANER v3.00  #######')
  print('#########  @jotalanusse && @inakineitor  #######')
  print('################################################')

  worlds = get_worlds() # Get all available worlds to process

  print('Main process started!')
  
  for world in worlds:  # Process all the worlds
    print(f'Setting up world [{world["name"]}]')

    check_world_config(world) # Check the world's configuration to make sure everything is fine

    process_world(world) # Process world

if __name__ == '__main__':
  main() # Let's go