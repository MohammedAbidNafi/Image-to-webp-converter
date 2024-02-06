from PIL import Image, ImageOps
import os

def convert_to_webp(input_path, output_path):
    try:
        image = Image.open(input_path)

        # Apply EXIF orientation transformation
        image = ImageOps.exif_transpose(image)

        image.save(output_path, 'WEBP')
        print(f"Conversion successful: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error converting {input_path} to WebP: {str(e)}")

# Replace 'input_folder' and 'output_folder' with your actual folder paths
input_folder = 'path to folder'
output_folder = 'path to folder'
id = 1

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(str(id))[0] + '.webp'
        output_path = os.path.join(output_folder, output_filename)
        convert_to_webp(input_path, output_path)
        id = id + 1
