FROM python:3
MAINTAINER Lokesh Kumar

ENV PYTHONBUFFERED 1

WORKDIR /usr/src/resumeparser
COPY requirements.txt ./
COPY . .

RUN pip install - r /requirements.txt
CMD ["python","-m spacy download en"]
CMD ["python","-m nltk.downloader all"]

CMD ["python","manage.py runserver"]
