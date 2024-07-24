FROM amazon/aws-lambda-python:3.12

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install AWS Athena ODBC driver
RUN dnf install -y tar wget

RUN wget -q https://ftp.gnu.org/gnu/glibc/glibc-2.40.tar.gz
RUN tar -xvzf glibc-2.40.tar.gz

RUN wget -q https://www.unixodbc.org/unixODBC-2.3.12.tar.gz
RUN tar -xvzf unixODBC-2.3.12.tar.gz

RUN wget -q https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Linux/AmazonAthenaODBC-2.0.3.0.rpm
RUN yes | rpm -Uvh ./AmazonAthenaODBC-2.0.3.0.rpm

RUN ls -lht /opt/athena/odbc/ini/

# copy application code
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]