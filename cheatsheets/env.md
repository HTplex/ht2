# pip using alt mirror
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
popular mirrors: https://pypi.org/simple

# enable/disable nvidia mps

sudo nvidia-smi -c EXCLUSIVE_PROCESS
nvidia-cuda-mps-control -d        

ps -ef | grep mps  

sudo nvidia-smi -c DEFAULT      
echo quit | nvidia-cuda-mps-control

