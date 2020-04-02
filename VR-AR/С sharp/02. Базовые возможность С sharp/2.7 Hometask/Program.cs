using System;

namespace _2._7_Hometask
{
    class Program
    {

        static void Main()
        {
                  

            while (true)
                {
                Console.WriteLine("Приветствую! Это Ваша записная книжка!\n");
                Console.WriteLine("Mеню записной книжки:\n" +
                    "1. Ввести данные о себе\n" +
                    "2. Ввести данные об успеваемости\n" +
                    "3. Ввести заметку\n" +
                    "4. Выйти из записной книжки (любая клавиша)\n");
                Console.WriteLine("Введите пункт меню:");

                int choice = int.Parse(Console.ReadLine());

                if (choice == 1)
                {
                    user_data();
                    break;
                }
                else if (choice == 2)
                {
                    user_marks();
                }
                else if (choice == 3)
                {
                    user_notes();
                }
                else
                {
                    return;
                }

            }

           

        }

        static void user_data()
        {
            while (true)
            { 
                Console.WriteLine("1. Изменить данные о себе\n" +
                                    "2. Вернуться в главное меню\n");
                Console.WriteLine("Введите пункт меню:");
                int choice = int.Parse(Console.ReadLine());

                if (choice == 1)
                {
                    Console.WriteLine("Введите имя:");
                    string name = Console.ReadLine();
                    Console.WriteLine("Введите возраст:");
                    int age = int.Parse(Console.ReadLine());
                    Console.WriteLine("Введите рост:");
                    double height = double.Parse(Console.ReadLine());

                    Console.WriteLine($"Введенные данные пользователя:\nИмя: {name} \nВозраст: {age} \nРост: {height}\n");
                    continue;
                }
   
                else
                {
                    Main();
                    break;
                }
            }


        }

        static void user_marks()
        {
            while (true)
            { 
            Console.WriteLine("1. Изменить данные об успеваемости\n" +
                                    "2. Вернуться в главное меню\n");
            Console.WriteLine("Введите пункт меню:");
            int choice = int.Parse(Console.ReadLine());


                if (choice == 1)
                {
                    Console.WriteLine("История: ");
                    double history_mark = double.Parse(Console.ReadLine());
                    Console.WriteLine("Математика:");
                    double math_mark = double.Parse(Console.ReadLine());
                    Console.WriteLine("Русский язык:");
                    double russian_lang_mark = double.Parse(Console.ReadLine());

                    double average_mark = (history_mark + math_mark + russian_lang_mark) / 3;

                    Console.WriteLine($"Введенные оценки:\nИстория: {history_mark} \nМатематика: {math_mark} \nРусский язык: {russian_lang_mark}\nСредний балл: {average_mark}");
                    continue;
                }
                else
                {
                    Main();
                    break;
                }
            }
        }


        static void user_notes()
        { }
    }
}
