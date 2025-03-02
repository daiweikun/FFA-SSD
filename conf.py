import numpy as np
import matplotlib.pyplot as plt
# classes = ['A','B','C','D','E']
# confusion_matrix = np.array([(9,1,3,4,0),(2,13,1,3,4),(1,4,10,0,13),(3,1,1,17,0),(0,0,0,1,14)],dtype=np.float64)


# 标签
classes=[' open_eye  ','closed_eye']

# 标签的个数
classNamber=2 #表情的数量

# 在标签中的矩阵
confusion_matrix = np.array([[462  , 42],
 [  28 ,421],
 ],dtype=np.float64)

plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)  #按照像素显示出矩阵
plt.title('Confusion matrices',fontsize=14)
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)

thresh = confusion_matrix.max() / 2.
#iters = [[i,j] for i in range(len(classes)) for j in range((classes))]
#ij配对，遍历矩阵迭代器
iters = np.reshape([[[i,j] for j in range(classNamber)] for i in range(classNamber)],(confusion_matrix.size,2))
for i, j in iters:
    if (i == j):
        plt.text(j, i, int(confusion_matrix[i, j]), va='center', ha='center',color='white', fontsize=14)
    else:
        plt.text(j, i, int(confusion_matrix[i, j]),va='center',ha='center',fontsize=14)   #显示对应的数字
#plt.rcParams['font.sans-serif'] = ['SimHei']

plt.ylabel('True Class',fontsize=14)
plt.xlabel('Predicted Class',fontsize=14)

plt.tight_layout()

plt.show()
