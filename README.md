# DeepLearningProject

## Useful comands

Check docker containers and images  
`docker system df -v`  

```{bash}
for container in $(docker ps --all --quiet --format '{{ .Names }}'); do \
    echo "$(docker inspect $container --format '{{.GraphDriver.Data.MergedDir }}' | \
    grep -Po '^.+?(?=/merged)'  ) = $container"; \
done
```

Export cog result as dockerfile  
`cog debug > Dockerfile1`

Cleanup caches of failed builds  
`docker system prune`

`docker rmi $(docker images -f dangling=true -q)`

Start docker sevice  
`systemctl --user start docker`


See what runs on a GPU (continiously, every 1 second)  
`nvidia-smi -l 1`


regex for replace = with == 
(.*)\s=\s"\^?([\d\.]*)

    - "$1==$2


# Valuable forks AudioLDM training:  
- these guys expand the readme a lot, particularly on how to structure your own dataset and train with it  
https://github.com/DCASE2024-Task7-Sound-Scene-Synthesis/AudioLDM-training-finetuning

- Uses it for EEG?   
https://github.com/inogii/AudioLDM-training-finetuning

- Another example for your own dataset  
https://github.com/k1064190/MusicCLAP

- Fixes bug I encountered on librosa  
https://github.com/smrl/AudioLDM-training-finetuning


# Valuable forks AudioSR:

- adds notebooks with user interface  
https://github.com/Nick088Official/versatile_audio_super_resolution

- adds pytorch autocasting (https://wandb.ai/wandb_fc/tips/reports/How-To-Use-Autocast-in-PyTorch--VmlldzoyMTk4NTky)  
https://github.com/bookbot-hive/versatile_audio_super_resolution

- adds a class used to read/write audio file metadata tags.  
https://github.com/smrl/versatile_audio_super_resolution

- adds code to compute metrics  
https://github.com/ghnmqdtg/AudioSR

