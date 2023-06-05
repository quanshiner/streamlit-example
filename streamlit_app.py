import streamlit as st
import openai

# 设置OpenAI API凭证
openai.api_key = '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'

# 定义应用程序逻辑
def main():
    # 设置页面标题
    st.title('AI牧民的ChatGPT')

    # 显示文本输入框和提示信息
    input_text = st.text_area('我是你的Al助手，请在这里提问')



    # 处理按钮点击事件
    if st.button("发送"):
        # 创建OpenAI API调用
        with st.spinner("正在生成回答..."):
            # 调用OpenAI API进行聊天
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=input_text,
                max_tokens=500,
                temperature=0.0,
                n=1,
                stop=None,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )

        # 从API的响应中提取模型生成的回答
        if response.choices:
            answer = response.choices[0].text.strip()
            st.write("Al助手回答：")
            st.write(answer)
        else:
            st.write("未能获取到回答，请稍后再试。")

# 运行应用程序
if __name__ == '__main__':
    main()
