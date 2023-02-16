FROM python as base
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3 python3-pip
RUN make all

FROM base as test
RUN make test
