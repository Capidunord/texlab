FROM alpine

RUN apk add git python bash py-pip
RUN pip install --upgrade pip
RUN pip install sympy pygments
RUN apk add texlive-full
ADD . texlab
ADD latexmk/.latexmkrc-docker /root/.latexmkrc