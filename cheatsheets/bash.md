# list of useful bash scripts

## xargs
run a script n times with args
`seq 1000 | xargs -P 64 -I {} sh -c "./sample.sh" `

# peroidically run script
`while true; do ls -1 | wc -l; sleep {wait_time}; done`


# parallel zip

`find /path/to/Folder -maxdepth 1 -type d -name 'chunk_*' | parallel "zip -r {}.zip {} && rm -rf {}"`

# parallel untar
`find . -type f -name '*.tar.gz' -print0 | xargs -0 -P 16 -n1 tar -xvf`


