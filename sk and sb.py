import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

import seaborn as sns
iris = sns.load_dataset('iris')
import seaborn as sns; sns.set()
sns.pairplot(iris, hue='species', height=3)


X_iris = iris.drop('species', axis=1)
print(X_iris.shape)
y_iris = iris['species']
print(y_iris.shape)
