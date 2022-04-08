# Information

## Build
sudo docker build --tag python-docker .

## Run
sudo docker run --privileged -d -p 5000:5000 python-docker
-d: detached
--privileged: allow access to GPIO
-p: external/internal ports
python-docker: name of the image

# View running images
sudo docker ps

# Stop running image
sudo docker stop XXXXXX
replace XXXXXX with name found in docker ps command
