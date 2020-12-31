[Needs More Information]

# Dataset Card for The Pile

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** http://pile.eleuther.ai/
- **Repository:** https://github.com/EleutherAI/The-Pile
- **Paper:** todo
- **Leaderboard:** http://pile.eleuther.ai/
- **Point of Contact:** [EleutherAI](mailto:contact@eleuther.ai)

### Dataset Summary

The Pile is a 1.25 TiB diverse, open source language modelling data set that consists of 22 smaller, high-quality datasets combined together. By including as many different types of text data as possible, it ensures that models trained using the Pile will have much broader generalization abilities.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

The Pile consists predominantly (97%) of English.

## Dataset Structure

### Data Instances

```
{"text": "Wirex, a prominent UK\u2019s FCA supported cryptocurrency remittance provider, has partnered with Stellar, bringing in its over 2 million users and more than 5000 business clients into the cryptocurrency project\u2019s ecosystem.\n\nThe surprising collaboration will see Wirex launch \u201c26 fiat-backed stablecoins\u201d on Stellar network, a crypto platform that also partnered with tech giant IBM.\n\nStellar network is receiving different supports from big firms across the globe. The launch of Wirex Stablecoins on Stellar Network infers that the crypto platform is uniquely designed to also accommodate Stablecoins.\n\nWhile some analysts opined that Stablecoins are created to bring growth into the crypto space, they are becoming a solid way to reduce crypto volatility due to the fact that their value are pegged to fiat currency.\n\nFor Low Cost and Almost Instant Across Border Remittance\n\nWhen Stellar-based Wirex stablecoins finally launches, they are going to be used to perfect low-cost and all most immediately cross-border remittance, just like the IBM Stablecoin which has received support from six respected international banks.\n\nFirst of its Kind in the Crypto Space\n\nThis Wirex Stablecoins is going to be the first of its kind for many reasons. They are the maiden stablecoins to be spend easily in day to day dealings using Wirex Visa card. It is the first stablecoins to be pegged to different fiat currencies like USD, EUR, GBP, HKD and SGD with exchange at interbank rates. Similarly, it is the foremost stablecoins that can be easily exchanged with other virtual currencies at OTC rates.\n\nImportantly, it is the first stablecoins to be released by an FCA supported crypto and fiat payment firm. All these will propel the stablecoins when it is finally unveiled.\n\nWirex\u2019 Over 2 million Users and 5K business clients Added to Stellar (XLM) Ecosystem\n\nThe advent of Wirex Stablecoins on Stellar network means the FCA-regulated company\u2019s over 2 million Users and 5K business clients are to be added to the Stellar ecosystem. This is definitely going to propel the cryptocurrency project.\n\nWirex has an outstanding user base. The number of people using the Wirex platform are enough to bring revolution to the Stellar (XLM) network.\n\nMore Use Cases Than Expected.\n\nThe stellar-based stablecoins have diverse use cases than one can imagine at the moment. Its functions in the business and retail arena indicate the partnership is the beginning of development for Stellar (XLM).\n\nThe stellar-backed Wirex Stablecoins is unique for international remittance, and offers faster and cheaper alternatives to Mastercard and Visa. It offers immediate token issues and redemption, stands as the beginning of crypto adoption with its instant merchant settlement among other use cases.", "meta": {"pile_set_name": "OpenWebText2"}}
{"text": "Effect of sleep quality on memory, executive function, and language performance in patients with refractory focal epilepsy and controlled epilepsy versus healthy controls - A prospective study.\nWe aimed to evaluate the effect of sleep quality on memory, executive function, and language performance in patients with refractory focal epilepsy and controlled epilepsy and compare these with healthy individuals. We prospectively enrolled 37 adolescent and adult patients with refractory focal epilepsy (Group 1) and controlled epilepsy (Group 2) in each group. History pertaining to epilepsy and sleep were recorded, and all patients underwent overnight polysomnography. Language, memory, and executive function assessments were done using Western Aphasia Battery, Post Graduate Institute (PGI) memory scale, and battery of four executive function tests (Trail Making Test A & B, Digit symbol test, Stroop Task, and Verbal Fluency Test), respectively. Forty age- and sex-matched controls were also included in the study. Significant differences were noted in both objective and subjective sleep parameters among all the groups. On polysomnography, parameters like total sleep time, sleep efficiency, sleep latency, and rapid eye movement (REM) latency were found to be significantly worse in Group 1 as compared with Group 2. Cognitive and executive parameters were significantly impaired in Group 1. Shorter total sleep time, poorer sleep efficiency, and prolonged sleep latencies were observed to be associated with poor memory and executive function in patients with refractory epilepsy. Our study strongly suggests that sleep disturbances, mainly shorter total sleep time, poor sleep efficiency, and prolonged sleep latencies, are associated with impaired memory and executive function in patients with refractory focal epilepsy and to a lesser extent, among those with medically controlled epilepsy.", "meta": {"pile_set_name": "PubMed Abstracts"}}


```

### Data Fields

 - `text`: The text content of the document.
 - `pile_set_name`: The name of the dataset that the data instance originates from

### Data Splits

Train
Validation
Test

The validation and test data is deduplicated for exact matches against the training set.

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]