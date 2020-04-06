using System;
using System.Collections.Generic;
using System.Text;

namespace _2._7_Hometask
{
    public class user_notes
    {

        // Переменная список для хранения заметок
        public static List<string> notes = new List<string>();

        // Переменная список для хранения пунктов меню заметок
        public static List<string> notes_menu = new List<string>(new string[]
        {
        "Заметки пользователя:",
        $"{Program.separator}",
        "1. Посмотреть заметки",
        "2. Добавить заметку",
        "3. Вернуться в главное меню",
        $"{Program.separator}",
        "Введите пункт меню:"
        });

        public static void user_notes_main()
        {
            //Проверка изменения размера окна консоли
            if (Console.WindowHeight / 2 != Program.win_height || Console.WindowWidth != Program.win_width)
            {
                Program.win_height = Console.WindowHeight / 2;
                Program.win_width = Console.WindowWidth / 2;
            }

            while (true)
            {

                Console.Clear();
                // Вывод главного меню заметок
                int row_number = 0;

                foreach (var item in notes_menu)
                {
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                    Console.WriteLine(item);
                    row_number++;
                }

                Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                int choice = int.Parse(Console.ReadLine());
                row_number = 0;

                ///Вывод заметок
                if (choice == 1)
                {
                    ///Проверка наличия заметок в списке и вывод сообщения об их отсутсвии в центре консоли
                    Console.Clear();
                    if (notes.Count == 0)
                    {
                        
                        Console.SetCursorPosition((Program.win_width - ("Заметки пусты!".Length / 2)), Program.win_height - 3);
                        Console.WriteLine("Заметки пусты!");
                        Console.SetCursorPosition((Program.win_width - ("Чтобы вернуться назад нажмите Ввод".Length / 2)), Program.win_height);
                        Console.WriteLine("Чтобы вернуться назад нажмите Ввод");
                        if (Console.ReadKey().KeyChar == 13)
                        {
                            continue;
                        }
                    }
                
                    else
                    {
                        foreach (var note in notes)
                        {
                            Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3 + row_number);
                            Console.WriteLine(row_number + 1 + ". " + note);
                            // Проверка длины заметки
                            if (note.Length > Program.win_width)
                            {
                                row_number = note.Length / Program.win_width;
                                row_number++;
                            }
                            row_number++;
                        }
                        Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 2 + row_number);
                        Console.WriteLine("Чтобы вернуться назад нажмите Ввод");
                        if (Console.ReadKey().KeyChar == 13)
                        {
                            continue;
                        }

                    }
                }



                // Внесение заметок
                if (choice == 2)
                {
                    Console.Clear();

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 3);
                    Console.WriteLine("Введите заметку: ");
                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height - 2);
                    string new_note = Console.ReadLine();
                    notes.Add(new_note);

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height + new_note.Length / Program.win_width);
                    Console.WriteLine("Заметка сохранена!");

                    Console.SetCursorPosition((Program.win_width - (Program.separator.Length / 2)), Program.win_height + new_note.Length / Program.win_width + 1);
                    Console.WriteLine("Чтобы вернуться назад нажмите Ввод");

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