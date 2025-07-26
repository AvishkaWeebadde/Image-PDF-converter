"""
Image to PDF conversion functionality
"""

from pathlib import Path
from PIL import Image
from typing import List
from converter.exceptions import ConversionError
from converter.utils import validate_file_exists, create_directory

class ImageToPDFConverter:

    def __init__(self):
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif', '.webp'}

    """
        Convert a single image to PDF
        
        Args:
            image_path: Path to input image
            output_path: Path for output PDF
            quality: JPEG quality (1-100)
            
        Returns:
            bool: Success status
    """    
    def convert_single_image(self, image_path: str, output_path: str, quality: int = 95) -> bool:
        try:
            validate_file_exists(image_path)
            create_directory(Path(output_path).parent)

            with Image.open(image_path) as img:
               if img.mode != 'RGB':
                    img = img.convert('RGB')
               img.save(output_path, "PDF", quality = quality, optimize = True) 
               
            return True
        except Exception as e:
            raise ConversionError(f"Failed to convert image to PDF: {e}")

