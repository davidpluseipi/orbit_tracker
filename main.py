from map_on_earth import map_on_sphere
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from skyfield.api import EarthSatellite, load


# Variable Declaration / Definition
earth_radius = 6378.0
hours = np.arange(0, 3, 0.01)
radians_to_degrees, degrees_to_radians = 180 / np.pi, np.pi / 180
time_scale = load.timescale()
time = time_scale.utc(2018, 2, 7, hours)
TLE = """1 43205U 18017A   18038.05572532 +.00020608 -51169-6 +11058-3 0  9993
2 43205 029.0165 287.1006 3403068 180.4827 179.1544 08.75117793000017"""
line1, line2 = TLE.splitlines()
roadster = EarthSatellite(line1, line2)

# Plot 3D
fig = plt.figure(figsize=[10, 8])
axes1: Axes3D = fig.gca(projection='3d')
x, y, z = roadster.at(time).position.km

# Plot the orbit of the roadster
axes1.plot3D(x, y, z, '-r')

# Plot the globe
x_earth, y_earth, z_earth, img = map_on_sphere(earth_radius, 'land_ocean_ice_2048.jpg')
axes1.plot_wireframe(x_earth, y_earth, z_earth, rstride=10, cstride=10)
# axes1.plot_surface(x_earth.T, y_earth.T, z_earth.T, facecolors=img/255, cstride=1, rstride=1)

# # Plot globe as wireframe
# # Calculate lines of longitude
# for phi in degrees_to_radians * np.arange(0, 180, 15):
#     cos_phi, sin_phi = [f(phi) for f in (np.cos, np.sin)]
#     lon = np.vstack((earth_radius * (np.cos(theta) * cos_phi - np.zeros_like(theta) * sin_phi),
#                      earth_radius * (np.zeros_like(theta) * cos_phi + np.cos(theta) * sin_phi),
#                      earth_radius * np.sin(theta)))
#     longitudes.append(lon)
#
# # Calculate lines of latitude
# for phi in degrees_to_radians * np.arange(-75, 90, 15):
#     cos_phi, sin_phi = [f(phi) for f in (np.cos, np.sin)]
#     lat = earth_radius * np.vstack((np.cos(theta) * cos_phi, np.sin(theta) * cos_phi, np.zeros_like(theta) + sin_phi))
#     latitudes.append(lat)
# for x, y, z in longitudes:
#     axes1.plot(x, y, z, '-k')
# for x, y, z in latitudes:
#     axes1.plot(x, y, z, '-k')
axes1.axis('auto')
plt.show()

