
### The selected document is the Wikipedia page for Ranni the Witch 
*https://en.wikipedia.org/wiki/Ranni_the_Witch*
**This article provides lore, character background, and game mechanics related to Ranni, including her role in the Elden Ring story, questline details, relationships, and major outcomes.**




##### AI‑Generated Q&A :

**1. What is the embedding dimensionality produced by our model?** 
<ins>Answer</ins>: The sentence-transformers/all-distilroberta-v1 model generates fixed‑length vectors of 768 dimensions, balancing representational power with computational efficiency.


**2. How does FAISS IndexFlatL2 search behavior affect retrieval?** 
<ins>Answer</ins>: IndexFlatL2 uses Euclidean distance (L2) to rank document embeddings. It returns the closest vectors in embedding space, ensuring that semantically similar chunks are retrieved efficiently, though without any quantization or compression.


**3. How do chunk_size and chunk_overlap influence retrieval quality?** 
<ins>Answer</ins>: A larger chunk_size outputs more context per chunk but risks diluting focus on specific facts. Introducing chunk_overlap ensures continuity helps capture information that spans chunk edges, improving awnsers at the cost of occational redundancy.


**4. What role does prompt design play in generation quality?** 
<ins>Answer</ins>: A well‑structured prompt (clearly labeling context and the question) guides the LLM to ground answers in retrieved text.


**5. How does the choice of top_k affect precision versus recall?**
<ins>Answer</ins>: A smaller top_k (5) focuses on the most relevant chunks, boosting precision but possibly missing peripheral details. Increasing top_k enhances recall by pulling in more context but may introduce noise that confuses the generator.

 

##### Experimentig with chunk_size and chunk_overlap :

Small chunks (250) with low overlap (25): Awnsers were precise for narrow questions but often missed nuanced connections.

Large chunks (800) with no overlap (0): Context was broad but sometimes buried key sentences, leading to less targeted retrieval.

Moderate size (500) with 50 or 75 overlap: Was the sweet spot to get the most factual details, with minimal redundancy.



##### Quality of Responses :

The answers were generally coherent and context‑aware, accurately reflecting retrieved snippets, occasionally it was overly general if prompts lacked specificity.



##### Suggestions for Improvements :

Adapt chunk sizes based on sentence boundaries or semantics.

Use a template engine to experiment with instruction phrasing and max_length settings.
