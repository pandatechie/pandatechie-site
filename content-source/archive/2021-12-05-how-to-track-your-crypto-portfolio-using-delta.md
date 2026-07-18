---
title: "How to Track Your Crypto Portfolio using Delta?"
date: "2021-12-05"
slug: "how-to-track-your-crypto-portfolio-using-delta"
categories: ["Cryptocurrency"]
tags: ["centralized exchange", "exchange", "portfolio", "tracker"]
original_url: "https://pandatechie.in/2021/12/05/how-to-track-your-crypto-portfolio-using-delta/"
cover_image: "https://pandatechie.in/wp-content/uploads/2021/12/image-6.png"
archive: true
---

Every time I hit the **refresh** **button** on my social media feed, there's someone who is saying that you should buy **bitcoin** because it's still very **early**. While they are true, they often overlook the **downsides** of **newer** **technologies**. Yes, it's because we are **so new in the entire crypto ecosystem** and **web3**, there's a lot of **ground** to **cover** before we can see the **mass** **adoption**. One issue coming out of this **nascence**, that I face on a daily basis, is **tracking** of my **crypto** **portfolio**.

You see, in **centralized** exchanges, they would tell you the **amount** of the **assets** that you have and it's **current** **value**. Some exchanges might also show the **net profit/loss**. But no body is talking about my **lifetime**, **asset wise**, **profits or losses**. This is implemented so seamlessly in stock brokers like [Zerodha](https://pandatechie.in/2021/04/13/kite-zerodhas-disruptive-fintech-platform/), ICICI Direct, [Upstox](https://pandatechie.in/2021/04/24/upstox-new-age-stock-broker/) etc. that I kind of miss it now.

![](https://pandatechie.in/wp-content/uploads/2021/12/image-6.png)

Amongst the exchanges that I use: CoinDCX, WazirX, Binance, FTX, none of them have this feature. Oh, I have heard that **Coinswitch Kuber** has it, but it was late before I came to know about it.

So I decided to take matters in my hands and **track** that damned **portfolio** of mine, spread across **various** exchanges. This blogpost reviews the platform that I doubled down on: **Delta**. How to track your **crypto** **portfolio**? Let's go!

## Why Delta?

Before jumping in to this particular platform, I tried to dabble around with a couple of apps. A quick context of why I chose Delta over the others.

* It had a rather **simple** **UI**. Other apps on the top of the charts like **blockfolio**, **Pionex**, **Coin Market Manager** had other services too, which kind of felt like a clutter to me. I already have so many crypto related apps. So I wanted one just for my portfolio management and nothing else.

![](https://play-lh.googleusercontent.com/zGGq09jLVBGj9H6lfuvp5_v1mviVy5l-MGdbWjHPVbMZIjePf7N8IsmEUFb1pLtzj8Aw)

* This one is both **downside** and **upside** of Delta. It connects to all key **foreign** **exchanges**. This means I could easily connect to **Binance** (which has most of my holdings) but missed out on **CoinDCX**, which is my go to platform for multiple purchases.

* In terms of cost, some exchanges **charged** for connecting to **exchanges**, delta was free up to a certain limit.

## How to Connect Binance with Delta:

In this section, we would connect **Binance** with **Delta** so that it can track your portfolio **automatically** without any manual intervention. For that, let's first understand what all do we need:

* Delta application (Duh!) ([Google Playstore](https://play.google.com/store/apps/details?id=io.getdelta.android&hl=en_IN&gl=US) || [iOS App Store](https://apps.apple.com/us/app/delta-investment-tracker/id1288676542))
* You would also need a **laptop** to login to Binance. The mobile app does not have the options we are going to use.

Sorted? Let's go.

### Step 1:

Head over to the **menu** as shown in the **screenshot** and **tap** on **connections**. You would find options to connect with **exchanges**, **wallets** and **brokers** here. You want to head over to the **exchange** and select **Binance** if you are outside US or Binance US if you are within the states.

### Step 2:

Head over to [Binance](https://www.binance.com/en) and login with your credentials. Head over to your profile picture icon and from the dropdown menu, select API Management. (Screenshot below)

![](https://pandatechie.in/wp-content/uploads/2021/12/image-2-1024x483.png)

### Step 3:

Create a label for this API. You might want to do it multiple times for **different** **purposes** in the future, so let's call what it is right now: **Delta API**.

### Step 4:

Click on **create API** and verify using your **email ID** and **mobile** **number**. Why? Because you are essentially **exposing** your **personal** **financial** **data** through this API to a **third** **party**. So beware of the consequences of this falling in the incorrect hands.

Once verified, you would see a screen that looks something like what is is shown in the **screenshot**. Keep this data **handy** because you are going to use it in the Delta application.

![](https://pandatechie.in/wp-content/uploads/2021/12/image-3-1024x490.png)

Make sure that read only option is enabled here. You could edit the restrictions from the button but since we are simply tracking the portfolio, it is better that you give the read only access. Further access is meant for bot trading etc.

### Step 5:

From the application, select the camera button you see next to the API key. Scan the QR code shown in the screenshot above and it will automatically fetch API key and API Secret. Alternatively you can also copy and paste it from Binance (I would judge you if you did so). At this point you would have four options to import which are pretty much self explanatory:

* Import all transactions
* Import all transactions since date
* Import new transactions only (Transactions that you would make after connecting to Delta)
* Import balances only (This would only show the current balances and NOT PnL.)

![](https://pandatechie.in/wp-content/uploads/2021/12/WhatsApp-Image-2021-12-05-at-2.20.15-PM-502x1024.jpeg)

## Conclusion:

And that's pretty much it. Once you have completed the steps above, your portfolio should get refreshed in a minute or so. If there is any issue with the API, there is an option to manually add or delete the data as well.   
I personally had some glitches while portfolio was trying to gauge my PnL on staking rewards. However, after manual tweaking, it is working just fine.

Secondly, I also added my transactions from Indian exchanges manually and it merges it with Binance transactions seamlessly.

If you have a better solution of solving this problem, would love to hear from you.
