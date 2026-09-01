# Импортируем нужные компоненты из Kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Импортируем модуль time для работы со временем
import time

class MyApp(App):
    def build(self):
        # Создаем вертикальный контейнер для элементов
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # --- СОЗДАЕМ ЭЛЕМЕНТЫ ИНТЕРФЕЙСА ---
        
        # Метка для отображения текущего времени в миллисекундах
        self.time_label = Label(text='0.000 с', font_size=40)
        
        # Кнопка "Пуск"
        self.start_button = Button(text='ПУСК', font_size=30)
        # При нажатии вызываем метод start_click
        self.start_button.bind(on_press=self.start_click)
        
        # Кнопка "Запись"
        self.record_button = Button(text='ЗАПИСЬ', font_size=30)
        # При нажатии вызываем метод record_click
        self.record_button.bind(on_press=self.record_click)
        
        # --- ДОБАВЛЯЕМ ЭЛЕМЕНТЫ В КОНТЕЙНЕР ---
        layout.add_widget(self.time_label)
        layout.add_widget(self.start_button)
        layout.add_widget(self.record_button)
        
        # --- ИНИЦИАЛИЗИРУЕМ ПЕРЕМЕННЫЕ ---
        self.start_time = None          # Время первого запуска таймера
        self.timer_running = False      # Флаг: запущен ли таймер
        self.time_stack = []            # Стек (список) для хранения моментов времени
        self.current_time = 0.0         # Текущее время в миллисекундах
        self.update_event = None        # Событие для обновления времени
        
        # Запускаем обновление времени (таймер)
        self.update_time()
        
        return layout
    
    def start_click(self, instance):
        """
        Метод, вызываемый при нажатии кнопки "Пуск".
        Записывает текущий момент времени в стек.
        """
        # Получаем текущее время в секундах (с дробной частью)
        current_time_sec = time.time()
        print ("cur", current_time_sec)
        # Если таймер еще не запущен (первое нажатие) - запоминаем время старта
        if self.start_time is None:
            self.start_time = current_time_sec
            self.timer_running = True
            print("Таймер запущен!")
        
        # Вычисляем время, прошедшее с момента первого нажатия
        elapsed_time = current_time_sec - self.start_time
        
        # Переводим в миллисекунды и сохраняем в стек
        elapsed_ms = elapsed_time * 1000
        self.time_stack.append(elapsed_ms)
        
        # Выводим в терминал для отладки
        print(f"Добавлен момент времени: {elapsed_ms:.0f} мс")
        print(f"Всего записей в стеке: {len(self.time_stack)}")
    
    def record_click(self, instance):
        """
        Метод, вызываемый при нажатии кнопки "Запись".
        Записывает все моменты времени из стека в файл.
        """
        # Проверяем, есть ли что записывать
        if len(self.time_stack) == 0:
            print("Нет данных для записи! Стек пуст.")
            return
        
        # Создаем имя файла с текущей датой и временем
        filename = f"запись_{int(time.time())}.txt"
        
        try:
            # Открываем файл для записи (создаем новый или перезаписываем существующий)
            # 'w' - запись (write), 'encoding='utf-8'' - для поддержки русских букв
            with open(filename, 'w', encoding='utf-8') as file:
                # Записываем заголовок
                file.write("Время в миллисекундах\n")
                file.write("=" * 25 + "\n")
                
                # Проходим по всем значениям в стеке и записываем каждое в отдельной строке
                for time_value in self.time_stack:
                    # Форматируем: целое число без десятичных знаков
                    file.write(f"{time_value:.0f}\n")
                
                # Записываем итоговую информацию
                file.write("=" * 25 + "\n")
                file.write(f"Всего записей: {len(self.time_stack)}\n")
            
            # Сообщаем об успешной записи
            print(f"Файл '{filename}' успешно создан!")
            print(f"Записано {len(self.time_stack)} значений")
            
            # Очищаем стек после записи (по желанию)
            # self.time_stack.clear()
            
        except Exception as e:
            # Если произошла ошибка (например, нет прав на запись)
            print(f"Ошибка при записи файла: {e}")
    
    def update_time(self, dt=None):
        """
        Метод для обновления времени на экране.
        Вызывается каждые 0.05 секунды.
        """
        if self.timer_running and self.start_time is not None:
            # Если таймер запущен - вычисляем текущее время
            current_time_sec = time.time()
            elapsed_time = current_time_sec - self.start_time
            elapsed_ms = elapsed_time * 1000
            self.current_time = elapsed_ms
            
            # Обновляем текст на экране (3 знака после запятой)
            self.time_label.text = f'{elapsed_ms:.3f} мс'
        else:
            # Если таймер не запущен - показываем 0
            self.time_label.text = '0.000 мс'
        
        # Планируем следующий вызов этого же метода через 0.05 секунды
        # Clock.schedule_once планирует однократный вызов функции
        from kivy.clock import Clock
        Clock.schedule_once(self.update_time, 0.05)

# Запуск приложения
if __name__ == '__main__':
    MyApp().run()