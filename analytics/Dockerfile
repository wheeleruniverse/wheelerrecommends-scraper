FROM amazon/aws-lambda-python:3.12

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install AWS Athena ODBC driver
RUN dnf install -y AmazonAthenaODBC-2.X.Y.Z.rpm
RUN ls -lht /opt/athena/odbc/ini/

# copy application code
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]