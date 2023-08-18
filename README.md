# 主要程式說明

```vertical.py``` : 讀取申論題的題目與答案

```check_multiple.py``` : 把有選擇題的PDF檔放到其他資料夾(另外處裡)

```tester.py``` : 檢測產出的.csv檔有沒有問題(比如沒有讀到題目)

```multiple.py``` : 讀取選擇題的內容

```plainread.py``` : 讀取PDF檔裡所有的內容(debug需要)

```linebreaker.py``` : 建立一個GUI幫助刪除不必要的換行(手動)


# 執行畫面

1. 處裡申論題(12個PDF)
![video.gif loading...]()


# 如何讀取PDF內容

1. 純Python:
```python

from PyPDF2 import PdfReader
reader = PdfReader("file.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

```

2. linux command:
```
pdftotext file.pdf
```
產生```file.txt```

# run code
```python3 [filename].py [filename].pdf```
