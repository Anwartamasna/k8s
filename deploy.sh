#!/usr/bin/env bash
set -e

echo "🚀 Deploying application to Kubernetes..."

# Apply manifests in order
echo "📦 Applying Kubernetes manifests from k8s-manifests/..."
kubectl apply -f k8s-manifests/book_namespace.yaml
kubectl apply -f k8s-manifests/book_deployment.yaml
kubectl apply -f k8s-manifests/book_service.yaml

# Wait for deployment rollout to complete
echo "⏳ Waiting for deployment rollout..."
kubectl rollout status deployment/book-deployment -n book-store --timeout=60s

# Print status of resources
echo "✅ Deployment completed! Current resources in 'book-store' namespace:"
kubectl get all -n book-store
