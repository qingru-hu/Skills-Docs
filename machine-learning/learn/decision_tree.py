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

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)
dtc_y_predict = dtc.predict(x_test)

from sklearn.metrics import classification_report
print(dtc.score(x_test, y_test))
print(classification_report(y_test, dtc_y_predict))