"""
CAOS Bootstrap Wrapper
System-owned entrypoint enforcing Context Journal
before server startup.
"""

from context.context_journal import ContextJournal
from context.loaders import load_kernel_context, load_boot_context

def bootstrap():
    journal = ContextJournal()
    journal.load_kernel(load_kernel_context())
    journal.load_boot(load_boot_context())
    if not journal.validate():
        raise RuntimeError("Context Journal validation failed")
    return journal

if __name__ == "__main__":
    journal = bootstrap()
    print("CAOS BOOTSTRAP OK")
    print("Context hash:", journal.hash())

    # Import AFTER context validation
    from framework_adapters.dev_server import app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
