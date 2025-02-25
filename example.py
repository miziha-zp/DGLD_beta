import os
import sys
sys.path.append('./src')

from dgld.utils.dataset import GraphNodeAnomalyDectionDataset
from dgld.models.CoLA import CoLA
from dgld.models.CoLA import get_parse
from dgld.utils.evaluation import split_auc

import dgl
import torch
import numpy as np

gnd_dataset = GraphNodeAnomalyDectionDataset("Cora", p = 15, k = 50)
g = gnd_dataset[0]
label = gnd_dataset.anomaly_label
model = CoLA(in_feats=g.ndata['feat'].shape[1])
model.fit(g, num_epoch=5, device=0)
result = model.predict(g, auc_test_rounds=2)
print(split_auc(label, result))
