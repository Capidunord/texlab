#!/bin/sh

apt update
apt upgrade -y
apt install -y texlive-full
apt install -y git python3 python3-pip
python3 -m pip install sympy pygments
cd ..
mkdir /texlab
cp -r . /texlab
cp /texlab/latexmk/.latexmkrc-docker /home/stephane/.latexmkrc
cp /texlab/latexindent/latexindentconfig.yaml /home/stephane/latexindentconfig.yaml
cp /texlab/latexindent/indentconfig_wsl.yaml /home/stephane/indentconfig.yaml