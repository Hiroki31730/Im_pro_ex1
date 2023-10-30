import cv2
import matplotlib.pyplot as plt
import numpy as np

pm = 3
img_l = []

for i in range(1,10):
    img = cv2.imread("fruit_" + str(i) + ".png")
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    re_img = np.asarray(img)
    img_rs = cv2.resize(re_img, (200, 200),cv2.INTER_LANCZOS4)
    img_l.append(re_img)
    
fig, ax = plt.subplots(pm, pm, figsize=(6, 6))
fig.subplots_adjust(hspace=0, wspace=0)
for i in range(pm):
    for j in range(pm):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(img_l[pm*i+j], cmap="bone")
plt.show()