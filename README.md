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