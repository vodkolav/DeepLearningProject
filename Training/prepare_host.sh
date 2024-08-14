
# install nvidia drivers (if not already)
# sudo apt install nvidia-driver-550 nvidia-dkms-550

# install docker
## uninstall old versions
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

## Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
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


## Verify that the Docker Engine installation is successful by running the hello-world image.
sudo docker run hello-world


# define working directory
WD=~/DLproj
mkdir $WD && cd $WD

# clone AudioLDM-training-finetuning repo
git clone https://github.com/haoheliu/AudioLDM-training-finetuning.git

# download checkponts and dataset
pip install gdown

# checkpoints(7Gb): (https://drive.google.com/file/d/1T6EnuAHIc8ioeZ9kB1OZ_WGgwXAVGOZS/view?usp=drive_link)
gdown --id 1T6EnuAHIc8ioeZ9kB1OZ_WGgwXAVGOZS --output checkpoints.tar

# preprocessed AudioCaps (30Gb): (https://drive.google.com/file/d/16J1CVu7EZPD_22FxitZ0TpOd__FwzOmx/view?usp=drive_link)
gdown --id 16J1CVu7EZPD_22FxitZ0TpOd__FwzOmx --output dataset.tar


# extract them to repo/data
tar -xf checkpoints.tar -C AudioLDM-training-finetuning/data/ --strip-components=1

tar -xf dataset.tar -C AudioLDM-training-finetuning/data/ --strip-components=1