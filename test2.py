with open(r"C:\Users\azooz\Desktop\33093a74-8b0d-403c-9796-ee8029fba0de.jpg","rb") as image_file:
    image_bytes= image_file.read()

with open("newImaggee.jpg","wb") as d:
    d.write(image_bytes)

