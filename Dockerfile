FROM python:3.7
RUN mkdir /code
WORKDIR /code
RUN pip install mysql-connector-python
COPY app.py /code/app.py
CMD python3 app.py

