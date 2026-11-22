<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./images/hanoi-after-dark-still.webp" />
  <img src="./images/hanoi-after-dark.webp" width="100%" alt="A glowing teal path crosses Hanoi’s Long Biên Bridge after dark, splits in two, and rejoins at an amber light." />
</picture>

# Hi, I’m Tú Phan.

I build Java backends in Hanoi.
The part I enjoy most is figuring out what happens when a request times out, an event arrives twice, or a player hits Buy again.

[Portfolio](https://tus-portfolio.vercel.app/) · [Email](mailto:mudotet@gmail.com) · [Other repositories](https://github.com/mudotet?tab=repositories)

## One purchase. Two requests.

Say the server charges the player, but the response never reaches their phone.
When the player retries with the same request ID, my game server returns the saved receipt.
If the retry changes what they’re buying, the server returns a conflict.

<details>
<summary><strong>Replay the request</strong></summary>

1. **Buy one item** with ID `buy_000000000001`. The server charges once and saves the receipt.
2. **Retry the same purchase** with that ID. The server returns the saved receipt.
3. **Change the item** and reuse that ID. The server returns `409` with `REQUEST_ID_REUSED`.

</details>

[Game server source](https://github.com/mudotet/mini-intern-server-project/tree/main/server) · [Purchase API contract](https://github.com/mudotet/mini-intern-server-project/blob/main/server/docs/API_CONTRACT.md)

## More things I’ve built

- **[E-commerce Microservices](https://github.com/mudotet/ecommerce-microservices)** uses Kafka to coordinate orders and inventory across separate PostgreSQL databases. The inventory service remembers which order IDs it processed so a redelivered event can’t deduct stock twice.
- **[GuideLens AI](https://github.com/mudotet/GUIDELENS_AI)** takes a screenshot and a question, then draws the suggested steps directly on the interface.
- **[CivicPath AI](https://ai-guided-public-service-procedures.vercel.app/)** walks Vietnamese families through the documents they need to register a birth. [Source code](https://github.com/mudotet/AI-guided-public-service-procedures-Lonely-Stone-)

## My commits are the bricks

A year of GitHub contributions becomes a Breakout animation.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./images/breakout-preview-still.webp" />
  <source media="(prefers-color-scheme: dark)" srcset="./images/breakout-dark.svg" />
  <img src="./images/breakout-light.svg" width="100%" alt="A Breakout animation with bricks laid out like my GitHub contribution graph." />
</picture>
