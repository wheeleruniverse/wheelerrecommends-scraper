FROM amazon/aws-lambda-python:3.12

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy application code
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]