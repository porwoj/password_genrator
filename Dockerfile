FROM python:3.11.3-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY generate_password.py generate_password.py
ENTRYPOINT ["python3","generate_password.py"]
CMD ["-h"]
