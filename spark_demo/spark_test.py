from pyspark.ml.linalg import VectorUDT
from pyspark.sql import SparkSession
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.classification import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType
from pyspark.sql.types import FloatType


spark = SparkSession \
    .builder \
    .appName("jgj_predict") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

data = spark.read.option("delimiter","|").option("header","false").csv('D:\\Users\\JIANGSHUAI516\\Desktop\\msg_train_data.csv')

a = data.selectExpr("_c0 as labels","split(_c1,',') as rawfeatures")
a = a.withColumn("labels",a.labels.cast("double"))
cv = CountVectorizer(inputCol="rawfeatures", outputCol="features")
model = cv.fit(a)
result = model.transform(a)
(trainingData, testData) = result.randomSplit([0.8, 0.2],seed=2)
mlor = LogisticRegression(regParam=1,featuresCol="features",labelCol="labels",probabilityCol="predict_proba")
mlorModel = mlor.fit(trainingData)
coef = mlorModel.coefficients
features_name = model.vocabulary

for j in range(0, len(coef)):
    print (features_name[j]+':'+str(coef[j]))

firstelement=udf(lambda v:float(v[0]),FloatType())
predict = mlorModel.transform(testData).select("labels",firstelement("predict_proba").alias("predict_proba"))
predict.show()
real = testData.select("labels")
labels_predict_pro = predict.rdd.map(lambda x:x.predict_proba[1]).collect()
labels_test = real.rdd.map(lambda x:x.labels).collect()

fpr, tpr, _ = metrics.roc_curve(labels_test, labels_predict_pro)
# calculate_ks(labels_predict_pro,labels_test)
roc_auc = metrics.auc(fpr, tpr)
print("auc:", roc_auc)

plt.title("ROC curve")
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([-0.1, 1.0])
plt.ylim([-0.1, 1.0])
plt.show()


