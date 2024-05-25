**Real Time Data Ingestion Kafka**

A beginner-level project demonstrating real-time data ingestion using Apache Kafka. 
This project includes a producer script to send messages to a Kafka topic and a consumer script to read messages from the topic,
all implemented in Python.

**What is Apache Kafka?**

Apache kafka is a distributed real time streaming framework that 
stores ordered sequence of events in logs often called topics. 
Programs can consume these events, process and generate new 
events in another topic. There is no rule for topics to be small 
or large and topics can hold events for a few hours or hundreds of 
years if required. 

Kafka connect is usually used to be able to integrate with legacy systems. There are a large number of pluggable modules
both open source or commercial which can be deployed to integrate with legacy systems.This 
is done in a declarative way without writing any additional code. You just need 
to configure and deploy them. 

Kafka streams is a java API that can help aggregate, group, join or filter multiple events
without writing extensive code within the programs or services that consumes events from topics. 

**Steps**

1. Create a repository on the local computer named "real-time-data-ingestion-kafka" and publish it on Github. 
2. Create a new branch called "feature/init-setup" from the main branch. 
3. Add a README.md to document learnings and steps to complete the project. 
4. This project used PyCharm as an IDE and Anaconda as the distribution for Python.
5. Create a separate conda environment for the project.
   `conda create --name kafka-env python=3.10`
6. Activate the conda environment. 
   `conda activate kafka-env`
7. Check Java version to make sure that 8+ version is installed. Open command prompt and
type `java --version`. It should return a similar message as in the image. 
![img.png](images/check_java_version.png)
8. Go to https://www.apache.org/dyn/closer.cgi?path=/kafka/3.7.0/kafka_2.13-3.7.0.tgz, 
download the latest kafka release and extract content. 
9. Open window powershell and go to the directory where kafka was extracted. 
`cd kafka_2.13-3.7.0/kafka_2.13-3.7.0`
10. Run Kafka with zookeeper. Start the Zookeeper service.
`bin/zookeeper-server-start.sh config/zookeeper.propertie`
11. Now start the kafka broker service. 
`bin/kafka-server-start.sh config/server.properties`