# The selected document is the [Wikipedia page for Ranni the Witch](https://en.wikipedia.org/wiki/Ranni_the_Witch)
**This article provides lore, character background, and game mechanics related to Ranni, including her role in the Elden Ring story, questline details, relationships, and major outcomes.**  
  
  
### AI‑Generated Q&A :

**1. What is the embedding dimensionality produced by our model?** 
<ins>Answer</ins>: The sentence-transformers/all-distilroberta-v1 model generates fixed‑length vectors of 768 dimensions, balancing representational power with computational efficiency.


**2. How does FAISS IndexFlatL2 search behavior affect retrieval?** 
<ins>Answer</ins>: IndexFlatL2 uses Euclidean distance (L2) to rank document embeddings. It returns the closest vectors in embedding space, ensuring that semantically similar chunks are retrieved efficiently, though without any quantization or compression.


**3. How do chunk_size and chunk_overlap influence retrieval quality?** 
<ins>Answer</ins>: A larger chunk_size outputs more context per chunk but risks diluting focus on specific facts. Introducing chunk_overlap ensures continuity and helps capture information that spans chunk edges, improving answers at the cost of occasional redundancy.


**4. What role does prompt design play in generation quality?** 
<ins>Answer</ins>: A well‑structured prompt (clearly labeling context and the question) guides the LLM to ground answers in retrieved text.


**5. How does the choice of top_k affect precision versus recall?**
<ins>Answer</ins>: A smaller top_k (5) focuses on the most relevant chunks, boosting precision but possibly missing peripheral details. Increasing top_k enhances recall by pulling in more context but may introduce noise that confuses the generator.  
  
   
  
### Experimentig with chunk_size and chunk_overlap :

• Moderate size (500) with (50) overlap:  
These parameters were the sweet spot to get the most factual details with minimal redundancy.  

• Small chunks with low overlap:  
Answers were precise for narrow questions but often missed nuanced information and often missed the entire point of the question.

• Large chunks with little to no overlap:  
Context was broad and also buried key sentences, leading to broad answers that sometimes were incorrect.

• Small chunks with high overlap:  
Answers ranged from lacking nuance and being inaccurate, to also being verbose and accurate.

• Very large chunks and chunk overlap:  
Surprisingly accurate and informative in most cases, narrow questions can return unexpected answers.
  
[See the prompts utilized and resulting answers](prompts.md)
  
### Quality of Responses :

The answers were generally coherent and context‑aware, accurately reflecting retrieved snippets; occasionally it was overly general if prompts lacked specificity.  
  
  
  
### Suggestions for Improvements :

Adapt chunk sizes based on sentence boundaries or semantics.

Use a template library to experiment with phrasing and max_length settings.
