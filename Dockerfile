FROM python:3.13-alpine
 
WORKDIR /app
COPY app.py .
 
ENV HOSTNAME=unknown
ENV PORT=8080
 
EXPOSE 8080
 
CMD ["python", "app.py"]
 
