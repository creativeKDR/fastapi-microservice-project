FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY . /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]