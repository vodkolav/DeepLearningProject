
host_AudioLDM=~/tensor_project/AudioLDM-training-finetuning
host_cache=~/tensor_project/cache

docker run -it -p 5001:5000 --gpus all \
 --env="DISPLAY=172.28.128.1:0" \
 --env="QT_X11_NO_MITSHM=1" \
 --env="HF_HOME=/root/.cache/huggingface" \
 --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
 --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
 --volume="$host_AudioLDM:/root/AudioLDM-training-finetuning" \
 --volume="$host_cache:/root/.cache" \
 --net=host --shm-size=8g --memory="16g" afeka_dl.2
 
