using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MatematikoCountScores;

namespace CountScoresTestProject
{

    class MainClass
    {
        static Stack<int> InitializeCards(int field_len, int max_val=13)
        {
            var Cards = new Stack<int>();
            /*  Заполняет стек из 25 карточек случайными числами от 1 до 13 
             * (каждое повторяется не более 4х раз) */
            byte[] repetition_array = new byte[max_val]; //Массив, содержащий кол-во повторений одного числа в стеке
            /* Инициализируем "массив повторений" нулями */
            for (int i = 0; i < max_val; i++)
            {
                repetition_array[i] = 0;
            }
            Random rand = new Random((int)(DateTime.Now.Ticks));
            /* Записываем случайные числа от 1 до 13 в стек, проверяя кол-во повторений */
            int tmp;
            int count = 0;
            while (count != field_len*field_len)
            {
                tmp = rand.Next(1, max_val);
                if (repetition_array[tmp - 1] < 4)
                {
                    ++repetition_array[tmp - 1];
                    Cards.Push(tmp);
                    ++count;
                }
            }
            return Cards;
        }
        public static void Main()
        {
            const int field_lght = 5;
            var cards = InitializeCards(field_lght);
            int[] field = new int[field_lght * field_lght];
            //int[,] field = new int[field_lght, field_lght];
            for (int i = 0; i < field_lght * field_lght; i++)
            {
                field[i] = cards.Pop();
            }
            //for (int i=0; i<field_lght; i++)
            //{
            //    for (int j=0; j<field_lght; j++)
            //    {
            //        field[i, j] = cards.Pop();
            //    }
            //}
            var result = ResultCounter.CountResults(field, field_lght);
            Console.WriteLine(result);
        }

    }
}
