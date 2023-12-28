FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY input.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python ./Day4.py;cat output.txt