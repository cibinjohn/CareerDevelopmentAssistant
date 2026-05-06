## RAG Retrieval Evaluation

Evaluates ChromaDB retrieval against ground-truth contexts from `eval_dataset_v3.json`.

### Metrics Computed

| Metric | Description |
|--------|------------|
| **Hit@K** | Whether at least one ground-truth context appears in the top-K retrieved results |
| **Precision@K** | Proportion of retrieved chunks in top-K that are relevant |
| **Recall@K** | Proportion of total ground-truth contexts successfully retrieved |
| **MRR (Mean Reciprocal Rank)** | Rank quality of the first relevant retrieved chunk |

## Naive RAG Evaluation

### Metrics by Match Type (Strict vs Fallback)

| Match Type | Count | Hit@K (%) | Precision@K (%) | Recall@K (%) | MRR   |
|------------|-------|-----------|-----------------|--------------|-------|
| Fallback   | 184   | 87.5      | 46.9            | 63.4         | 0.8043|
| Strict     | 160   | 66.9      | 30.2            | 60.6         | 0.5958|