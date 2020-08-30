FROM python:3.8
EXPOSE 8501
WORKDIR /src
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY /src .
COPY /data ./data
CMD streamlit run app.py --server.port $PORT
#--server.port $PORT