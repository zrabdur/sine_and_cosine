import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
angle = np.arange(0,361)

# Set Amplitude
amp = 10
pi = math.pi
# Add constant phas
const_phase = pi/3
# Angle in Radians
angle_rad = angle*pi/180 + const_phase
# Cosine and Sine curves
value_cosine = [amp*math.cos(angles) for angles in angle_rad]
value_sine = [amp*math.sin(angles) for angles in angle_rad]

fig, ax = plt.subplots(2)
fig.suptitle('Sine & Cosine: constant phase, {} rad'.format(str(const_phase)))

ax[0].plot(angle_rad, value_cosine)
ax[1].plot(angle_rad, value_sine)
#for ax in axs.flat:
ax[0].set(xlabel='x-label', ylabel='y-label')
ax[1].set(xlabel="Exam score-1", ylabel="Exam score-2")

ax[0].legend( ["Cosine" ])
ax[1].legend(['Sine'])
plt.show()