FROM python:2.7

CMD ['mkdir', '-p', '/opt/dockerflasktesting']
WORKDIR /opt/dockerflasktesting

COPY requirements.txt /opt/dockerflasktesting/requirements.txt
RUN pip install -r /opt/dockerflasktesting/requirements.txt

COPY ./ /opt/dockerflasktesting/
RUN pip install -e .
EXPOSE 5000
# We could run all our tests here. How? :)
CMD ["python","/opt/dockerflasktesting/FlaskHello/hello.py"]