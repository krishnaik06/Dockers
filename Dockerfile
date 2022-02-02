FROM python:3.8-slim
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install -r requirements.txt
CMD ["python3", "flask_api.py"]
