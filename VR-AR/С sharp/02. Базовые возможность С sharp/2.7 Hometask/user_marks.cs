using System;
using System.Collections.Generic;
using System.Text;

namespace _2._7_Hometask
{
    public class user_marks
    {
        // Переменные с данными успеваемости пользователя
        public static double history_mark = 0;
        public static double math_mark = 0;
        public static double russian_lang_mark = 0;
        public static double average_mark = 0;

        // Список с данными успеваемости пользователя
        public static List<double> user_marks_list = new List<double>(new double[]
            {
            history_mark,
            math_mark,
            russian_lang_mark,
            average_mark,
            });

        // Список названий предметов
        public static List<string> user_marks_labels_list = new List<string>(new string[]
           {
            "История: ",
            $"Математика: ",
            $"Русский язык: ",
            $"Средний балл: "
    });

	
        
        // Переменная список для хранения пунктов меню успеваемости пользователя
        public static List<string> user_marks_menu = new List<string>(new string[]
        {"Данные об успеваемости:",
        $"{Program.separator}",
        "1. Посмотреть данные",
        "2. Изменить данные",
        "3. Вернуться в главное меню",
        $"{Program.separator}",
        "Введите пункт меню:"});

        public static void user_marks_main()
        {

            while (true)
            {
                //Проверка изменения размера окна консоли
                if (Console.WindowHeight / 2 != Program.win_height || Console.WindowWidth != Program.win_width)
                {
                    Program.win_height = Console.WindowHeight / 2;
                    Program.win_width = Console.WindowWidth / 2;
                }

                string pattern_marks = "Введенные оценки: История: {0}; Математика: {1}; Русский язык: {2}; Средний балл: {3}";

                int row_number = 0;

                Console.Clear();

                foreach (var item in user_marks_menu)
                {
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                    Console.WriteLine(item);
                    row_number++;
                }

                Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                int choice = int.Parse(Console.ReadLine());

                if (choice == 1)
                {
                    
                    ///Вывод в центр консоли данных об успеваемости пользователя
                    row_number = 0;

                    Console.Clear();
                    foreach (var label in user_marks_labels_list)
                    {
                        Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                        Console.WriteLine(label + user_marks_list[row_number].ToString("#.#"));
                        row_number++;
                    }

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 2 + row_number);
                    Console.WriteLine("Чтобы вернуться назад нажмите Ввод");
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 1 + row_number);
                    if (Console.ReadKey().KeyChar == 13)
                    {
                       continue;
                    }
       
                }

                if (choice == 2)
                {
                    ///Ввод новых данных по успеваемости
                    Console.Clear();

                    row_number = 0;
                    while (row_number < 3)
                    {
                        Console.Clear();
                        Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3);
                        Console.WriteLine("Введите новое значение: " + user_marks_labels_list[row_number]);
                        Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + 1);
                        user_marks_list[row_number] = double.Parse(Console.ReadLine());
                        row_number++;

                    }

                    // Вычисление среднего балла
                    average_mark = (user_marks_list[0] + user_marks_list[1] + user_marks_list[2]) / 3;
                    user_marks_list[3] = average_mark;

                    Console.Clear();
                    Console.SetCursorPosition((Program.win_width - (pattern_marks.Length / 2)), Program.win_height - 3);
                    Console.WriteLine(pattern_marks, user_marks_list[0], user_marks_list[1], user_marks_list[2], average_mark.ToString("#.#"));

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 2);
                    Console.WriteLine("Чтобы вернуться назад нажмите Ввод");

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 1);
                    if (Console.ReadKey().KeyChar == 13)
                    {
                        continue;
                    }
                }

                else
                {
                    Program.Main();
                    break;
                }
            }
        }
    }
}
