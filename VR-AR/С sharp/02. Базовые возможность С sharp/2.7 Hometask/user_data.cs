﻿using System;
using System.Collections.Generic;
using System.Text;

namespace _2._7_Hometask
{
    public class user_data
    {
        // Переменные с именем, возрастом и ростом пользователя
        public static string name = "none";
        public static int age = 0;
        public static double height = 0;

        public static List<string> user_data_list = new List<string>(new string[] { });
        
        // Переменная список для хранения пунктов меню информации о пользователе
        public static List<string> user_data_menu = new List<string>(new string[]
        {"Данные пользователя:",
        $"{Program.separator}",
        "1. Посмотреть данные",
        "2. Изменить данные",
        "3. Вернуться в главное меню",
        $"{Program.separator}",
        "Введите пункт меню:"});



        public static void user_data_main()
        {
            while (true)
            {
                //Проверка изменения размера окна консоли
                if (Console.WindowHeight / 2 != Program.win_height || Console.WindowWidth != Program.win_width)
                {
                    Program.win_height = Console.WindowHeight / 2;
                    Program.win_width = Console.WindowWidth / 2;
                }

                Console.Clear();

                int row_number = 0;

                foreach (var item in user_data_menu)
                {
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                    Console.WriteLine(item);
                    row_number++;
                }

                Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                int choice = int.Parse(Console.ReadLine());

                if (choice == 1)
                {
                    ///Вывод в центр консоли данных о пользователе

                    row_number = 0;

                    Console.Clear();

                    //вывод имени

                    string word = "Имя: ";
                    name.Split(" ");
                    foreach (char letter in name)
                    {
                        if (Char.IsWhiteSpace(letter))
                        {
                            if (word.Length >= Program.separator.Length)
                            {
                                row_number++;
                                word += letter;
                                Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                                Console.WriteLine(word);
                                word = "";
                                continue;
                            }
                        }
                        word += letter;
                    }
                    // вывод последней части имени
                    row_number++;
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                    Console.WriteLine(word);
 
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 2 + row_number);
                    Console.WriteLine($"Возраст: {age,1}");
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 1 + row_number);
                    Console.WriteLine($"Рост: {height,4}");
                    

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height + row_number);
                    Console.WriteLine("Чтобы вернуться назад нажмите Ввод");
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height + row_number);
                    if (Console.ReadKey().KeyChar == 13)
                    {
                        user_data_list.Clear();
                        continue;
                    }
       
                }

                if (choice == 2)
                {
                    // Изменение данных пользователя
                    Console.Clear();
                    user_data_list.Add("Введите имя: ");
                    user_data_list.Add("Введите возраст: ");
                    user_data_list.Add("Введите рост: ");

                    
                    row_number = 0;
                    while (row_number < 3)
                    {
                        Console.Clear();
                        Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3);
                        Console.WriteLine(user_data_list[row_number]);
                        Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 2);
                        if (row_number == 0)
                        {
                            name = Console.ReadLine();
                        }
                        else if (row_number == 1)
                        {
                            age = int.Parse(Console.ReadLine());
                        }
                        else
                        {
                            height = double.Parse(Console.ReadLine());
                        }
                        row_number++;
                    }
                    
                    Console.Clear();                   
                    Console.SetCursorPosition((Program.win_width - 29), Program.win_height - 2);
                    Console.WriteLine("Новые данные введены. Чтобы вернуться назад нажмите Ввод");
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 1);
                    if (Console.ReadKey().KeyChar == 13)
                    {
                        user_data_list.Clear();
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
