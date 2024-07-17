FROM amazon/aws-lambda-python:3.12

RUN pip install -r requirements.txt

#RUN dnf install -y \
#    alsa-lib at-spi2-atk atk cups-libs dbus-glib dbus-glib-devel gtk3 jq libXcomposite libXcursor libXdamage libXext \
#    libXi libXrandr libXScrnSaver libXt libXtst mesa-libgbm nss pango unzip xorg-x11-server-Xvfb xorg-x11-xauth

#COPY ./chrome-installer.sh ./chrome-installer.sh
#
#RUN ./chrome-installer.sh
#
#RUN rm ./chrome-installer.sh

COPY classes/ classes

COPY services/ services

COPY handler.py handler.py

RUN ls -lht

CMD [ "handler.main" ]