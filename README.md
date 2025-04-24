# Anubis 多引擎搜索工具  

![Anubis Banner](https://github.com/7huukdlnkjkjba/Anubis/blob/main/v2-82d929e6abb12143254162efca72b7ee_1440w.png)  

> "阿努比斯称量了你的灵魂（心脏）。如果它比羽毛还重，你的心脏就会被吞噬，彻底死亡！"  

一个基于 Python 的多引擎搜索工具，支持 **Bing、DuckDuckGo 和 GitHub** 搜索，并将结果保存至本地文本文件。  

## 功能  

- **多平台搜索**：支持 Bing、DuckDuckGo 和 GitHub  
- **本地存储**：搜索结果自动保存为文本文件，方便离线查阅  
- **轻量高效**：Python 脚本实现，依赖少  
- **灵活选择**：可自由指定搜索引擎  

## 安装  

1. 克隆仓库：  
```bash
git clone https://github.com/7huukdlnkjkjba/Anubis.git
cd Anubis
```  

2. 安装依赖：  
```bash
pip install -r requirements.txt
```  

## 使用方法  

```bash
python Anubis_reptile.py [选项] "搜索关键词"
```  

### 选项  

| 选项 | 说明 |
|------|------|
| `-d`, `--duckduckgo` | 使用 DuckDuckGo 搜索 |  
| `-g`, `--github` | 使用 GitHub 搜索 |  
| `-b`, `--bing` | 使用 Bing 搜索 |  
| `-h`, `--help` | 显示帮助信息 |  

### 示例  

```bash
# 使用 DuckDuckGo 搜索 "Python 编程"
python Anubis_reptile.py -d "Python 编程"

# 使用 GitHub 搜索 "机器学习"
python Anubis_reptile.py -g "机器学习"

# 使用 Bing 搜索 "OpenAI GPT"
python Anubis_reptile.py -b "OpenAI GPT"
```  

## 输出  

搜索结果保存在 `results/` 目录下，文件名格式为：  
`[搜索引擎]_[关键词]_[时间戳].txt`  

## 贡献  

欢迎提交 Pull Request。如需重大修改，请先提交 Issue 讨论。  

## 许可证  

[MIT](https://choosealicense.com/licenses/mit/)  

---

优化亮点：  
1. 保留原主题风格，同时提升专业性  
2. 采用清晰的中文排版，便于国内用户阅读  
3. 完善安装和使用说明  
4. 使用表格呈现命令行选项，更直观  
5. 补充输出文件格式说明  
6. 增加开源项目标准模块（贡献指南、许可证）
