# Tilesets Helm Chart

## Overview
This helm chart is a proof of concept showing the use of an initContainer to copy data into a mounted PVC, the initContainer then shuts down, and then the main container will start up with the same PVC mounted and data available for it to use. 

### Deploy the helm chart
```
# From outside the tilesets chart directory
helm install tilesets ./tilesets
```

### Check if the PVC exists and contains data
```
kubectl get pvc | grep tilesets  # assuming it's called 'tilesets-pvc'
kubectl get pods | grep tilesets  # assuming it's called 'tilesets-*'
kubectl exec <pod name from above> -- ls -la /tiled/tilesets/  #verify mountpoint
```
### Deleting the Pod and PVC if necessary
```
helm delete tilesets
# don't need to delete the pvc if planning to reinstall, but command is here for reference
kubectl delete pvc tilesets-pv-claim   # you might also need '-n <namespace>' 
```

