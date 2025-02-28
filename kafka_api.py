from configparser import ConfigParser
from confluent_kafka import Producer

from log import logger
# config = {
#     'bootstrap.servers': '172.16.3.171:9092',
#     'client.id': 'python-producer-test'
#     # 'group.id': 'mygroup',
#     # 'auto.offset.reset': 'earliest'
# }

# producer = Producer(config)


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    # else:
    #     print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def send_data_to_kafka(data: dict, config: ConfigParser):
    try:
        config = {
            'bootstrap.servers': config['kafka']['kafka_con_string'],
            'client.id': config['kafka']['kafka_client_id']
            # 'group.id': 'mygroup',
            # 'auto.offset.reset': 'earliest'
            }
        producer = Producer(config)
        for message in data:
            topic = config['kafka']['topic']
            producer.produce(topic, message, callback=delivery_report)
            producer.flush()
    except Exception as e:
        logger.error("Ошибка отправки данных в Kafka\n", e)


if __name__ == '__main__':
    pass
