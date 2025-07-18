FROM public.ecr.aws/lambda/python:3.12

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
    && mv unixODBC-2.3.12 unixODBC-2.3.12.tar.gz /tmp

# install AmazonAthenaODBC
RUN wget -q https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Linux/AmazonAthenaODBC-2.0.3.0.rpm \
    && yes | rpm -Uvh --nodeps ./AmazonAthenaODBC-2.0.3.0.rpm \
    && rm AmazonAthenaODBC-2.0.3.0.rpm

# copy odbc config files
COPY odbc.ini /opt/athena/odbc/ini/odbc.ini
COPY odbcinst.ini /opt/athena/odbc/ini/odbcinst.ini

# configure odbc environment variables
ENV ODBCINI=/opt/athena/odbc/ini/odbc.ini
ENV ODBCSYSINI=/opt/athena/odbc/ini
RUN ./bin/odbcinst -j

# install python dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

# copy application code
COPY handler.py ${LAMBDA_TASK_ROOT}

# define the handler
CMD [ "handler.main" ]