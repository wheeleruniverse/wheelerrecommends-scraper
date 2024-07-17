FROM amazon/aws-lambda-python:3.12

# install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install chrome dependencies
RUN dnf install -y \
    alsa-lib at-spi2-atk atk cups-libs dbus-glib dbus-glib-devel gtk3 jq libXcomposite libXcursor libXdamage libXext \
    libXi libXrandr libXScrnSaver libXt libXtst mesa-libgbm nss pango unzip xorg-x11-server-Xvfb xorg-x11-xauth

# install chrome
COPY chrome-installer.sh chrome-installer.sh
RUN ls -lht
RUN chmod +x chrome-installer.sh
RUN ls -lht
RUN ./chrome-installer.sh

# copy application code
COPY classes/ classes
COPY services/ services
COPY handler.py handler.py

# define the handler
CMD [ "handler.main" ]