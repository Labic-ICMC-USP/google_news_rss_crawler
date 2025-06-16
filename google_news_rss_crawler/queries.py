def load_queries(txt_path):
    """
    Load search queries from a TXT file (one per line).
    """
    with open(txt_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]
