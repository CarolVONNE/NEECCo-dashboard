FROM python:3.10-bullseye

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8085
ADD . /app/

ARG now
ENV build_date=$now

# Changing to non-root user
RUN useradd -m appUser
USER appUser

CMD ["gunicorn", "-b", "0.0.0.0:8085", "--workers", "2", "index:server"]