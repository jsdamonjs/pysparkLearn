from pyspark.sql import SparkSession
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.classification import LogisticRegression
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("jgj_real_predict") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
schema = StructType([
    StructField("userphone", StringType(), True),
    StructField("rawfeatures", StringType(), True)
])
model_path = '/wls/dev/model'
df = spark.read.option("delimiter","|").option("header","false").schema(schema).csv('/wls/dev/jgj_pj.csv')
vec_model = CountVectorizer.load(model_path+'/shouxian_CountVectorizer')

predict_data = vec_model.transform(df)

lr_model = LogisticRegression.load(model_path+'/shouxian_lr_model')
predict = lr_model.transform(predict_data).select("userphone","predict_proba")
predict.write.csv('/wls/dev/shouxian_score.csv')
