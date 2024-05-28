import matplotlib.pyplot as plt
import numpy as np

x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
image = np.sin(np.exp(np.sin(x)**3 + np.cos(y)**2))

isocontour = []
isovalue = 0.8  # Change me !


def interpol(val1, val2):
    # Linear interpolation of the isovalue between val1 and val2
    # Returns a value between 0 and 1

    # TODO


# Isocontour processing
for line in range(len(image) - 1):
    for col in range(len(image[0]) - 1):
        # Retrieve vertex scalars
        scalars = [image[line + 1][col], image[line + 1][col + 1], image[line][col + 1], image[line][col]]

        # First, we compute the score for this square
        # Add 1 to score if the bottom-left corner is higher than threshold
        # 2 if bottom-right is, 4 for top-right and 8 for top-left
        score = 0

        # TODO

        # Cell is completely in or out of the contour
        if score in [0,15]:
            continue

        # Draw a line if point 1 is in, but not 2 and 3 (or the opposite)
        if score in [1, 10, 14]:
            isocontour.append() # TODO)
        # point 2 in
        if score in [2, 5, 13]:
            isocontour.append() # TODO)
        # point 4 in
        if score in [4, 10, 11]:
            isocontour.append()  # TODO)

        # point 8 in
        if score in [5, 7, 8]:
            isocontour.append()  # TODO)

        # up and down
        if score in [3, 12]:
            isocontour.append()  # TODO)

        # left and right
        if score in [6, 9]:
            isocontour.append()  # TODO)

# Plotting stuff
fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray)
ax.axis('image')
for l in isocontour:
    ax.plot(l[:2],l[2:])

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
