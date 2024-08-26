
host_AudioLDM=~/DLproj/AudioLDM-training-finetuning
host_cache=~/DLproj/cache

docker run -p 5001:5000 --gpus all \
 --env="DISPLAY=172.28.128.1:0" \
 --env="QT_X11_NO_MITSHM=1" \
 --env="HF_HOME=/root/.cache/huggingface" \
 --env="PYTHONPATH=/src/AudioLDM-training-finetuning" \
 --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
 --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
 --volume="$host_AudioLDM:/src/AudioLDM-training-finetuning" \
 --volume="$host_cache:/root/.cache" \
 --net=host --shm-size=8g --memory="30g" afeka_dl.2 
