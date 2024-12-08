import tkinter
import tkinter.messagebox
import tkinter.filedialog
import base64

class ScConverterGUI:
    def __init__(self):

        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x218")
        self.main_window.resizable(width=False, height=False)
        self.main_window.title ('MSK66-EKB')

        icons8_beaver_48b = b'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'
        icons8_beaver_48d = base64.b64decode(icons8_beaver_48b)
        icons8_beaver_48 = tkinter.PhotoImage(data=icons8_beaver_48d)
        self.main_window.iconphoto(False, icons8_beaver_48)

        # Создать виджет меню.
        self.main_menu = tkinter.Menu()

        # Добавить пункты меню.
        self.file_menu = tkinter.Menu(tearoff=0)
        self.file_menu.add_command(label="Открыть Файл",
                                   command=self.open_file)
        self.file_menu.add_command(label="Сохранить как",
                                   command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход",
                                   command=self.main_window.destroy)
        
        self.file_menu2 = tkinter.Menu(tearoff=0)
        self.file_menu2.add_command(label="Справка",
                                    command=self.reference)
        self.file_menu2.add_command(label="О программе",
                                    command=self.click_about)

        # Добавить заголовки меню.
        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.main_menu.add_cascade(label="Обзор", menu=self.file_menu2)

        # Создать шесть рамок, чтобы сгруппировать виджеты.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame3 = tkinter.Frame(self.main_window)
        self.mid_frame4 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать объект IntVar для использования
        # с виджетами Radiobutton.
        self.radio_var = tkinter.IntVar()

        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)

        # Объект StringVar нужен для того, чтобы его связать
        # с выходной надписью. Для сохранения последовательности
        # пробелов используется метод set данного объекта.
        self.value = tkinter.StringVar()
        self.path = tkinter.StringVar()
        self.ok = tkinter.StringVar()
        self.state_button = tkinter.StringVar()

        self.default_value()

        # Создать виджеты в рамке top_frame.
        self.label1 = tkinter.Label(self.top_frame,
                                    text = 'Пересчёт координат: ')
        
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                        text = 'Из СК ЕКБ в МСК66',
                                        variable = self.radio_var,
                                        value= 1)
        
        self.rb2 = tkinter.Radiobutton (self.top_frame,
                                        text = 'Из МСК66 в СК ЕКБ',
                                        variable = self.radio_var,
                                        value= 2)
        
        # Упаковать виджеты верхней рамки.
        self.label1.pack(side='left',padx=(5,5), pady=(10,2))
        self.rb1.pack(side='left',padx=(20,10), pady=(10,2))
        self.rb2.pack(side='left',padx=(10,30), pady=(10,2))

        # Создать виджеты для средних рамок.
        self.descr_label1 = tkinter.Label(self.mid_frame1,
                                         text = 'Имя')
        
        self.descr_label2 = tkinter.Label(self.mid_frame1,
                                         text = 'X')
        
        self.descr_label3 = tkinter.Label(self.mid_frame1,
                                         text = 'Y')
        
        self.descr_label4 = tkinter.Label(self.mid_frame1,
                                         text = 'Высота')
        
        self.coordinate_entry1 = tkinter.Entry(self.mid_frame2,
                                               width=15,
                                               font=("Helvetica", 8))
        
        self.coordinate_entry2 = tkinter.Entry(self.mid_frame2,
                                               width=15,
                                               font=("Helvetica", 8))
        
        self.coordinate_entry3 = tkinter.Entry(self.mid_frame2,
                                               width=15,
                                               font=("Helvetica", 8))
        
        self.coordinate_entry4 = tkinter.Entry(self.mid_frame2,
                                               width=10,
                                               font=("Helvetica", 8))
        
        self.text_label1 = tkinter.Label(self.mid_frame3,
                                         text = 'Координаты: ')

        self.output_text = tkinter.Entry(self.mid_frame3,
                                         width=100,
                                         font=("Helvetica", 8),
                                         textvariable=self.value)

        self.text_label2 = tkinter.Label(self.mid_frame4,
                                         text = 'Загруженный файл: ')

        self.path_string = tkinter.Label(self.mid_frame4,
                                  foreground=('#000080'),
                                  textvariable=self.path)
    
        
        # Упаковать виджеты для средней рамки.
        self.descr_label1.pack(side='left',padx=(51,47), pady=2)
        self.descr_label2.pack(side='left',padx=(58,60), pady=2)
        self.descr_label3.pack(side='left',padx=(53,39), pady=2)
        self.descr_label4.pack(side='left',padx=(38,30), pady=2)
        self.coordinate_entry1.pack(side='left', padx=(5,5), pady=5, ipadx=10)
        self.coordinate_entry2.pack(side='left', padx=(5,5), pady=5, ipadx=10)
        self.coordinate_entry3.pack(side='left', padx=(5,5), pady=5, ipadx=10)
        self.coordinate_entry4.pack(side='left', padx=(5,5), pady=5, ipadx=10)
        self.text_label1.pack(side='left',padx=(20,10), pady=5)
        self.output_text.pack(side='left',padx=(3,22), pady=5)
        self.text_label2.pack(side='left',padx=5,pady=5)
        self.path_string.pack(side='left',padx=5,pady=5)

        # Иконки в байтовом представлении.

        icon_question16b = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAHYAAAB2AH6XKZyAAAAB3RJTUUH6AsHCho70HWszgAAAhxJREFUOMttk01IVFEUx3/3OeMEGYQEIUEwU5MfNetWRYthFkGug7RIohBimqGVmdWiCGyhudRaaZuIwISCdBtUuAkioexNBUmBEmnqOO/ec1o4M74ZPXAX93z8z/98Gerk2J0fjapcA9JAvKwuADPGY+Tj7YMbYX8PINVXAKBjwM+pyAYqgyqSUZWkqiRVJIPKoDopdgwU8gCtN30ATAWpo39+HEMXGtbWScWm+uTTvWRXFaC9by6HMUNhx8ao4eSRJjwDb+ZX+VcUTBhYNT93v33YtF3/ECMaKVbQDdDWsovn2URN8guj33nvr5YZlFMHNuap0SxiQS2IpVQKuHFmPwAjr39xd3IBgKvpfZSCgLCvGs1GUJdWt1V3g4Hex/M0ePB33ZFJ7QVgfaMcJGarH5COqNh4lVZZltctBjh6YDcPzycQVfqf+kQ9h0pNUxMRxO7Y8LVAeHAuBcCJW7MsrgQ7+kXU2QKGZJgBgBHh7Zc/TM3+ZmFpjWhD3Ww3vwVP1c2oc6jUPqOOpeUSiysljG63q3Ooc9PmcO90DNVifR+a90R5N3gKgJaeVzTFIrXZN0cZMwCHLr/MYRgKAzhRjrc2s7xm+fxzZTt9Jf919PRwtbDEpRfjQFc9kx0CwTDhj3V2V48p3jOJ/6izG7U5dRYNLUtlcVQs6iyozftjnd2JK1O1x1SR+MVnUSALZOrPWQM78m3ibM05/wfDJx+SNfGdwAAAAABJRU5ErkJggg=='
        icon_question16d = base64.b64decode(icon_question16b)

        icons_8beaver_16b = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AsHChwWw/BXPQAAAnBJREFUOMutk89rnGUQxz/zPO+7u8lm0/ojhhQSkpggSdWDB72IkZggxR5SUZpDKR5zaUqVHLRqbl5UjAb1JvgPBJUWwaCEolAoKm0hmjQkpCSUFhKS3c2bfX88z3hYEhL8BaVzGmaYzwzznYEHZZdHu/4xPj3S/Z91wZ7z7UrUPvPG8cHE6RkrDEWJo1JLP2u0hQkg+V9AS3NhNZ8LpVqpYY2QZB5rZNyR9APD/waQPefGOwPlKMlKC2sb1FJH4hw5a7BGUNVbqnzuVGfF6+LYN8vZp+d6OD+9hNkDeNXnGnLBF0ebGn7b3IlRBRS8V1DpzVkzlQ/s7051bvrVria/mMihCQ7axyc7rwdGng6NQQyEVijmQgIrbEcJ5Vr655uXVvsALMDbL7QyNdZDq+Olkaceu1jMByfi1OFUcc6jKlgjWAOp81Rq2aMv9x4tzy5tX7UAP6/u8HCiZ8F8qejVYj5ciVPXV8oF9pHmAoWcZTfO2IkdUZKRpI7M+9JPy5Wv9lUwIjPGyHfvza5vAXw9+kR/c0P4TGAFVSiEls1qzEa1hlcFJTwk4wdX7lYP7sErLXHqAQMKaebJBQENYcBWlJAPzTXqWXhruPVvi4zi7KPt3ZTNasJWlFCpZVTjFEUATXq6G88fUmH8+baBOHWvxU5LqrolIvOdDxXeLQSmvX4LEGeeapyWiwHPvv/jnYXJk211wORw+5O/rpVvZk73kSIgKj6wYqR+Eniv64ieuvRH+donr3Rw4fJtZOJEBx9+f5uhx0ungVGEYyIEgFPProreU2Xee//D3Er0C8CL3UXmlnfqnV4HBvuO3PcX/wVMnxmcomWkqgAAAABJRU5ErkJggg=='
        icons_8beaver_16d = base64.b64decode(icons_8beaver_16b)

        # Создать переменные для отображения кртинок на кнопках.
        self.image_question = tkinter.PhotoImage(data=icon_question16d,format='png')
        self.image_bobr = tkinter.PhotoImage(data=icons_8beaver_16d,format='png')

        # Создать виджеты Button для нижней рамки.
        self.question_button = tkinter.Button(self.bottom_frame,
                                          image = self.image_question,
                                          command=self.reference)
        self.bobr_button = tkinter.Button(self.bottom_frame,
                                          image = self.image_bobr,
                                          command=self.click_bobr)
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='    Рассчитать    ',
                                          command=self.choice)
        self.save_string = tkinter.Button(self.bottom_frame,
                                          text='  Сохранить в конец файла  ',
                                          command=self.save_file_add,
                                          state='disabled')
        self.save_ok = tkinter.Label(self.bottom_frame,
                                          foreground=('#228B22'),
                                          textvariable=self.ok)         
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text=' Выйти ',
                                          command=self.main_window.destroy)
        
        # Упаковать кнопки.
        self.question_button.pack(side='left',padx=(15,2), pady=(10,8))
        self.bobr_button.pack(side='left',padx=(2,35), pady=(10,8))
        self.calc_button.pack(side='left',padx=15, pady=(5,10))
        self.save_string.pack(side='left',padx=(3,3), pady=(5,10))
        self.save_ok.pack(side='left',padx=10, pady=(5,10))
        self.quit_button.pack(side='right',padx=(0,14), pady=(5,10))


        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
        self.mid_frame4.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        self.main_window.config(menu=self.main_menu)
        tkinter.mainloop()

    # Метод convert является функцией обратного вызова
    # для кнопки 'Рассчитать'.

    def convert_ekb_msk(self):
        # Получить значение, введенное пользователем
        # в виджеты self.coordinate_entry.

        name = str(self.coordinate_entry1.get())

        X = float(self.coordinate_entry2.get())
        
        Y = float(self.coordinate_entry3.get())

        high = str(self.coordinate_entry4.get())


        # Конвертировать координаты.
        X2 = float(350201.477094956 + X * 0.999947241 + Y * 0.007808129)
        Y2 = float(1492688.10180136 + X * (-0.007807914) + Y * 0.999947949)

        # Результат.
        coordinates = (f'{name},{X2:.3f},{Y2:.3f},{high}')

        # Конвертировать координаты в строковое значение
        # и сохранить его в объекте StringVar. В результате
        # виджет self.output_text будет автоматически обновлен.
        self.value.set(coordinates)
        self.ok.set('     ')
        self.state_button_check()

    def convert_msk_ekb(self):
        # Получить значение, введенное пользователем
        # в виджеты self.coordinate_entry.

        name = str(self.coordinate_entry1.get())

        X = float(self.coordinate_entry2.get())
        
        Y = float(self.coordinate_entry3.get())

        high = str(self.coordinate_entry4.get())

        A =	350201.4771
        B =	0.999947241
        C =	0.007808129
        E =	1492688.102
        F =	-0.007807914
        G =	0.999947949

        # Конвертировать координаты.
        X2 = float(((X - A) * G - C * (Y - E)) / (B * G - C * F))
        Y2 = float((B * (Y - E) - (X - A) * F) / (B * G - C * F))

        # Результат.
        coordinates = (f'{name},{X2:.3f},{Y2:.3f},{high}')

        # Конвертировать координаты в строковое значение
        # и сохранить его в объекте StringVar. В результате
        # виджет self.output_text будет автоматически обновлен.
        self.value.set(coordinates)
        self.ok.set('     ')
        self.state_button_check()

    def choice(self):
        # Получить значение radiobutton.
        position = self.radio_var.get()
        
        if (position == 1):
            self.convert_ekb_msk()

        elif (position == 2):
            self.convert_msk_ekb()

    def click_about(self):
        tkinter.messagebox.showinfo("О программе", "Разработка: WildRoger.                                                          "
                                    "Электронная почта: mx.sverre@gmail.com                                                                                                                                     "
                                    "Версия 0.2")
        
    def click_bobr(self):
        tkinter.messagebox.showinfo("Bóbr", "Bóbr kurwa!")

    def reference(self):
        tkinter.messagebox.showinfo("Справка", 'Программа для пересчёта геодезических координат из местной системы города Екатеринбурга в МСК66 и наоборот.'
                                    "                                                                                                                                                                                              "
                                    'Для пересчёта координат, нажать кнопку "Рассчитать".'
                                    "                                                                                                                  " 
                                    'Для выбора системы координат переключить кнопку в поле "Пересчёт координат:".'
                                    "                                                                                                                                                         "
                                    'Кнопка "Открыть файл" позволяет загрузить файл с координатами с целью добавления в него новых строк.'
                                    "                                                                                                                    "
                                    'Кнопка "Сохранить файл" сохраняет результаты в новый файл.' 
                                    "                                                                                                                                                                                                  "
                                    'Кнопка "Сохранить в конец файла", добавляет строку с результатами в конец загруженного файла, предварительно файл нужно загрузить. ')

    # Открываем файл.
    def open_file(self):
        self.filepath = tkinter.filedialog.askopenfilename()
        if self.filepath != "":
            tkinter.messagebox.showinfo("Информация", "Файл загружен.")
            self.path.set(self.filepath)
            self.ok.set('     ')
            self.state_button_check()

    # Cохраняем текст из текстового поля в новый файл.
    def save_file(self):
        self.filepath = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",initialfile = "Новый текстовый документ",title = "Select file",filetypes = (("Текстовые документы (*.txt)","*.txt"),("Все файлы","*.*")))
        if self.filepath != "":
            text = (self.output_text.get() + '\n')
            with open(self.filepath, 'a') as file:
                file.write(text)
                tkinter.messagebox.showinfo("Информация", "Файл сохранен.")
                self.path.set(self.filepath)
                self.ok.set('     ')
                self.state_button_check()

    # Cохраняем текст из текстового поля в последнюю строку загруженного файла.
    def save_file_add(self):
        if self.filepath != "":
            text = (self.output_text.get() + '\n')
            with open(self.filepath, 'a') as file:
                file.write(text)
                self.ok.set('Ok')
                self.state_button_check()

    def default_value(self):
        # Переменная открытого файла по умолчанию.
        self.path.set('Файл не выбран')
        self.ok.set('     ')

    def state_button_check(self):
        if self.ok.get() == 'Ok':
            self.save_string["state"] = ("disabled")
        elif self.path.get() == 'Файл не выбран':
            self.save_string["state"] = ("disabled")
        elif len(self.value.get()) == 0:
            self.save_string["state"] = ("disabled")
        else: 
            self.save_string["state"] = ("normal")

# Создать экземпляр класса ScConverterGUI.
if __name__ == '__main__':
    sc_conv = ScConverterGUI()