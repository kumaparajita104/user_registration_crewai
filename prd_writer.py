class PRDWriter:
    PRD_FILE = "prd_document.md"

    @staticmethod
    def write_section(title, content):
        """Appends a section to the PRD document."""
        with open(PRDWriter.PRD_FILE, "a", encoding="utf-8") as f:
            f.write(f"## {title}\n\n{content}\n\n---\n\n")

    @staticmethod
    def clear_document():
        """Clears the existing PRD document to start fresh."""
        with open(PRDWriter.PRD_FILE, "w", encoding="utf-8") as f:
            f.write("# Product Requirement Document (PRD)\n\n")
