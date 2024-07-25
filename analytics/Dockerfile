FROM amazon/aws-lambda-python:3.12

# install odbc dependencies
RUN dnf install -y gcc gzip libX11 libXext tar wget

# install unixODBC
RUN wget -q https://www.unixodbc.org/unixODBC-2.3.12.tar.gz \
    && tar -xzf ./unixODBC-2.3.12.tar.gz \
    && cd unixODBC-2.3.12 \
    && ./configure \
    --disable-drivers \
    --disable-gui \
    --enable-iconv \
    --prefix=/home \
    --sysconfdir=/var/task \
    --with-iconv-char-enc=UTF8 \
    --with-iconv-ucode-enc=UTF16LE \
    && make install \
    && cd .. \
    && mv /home/* . \
    && mv unixODBC-2.3.12 unixODBC-2.3.12.tar.gz /tmp \
    && ./bin/odbcinst -j

# copy odbc config files
COPY odbc.ini odbc.ini
COPY odbcinst.ini odbcinst.ini

# install AmazonAthenaODBC
RUN wget -q https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Linux/AmazonAthenaODBC-2.0.3.0.rpm
RUN yes | rpm -Uvh --nodeps ./AmazonAthenaODBC-2.0.3.0.rpm

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy application code
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]