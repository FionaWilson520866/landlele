FROM python:3.10
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
# Install ffmpeg using apt
RUN apt update && apt install -y ffmpeg
CMD ["python", "bot.py"]

# docker build -t my-python-app .

# docker run -it --rm my-python-app
