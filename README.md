# Hostname App

## Build

```bash
docker build -t hostname-app .
```

## Run (in docker)

Pass hostname explicitly:

```bash
docker run -e HOSTNAME=my-machine -p 8080:8080 hostname-app
```

And get the page:

```bash
curl localhost:8080
```

## Apply the k8s manifests

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

or

```bash
make apply
```

## Test

```bash
curl http://<ip>:30001/
```
