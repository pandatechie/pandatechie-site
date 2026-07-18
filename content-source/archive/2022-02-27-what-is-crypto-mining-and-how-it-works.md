---
title: "What is Crypto Mining and How it Works?"
date: "2022-02-27"
slug: "what-is-crypto-mining-and-how-it-works"
categories: ["Cryptocurrency"]
tags: ["crypto", "mining"]
original_url: "https://pandatechie.in/2022/02/27/what-is-crypto-mining-and-how-it-works/"
cover_image: "https://spectrum.ieee.org/media-library/illuminated-cryptocurrency-mining-farm-racks-in-russia.jpg?id=27400476&amp;width=3000&amp;height=2250"
archive: true
---

All of us have heard that crypto is a decentralized form of money. It is a peer to peer transaction. If that is the case, there is no one safeguarding your interests while you are transferring crypto. In a traditional banking ecosystem, you can reach out to bank if there is an issue with your funds. However, there are no banks involved in crypto world. So how does one ensure everything is working as expected?

![](https://spectrum.ieee.org/media-library/illuminated-cryptocurrency-mining-farm-racks-in-russia.jpg?id=27400476&width=3000&height=2250)

Enter: Miners. These miners validate the transaction and get rewarded with the tokens (BTC/ETH etc.) in return for that. Since they are doing some work to get these rewards, the process is called 'crypto mining'. So today, we plan to talk about what is crypto mining and how it works. The term mining has undergone a paradigm shift ever since crypto came into picture. It is like creating a crypto token out of thin air. Let us explore this in detail.

## What is Crypto Mining?

As we all know, blockchain is made up of blocks of data. These blocks are stacked on the top of one another like Legos, hence forming a blockchain. However, a block cannot be added randomly to the blockchain. Before adding this block, all the transactions within this block have to be validated to ensure everything is fine. The process of validating these transactions to add the next block in the blockchain is known as crypto mining.

![](https://media1.giphy.com/media/Xtg9ygGsjvouF7vZ1w/giphy.gif)

With that explanation out of the way, the next logical question that comes to our mind is that how does one validate the transaction? What is really meant by validation? This cannot be a manual process for sure. You cannot expect a person to manually sit and calculate if these transactions are correct. So what is happening in the back ground? Let us try to understand.

### Validating the transactions:

While venturing into crypto space, you must have come across this statement multiple times: 'Miners solve a complicated mathematical problem to add the next block in the blockchain.'

This mathematical problem is based on a technical cryptography algorithm called SHA256.

Without going into too much of details, think of it as a game of guessing using nothing but all permutations and combinations. Here's an example:

Think of it in the form of a simple equation like this: A+B = C

Miners are already aware of what A and C are. What they are trying to do is guess B. There is no way of guessing B without using numbers randomly from 0 to 1,2,3,4... and so on.

![](https://pandatechie.in/wp-content/uploads/2022/02/unnamed-file-1024x576.png)

The one who solves this puzzle gets to win the rights to mine the next block and hence claim the rewards.

### Consensus Algorithm:

But anyone can setup a node and take part in the Blockchain maintenance and validation. There are multiple 'nodes' (individual computers) that would want to earn some crypto rewards. So how do we decide who gets to mine the next block?

Turns out that there are multiple ways of deciding the next miner.

![](https://i-invdn-com.akamaized.net/content/pic4b514c91a8c1c68c0827ed632501fec6.jpg)

A consensus algorithm is a procedure by which all the nodes in a network come to an agreement on the current state of the network. Simply put, it is the method by which everyone agrees to decide if the next block is worth stacking in a blockchain.

Now depending on the Blockchain, this task is carried out in multiple ways.

Back in 2008, when Blockchain technology emerged with the advent of Bitcoin, the consensus algorithm used was 'Proof of Work' or PoW in short.

Later a lot of Blockchains moved to something called 'Proof of Stake' or PoS. Currently, there are about 9 different consensus mechanisms being used across different blockchains that exist today. However, 80% of these Blockchains use either of PoW or PoS.

![](https://www.rohasnagpal.com/style/images/mindmaps/_older/consensus-mind-map.png)

Interested in understanding what is PoW and PoS? Well, you have come to the right place. Let us dig deeper.

## Proof of Work:

In a proof of work consensus algorithm, all the nodes compete with each other to find the answer to the mathematical puzzle discussed above.

Think of it like a horse race. Only one of the horses is going to win the grand prize (which in our case is the crypto). However, all of them try their best to win it. Who is the eventual winner, you ask? The fastest of them.

While speed of the horse has so many variables attached to it, for a Blockchain, it is rather simple. The node which can compute faster will reach the answer quickly. This solely depends on the processing power of the system deployed for mining.

This is why you would see a lot of mining rigs have multiple graphic cards stacked together to extract the maximum potential and hence mine faster than everyone else.

![](https://en.bitcoinwiki.org/upload/en/images/thumb/5/55/Ea5b21f014547b4b44cf2dafcd76aad2.jpg/400px-Ea5b21f014547b4b44cf2dafcd76aad2.jpg)

Some of the blockchains that use proof of mining consensus algorithm are Bitcoin and Ethereum.

If you are wondering how much rewards are we talking about here, it is currently at 6.25 BTC per block for Bitcoin. This number gets halved roughly every four years. Back in 2008, this number was 50. We would recommend you to not calculate the dollar value of this now as it will just hurt at this point.

### Proof of Work and Environmental Concerns:

Another aspect that we wanted to highlight was around proof of work (BTC specifically) and environmental concerns.

By now, you might have guessed what is this tussle about. While multiple nodes gun for the rewards, giving it their best shot, only one of them stands a chance to win.

![](https://specials-images.forbesimg.com/imageserve/5d234198142c500008c87aec/960x0.jpg?fit=scale)

What happens to the computational power spent by all the other nodes? You guessed it right. It goes to a waste. If you are still unable to connect the dots, this computational power is generated through electricity and that is where the environmental concerns start rising. For more information on what exactly is the impact of mining on environment, head over to this [blogpost](https://pandatechie.in/2022/01/30/blockchains-and-sustainability-how-green-is-blockchain-technology/).

## Proof of Stake (PoS):

![](https://en.bitcoinwiki.org/upload/en/images/thumb/e/e5/Proof%E2%80%93of%E2%80%93Stake_%28PoS%29.jpg/500px-Proof%E2%80%93of%E2%80%93Stake_%28PoS%29.jpg)

With growing concerns over environmental problems with the proof of work consensus algorithm, the industry came up an alternate way of reaching agreement. This time around the winner of the reward wasn't the one who solved the problem, fastest.

Allow us to explain. In a proof of stake algorithm, only one node gets an opportunity to forge the next block. This means that there is no extra energy (electricity) being spent to validate the transactions.

But if only one node is solving the mathematical problem, how do we ensure that this node doesn't dupe the network? More importantly, how is this node chosen?

Turns out, in order to take part in the proof of stake consensus algorithm, you need to stake some of the native crypto to become eligible to validate the transactions (mine). This amount is generally kept a little higher with an intention to onboard only the serious players. So, when you have a skin in the game, it is highly unlikely that you would cheat right?

![](https://www.ledger.com/wp-content/uploads/2019/10/What-is-proof-of-stake-1.jpg)

The next miner is chosen on the basis of multiple factors like, amount staked, time spent in the network and an element of randomization.

Now this race is being run by a single node (horse) and hence there is no need to rush and spend massive amounts of power to win it. But that doesn't mean that a node can now take its own sweet time and commit mistakes while validating.

If anything goes wrong, network levies a penalty on that node and chances of it getting selected for the upcoming blocks decrease significantly.

The image below will highlight the difference between PoW and PoS

## To Mine or Not to Mine?

Technically, there is no eligibility criteria for someone to become a miner. Anyone with technical know how can start mining. However, unlike older times when people used personal computers to mine, things have changed significantly now.

![](https://media0.giphy.com/media/6fDQ3k4IOqnEA/giphy.gif)

This is because Bitcoin blockchain is made to evolve and adjust the difficulty of the mathematical problem every two weeks roughly. More the number of people which are mining (competition), the more difficult it gets to reach a solution.

Therefore with existing scenario, it is very difficult to mine unless you invest in high power GPUs (Graphic Processing Units) which range from $500 to tens of thousands of dollars. Apart from that, one of these machines is probably not going to cut it.

Today, Bitcoin mining hardware is almost entirely made up of ASIC machines, which in this case, specifically do one thing and one thing only: Mine for bitcoins.

## Where's The Moolah?

While mining may seem like a profitable venture from a distance, the nitty gritty involved is just too much for a newbie. Therefore, if you are just starting out on your crypto journey, I would recommend that you buy it off from a centralized exchange like CoinDCX and HODL. That can be equally rewarding. Don't believe me? Just checkout the returns BTC and ETH have given in past 5 years.

Until then, signing off. Got questions?

https://www.instagram.com/p/CaFG6\_FvNj\_/
