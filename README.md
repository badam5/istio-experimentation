# Istio Experimentation
Here's how I run istio locally to figure out how it works.

### Installing `minikube` and `kubectl`

Follow the Kubernetes [docs](https://kubernetes.io/docs/tasks/tools/install-minikube/)
to install `minikube` and `kubectl`. (I chose VirtualBox as a hypervisor.)

On my system:

```
$ minikube version
minikube version: v0.32.0
```
To check the `kubectl` version, you must be running a cluster with minikube:

```
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"13", GitVersion:"v1.13.1", GitCommit:"eec55b9ba98609a46fee712359c7b5b365bdd920", GitTreeState:"clean", BuildDate:"2019-01-10T01:46:17Z", GoVersion:"go1.11.4", Compiler:"gc", Platform:"darwin/amd64"}
Server Version: version.Info{Major:"1", Minor:"9", GitVersion:"v1.9.4", GitCommit:"bee2d1505c4fe820744d26d41ecd3fdd4a3d6546", GitTreeState:"clean", BuildDate:"2018-03-12T16:21:35Z", GoVersion:"go1.9.3", Compiler:"gc", Platform:"linux/amd64"}
```

### Running minikube for istio

The istio docs outline [how to run minikube](https://istio.io/docs/setup/kubernetes/platform-setup/minikube/).

I ended up using the following command, omitting the cert configs:

```
minikube start --memory=8192 --cpus=4 --kubernetes-version=v1.9.4 \
    --extra-config=apiserver.admission-control="NamespaceLifecycle,LimitRanger,ServiceAccount,PersistentVolumeLabel,DefaultStorageClass,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota" \
    --vm-driver=virtualbox
```

### Installing istio

Follow the docs for [installing istio with Helm](https://istio.io/docs/setup/kubernetes/helm-install/).

First, download:

```
$ curl -L https://git.io/getLatestIstio | sh -
$ mv istio-1.0.5/bin/istioctl /usr/local/bin/
$ istioctl version
Version: 1.0.5
...
```

Next, create and apply the yamls. Make any changes you want to `istio.yaml`
before deploying it. I disabled the egress gateway for my experiments.

```
$ cd istio-1.0.5/
$ helm template install/kubernetes/helm/istio --name istio --namespace istio-system > istio.yaml
$ kubectl create namespace istio-system
$ kubectl apply -f istio.yaml
```
