# 數位影像處理
## 資工三甲  李致翰
### 壹、摘要
早期工程圖影像以紙本方式來保存，需利用掃描儀器數位化建檔儲存電腦後，才可進一步在工程圖影像開發相關的應用。但在科技的日新月異下，透過影像處理將工程圖經過二值化處理可把背景與物件分離，即可成功取得工程圖影像字元的位置，獲得相當高的正確率[1]。現在影像辨識的應用層面也越來越廣泛，影像處理、分析與辨識，能夠將圖片作某些特徵處理，依照特徵點去與其他影像圖片作比對，進一步得到兩者間的相似度[2]。
鑒於科技進步，電腦能夠辨識的物品越來越多，本實驗將設計一套匯入圖片可將圖片進行影像處理的應用程式，如將圖片二值化，透視投影，色彩空間轉換等等，讓使用者影像處理更方便。
### 貳、	文獻回顧
#### 一、	Open CV函式庫
OpenCV 全名是Open Source Computer Vision Library(開源計算機視覺函式庫)，是一個跨平台的電腦視覺函式庫，常應用於擴增實境、臉部辨識、手勢辨識、動作辨識、運動跟蹤、物體辨識或圖像分割...等領域，能使用各種不同語言(Java、Python、C/C++...等)進行開發，由於 OpenCV 的高執行效率，甚至可用來開發 Real-time 的應用程式[3]。
#### 二、	使用Python編寫Open CV程式
選擇Python編寫Open CV的原因：Python為解釋型語言，因此適合快速學習，同時Python具有結構鬆散，外部可用模組較多的優點，使用Python學習Open CV對於初學者來說非常適合[4]。
### 參、	實驗方法與結果
一、	功能選單
本實驗選單功能分為三種：檔案(File)、影像處理(Image Processing)、功能(Function)如圖 1所示。
```python
window = tk.Tk()# 設定視窗標題
window.title('影像處理程式開發平台')#設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("800x500+250+150")
def create_label(txt):
    lbl_1 = tk.Label(window, text=txt, bg='skyblue', font=('Arial', 12), width=88, height=2)
    lbl_1.grid(column=0, row=0)
def quit():
    window.destroy()
create_label('資工三甲4A8G0007李致翰      影像處理程式開發平台')
menu = tk.Menu(window)
window.config(menu=menu)
menu2 = tk.Menu(menu,tearoff=0)
menu2.add_command(label='讀取/寫入影像',command=openfile)
menu2.add_command(label='儲存檔案')
menu2.add_command(label='離開程式',command=quit)
menu.add_cascade(label='檔案(File)',menu=menu2)
menu4 = tk.Menu(menu,tearoff=0)
menu4.add_command(label='色彩空間轉換',command=RGB)
menu4.add_command(label='影像資訊呈現',command=Histogram)
menu4.add_command(label='幾何轉換功能',command=rotate)
menu4.add_command(label='透視投影轉換',command=perspective)
menu4.add_command(label='影像二值化處理',command=Binarization)
menu.add_cascade(label='影像處理(Image Processing)',menu=menu4)
menu3 = tk.Menu(menu,tearoff=0)
#menu3.add_command(label='繪製影像輪廓',command=Contours)
menu3.add_command(label='模擬色票面板',command=BGR)
menu.add_cascade(label='功能(Function)',menu=menu3)
text = tk.Text(window,undo=True,height=5,width=30)#執行主程式
window.mainloop()
```
