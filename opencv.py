# 引入 tkinter 模組
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import numpy as np
import cv2
import matplotlib.pyplot as plt


def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img
def openfile():#檔案(File)-讀取/寫入影像
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    img=cv2.imread(filename)#寫入圖檔
    cv2.imshow("寫入圖片",img)#在視窗顯示圖片
    cv2.waitKey()#when按下鍵盤任意案件
    cv2.destroyAllWindows()#關閉視窗
    

def RGB():#影像處理(Image Processing)-色彩空間轉換
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    img=cv2.imread(filename)#寫入圖檔
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#將RGB轉換成HSV顏色空間
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('原始圖片',img)
    cv2.imshow('HSV圖片',hsv)
    cv2.imshow('Gray圖片',gray)
    cv2.waitKey(0)#when按下鍵盤任意案件
    cv2.destroyAllWindows()#關閉視窗
    
def Histogram():#影像處理(Image Processing)-影像資訊呈現
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    Phelp=cv2.imread(filename)#寫入圖檔
    cv2.imshow("原始圖片",Phelp)#原始圖片
    cv2.waitKey()#when按下鍵盤任意案件
    cv2.destroyAllWindows()#關閉視窗
    plt.hist(Phelp.ravel(), 256, [0, 256])#繪製直方圖
    plt.show()#列印直方圖
    
    
def rotate():#影像處理(Image Processing)-幾何轉換功能
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    pig=cv2.imread(filename)#寫入圖檔
    height,width=pig.shape[:2]
    M=cv2.getRotationMatrix2D((width/2,height/2),45,0.6)#取得轉換矩陣(轉45度,縮小0.6倍
    rotate=cv2.warpAffine(pig,M,(width,height))#影像進行選轉
    cv2.imshow("原始圖片",pig)#原始圖片
    cv2.imshow("旋轉圖片",rotate)#選轉後圖片
    cv2.waitKey(0)#when按下鍵盤任意案件
    cv2.destroyAllWindows()#關閉視窗
    
def perspective():#影像處理(Image Processing)-透視轉換
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    shark=cv2.imread(filename)
    rows,cols=shark.shape[:2]
    print(rows,cols)
    pts1=np.float32([[150,50],[400,50],[60,450],[310,450]])#輸入影像四個頂點座標
    pts2=np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])#輸出影像四個頂點座標
    M=cv2.getPerspectiveTransform(pts1,pts2)
    dst=cv2.warpPerspective(shark,M,(cols,rows))
    #透視轉換(要透視的圖片,3x3轉換矩陣,())
    cv2.imshow("原始圖片",shark)#原始圖片
    cv2.imshow("透視圖片",dst)#選轉圖片
    cv2.waitKey()#when按下鍵盤任意案件
    cv2.destroyAllWindows()#關閉視窗

def Binarization():#影像處理(Image Processing)-二值化處理(使前景和背景分離)
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    img = cv2.imread(filename)
    t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    #當像素大於127將被處理為255，其餘值變為0
    cv2.imshow("原始圖片",img)
    cv2.imshow("二值化圖片",rst)
    cv2.waitKey()#when按下鍵盤任意案件
    cv2.destroyAllWindows()#關閉視窗
def Vague():#影像處理(Image Processing)-模糊化
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    img = cv2.imread(filename)
    
    output1 = cv2.blur(img, (5, 5))     # 指定區域單位為 (5, 5)
    output2 = cv2.blur(img, (25, 25))   # 指定區域單位為 (25, 25)
    cv2.imshow("原始圖片",img)#原始圖片
    cv2.imshow('模糊化1', output1)
    
    
    cv2.imshow('模糊化2', output2)
    cv2.waitKey(0)# 按下任意鍵停止
    cv2.destroyAllWindows()#關閉視窗
def mosaic():
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    img = cv2.imread(filename)
    cv2.imshow('原始圖片', img)
    size = img.shape         # 取得原始圖片的資訊
    level = 15               # 縮小比例 ( 可當作馬賽克的等級 )
    h = int(size[0]/level)   # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
    w = int(size[1]/level)   # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
    mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
    mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
    cv2.imshow('馬賽克圖片', mosaic)
    cv2.waitKey(0)           # 按下任意鍵停止
    cv2.destroyAllWindows()
    
def Contours():
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    o = cv2.imread(filename)
    cv2.imshow("original",o)
    gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
    ret,binary= cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)
    o = cv2.drawContours(o,contours,-1,(0,0,255),5)
    cv2.imshow("result",0)
    cv2.waitKey()
    cv2.destroyAllWindows()#關閉視窗
    

def BGR():#功能(Function)--模擬色票面板
    def changeColor(x):
        r=cv2.getTrackbarPos('R','image')#產生捲軸
        g=cv2.getTrackbarPos('G','image')
        b=cv2.getTrackbarPos('B','image')
        img[:]=[b,g,r]
    img = np.zeros((100,700,3),np.uint8)
    cv2.namedWindow('image')
    cv2.createTrackbar('R','image',0,255,changeColor)
    cv2.createTrackbar('G','image',0,255,changeColor)
    cv2.createTrackbar('B','image',0,255,changeColor)
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1)&0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    
def Brightnes():
    filetypes = {
        ('jpg files','*.jpg'),
        ('png files','*.png'),
        ('All files','*.*')
        }
    filename = filedialog.askopenfilename(#開啟檔案
        title='Open a file',#對話框標題
        initialdir='/',
        filetypes=filetypes
        )
    img = cv2.imread(filename)
    cv2.imshow('oxxostudio', img)

    contrast = 0    # 初始化要調整對比度的數值
    brightness = 0  # 初始化要調整亮度的數值
    cv2.imshow('oxxostudio', img)

    # 定義調整亮度對比的函式
    def adjust(i, c, b):
        output = i * (c/100 + 1) - c + b    # 轉換公式
        output = np.clip(output, 0, 255)
        output = np.uint8(output)
        cv2.imshow('oxxostudio', output)

    # 定義調整亮度函式
    def brightness_fn(val):
        global img, contrast, brightness
        brightness = val - 100
        adjust(img, contrast, brightness)

    # 定義調整對比度函式
    def contrast_fn(val):
        global img, contrast, brightness
        contrast = val - 100
        adjust(img, contrast, brightness)

    cv2.createTrackbar('brightness', 'oxxostudio', 0, 200, brightness_fn)  # 加入亮度調整滑桿
    cv2.setTrackbarPos('brightness', 'oxxostudio', 100)
    cv2.createTrackbar('contrast', 'oxxostudio', 0, 200, contrast_fn)      # 加入對比度調整滑桿
    cv2.setTrackbarPos('contrast', 'oxxostudio', 100)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
def abc():
    cap = cv2.VideoCapture(0)# 讀取攝影鏡頭
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        # 套用二值化黑白影像
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        img_gray = cv2.medianBlur(img_gray, 5)
        output = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        cv2.imshow('二值化黑白影像', output)
        if cv2.waitKey(1) == ord('q'):
            break       # 按下 q 鍵停止
    cap.release()
    cv2.destroyAllWindows()
    
window = tk.Tk()
# 設定視窗標題
window.title('影像處理程式開發平台')
# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
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
menu4.add_command(label='影像模糊化處理',command=Vague)
menu4.add_command(label='影像馬賽克處理',command=mosaic)
menu4.add_command(label='影像二值化處理',command=Binarization)

menu.add_cascade(label='影像處理(Image Processing)',menu=menu4)


menu3 = tk.Menu(menu,tearoff=0)
menu3.add_command(label='模擬色票面板',command=BGR)
menu3.add_command(label='調整亮度與對比',command=Brightnes)
menu3.add_command(label='影片二值化效果',command=abc)
menu.add_cascade(label='功能(Function)',menu=menu3)

text = tk.Text(window,undo=True,height=5,width=30)
# 執行主程式
window.mainloop()
