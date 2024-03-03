#-*-coding:utf-8-*-
from stardict import DictCsv
import os
from datetime import datetime

# 初始化词典实例
dictionary = DictCsv('ecdict.csv')

# 创建保存查询结果的文件夹
results_folder = "query_results"
os.makedirs(results_folder, exist_ok=True)

# 记录单词查询次数的字典
word_counts = {}

# 询问论文名字
paper_name = input("请输入论文名字: ").strip()

# 主循环，不断查询单词
while True:
    word_to_query = input("请输入要查询的英文单词（输入 'exit' 退出）: ").strip()
    if word_to_query.lower() == 'exit' or word_to_query == "":
        break
    result = dictionary.query(word_to_query)
    word_counts[word_to_query] = word_counts.get(word_to_query, 0) + 1
    if result:
        print(f"单词: {result['word']}")
        if 'phonetic' in result:
            print(f"英标: {result['phonetic']}")
        if 'translation' in result:
            print(f"中文释义: {result['translation']}")
    else:
        print(f"词典中未找到单词 '{word_to_query}'。")
    print()

# 构建文件名：论文名_单词数_日期.txt
file_name = f"{paper_name}_{len(word_counts)}_{datetime.now().strftime('%Y%m%d')}.txt"
file_path = os.path.join(results_folder, file_name)

# 保存查询结果和查询次数
with open(file_path, 'w', encoding='utf-8') as file:
    for word, count in word_counts.items():
        result = dictionary.query(word)
        if result:
            phonetic = result.get('phonetic', '无英标')
            translation = result.get('translation', '无中文释义')
            file.write(f"{word} [{phonetic}]: {translation} - 查询次数 {count} 次\n")

print(f"查询结果和次数已保存到 '{file_path}'。")


