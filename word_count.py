import findspark
findspark.init('/home/ubuntu/spark-2.1.1-bin-hadoop2.7')
from pyspark import SparkContext

sc = SparkContext(appName="WordCount")

input_file = sc.textFile("words.txt")

map = input_file.flatMap(
    lambda line: line.split(" ")).map(
    lambda word: (word, 1))

counts = map.reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("out")

