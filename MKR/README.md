# mkr-recommendation
MKR is a Multi-task learning approach for Knowledge graph enhanced Recommendation. MKR consists of two parts: the recommender system (RS) module and the knowledge graph embedding (KGE) module. The two modules are bridged by cross&compress units, which can automatically learn high-order interactions of item and entity features and transfer knowledge between the two tasks.
![framework](https://github.com/demomagic/mkr-recommendation/blob/master/img/framework.png)

# Usage
For movie:

          python preprocess.py -d movie
          python main.py -dataset movie
          python predict_test.py -d movie  # Testing the .pd model

For book:

          python preprocess.py -d book
          python main.py -dataset book
          python predict_test.py -d book  # Testing the .pd model

For music:

          python preprocess.py -d music
          python main.py -dataset music
          python predict_test.py -d music  # Testing the .pd model

# File structure
* model/

  * movie/, book/, music/
    
    * restore/: model save recovery save/restore method,  use it to restore model weights
    
    * result/: save the .pd model, deploy model using tensorflow serving
    
    * vocab/: save the embedding, in order to transfer weight,  use it for iterative training if new users or new movie/music/book join

* data/
  * book/
    * BX-Book-Ratings.csv: raw rating file of Book-Crossing dataset
    * item_index2entity_id.txt: the mapping from item indices in the raw rating file to entity IDs in the KG
    * kg.txt: knowledge graph file
  * movie/
    * item_index2entity_id.txt: the mapping from item indices in the raw rating file to entity IDs in the KG
    * kg.txt: knowledge graph file
    * ratrings.dat: raw rating file of MovieLens-1M
  * music/
    * item_index2entity_id.txt: the mapping from item indices in the raw rating file to entity IDs in the KG
    * kg.txt: knowledge graph file
    * user_artists.dat: raw rating file of Last.FM

# Reference
[hwwang55/MKR](https://github.com/hwwang55/MKR)

[Multi-Task Feature Learning for Knowledge Graph Enhanced Recommendation. In Proceedings of The 2019 Web Conference (WWW 2019)](https://arxiv.org/abs/1901.08907)
