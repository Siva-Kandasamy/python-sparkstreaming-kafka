# sparkstreaming
This project is to demonstrate integrating apache Spark streaming with Apache Kafka

data streaming nano degree: SF Crime Statistics with Spark Streaming 

Beginning the Project
This project includes creating topics, starting Zookeeper and Kafka servers, and Kafka bootstrap server. This required choosing a port number (e.g., 9092, 9093..) for Kafka topic used in this project, and come up with a Kafka topic name and modify the zookeeper.properties and server.properties appropriately.

1. Install requirements using the provided ./start.sh script.

2. Following .py files are created as part of this project: 

producer_server.py
data_stream.py
kafka_server.py
consumer_server.py

3.  verify the port number: 2181 in config/zookeeper.properties
    verify the port number: 9092 in config/server.properties

Note:
To avoid facing below error, add offsets.topic.replication.factor=1 on server.properties
ERROR [KafkaApi-0] Number of alive brokers '1' does not meet the required replication factor '3' for the offsets topic (configured via 'offsets.topic.replication.factor'). This error can be ignored if the cluster is starting up and not all brokers are up yet. (kafka.server.KafkaApis)

4. After the port numbers are modified execute the following commands in separate terminals in order:
/usr/bin/zookeeper-server-start config/zookeeper.properties
/usr/bin/kafka-server-start config/server.properties

5. From workspace, run command: python producer_server.py to setup the kafka producer server

6. From workspace, run command: python kafka_server.py to ingest the json file:police-department-calls-for-service.json into kafka topic <our own topic name>

7. To validate if kafka produces the message to kafka topic, run the following consumer console command:
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic “org.udacity.kafka.sfcrime.policedepartment” --from-beginning

8. Script data_stream.py is to ingest the radio_code.json file into spark DF via spark streaming

9. Run the command: spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
  Changing following few parameters will increase parallelism and throughput 
  For ex: With the variations on applications using maxRatePerPartition & Trigger, noticed the progress report changes the number of rows processed. 

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
          spark.conf.set("spark.sql.shuffle.partitions", 6)
          spark.conf.set("spark.executor.memory", "2g")
          spark.default.parallelism
  To use the full cluster the level of parallelism of each program should be high enough. According to the size of the file, Spark sets the number of “Map” task to run on each file. The level of parallelism can be passed as a second argument. We can set the config property spark.default.parallelism to change the default.
          

