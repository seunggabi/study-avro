import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


def write(name):
    schema = avro.schema.parse(open(f"avsc/{name}.avsc", "rb").read())

    writer = DataFileWriter(open(f"avro/{name}.avro", "wb"), DatumWriter(), schema)
    writer.append({"name": "Alyssa", "favorite_number": 256})
    writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})

    writer.close()


def read(name):
    reader = DataFileReader(open(f"avro/{name}.avro", "rb"), DatumReader())

    for user in reader:
        print(user)

    reader.close()


if __name__ == "__main__":
    name = "user"
    write(name)
    read(name)
