---
title: "What is an Automated Market Maker (AMM)?"
date: "2021-10-09"
slug: "what-is-an-automated-market-maker-amm"
categories: ["Cryptocurrency"]
tags: ["AMM", "Automated Market Maker", "Finance", "decentralized finance", "defi"]
original_url: "https://pandatechie.in/2021/10/09/what-is-an-automated-market-maker-amm/"
cover_image: "https://exchange-support.blockchain.com/hc/article_attachments/360079367271/Screenshot_2020-12-10_at_13.30.25.png"
archive: true
---

Complicated term right? Well, the job it does isn't easy either. So buckle up and catch hold of the nearest chair. As always, I won't be using any fancy jargons to explain this to you. Apart from that, once you wrap your head around this technology, it would feel no less than magic. A part of the **complexity** in the **blockchain** world is also because our **mental** **models** aren't equipped to come to **terms** with these new **developments** in **Decentralized** **Finance** (**DeFi**) world. The very fact that a **piece** of **code** is **replacing** an entire **industry** is just so **overwhelming**. Jumping right into it.

## Centralized Exchanges and Order Book Model:

I am sure you must have traded **stocks** or **crypto** by now on your favorite **exchanges** like [Zerodha](https://pandatechie.in/2021/04/13/kite-zerodhas-disruptive-fintech-platform/), [CoinDCX](http://coindcx.com). These exchanges are **centralized** in nature. This means that companies like **Zerodha** and CoinDCX store your stocks or cryptos with them.

These type of exchanges work on an **order book model**. That means if you plan to buy a specific **cryptocurrency**, say BAT, you place an order at a **specific** **price**. The order book **matches** the price **quoted** by you to all the **bids** raised by the **sellers**. Whenever there is a **match**, your order gets **executed**.

![](https://exchange-support.blockchain.com/hc/article_attachments/360079367271/Screenshot_2020-12-10_at_13.30.25.png)

Supply and demand is automatically taken care of as the users themselves are quoting the best price of their assets. In other words, higher the demand, higher the price of an asset.

## Decentralized Exchanges or DEX and Automatic Market Maker (AMM) Model:

Now the entire narrative of blockchain is developed around **decentralization**. But then what is the point of using a **centralized** **exchange**? Agreed that you are getting rid of **governments** snooping into your account, but what about the **exchange** itself? It is like placing **trust** in a **different** **entity** if not the government.

![](https://images.ctfassets.net/0idwgenf7ije/4x7WOEo3WbGqkrC5OddEa3/8c50159c033cdc83c1c0d471f2b0af24/Gemini-What_Are_Automated_Market_Makers_.png?fm=webp)

So the question that arises is that can we do it without anyone's **involvement** in a truly **decentralized** and **trustless** way? Well, the answer is yes. Enter **Automatic Market Maker or AMM** in short.

AMM helps individuals exchange one cryptocurrency with the other using smart contracts and liquidity pools. Too much to digest? Let's take it from the top:

## How do AMMs work?

Imagine it's year 1850. You are a **farmer**, living peacefully in a **village**. All of you **grow** **potatoes** for living. You can make **fries**, **mashed potato** etc. from that potato but now you are kind of **sick**. Your spouse is **demanding** **something** **else** to eat.

At the same time, a **trader** comes from the other side of the world. He mentions that he knows of a **village** where people are **sick** of eating **apples** every day. He offered a **deal** where he could **facilitate** a deal to **trade** **50,000** **apples** **against** **50,000** **potatoes**. Since that's exactly you were looking for, all your villagers agree.

![](https://images.news18.com/ibnlive/uploads/2019/10/Untitled-design-2019-10-17T091045.576.png?impolicy=website&width=0&height=0)

The trader continues: he has a **magic warehouse** where all these **apples** and **potatoes** will be **stored**. Since there should be a balance between the value of **apples** and **potatoes**, the product of both these **entities** would be equal to **2.5bn** **(50,000 apples X 50,000 potatoes)**.

![](https://media.istockphoto.com/photos/balancing-scale-healthy-vs-unhealthy-picture-id518981951)

This way, if there are **more** **potatoes** than **apples** in the warehouse, each **apple** would **cost** **more** potatoes to buy. If this is clear, congratulations, you just learnt the basic principal of a **constant product automated market maker.**

It is based on the formula X \* Y= k. In our case, X is apples, Y is potatoes and k is always a constant at 2.5bn.

In the **beginning** the price of **apples** is equal to the price of **potatoes** because each of them is kept at a **Re. 1 mark**. However, as the trading (exchange) begins **one might become more valuable than the other** thus pushing it's price more than a dollar.

## Calculations in Automated Market Maker:

Let's continue with our example. Our magical warehouse has began **trading** with 50,000 apples and 50,000 potatoes. Comes along a farmer with his produce of **7,000 potatoes** and wants to **exchange** it with **apples**. So let's calculate how many apples would he get in return:

(Mathematics Time)

Number of potatoes in the magic warehouse: 57,000 (50K+7K)  
Number of Apples in the magic warehouse: 50,000  
  
Using 'X' (apple) \* 'Y' (potato) = k (2.5bn)  
  
X \* 57,000 = 2,500,000,000  
  
This means that number of Apples that should be there in the warehouse to maintain a balance should be:  
  
X = 2,500,000,000/57,000 = 43,859  
  
So how many apples should he get in return?   
  
50,000- 43,859 = 6140 Apples

*Since the number of potatoes in the warehouse was more than number of apples, farmer could fetch only 6140 apples for 7000 potatoes.*

Does our constant product AMM hold **true**? Yes it does **(43,859 \* 57,000 = 2.5bn)**

### Rupee Cost of Potatoes:

Since we started with the cost of Re. 1 per potato, the cost would be **constant** at R**s. 50,000 for the entire lot**. Now that **57,000 potatoes** could be bought in **Rs. 50,000** the cost of each **potato** would be **50,000/57,000 = 0.87p**.

On a similar note, the **cost of apple** would be **50000/43859 = Rs. 1.14**

Its basic supply and demand you see? Since someone brought more potatoes to the magic warehouse, the price of potato fell under a rupee and apple observed a contrary effect.

![](https://englishtribuneimages.blob.core.windows.net/gallary-content/2021/6/Desk/2021_6$largeimg_904412189.jpeg)

### Example 2:

This time another farmer comes along and tries to add 10,000 more potatoes to the magic warehouse. Also, let's call this magic warehouse what it actually is: **Liquidity pool**. Let's quickly run through the numbers:

Number of potatoes in the liquidity pool: 67,000 (57K+10K)  
Number of Apples in the liquidity pool: 43,859  
  
Using X(apples) \* Y(potatoes) = K (2.5bn)  
  
X \* 67,000 = 2,500,000,000  
  
The number of apples that should be in the Liquidity pool = 37,313  
  
Apples he would get in return: 43,859 - 37,313 = 6,546

Can you calculate the rupee cost of each Apple and potato now? Drop your answers in the comments section.

I hope it's a lot clearer now. The rupee value of potatoes and apples would always be equal to 50,000 each in the liquidity pool. The pool will always maintain the ratio of value to 50:50.

## The Real Liquidity Pool:

Jotting down a couple of differences from the above example when you are dealing with real liquidiuty pools:

* Unlike apples and potatoes, real liquidity pools can have **millions worth of cryptocurrencies** locked in it.
* Also, **more** the value locked in a liquidity pool, **stable** are the prices. When you are dealing with 5,000,000 apples and potatoes the impact of 5,000 may not be much right?

## Who is Adding Value to the Liquidity Pool?

In real life, who is bringing those initial 50,000 apples and potatoes to the magic warehouse to get started? Well, its **investors** like you and me. And why would one do that? Because they are **rewarded** with a **fee** during each **transaction**. Even if this fee <1% but the numbers add up really fast.

![](https://agcdn-2mrybbgckm7omi0k.netdna-ssl.com/wp-content/uploads/2019/09/alphagamma-7-surprising-ways-to-attract-new-investors-for-your-business-entrepreneurship.png)

## Conclusion:

Pay yourself on the back. It took me a while before grasping the concept of AMMs and articulating in a blog. Also, please don't judge me next time when I refer to any such technology as magic. Hopefully now, you know why!

What do you think about AMMs?
