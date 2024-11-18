# 大模型数据助手

💡 **项目简介**

一个轻量级、支持全链路且易于二次开发的大模型应用项目

基于 Dify 、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

作为轻量级的大模型应用开发项目，Sanic-Web 🛠️ 支持快速迭代与扩展，助力大模型项目快速落地。🚀

🌈 **Live Demo**  
[在线体验即将上线，敬请期待！]()

## 架构方案
![image](./images/app-01.png)

## 🎉 **特性**
- **核心技术栈**：Dify + Ollama + Sanic + Text2SQL
- **UI 框架**：Vue 3 + TypeScript + Vite 5
- **数据问答**：集成 ECharts大模型实现NL2SQL轻量级的数据图形化问答展示
- **表格问答**：支持 CSV格式文件的上传与基于大模型总结预处理和NL2SQL的表格数据问答
- **通用问答**：支持通用数据形式问答基于对接三方RAG系统+公网检索模式
- **应用架构**：作为一个轻量级全链路一站式大模型应用开发框架方便扩展落地
- **灵活部署**：支持大模型应用开发各依赖组件docker-compose一键拉起快速部署零配置

## 运行效果
![image](./images/chat-04.gif)
![image](./images/chat-01.png)
![image](./images/chat-03.png)

## 💡环境配置要求

在开始之前，请确保您的开发环境满足以下最低配置要求：

- **操作系统**：Windows 10/11, macOs M1系列, Centos/Ubuntu
- **GPU**: 本地使用ollama部署，推荐使用Nvidia显卡或单CPU模式。
- **内存**：8GB+

## 🔧 **前置条件**
* Python 3.8+
* Poetry 1.8.3+
* Node.js 18.12.x+
* Pnpm 9.x
* Dify 0.7.1+
* Mysql 8.0+

📚 **大模型部署**
- [参考Ollama官网部署](https://ollama.com/docs/install)
- 模型: Qwen2.5


## 🚀 **快速开始**

   - 为了兼顾第一次接触大模型应用的同学，我们提供了一键拉起Dify服务零配置，同时启动前端方式，方便大家快速体验。
   - 如果本地已经安装过Dify的同学，可以跳过安装Dify的步骤，直接导入***数据问答流程画布***进行相应配置即可。
   - 如果需要安装最新版Dify的同学,可以参考官方文档[Dify文档](https://docs.dify.ai/zh-hans)。
   - 具体步骤如下：

1. **启动服务**
   ```bash
   # 拉起dify服务
   cd docker/dify
   docker-compose up -d
   
   # 启动前后端服务
   cd docker
   docker compose up -d

2. **数据初始化**
   ```bash
   cd docker
   ./init.sh
   
   或执行
   
   python3 common/initialize_mysql.py
   
3. **访问服务**
 - 前端服务：http://localhost:8081


## 🛠️ **本地开发**
- 需要安装项目所有前置依赖、参考上面前置条件

1. **后端依赖安装**  
   - poetry安装 [参考poetry官方文档](https://python-poetry.org/docs/)
   ```bash
   # 安装项目依赖
   poetry install
   
2. **初始化数据库**
   ```bash
   # 安装mysql&初始化数据库
   python3 common/initialize_mysql.py

3. **前端依赖安装**  
   - 前端基于chatgpt-vue3-light-mvp开源项目[参考chatgpt-vue3-light-mvp安装](https://github.com/pdsuwwz/chatgpt-vue3-light-mvp)
   
4. **访问服务**
 - 前端服务：http://localhost:2048

## 🌹 支持

如果你喜欢这个项目或发现有用，可以点右上角 [`Star`](https://github.com/pdsuwwz/chatgpt-vue3-light-mvp) 支持一下，你的支持是我们不断改进的动力，感谢！ ^_^ 

## QA交流群
![image](./images/ding.png)

## License

[MIT](./LICENSE) License | Copyright © 2024-PRESENT [AiAdventurer](https://github.com/apconw)