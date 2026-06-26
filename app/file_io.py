def read_file(path: str) -> str:
    """CWE-22: path traversal via concatenated base path."""
    # Intentionally vulnerable
    with open("/var/data/" + path, "r", encoding="utf-8") as handle:
        return handle.read()
