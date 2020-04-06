using System;
using System.Collections.Generic;

namespace _2._7_Hometask
{
    class Program
    {
        
         // Переменные с оценками по предметам и переменная для хранения среднего балла
        public static double history_mark = 0;
        public static double math_mark = 0;
        public static double russian_lang_mark = 0;
        public static double average_mark = 0;

        // Строковый сепаратор для визуального разделения в консоли
        public static string separator = new string('=', 30);

        // Переменная список для хранения пунктов главного меню
        public static List<string> main_menu = new List<string>(new string[] 
        { "Приветствую! Это Ваша записная книжка!",
          "Mеню записной книжки:", 
          $"{separator}", 
          "1. Данные о пользователе", 
          "2. Данные об успеваемости", 
          "3. Заметки", 
          "4. Выйти из записной книжки", 
          $"{separator}", 
          "Введите пункт меню:",  });



        // Определение высоты и ширины окна консоли
        public static int win_height = Console.WindowHeight / 2;
        public static int win_width = Console.WindowWidth / 2;
        
        public static void Main()
        {
            //Проверка изменения размера окна консоли
            if (Console.WindowHeight / 2 != win_height || Console.WindowWidth != win_width)
            {
                win_height = Console.WindowHeight / 2;
                win_width = Console.WindowWidth / 2;
            }

            /* Бесконечный цикл для постоянной работы программы 
            пока пользователь не решит выйти*/
            while (true)
                {

                /// Основное меню записной книжки
                Console.Clear();
                int menu_string = 0;


                foreach (var item in main_menu)
                {
                    Console.SetCursorPosition((win_width - (separator.Length / 2)), win_height - 5 + menu_string);
                    Console.WriteLine(item);
                    menu_string++;
                }

                Console.SetCursorPosition((win_width - (separator.Length / 2)), win_height - 5 + menu_string);
                int choice = int.Parse(Console.ReadLine());

                /// Выбор пункта 1 запускает класс с отображением данных пользователя
                if (choice == 1)
                {
                    win_height = Console.WindowHeight / 2;
                    win_width = Console.WindowWidth / 2;
                    user_data.user_data_main();
                    break;
                }

                /// Выбор пункта 2 запускает класс с отображением данных по успеваемости пользователя
                else if (choice == 2)
                {
                    user_marks.user_marks_main();
                }

                /// Выбор пункта 3 запускает класс с отображением заметок пользователя
                else if (choice == 3)
                {
                    user_notes.user_notes_main();
                }

                /// Выбор пункта 4 или любой символ завершает программу
                else
                {
                    return;          
                }

            }


        }

    }
}
