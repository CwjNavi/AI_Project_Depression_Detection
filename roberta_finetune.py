from transformers import RobertaTokenizer, RobertaModel
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


class Roberta_base_classifier(nn.Module):
    def __init__(self):
        super().__init__()

        self.tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
        self.roberta = RobertaModel.from_pretrained('roberta-base')
        self.classifier = nn.Linear(512, 1)
        self.sigmoid = nn.Sigmoid()

        self.model = nn.Sequential(self.roberta, self.classifier)

    def forward(self, x):
        y = self.model(x)
        return y


if __name__ == "__main__":
    model = Roberta_base_classifier()

    input_sentence = "I am so fucking tired and sick of this life right now, everything seems hopeless"

    output = model(input)

    print(input_sentence)
    print(output)
