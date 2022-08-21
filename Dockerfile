FROM ubuntu:latest
RUN apt-get update && yes|apt-get upgrade && \
    apt-get install -y wget bzip2 sudo && \
    apt-get install -y emacs nano vim default-jre

RUN adduser --disabled-password --gecos '' sthapa
RUN adduser sthapa sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER sthapa
WORKDIR /home/sthapa/

RUN sudo chmod a+rwx -R /home/sthapa/

RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
RUN bash Anaconda3-2022.05-Linux-x86_64.sh -b
RUN rm Anaconda3-2022.05-Linux-x86_64.sh
ENV PATH /home/sthapa/anaconda3/bin:$PATH

RUN pip install --upgrade pip

RUN jupyter notebook --generate-config --allow-root

RUN sudo apt-get install -y gcc
RUN pip install apache-airflow typing_extensions

ENV AIRFLOW__CORE__DAGS_FOLDER="/home/sthapa/kafka_stock/airflow/dags"
RUN pip install Flask
RUN airflow db init
RUN airflow users  create --role Admin --username admin --email admin@admin.com --firstname admin --lastname admin --password admin

ADD . /home/sthapa/kafka_stock
RUN sudo chmod 777 -R /home/sthapa/kafka_stock

ENV BOKEH_PORT="5006" BOKEH_PREFIX="" BOKEH_LOG_LEVEL="info"

RUN pip install --upgrade -r kafka_stock/requirements.txt

RUN sudo apt-get install -y tmux
ENV NAME kafka_stock