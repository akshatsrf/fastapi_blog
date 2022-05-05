# 
FROM python:3.8.10

# 
WORKDIR /fastapi

# 
COPY ./requirements.txt /fastapi/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

# 
COPY ./app /fastapi/app

# 
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
