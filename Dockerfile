FROM continuumio/anaconda3:latest
COPY . /Dockers
EXPOSE 8501
WORKDIR /Dockers
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD streamlit run app1.py