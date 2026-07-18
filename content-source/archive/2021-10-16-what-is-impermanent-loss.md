---
title: "What is Impermanent Loss?"
date: "2021-10-16"
slug: "what-is-impermanent-loss"
categories: ["Cryptocurrency"]
tags: ["decentralized", "decentralized finance", "defi", "fintech"]
original_url: "https://pandatechie.in/2021/10/16/what-is-impermanent-loss/"
cover_image: "https://www.leaprate.com/wp-content/uploads/2019/08/liquidity-provider.gif"
archive: true
---

We recently covered the working of an [automated market maker](https://pandatechie.in/2021/10/09/what-is-an-automated-market-maker-amm/). For the uninitiated, it is a way to **exchange** two **cryptocurrencies** (assets) in a way that the **price** is decided by the **amount** of **crypto** left in the **liquidity** **pool**. Simply put, on the basis of **supply** and **demand**, the price of an **asset** is decided. If this sounds a little confusing, don't worry! While you would find the detailed explanation [here](https://pandatechie.in/2021/10/09/what-is-an-automated-market-maker-amm/), a part of this blogpost would cover that as well. For now, let's play some attention to this term: what is **impermanent loss**. We shall dive into the specifics real soon.

## Liquidity Pool and Liquidity Providers (LP)

Think of **liquidity** **pool** as a digital stash. This stash has huge **volumes** of **cryptocurrencies** which are being **swapped**. For example, an **Ethereum** and **Basic Attention Token** liquidity pool, would be full of **ETH** and **BAT**. Initially this pool would contain an **equal** **amount** (Dollar value worth) of **BAT** and **ETH**. But as and when people come and **deposit** a crypto (ETH or BAT), the value of each one of them would **fluctuate**.

How? Say someone comes along and deposits a lot of ETH to buy BAT, the **price of ETH in the liquidity pool will fall down** and more number of ETH would be required to buy a single BAT. The same is true for the flip side as well.

The question that arises is **who** put that **initial equivalent value of ETH and BAT in that liquidity pool** now? The answer is investors. These people, called ***liquidity providers***, come and **deposit** their **crypto** in 50:50 ratio in order to **gain** some **return** out of it. How? Through the **fees** levied to **individuals** who come along to swap their cryptocurrency.

![](https://www.leaprate.com/wp-content/uploads/2019/08/liquidity-provider.gif)

This sounds like a really cool investment right? You just deposit your crypto and make a **sweet ROI** by the fee being charged to the traders. While it is cool, it is definitely **NOT risk free**. And that's what today's blogpost will talk about. Read on.

## What is Impermanent Loss:

***Impermanent loss is the loss incurred by the liquidity provider due to price fluctuations in the liquidity pool such that the LP (liquidity provider) would have been more profitable if he had just held his tokens without providing the liquidity.***

![](https://image.binance.vision/uploads/42d737922c424a71900d7fd9baa9a911.png)

Why impermanent? Because unless you withdraw your liquidity, this loss isn't realized. In other words, impermanent loss is the temporary loss when the share of liquidity provider positions becomes uneven as compared to it's original position.

## Illustration to Demonstrate Impermanent Loss:

Ya. That would make sense. Let's take it with an example. Imagine there is a liquidity pool where you deposit **$10,000 worth of USDT (a stable coin) and 100 ETH.** Since most liquidity pools want a 50:50 ratio, it is fair to assume that 1 ETH here would cost $100 (100 ETH worth $10,000). In totality, you have put a total of $20,000 in the liquidity pool with a hope of earning some income from the trader fees.

![](https://pandatechie.in/wp-content/uploads/2021/10/Liquidity-Pool-1024x576.png)

### Mathematics Time:

Now imagine that the price of ETH on [CoinDCX](http://coindcx.com) is $110. So a trader realizes this arbitrage opportunity and decides to make use of it. He can now buy ETH from our liquidity pool at $100 and sell it on CoinDCX @ $110. So by the rule of constant product automated market maker, he was able to buy 4.652 ETH worth $488 in our liquidity pool. After that, the price of ETH in our pool also shot up to $110. If he would purchase any more ETH from us, he would bear a loss.

Trader Profits:  
  
Trader sold 4.652 ETH at CoinDCX for $511.82. The purchase price was $488. Therefore, the trader made a profit of $23.82  
  
Your Profit:  
  
The liquidity pool now has $10,488 in USDT and 95.347 ETH.   
  
Or, 95.347 \* 110 = $10,488   
  
Total pool value= 10,488 (USDT) + 10,488 (ETH) = $20,976  
  
Total Profits= $976 (Mama Mia!)  
  
But wait...   
  
What's the impermanent loss?  
  
If he had not invested this money in the liquidity pool, the investor would have $10,000 in Stable coin and 100 ETH.   
  
Price of 100 ETH: 100\*110 = $11,000  
  
Total Money: 11,000 (ETH)+ 10,000 (Stable Coin) = $21,000  
  
So the impermanent loss is now at = 21,000 (Money he would have had by NOT investing in L. Pool) - 20976 (Money he has)  
  
= $24

In short, this LP would have made more had he not invested his money in a liquidity pool. This might not seem to be a lot in the first glance, but imagine a situation where the price of ETH drops by 50% or it jumps by 25%. In either case, the losses could have been exponential.

Please note, that if ETH goes back to it's original price of $100, there is no impermanent loss.

## But Why Does Impermanent Loss Happen?

As a rule of thumb, impermanent loss happens when the **two** **assets** start moving in **opposite** **direction** **relative** to each other as compared to the time when you provided the liquidity. So, it's better when the **two assets you are investing in are roughly the same** price.

If both these assets start moving in opposite direction, the exposure to impermanent loss increases. Contrary to this, if both the **assets start moving in the same direction** (can be up or down) proportionately, the LP makes a profit.

The graph below explains the impermanent loss to a LP due to price variation. If you observe closely you would note that price movement in either direction will cause an impermanent loss. **Also, the loss is in the range of 0-25%** if the prices tend to go up.

![](https://finematics.com/wp-content/uploads/2020/08/impermanent-loss-chart-1024x575.png)

You can also calculate the impermanent loss using the calculator available [here](https://www.impermanent-loss-calculator.net/). Simply put in the current and original price of assetsand Viola!

## Why do People Provide Liquidity at all then?

Valid question right? If there is a cash loss, why are people providing liquidity at all? Must be some catch? Well, the answer was always there in front of you. **I mentioned that traders earn a part of the total fees for providing liquidity. This fee might be less (~0.3%) but it adds up exponentially when the total traded volumes are to the the tune of billions.** For example, the traded volume on Uniswap touched $10bn in a single day this April ([source](https://finance.yahoo.com/news/uniswap-weekly-trading-volume-crosses-065600669.html)).

The earning from this trading fee compensates for the impermanent loss and more than often beats it.

But with that being said, there are ways to mitigate impermanent loss to. We shall explore more about it as we go in the upcoming blogs.

## Conclusion:

I am not scaring you, but rather pacifying myself with this. Yes, this is just the tip of the iceberg. The world of DeFi has a lot more to explore and I am all set to take that journey with you.

The question is, are you game?
