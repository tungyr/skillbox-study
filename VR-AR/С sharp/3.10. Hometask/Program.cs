using System;
using System.Collections.Generic;
using static System.Console;

namespace _3._10._Hometask
{
    class Program
    {
        static void Main(string[] args)
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

            List<string> players = new List<string> { };
            
            Write("Максимальный размер хода: ");
            int userTryMax = Convert.ToInt32(ReadLine());

            Write("Нижняя граница загадываемого числа: ");
            int min_gameNumber = Convert.ToInt32(ReadLine());

            Write("Верхняя граница загадываемого числа: ");
            int max_gameNumber = Convert.ToInt32(ReadLine());


            Random rand = new Random();
            int gameNumber = rand.Next(min_gameNumber, max_gameNumber + 1);
            string player;
            int counter = 0;
            bool playing = true;

            while (true)
            {
                Write("Введите имя игрока: ");
                player = ReadLine();
                players.Add(player);
                counter++;
                WriteLine($"Всего игроков:{counter}.\nЕще игрок? д/н: ");
                string reply = ReadLine();
                if (reply == "н" && counter == 1)
                {
                    Write("Всего один игрок! Хотите сыграть с компьютером?д/н: ");
                    if (ReadLine() == "д") ComputerGame.computer_game(player);
                    return;
                }
                else if (reply == "д")
                { 
                    continue;
                }
                else
                {
                    break;
                }
                    
            }

            counter = 0;

            do
            {
                WriteLine($"Загаданное число {gameNumber}");

                 player = players[counter];
         
                WriteLine($"Ход игрока {player}");

                int userTry = Convert.ToInt32(ReadLine());

                if (userTry > userTryMax)
                {
                    WriteLine($"Ошибка! Число не должно быть больше {userTryMax}!");
                    continue;
                }
                else
                {
                    gameNumber -= userTry;
                    counter++;
                }

                if (gameNumber < 0)
                { 
                    WriteLine($"Победитель - {player}");
                    WriteLine("Сыграть еще? д/н: ");
                    string reply = ReadLine();
                    if (reply == "н")
                    {
                        playing = false;
                    }
                    else
                    {
                        gameNumber = rand.Next(min_gameNumber, max_gameNumber + 1);
                        continue;
                    }
                }
                counter = (counter == players.Count) ? 0 : counter;

            } while (playing);

           


        }
    }
}
