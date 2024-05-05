FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
ADD CONFIG.py CONFIG.py
ADD server.py server.py
EXPOSE 80
CMD python -m server.server 80