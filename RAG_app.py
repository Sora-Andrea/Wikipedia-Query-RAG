import logging
from transformers import logging as hf_logging
import warnings

# 3.1 Suppress Noisy Logs
logging.getLogger("langchain.text_splitter").setLevel(logging.ERROR)
hf_logging.set_verbosity_error()
warnings.filterwarnings("ignore")

# 3.2 Parameters
chunk_size = 500
chunk_overlap = 50
model_name = "sentence-transformers/all-distilroberta-v1"
top_k = 5

# 3.3 Read the Pre-scraped Document
with open("Selected_Document.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 3.4 Split into Appropriately-sized Chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)
chunks = text_splitter.split_text(text)

# 3.5 Embed & Build FAISS Index
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

embedder = SentenceTransformer(model_name)
embeddings = embedder.encode(chunks, show_progress_bar=True)
embeddings = np.array(embeddings, dtype=np.float32)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# 3.6 Load the Generator Pipeline
from transformers import pipeline
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    device=-1
)

# 3.7 Retrieval & Answering Functions
def retrieve_chunks(question, k=top_k):
    # Encode the question
    q_emb = embedder.encode([question])
    q_emb = np.array(q_emb, dtype=np.float32)
    # Search the FAISS index
    D, I = index.search(q_emb, k)
    # Return top-k chunks
    return [chunks[i] for i in I[0]]


def answer_question(question):
    # Retrieve relevant chunks
    relevant_chunks = retrieve_chunks(question)
    # Build prompt with context
    context = "\n\n".join(relevant_chunks)
    prompt = (
        f"Answer the question based on the following context:\n\n"
        f"{context}\n\nQuestion: {question}\nAnswer:"
    )
    # Generate answer
    result = generator(prompt, max_length=200)
    return result[0]["generated_text"]

# 3.8 Interactive Loop
if __name__ == "__main__":
    print("Enter 'exit' or 'quit' to end.")
    while True:
        question = input("Your question: ")
        if question.lower() in ("exit", "quit"):
            break
        print("Answer:", answer_question(question))
