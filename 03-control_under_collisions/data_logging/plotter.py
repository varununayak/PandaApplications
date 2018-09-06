#!/usr/bin/env python3

# read text files and plot them

import matplotlib.pyplot as plt
import numpy as np
import sys

# data file to read given as argument
if len(sys.argv) < 2:
	print("Give the name of the file to read as an argument\n")
	exit()

file = np.loadtxt(sys.argv[1] ,skiprows=1)

time = file[1::,0]
r_vel = file[1::,1:8]
r_mom = file[1::,8:15]
tau_comp = file[1::,15:22]
tau_cmd = file[1::,22:29]
x_curr = file[1::,29:32]
x_des = file[1::,32:35]

time = np.arange(np.shape(r_vel)[0])
time = time/100

print(np.sqrt(np.mean((x_des-x_curr).dot((x_des - x_curr).T))))

# plt.figure(1, figsize=(7,8))
# plt.subplot(211)
# plt.plot(time,r_vel)
# plt.title("velocity based observer")
# plt.subplot(212)
# plt.plot(time,tau_comp)
# plt.title("contact comensation torques")

plt.figure(2, figsize=(5,3))
plt.title("x vs xd")
plt.subplot(311)
plt.plot(time,x_des[:,0]-x_curr[:,0], c='r')
plt.axis([0,time[-1], -0.007, 0.007])
plt.subplot(312)
plt.plot(time,x_des[:,1]-x_curr[:,1], c='g')
plt.axis([0,time[-1], -0.007, 0.007])
plt.subplot(313)
plt.plot(time,x_des[:,2]-x_curr[:,2], c='b')
plt.axis([0,time[-1], -0.005, 0.005])


# plt.figure(3, figsize=(5,4))
# plt.plot(time, tau_cmd)
# plt.title("Torques commanded")

plt.show()


