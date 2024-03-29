# 
FROM python:3.8.10

# 
WORKDIR /fastapi

# 
COPY ./requirements.txt /fastapi/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

# 
COPY ./* /fastapi/

# 
CMD ["uvicorn", "blog_project.main:app", "--host", "0.0.0.0", "--port", "80"]
