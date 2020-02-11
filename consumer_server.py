# Please complete the TODO items in the code

import asyncio


from kafka import KafkaConsumer
#from kafka.client_async import KafkaClient, selector
import json
import time

#consumer = KafkaConsumer("org.udacity.kafka.sfcrime.policedepartment")

BROKER_URL = "localhost:9092"


async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    # Sleep for a few seconds to give the producer time to create some data
    await asyncio.sleep(2.5)

    # TODO: Set the auto offset reset to earliest
    #       See: https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    #c = KafkaConsumer(
     #   {
      #      "bootstrap.servers": BROKER_URL,
       #     "group.id": "siva_101",
        #    # TODO
         #   "auto.offset.reset": "earliest"
        #}
    #)

    c = KafkaConsumer(topic_name,
                        group_id='siva_101',
                        bootstrap_servers=BROKER_URL,
                        auto_offset_reset='earliest', enable_auto_commit=False
                     )
    
    for message in c:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

def main():
    
    """Runs the exercise"""
    asyncio.run(consume("org.udacity.kafka.sfcrime.policedepartment"))



if __name__ == "__main__":
    main()

