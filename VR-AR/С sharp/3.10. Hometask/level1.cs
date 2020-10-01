using System;
using System.Collections.Generic;
using System.Text;
using static System.Console;

namespace _3._10._Hometask
{
    class level1
    {
        static void level_one(string[] args)
        {
            // Написать игру, в которою могут играть два игрока.
            // При старте, игрокам предлагается ввести свои никнеймы.
            // Никнеймы хранятся до конца игры.
            // Программа загадывает случайное число gameNumber от 12 до 120 сообщая это число игрокам.
            // Игроки ходят по очереди(игра сообщает о ходе текущего игрока)
            // Игрок, ход которого указан вводит число userTry, которое может принимать значения 1, 2, 3 или 4,
            // введенное число вычитается из gameNumber
            // Новое значение gameNumber показывается игрокам на экране.
            // Выигрывает тот игрок, после чьего хода gameNumber обратилась в ноль.
            // Игра поздравляет победителя, предлагая сыграть реванш

            //*Бонус:
            // Подумать над возможностью реализации разных уровней сложности.
            // В качестве уровней сложности может выступать настраиваемое, в начале игры,
            // значение userTry, изменение диапазона gameNumber, или указание большего количества игроков (3, 4, 5...)


            string turn;
            Write("Никнейм первого игрока:");
            string first_player = turn = ReadLine();
            Write("Никнейм второго игрока:");
            string second_player = ReadLine();
            Random rand = new Random();
            int gameNumber = rand.Next(12, 120);
            int counter = 1;
            bool playing = true;


            do
            {
                WriteLine($"Загаданное число {gameNumber}");
                if (counter % 2 == 1)
                {
                    turn = first_player;
                }
                else
                {
                    turn = second_player;
                }
                WriteLine($"Ход игрока {turn}");

                int userTry = Convert.ToInt32(ReadLine());

                if (userTry > 4)
                {
                    WriteLine("Ошибка! Число не должно быть больше 4!");
                    continue;
                }
                else
                {
                    gameNumber -= userTry;
                    counter++;
                }

                if (gameNumber < 0)
                {
                    WriteLine($"Победитель - {turn}");
                    WriteLine("Сыграть еще? д/н");
                    string reply = ReadLine();
                    if (reply == "д")
                    {
                        playing = false;
                    }
                    else
                    {
                        gameNumber = rand.Next(12, 120);
                        continue;
                    }
                }

            } while (playing);




        }
    }
}
