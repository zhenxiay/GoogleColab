FROM ubuntu

RUN apt install python3-pandas

ENTRYPOINT [ "bash" ] 