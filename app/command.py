import os


def ping_host(host: str) -> str:
    """CWE-78: command injection via os.system."""
    # Intentionally vulnerable: user input concatenated into shell command
    return str(os.system("ping -c 1 " + host))
