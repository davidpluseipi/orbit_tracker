import matplotlib.pyplot as plt
import numpy as np


def map_on_sphere(radius, image_file):
    img = plt.imread(image_file)

    # define a grid matching the map size, subsample along with pixels
    theta = np.linspace(0, np.pi, img.shape[0])
    phi = np.linspace(0, 2*np.pi, img.shape[1])

    count = 180  # keep 180 points along theta and phi
    theta_index = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
    phi_index = np.linspace(0, img.shape[1] - 1, count).round().astype(int)
    theta = theta[theta_index]
    phi = phi[phi_index]
    img = img[np.ix_(theta_index, phi_index)]

    theta, phi = np.meshgrid(theta, phi)

    # sphere
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)

    return x, y, z, img

