from PIL import Image

# Define ASCII characters based on intensity (dark to light)
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """Resize the image to a new width while maintaining the aspect ratio."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjust height for ASCII aspect
    return image.resize((new_width, new_height))

def grayscale_image(image):
    """Convert the image to grayscale."""
    return image.convert("L")

def map_pixels_to_ascii(image):
    """Map each pixel to an ASCII character."""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, output_width=100):
    """Convert an image to ASCII art."""
    try:
        # Load and process the image
        image = Image.open(image_path)
        image = resize_image(image, new_width=output_width)
        image = grayscale_image(image)
        
        # Map pixels to ASCII
        ascii_str = map_pixels_to_ascii(image)
        
        # Format ASCII into rows
        pixel_count = len(ascii_str)
        ascii_art = "\n".join([ascii_str[i:i+output_width] for i in range(0, pixel_count, output_width)])
        
        return ascii_art
    except Exception as e:
        return f"Error: {e}"

def save_ascii_art(ascii_art, output_file):
    """Save the ASCII art to a text file."""
    with open(output_file, "w") as f:
        f.write(ascii_art)

# Example Usage
image_path = "image_file_here.jpg"  # Replace with your image path
output_file = "ascii_art.txt"
ascii_art = convert_image_to_ascii(image_path, output_width=100)
save_ascii_art(ascii_art, output_file)
print(ascii_art)