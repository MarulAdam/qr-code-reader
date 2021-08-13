from tkinter import *
from tkinter import Button, Label, Tk, filedialog
from PIL import ImageTk,Image
from pyzbar.pyzbar import decode

class QrOkuyucu:

    def __init__(self, root):
        root.title("Qr Okuyucu")
        root.geometry("400x400")
        root.resizable(width=True, height=True)
        Button(root, text='resmi sec', command=self.resim_ac).pack()
        Button(root, text='yazi temizle', command=self.yazi_temizle).pack()

    def openfilename(self):
        filename = filedialog.askopenfilename(title="resim")
        return filename

    def resim_ac(self):
        global label
        global qr_label
        resim_adi = self.openfilename()
        yazi = ""
        for i in decode(Image.open(resim_adi)):
            yazi += str(i.data)[2:-1]
        label = Label(root, text=yazi)
        label.pack()

        qr_yol = resim_adi
        qr = Image.open(qr_yol)
        sekilli = qr.resize((150, 150), Image.ANTIALIAS)
        yeni_qr = ImageTk.PhotoImage(sekilli)
        qr_label = Label(root)
        qr_label.pack()
        qr_label.configure(image=yeni_qr)
        qr_label.image = yeni_qr
        

    def yazi_temizle(self):
        label.pack_forget()
        qr_label.pack_forget()

if __name__ == "__main__":
    root = Tk()
    uygulama = QrOkuyucu(root)
    root.mainloop()
