import textwrap


def wrap_text_preserve_newlines(text, width=110):
    lines = text.split("\n")
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = "\n".join(wrapped_lines)
    return wrapped_text


def _prepare_meta(source_documents):
    sources = []
    for source in source_documents:
        meta = []
        id = None
        for key, value in source.metadata.items():
            if key in ("id", "another_type_of_id"):
                id = value
            else:
                meta.append(f"{key} - {value}\n")

        sources.append({"meta": meta, "chunk": str(source.page_content), "id": id})
    return sources


def process_llm_response(llm_response):
    return {
        "result": llm_response["result"],
        "sources": _prepare_meta(llm_response["source_documents"]),
    }
