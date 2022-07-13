FROM python:3.9

COPY ./spotify /source

WORKDIR /source

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver" ,"0.0.0.0:8000"]