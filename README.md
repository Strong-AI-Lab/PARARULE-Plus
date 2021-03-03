# PARARULE Plus
The new generated dataset for PARARULE. It is generated based on the closed-world assumption.
PARARULE Plus is an improvement on the dataset of PARARULE (Peter Clark, 2020). The motivation is to generate deeper PARARULE training samples. We add more training samples for the case where the depth is greater than or equal to 2 to explore whether Transformer has reasoning ability.

# PARARULE Plus Data distribution
For each depth dataset, we have more than 100,000 datasets to be used, much larger than the same depth in PARARULE.
## PARARULE Plus
<img src="./image/data-distribution.PNG" width="300" />

## PARARULE
<img src="./image/pararule_depth_distribution.png" width="300" />

# Example
## An example with the non-negation rules for Depth=2 means the question needed to be derived by two rules.
<img src="./image/NonNegationRule-D2-1.PNG" width="500" />

## An example with the negation rules for Depth=2 means the question needed to be derived by two rules.
<img src="./image/NegationRule-D2-1.PNG" width="450" />

# Other links
The PARARULE dataset is from that paper.
 [Transformers as Soft Reasoners over Language](https://arxiv.org/abs/2002.05867). 

The online demo for PARARULE.
https://rule-reasoning.apps.allenai.org/

PARARULE
https://allenai.org/data/ruletaker
