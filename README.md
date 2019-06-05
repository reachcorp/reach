# reach

## recupération de tous les projets

    setup.py

## install/run/stop de Reach
a. Modifier le fichier .env avec les @IP adéquates, et masquer les modifs de git:
      
    git update-index --assume-unchanged .env

a. install/run/stop

    ./docker/compose/reach.sh {install/run/stop}
    
   Démarre d'abord Kafka/Zookeeper puis Reach. A l'inverse, éteint d'abord Reach puis Kafka/Zook
   
b. par docker compose
    
    docker-compose -f docker/compose/kafka.yml up -d    
    docker-compose -f docker/compose/reach.yml up -d
   
## Déploiement de Reach
![alt text](project/deployment%20template.JPG?raw=true "Deployment Reach")