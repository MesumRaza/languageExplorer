FROM python:3.8
EXPOSE 8501
WORKDIR -p /src
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD streamlit run src/app.py