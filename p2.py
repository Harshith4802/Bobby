from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def line_dir_pt(m,A):
  len = 10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

#defining lines : x(k) = A + k*l
A1 = np.array([-2*np.sqrt(2),0,0]).reshape((3,1))
l1 = np.array([12,6,-1]).reshape((3,1))
A2 = np.array([0,-4*np.sqrt(2),2*np.sqrt(2)]).reshape((3,1))
l2 = np.array([6,6,1]).reshape((3,1))
A3 = (1.0/21.0) * np.array([90*np.sqrt(2),66*np.sqrt(2),-11*np.sqrt(2)]).reshape((3,1))
l3 = (1.0/7.0) * np.array([8*np.sqrt(2),-12*np.sqrt(2),24*np.sqrt(2)]).reshape((3,1))

#defining point of intersection
A = (1.0/21.0) * np.array([90*np.sqrt(2),66*np.sqrt(2),-11*np.sqrt(2)])
B = (1.0/21.0) * np.array([114*np.sqrt(2),30*np.sqrt(2),61*np.sqrt(2)])

#generating points in line 
l1_p = line_dir_pt(l1,A1)
l2_p = line_dir_pt(l2,A2)
l3_p = line_dir_pt(l3,A3)

#plotting line
plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line L1")
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line L2")
plt.plot(l3_p[0,:],l3_p[1,:],l3_p[2,:],label="AB")

#plotting point
ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.text(6.07,4.46,-0.77,'A')
ax.text(7.68,2.03,4.12,'B')


#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.show()
