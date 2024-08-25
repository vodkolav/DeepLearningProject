
host_cache=~/DLproj/cache

docker run -d -p 5003:5000 --gpus all  --gpus all \
 --env="HF_HOME=/root/.cache/huggingface" \
 --volume="$host_cache:/root/.cache" \
 cog-versatileaudiosuperresolut && detach


curl http://localhost:5003/predictions -X POST \
    -H 'Content-Type: application/json' \
    -d '{"input": {"input_file": "https://audioldm.github.io/audiosr/vis_demo/speech_resunet_1.wav"}}' \
    > sred.wav

   