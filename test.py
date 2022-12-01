from tkinter import *
from tkinter.messagebox import *
tk=Tk()
tk.title('auth')

def checkToken():
    print(accountEdit.get())
    if accountEdit.get() == 'test' and passwordEdit.get() == 'test':
        print("keyclaok成功登入")
        showinfo(title='正確', message='帳號密碼正確，請至您的信箱收信') 
        otpEdit = Entry(tk)    
        otpEdit.grid(row=2, column=1)
        
    else:
        showinfo(title='錯誤', message='帳號密碼錯誤，請重新輸入') 

def checkOTP():
    if otpEdit.get() == "aaa" :
        print("OTP驗證成功")
        showinfo(title='OTP驗證正確', message='OTP正確，歡迎使用本系統') 
    else:
        showinfo(title='錯誤', message='OTP輸入錯誤，請重新輸入')
        

# account label + account btn
accLabel = Label(tk, text='Account:')
accLabel.grid(row=0, column=0)
accountEdit = Entry(tk)
accountEdit.grid(row=0, column=1)

# password label + password btn
passwordLabel = Label(tk, text='Password:')
passwordLabel.grid(row=1, column=0)
passwordEdit = Entry(tk,show='*') 
passwordEdit.grid(row=1, column=1)

# otp label + otp btn
otpLabel = Label(tk, text='OTP Code:')
otpLabel.grid(row=2, column=0)
otpEdit = Entry(tk,state="disable") 
otpEdit.grid(row=2, column=1)

# btn 
authBtn = Button(tk,text="  帳密登入 ",command = checkToken)
authBtn.grid(row=3,column=0)

outBtn = Button(tk,text="   OTP碼認證   ",command = checkOTP)
outBtn.grid(row=3,column=1)

otpBtn = Button(tk,text="  退出 ")
otpBtn.grid(row=3,column=2)

#主事件循环
mainloop()