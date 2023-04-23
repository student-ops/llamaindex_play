from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
index.save_to_disk('data/index.json')
# response = index.query("何人が研究関わっていますか。またそれぞれの名前も教えて")
response = index.query("研究している分野、研究内容、研究の目的、研究の方法、研究の結果、研究の成果について詳しく教えてください。情報が足りない項目があれば{情報が足りない}として")
print(response)
