checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi

}
checkroot
pacman -Sy
pacman -S python
pacman -S python3
pacman -S python3-pip
pacman -S php
pacman -S php-curl
pip install --upgrade pip
python3 -m pip install -r requirments.txt
echo "Installed!"
