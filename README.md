# csci250
Course Materials for csci250 Colorado School of Mines

RANDOM STUFF BELOW

**Going Headless**
https://elearning.mines.edu/courses/6667/files/folder/HeadlessDocs?preview=186464

**Vim**

If your using vim raspberry pi OS often defaults python to python3

To check that python3 is enabled use this command: "vim --version | grep python" and you should see a + sign by python.

If no python3 you should be able to get it simply by just running "sudo apt-get install vim-nox"

Alternatively, compile vim from source and use the tag: -with-python3-config-dir=/usr/lib/python3.4.2/config

Syntax highlighting may not work by default. To enable: sudo nano etc/vim/vimrc and uncomment the "syntax on" line and your custom 
vim stuff should now work. I have a .vimrc for python posted as a repo if you want to view the plugins I use.


**MatPlotLib not installing**
After trying each of these make sure to test it (matplotlib may import but have some graphing errors still). Run this code
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

Try these options
1. Installing with Pip3 
$sudo apt-get install python3-pip
$sudo pip3 install matplotlib

if importing matplotlib gives an error (saying it needs cairocffi) then install what it is asking for...
$sudo pip3 install cairocffi


2. Installing from official repository 
$sudo apt-get update
$sudo apt-get matplotlib-python3

3. Source install
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
python3 setup.py build
sudo python3 setup.py install


