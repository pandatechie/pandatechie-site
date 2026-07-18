---
title: "What is XIRR and How to Calculate it?"
date: "2021-04-28"
slug: "what-is-xirr-and-how-to-calculate-it"
categories: []
tags: ["BlogchatterA2ZChallenge", "Finance", "Returns", "XIRR", "mutual fund", "return"]
original_url: "https://pandatechie.in/2021/04/28/what-is-xirr-and-how-to-calculate-it/"
cover_image: "https://dannydainton.files.wordpress.com/2017/06/angtft.jpg?w=816&amp;h=9999"
archive: true
---

There are surprises for guessing this. In a [challenge](https://pandatechie.in/2021/03/27/blogchattera2z-challenge-theme-reveal-fintech-platforms-in-india/) where you are **supposed to write with** [**every letter of English** **alphabet**](https://pandatechie.in/tag/blogchattera2zchallenge/), you are **bound** to get **stuck** on the likes of **'Q' and 'X'**. And if your **theme** of writing has been **fintech**, you can be sure of the fact that **letter 'X' is going to be difficult**. So this time around, I decided to cover a very important aspect of **investing in mutual funds** world called **XIRR**. Because I also would tell you in this blogpost that how do we **calculate XIRR** using simple, good old, **excel**, it is a **fin+tech** of sorts. If you don't agree, focus on the keyword '**sorts**'.

A few days ago, I tried to cover an important metric for evaluating returns: [CAGR](https://pandatechie.in/2020/11/25/what-is-cagr/). But one may wonder, that CAGR is used to evaluate returns over a period for **lumpsum investments**. In all likelihood, we don't invest lumpsum amounts. More than often it is in the form of **monthly investments a.k.a SIP**. We invest in Systematic Investment Plans by in putting in a fixed/variable amount in a mutual fund at a fixed interval. So how do we calculate returns for an investment (stretched over a period of time) where there are **multiple entry points**. Enter: **XIRR or Extended Internal Rate of Return**.

## XIRR vs CAGR

The best way to pick the correct metric for evaluating a return amongst CAGR and XIRR would be to gauge the number of entry and exit points.

So if you are entering an investment instrument **once** and exiting it **once**, CAGR would work perfectly fine. However, if you invest over a **period of** **time in bursts**, or you may also **redeem/exit partially** in that period, CAGR won't help. Latter cases would need XIRR to evaluate the returns.

## Why XIRR?

Let's understand with the help of an example. Suppose you have invested in a **mutual fund with Rs. 1000 as a monthly investment (for 1 year) starting from 5th January 2019**. Now, your first installment is going to stay invested for **14 months**. Second installment will be invested for **13 months** and the final installment would be invested only for **1 month**. So, it is fair to assume that returns these investments are making is not going to be the same.

|  |  |
| --- | --- |
| SIP Date | Amount |
| 05-01-2019 | -1000 |
| 05-02-2019 | -1000 |
| 05-03-2019 | -1000 |
| 05-04-2019 | -1000 |
| 05-05-2019 | -1000 |
| 05-06-2019 | -1000 |
| 05-07-2019 | -1000 |
| 05-08-2019 | -1000 |
| 05-09-2019 | -1000 |
| 05-10-2019 | -1000 |
| 05-11-2019 | -1000 |
| 05-12-2019 | -1000 |
| 05-01-2020 | -1000 |
| 08-02-2020 (Redemption) | 14500 |

Illustration of SIP for 1 year @Rs. 1000 p.m.

So, if we were to calculate the absolute returns in this case, we would get a figure of **11.5%**

=(14500-13000)/13000

Do you think that is the return you are making? Absolutely not!

## How to Calculate XIRR:

A labor intensive way of doing it would be to calculate it for each 1,000 using a pen and paper. Convenient right?

![Meme Showing No body has time to manually calculate returns](https://dannydainton.files.wordpress.com/2017/06/angtft.jpg?w=816&h=9999)

So, thanks to excel which has ready formula for calculating XIRR (Office 2016 onwards). Simply type in **=XIRR** in the cell. It seeks two arguments from you:

A. The amount range (which includes redemption as well)

B. The date range

So for the above example, calculations would look something like this:

![How to calculate XIRR in excel.](https://pandatechie.in/wp-content/uploads/2020/11/image-30.png)

Calculation of XIRR in Excel

Using this, XIRR for this investment comes out to be **19.8%**. And that is the return we are going to make.

There are a a few things you need to keep in mind for this formula to work:

* Date has to be in DD-MM-YYYY format. For some reason, other formats don't work.
* All the outflows (from your PoV) should be in negative and accompanied by a minus(-) sign.
* All in the inflows (from your PoV) should be in positive (+).

The same method is also going to work for the following cases as well:

* **If entry points are not uniform**: In case you may not be able to invest for a couple of months every now and then.

* **If amount is not consistent**: You may invest a varied amount in SIPs depending on the situation. Especially if you are into business and don't have a fixed income.

* **If there are multiple payouts:** You may redeem your amount partially to book profits or in case you need money.

## Conclusion:

XIRR is one of the key metrics when you are comparing performances of multiple mutual funds. Once again, don't fall in the trap of absolute returns and be a smart investor. Hope this adds value to your life (literally)

What are your thoughts about this? Have you ever used XIRR as a metric to gauge your MF performance?

This blogpost is in association with [Blogchatter's](http://theblogchatter.com) #BlogchatterA2ZChallenge.
