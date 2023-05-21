import requests
# 进QQ群781055163，获取APIKEY
apikey = "0123456789ABCDEF"
api = f"http://fenserver1.e1.luyouxia.net:27725/?apikey={apikey}&an="
# 问答
while True:
    question = input("Your Question> ")
    apiback = requests.get(api+question)
    print("GPT-Fenserver> "+apiback.text)