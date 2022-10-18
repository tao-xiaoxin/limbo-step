FROM python:3.7-alpine


RUN apk update \
    && apk --update add --no-cache gcc \
    && apk --update add --no-cache g++ \
    && apk --update add --no-cache tzdata \
    && apk --update add --no-cache libffi-dev \
    && apk --update add --no-cache libxslt-dev \
    && apk --update add --no-cache jpeg-dev

ENV  TIME_ZONE Asia/Shanghai
ENV PIPURL "https://pypi.tuna.tsinghua.edu.cn/simple"

RUN echo "${TIME_ZONE}" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime

COPY . /app
WORKDIR /app

RUN pip --no-cache-dir install  -i ${PIPURL} --upgrade pip \
    && pip --no-cache-dir install  -i ${PIPURL} -r requirement/requirement-dev.txt \
    && pip --no-cache-dir install  -i ${PIPURL} gunicorn \
    && chmod +x start.sh
CMD ./start.sh