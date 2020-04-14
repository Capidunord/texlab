#!/bin/sh

apt update
apt upgrade -y
apt install -y texlive-full
apt install -y git python3 python3-pip
python3 -m pip install sympy pygments
cd ..
rm -rf /texlab
mkdir /texlab
cp -r . /texlab
cp -f /texlab/latexmk/.latexmkrc-docker /home/stephane/.latexmkrc
cp -f /texlab/latexindent/latexindentconfig.yaml /home/stephane/latexindentconfig.yaml
cp -f /texlab/latexindent/indentconfig_wsl.yaml /home/stephane/indentconfig.yaml