FROM ubuntu

RUN apt update

ENTRYPOINT [ "bash" ]

CMD ["/bin/bash"]
