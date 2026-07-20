<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/profile-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./images/profile-light.svg" />
  <img
    src="./images/profile-dark.svg"
    width="100%"
    alt="Phan Thanh Tu — Java Backend Developer"
  />
</picture>

<p align="center">
  <kbd>OPEN TO JAVA BACKEND INTERN / FRESHER OPPORTUNITIES</kbd>
</p>

<p align="center">
  <a href="https://tus-portfolio.vercel.app/"><strong>Portfolio</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/mudotet"><strong>GitHub</strong></a>
  &nbsp;•&nbsp;
  <a href="https://www.linkedin.com/in/t%C3%BA-phan-203970327/"><strong>LinkedIn</strong></a>
  &nbsp;•&nbsp;
  <a href="mailto:mudotet@gmail.com"><strong>Email</strong></a>
</p>

---

## `01. system.identity`

```yaml
developer:
  name: "Phan Thanh Tu"
  role: "Java Backend Developer"
  direction: "Backend-Focused Full-Stack Engineer"
  location: "Hanoi, Vietnam"
  education: "Final-year IT Engineering Student"

current_focus:
  - "Secure and maintainable Spring Boot services"
  - "REST API design and database-backed applications"
  - "Authentication, authorization and data consistency"
  - "AI services integrated into real-world products"

opportunity:
  target: "Java Backend Intern / Fresher"
  availability: "Open to opportunities"
```

I build backend systems that turn product requirements into clear APIs, reliable data flows and maintainable application code.

My main direction is **Java and Spring Boot**, with practical experience across authentication, relational databases, caching, containerized development and AI-service integration.

---

## `02. engineering.focus`

| Area                   | What I work on                                                                                |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| **API Engineering**    | RESTful endpoints, DTO design, validation, exception handling and clear API contracts         |
| **Security**           | Spring Security, JWT authentication, refresh tokens, RBAC and OAuth2 concepts                 |
| **Data Layer**         | Relational modelling, JPA/Hibernate, PostgreSQL, MySQL, Redis and transaction-aware workflows |
| **System Integration** | Connecting Spring Boot applications with Python/FastAPI AI services                           |
| **Delivery**           | Dockerized environments, Maven builds, Git workflows and OpenAPI documentation                |

### Principles I try to follow

```text
clear contracts       > hidden assumptions
simple architecture   > unnecessary complexity
validated boundaries  > debugging corrupted data later
secure defaults       > security added at the end
working software      > impressive-looking demos
```

---

## `03. backend.architecture`

A typical system I enjoy building looks like this:

```text
                         ┌─────────────────────────┐
                         │      Web / Mobile       │
                         │        Client           │
                         └────────────┬────────────┘
                                      │
                                  REST / JSON
                                      │
                                      ▼
┌───────────────────────────────────────────────────────────────┐
│                     SPRING BOOT API                           │
│                                                               │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────┐ │
│  │   Controllers   │──▶│    Services     │──▶│ Repositories│ │
│  │ DTO + Validation│   │ Business Rules  │   │  JPA / SQL  │ │
│  └─────────────────┘   └────────┬────────┘   └──────┬──────┘ │
│                                 │                   │        │
│  ┌─────────────────┐            │             ┌─────▼──────┐ │
│  │ Security Layer  │            │             │ PostgreSQL │ │
│  │ JWT · RBAC      │            │             │   MySQL    │ │
│  │ OAuth2          │            │             └────────────┘ │
│  └─────────────────┘            │                              │
└─────────────────────────────────┼──────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
              ┌─────▼─────┐              ┌──────▼────────┐
              │   Redis   │              │ FastAPI / AI  │
              │ Cache/Data│              │ OCR · RAG · ML│
              └───────────┘              └───────────────┘
```

The diagram reflects the areas I am actively strengthening: separation of concerns, secure request flows, predictable persistence and practical AI integration.

---

## `04. experience.snapshot`

### Backend development in a real product environment

During my Full-Stack Developer Internship at **PathTech JSC**, I contributed to backend services for the **NYALA real-estate auction platform**.

```text
NestJS · PostgreSQL · Redis · JWT · Role-Based Access Control
Stripe Payments · Webhooks · REST APIs · Git Collaboration
```

My work exposed me to the difference between building a classroom feature and contributing to a system with authentication, payments, shared data and real product requirements.

### Community and product building

* Team Lead — **GuideLens AI**
* Third Place — **Codex Community Hackathon**
* Interested in AI-native applications that solve practical user problems rather than adding AI only as a presentation feature

---

## `05. selected.builds`

### [`identity_services`](https://github.com/mudotet/identity_services)

> A Spring Boot identity service focused on authentication and authorization foundations.

```text
Java 17 · Spring Boot · Spring Security · OAuth2 Resource Server
Nimbus JWT · Spring Data JPA · MapStruct · MySQL · H2 · Maven
```

**Engineering topics demonstrated**

* JWT validation and identity-related security concerns
* Layered Spring Boot application structure
* Persistence with Spring Data JPA
* DTO mapping using MapStruct
* Test-ready database configuration
* Consistent formatting with Spotless

---

### [`AI_EMOTION_APP`](https://github.com/mudotet/AI_EMOTION_APP)

> A Java desktop application combining AI-guided conversation, emotion analysis and mood history.

```text
Java · JavaFX · MySQL · AI Model Integration · Maven
```

**Engineering topics demonstrated**

* AI response integration inside a Java application
* Emotion classification from user-provided text
* Persistent user, conversation and emotion records
* Relational data modelling
* Modular desktop application design

---

### [`Invoice_Extraction_Project`](https://github.com/mudotet/Invoice_Extraction_Project)

> An OCR and document-understanding pipeline for extracting structured information from invoice images.

```text
Python · PyTesseract · LayoutLM · PyTorch · Streamlit
OCR · Document Understanding · JSON / CSV Export
```

**Engineering topics demonstrated**

* OCR preprocessing and text extraction
* Layout-aware document classification
* Model inference pipeline
* Structured result export
* Lightweight Streamlit interface

---

### More work

My portfolio contains additional backend, full-stack and AI-related projects:

<p>
  <a href="https://tus-portfolio.vercel.app/">
    <strong>Explore my project portfolio →</strong>
  </a>
</p>

---

## `06. stack.runtime`

### Backend core

`Java` · `Spring Boot` · `Spring MVC` · `Spring Security`
`Spring Data JPA` · `Hibernate` · `REST API` · `JWT` · `RBAC`

### Data and persistence

`PostgreSQL` · `MySQL` · `MongoDB` · `Redis`
`Relational Modelling` · `Caching` · `Transactions`

### Development and delivery

`Docker` · `Maven` · `Git` · `GitHub`
`Swagger / OpenAPI` · `Postman` · `MapStruct`

### Integration layer

`Python` · `FastAPI` · `NestJS` · `React`
`OCR` · `RAG` · `AI Model Integration`

---

## `07. current.status`

```java
public final class CurrentDirection {

    private final String primaryStack =
            "Java + Spring Boot + PostgreSQL";

    private final String learningFocus =
            "Scalable backend architecture and system design";

    private final String productInterest =
            "AI-powered applications with practical value";

    private final String targetRole =
            "Java Backend Intern / Fresher";

    public boolean openToOpportunities() {
        return true;
    }
}
```

I am currently improving my ability to:

* Explain technical decisions clearly
* Design maintainable service boundaries
* Handle authentication and authorization correctly
* Model data around real business requirements
* Test backend behavior instead of only testing happy paths
* Deploy multi-service applications with Docker
* Integrate AI services without tightly coupling them to the core application

---

## `08. contact.channel`

<p align="center">
  <strong>Looking for a Java Backend Intern or Fresher who enjoys learning by building?</strong>
</p>

<p align="center">
  <a href="mailto:mudotet@gmail.com">mudotet@gmail.com</a>
  &nbsp;•&nbsp;
  <a href="https://tus-portfolio.vercel.app/">Portfolio</a>
  &nbsp;•&nbsp;
  <a href="https://www.linkedin.com/in/t%C3%BA-phan-203970327/">LinkedIn</a>
</p>

<p align="center">
  <sub>Hanoi, Vietnam · Open to backend and backend-focused full-stack opportunities</sub>
</p>

---

## `09. contribution.breakout`

<p align="center">
  <sub>My GitHub contribution history, transformed into a Breakout board.</sub>
</p>

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="images/breakout-dark.svg?v=1"
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="images/breakout-light.svg?v=1"
  />
  <img
    width="100%"
    alt="GitHub contribution Breakout Game"
    src="images/breakout-light.svg"
  />
</picture>

<p align="center">
  <sub>Build. Break. Learn. Improve. Repeat.</sub>
</p>
