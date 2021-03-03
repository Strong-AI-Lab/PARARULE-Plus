# PARARULE Plus
The new generated dataset for PARARULE. It is generated based on the closed-world assumption.
PARARULE Plus is an improvement on the dataset of PARARULE (Peter Clark et al., 2020). The motivation is to generate deeper PARARULE training samples. We add more training samples for the case where the depth is greater than or equal to 2 to explore whether Transformer has reasoning ability.

# PARARULE Plus Data distribution
For each depth dataset, we have more than 100,000 datasets to be used, much larger than the same depth in PARARULE.
## PARARULE Plus
<div align=center><img src="./image/data-distribution.PNG" width="300" /></div>

## PARARULE
<div align=center><img src="./image/pararule_depth_distribution.png" width="300" /></div>

# Examples
## An example with the non-negation rules for Depth=2 means the question needed to be derived by two rules.
<img src="./image/NonNegationRule-D2-1.PNG" width="550" />
The `QCat=0` means the question is generated from non-negation rules and the label is `true`. If the `QCat=0_0`, it means the question is generated from non-negation rules and the label is `false`.

## An example with the negation rules for Depth=2 means the question needed to be derived by two rules.
<img src="./image/NegationRule-D2-1.PNG" width="450" />

##### Depth=2
The `QCat=0_not_notTrue` means the question is generated from one negation rule and another negation rule `and` a positive rule and the label is `true`. 
The `QCat=0_0_not_notTrue` means the question is generated from one negation rule and another negation rule `and` a positive rule and the label is `false`. 
The `QCat=0_true_trueNot` means the question is generated from one positive rule and another positive rule `and` a negation rule and the label is `true`. 
The `QCat=0_0_true_trueNot` means the question is generated from one positive rule and another positive rule `and` a negation rule and the label is `false`. 

##### Depth=3
The `QCat=0_not_notTrue_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and a positive rule and the label is `true`. 
The `QCat=0_0_not_notTrue_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and a positive rule and the label is `false`. 
The `QCat=0_true_trueNot_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and and a positive rule and the label is `true`. 
The `QCat=0_0_true_trueNot_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and a positive rule and the label is `false`. 

##### Depth=4
The `QCat=0_not_notTrue_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and two more positive rules and the label is `true`. 
The `QCat=0_0_not_notTrue_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and two more positive rules and the label is `false`. 
The `QCat=0_true_trueNot_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and two more positive rules and the label is `true`. 
The `QCat=0_0_true_trueNot_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and two more positive rules and the label is `false`. 

##### Depth=5
The `QCat=0_not_notTrue_true_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and three more positive rules and the label is `true`. 
The `QCat=0_0_not_notTrue_true_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and three more positive rules and the label is `false`. 
The `QCat=0_true_trueNot_true_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and three more positive rules and the label is `true`. 
The `QCat=0_0_true_trueNot_true_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and three more positive rules and the label is `false`. 

## Detail for the data generation scripts
### Scripts
##### Depth=2
 - [new_data_generation_NegationRule-D2.py] - The question needed to be derived by two rules, part of them are the negation rules.
 - [new_data_generation_NegationRule-animal-D2.py] - The question with animal entities needed to be derived by two rules includes the negation rules.
 - [new_data_generation_NonNegationRule-D2.py] - The question needed to be derived by two rules, all of them are the non-negation rules.
 - [new_data_generation_NonNegationRule-animal-D2.py] - The question with animal entities needed to be derived by two rules includes the non-negation rules.
##### Depth=3
 - [new_data_generation_NegationRule-D3.py] - The question needed to be derived by three rules, part of them are the negation rules.
 - [new_data_generation_NegationRule-animal-D3.py] - The question with animal entities needed to be derived by three rules includes the negation rules.
 - [new_data_generation_NonNegationRule-D3.py] - The question needed to be derived by three rules, all of them are the non-negation rules.
 - [new_data_generation_NonNegationRule-animal-D3.py] - The question with animal entities needed to be derived by three rules includes the non-negation rules.
##### Depth=4
 - [new_data_generation_NegationRule-D4.py] - The question needed to be derived by four rules, part of them are the negation rules.
 - [new_data_generation_NegationRule-animal-D4.py] - The question with animal entities needed to be derived by four rules includes the negation rules.
 - [new_data_generation_NonNegationRule-D4.py] - The question needed to be derived by four rules, all of them are the non-negation rules.
 - [new_data_generation_NonNegationRule-animal-D4.py] - The question with animal entities needed to be derived by four rules includes the non-negation rules.
##### Depth=5
 - [new_data_generation_NegationRule-D5.py] - The question needed to be derived by five rules, part of them are the negation rules.
 - [new_data_generation_NegationRule-animal-D5.py] - The question with animal entities needed to be derived by five rules includes the negation rules.
 - [new_data_generation_NonNegationRule-D5.py] - The question needed to be derived by five rules, all of them are the non-negation rules.
 - [new_data_generation_NonNegationRule-animal-D5.py] - The question with animal entities needed to be derived by five rules includes the non-negation rules.
 
 [shuffle_data.py] - The generated data is shuffled by this scripts.

## Citation
```
@unpublished{
  title={PARARULE Plus: A Larger Deep Multi-Step Reasoning Dataset},
  author={Qiming Bao},
  year={2021}
}
```

# Other links
The PARARULE dataset is from that paper.
 [Transformers as Soft Reasoners over Language](https://arxiv.org/abs/2002.05867). 

The online demo for PARARULE.
https://rule-reasoning.apps.allenai.org/

PARARULE dataset
https://allenai.org/data/ruletaker

ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language
https://arxiv.org/pdf/2012.13048.pdf

PRover: Proof Generation for Interpretable Reasoning over Rules
https://arxiv.org/abs/2010.02830

Measuring Systematic Generalization in Neural Proof Generation with Transformers
https://arxiv.org/pdf/2009.14786.pdf

Investigating the Limitations of the Transformers with Simple Arithmetic Tasks
http://arxiv.org/abs/2102.13019v1
