import numpy as np
"""
confusion_matrix = [[6,0,0,0,0], 
                    [0,62,1,1,0], 
                    [0,0,30,0,0], 
                    [0,1,0,41,0], 
                    [0,0,0,0,2]]
"""
#
confusion_matrix = [[67,0,0], 
                    [2,71,4], 
                    [0,2,64]]


confusion_matrix=np.matrix(confusion_matrix)
FP = confusion_matrix.sum(axis=0) - np.diag(confusion_matrix)  
FN = confusion_matrix.sum(axis=1) - np.diag(confusion_matrix)
TP = np.diag(confusion_matrix)
TN = confusion_matrix.sum() - (FP + FN + TP)

# Sensitivity, hit rate, recall, or true positive rate
TPR = TP/(TP+FN)
# Specificity or true negative rate
TNR = TN/(TN+FP) 
# Precision or positive predictive value
PPV = TP/(TP+FP)
# Negative predictive value
NPV = TN/(TN+FN)
# Fall out or false positive rate
FPR = FP/(FP+TN)
# False negative rate
FNR = FN/(TP+FN)
# False discovery rate
FDR = FP/(TP+FP)

# Overall accuracy
ACC = (TP+TN)/(TP+FP+FN+TN)

print(TPR)
#This return:
"""
[[1.         1.05970149 0.95522388]
 [0.87012987 0.92207792 0.83116883]
 [1.01515152 1.07575758 0.96969697]]

"""
#Recall from pycm => 1.0           0.92208       0.9697
