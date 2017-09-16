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






