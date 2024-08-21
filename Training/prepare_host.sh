
# install nvidia drivers (if not already)
# sudo apt install nvidia-driver-550 nvidia-dkms-550

# install docker
## uninstall old versions
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

## Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install -y ca-certificates curl python3-pip
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

## Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

## Install the Docker packages. 
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin 


## Enable managing Docker as a non-root user
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker


## Verify that the Docker Engine installation is successful and does not require root by running the hello-world image.
docker run hello-world

## Install cog:
wget  https://cog.run/install.sh -O install_cog.sh
INSTALL_DIR=/usr/local/bin
chmod +x install_cog.sh 
sudo ./install_cog.sh 

# Install the NVIDIA Container Toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# configure Docker to use the NVIDIA Container Runtime.
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# define working directory
WD=~/DLproj
mkdir $WD && cd $WD
mkdir cache

# clone AudioLDM-training-finetuning repo
git clone git@github.com:vodkolav/AudioLDM-training-finetuning.git

# download checkponts and dataset
pip install gdown
PATH=~/.local:$PATH

# checkpoints(7Gb): (https://drive.google.com/file/d/1T6EnuAHIc8ioeZ9kB1OZ_WGgwXAVGOZS/view?usp=drive_link)
gdown --id 1T6EnuAHIc8ioeZ9kB1OZ_WGgwXAVGOZS --output $WD/checkpoints.tar

# preprocessed AudioCaps (30Gb): (https://drive.google.com/file/d/16J1CVu7EZPD_22FxitZ0TpOd__FwzOmx/view?usp=drive_link)
gdown --id 16J1CVu7EZPD_22FxitZ0TpOd__FwzOmx --output $WD/dataset.tar


# extract them to repo/data
tar -xf checkpoints.tar -C $WD/AudioLDM-training-finetuning/data/ 

tar -xf dataset.tar -C $WD/AudioLDM-training-finetuning/data/ 
