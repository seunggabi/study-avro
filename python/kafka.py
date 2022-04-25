import avro
from confluent_kafka.avro import AvroProducer


def on_delivery(err, msg):
    if err is not None:
        print("Message delivery failed: {}".format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))


def schema(name):
    return avro.schema.parse(open(f"avsc/{name}.avsc", "rb").read())


def value():
    return {"name": "Alyssa", "favorite_number": 256}


def produce(name, value):
    avroProducer = AvroProducer(
        {
            "bootstrap.servers": "localhost:9092",
            "on_delivery": on_delivery,
            "schema.registry.url": "http://localhost:8081",
        },
        default_key_schema=None,
        default_value_schema=schema(name),
    )

    avroProducer.produce(topic="test", key=None, value=value)
    avroProducer.flush()


if __name__ == "__main__":
    name = "user"
    produce(name, value())
