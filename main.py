#------------------------------------ Steps to create a watermarking app ------------------------------------#
# Create the tkinter root
# Create a canvas with scrollbars
# Create a frame inside the canvas
# Variables to store image data
# Create the file dialog box
# Create image importer
# Show the image in the Tkinter label
# Create watermark
    # Get the bounding box of the text
    # Calculate the position to place the watermark
    # Draw the watermark text
    # Display the watermarked image
# Create image exporter
    # Convert the image to RGB mode before saving as JPEG
# Create the buttons
# Create the image label
# Update the canvas scroll region
# Start the main loop
#--------------------------------------------------- Code ----------------------------------------------------#


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Create the tkinter root
root = Tk()
root.title("Watermarker App")

# Create a canvas with scrollbars
canvas = Canvas(root, width=600, height=400)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas
canvas_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Variables to store image data
image_path = None
loaded_image = None
watermark_image = None

# Create the file dialog box
def open_file_dialog():
    global image_path, loaded_image
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        import_image(image_path)

# Create image importer
def import_image(image_path):
    global loaded_image
    try:
        loaded_image = Image.open(image_path)
        photo = ImageTk.PhotoImage(loaded_image)
        show_image(photo)
        messagebox.showinfo("Status", "Image imported successfully.")
    except IOError:
        messagebox.showerror("Error", f"Unable to open image file: {image_path}")

# Show the image in the Tkinter label
def show_image(photo):
    global image_label
    if image_label is not None:
        image_label.destroy()
    image_label = Label(canvas_frame, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)

# Create watermark
def create_watermark():
    global loaded_image, watermark_image
    if loaded_image is not None:
        im = loaded_image.copy()
        width, height = im.size

        draw = ImageDraw.Draw(im)
        text = "byzd watermark"

        font = ImageFont.truetype('arial.ttf', 36)

        # Get the bounding box of the text
        bbox = draw.textbbox((0, 0), text, font=font)

        # Calculate the position to place the watermark
        margin = 10
        x = width - bbox[2] - margin
        y = height - bbox[3] - margin

        # Draw the watermark text
        draw.text((x, y), text, font=font)

        # Display the watermarked image
        photo = ImageTk.PhotoImage(im)
        show_image(photo)
        watermark_image = im
        messagebox.showinfo("Status", "Watermark placed successfully.")

# Create image exporter
def export_image():
    global watermark_image
    if watermark_image is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
        if save_path:
            # Convert the image to RGB mode before saving as JPEG
            rgb_image = watermark_image.convert("RGB")
            rgb_image.save(save_path)
            messagebox.showinfo("Status", "Image exported successfully.")

# Create the buttons
img_import = ttk.Button(canvas_frame, text="Select Image", command=open_file_dialog)
img_import.pack(pady=5)

watermark_button = ttk.Button(canvas_frame, text="Place Watermark", command=create_watermark)
watermark_button.pack(pady=5)

img_export = ttk.Button(canvas_frame, text="Export Image", command=export_image)
img_export.pack(pady=5)

# Create the image label
image_label = None

# Update the canvas scroll region
canvas_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Start the main loop
root.mainloop()
