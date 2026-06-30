# Hostname App

## Build & run:

```bash
docker build -t hostname-app .
```

## Pass hostname explicitly

```bash
docker run -e HOSTNAME=my-machine -p 8080:8080 hostname-app
```

## Or let the container use its own hostname (default Docker behaviour)

```bash
docker run -p 8080:8080 hostname-app
```

And get the page:
```bash
curl localhost:8080
```

## Apply the manifests

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

## Test

kubectl run -it --rm curl --image=curlimages/curl --restart=Never -- curl hostname-app
