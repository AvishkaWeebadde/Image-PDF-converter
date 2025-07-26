"""
Custom exceptions for the image-PDF converter
"""

"""Base exception for conversion operations"""
class ConversionError(Exception):
    
    def __init__(self, message:str, original_error:Exception = None):
        super().__init__(message)
        self.message = message
        self.original_error = original_error

    
    def __str__(self):
        if self.original_error:
            return f"{self.message} (Original error: {self.original_error})"
        return self.message
    

"""Raised when input file is not found"""    
class FileNotFoundError(Exception):

    def __init__(self, file_path:str):
        super.__init__(f"File not found: {file_path}")
        self.file_path = file_path


"""Raised when file permission issues occur"""
class PermissionError(Exception):
    
    def __init__(self, message: str, pdf_path: str = None):
        super().__init__(message)
        self.pdf_path = pdf_path