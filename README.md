# ChromaDB Learning Project

A comprehensive hands-on guide to learning ChromaDB, a powerful vector database for AI applications. This project walks through all essential ChromaDB concepts from basic setup to advanced OpenAI integration.

## What is ChromaDB?

ChromaDB is a smart vector database that understands the *meaning* and *context* behind text, not just exact word matches. It's the technology powering many modern AI applications including:
- Semantic search engines
- RAG (Retrieval-Augmented Generation) systems
- Document Q&A systems
- Recommendation engines

## Project Structure

```
ChromaDb/
├── step2_collections.py              # Creating and managing collections
├── step3_crud_operations.py          # CRUD operations on documents
├── step4_persistent_database.py      # Persistent storage
├── step4_verify_persistence.py       # Verification script
├── step4_persistent_demo.py          # Smart persistence demo
├── step5_collection_management.py    # CRUD on collections
├── step6_openai_embeddings.py        # OpenAI embeddings integration
├── chromadb-demo/
│   └── chromadb-guide.md            # Complete written guide
├── venv/                            # Virtual environment
└── chroma_db/                       # Persistent database storage (gitignored)
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git and GitHub account
- OpenAI API key (for Step 6 only)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd ChromaDb
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac/Linux/Git Bash:**
```bash
python -m venv venv
source venv/bin/activate  # or venv/Scripts/activate on Windows Git Bash
```

### 3. Install Dependencies

```bash
# Core ChromaDB
pip install chromadb

# For Step 6 (OpenAI integration)
pip install openai tiktoken
```

## Learning Path

### Step 1: Installation ✓
Set up Python virtual environment and install ChromaDB.

**Completed in setup above.**

### Step 2: Creating Collections

Learn how to initialize ChromaDB and create your first collection.

```bash
python step2_collections.py
```

**What you'll learn:**
- Initialize ChromaDB client
- Create collections (like database tables)
- Basic collection operations

### Step 3: CRUD Operations on Data

Master creating, reading, updating, and deleting documents.

```bash
python step3_crud_operations.py
```

**What you'll learn:**
- **CREATE**: Add documents with `add()`
- **READ**: Query documents with `query()`
- **UPDATE**: Modify documents with `upsert()`
- **DELETE**: Remove documents with `delete()`
- Understanding semantic search
- Working with metadata

### Step 4: Persistent Database

Learn how to save data permanently to disk.

```bash
python step4_persistent_database.py
```

**What you'll learn:**
- Difference between in-memory and persistent storage
- Using `PersistentClient`
- Data persistence between sessions

**Verify persistence:**
```bash
python step4_verify_persistence.py
```

**Smart demo (handles existing data):**
```bash
python step4_persistent_demo.py
```

### Step 5: Collection Management

Learn CRUD operations on collections themselves.

```bash
python step5_collection_management.py
```

**What you'll learn:**
- List all collections
- Rename collections
- Add collection metadata
- Delete collections (with warnings!)

### Step 6: OpenAI Embeddings (Advanced)

Integrate OpenAI's powerful embedding models.

```bash
# Set your OpenAI API key first
export OPENAI_API_KEY='your-api-key-here'  # Mac/Linux/Git Bash
# OR
set OPENAI_API_KEY=your-api-key-here       # Windows Command Prompt

python step6_openai_embeddings.py
```

**What you'll learn:**
- Count tokens with `tiktoken`
- Use OpenAI's `text-embedding-3-small` model
- Create custom embedding functions
- Compare OpenAI vs default embeddings

**Note:** This step requires an OpenAI API key and will incur small API costs (typically < $0.01 for the demo).

## Key Concepts

### Embeddings
Numerical representations of text that capture semantic meaning. Similar meanings = similar vectors.

### Collections
Containers for related documents, like tables in a traditional database.

### Metadata
Additional structured information about documents (e.g., `{"category": "travel", "date": "2024-10-18"}`).

### Semantic Search
Finding documents by meaning rather than exact keyword matches. "international flight policy" will find relevant documents even if they don't contain those exact words.

### Distance/Similarity
Lower distance = more similar documents. ChromaDB uses this to rank search results.

## Common Use Cases

- **Document Search**: Search through company policies, manuals, or knowledge bases
- **Q&A Systems**: Build chatbots that answer questions based on your documents
- **Recommendation Systems**: Find similar products, articles, or content
- **RAG Applications**: Enhance LLM responses with relevant context from your data

## Development Workflow

This project uses Git branching for development:

```bash
# Work on the develop_safa branch
git checkout develop_safa

# Make changes and commit
git add .
git commit -m "Description of changes"
git push origin develop_safa

# Merge to main when ready
git checkout main
git merge develop_safa
git push origin main
```

## Troubleshooting

### Virtual Environment Not Activating
- **Windows**: You may need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell
- **Git Bash**: Use `source venv/Scripts/activate` (not `venv/bin/activate`)

### OpenAI API Key Not Found
- Make sure to export/set the environment variable in the same terminal session where you run the script
- Alternatively, set it directly in the script (not recommended for production)

### Unicode Errors in Git Bash
The scripts have been updated to use ASCII-safe characters. If you still encounter issues, try running in PowerShell or Command Prompt instead.

### ChromaDB Import Errors
Make sure your virtual environment is activated before running scripts:
```bash
source venv/Scripts/activate  # or venv\Scripts\activate.bat on Windows
```

## Resources

- **ChromaDB Documentation**: https://docs.trychroma.com/
- **OpenAI Embeddings**: https://platform.openai.com/docs/guides/embeddings
- **Complete Guide**: See `chromadb-demo/chromadb-guide.md` for detailed written explanations

## Project Stats

- **6 Complete Steps**: From setup to advanced OpenAI integration
- **7 Python Scripts**: Hands-on examples for each concept
- **Real-World Example**: Travel policy management system
- **100% Hands-On**: Every concept demonstrated with working code

## What's Next?

After completing this guide, you can:

1. **Build Your Own Project**: Apply ChromaDB to your own data
2. **Integrate with LLMs**: Build a RAG (Retrieval-Augmented Generation) system
3. **Explore Advanced Features**: Multi-modal embeddings, custom distance functions
4. **Scale Up**: Use ChromaDB Server for production deployments

## License

This is a learning project. Feel free to use and modify for your own learning purposes.

## Acknowledgments

- ChromaDB team for creating an excellent vector database
- OpenAI for powerful embedding models
- The AI/ML community for advancing semantic search technology

---

**Happy Learning!** 🚀

If you found this helpful, consider starring the repo or sharing it with others learning about vector databases!

