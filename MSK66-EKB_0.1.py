import tkinter
import tkinter.messagebox
import tkinter.filedialog

class ScConverterGUI:
    def __init__(self):

        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x160")
        self.main_window.resizable(width=False, height=False)
        self.main_window.title ('MSK66-EKB')
        self.main_window.iconbitmap(default="./icons8-beaver-48.ico")

        # Создать виджет меню.
        self.main_menu = tkinter.Menu()

        # Добавить пункты меню.
        self.file_menu = tkinter.Menu(tearoff=0)
        self.file_menu.add_command(label="Открыть Файл",
                                   command=self.open_file)
        self.file_menu.add_command(label="Сохранить как",
                                   command=self.save_file)
        self.file_menu.add_command(label="Сохранить в текущий файл",
                                    command=self.save_file_add)
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

        # Создать пять рамок, чтобы сгруппировать виджеты.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame3 = tkinter.Frame(self.main_window)
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
        self.label1.pack(side='left',padx=(5.5), pady=(10,2))
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
    
        
        # Создать виджеты для средней рамки.
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

        # Создать переменные для отображения кртинок на кнопках.
        self.image_question = tkinter.PhotoImage(file = ".\icon_question16.png")
        self.image_bobr = tkinter.PhotoImage(file = ".\icons8-beaver-16.png")

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
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)
        
        # Упаковать кнопки.
        self.question_button.pack(side='left',padx=(15,2), pady=(10,8))
        self.bobr_button.pack(side='left',padx=(2,50), pady=(10,8))
        self.calc_button.pack(side='left',padx=(85,125), pady=(5,10))
        self.quit_button.pack(side='right',padx=(10,15), pady=(5,10))

        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
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
        coordinates = (f'{name},{X2:.3f},{Y2:.3f},{high},')

        # Конвертировать координаты в строковое значение
        # и сохранить его в объекте StringVar. В результате
        # виджет self.output_text будет автоматически обновлен.
        self.value.set(coordinates)

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
        coordinates = (f'{name},{X2:.3f},{Y2:.3f},{high},')

        # Конвертировать координаты в строковое значение
        # и сохранить его в объекте StringVar. В результате
        # виджет self.output_text будет автоматически обновлен.
        self.value.set(coordinates)

    def choice(self):
        # Получить значение radiobutton.
        position = self.radio_var.get()
        
        if (position == 1):
            self.convert_ekb_msk()

        elif (position == 2):
            self.convert_msk_ekb()

    def click_about(self):
        tkinter.messagebox.showinfo("О программе", "Версия 0.1                                                                            "
                                    "Разработка: WildRoger.                                                          "
                                    "Контакт для связи: mx.sverre@gmail.com")
        
    def click_bobr(self):
        tkinter.messagebox.showinfo("Bóbr", "Bóbr kurwa!")

    def reference(self):
        tkinter.messagebox.showinfo("Справка", 'Для пересчёта координат, нажать кнопку "Рассчитать".    ' 
                                    'Для выбора системы координат переключить кнопку в поле "Пересчёт координат:".                                           '
                                    'Кнопка "Открыть файл" позволяет загрузить файл с координатами с целью добавления в него новых строк. ' 
                                    'Кнопка "Сохранить файл" сохраняет результаты в новый файл.                                                                                             ' 
                                    'Кнопка "Сохранить в текущий файл", добавляет строку с результатами в конец загруженного файла. ')

    # Открываем файл.
    def open_file(self):
        self.filepath = tkinter.filedialog.askopenfilename()
        if self.filepath != "":
            tkinter.messagebox.showinfo("Информация", "Файл загружен.")

    # Cохраняем текст из текстового поля в новый файл.
    def save_file(self):
        self.filepath = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",initialfile = "Новый текстовый документ",title = "Select file",filetypes = (("Текстовые документы (*.txt)","*.txt"),("Все файлы","*.*")))
        if self.filepath != "":
            text = (self.output_text.get() + '\n')
            with open(self.filepath, 'a') as file:
                file.write(text)
                tkinter.messagebox.showinfo("Информация", "Файл сохранен.")

    # Cохраняем текст из текстового поля в последнюю строку загруженного файла.
    def save_file_add(self):
        if self._ilepath != "":
            text = (self.output_text.get() + '\n')
            with open(self.filepath, 'a') as file:
                file.write(text)
                tkinter.messagebox.showinfo("Информация", "Файл сохранён с результатами вычислений.")

# Создать экземпляр класса ScConverterGUI.
if __name__ == '__main__':
    sc_conv = ScConverterGUI()