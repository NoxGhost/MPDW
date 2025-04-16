# MPDW - Video Dialog Project

In this project, we aim to build a powerful pipeline for retrieving moments in videos using transformer-based architectures. Our goal is to enable efficient and accurate video moment searches, support natural language queries, and explore cross-modal reasoning.

## Project Overview

This project is divided into three phases:

1. **Phase 1: Embedding Spaces**  
   We create an index of video moments using Dual Encoders and OpenSearch. This phase involves indexing video metadata, implementing semantic search, and exploring embedding spaces.
   
2. **Phase 2: Vision and Language Models**  
   By integrating multimodal models like CLIP and LLaMA, we enable cross-modal queries and generate natural language answers.

3. **Phase 3: Advanced Topics**  
   We explore custom topics, such as enhanced retrieval methods or new applications, based on group-specific ideas.

### Methods and Key Features
- **Video Structure**: We organize content into moments, shots, and keyframes to support granular retrieval.
- **Search Functionalities**:
  - Keyword-based and semantic search.
  - Filtering by attributes (e.g., actions, entities, duration).
- **Embedding Spaces**:
  - Use dual encoders to create semantic embeddings.
  - Implement k-NN search for similarity-based retrieval.
- **Transformer-based Models**: We leverage self-attention mechanisms and contextual embeddings for advanced video understanding.

## Resources
- **ActivityNet Captions Dataset**: [Stanford](https://cs.stanford.edu/people/ranjaykrishna/densevid/), [Hugging Face](https://huggingface.co/datasets/HuggingFaceM4/ActivitiyNet_Captions)

