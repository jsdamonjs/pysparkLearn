
import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.classification import LogisticRegression
from sklearn import metrics
from pyspark.sql.types import *

def print_to_file(content,file_path):
    f = open (file_path,'a')
    content = content+"\n"
    f.write(content)
    f.close()

spark = SparkSession \
    .builder \
    .appName("jgj_predict") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

schema_1 = StructType([
    StructField("labels", DoubleType(), True),
    StructField("userphone", StringType(), True)
])
schema_2 = StructType([
    StructField("userphone", StringType(), True),
    StructField("rawfeatures", StringType(), True)
])
df_1 = spark.read.option("delimiter","|").option("header","false").schema(schema_1).csv('/wls/dev/jgj_isshouxian_data.csv')
df_2 = spark.read.option("delimiter","|").option("header","false").schema(schema_2).csv('/wls/dev/pj.csv')
df_2 = df_2.selectExpr("userphone as userphone","split(rawfeatures,',') as rawfeatures")
df_2 = df_2.join(df_1, "userphone", "left").select("rawfeatures","labels")
cv = CountVectorizer(inputCol="rawfeatures", outputCol="features")

model = cv.fit(df_2)
model_path = '/wls/dev/model'
model.save(model_path+'/shouxian_CountVectorizer')
result = model.transform(df_2)
(trainingData, testData) = result.randomSplit([0.8, 0.2],seed=2)
mlor = LogisticRegression(regParam=1,featuresCol="features",labelCol="labels",probabilityCol="predict_proba")
mlorModel = mlor.fit(trainingData)
mlorModel.save(model_path+'/shouxian_lr_model')
coef = mlorModel.coefficients
features_name = model.vocabulary

predict = mlorModel.transform(testData).select("predict_proba")
real = testData.select("labels")
labels_predict_pro = predict.rdd.map(lambda x:x.predict_proba[1]).collect()
labels_test = real.rdd.map(lambda x:x.labels).collect()

fpr, tpr, _ = metrics.roc_curve(labels_test, labels_predict_pro)
# calculate_ks(labels_predict_pro,labels_test)
roc_auc = metrics.auc(fpr, tpr)
print("auc:", roc_auc)





