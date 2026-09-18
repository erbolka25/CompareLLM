from llm_clients.openai_client import OpenAIClient


def main():
    client = OpenAIClient()
    result = client.generate("What is RAG in simple terms?")

    print(f"Model: {result.model}")
    print(f"Latency: {result.latency_ms:.0f} ms")
    print(f"Input tokens: {result.input_tokens}")
    print(f"Output tokens: {result.output_tokens}")
    print()
    print("Response:")
    print(result.text)


if __name__ == "__main__":
    main()
