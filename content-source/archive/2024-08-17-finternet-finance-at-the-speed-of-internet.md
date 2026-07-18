---
title: "Finternet: Finance at the Speed of Internet"
date: "2024-08-17"
slug: "finternet-finance-at-the-speed-of-internet"
categories: ["Uncategorized"]
tags: []
original_url: "https://pandatechie.in/2024/08/17/finternet-finance-at-the-speed-of-internet/"
cover_image: "https://pandatechie.in/wp-content/uploads/2024/08/imageshd-d.jpeg"
archive: true
---

After months of deliberation, I finally decided to opt for a second life insurance plan as my spouse felt I was underinsured (major sus?). I have lost about 20 kgs since I last opted for a term plan, five years ago but I am still way over the ideal weight.

I fill in the form that explicitly asks me if I have been insured before (*Problem 1*).

Then it asks for the insurance provider (*Problem 2*).

Later, I get a call from the agent, seeking details like what was the initial proposal amount? How much do you eventually pay? Any specific riders that you were forced to buy (*Problem 3*).

If this isn't the 'Know Your Customer', then what is?

It may look like just an irritant to the end user, but the problem lies deep inside the architecture of our financial ecosystem.

So what can be done to fix it? Well, that is exactly what I plan to talk about.

Today, I want to present a glimpse into the future of finance.

Penned down by Nandan Nilekani and Agustin Carstens, **Finternet** is a vision for interconnected financial ecosystems that put users at the centre, enabling seamless transactions across different assets and platforms, similar to how the internet connects information and communication systems.

![](https://pandatechie.in/wp-content/uploads/2024/08/imageshd-d.jpeg)

*(L-R, Nandan Nilekani, Co-founder and Non-Executive Chairman, Infosys ; Agustin Carstens, General Manager, Bank for International Settlements)*

Today, I will try to cover:

* Why do we need financial innovation at all?
* What is [Finternet](http://bis.org/publ/work1178.pdf)?
* Potential challenges or limitations of Finternet
* Ideas for implementation of Finternet
* Use cases for Finternet and Public Ledgers to work together

## But we already had UPI: Why Financial Innovation?

I wanted to address this question specifically because, as Indians, we have witnessed the transformation of the financial ecosystem up close by interventions like Aadhaar, UPI, and account aggregator.

In fact, some reports suggest that this has put India four decades ahead of its financial inclusion goals.

When I see our grandparents sending money on Diwali via GPay, I am forced to believe that we have made it as a country. However, without undermining the massive success of digital public infrastructure, we still have a long way to go.

For example, as users, we may not care enough about the backend operations, but in reality, our seemingly digital transactions are settled only once a day in the backend.

Behind the scenes, transferring money and financial assets relies on separate databases owned by different institutions.

These databases have varying standards and rules, making direct communication difficult.

Third-party messaging systems are used to connect them, but these systems may not always work smoothly together, leading to potential delays or complications in the transfer process.

In some cases, the exchange of physical contracts is still required.

Particularly in cross-border transactions, differences in time zones and business hours can slow down the process further.

To summarize, the core problems of existing financial ecosystem can be bucketed under the following categories:

![](https://pandatechie.in/wp-content/uploads/2024/08/Colorful-Elegant-Minimalist-3-Point-Infographic-Brainstorm-1-1024x576.png)

*The major challenges in the current financial ecosystem are Speed, Access and Cost*

### Speed:

If you are thinking about lightning speed of UPI, please keep in mind that it only solves for cash at the moment. There is a plethora of financial transactions, including equity, bonds and real estate, that need their UPI moment.

Also, even with UPI, siloed databases in the backend can lead to settlement delays.

### Cost:

Even UPI is not free. The cost is borne by Payment Service Providers, Government and Fintech companies etc. to promote adoption.

Other financial transactions often face delays and high costs due to outdated systems. These delays tie up capital, forcing businesses and individuals to rely on expensive alternatives.

Settlement delays create counterparty risks, requiring costly collateral.

Manual processes lead to errors and incomplete transaction views, necessitating extensive auditing.

The lack of competition results in high fees, especially for cross-border payments. These inefficiencies particularly impact low-value transactions and emerging markets.

### Access:

These costs and slow speed combined, limits the capability of an individual to diversify beyond traditional assets. It creates an ecosystem that is laden with minimum transaction amount norms which are uneconomical in certain geographies.

Why does it matter, though? Because the inability to access financial services lowers welfare. Limited access to financial services hinders individuals' ability to manage risks and save for the future. It's your arch nemesis, inflation, at work.

## What is Finternet?

Finternet is a vision for a future financial system where multiple interconnected financial ecosystems, built on unified ledgers and innovative technologies, empower individuals and businesses by placing them at the center of their financial lives.

It is inspired by the evolution of the iPhone, which integrated pagers used for textual communication, computers used for office work, and dial-up internet into one device. Finternet aims to replicate that model by combining various silos of innovations under a single umbrella, allowing them to interact seamlessly.

https://www.youtube.com/watch?v=ntjkwIXWtrc

*Types of devices gobbled by Apple*

### What does Finternet look like?

To achieve this gargantuan vision, a unified ledger approach that piggybacks on tokenization is suggested.

Unified ledgers act as a digital "town square" for financial assets, bringing together various financial instruments and transactions in one place.

Much like a shopping mall that houses multiple stores under one roof, unified ledgers bring together different financial assets (e.g. money, securities, real estate) on a single platform. This allows for easier "shopping" and management of various financial products.

High level architecture of Finternet looks something like this:

![](https://pandatechie.in/wp-content/uploads/2024/08/image-1024x678.png)

*Finternet Architecture*

A notable aspect is that when regulators come into picture, they can regulate the application layer without interfering with the base technology. To extend the analogy, much like how smartphones aren't regulated, but the apps running on them are.

To summarize, here's a quick comparison of unified tokenized financial realm vis-a-viś existing systems:

![](https://pandatechie.in/wp-content/uploads/2024/08/image-1-996x1024.png)

*Comparison of unified tokenized financial realm vis-a-viś existing systems:*

Sidharth Shetty, CTO of [Sahmati](https://sahamati.org.in/) and Technology Advisor at Unified interfaces, discusses three key principles or "U's" that guided the approach to designing the Finternet architecture:

![](https://pandatechie.in/wp-content/uploads/2024/08/Blue-Minimalist-3-Stage-Diagram-Venn-Infographic-Graph.png)

*The 3 U's of Finternet infrastructure : User Centricity, Unification and Universality as discussed by Sidharth Shetty, CTO of Sahmati and Technology Advisor at Unified interfaces*

### 1. User Centricity:

This principle focuses on putting individuals and businesses at the center of their financial lives. The goal is to design systems and frameworks that prioritize the needs and experiences of users rather than providers.

### 2. Unification:

This principle aims to create an approach that allows for unification across diverse environments, asset classes, sectors, and countries. The idea is to develop architectural constructs that enable interoperability and compatibility, even if different entities adopt the system at different times.

### 3. Universality:

This principle emphasizes the importance of making the technology universally available, much like the internet.

The goal is to ensure that the Finternet can potentially serve all 8 billion people and 300 million businesses globally. This approach allows for universal access to technology, while enabling appropriate regulations and rules to be layered on top for specific types of transactions or asset flows.

### Pre and Post Finternet World:

To make it real, let us consider a transaction that involves buying stocks in Indian market.

In the current Indian financial system:

1. Maria decides to buy shares of Company X through her stock broker.
2. Maria instructs her broker to purchase the shares.
3. The broker places the order on the NSE.
4. Once the order is matched, Maria's bank account is debited for the purchase amount.
5. The funds are transferred to the broker's account.
6. The broker's account at the clearing corporation is debited.
7. The clearing corporation settles the transaction with the seller's broker.
8. The shares are transferred from the seller's demat account to Maria's demat account through the depository (NSDL or CDSL).
9. This process typically takes T+2 days (where T is the transaction day) for settlement.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-2-1024x406.png)

*Securities Settlement*

To add more fun to the mix, the above transaction does not consider banking yet. That is an additional overload as shown in the image below:

![](https://pandatechie.in/wp-content/uploads/2024/08/image-3-1024x380.png)

*Banking Settlement*

If this isn't enough, just for the sake of realism, imagine if this transaction fails due to some constraint at Maria's broker's end; then there is an entire cost and time loss to reverse it.

**In a unified ledger system:**

1. All assets - Maria's bank account, her demat account, the shares of Company X, the broker's account, and the central bank reserves - would exist on the same digital ledger.
2. When Maria initiates the purchase:
   * The shares will be instantly transferred from the seller's tokenized demat account to Maria's.
   * Maria's tokenized bank account will be debited.
   * The seller's tokenized bank account will be credited.
   * The brokers' accounts will be updated simultaneously.
3. The entire transaction, including clearing and settlement, will occur almost instantaneously.
4. The Reserve Bank of India (RBI) oversees the system but doesn't need to be involved in each transaction.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-4-1024x563.png)

## Challenges and Limitations:

If it were easy, everyone would do it. There is a reason why Finternet needs further deliberation before it becomes a reality. A few of the challenges that I foresee in this journey are as follows:

![](https://pandatechie.in/wp-content/uploads/2024/08/Green-6-Points-Creative-Process-Diagram-Infographic-Graph.png)

*Challenges and Limitation of Finternet*

### 1. All or Nothing:

To harness the maximum potential of Finternet, it is paramount that it is done in its entirety. If we manage to bring the financial ecosystem on Finternet partially, the core problems of speed, cost and inclusivity mentioned above will still plague the ecosystem.

I understand this may not be a big bang implementation but the vision should incorporate the holistic approach.

### 2. Mass Scale Coordination and Integration:

UPI was conceived in 2012 and launched in 2016. By 2024, we see 62% of digital payments being done through UPI.

After so much rigor and relentless building, it took 12 years to absolutely nail an initiative that is native to India.

Finternet aims to establish a global footprint, which might take much longer.

Overcoming vested interests and existing infrastructure limitations is a major challenge.

> *Friction is almost celebrated by intermediaries as they make money out of it.*   
>   
> - Agustin
>
> [Click to Tweet](http://twitter.com/share?&text=%3Cem%3EFriction%20is%20almost%20celebrated%20by%20intermediaries%20as%20they%20make%20money%20out%20of%20it.%20%3C%2Fem%3E%3Cbr%3E%3Cbr%3E-%20Agustin&url=[post_permalink]&via=pandatechie_)

### 3. Regulations:

It is still easy to tackle the base regulatory layer if it is within the same jurisdiction. But when each nation-state has its own laws, it is necessary to tailor solutions to ensure compliance.

I see this as one of the major roadblocks.

Even after a decade since the launch of Bitcoin, we still have most of the world economies with no concrete regulations around blockchains. This requires a similar level of coordination if not more.

### 4. Infrastructure:

Developing the necessary technological infrastructure to support a global unified ledger system is a significant undertaking.

This includes ensuring scalability, reliability, and interoperability among different financial systems and technologies.

All of this needs to be done while being mindful of the associated costs to scale.

AWS, I am looking at you.

### 5. Geopolitical Navigation:

This innovation is likely to benefit EDMEs more than DEs. Moreover, the problem of inclusion is more likely to be pervasive in smaller economies. .

It is likely to be a blocker as it may not align with the interests of bigger economies. Ensuring that these changes benefit all participants and do not exacerbate existing inequalities is a key consideration.

### 6. Change Management and Training:

Even with UPI, the innovation at the application layer led to incentivized models of early adopters on both merchant and user sides. For example, [BharatPay](https://bharatpay.net/) absorbed the merchant fee of transactions to collect payment data for the merchant and offer them loans. Later, the government waived off the fee entirely.

In certain cases, users were paid to use UPI for capturing consumer base. For example, Amazon, Google, Cred ran programs for customers to use their platform for making payments.

Finternet would have to leave the room for similar innovation at application layer. Else, we might witness a muted adoption.

## Finternet in Action: Ideas for Implementation

I ran a word analysis on the Finternet paper. As you would guess, the most commonly occurring words are **Digital**, **Token**, **System**, **Financial**, **Unified**, and **Asset**.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-5-1024x1010.png)

*Word Cloud of Finternet Paper*

If you have been a part of Superteam for a while now, these words would point you towards a single direction: Blockchains.

In fact, towards the end, terms like smart contracts, ZK, and Cryptography become more common as we delve deeper.

But let us try to apply first principles thinking to the implementation, and the pros and cons of different implementation methodologies:

### 1. API-Based Approach with Progressive Decentralization

An API-based approach with decentralized elements leverages the flexibility and interoperability of APIs while incorporating the benefits of decentralization, such as increased security and trust.

However, an API based approach will also face huge issues in seamless integration between unified ledgers. Apart from that, the rules for most systems would differ further complicating the approach.

There would also be additional security and privacy concerns, complexity in managing decentralized elements, potential vulnerabilities, and dependency on external systems.

### 2. Centralized Database with Decentralized Governance

A centralized database approach with decentralized governance combines the efficiency and control of centralized systems with the benefits of decentralized decision-making and transparency. This approach aligns with the design principles of user-centricity, security, and privacy.

Some of the initial use cases for this includes secure data sharing and compliance reporting.

This can be done by implementing decentralized governance mechanisms, such as multi-signature schemes or decentralized autonomous organizations (DAOs), to enable inclusive and transparent decision-making processes.

### 3. Private Consortium Blockchain Approach

A private blockchain approach combines the strengths of both public and private blockchains, offering a balance between transparency, security, and scalability. This approach aligns well with the design principles of interoperability, evolvability, and modularity.

In this approach, the custodians of the ecosystem can become its nodes and act as guardians of the transactions rather than making changes to it.

Weighing the pros and cons of the implementation and alignment with Finternet's vision, **I propose a private consortium Blockchain** to be the best positioned for this implementation.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-12-891x1024.png)

## Use Cases of Finternet and Public Ledgers to Work Together:

I don't want this section to look like a forced attempt skewed in favor of promoting public ledgers (Blockchain). This is why, I will start by sharing a few reasons why it is indispensable for Finternet to incorporate public blockchains in their GTM eventually.

For starters, what Finternet aims to achieve, is done in bits and pieces by crypto rails worldwide. On the top of that, Finternet's vision of creating an interconnected, inclusive, and transparent financial ecosystem aligns well with the core principles of public ledgers.

Moreover, activity on public blockchains is no longer limited to dorm room nerds.

https://twitter.com/smtgpt/status/1821799625579503685

Look at this tweet by Sumit, CEO of CoinDCX. It highlights a report that talks about how web3 adoption is faster than that of the internet. If Finternet wants to become a one-stop shop for all financial activity, globally, it is going to be hard to ignore crypto.

Secondly, unlike most governments think, regulatory whip doesn't work anymore. An outright ban is out of the question because speculation powered by financial nihilism always finds a way. Therefore, a better approach is to figure out ways of working with public blockchains rather than staying muted about it, if not banning it.

Finally, a thought experiment to drive this home.

If given a choice between who gets all the power, the obvious answer is 'me'.

But if that's not an option, the next best bet is 'no-one'. And we all know which direction the multipolar world is headed right now.

And that is exactly what public blockchains do - enable trustless, decentralized ecosystems, for all of us to operate.

With that explanation out of the way, let us talk about how Finternet can work in conjugation with public ledgers.

### 1. Better Underwriting and Regulating Crypto:

One of the core problems for governments across the globe is their inability to attribute Blockchain transactions to an individual.

It is possible but it is time consuming and expensive.

One way to kill two birds with one stone would be to incentivize crypto natives to bring their onchain data to the Finternet unified ledger.

This helps lending authorities with better underwriting. Crypto natives get better rates in lieu of that.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-11-edited.png)

One inhibition to building this would be an underlying assumption of tax evasion by the user dealing in crypto. The government can use this opportunity to create Income Declaration Scheme (IDS) equivalent for crypto.

Under this scheme, individuals and entities could declare their undisclosed income (often referred to as "black money") and pay a penalty. In return, they would be granted immunity from prosecution under various laws, including the Income Tax Act, the Wealth Tax Act, and the Companies Act, among others.

An indirect benefit of this would also be felt by on-chain protocols that usually rely on overcollateralization for lending today.

### 2. End of Spamming:

What is the underlying reason behind relentless, futile attempts to sell a credit card today?

My hypothesis is that it is a 'spray and pray' technique, deployed by fintech companies because right now hyper-personalized, targeted campaigns are not possible or are very expensive.

Talking to public blockchains solves this problem as it signifies users with the highest intent of everything finance.

Here's an example: [Values DAO](https://app.valuesdao.io/community), an emerging protocol, assigns values to different projects and blockchains in crypto. Your social feed and your on-chain activity (soon) is then used to figure out your inclination.

This also reduces the cost of trust dramatically. As it is easier to find sticky customers who are aligned with what you stand for.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-6-1024x509.png)

Now imagine if [CRED](https://cred.club/) had an access to this user base, they would reach out to customers who believe in creativity, playfulness and may be burn a little less in CACs.

Similarly, tracking spends and strategies of users on DEXs like [Uniswap](https://uniswap.org/), [Raydium](http://raydium.io) and [Orca](http://orca.so) could give you an insight of their financial personality. For example, meme coiners are risk takers, Bitcoiners may be on the other side of the spectrum etc.

The best part of Finternet is that we still get to keep the users in the centre by letting them choose, whether they want to share this data or not.

Some fictional UI designs below:

![](https://pandatechie.in/wp-content/uploads/2024/08/image-7-1024x589.png)

### 3. Financial Literacy:

It is one of the top priorities of the government to educate the masses about finance. After all, financial literacy has a positive correlation with the per capita income of a country.

This can be seen in action in the screenshot below where NDSL is trying to highlight the importance of data privacy through a newsletter to me.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-8-1024x692.png)

I lead a digital team in an Indian conglomerate, and I'd be jobless if I were not wary of these concerns.

So how do we personalize this?

Well, once again, start with understanding how on-chain users get rekt. Figure out a pattern and then target them by explaining what went wrong for them. This type of education has the highest affinity towards learning.

If you could tell me how can I NOT loose money, I am all ears.

To take it up a notch, if an AI layer could translate this to my language, I would be sold the minute I receive it.

### 4. Insurance:

If there is one thing web3 is great at, its community aligned to a specific goal.

A few years ago, we saw the success of [STEPN](https://stepn.com/).

STEPN is a move-to-earn (M2E) game built on the **Solana blockchain**. The platform integrates elements of the play-to-earn (P2E) model but relies on physical activity to generate rewards.

STEPN saw a surge around its launch and then dwindled to some 30K MAU in the past 6 months.

This is primarily because of boredom around rewards and social elements.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-9-1024x290.png)

If Finternet could enable insurance companies to offer discounted premiums based on user physical activity, it could be valuable for both the insurance provider and the seeker. There is already a community that existing on-chain and all an insurance player has to do is plug-in.

Bottomline: Aligned incentives > Community around finance

## Conclusion:

As the cog of time tips in the favor of an hyper connected world, likes of Finternet are going to pave the way for next financial revolution.

In equity markets, they often say, if NASDAQ sneezes, NIFTY catches cold. Question here is, why can't Indians invest in US markets or vice-verse at the speed of this correlation of price action.

This article presents an overview of Finternet and its vision. It also tries to add implementation nuances using different techniques aligned with the Finternet's design principles.

Finally, it tries to delve deeper into a few use cases of Finternet and public ledgers together. This is based on the premise that given the current ugly state of UX, only few people with clear intent and goal in mind are migrating on-chain.

I will now hop on to KYC for the fifth time with a new age broker for discounted fee.

Until Finternet becomes a reality.

### References:

1. [The Vision for the Future Financial System](http://bit.ly/finternet-vision)
2. [Technology Vision and Architecture](http://bit.ly/finternet-tech)
3. [Finternet Specs](https://github.com/finternet-io/specs)
4. [Fireside Chat at BIS](https://www.youtube.com/watch?v=2-ukiKchQsI&t=1s)
5. [Successful Finternet Could Boost India, Global Economy By 2-3%: NPCI's Ajay Kumar Choudhary](https://www.ndtvprofit.com/technology/successful-finternet-could-boost-india-global-economy-by-2-3-npcis-ajay-kumar-choudhary)
6. [Dune](http://dune.com) for analytics

### Open-Source License Notice

This work is licensed under the Creative Commons Attribution 4.0 International License.

You are free to:

* **Share** — copy and redistribute the material in any medium or format
* **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms

* **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
