# helloworld
#我是資管二的劉正宇，此為數位應用程式設計的repo以及成品

#this is week 1's final app(已停止更新)
https://jack-helloworld.herokuapp.com/

#this is week 2's
https://weektwofinal.herokuapp.com/

第五週 留言板完成(遇到粉多問題)

第六週 註冊與登入系統完成(沒有做權限的部分，登入系統暫無作用)
      遇到的問題: is_authenticate在django2.0以後是屬性
                 if 下方要加一整行的空白才會中斷
      更新:目前登入後會自動填入暱稱(不再提供暱稱欄位)
      
第七週 搜尋、刪除、編輯留言功能完成
紀錄:
我習慣把問題拆成幾個細項來解決:

      1.要先把自己的資訊過濾出來:了解函數: Filter: 被歸類在objects裏頭，在()內加入條件，
                             這裡用的是talker 要是登入者(權限不同的關係)
      
      遇到的困難:思考條件到底要放在template的html裡還是view裡，雖然都能呈現出這個功能但是還是選擇view 因為等等還要使用這些資訊(最後才改)
      
      2.過濾每一項資訊，給予每則訊息一個post的機會: for loop 的 熟悉 以及 form 的各項 input
                                   
      遇到的困難:一開始很崩潰，因為不知道form有結束的點(</form>)，所以post的東西永遠是迴圈的最後一項
                
                解決方式:因為本來就對html有些許的背景知識，所以猜到了可以關掉form的語法(很有成就感)
      
      3.刪除特定資訊:要了解delete怎麼運作
            沒遇到特別困難
 
      4.編輯特定資訊:要了解update
            遇到的困難:一開始認為 給input type="text"的欄位 value 後，如果再上面做修正， value會更改 (結果不會)
                     解決方案: 看助教的範例發現不用在輸入欄上顯示原訊息， 我選擇在上方顯示，用span
      
      5.搜尋:沒有更新的概念(這次用的是filter)
            遇到的困難:沒有看懂 __contain 並不是資料庫欄位的名字，所以愣了很久
            解決:就試試看就成功啦~
       小結:
            其實對於有程式基礎的人去看助教給的教學網站，絕對都可以順利做出每週目標，沒做出來的八成是太懶或是沒認真看
      Reference:
            http://dokelung-blog.logdown.com/archives
            https://code.ziqiangxuetang.com/django/django-queryset-api.html
