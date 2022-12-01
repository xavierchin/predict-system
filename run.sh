docker run --rm -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=$DISPLAY \
    -u qtuser \
    predict/system:latest python3.7 /usr/local/predict-system/system_main.py
