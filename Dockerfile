FROM debian

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y texlive-full
RUN apt-get install -y git python3 python3-pip
RUN python3 -m pip install sympy pygments
ADD . /texlab
ADD latexmk/.latexmkrc-docker /root/.latexmkrc
ADD latexindent/latexindentconfig.yaml /root/latexindentconfig.yaml
ADD latexindent/indentconfig_docker.yaml /root/indentconfig.yaml