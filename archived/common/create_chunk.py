# Create the chunk from a given chunk object
def create_chunk(chunk_object):
  chunk = {
    'inhabited_ticks': chunk_object.data['InhabitedTime'].value,
    'x_pos': chunk_object.data['xPos'].value,
    'z_pos': chunk_object.data['zPos'].value
  }
  
  return chunk