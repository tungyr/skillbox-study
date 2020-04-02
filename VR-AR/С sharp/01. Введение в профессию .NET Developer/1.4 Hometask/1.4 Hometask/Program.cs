using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Homework_01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("\t-=Задание 1=-\n");

            // Создание базы данных из 20 сотрудников для Задания 1
            Repository repository = new Repository(20);

            // Печать в консоль всех сотрудников для Задания 1
            repository.Print("База данных до преобразования");

            Console.WriteLine("\t-=Задание 2=-\n");

            // Создание базы данных из 40 сотрудников для Задания 2
            Repository repository_two = new Repository(40);

            // Печать в консоль всех сотрудников для Задания 2
            repository_two.Print("База данных до удаления 10 сотрудников");

            while (repository_two.Workers.Count >= 30)
            {
                repository_two.DeleteRandomWorker();
            }

            // Печать в консоль отдел, в котором менее 30 сотрудников
            repository_two.Print("База данных после увольнения 10 сотрудников");

            Console.WriteLine("\t-=Задание 3=-\n");

            // Создание базы данных из 50 сотрудников для Задания 3
            Repository repository_three = new Repository(50);

            // Печать в консоль всех сотрудников для Задания 3
            repository_three.Print("База данных до увольнения всех с зп более 30000руб");

            // Увольнение всех работников с зарплатой выше 30000
            repository_three.DeleteWorkerBySalary(30000);

            // Печать в консоль отдел, в котором у всех сотрудников зарплата менее 30000руб
            repository_three.Print("База данных после увольнения всех с зп более 30000руб");
            Console.ReadKey();

            #region Домашнее задание

            // Уровень сложности: просто
            // Задание 1. Переделать программу так, чтобы до первой волны увольнени в отделе было не более 20 сотрудников

            // Уровень сложности: средняя сложность
            // * Задание 2. Создать отдел из 40 сотрудников и реализовать несколько увольнений, по результатам
            //              которых в отделе болжно остаться не более 30 работников

            // Уровень сложности: сложно
            // ** Задание 3. Создать отдел из 50 сотрудников и реализовать увольнение работников
            //               чья зарплата превышает 30000руб



            #endregion

        }
    }
}
