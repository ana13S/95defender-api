FROM lapidarioz/docker-python-opencv3-dlib

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY ./shape_predictor_68_face_landmarks.dat /app

COPY ./app.py /app

COPY ./mask.png /app

EXPOSE 5000

RUN export FLASK_APP=/app/app.py

CMD flask run --host=0.0.0.0 
