---
title: "How to Enable Public Trading of Your Own Cryptocurrency on Pancakeswap?"
date: "2021-11-07"
slug: "how-to-enable-public-trading-of-your-own-cryptocurrency-on-pancakeswap"
categories: ["Cryptocurrency", "Technology Trends"]
tags: ["Finance", "liquidity", "pancakeswap", "token"]
original_url: "https://pandatechie.in/2021/11/07/how-to-enable-public-trading-of-your-own-cryptocurrency-on-pancakeswap/"
cover_image: "https://pandatechie.in/wp-content/uploads/2021/10/Automated-Market-Maker.png"
archive: true
---

*Disclaimer: This blogpost is in continuation to the previous blogpost that talks about how one can create their own cryptocurrency. If you haven't read that article, this one is probably not meant to be read in isolation.*

With that out of the way, let's get started. Last time, we created our token called **PandaToken** on **Binance Smart Chain**. Until that point, we were able to **transfer** all the **token supply** in our **Metamask** **Wallet** and it was **ready** to be **shared** with our **friends** and **family**. From participating in **petty** **airdrops** to actually **conducting** one, we have come a long way in this journey. However, we want more right? We want to list it on **Pancakeswap** for the **world** to **transact** with our **token** right?

That's exactly what we are going to learn today. Raise your hands if you are as excited as me. Dopamine shot is real with this one!

## How Pancakeswap Works?

So any Decentralized Exchange or DEX like **Uniswap** or **Pancakeswap** is a lot different in working as compared to a **centralized exchange** or **CEX** like **CoinDCX**, **Binance** etc. You see in a CEX, there's an **order book** where all the **open buy** and **sell** **orders** are **matched** with each other and the **exchange** takes care of the **asset swapping**. On the other hand, in a **DEX**, this happens in a **decentralized** manner.

Investors put in some assets (any cryptocurrency) in something called a liquidity pool. Later, traders come along and exchange their assets with the ones in the liquidity pool. Basic supply and demand takes care of the prices of the assets in the pool. If you wish to dive deeper in to the working of decentralized exchanges, read my blogpost on Automatic Market Maker [here](https://pandatechie.in/2021/10/09/what-is-an-automated-market-maker-amm/).

![Robot representing automated market maker](https://pandatechie.in/wp-content/uploads/2021/10/Automated-Market-Maker.png)

Automated Market Maker

Since **nobody knows** about your **token** yet, there is no **liquidity available** for it in a decentralized exchange. Similarly, none of the **exchanges have so far listed your token**. So it is important for you to **enable** it's **trading** starting from a **DEX**. Let's explore how to do that on Pancakeswap in a step by step guide.

## Step 1: Login and Connecting to Pancakeswap:

Go to [pancakeswap.finance](https://pancakeswap.finance/). On the **top right corner**, find an **option** to **connect** the wallet. Once you press that button, you would be shown a **pop up** with a variety of wallets (as shown in the image below). Select **Metamask** and authorize the connection from the Metamask extension when prompted.

Once you are done, your Metamask wallet address should be displayed on the homepage indicating that it's connected.

![](https://pandatechie.in/wp-content/uploads/2021/11/image-13.png)

Connecting wallet to Pancakeswap.finance

## Step 2: Finding Contract Address for Your Token:

This is very important. Not only because you need this address for **providing liquidity**, but also this is like the **unique identity** of your token. There are multiple **PandaTokens** out there, however, the token with contract address: *0xB7e78d2843e65851BBBd5426D4eE423ebbAf8711* belongs to me.

Moving on, so in the previous blogpost, we **transferred** all the **tokens** after **deployment** to our own **Metamask** wallet. Let's explore the **transactions** of our **wallet** to find the **contract address** of our token. Since **blockchain** **records** all the data in a public domain, all the transactions for a particular wallet can be viewed on [BSCScan](https://bscscan.com/).

Simply open the link and enter your **Metamask wallet address** on the search bar provided. Once you do that, you would see a **screen** that will have the entire information including **transactions** happening from your wallet.

![](https://pandatechie.in/wp-content/uploads/2021/11/image-15-1024x369.png)

BSC Scan screenshot of my Metamask Wallet

Refer to screenshot to find the **dropdown** that is going to have the **list** of all the **tokens** in your wallet. Once you select your own token, it will open up a **different page** which will be like a *Janam Kundli* for the token. In that page, you would find a section called **profile summary**. This would have the contract address. You can copy that same with a single click. (Screenshot below)

![](https://pandatechie.in/wp-content/uploads/2021/11/image-16.png)

BSC Scan screenshot of PandaToken

## Step 3: Liquidity Provision

From the **navigation menu** on the top select **trade** and then select **liquidity** from the menu. Once you do that, you should land on a **page** where can now **add liquidity**.

Tap on add liquidity and you should be able to select the **cryptocurrency pair** from this screen.

In the first input, enter **BNB**. Why? Because you already have BNB in your **Metamask** ever since we started this experiment.

![](https://pandatechie.in/wp-content/uploads/2021/11/image-14.png)

Liquidity Provision Pancakeswap

In the **second input enter the contract address** you found in the **previous step**. This will ensure that you are **providing liquidity** to your **own coin** and not some **doppelganger** crap (assuming that yours have some real use case)

## Step 4: Deciding the Price:

Once you select the pair, you would get a notification saying that you are the first liquidity provider. (Screenshot below).

![](https://pandatechie.in/wp-content/uploads/2021/11/image-17.png)

As a liquidity provider, you would have to add both **BNB** and your own token. This **ratio** is going to **determine** the **price** of your **token**. Example, I added **1,000,000 PND** against a price of **0.01 BNB**.

This would mean that entire supply of **PND** can be bought with **Rs. 500** OR, **1 PND** would cost about **Rs. 0.000049**.

You can tweak the price as per your convenience to select a price band for your token.

*Note: You will have to pay a ga*s fee to enable the liquidity. This price would be less than $2 in most cases.

## Conclusion:

That was it. Go ahead and share the contract address with anyone. Simply ask them to swap your token with BNB. You could also provide liquidity against other tokens like USDT, ETH as and when required using the exact same steps.

And just like that, you have a running publicly traded token at your disposal. Have fun and let me know what you plan to do with this information.
