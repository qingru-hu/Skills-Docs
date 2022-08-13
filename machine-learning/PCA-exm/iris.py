import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,decomposition

def load_data():
    iris = datasets.load_iris()
    return iris.data, iris.target

def test_PCA(*data):
    x,y = data
    pca = decomposition.PCA(n_components=None)
    pca.fit(x)
    print("可解释的方差占比：%s"%str(pca.explained_variance_ratio_))

x, y = load_data()
print(x[:5])
test_PCA(x, y)

def plot_PCA(*data):
    x, y = data
    pca = decomposition.PCA(n_components=2)
    pca.fit(x)
    x_r = pca.transform(x)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    labels = np.unique(y)
    colors = ['r', 'b', 'y']
    for label in labels:
        pos = (y==label)
        ax.scatter(x_r[pos, 0], x_r[pos, 1], color=colors[label], label='target:%s'%label)

    plt.legend(loc='lower right')
    plt.show()

plot_PCA(x, y)