FROM python:3
MAINTAINER Lokesh Kumar

ENV PYTHONBUFFERED 1

WORKDIR /home/anonymous/resumeparser
COPY requirements.txt ./
COPY . .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["python","-m spacy download en"]
CMD ["python","-m nltk.downloader all
CMD ["python","manage.py", "runserver"]
