# PARARULE Plus
The new generated dataset for PARARULE. It is generated based on the closed-world assumption.
PARARULE Plus is a deep multi-step reasoning dataset over natural language. It can be seen as an improvement on the dataset of PARARULE [(Peter Clark et al., 2020)](https://www.ijcai.org/proceedings/2020/0537.pdf). The motivation is to generate deeper PARARULE training samples. We add more training samples for the case where the depth is greater than or equal to two to explore whether Transformer has reasoning ability. PARARULE Plus is a combination of two types of entities, `animals` and `people`, and corresponding relationships and attributes. From the depth of 2 to the depth of 5, we have around 100,000 samples in the depth of each layer, and there are nearly 400,000 samples in total.

We published the PARARULE Plus dataset to the paper [Multi-Step Deductive Reasoning Over Natural Language: An Empirical Study on Out-of-Distribution Generalisation](https://www.cs.ox.ac.uk/isg/conferences/tmp-proceedings/NeSy2022/paper15.pdf). The code and experiment in this paper can be found in that [GitHub link](https://github.com/Strong-AI-Lab/Multi-Step-Deductive-Reasoning-Over-Natural-Language). [PARARULE-Plus](https://github.com/Strong-AI-Lab/PARARULE-Plus) has also been collected by [LogiTorch](https://www.logitorch.ai/) which is a PyTorch-based library for logical reasoning on natural language.

You can use `Huggingdace/Datasets` to load the PARARULE-Plus dataset from this [link](https://huggingface.co/datasets/qbao775/PARARULE-Plus). We upload `PARARULE-Plus`, `PARARULE-Plus-Depth-2`, `PARARULE-Plus-Depth-3`, `PARARULE-Plus-Depth-4`, and `PARARULE-Plus-Depth-5` to the `Huggingface/Datasets`. `PARARULE-Plus` includes the datasets from all four different depths and the other datasets only include the dataset corresponding to each depth. For example, `PARARULE-Plus-Depth-2` only includes the datasets with 2 reasoning depths.  Here is an example to load the PARARULE-Plus with all reasoning depths.
### Create a virtual environment
```
conda create -n pararule-plus python=3.8
conda activate pararule-plus
git clone https://github.com/Strong-AI-Lab/PARARULE-Plus.git
cd PARARULE-Plus
```

### 🤗 Install the datasets and other requirements
```
pip install -r requirements
```

### 🤗 Load the PARARULE-Plus dataset
```
from datasets import load_dataset
dataset = load_dataset("qbao775/PARARULE-Plus")  ## You can use "qbao775/PARARULE-Plus-Depth-2", "qbao775/PARARULE-Plus-Depth-3", "qbao775/PARARULE-Plus-Depth-4", and "qbao775/PARARULE-Plus-Depth-5" to load datasets from different reasoning depths.
```

### 🤗 An example script to load PARARULE-Plus and fine-tune BERT
```
python run_glue_no_trainer.py \
  --model_name_or_path bert-base-cased \
  --task_name qbao775/PARARULE-Plus\
  --max_length 256 \
  --per_device_train_batch_size 32 \
  --learning_rate 2e-5 \
  --num_train_epochs 3 \
  --output_dir /tmp/PARARULE-Plus/
```

## PARARULE-Plus Dataset Description
### Animals
`Animal Entities` ['the bald eagle', 'the tiger', 'the bear', 'the lion', 'the wolf', 'the crocodile', 'the dinosaur', 'the snake', 'the leopard']

`Animal Entities-2` ['the cat', 'the dog', 'the mouse', 'the rabbit', 'the squirrel']

`Animal Relationship` ['is', 'likes', 'chases', 'needs', 'visits', 'attacks', 'sees']

`Animal Attributes-1` ['kind', 'quiet', 'round', 'nice', 'smart', 'clever']

`Animal Attributes-2` ['dull', 'rough', 'lazy', 'slow', 'sleepy', 'boring', 'tired', 'reckless']

`Animal Attributes-3` ['furry', 'small', 'cute', 'lovely', 'beautiful', 'funny']

`Animal Attributes-4` = ['big', 'strong', 'awful', 'fierce', 'heavy', 'horrible', 'powerful', 'angry']

|The Num of Animal Entities|The Num of Animal Relationships|The Num of Animal Attributes|
|:----:|:----:|:----:|
|14|7|28|

### People
`People Entities` ['Anne', 'Alan', 'Bob', 'Charlie', 'Dave', 'Erin', 'Harry', 'Gary', 'Fiona']

`People Relationship` ['is']

`People Attributes-1` ['big', 'strong', 'high', 'huge']

`People Attributes-2` ['short', 'thin', 'small', 'little', 'tiny']

`People Attributes-3` ['wealthy', 'smart', 'nice', 'quiet', 'kind', 'clever']

`People Attributes-4` = ['poor', 'dull', 'rough', 'bad', 'sad']


|The Num of People Entities|The Num of People Relationships|The Num of People Attributes|
|:----:|:----:|:----:|
|9|1|20|


## PARARULE Plus Data distribution
For each depth dataset, we have around 90,000 datasets to be used, much larger than the same depth in PARARULE.
### PARARULE Plus

|Dataset|Train|Dev|Test|
|:---|:----:|:----:|:----:|
|Depth=2|89952|16204|2708|
|Depth=3|90016|16154|2694|
|Depth=4|90010|16150|2704|
|Depth=5|90022|16150|2692|

<!--<img src="./image/data-distribution.PNG" width="300" />-->
### PARARULE

|Dataset|Train|Dev|Test|
|:---|:----:|:----:|:----:|
|Depth=0|290435|41559|83119|
|Depth=1|157440|22276|45067|
|Depth=2|75131|10833|21496|
|Depth=3|48010|6959|13741|
|Depth=4|9443|1334|2691|
|Depth=5|7325|1038|2086|

<!--<div align=center><img src="./image/pararule_depth_distribution.png" width="300" /></div>-->

## Examples
### An example with the non-negation rules for Depth=2 means the question needed to be derived by two rules.
<img src="./image/NonNegationRule-D2-1-2.PNG" width="550" />
The `QCat=0` means the question is generated from non-negation rules and the label is `true`. If the `QCat=0_0`, it means the question is generated from non-negation rules and the label is `false`.

### An example with the negation rules for Depth=2 means the question needed to be derived by two rules.
<img src="./image/NegationRule-D2-1.PNG" width="450" />

### An example with the non-negation rules for Depth=3 means the question needed to be derived by three rules.
<img src="./image/NonNegationRule-Animal-D3-1-2.PNG" width="600" />

### An example with the negation rules for Depth=3 means the question needed to be derived by three rules.
<img src="./image/NegationRule-Animal-D3-1.PNG" width="450" />

### An example with the non-negation rules for Depth=4 means the question needed to be derived by four rules.
<img src="./image/NonNegationRule-D4-1.PNG" width="450" />

### An example with the negation rules for Depth=4 means the question needed to be derived by four rules.
<img src="./image/NegationRule-D4-1-2.PNG" width="400" />

### An example with the non-negation rules for Depth=5 means the question needed to be derived by five rules.
<img src="./image/NonNegationRule-Animal-D5-1.PNG" width="600" />

### An example with the negation rules for Depth=5 means the question needed to be derived by five rules.
<img src="./image/NegationRule-Animal-D5-1.PNG" width="600" />

#### Depth=2
The `QCat=0_not_notTrue` means the question is generated from one negation rule and another negation rule `and` a positive rule and the label is `true`. 
The `QCat=0_0_not_notTrue` means the question is generated from one negation rule and another negation rule `and` a positive rule and the label is `false`. 
The `QCat=0_true_trueNot` means the question is generated from one positive rule and another positive rule `and` a negation rule and the label is `true`. 
The `QCat=0_0_true_trueNot` means the question is generated from one positive rule and another positive rule `and` a negation rule and the label is `false`. 

#### Depth=3
The `QCat=0_not_notTrue_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and a positive rule and the label is `true`. 
The `QCat=0_0_not_notTrue_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and a positive rule and the label is `false`. 
The `QCat=0_true_trueNot_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and and a positive rule and the label is `true`. 
The `QCat=0_0_true_trueNot_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and a positive rule and the label is `false`. 

#### Depth=4
The `QCat=0_not_notTrue_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and two more positive rules and the label is `true`. 
The `QCat=0_0_not_notTrue_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and two more positive rules and the label is `false`. 
The `QCat=0_true_trueNot_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and two more positive rules and the label is `true`. 
The `QCat=0_0_true_trueNot_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and two more positive rules and the label is `false`. 

#### Depth=5
The `QCat=0_not_notTrue_true_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and three more positive rules and the label is `true`. 
The `QCat=0_0_not_notTrue_true_true_true` means the question is generated from one negation rule and another negation rule `and` a positive rule and three more positive rules and the label is `false`. 
The `QCat=0_true_trueNot_true_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and three more positive rules and the label is `true`. 
The `QCat=0_0_true_trueNot_true_true_true` means the question is generated from one positive rule and another positive rule `and` a negation rule and three more positive rules and the label is `false`. 

## Detail for the data generation scripts
### Scripts
#### Depth=2
 - `new_data_generation_NegationRule-D2.py` - The question needed to be derived by two rules, part of them are the negation rules.
 - `new_data_generation_NegationRule-animal-D2.py` - The question with animal entities needed to be derived by two rules includes the negation rules.
 - `new_data_generation_NonNegationRule-D2.py` - The question needed to be derived by two rules, all of them are the non-negation rules.
 - `new_data_generation_NonNegationRule-animal-D2.py` - The question with animal entities needed to be derived by two rules includes the non-negation rules.
#### Depth=3
 - `new_data_generation_NegationRule-D3.py` - The question needed to be derived by three rules, part of them are the negation rules.
 - `new_data_generation_NegationRule-animal-D3.py` - The question with animal entities needed to be derived by three rules includes the negation rules.
 - `new_data_generation_NonNegationRule-D3.py` - The question needed to be derived by three rules, all of them are the non-negation rules.
 - `new_data_generation_NonNegationRule-animal-D3.py` - The question with animal entities needed to be derived by three rules includes the non-negation rules.
#### Depth=4
 - `new_data_generation_NegationRule-D4.py` - The question needed to be derived by four rules, part of them are the negation rules.
 - `new_data_generation_NegationRule-animal-D4.py` - The question with animal entities needed to be derived by four rules includes the negation rules.
 - `new_data_generation_NonNegationRule-D4.py` - The question needed to be derived by four rules, all of them are the non-negation rules.
 - `new_data_generation_NonNegationRule-animal-D4.py` - The question with animal entities needed to be derived by four rules includes the non-negation rules.
#### Depth=5
 - `new_data_generation_NegationRule-D5.py` - The question needed to be derived by five rules, part of them are the negation rules.
 - `new_data_generation_NegationRule-animal-D5.py` - The question with animal entities needed to be derived by five rules includes the negation rules.
 - `new_data_generation_NonNegationRule-D5.py` - The question needed to be derived by five rules, all of them are the non-negation rules.
 - `new_data_generation_NonNegationRule-animal-D5.py` - The question with animal entities needed to be derived by five rules includes the non-negation rules.
 
 `shuffle_data.py` - The generated data is shuffled by this scripts.

## Citation
```
@inproceedings{bao2022multi,
  title={Multi-Step Deductive Reasoning Over Natural Language: An Empirical Study on Out-of-Distribution Generalisation},
  author={Qiming Bao and Alex Yuxuan Peng and Tim Hartill and Neset Tan and Zhenyun Deng and Michael Witbrock and Jiamou Liu},
  year={2022},
  publisher={The 2nd International Joint Conference on Learning and Reasoning and 16th International Workshop on Neural-Symbolic Learning and Reasoning (IJCLR-NeSy 2022)}
}
```

## Other links
The PARARULE dataset is from that paper.
 [Transformers as Soft Reasoners over Language](https://arxiv.org/abs/2002.05867). 

The online demo for PARARULE.
https://rule-reasoning.apps.allenai.org/

PARARULE dataset
https://allenai.org/data/ruletaker

Explaining Answers with Entailment Trees
https://arxiv.org/pdf/2104.08661.pdf

ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language
https://arxiv.org/pdf/2012.13048.pdf

PRover: Proof Generation for Interpretable Reasoning over Rules
https://arxiv.org/abs/2010.02830

Neural Unification for Logic Reasoning over Natural Language
https://www.researchgate.net/profile/Gabriele-Picco-2/publication/354653211_Neural_Unif[…]-Unification-for-Logic-Reasoning-over-Natural-Language.pdf

Measuring Systematic Generalization in Neural Proof Generation with Transformers
https://arxiv.org/pdf/2009.14786.pdf

Investigating the Limitations of the Transformers with Simple Arithmetic Tasks
http://arxiv.org/abs/2102.13019v1

NATURALPROOFS: Mathematical Theorem Proving in Natural Language
https://arxiv.org/pdf/2104.01112.pdf

Graph-to-Tree Learning for Solving Math Word Problems
https://www.aclweb.org/anthology/2020.acl-main.362.pdf

Natural Language Premise Selection: Finding Supporting Statements for Mathematical Text
https://arxiv.org/pdf/2004.14959.pdf

Learning To Prove From Synthetic Theorems
https://arxiv.org/pdf/2006.11259.pdf

Are Pretrained Language Models Symbolic Reasoners Over Knowledge?
https://arxiv.org/pdf/2006.10413.pdf

Facts as Experts: Adaptable and Interpretable Neural Memory over Symbolic Knowledge
https://arxiv.org/pdf/2007.00849.pdf

Compressive Transformers for Long-Range Sequence Modelling
https://arxiv.org/abs/1911.05507

HOTPOTQA: A Dataset for Diverse, Explainable Multi-hop Question Answering
https://www.aclweb.org/anthology/D18-1259.pdf

Applying the Closed World Assumption to SUMO-based FOL Ontologies for Effective Commonsense Reasoning
http://ecai2020.eu/papers/1076_paper.pdf

Teaching Pre-Trained Models to Systematically Reason Over Implicit Knowledge
https://arxiv.org/pdf/2006.06609.pdf
