FROM python:3.6

RUN pip install --upgrade pip

# Install cython, required for compilation
RUN pip install Cython
# Example commands for installing other python packages required for your python code
RUN pip install pyvoronoi==1.0.5
# Install web framework
RUN pip install cherrypy==11.0



WORKDIR /ws
ADD ws.py .
ADD myprocessor.py .
RUN mkdir logs

# Start web service
ENTRYPOINT ["python", "/ws/ws.py"]
CMD ["--logLevel", "INFO"]
