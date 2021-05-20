FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

WORKDIR /workspace
RUN chmod -R a+w /workspace

RUN apk --no-cache add musl-dev linux-headers g++

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

#EXPOSE 8000
#CMD ["uvicorn", "main:app",  "--port", "8000", "--host", "0.0.0.0", "--reload"]