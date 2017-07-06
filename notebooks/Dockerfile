# hash is just to make sure it doesn't change unexpectedly,
# feel free to update to a later version occasionally.
FROM jupyter/scipy-notebook:11be019e4079

USER root

# add installations here
RUN apt-get -y update && apt-get -y install exiftool

USER jovyan

ENV PYTHONPATH $PYTHONPATH:/home/jovyan/work
