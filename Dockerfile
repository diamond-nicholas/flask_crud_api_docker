FROM python:3.9.13

COPY requirement.txt .

RUN pip3 install -r requirement.txt

COPY . .

EXPOSE 80

CMD ['flask', 'run', '--host-0.0.0.0', '--port-80']