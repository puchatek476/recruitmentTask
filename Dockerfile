FROM python:3.9
RUN mkdir /application
WORKDIR "/application"
RUN pip install --upgrade pip \
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD main.py /application/
ADD map.py /application/
ADD exceptions.py /application/
ENTRYPOINT ["python", "main.py"]