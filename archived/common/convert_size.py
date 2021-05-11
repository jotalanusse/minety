# Convert bytes to a more user-friendly scale
def convert_size(size_bytes):
  if size_bytes == 0: # If 0 return 0, I mean...
    return '0B'

  size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB') # All possible unit names
  index = int(math.floor(math.log(size_bytes, 1024))) # Get the index of the unit
  bites_per_unit = math.pow(1024, index) # How many bytes are there per unit
  total_units = round(size_bytes / bites_per_unit, 2) # How many units do we have
  return f'{total_units} {size_name[index]}' # Return the formatted result