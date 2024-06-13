from services.gpt_service import GPTService
from services.prompt_chain_service import ChainPromptsService

if __name__ == "__main__":
    prompt = """
    Напиши fizzbuzz с помощью паттерна Chain of Responsibility
    """
    with open(
        "/Users/silver_machine/Development/gpt_prompt_chainer/templates/write_python_code.txt"
    ) as f:
        response = ChainPromptsService(
            prompts_templates=f.read(),
            gpt_service=GPTService(),
        ).generate(
            initial_text=prompt,
        )
        print(response)
