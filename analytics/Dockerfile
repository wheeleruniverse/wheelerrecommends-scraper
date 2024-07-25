FROM amazon/aws-lambda-python:3.12

# install AWS Athena ODBC driver
#RUN dnf install -y \
#    gzip libXcomposite libXcursor libXdamage libXext libXi libXrandr libXScrnSaver libXt libXtst tar wget

#RUN wget -q https://rpmfind.net/linux/openmandriva/5.0/repository/aarch64/main/release/lib64unixODBC2-2.3.12-1-omv2390.aarch64.rpm
#RUN yes | rpm -Uvh ./lib64unixODBC2-2.3.12-1-omv2390.aarch64.rpm

#RUN wget -q https://ftp.gnu.org/gnu/glibc/glibc-2.40.tar.gz
#RUN ls -lht
#RUN tar -xvzf glibc-2.40.tar.gz

RUN dnf install -y gzip tar wget
RUN wget -q https://www.unixodbc.org/unixODBC-2.3.12.tar.gz
RUN tar -xzf ./unixODBC-2.3.12.tar.gz
RUN cd unixODBC-2.3.12 && ./configure \
    --disable-drivers \
    --disable-gui \
    --enable-iconv \
    --prefix=/home \
    --sysconfdir=/var/task \
    --with-iconv-char-enc=UTF8 \
    --with-iconv-ucode-enc=UTF16LE

RUN cd unixODBC-2.3.12 && make install

RUN mv /home/* .

RUN ls -lht .

#RUN wget -q https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Linux/AmazonAthenaODBC-2.0.3.0.rpm
#RUN yes | rpm -Uvh ./AmazonAthenaODBC-2.0.3.0.rpm

#RUN ls -lht /opt/athena/odbc/ini/

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy application code
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]