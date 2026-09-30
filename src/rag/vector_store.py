from typing import List, Dict, Any
from src.rag.document_loader import document_loader, DocumentChunk
from config.logging_config import logger

class VectorKnowledgeStore:
    """In-memory and Chroma vector store for RAG document retrieval."""
    def __init__(self):
        self._chunks: List[DocumentChunk] = []
        self._initialized = False

    def initialize_knowledge_base(self):
        """Index SharePoint SOPs into vector store."""
        if not self._initialized:
            self._chunks = document_loader.fetch_and_chunk_sharepoint_docs(query="SOP Cancellation Policy")
            self._initialized = True
            logger.info(f"VectorKnowledgeStore initialized with {len(self._chunks)} documents.")

    def search_knowledge(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        self.initialize_knowledge_base()
        query_words = set(query.lower().split())
        
        # Simple similarity scoring algorithm (keyword/TF-IDF based scoring fallback)
        scored_results = []
        for chunk in self._chunks:
            chunk_words = set(chunk.text.lower().split())
            overlap = len(query_words.intersection(chunk_words))
            score = overlap / (len(query_words) + 1)
            scored_results.append((score, chunk))

        scored_results.sort(key=lambda x: x[0], reverse=True)
        top_matches = scored_results[:top_k]

        return [
            {
                "doc_title": chunk.title,
                "content": chunk.text,
                "relevance_score": score,
                "metadata": chunk.metadata
            }
            for score, chunk in top_matches
        ]

knowledge_store = VectorKnowledgeStore()
