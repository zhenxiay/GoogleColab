FROM ubuntu

RUN apt update

RUN apt install python3-pandas

ENTRYPOINT [ "bash" ] 