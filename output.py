import findspark
import time
findspark.init('/home/ubuntu/spark-2.1.1-bin-hadoop2.7')
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

negative = [line.rstrip('\n') for line in open('negative.txt')]
positive = [line.rstrip('\n') for line in open('positive.txt')]
both = negative + positive
score = 0

def is_useful(check_word):
    for word in both:
        if word == check_word:
            return True
    return False
    
    
def update_score(check_word):
    global score
    with open('score.txt', 'a') as f:
        f.write(str(score)+ '\n')
    for word in positive:
        if word == check_word:
            score += 1
        else:
            score -= 1

sc = SparkContext()
ssc = StreamingContext(sc, 10 ) #.getOrCreate(checkpointPath=None,setupFunc=sc)
sqlContext = SQLContext(sc)

lines = ssc.socketTextStream("ip-172-31-37-210", 5555)
words = lines.flatMap(lambda line: line.split(" "))
useful_words = words.filter(is_useful)
update_score = useful_words.map(update_score).pprint()


ssc.start()    

time.sleep(35)

ssc.stop()



