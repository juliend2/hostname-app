# Hostname App

## Build

```bash
docker build -t hostname-app .
```

## Run

### Pass hostname explicitly

```bash
docker run -e HOSTNAME=my-machine -p 8080:8080 hostname-app
```

### Or let the container use its own hostname (default Docker behaviour)

```bash
docker run -p 8080:8080 hostname-app
```

And get the page:
```bash
curl localhost:8080
```

## Apply the manifests

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Test

```bash
kubectl run -it --rm curl --image=curlimages/curl --restart=Never -- curl hostname-app
```
