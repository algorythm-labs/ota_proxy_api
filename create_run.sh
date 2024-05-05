docker build -f Dockerfile . -t ota_proxy_api
docker run -p 80:80 ota_proxy_api