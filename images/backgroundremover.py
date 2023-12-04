from rembg import remove
from PIL import Image
input_path = 'dogcat.png'
output_path = 'dogcatre.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print("done!")
