from itertools import combinations
from collections import Counter

dfk = dfb.query("precentage_bid<100")

#Get tuple for companies that bid together
a_series = dfk.groupby('block_code')['company'].apply(list).apply(lambda r: list(combinations(r, 2))).dropna()
a_list = list(filter(None, a_series.tolist()))
flatten_list = [item for sublist in a_list for item in sublist]

#DataFrame with counts
x=Counter(flatten_list).keys()
y=Counter(flatten_list).values()
dfg = pd.DataFrame(x, columns=['comp1', 'comp2'])
dfg['count']=y

#create graph
H = nx.from_pandas_edgelist(dfg, 'comp1', 'comp2', edge_attr='count')
