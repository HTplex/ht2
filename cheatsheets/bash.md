# list of useful bash scripts

## xargs
run a script n times with args
`seq 1000 | xargs -P 64 -I {} sh -c "./sample.sh" `

# peroidically run script
`while true; do ls -1 | wc -l; sleep {wait_time}; done`


# parallel untar
`find . -type f -name '*.tar.gz' -print0 | xargs -0 -P 16 -n1 tar -xvf`

# typical parallel run script

`find /data/datasets_v2/clip_videos_v3/ -type f -name "2016*.mp4" | xargs -I {} -P 6 sh -c "CUDA_VISIBLE_DEVICES=0 python ./spiga/demo/app.py --input {} --outpath /data/datasets_v2/faces_v3/" &`


