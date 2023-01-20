FROM python:3.9
RUN mkdir /application
WORKDIR "/application"
# Upgrade pip
RUN pip install --upgrade pip \
# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD main.py /application/
ADD map.py /application/
ADD exceptions.py /application/
CMD [ "python", "main.py" ]