import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#12EDO
print("input your pc class (separate with commas, maximum of 12 pitch classes with multisets allowed):")
pc_set=input()
while True:
  pc_set_s=pc_set.split(",")
  pc_set_array=np.array(pc_set_s, dtype=int) # Convert to integer array
  if np.any(pc_set_array > 11):
    print("please keep pitches under 11")
    pc_set=input()
  else:
    break

char_func = np.bincount(pc_set_array, minlength=12)
print("Characteristic Function:",char_func)
pc_dft = np.fft.fft(char_func)
pc_dft_s = pc_dft[0:7]
pc_mag = np.abs(pc_dft_s)
pc_mag_sq = pc_mag ** 2
pc_phase = np.angle(pc_dft_s[1:7], deg = True)
pc_phase = pc_phase + 360 % 360
pc_phase_norm = pc_phase / 30

print("Magnitudes squared:", np.round(pc_mag_sq, decimals = 2))
print("Normalized phase:", np.round(pc_phase_norm, decimals = 2))
print("Phase:", np.round(pc_phase, decimals = 2))


#Polar graph
plt.figure(2)
polarplot = plt.subplot(111, projection='polar')

# Set 0 to north and direction to clockwise
polarplot.set_theta_zero_location('N')
polarplot.set_theta_direction(-1)

# Plotting lines from the origin
radians_phase = np.deg2rad(pc_phase)
pc_mag_nototal = pc_mag_sq[1:7]
for i in range(len(pc_mag_nototal)): # Iterate through each point
    line, = polarplot.plot([0, radians_phase[i]], [0, pc_mag_nototal[i]], marker='o', markersize=5)
    lcolor = line.get_color()
    polarplot.text(radians_phase[i]- 0.1, pc_mag_nototal[i], str(i+1), color=lcolor)
plt.show()

#magnitude graph
plt.figure(1)
plt.plot(pc_mag_sq)
plt.xlabel("Fourier coeff")
plt.ylabel("Mag squared")
plt.title("Magnitutdes squared")
