
# Production Platform Decision: Amazon EKS vs Amazon ECS with Fargate

## 1. Decision

The team recommends Amazon Elastic Kubernetes Service (Amazon EKS) for the production environment.

## 2. Project Context

The project uses a hybrid cloud-native architecture:
- K3s Kubernetes cluster on the Center's virtualization hosts for development and staging.
- AWS cloud infrastructure for production deployment.
- GitHub Actions for CI/CD pipelines.
- Amazon ECR as the private container image registry.

## 3. Why We Choose Amazon EKS

The main reason for selecting EKS is consistency between development, staging, and production environments.

Our development and staging environments use K3s, which is Kubernetes-based. Amazon EKS also uses Kubernetes.

This allows the team to:
- Reuse Kubernetes deployment manifests.
- Maintain consistent deployment workflows.
- Use Kubernetes namespaces, ConfigMaps, Secrets and RBAC.
- Reduce differences between development and production.
- Use Kubernetes knowledge already developed by the team.

## 4. EKS vs ECS with Fargate

| Criteria | Amazon EKS | Amazon ECS with Fargate |
|---|---|---|
| Kubernetes support | Yes | No |
| Kubernetes manifest reuse | Yes, with appropriate adjustments | No, requires ECS task definitions |
| Operational complexity | Higher | Lower |
| Integration with K3s | Strong | Less direct |
| Infrastructure management | AWS manages the control plane | AWS manages the serverless task infrastructure |

## 5. Trade-offs

Amazon EKS provides Kubernetes compatibility but introduces additional operational complexity and costs.

Amazon ECS with Fargate is simpler to operate and reduces infrastructure management. However, it would require a separate ECS deployment configuration instead of directly reusing Kubernetes manifests.

The team accepts the additional complexity of EKS because consistency with the existing K3s environment is important.

## 6. Security Considerations

- Use IAM least-privilege permissions.
- Enable MFA for human AWS accounts.
- Store credentials in GitHub Actions Secrets or use OIDC.
- Do not store credentials in source code or Docker images.
- Scan and sign container images before deployment.
- Use version-specific image tags instead of latest.

## 7. Conclusion

Amazon EKS is the recommended production platform because it provides a Kubernetes-based environment consistent with the project's existing K3s development and staging infrastructure.

The final implementation should also consider AWS costs, team expertise, and operational capacity.
