# Phan Thanh Tu

**Backend Software Engineering · Java & Spring Boot**

I’m Tú, an IT Engineering student in Hanoi, Vietnam.
I build Java backend systems and work on how they handle concurrent requests, retries, and failures.
I’m open to software engineering internships and new-grad roles with a backend focus.

[Portfolio](https://tus-portfolio.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/phan-thanh-tu/) · [Email](mailto:mudotet@gmail.com)

## Selected projects

### E-commerce Microservices

A Spring Boot backend that coordinates orders and inventory across services using Kafka.
It records processing results by order ID to avoid deducting stock twice when Kafka redelivers an event, and uses database row locks to protect stock updates when orders arrive concurrently.

**Java 21 · Spring Boot · Kafka · PostgreSQL · Redis**

[Source code](https://github.com/mudotet/ecommerce-microservices) · [Order workflow](https://github.com/mudotet/ecommerce-microservices#order-workflow)

### Mini Game Server

A Java game backend with Protobuf APIs for login, shop purchases, and Battle Pass progression and reward claims.
The repository includes a Docker Compose setup, Swagger UI, and a script that walks through the Battle Pass flow.

**Java · Akka HTTP · Protobuf · Redis · DynamoDB**

[Source code and local setup](https://github.com/mudotet/mini-intern-server-project/tree/main/server#mini-game-server) · [Battle Pass demo](https://github.com/mudotet/mini-intern-server-project/tree/main/server#battle-pass-demo)

### HUMG Regulation Assistant

An assistant that helps students find answers in university regulations.
It retrieves relevant passages from PDFs and cites the source so students can check the original wording.

[Open the assistant](https://humg-ai-server-beryl.vercel.app/)

## More projects

- [Identity Service](https://github.com/mudotet/identity_services) - A Spring Boot service for user authentication and role-based access.
- [Invoice Extraction](https://github.com/mudotet/Invoice_Extraction_Project) - Extracts structured fields from invoice images and exports them to JSON or CSV.
- [AI Birth Registration Guide](https://ai-guided-public-service-procedures.vercel.app/) - Walks users through the documents and steps for birth registration.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/dark.svg?v=4" />
  <source media="(prefers-color-scheme: light)" srcset="./images/light.svg?v=4" />
  <img width="100%" src="./images/dark.svg?v=4" alt="Phan Thanh Tu, Java Backend Developer" />
</picture>
