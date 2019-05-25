FROM debian

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python git python-pygments
RUN apt-get install -y texlive-full
RUN apt-get install -y python-pip
RUN pip install sympy
ADD . /texlab
ADD latexmk/.latexmkrc /root/.latexmkrc