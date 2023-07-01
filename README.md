# USA-China Great Power Competition

## Birth-Death Model for Population Demographics: United States & China

**Death Rate, crude( per 1000 people)**

![image](https://github.com/LNshuti/USA-Competitive-Advantage/assets/13305262/423d7fed-3e24-470b-94a3-26b34822b595)

*Source: World Bank data. https://data.worldbank.org/indicator/SP.DYN.CDRT.IN?locations=CN-US*

### Overview

The birth-death model, frequently used in ecology and epidemiology, can also be applied to demography to study changes in population over time. In the context of demographic analysis, the birth-death model allows us to track and predict changes in population size. We calculate the net change in population by subtracting the number of deaths from the number of births in a given period.

```
Net Population Change = Births - Deaths
```

This simple model is a fundamental part of population projection methods, contributing to our understanding of demographic trends, social changes, and policy-making implications.

#### United States

In 1950, the United States population was approximately 150 million, which rose to around 331 million by 2020. The annual birth rate decreased from 24.1 (per 1000 people) in 1950 to around 11.6 by 2020, while the death rate has seen lesser changes.

```python
# 2020
births = US_population * birth_rate / 1000 = (331 million * 11.6)/1000 = 3.84 million
deaths = US_population * death_rate / 1000 = (331 million * 10.44)/1000 =  3.46 million
net_population_change = births - deaths = 3.84 - 3.46 = 0.38 million
```

##### Immigration


#### China

China, the world's most populous country, had a population of approximately 551 million in 1950, which surged to over 1.4 billion by 2020. Birth rates have varied due to factors such as the One-Child policy, declining from 36.9 (per 1000 people) in 1950 to roughly 11.3 by 2020. Death rates have also decreased over time.

```python
# 2020
births = China_population * birth_rate / 1000 = (1.4 billion * 11.3) / 1000 = 15.82 million
deaths = China_population * death_rate / 1000 = (1.4 billion * 7) / 1000 = 9.8 million
net_population_change = births - deaths = 15.82 - 9.8 = 6.02 million

```

##### Immigration

**Trade relationships**
----------------------

**Imports**
-----------

![image](https://user-images.githubusercontent.com/13305262/231326784-68aa4684-0841-43e4-a0ae-49e485eff4c9.png)


![image](https://user-images.githubusercontent.com/13305262/231327133-402ab1f8-7bf7-4aa5-9642-2944e22aad09.png)

**Exports**
-----------

![image](https://user-images.githubusercontent.com/13305262/231329056-a465b243-d92c-473f-a877-d3b02bb3652a.png)

![image](https://user-images.githubusercontent.com/13305262/231329260-877b3c33-93d5-4035-bd70-be99c07bbc80.png)

## References
-------------
1. https://atlas.cid.harvard.edu/
2. American Community Survey. 2021. Accessed July 1st 2023. https://data.census.gov/table?q=DP02
