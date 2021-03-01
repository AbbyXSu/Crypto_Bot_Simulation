FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN apk add jpeg-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5004

CMD ["python","app.py"]


