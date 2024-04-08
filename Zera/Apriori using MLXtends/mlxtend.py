# -*- coding: utf-8 -*-
"""mlxtend.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TnKBzwdxX-9m-S-fd6mn_eOQqFOr344_

# **Apriori using Mlxtend**

Association rule mining, at a basic level, involves the use of machine learning models to analyze data for patterns, or co-occurrences, in a database. It identifies frequent if-then associations, which themselves are the association rules. An association rule has two parts: an antecedent (if) and a consequent (then)

mlxtend ( machine learning extensions) is a python library of useful tools for the day-to-day data science tasks.

1.   from mlxtend.frequent_patterns import

*   Apriori function to extract frequent itemsets for association rule mining
*   Support threshold can be mentioned to retrieve frequent itemset



2.   from mlxtend.frequent_patterns import association_rules
*   functionn to generate association rules from frequent itemsets
*   dataframe,metrics and minimum threshold needs to be mentioned
*   Metrics values are support, confidence, lift

**Code**
"""

pip install mlxtend

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
df

from mlxtend.frequent_patterns import apriori

apriori(df, min_support=0.6)

apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

frequent_itemsets[ (frequent_itemsets['length'] == 2) &
                   (frequent_itemsets['support'] >= 0.8) ]

frequent_itemsets[ frequent_itemsets['itemsets'] == {'Onion', 'Eggs'} ]

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
rules

rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
rules