from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
# print(breast_cancer)

x = breast_cancer.data
y = breast_cancer.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.preprocessing import StandardScaler
breat_cancer_ss = StandardScaler()
# print(x_train)
x_train = breat_cancer_ss.fit_transform(x_train)
x_test = breat_cancer_ss.fit_transform(x_test)

from sklearn.svm import LinearSVC

lsvc = LinearSVC()
lsvc.fit(x_train, y_train)
lsvc_y_pre = lsvc.predict(x_test)

from sklearn.metrics import classification_report
print(f"Accuracy: {lsvc.score(x_test, y_test)}")
print(classification_report(y_test, lsvc_y_pre, target_names=['benign', 'malignant']))