using System;

class Program
{
    static void Main()
    {
        // Исходный массив строк
        string[] originalArray = { "hello", "2", "world", ":-)" };

        // Вывод исходного массива
        Console.WriteLine("Исходный массив:");
        foreach (var item in originalArray)
        {
            Console.WriteLine(item);
        }

        // Подсчет строк, длина которых меньше или равна 3 символам
        int count = 0;
        foreach (var item in originalArray)
        {
            if (item.Length <= 3) count++;
        }

        // Создание нового массива подходящего размера
        string[] newArray = new string[count];

        // Заполнение нового массива строками подходящей длины
        int index = 0;
        foreach (var item in originalArray)
        {
            if (item.Length <= 3)
            {
                newArray[index] = item;
                index++;
            }
        }

        // Вывод нового массива
        Console.WriteLine("\nНовый массив:");
        foreach (var item in newArray)
        {
            Console.WriteLine(item);
        }
    }
}
