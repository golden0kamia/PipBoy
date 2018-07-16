sudo apt-get update --yes
print("Installing dependencies")
sudo apt-get install python3 python3-tk python3-pil --yes

print("Installing Font")
sudo mkdir /usr/share/fonts/truetype/Poetsen\ One
sudo mv Poetsen\ One /usr/share/fonts/truetype/Poetsen\ One/
