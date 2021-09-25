# 今日头条账号的爬取

## 爬取来源分析

- 今日头条App端：
  - 可以通过抓包获取APP内加载单条文章的api
    - api中包含二级页面中所有的内容，问题是夹杂着HTML代码，清洗麻烦
  - 无法通过正常方式获取加载文章的列表，无法实现自动化爬虫
- 今日头条web端:
  - 正常requets方式：
    - web端的api被做了加密处理，包括token，自定义字段（signature、as、cp），
    - 通过bp抓包获取到请求后发现，因为token的存在，api的有效时间只有3分钟，同样无法满足完全自动化爬取的要求
    - 加密问题，可以通过逆向解密自定义字段来破解，但短时间内来看学习成本较高，涉及知识面广。所以暂时排除此方法
  - selenium模拟浏览器方式：
    - 模拟正常访问操作，无需考虑加密，甚至反爬
    - 缺点，太慢