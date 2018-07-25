#sudo apt-get update
echo Installing dependencies
sudo apt-get -y install python3 python3-tk python3-pil libsdl-image1.2-dev libdevil-dev libglc-dev freeglut3-dev libxmu-dev libfribidi-dev libglc-dev freeglut3-dev libgl1-mesa-dev libqt4-dev libgps-dev -y
echo Installing Font
sudo mkdir /usr/share/fonts/truetype/Poetsen\ One/
sudo cp asset/Poetsen\ One.ttf /usr/share/fonts/truetype/Poetsen\ One/
