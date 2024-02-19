import ollama
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

## Ollama 문제점
## 가장 큰 문제점은 내가 어떻게 사용해야 할지 모른다는 것
## 로컬에 받아서 실행해야 하는지, Ollama 웹 UI로 따로 실행해야 하는지 모르겠음
## Ollama를 실행한다고 쳐도 이걸 어떻게 기존 코드와 함께 사용할지 모르겠음