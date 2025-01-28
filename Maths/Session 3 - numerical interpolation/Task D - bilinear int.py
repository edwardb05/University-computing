import numpy as np
import matplotlib.pyplot as plt

# Load the original image
Pic = plt.imread("Flower.jpg")
Ny, Nx, _ = Pic.shape
Nscale = 5

# Shrink the image by taking a pixel every Nscale pixels
PicShrunk = Pic[0:Ny:Nscale, 0:Nx:Nscale, :]
plt.imshow(PicShrunk)
plt.title("Shrunk Image")
plt.axis('off')
plt.show()

# Size of shrunk image
Nx_shrunk = PicShrunk.shape[1]
Ny_shrunk = PicShrunk.shape[0]

# Scale factor for enlarging
Scale = 7
NyL = (Ny_shrunk - 1) * Scale + 1
NxL = (Nx_shrunk - 1) * Scale + 1
ImLarge = np.zeros((NyL, NxL, 3), dtype=np.uint8)

# Place the pixels from the shrunk image into the larger image
ImLarge[0::Scale, 0::Scale, :] = PicShrunk[:, :, :]

# Interpolate to fill in the missing pixels using bilinear interpolation
for c in range(3):  # For each color channel
    for j in range(NyL-1):  # Iterate over the enlarged image height
        for i in range(NxL-1):  # Iterate over the enlarged image width
            if i % Scale != 0 or j % Scale != 0:  # Skip original pixels
                # Calculate surrounding pixel indices
                x1 = i - i % Scale
                x2 = x1 + Scale
                y1 = j - j % Scale
                y2 = y1 + Scale

                # Check bounds
               
                 # Construct the bilinear interpolation matrix
                Matrix = np.array([
                        [x2 * y2, -x1 * y2, -x2 * y1, x1 * y1],
                        [-y2, y2, y1, -y1],
                        [-x2, x1, x2, -x1],
                        [1, -1, -1, 1]
                    ])

                    # Gather pixel values from the enlarged image
                Vector = np.array([
                        ImLarge[y1, x1, c],
                        ImLarge[y1, x2, c],
                        ImLarge[y2, x1, c],
                        ImLarge[y2, x2, c]
                    ])

                    # Perform the bilinear interpolation
                a = 1 / ((y2 - y1) * (x2 - x1)) * Matrix.dot(Vector)
                    # Assign the computed value to the enlarged image
                ImLarge[j, i, c] = a[0] + a[1] * i + a[2] * j + a[3] * i * j

# Display the enlarged image
plt.imshow(ImLarge)
plt.title("Enlarged Image with Interpolation")
plt.axis('off')
plt.show()
