# our base image
FROM alpine:3.9

# Install python and pip
RUN apk add --update py3-pip

# install Python modules needed by the Python app
COPY requirements.txt /sentiment_analysis_textblob/
RUN pip3 install --no-cache-dir -r /sentiment_analysis_textblob/requirements.txt
RUN python3 -m textblob.download_corpora


# copy files required for the app to run
#COPY app.py /sentiment_analysis_textblob/
COPY api_app.py /sentiment_analysis_textblob/
COPY templates/index.html /sentiment_analysis_textblob/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
#CMD ["python3", "/sentiment_analysis_textblob/app.py"]
CMD ["python3", "/sentiment_analysis_textblob/api_app.py"]
