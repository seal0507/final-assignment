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
本實驗選單功能分為三種：檔案(File)、影像處理(Image Processing)、功能(Function)如下圖所示。

![image](https://github.com/seal0507/final-assignment/blob/3/1.png)

本實驗在檔案(File)分為三種功能(圖 1)，寫入影像，儲存檔案，離開程式如所示，寫入影像的部分本實驗使用filedialog.askopenfilename()函數，開啟檔案對話框，匯入圖片[5]。

![image](https://github.com/seal0507/final-assignment/blob/3/2.png)

#### 二、	影像處理
首先再檔案(File)選單開啟圖檔開啟，將原始圖片選擇使用者想使用的影像處理進行影像轉換，在影像處理(Image Processing)選單中(圖 3)，本實驗設計八種功能，色彩空間轉換、影像資訊呈現、幾何轉換功能、透視投影轉換、影像二值化處理、影像模糊化處理、影像馬賽克處理。

![image](https://github.com/seal0507/final-assignment/blob/3/3.png)

將原始圖片進行色彩空間轉換，本實驗使用Open CV內的cv2.cvtColor()函數來實現色彩空間的轉換，經過處理後的圖片新增兩種樣式如圖 所示，第一種HSV圖片，HSV色彩空間三要素是色調(Hue)、飽和度(Saturation)、亮度(Value)將圖片提高色彩，本實驗在cv2.cvtColor()函數中填入了cv2.COLOR_BGR2HSV參數，第二種Gray圖片，將圖片轉為灰階，這邊使用了cv2.COLOR_BGR2GRAY參數[6]。

![image](https://github.com/seal0507/final-assignment/blob/3/4.jpg)

幾何轉換功能，此幾何轉換功能在本實驗為旋轉功能，點擊此功能時會將原始圖片縮小0.6倍，再將圖片旋轉45度如圖 5所示，使用函數cv2.warpAffine()對影像進行選轉，再透過cv2.getRotationMarix2D()取得轉換矩陣[7]。

![image](https://github.com/seal0507/final-assignment/blob/3/5.png)

透視投影轉換，此功能能夠將矩形對映為任意四邊形如圖 6所示，首先先取得輸入影像的四個點座標及輸出影像的四個點座標，將輸入與輸出點放入函數cv.getPerspectiveTransform()產生四邊形的轉換矩陣，最後透過cv2.warpPerspective()來實現此功能[8]。

![image](https://github.com/seal0507/final-assignment/blob/3/6.png)

影像二值化處理，將原始影像處理為僅有兩個值的二值影像如圖 7所示，當影像大於127的像素會被處理為255，其餘值為0，本實驗使用cv2.threshold()對影像進行二值化設定值處理[9]。

![image](https://github.com/seal0507/final-assignment/blob/3/7.png)

影像模糊化，將原始影像變得不清楚如圖 8所示，使用cv2.blur()函式計算指定區域所有像素的平均值，再將平均值取代中心像素[10]。

![image](https://github.com/seal0507/final-assignment/blob/3/8.png)

影像的馬賽克效果，在瀏覽圖片時，如果將小張的圖片不斷放大，就會看見圖片的像素變大，成為一格格的馬賽克如圖 9所示，運用同樣的原理，首先使img.shape取得圖片尺寸，接著使用cv2.resize()函式(interpolation=cv2.INTER_LINEAR)將圖片進行縮小，接著再度使用cv2.resize()方法搭配( interpolation=cv2.INTER_NEAREST)將圖片進行放大，即可出現馬賽克效果[11]。

![image](https://github.com/seal0507/final-assignment/blob/3/9.png)

#### 三、	功能操作
功能(Function)選單三種功能如圖 10所示，首先第一種為模擬色票面板，此功能提供R、G、B三捲軸，滑動捲軸設定捲軸值，可依據使用者的喜愛自行調色如圖 11所示，本實驗使用cv2.createTrackbar()來定義三個捲軸，使用函數cv2.createTrackbarPos()取得捲軸的值[12]。

![image](https://github.com/seal0507/final-assignment/blob/3/10.png)

![image](https://github.com/seal0507/final-assignment/blob/3/11.png)

第二種功能為調整亮度與對比，依據使用者需求調整搖桿，能將亮度與對比對調高調低如圖 12所示，在此本實驗搭配NumPy來調整對比度與亮度，在OpenCV裡讀取的影像，是使用NumPy陣列，因此在讀取影像後，透過NumPy「陣列廣播」的功能，能迅速更改圖片中每個像素的顏色。本實驗，使用了簡單的轉換公式，只需調整 contrast(對比)和brightness(亮度)的數值，就能改變影像的對比度和亮度[13]。

![image](https://github.com/seal0507/final-assignment/blob/3/12.png)

第三種功能為影像二值化的黑白效果，首先開啟攝像頭，本實驗使用VideoCapture()方法，讀取攝像頭，開啟影像畫面，cap.isOpened()判斷影像畫面是否正常開啟，成功開啟後透過二值化程式將畫面轉為黑白色的如圖 13所示[14]。

![image](https://github.com/seal0507/final-assignment/blob/3/13.png)

### 肆、	結論
本研究將眾多影像處理的技術統整到GUI圖形使用者介面上，讓使用者使用影像處理更方便，本研究在功能區塊有兩種功能，第一種模擬色票面板的功能，可讓使用者清楚的得知電腦使用多少位元(bit)來記錄色彩，第二種對比亮度調整功能，依據使用者需求，能將圖片對比及亮度最佳化。

### 伍、	參考文獻
[1]CHEN)TSENG)；陳文儉(WEN-JAN曾伊秀(I-HSIU. (2019年03月01日).工程圖影像字元萃取實作. 科學與工程技術期刊, 頁 科學與工程技術期刊.

[2]Chen)Hu)；陳傳傑(Chuan-Jie Chen)；黃致軒(Zhi-Xuan Huang)；陳茂林(Mao-Lin胡永柟(Yung-Nan. (2006年06月01日).模型估測應用於影像辨識之研究與設計.科學與工程技術期刊2卷2期, 頁 P79 - 86.

[3]OXXO.STUDIO.(無日期).OpenCV 函式庫. 擷取自 STEAM教育學習網.

[4]TalkShengYu. (2020年11月26日). Python tkinter filedialog 開啟檔案對話框. 擷取自 PYTHON教學.

[5]Tubaspieler. (2021年03月01日). Python tkinter filedialog 開啟檔案對話框. 擷取自 知乎.

[6]阿新. (2019年02月18日).使用python編寫opencv程式. 擷取自 程式人生.

[7]嗡嗡. (2020年09月15日).【沒錢ps,我用OpenCV!】. 擷取自 第 12 屆 iThome 鐵人賽.

[8]CSDN. (2019年10月10日).python -opencv 使用滑动条. 擷取自 夏华东的博客.

[9]Liu六六六. (2018年05月18日).Python和OpenCV做图像处理. 擷取自 知乎.

[10]TalkShengYu. (2020年03月14日) Python OpenCV影像二值化 Image Thresholding. 擷取自 PYTHON教學.

[11]TalkShengYu. (2020年03月16日).Python OpenCV影像平滑模糊化 blur. 擷取自 PYTHON教學.

[12]調整影像的對比和亮度. 擷取自 STEAM教育學習網.

[13]影像的馬賽克效果. 擷取自 STEMAM教育學習網.

[14]二值化黑白影像. 擷取自 STEAM教育學習網.
