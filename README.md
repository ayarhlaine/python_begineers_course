Learn Python - Full Course for Beginners [Tutorial]

This is the learning repository for the video of the following link :
https://www.youtube.com/watch?v=rfscVS0vtbw


# How to run the code?

Run the docker container with the following command:
```
docker-compose -f docker/docker-compose.yml up -d
```

Login to the docker container with the following command:
```
docker exec -it docker_turorial /bin/sh
```

Then run the specific file like:
```
python3 hello_world.py
```