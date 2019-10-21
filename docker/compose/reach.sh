#!/usr/bin/env bash

if [ $# -lt 1 ]; then
  echo "Usage: reach.sh VERB"
  echo
  echo VERB must be one of:
  echo "  • install"
  echo "  • run "
  echo "  • stop "
  echo
  echo "Examples:"
  echo "  • $0 install"
  echo "  • $0 run"
  exit 1
fi

verb=$1
case $verb in
run|install|stop)
  ;;
*)
  echo "error: unknown verb '$verb'"
  exit 1
esac

case $verb in

install)
echo "stopping reach if running"
docker-compose -f reach.yml down
echo "installing reach .. "
#create directory /files OR execute preparation scripts BELOW, before build
docker-compose -f kafka-elastic.yml up -d
docker-compose -f reach.yml -p reach up -d --build
;;

run)

echo "starting reach .. "
docker-compose -f kafka-elastic.yml up -d
docker-compose -f reach.yml -p reach up -d
;;

stop)

echo "stopping reach .. "
docker-compose -f reach.yml -p reach down
docker-compose -f kafka-elastic.yml down
;;
esac
