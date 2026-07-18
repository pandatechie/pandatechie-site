---
title: "How to Create Your Own Cryptocurrency Under Rs. 500"
date: "2021-11-06"
slug: "how-to-create-your-own-cryptocurrency-under-rs-500"
categories: ["Cryptocurrency", "Technology Trends"]
tags: ["Finance", "cryptocurrency", "experiments", "how to"]
original_url: "https://pandatechie.in/2021/11/06/how-to-create-your-own-cryptocurrency-under-rs-500/"
cover_image: "https://pandatechie.in/wp-content/uploads/2021/11/image.png"
archive: true
---

Back in college, I used to **Jailbreak** iOS devices for fun (and may be a little side income). I also used to **flash Symbian devices** too just for the sake of it. And I once **bricked** my **HTC** device by **flashing** an **unsupported custom ROM**. Had to cook a story to convince the **service center** guys that I had nothing to do with it. The real question is not how, but, why? Because it gave me that **subtle dopamine hit**. When screen went **blank** and for a **moment** your **device** worth thousands was **worthless**, those **chills** were **addictive**. But as I grew older, that hit **vanished** from my life.

Only until a few days ago, I tried making my own **cryptocurrency**. That's when I **relived** the sheer **joy** of my college days. So today, I hope I would be able to ignite that spark in you too. Let's find out ***how to create your own cryptocurrency under Rs. 500***. Once again, this would be a completely **non technical** way to do it. You **don't** have to be from a **coding** **background** to make it happen. Also, from start to end it isn't going to cost you a fortune to come up with it. Let's take it step by step.

## Step 1: Create a Metamask Wallet

If you are an **active user** of **web3.0**, you must have come across the words like **Metamask** or **Trust Wallet**. If you already don't have a **wallet** created on **Metamask**, here's how you can do it under 30s.

Head over to the website [metamask](http://metamask.io).io and hit the **download** button. The wallet can be downloaded as a **browser extension** or **mobile application**. For this particular tutorial, it is recommended to use a laptop throughout the process. Once you download the browser **extension**, simply follow the **instructions** of setting up a **seed phrase** and **logging** into your wallet. ***Make sure that you store this seed phrase in a safe location as losing it would mean losing your crypto.***

![Screenshot of Metamask Wallet to show how to add custom RPC ](https://pandatechie.in/wp-content/uploads/2021/11/image.png)

## Step 2: Add BSC Network to Metamask

Since Metamask originally supported only **Ethereum** based tokens, it is defaulted at **Ethereum network** only. However, you can also add **Binance Smart Chain** network to it as well. You can do it by following these quick steps:

### 2.1

Go to your Metamask wallet and select add custom RPC as shown in the screenshot

![Screenshot of Metamask Wallet to show how to add custom RPC ](https://pandatechie.in/wp-content/uploads/2021/11/image-1.png)

### 2.2

Once you select the custom RPC, you would be required to fill a form. Copy paste the following details for the same:

**A. Network Name:** Binance Smart Chain

**B. New RPC URL:** https://bsc-dataseed.binance.org/

**C.** **ChainID:**0x38

**D**. **Symbol:**BNB

**E.** **Block Explorer URL:**https://bscscan.com/

Hit save once you are done.

Congratulations, you just added BSC network to your Metamask.

## Step 3: Transfer BNB to your Metamask Wallet:

Now go to a **centralized exchange like [CoinDCX](http://coindcx.com)** or **Binance** and purchase BNB worth **Rs. 500**. That's all you are going to need for this mini project. For this activity, I would be using **Binance** for purchasing **BNB** and **adding funds** to the **Metamask** Wallet.

Once you purchase the BNB, next step is to send it to your Metamask wallet. For that, simply head over to **Metamask** and **copy** your **BNB address** as shown in the screenshot below:

![How to copy wallet address from Metamask](https://pandatechie.in/wp-content/uploads/2021/11/image-3.png)

Once you are done, head over to Binance and find your purchased BNB in your funding wallet. Select Withdraw (underlined in the screenshot below)

![](https://pandatechie.in/wp-content/uploads/2021/11/image-4-1024x75.png)

On the **screen** that appears post that, enter the address that you **just copied** from **Metamask** in the step above. Choose the **network** as **Binance Smart Chain (BSC) BEP20**.

This will cost you a **withdrawal fee** of **0.0005 BNB OR ~ Rs. 20**.

Once you withdraw your BNB, the remainder should reflect in your Metamask wallet within a couple of minutes.

## Step 4: Creating Your Cryptocurrency

### 4.1 Coding:

Coding time! Don't worry, for people like us, it is mainly going to be a **copy paste** thing. Now, I want you to head over to this [link](https://github.com/jklepatch/eattheblocks/blob/master/screencast/308-create-bep20-token-bsc/Token.sol)

This link contains the **source code** of a **token** that runs on **Binance Smart Chain**. All you need to do is **copy paste** that token **source code** and head over to the **Token Launcher** [here](https://remix.ethereum.org/). Follow the steps mentioned in the screenshot below:

![How to create a new smart contract](https://pandatechie.in/wp-content/uploads/2021/11/Select-Contracts-1024x512.png)

Once you have created a new contract, a **blank window** should appear. **Paste the code** copied from the **link** above here. Now all you have to do is tweak a few settings highlighted in the screenshot below.

*Select the total supply for your token, the name of your token and the ticker symbol you want*. I personally kept the supply of my token at 100,000,000. The name I opted for was "ThePandaToken" (Duh!) and the symbol I doubled down on was "PND".

![How to create a new smart contract](https://pandatechie.in/wp-content/uploads/2021/11/image-5-1024x435.png)

Aaaaanddd that was it. You're done with the "Coding" part of this activity.

### 4.2 Compiling:

Time to compile the code, follow the images below to quickly complete that step.

![How to create a new smart contract](https://pandatechie.in/wp-content/uploads/2021/11/1-1024x512.png)
![Compiling the code for a new token](https://pandatechie.in/wp-content/uploads/2021/11/2-1024x512.png)
![Compiling the code for a new token](https://pandatechie.in/wp-content/uploads/2021/11/image-7.png)

Please note that you may get a couple of warnings while trying to compile the code but that's okay. You can still run the code.

### 4.3 Deploying:

This step involves money. **It will cost you about 0.0044BNB to deploy your code in real time environment**. This will amount to be Rs. 110 approximately. Once you approve the transaction, your code should be deployed. Refer to the image for the next steps:

![Compiling the code for a new token](https://pandatechie.in/wp-content/uploads/2021/11/image-8.png)

Once your code is deployed, you need to **claim** them. Think of it like this. You have created your tokens now, but no one **holds** them. They are out there in the open. So how do you claim them now? Refer to the image below:

![Compiling the code for a new token](https://pandatechie.in/wp-content/uploads/2021/11/image-10.png)

Once again this is going to cost you about **0.000167BNB** which is about Rs. 7. So hit that transact button.

![Compiling the code for a new token](https://pandatechie.in/wp-content/uploads/2021/11/image-9-1024x493.png)

## Step 5: Do Whatever the Heck You Want:

If you have followed all the above steps diligently, by now you must have your tokens in your wallet. Now you can send them to your friends and family by simply asking for their BNB Metamask address.

***Please Note**: At this point, general public won't be able to trade with your cryptocurrency. For that you would have to provide liquidity on famous exchanges like Pancakeswap, Uniswap etc.*

Do you want me to cover another tutorial on how that's done? Let me know in the comments section below.

**I have added PND to Pancakeswap and you can buy it if you're interested using the address: 0xB7e78d2843e65851BBBd5426D4eE423ebbAf871**

![](https://pandatechie.in/wp-content/uploads/2021/11/image-11.png)

Pandatoken in my Metamask Wallet

![](https://pandatechie.in/wp-content/uploads/2021/11/image-12.png)

Pandatoken on Pancakeswap

## Conclusion:

While it will certainly quench your geek thirst, there's a lesson to learn here as an investor too. If you and I can create a cryptocurrency at a menial cost of Rs. 300-500 within 20 odd minutes, everyone else can too. Therefore, next time you try to be a part of the Squid Games Token like noise, please [DYOR](https://pandatechie.in/2021/08/27/8-cryptocurrency-lingo-you-should-know-crypto-glossary/) and then take a call.

For now, you can buy all of the PandaTokens at a very cheap rate (JK, they don't have any real value and I don't intend to take it anywhere).

What crypto are you planning to make?

https://www.instagram.com/p/CVekrTrvdjV/
