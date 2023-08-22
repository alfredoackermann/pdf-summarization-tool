import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

def gpt3_completion(prompt, engine='text-davinci-003', temp=0.5, top_p=0.3, tokens=1000):

  prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
  try:
    response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    temperature=temp,
    top_p=top_p,
    max_tokens=tokens
    )
    return response.choices[0].text.strip()
  except Exception as oops:
    return 'GPT-3 error: %s' % oops