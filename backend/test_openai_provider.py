from app.services.openai_provider import OpenAIProvider


provider = OpenAIProvider()

print("Prompt loaded successfully.")
print()
print(provider.system_prompt[:300])