import requests

# 定义接口的URL
url = 'https://jsonplaceholder.typicode.com/posts/1'  # 这是一个示例URL，请根据你的需求修改

# 发送GET请求
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()
    print("接口响应数据：")
    print(data)
else:
    print(f"接口请求失败，状态码：{response.status_code}")



print('sssssssss')