Watermarker App
The Watermarker App is a Python application built using the Tkinter library and Pillow (PIL) for image processing. It allows users to import an image, apply a watermark, and export the watermarked image.

Features
Image Import: Users can select an image file (in formats such as PNG, JPG, JPEG) using the "Select Image" button. The selected image is displayed in the application window.
Watermark Placement: Users can apply a watermark to the imported image by clicking the "Place Watermark" button. The watermark, in this case, is the text "byzd watermark" placed in the bottom right corner of the image.
Image Export: After applying the watermark, users can export the watermarked image as a JPEG file by clicking the "Export Image" button. A file dialog prompts the user to choose the save location and file name.
Usage
Run the watermarker_app.py file using Python.
Click the "Select Image" button to choose an image file.
Once an image is imported, click the "Place Watermark" button to apply the watermark.
The watermarked image will be displayed in the application window.
To export the watermarked image, click the "Export Image" button and choose the save location and file name in the file dialog.
Requirements
Python 3.x
Pillow (PIL) library
Tkinter library (usually included with Python)
Note
The watermark text, font, and size can be modified in the create_watermark function.
The Watermarker App currently supports PNG, JPG, and JPEG image formats.
