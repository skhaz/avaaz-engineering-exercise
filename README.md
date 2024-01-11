# Rodrigo Delduca

## Question 1

### Setup

Just run the following command:

```bash
make setup
```

### Running the tests

Just run the following command:

```bash
make tests
```

Open coverage report:

```bash
open htmlcov/index.html
```

### Running locally through Docker compose

Just run the following command:

```bash
make run
```

(Wait for everything to be ready).

Populate the database:

```shell
curl -X POST -H "Content-Type: application/json" -d @input/data.json "http://0.0.0.0:8000/v1/bulk"
```

Query it (do not forget to populate before querying):

```shell
curl "http://localhost:8000/v1/?before=2020-01-01&after=2012-01-01&contains=confort"
```

Get by ID:

```shell
curl "http://localhost:8000/v1/1"
```

### Notes

I tend to like boring code.

I used Pydantic (Flask Pydantic) because I think it's a great tool for validating input and output. I added a caching layer, created a generic decorator, and even used pickle to hash all the parameters, assuming the data changes infrequently, so a cache would be beneficial.

I improved the Docker file to use a multi-stage build and other improvements.

I improved the Docker Compose, added health checks for Redis and MySQL, ensuring the application only starts when both are healthy, thus avoiding crashes at startup due to lack of database connection.

I added some typing, and I know this can be controversial in the Python world; some love it, others hate it.

I created indexes on almost all fields. This could be bad as it might increase the database's disk space, but if that becomes an issue, particularly in production, partial indexes could be used.

I used Clean Architecture and Clean Code moderately. I particularly like the approach of using use cases to keep controllers lean.

Due to lack of time, I only wrote tests for the endpoints, but they cover 99-100%. Normally at work, I write tests 1:1; for every file, there's a test file covering all statements.

There are several things that could be improved, like using Flask Config for configurations.

## Question 2

Consider the following scenario; You were assigned to design and build an application that will act as an API gateway and be used with multiple services that are running on AWS and behind Cloudflare. Please explain how you would approach architecting and rolling out such a system. How would you design the authentication and authorization flows knowing that the gateway will receive requests from users and also handle cross-service communications? What other, if any, security considerations will you take into account?

### Amazon AWS Architecture

In an architecture based on AWS services and using Cloudflare, we can firstly enforce the use of HTTPS and enable HSTS for maximum security on Cloudflare. Additionally, we can enable WAF, anti-DDoS protection, bot protection, and possibly Page Shield.

On the AWS side, we'll have the API Gateway as the entry point, with route definitions, headers, services, CORS, and authentication using authorizers.

For user authentication, we can use Cognito to avoid reinventing the wheel or introducing security vulnerabilities.

For authentication between microservices, we can use a combination of VPC and IAM, ensuring isolation and security by preventing unauthorized service requests.

Communication between microservices can be via HTTP REST or gRPC. The advantage of gRPC is maintaining bidirectional communication and schema version backward compatibility.

Security between microservices can be implemented using mTLS (mutual TLS) among the services.

Monitoring can be handled by AWS CloudTrail and Cloudflare to monitor API usage, usage patterns, and potential threats.

It's important to have rate limiting to prevent abuse, which can be configured in the API Gateway.

Rollout steps:

1. Definition of the API, security protocols, and service integration.

2. Use of Infrastructure as Code (IaC); since we're using Amazon AWS, CloudFormation can be employed.

3. Performance testing could involve using a Locust cluster with various scenarios to assess the stability of the API and its services.

4. Continuous build and deployment using CI/CD tools.

### Kubernetes (alternative) Architecture

An alternative solution would be the use of Kubernetes, which offers the advantage of migrating between clouds or having a multicloud architecture due to the absence of vendor lock-in.

As an entry point, we can use Kong, which serves as a load balancer and API Gateway. It allows for infrastructure as code to define routes, permissions, authorizations, traffic control, IAM, among other things.

For microservices, Horizontal Pod Autoscaling (HPA) or, even better, Kubernetes Event-driven Autoscaling (KEDA) can be used. This enables pods to scale up or down depending on demand, not on load.

Finally, as it is a service that can be accessed both externally and internally, JSON Web Key Set (JWKS) could be employed. With JWKS, when a service is about to send a request to another, it first obtains (and possibly caches for a while) the public keys, signs the message, and sends it. Then, the receiving microservice verifies the JWT token.

For external access, the same JWT mechanism could be used to generate tokens for external clients. When the client makes a request with the token, it is validated.

This exact approach with JWKS was used in a project I participated in (Nations Pro) and worked very well.

AgorCD for continuous deployment and Helm for package management can be used.
