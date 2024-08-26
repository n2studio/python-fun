# Map Tiles PVC

**_NOTE:_** The Lattice platform and helm chart depends on this tileset being in place and assumes the pvc called 'tilesets-pvc' is available to be mounted. Otherwise, the "tiled" pod will fail to start without any tilesets.

## Overview
This helm chart will create a minimal pod with a PVC containing at least one tileset (e.g. marble512.mbtile) that other pods can then mount and use. 

### Check if the PVC already exists and contains data
```
kubectl get pvc | grep tilesets  # assuming it's called 'tilesets-pvc'
kubectl get pods | grep tilesets  # assuming it's called 'tilesets'
kubectl exec <pod name from above> -- ls -la /tiled/tilesets/  #verify mountpoint
```
### Deleting the PVC if necessary
```
kubectl delete pvc -n <namespace> tilesets-pv-claim --grace-period=0 --force
# oc delete pvc -n minerva-dev tilesets-pv-claim --grace-period=0 --force
```

### Deploy the helm chart
```
# From outside the tilesets chart directory
helm install tilesets ./tilesets
```