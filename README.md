# Phan Thanh Tú

**Software engineering intern and new-grad candidate focused on Java backend development** · Hanoi, Vietnam

I build backend systems and like working through what happens when requests are retried, events arrive twice, or several users update the same data.

[Portfolio](https://tus-portfolio.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/phan-thanh-tu/) · [Email](mailto:mudotet@gmail.com)

## Selected projects

### [E-commerce Microservices](https://github.com/mudotet/ecommerce-microservices)

A Java 21 and Spring Boot learning project where Order and Product services coordinate inventory through Kafka.
The inventory consumer stores the result by order ID so replaying an order event returns the previous result without deducting stock again.

[Order workflow](https://github.com/mudotet/ecommerce-microservices#order-workflow) · [Inventory tests](https://github.com/mudotet/ecommerce-microservices/blob/main/product-service/src/test/java/com/mudotet/ecommerce/product/InventoryLockTests.java)

### [Mini Game Server](https://github.com/mudotet/mini-intern-server-project)

A Java game API with login, a daily shop, and a Battle Pass.
The server uses Akka HTTP, Redis, and DynamoDB, and pins the Protobuf contracts in a shared repository so clients can build against a known schema revision.

[Run locally and test](https://github.com/mudotet/mini-intern-server-project/tree/main/server) · [Battle Pass rules](https://github.com/mudotet/mini-intern-server-project/blob/main/server/docs/BATTLE_PASS.md)

### [CivicPath AI](https://github.com/mudotet/AI-guided-public-service-procedures-Lonely-Stone-)

A team hackathon prototype that helps people prepare birth-registration documents.
The FastAPI backend uses deterministic rules to flag missing or conflicting fields and flags uncertain cases for officer review.

[Architecture](https://github.com/mudotet/AI-guided-public-service-procedures-Lonely-Stone-#-architecture) · [Project demo](https://ai-guided-public-service-procedures.vercel.app/)

## Contribution Breakout

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/breakout-dark.svg?v=1" />
  <source media="(prefers-color-scheme: light)" srcset="./images/breakout-light.svg?v=1" />
  <img width="100%" src="./images/breakout-light.svg?v=1" alt="Animated Breakout game based on my GitHub contribution graph" />
</picture>
