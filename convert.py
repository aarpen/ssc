from pdf2image import convert_from_path
import os

pdf_path = "bioques.pdf"  # ← your PDF filename
POPPLER_PATH = r"C:\poppler-25.12.0\Library\bin"  # ← update this to your actual path

output_folder = "pdf_images"
os.makedirs(output_folder, exist_ok=True)

print("Converting PDF pages to images...")
images = convert_from_path(
    pdf_path,
    dpi=150,
    fmt="jpeg",
    thread_count=4,
    poppler_path=POPPLER_PATH
)

for i, image in enumerate(images, start=1):
    filename = os.path.join(output_folder, f"page_{i:04d}.jpg")
    image.save(filename, "JPEG", quality=85)
    print(f"Saved: {filename}")

print(f"\nDone! {len(images)} images saved to '{output_folder}/'")