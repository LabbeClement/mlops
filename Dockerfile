
FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY webapp.py ./app/

EXPOSE 8963
CMD ["fastapi", "run" , "app/webapp.py,"]
