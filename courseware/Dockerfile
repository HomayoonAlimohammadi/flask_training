FROM python:3.8

ENV FLASK_APP=main
WORKDIR /courseware
COPY ./requirements.txt /courseware
RUN pip install -r requirements.txt
COPY . /courseware
CMD ["flask", "run", "-p", "80", "-h", "0.0.0.0"]