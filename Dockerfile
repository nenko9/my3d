FROM python:alpine3.8
EXPOSE 5000
WORKDIR /code
COPY ./code /code 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST='0.0.0.0'
CMD ["flask","run"]