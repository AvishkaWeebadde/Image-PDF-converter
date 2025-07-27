#!/usr/bin/env python3
"""
Simple test script that works from tests/ subdirectory
"""

import sys
import os
from pathlib import Path

# Add parent directory to Python path so we can import converter
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

print(f"🔍 Looking for converter package in: {project_root}")

# Test the import first
try:
    from converter.image_converter import ImageToPDFConverter
    print("✅ Import successful!")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("\n📁 Current directory structure:")
    print(f"   Tests directory: {current_dir}")
    print(f"   Project root: {project_root}")
    
    # Check if converter directory exists
    converter_path = project_root / "converter"
    if converter_path.exists():
        print(f"✅ Found converter directory: {converter_path}")
        
        # Check individual files
        required_files = ["__init__.py", "image_converter.py", "exceptions.py", "utils.py"]
        for file in required_files:
            file_path = converter_path / file
            if file_path.exists():
                print(f"   ✅ {file}")
            else:
                print(f"   ❌ {file} - MISSING!")
    else:
        print(f"❌ Converter directory not found at: {converter_path}")
        print("\n📋 Expected structure:")
        print("   your-project/")
        print("   ├── converter/")
        print("   │   ├── __init__.py")
        print("   │   ├── image_converter.py")
        print("   │   ├── exceptions.py")
        print("   │   └── utils.py")
        print("   └── tests/")
        print("       └── simple_test.py")
    
    sys.exit(1)

# Test PIL
try:
    from PIL import Image
    print("✅ PIL (Pillow) is available")
except ImportError:
    print("❌ Install Pillow: pip install Pillow")
    sys.exit(1)

# Create converter
try:
    converter = ImageToPDFConverter()
    print("✅ Converter created successfully")
except Exception as e:
    print(f"❌ Failed to create converter: {e}")
    sys.exit(1)

# Show supported formats
print(f"📋 Supported formats: {converter.supported_formats}")

# Test with a specific file (change this path!)
# Look for images in project root or tests directory
possible_images = [
    project_root / "test_image.png"
]

input_image = None
for img_path in possible_images:
    if Path(img_path).exists():
        input_image = str(img_path)
        break

if input_image is None:
    print("\n❌ No test image found. Tried:")
    for img_path in possible_images:
        print(f"   - {img_path}")
    print("\n📝 To test:")
    print("  1. Put an image file in the project root directory")
    print("  2. Or modify this script with the correct path")
    print("  3. Supported formats: JPG, PNG, BMP, TIFF, GIF, WebP")
else:
    output_pdf = project_root / "test_output.pdf"
    
    try:
        print(f"🔄 Converting {input_image} to {output_pdf}...")
        success = converter.convert_single_image(input_image, str(output_pdf))
        
        if success:
            print("✅ Conversion successful!")
            if output_pdf.exists():
                size_kb = output_pdf.stat().st_size / 1024
                print(f"📄 Created {output_pdf} ({size_kb:.1f} KB)")
            else:
                print("❌ PDF file not created")
        else:
            print("❌ Conversion failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n🎉 Test complete!")