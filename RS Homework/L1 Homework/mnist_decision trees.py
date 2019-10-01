from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics
from sklearn.datasets import load_digits

#导入mnist数据集
digits = load_digits()
#指定样本集digits_x
digits_x = digits.data
#指定样本集标签digits_y
digits_y = digits.target

#划分训练集（75%样本条目数）和测试集（25%样本条目数）
train_x, test_x, train_y, test_y = train_test_split(digits_x, digits_y, test_size = 0.25)

#实例化sd进行Z-score进行数据标准化
sd = preprocessing.StandardScaler()
#训练集标准化
train_sd_x = sd.fit_transform(train_x)
#测试集标准化
test_sd_x = sd.transform(test_x)

#实例化DecisionTree算法
dt = DecisionTreeClassifier()
#利用DecisionTree训练模型（未进行Z-score标准化的样本集train_x + 样本标签train_y）
dt.fit(train_x, train_y)
#预测样本集（未进行Z-score标准化）
bef_sd_result = dt.predict(test_x)

#利用DecisionTree训练模型（已进行Z-score标准化的样本集train_sd_x + 样本标签train_y）
dt.fit(train_sd_x, train_y)
#预测样本集（已进行Z-score标准化）
aft_sd_result = dt.predict(test_sd_x)

#输出进行Z-score标准化与未进行Z-score标准化的样本数据预测准确率对比
print('accuracy before preprocessing: %.2f%%' % (metrics.accuracy_score(bef_sd_result, test_y) * 100),
      '\naccuracy after preprocessing: %.2f%%' % (metrics.accuracy_score(aft_sd_result, test_y) * 100))
#输出进行Z-score标准化与未进行Z-score标准化的样本数据召回率对比
print('recall before preprocessing: %.2f%%' % (metrics.recall_score(bef_sd_result, test_y, average = 'macro') * 100),
      '\nrecall after preprocessing: %.2f%%' % (metrics.recall_score(aft_sd_result, test_y, average = 'macro') * 100))

