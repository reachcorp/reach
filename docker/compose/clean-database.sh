#!/usr/bin/env bash

for DIR in ~/repositories/insight/src/main/docker/compose/graph/cassandra/data ~/repositories/insight/src/main/docker/compose/mongodb/data ~/repositories/insight/src/main/docker/compose/feeder/templates
do
	echo "recreating data directory: $DIR"
	sudo rm -rf $DIR
	mkdir -p $DIR
	sudo echo '*.*' > $DIR/.gitignore
	sudo echo '/**' >> $DIR/.gitignore
done

echo "recreating data directory: ./elk/elasticsearch/data"
sudo rm -rf ~/repositories/insight/src/main/docker/compose/elk/elasticsearch/data
mkdir -p  ~/repositories/insight/src/main/docker/compose/elk/elasticsearch/data

echo "./elk/elasticsearch/data dans .gitignore"
touch ./elk/elasticsearch/data/.gitignore
sudo echo '*.*' > ~/repositories/insight/src/main/docker/compose/elk/elasticsearch/data/.gitignore
sudo echo '/**' >> ~/repositories/insight/src/main/docker/compose/elk/elasticsearch/data/.gitignore

echo "adding exec rights to janus init script"
chmod +x ~/repositories/insight/src/main/docker/compose/graph/janus/init.sh

