This is the depression detection project for SUTD 50.021 Artificial Intelligence in February-May 2025
The repository contains the notebook containing the training of our models for the task of classifying a text into one of 3 classes: not depression, moderate, severe.
We adapted this from the DepSign-LT-EDI@ACL-2022 shared task and compared our model against their best performing models.

Our contribution is a Roberta-CNN model that uses convolutional layers on top of the Roberta embeddings to make a prediction.

This is our results
Test Accuracy: 0.6579
Test F-1 score: 0.5139

While we did not manage to beat the best performing models in the shared task, we contributed by introducing this new architecture and making some improvements over fine-tuning Roberta.


Citations

@InProceedings{10.1007/978-3-031-16364-7_11,
author= { Kayalvizhi, Sampath
and Thenmozhi, Durairaj},
editor={Kalinathan, Lekshmi
and R., Priyadharsini
and Kanmani, Madheswari
and S., Manisha},
title={Data Set Creation and Empirical Analysis for Detecting Signs of Depression from Social Media Postings},
booktitle={Computational Intelligence in Data Science},
year={2022},
publisher={Springer International Publishing},
address={Cham},
pages={136--151},
isbn={978-3-031-16364-7}
}

@inproceedings{s-etal-2022-findings,
    title = {Findings of the Shared Task on Detecting Signs of Depression from Social Media},
    author = {S, Kayalvizhi  and
      Durairaj, Thenmozhi  and
      Chakravarthi, Bharathi Raja  and
      C, Jerin Mahibha},
    booktitle = {Proceedings of the Second Workshop on Language Technology for Equality, Diversity and Inclusion},
    month = {May},
    year = {2022},
    address = {Dublin, Ireland},
    publisher = {{Association for Computational Linguistics}},
    url = {https://aclanthology.org/2022.ltedi-1.51},
    doi = {10.18653/v1/2022.ltedi-1.51},
    pages = {331--338}
    
}
