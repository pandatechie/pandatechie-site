---
title: "What is Hash Function in Blockchain? How is it used in Proof of Work?"
date: "2021-09-05"
slug: "what-is-hash-function-in-blockchain-how-is-it-used-in-proof-of-work"
categories: ["Cryptocurrency"]
tags: ["bitcoin", "hashing", "mining", "proof of work"]
original_url: "https://pandatechie.in/2021/09/05/what-is-hash-function-in-blockchain-how-is-it-used-in-proof-of-work/"
cover_image: "https://miro.medium.com/max/468/1*zv5kl3Z9F1XHcRtAk18fHA.png"
archive: true
---

One of my friends is very **bullish** on **cryptocurrency**. He claims that it is the **future** of **money** and has the **potential** to **change** the **world** we live in. I couldn't **agree** more. However, just like most of the **speculators**, he finds it **annoying** when **someone** talks about the underlying **blockchain** **technology**. He might be **great** at **reading** the **charts**, but lack of **understanding** of how [**Bitcoin** works](https://pandatechie.in/2021/07/29/how-does-bitcoin-work/) is something that is just **outright** **crime**. So when I asked him what is **hash** **function**, he laughed it off. Are you the **friend** I am referring to? If yes, then read on. If you are reading this, you obviously are into **cryptoverse**. Which by the way, also means that you must have come across the term: **Proof of Work.**

![](https://miro.medium.com/max/468/1*zv5kl3Z9F1XHcRtAk18fHA.png)

But before I jump into **proof of work**, I want to touch upon a rather **spectacular** concept of a **hash function**. It forms the **basis** of proof of work and very soon you'll know how. As always, the topics that are **explained** after I **try** and **test** on my **mother**. Only when she says that she has an **idea** of what I am **speaking**, I resort to **writing**. So, trust me on this. This one would have no **fancy** words whatsoever. Let's get started!

## What is Hash Function?:

To put it into **simplest** terms, hash is nothing but a **random string** of **numbers** that represents **some** **kind** of **input** **data**. Think of it as a **converter**. You put **something** from one end and you get a **string of numbers** from the other side. You can put anything here. A **text**, an **image**, even a **single character** for that matter.

![](https://sectigostore.com/blog/wp-content/uploads/2020/12/hash-function-in-cryptography-1024x440.png)

So, if you put **P.A.N.D.A.T.E.C.H.I.E.** as an **input** to a **hash** **function**, you would get something like **123724123123** on the other side. As simple as that.

With that being said, hash function has a unique set of **properties**. These properties make it much more useful. Let's explore each of these traits in detail.

## A. Fast:

A hash function is **lightning** **fast**. Anything that you **input** from one **end**, will **yield** the **output** string **instantaneously**. This is critical as **hash** has to be a **randomly** **generated** number. And if someone is guessing a specific hash, they need to do that as soon as possible (more on this shortly)

![](https://cdn.vox-cdn.com/thumbor/9Ub3UtVIrjNkI83o_-eo62JEtwc=/27x0:663x424/1400x1050/filters:focal(27x0:663x424):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49620497/Screen_Shot_2016-05-18_at_10.42.31_AM.0.0.png)

## B. Deterministic:

This means that every time you put a **specific** **input**, the hash function should yield the **same** output. For example, if you put **PANDA** as an input and the output is **12345**, every time you put in PANDA, the **output** should be the **same**.

## C. Collision Resistant:

No we are not talking about real collisions. But this one is not **fundamentally** very different from that. While some of you might have guessed where this is headed, for others, collision resistance is the property of hash functions that allows **no two inputs** to have a **same output**. Makes sense right?

![](https://pandatechie.in/wp-content/uploads/2021/09/image.png)

When I say two inputs, the difference between them can be **miniscule**. For example, even **PANDA** and **PaNDa** should yield a different output.

## D. One Way:

Yup. You guessed it right. Hash functions are one way only. That means you can **create** a **random** **string** of numbers from a hash function using any **input**, however, you **cannot** **trace** **back** an **input** using those numbers. In a similar example, there should be no way for you to learn that **12345 stands for PANDA**.

While reverse engineering is a legit strategy in most of the products, it shouldn't be possible for a hash function.

## E. Avalanche Effect:

Once again, this property has a lot to do with how entire scheme of hash functions fits into **Bitcoin's** infamous **proof** of **work**. Avalanche effect refers to the attribute that would **change** the **output** of a hash function **dramatically** even if the **input** is changed **slightly**.

![](https://media.geeksforgeeks.org/wp-content/uploads/20200203162309/Capture3331.png)

For example, if the input **"TECHIE"** is **changed** to **"TECHY"**, the two outputs generated would be so different that they would have no **correlation** with each other whatsoever. It would be almost impossible to draw a **connection** between these two **outputs**.

## How is Hash Function used in Mining?

Now that you are aware of properties of a hash function, let's find out how it used in mining. What is proof of work? Very often we hear that **miners** solve a **complicated mathematical puzzle** to **prove** the **work** has been done. But what is this **complex** **problem**?

Well, it's nothing but a hash function called SHA-256. Miners use the following **inputs** in a hash function:

* **Transaction** **Data** of the block
* **Reference** **number** (also called **hash number**) of the **previous** block
* **Work number** (also called **nonce**)

![](https://pandatechie.in/wp-content/uploads/2021/09/image-1.png)

They club these inputs in such a way that **output** **generated** (from hash function) is in such a way that it starts with **four ZEROES**. Miner to reach this hash output the fastest wins the right to mine the next block.

![](https://www.hodlbot.io/public/nonce-1.png)

How do they reach this number? It's purely **guess work**. Miners already have the **reference** number of previous block and **transaction** data. What they do is **start** **guessing** the **work** **number** (nonce) from 0,1,2 till 100 to 1000 until they by **accident** reach a number which would **generate** the **desired** hash output.

This also means that more the **computational** power, better are your **chances** of guessing this **work** **number** **faster** and hence winning this race.

## Conclusion:

Anyone who believes in technology would know that this is no less than magic. I still wonder the thought process that would've gone behind using these methodologies to come up with world's first permissionless, trust less, decentralized peer to peer transaction system.

If you are as awestruck as me, hit me up. I can talk about it endlessly!

https://www.instagram.com/p/CRiThtVrAsb/
