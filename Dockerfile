FROM python:3.10.*
WORKDIR /app
# Clone git repo and install dependencies
RUN git clone
RUN pip install -r requirements.txt
# Run the app
CMD ["python", "main.py"]
