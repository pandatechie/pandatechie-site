---
title: "Proto: Next Incarnation of Maps?"
date: "2024-08-25"
slug: "proto-next-incarnation-of-maps"
categories: ["Cryptocurrency"]
tags: ["Project", "deep dive"]
original_url: "https://pandatechie.in/2024/08/25/proto-next-incarnation-of-maps/"
cover_image: "https://pandatechie.in/wp-content/uploads/2024/08/Beige-Aesthetic-Blog-Banner-1-1024x576.png"
archive: true
---

It was one of those hangry evenings, where you reconsider legal bans on cannibalism. Glued to the screen, I kept on visiting the Zomato app, watching my Tandoori Chicken travel at the speed of a snail. Half dead, lying on my sofa, I finally got the coveted notification:

"Your order has been delivered"

![Proto: Next Incarnation of Maps](https://pandatechie.in/wp-content/uploads/2024/08/Beige-Aesthetic-Blog-Banner-1-1024x576.png)

But wait - to whom?

I instantly called the delivery person, and what came next was one of my biggest fears come true.

See, I live in I-2706. So? Is it "I" or an "l"? Get it? This is exactly the plight of hundreds of delivery agents, every day. If I experience it 2-4 times a month, imagine the quantum of the problem for residents of 216 flats in I wing.

This is one of the smaller problems in the mapping ecosystem. Clunky, non-standarized, human-unfriendly addresses are some of the major concerns. On average, [this leads to economic losses worth $10–14 billion annually in India](https://www.researchgate.net/publication/323164874_Economic_Impact_of_Discoverability_of_Localities_and_Addresses_in_India)*.*

So, what do we do? Just live with it? After all, you can't choose your address.

Nope! Today, I present a potential solution to this major irritant. You are in for a ride on the following topics:

* Why Maps Deserve Better and Why Now?

* What exactly needs a fix?

* How 'Proto' fixes it?

* A Case Study of 'Proto' in Action

## Maps: The Forgotten Hero

If there were a reservation category in India for navigationally challenged individuals, I would have landed a government job. My reliance on maps is so extensive that I find myself shutting down when someone starts explaining the routes the conventional way.

Recently, I was visiting one of my relatives for Rakshabandhan. They had just moved homes, and my uncle didn't know how to share a pin.   
  
So instead, he chose to say, "You take 3 flyovers and take right from the fourth one"  
  
'*Ummm. Uncle, I can't drive and count the flyovers at the same time*'

Anyway, there are roughly [50 million searches, and over 2.5 billion kms mapped](https://economictimes.indiatimes.com/tech/technology/google-announces-ai-powered-features-for-maps-in-india/articleshow/106130709.cms) in India on Google Maps.

Globally, Google Maps has over a billion users.

But how many of us actually contribute to the maps? Do we even know that there's an option to do that?

According to a 2024 survey, Google has roughly [120 million contributors](https://www.enterpriseappstoday.com/stats/google-maps-statistics.html), which accounts for only 10% of its user base.

The truth is, maps have never been the sexy, in-vogue topic of discussion in tech. They’re often in their own corner, with an almost cult-like community dedicated to their creation and utilization.

### Why is that Set to Change?

You might ask that what will suddenly change this status quo, right? Well, it is not a conjecture but based on some mega trends as discussed below.

![](https://pandatechie.in/wp-content/uploads/2024/08/Green-6-Points-Creative-Process-Diagram-Infographic-Graph-1.png)

#### 1. Technological Advancements:

The infrastructure layer required to turbocharge maps has been up and running smoothly for the past couple of years. Take, **Spacetech democratization**, for instance. Thanks to the likes of ISRO and SpaceX, access to Earth Observation data and satellite imagery is on the rise. This means maps will become more accessible, accurate, and up-to-date than ever before.

Secondly, **AI** is all the rage. Better AI capabilities will enable real-time vectorization of satellite imagery, allowing maps to reflect environmental and built-form changes as they happen.

#### 2. Evolving User Experience:

Even users do not expect maps to be docked on their car dashboard solely. They are experiencing technology in new ways.

Consider, **Wearable technology**. The next evolution of personal devices will focus on augmenting vision, making maps an integral part of how we experience and engage with reality.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-13-1024x556.png)

An illustrative view of the world through your wearable glasses

Apart from that, **Personalized reality** will become a significant trend. AI and map data will enable the rendering of infinite personalized versions of reality, tailored to individual needs and preferences. Apple's Vision Pro is a significant step in that direction.

### 3. Creator's Economy:

Ever since the pandemic, the creator's economy has been booming. And believe it or not, maps are nothing but an extension of content.

For example, platforms like [OpenStreetMap](http://openstreetmap.org/) allows individuals to contribute to and create detailed maps, turning cartography into a collaborative creative endeavor.

Creators are developing visually striking and thematic maps, turning geographic data into artistic expressions and infographics.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-14-1024x640.png)

You could use maps as storytelling media. Digital maps are now being used to tell stories, with creators embedding multimedia content into geographic contexts.

And, there is no dearth of monetization opportunities as well. Location intelligence and map-based apps are offering real $$ for contributing to their platform.

To top it all off, there are legit communities around maps as well. For instance, many creators spent hours playing [Geoguessr](http://geoguessr.com) during Covid, garnering millions of views.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-15-1024x575.png)

Samay Raina raising money by playing Geoguessr on livestream for hours during Covid

## The Fault in Our Maps:

We get it. Maps were once an abandoned tech child. But why exactly does it need attention now? What's wrong with them? I open Google Maps, reach my location -what else do I need?

Well, first of all, thank you for dumping your privilege on us. The real problems starts in unplanned, tier 2 and 3 cities with cluttered streets and old buildings.

What exactly are these problems? Glad you asked.

![](https://pandatechie.in/wp-content/uploads/2024/08/Green-6-Points-Creative-Process-Diagram-Infographic-Graph-3.png)

Problems with Current Mapping System

### 1. Human-unfriendly identifiers:

Current solutions often rely on obscure strings or random words assigned to locations, which are difficult for people to communicate and remember. There's a need for more intuitive and user-friendly location identifiers.

For example, have you ever seen addresses in the following format on your maps app?

![](https://pandatechie.in/wp-content/uploads/2024/08/image-16.png)

These are called plus codes that represents a location.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-17-1024x580.png)

While this initiative helps systems understand the coordinates better, humans can barely use it.

My Zomato guy will spit in my food if I ask him to come to 420X69C+42.

Solutions like Google Plus Codes, What3Words or Pataa have been tried in the past to solve this problem.

But then, they end up creating a new set of issues as follows.

### 1.1 Lack of interoperability:

Many existing mapping solutions are platform-specific and difficult to use universally across different systems.

Currently, maps are utilized in logistics, ride hailing services, autonomous cars, government agencies etc.

However, using any of these services (What3Words, Plus Codes) that are non-native to the ecosystem is not possible.

### 1.2 Lack of customization:

And you thought only web3 has UX issues!

Many existing systems assign codes to places by default, without allowing user customization. This limits the personalization and a user-centric approach to location data.

For example, imagine a local tailor's shop in Dharavi. The address is marked as "Shop No. 3, Lane 7, Dharavi" by default mapping systems.

However, this generic label fails to capture the shop's well-known local identity as "MM Tailors," a name familiar to residents for decades.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-19-1024x682.png)

The inability to customize this location identifier limits the usefulness of the map for locals and visitors alike, who rely on community knowledge rather than official designations to navigate the area.

### 2. Scalability issues:

As urban areas grow rapidly, especially in developing countries, traditional addressing systems struggle to keep pace. More adaptable and scalable solutions are needed.

Incumbents will find it increasingly difficult to update maps in real-time due to cost barriers. Therefore, it is important to involve community in this process.

### 3. Dialects:

India is often described as multiple countries mushed together. To appreciate this nuance, maps need to cater to different languages.

This creates challenges in finding, typing, pronouncing the actual locations.

Unless there is an interoperable solution with common identifiers, a Delhiite moving to Chennai will always face problems.

### 4. Insufficient participation of stakeholders:

We've already discussed how maps are often treated as a purely transactional product. There's often a lack of involvement from key stakeholders in the design process.

tl;dr 👇

![](https://pandatechie.in/wp-content/uploads/2024/08/image-21.png)

These problems highlight the need for more user-friendly, customizable, interoperable, and privacy-conscious mapping solutions that can scale with rapid urban growth and provide accurate, consistent data across various applications.

## Proto: The Hero We All Need

[Proto](http://protomap.xyz) is a decentralized mapping platform that aims to build a new, more accessible and efficient way of handling location data.

I appreciate and love the content lens they have applied to the whole mapping ecosystem.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-20-1024x875.png)

Proto is creating a foundational layer for map data, making it more transparent, verifiable, interoperable and accessible.

At the heart of Proto is the Localcode, which assigns human-readable, customizable addresses to any location on Earth. These addresses are designed to be more intuitive and user-friendly than traditional coordinates or complex addressing systems.

![](https://pandatechie.in/wp-content/uploads/2024/08/0_GO9QQhcaSxYn_68S.png)

Localcode

For example,

**We have User A: Shankar**

* He lives in an apartment with his partner Neha: *101, ABC Apartments, XYZ Neighborhood, Main Road, Near Major Hospital, New Delhi, 110001*

* And their office is at: ***505, PQR Office Park, Building R, GHI Neighborhood, 2nd Road, Near University Gate K, New Delhi, 110053***

* Shankar creates two localcodes for these places, repsectively:  
  - ***shankar.home.proto***  
  - ***shankar.work.proto***

And the real beauty of Localcode lies in its composability and interoperability.

This is one of they key levers of blockchain innovation, and localcodes leverage it to enable a map data-based ecosystem for Proto.

Imagine if anyone could build anything related to maps using this foundational layer.

With Google, the best you could do is use APIs to create whatever possible with the exposed data.

Proto aims to make detailed, accurate location data more accessible to developers, businesses, and individuals, potentially enabling new services and applications.

While Proto can be used for general mapping purposes, it also has potential applications in various fields such as urban planning, logistics, emergency services, and renewable energy deployment.

### Why Crypto Though?

I work for a Web2 company, focused on scaling Web3 applications relevant for our businesses. One obvious question I often encounter is: Why crypto or Blockchain?

Proto seems to have one of the best possible answers to this question.

I will explore this by drawing parallels between Proto and ONDC. This will serve as a primer for two aspects:

* Why couldn't Proto be a simple ONDC implementation?
* Why should ONDC learn how to integrate web3 incentives to solve their problems?

Proto, like ONDC, aims to create a decentralized infrastructure for location data. Both face similar challenges in terms of adoption and network effects. However, Proto's approach of using blockchain technology and tokenization could potentially give it an advantage in overcoming the cold start problem that ONDC might encounter.

For normies, ONDC (Open Network for Digital Commerce) is an ambitious initiative by the Indian government to create a decentralized e-commerce ecosystem. It aims to democratize digital commerce by providing an open network that any seller can join, potentially breaking the monopoly of large e-commerce platforms.

![](https://pandatechie.in/wp-content/uploads/2024/08/1694129493904.png)

Architecture of ONDC

But ONDC, just like any other marketplace, faces the chicken and egg problem.

* Sellers won't join without buyers
* Buyers won't join without sellers

Crypto solves this problem in two ways:

Token incentives can solve the cold start problem by encouraging early adopters with crypto tokens.

And decentralized governance allows for community-driven decision-making, which can potentially increase both trust and adoption.

## Proto'ing Tyres Supply Chain:

In my opinion, early adoption for Proto would be seen in B2B before B2C.

Recently, Bhavesh Aggarwal, founder of OLA, [announced](https://indianexpress.com/article/business/economy/ola-exits-google-maps-to-save-rs-100-cr-yr-with-in-house-maps-9437572/) that they are getting rid of Google Maps with their in-house mapping solution for their fleet.

This move has helped them save INR 100 Crores per year.

![](https://pandatechie.in/wp-content/uploads/2024/08/1-1-1024x553-1.jpg)

What I am trying to say is that quantum of impact is much higher in B2B, and B2C will benefit from this revolution in due course.

### The 'Tyre-ing' Delivery Process:

I work with a leading tyre brand in India and have had the opportunity to wear various hats in the organization, including Sales, Supply Chain and Digital.

The tyre you go to buy at a store has traveled thousands of kilometers to reach you.

It starts its journey in a manufacturing plant located in either Halol, Chennai or Mumbai.

From there, it is transported to around 12 DC (distribution centers).

These DCs cater to around 120 CFAs (Carrying and Forward Agents) across the nation.

The CFAs then either deliver it to the bigger shops directly (5000+), or to a distributor's network who in turn handles the delivery to 50,000+ sub-dealers.

So much effort for you to incessantly honk in a traffic jam. Right?

#### Problem 1: Where are you located?

While evaluating me as a potential groom for their daughter, my in-laws decided to deploy their relative in Gurugram to check on my office.   
  
My visiting card had our CFA address (Khasra No. 18, Paani ki Tanki ke Neeche).  
  
Hell broke loose, when they realized that my office doesn't exist.  
  
I am thankful (or maybe not) to that relative who pointed out that it's an industrial area where my office might be buried somewhere.   
  
Or else, I could have been dismissed as a scammer!

Over the years, I have traveled extensively to these CFAs due to the nature of my job. And trust me, I haven't found a single CFA that is searchable within the bounds of sanity.

The problem starts when you realize that these are de-facto locations for all transport vehicles, who are often rented, carrying tyres to and fro for the entire network.

But this is just the beginning.

#### Problem 2: I am the OG Raj Tyres, He is New Raj Tyres:

Every month, we add new sub-dealers and churn out old ones. It is a part of every FMCGish businesses.

These sub-dealers are catered by an on-field employee known as a DSE (Distributor Sales Executive). DSEs have a hard time locating them given that their beat plans include visits to a particular store, only once a week.

Inability to find a store aside, imagine if incorrect order is delivered. The inventory at an ERP level goes for a toss.

For anyone working in the field sales operations, it would be a common occurrence to see entries like Raj Tyres (Chota bhai), Raj Tyres (Bada Bhai) in their CRMs.

And if that's the way one chooses to address them, then maps should adapt to it, not you. Localcode, solves this.

A report by Capgemini found that last-mile delivery accounts for 41% of total supply chain costs and the inefficiencies in this stage can significantly impact the overall logistics expenses.

#### Problem 3: The Road Not Taken

And all these problems are not buried deep inside the operational rigmarole. It has been identified as a critical piece and we have been trying to solve it through machine learning.

But it always fall short since pin codes aren't the best way to define an area. Within this single pin code, there can be numerous delivery points, spread across a complex network of streets and localities.

Apart from that, pin codes don't account for the intricate layout of streets, one-ways, traffic patterns, or local landmarks, which greatly affects the optimal route.

AI algorithms relying solely on pin codes might group distant deliveries together simply because they share a pin code, missing opportunities to optimize, based on actual proximity and road networks.

A [study](https://www.sciencedirect.com/science/article/pii/S0921344922005043) by Boston Consulting Group found that optimizing delivery routes can reduce mileage by 10% to 30%, translating to significant fuel and time savings.

![](https://pandatechie.in/wp-content/uploads/2024/08/image-22.png)

For local context, [Freight Tiger](https://www.freighttiger.com/), a leading player in this industry is [valued at ~INR 500Cr](https://entrackr.com/2023/10/tata-motors-to-acquire-27-stake-in-freight-tiger-for-rs-150-cr/). Imagine if Proto solves their ML problems, we have a gold mine at hand.

### Proto to the Rescue:

Piggybacking on the ethos of Proto - decentralized, composable and human-friendly addresses - we can now choose to create a Supply Chain application specifically for all our channel partners.

Proto's Localcode system offers a comprehensive solution to the mapping and location challenges faced by our company.

*By providing unique, human-readable identifiers for each point in the supply chain, from CFAs to individual dealers, Proto could significantly improve location accuracy and reduce confusion.*

This system would replace vague or confusing addresses with precise, easily shareable Localcodes, making it simpler for transport vehicles, DSEs, and other stakeholders to locate their destinations.

Furthermore, the hierarchical and customizable nature of Localcodes could help manage the complex network of dealers and sub-dealers, addressing issues such as similarly named stores and frequent additions or removals from the network.

Each dealer, regardless of similar names, would have a unique Localcode; e.g.,

* Raj.tyres.original.vashi;
* Raj.tyres.new.vashi

*Localcodes could be integrated with the company's CRM, reducing confusion for DSEs and ensuring accurate order deliveries.*

Unlike pin codes, Localcodes provide precise location information, allowing for more accurate route planning.

*Additionally, localcodes could incorporate local landmarks or commonly used names, making navigation easier for delivery personnel.*

While full implementation would require some change management, the potential for cost savings and efficiency improvements makes Proto a promising solution for the persistent location challenges in the tyre distribution industry.

## Conclusion:

In a world where technology evolves at breakneck speed, our maps seem to have been left in the dust. But Proto is stepping up to transform this landscape.

Once you build everything around user and not the technology, you end up with magic.

While I niched it down to specific supply chain problems in our industry, I am sure this has the potential of horizontal deployment across the distribution gamut.

Until then, see you at panda.office.mumbai someday!

Here’s to Proto—the hero we didn’t know we needed, but one we’re certainly glad to have.

## References:

1. [Entrackr](https://entrackr.com/)
2. [ONDC Landscape in India](https://www.antler.co/blog/ondc-landscape)
3. [Crypto & Net new marketplaces](https://variant.fund/articles/crypto-net-new-marketplaces/)
4. [Intro to Localcode](https://proto-geo.medium.com/localcodes-the-92e15a00bf9e)
5. [The future of maps](https://medium.com/@proto-geo/maps-are-having-a-moment-finally-15a60c48a5fc)
6. [CEAT](https://ceat.com)
