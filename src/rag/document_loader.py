from typing import List, Dict, Any
from src.integrations.ms_graph_client import ms_graph_client
from config.logging_config import logger

class DocumentChunk:
    def __init__(self, doc_id: str, title: str, text: str, metadata: Dict[str, Any]):
        self.doc_id = doc_id
        self.title = title
        self.text = text
        self.metadata = metadata

class DocumentLoader:
    """Loader and chunker for company knowledge documents (SharePoint, Policies, SOPs)."""
    
    def fetch_and_chunk_sharepoint_docs(self, query: str = "SOP Policy", chunk_size: int = 250) -> List[DocumentChunk]:
        docs = ms_graph_client.search_sharepoint_documents(query)
        chunks: List[DocumentChunk] = []

        for doc in docs:
            content = doc["content"]
            # Simple sentence/character chunking strategy
            words = content.split(" ")
            for i in range(0, len(words), chunk_size):
                chunk_text = " ".join(words[i:i + chunk_size])
                chunk = DocumentChunk(
                    doc_id=f"{doc['doc_id']}_chunk_{i // chunk_size}",
                    title=doc["title"],
                    text=chunk_text,
                    metadata={
                        "doc_id": doc["doc_id"],
                        "category": doc.get("category", "General"),
                        "url": doc.get("url", "")
                    }
                )
                chunks.append(chunk)

        logger.info(f"Loaded and created {len(chunks)} chunks from SharePoint.")
        return chunks

document_loader = DocumentLoader()
