import matplotlib.pyplot as plt
import numpy as np

x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
image = np.sin(np.exp(np.sin(x)**3 + np.cos(y)**2))

isocontour = []
isovalue = 0.8  # Change me !


def interpol(val1, val2):
    # Linear interpolation of the isovalue between val1 and val2
    # Returns a value between 0 and 1
    return (isovalue - val1) / (val2 - val1)


# Isocontour processing
for line in range(len(image) - 1):
    for col in range(len(image[0]) - 1):
        # Retrieve vertex scalars
        scalars = [image[line + 1][col], image[line + 1][col + 1], image[line][col + 1], image[line][col]]

        # First, we compute the score for this square
        # Add 1 to score if the bottom-left corner is higher than threshold
        # 2 if bottom-right is, 4 for top-right and 8 for top-left
        score = 0
        for i in range(4):
            if scalars[i] > isovalue:
                score |= 1 << i


        if score in [0,15]:
            continue

        # Draw a line if point 1 is in, but not 2 and 3 (or the opposite)
        if score in [1, 10, 14]:
            isocontour.append(
                (col, col + interpol(scalars[0], scalars[1]), line + interpol(scalars[3], scalars[0]),  line + 1))

        # point 2 in
        if score in [2, 5, 13]:
            isocontour.append(
                (col + interpol(scalars[0], scalars[1]), col + 1, line + 1,  line + interpol(scalars[2], scalars[1])))

        # point 4 in
        if score in [4, 10, 11]:
            isocontour.append(
                (col + interpol(scalars[3], scalars[2]), col + 1, line,  line + interpol(scalars[2], scalars[1])))

        # point 8 in
        if score in [5, 7, 8]:
            isocontour.append(
                (col, col + interpol(scalars[3], scalars[2]), line + interpol(scalars[3], scalars[0]),  line))

        # up and down
        if score in [3, 12]:
            isocontour.append((
                col,
                col + 1,
                line + interpol(scalars[3], scalars[0]),
                line + interpol(scalars[2], scalars[1]),
            ))

        # left and right
        if score in [6, 9]:
            isocontour.append((
                col + interpol(scalars[0], scalars[1]),
                col + interpol(scalars[3], scalars[2]),
                line+1,
                line
            ))

fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray)
ax.axis('image')
for l in isocontour:
    ax.plot(l[:2],l[2:])

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
