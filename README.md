# Phan Thanh Tu

**Java Backend Engineer | Hanoi, Vietnam**

I build Java services for workflows that need to handle retries and failures reliably, from inventory updates to in-game purchases.
I'm open to backend engineering internships and new-grad roles.

[Portfolio and résumé](https://tus-portfolio.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/phan-thanh-tu/) · [Email](mailto:mudotet@gmail.com)

## Experience

### GearGames · Server Engineer Intern

Implemented Battle Pass mission progression and static and daily shop purchases in a Java game server using Akka and Protocol Buffers.

### PathTech JSC · Backend development

Built protected APIs for real-estate listings, reservations, and bidding, and integrated Stripe Payment Intents and webhooks with NestJS and PostgreSQL.

[View experience and case studies](https://tus-portfolio.vercel.app/)

## Selected projects

### [E-commerce Microservices](https://github.com/mudotet/ecommerce-microservices)

Built a Java 21 and Spring Boot learning project where order and inventory services own separate PostgreSQL databases and coordinate through Kafka.
The inventory service records processing results by order ID so a redelivered event does not deduct stock twice.
Kafka retry topics and dead-letter routing handle processing failures.

[Architecture and order flow](https://github.com/mudotet/ecommerce-microservices#architecture) · [Local setup](https://github.com/mudotet/ecommerce-microservices#run-locally)

### [Mini Game Server](https://github.com/mudotet/mini-intern-server-project/tree/main/server)

Built a Java and Akka HTTP demo with Protobuf APIs for login, shops, and a Free/Premium Battle Pass.
Shop purchases record a receipt by request ID so a retry can return the original result without charging the player twice.

[Server source and setup](https://github.com/mudotet/mini-intern-server-project/tree/main/server) · [Shared Protobuf schemas](https://github.com/mudotet/proto_mini-intern-server-project)

### [CivicPath AI](https://github.com/mudotet/AI-guided-public-service-procedures-Lonely-Stone-)

Led a three-person team that built a Vietnamese birth-registration guide for the AI Innovation Challenge.
The FastAPI backend builds document checklists from case rules and flags missing or conflicting information for the assistant to explain in plain language.

[Live demo](https://ai-guided-public-service-procedures.vercel.app/)

## Contribution Breakout

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/breakout-dark.svg?v=1" />
  <source media="(prefers-color-scheme: light)" srcset="./images/breakout-light.svg?v=1" />
  <img width="100%" src="./images/breakout-light.svg?v=1" alt="Animated Breakout game built from my GitHub contribution graph" />
</picture>
