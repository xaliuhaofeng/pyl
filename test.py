import ollama

response = ollama.chat(model='codegemma', messages=[
  {
    'role': 'user',
    'content':'查一下当前python库的版本',
  },
])
print(response['message']['content'])