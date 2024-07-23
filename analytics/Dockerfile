FROM amazon/aws-lambda-python:3.12

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install AWS Athena ODBC driver
RUN dnf install -y wget
RUN wget -q https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Linux/AmazonAthenaODBC-2.0.3.0.rpm
RUN yes | rpm -i ./AmazonAthenaODBC-2.0.3.0.rpm
RUN ls -lht /opt/athena/odbc/ini/

# copy application code
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]