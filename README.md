### docs
- https://avro.apache.org/docs/current/gettingstartedpython.html
- https://github.com/confluentinc/confluent-kafka-python
- https://hevodata.com/learn/kafka-schema-registry

### dir
- avsc
- avro

### start
- https://github.com/confluentinc/confluent-kafka-python/issues/184
```
# ~/.zshrc
C_INCLUDE_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/include/
export C_INCLUDE_PATH
LIBRARY_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/lib
export LIBRARY_PATH
```
```shell
cd python
pip3 install -r requirements.txt 
```
- [`#include <librdkafka/rdkafka.h> error: command '/usr/bin/clang' failed with exit code 1`](https://github.com/confluentinc/confluent-kafka-python/issues/184)
```shell
brew install zookeeper
brew install kafka

brew services restart zookeeper
brew services restart kafka

vi /opt/homebrew/etc/zookeeper/zoo.cfg
admin.serverPort=8082 # default: 8080

sudo vi /etc/hosts
127.0.0.1 host.docker.internal

vi /opt/homebrew/etc/kafka/server.properties
listeners=PLAINTEXT://localhost:9092
advertised.listeners=PLAINTEXT://host.docker.internal:9092


brew install librdkafka

C_INCLUDE_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/include/
export C_INCLUDE_PATH
LIBRARY_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/lib
export LIBRARY_PATH
```
```shell
docker run \
  --name cp-schema-registry \
  -d \
  -p 8081:8081 \
  -e SCHEMA_REGISTRY_KAFKASTORE_CONNECTION_URL=host.docker.internal:2181 \
  -e SCHEMA_REGISTRY_HOST_NAME=localhost \
  -e SCHEMA_REGISTRY_LISTENERS=http://0.0.0.0:8081 \
  -e SCHEMA_REGISTRY_DEBUG=true \
  confluentinc/cp-schema-registry:5.3.2
```
