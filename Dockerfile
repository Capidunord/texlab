FROM archlinux/base

RUN pacman -Syu --noconfirm
RUN pacman -Syu python python-pip git --noconfirm
RUN pip install sympy
RUN pacman -Syu texlive-most --noconfirm
RUN pacman -Syu tar --noconfirm
ADD . /texlab
ADD latexmk/.latexmkrc /root/.latexmkrc
RUN pacman -Syu python-pygments