ps -ef | grep 8088 | awk '{print $2}' | xargs sudo kill -9
docker ps -a | grep ota_proxy_api | awk '{print $1}' | xargs docker rm
docker image ls | grep ota_proxy_api | awk '{print $1}' | xargs docker image rm