using System;
using Newtonsoft.Json;
namespace MatematikoCountScores
{
    public static class ResultCounter
    {
        const string INLINE = "INLINE"; //для передачи в качестве параметра string Placing в CheckConditions
        const string BIAS = "BIAS"; //для передачи в качестве параметра string Placing в CheckConditions

        /// <summary>
        /// 
        /// </summary>
        /// <param name="Field">Field reshaped to 1D shape (field_lgh*field_lgth,)</param>
        /// <returns>JSON string with results</returns>
        public static string CountResults(int[] Field, int field_lgth)
        {
            var Field2D = ReshapeField(Field, field_lgth);
            Results result = new Results();
            /* Подсчитывает результаты для игрока */
            int[] NumsRepetitions = new int[13];
            for (int i = 0; i < 13; i++)
            {
                NumsRepetitions[i] = 0;
            }

            /* ПРОВЕРЯЕМ СТРОКИ */
            for (int row = 0; row < field_lgth; row++)
            {
                for (int column = 0; column < field_lgth; column++)
                {
                    ++NumsRepetitions[Field2D[row, column] - 1];
                }
                CheckConditions(NumsRepetitions, ref result, INLINE);
                /* очищаем массив NumsRepetitions */
                for (int i = 0; i < 13; i++)
                {
                    NumsRepetitions[i] = 0;
                }
            }
            /* ПРОВЕРЯЕМ СТОЛБЦЫ */
            for (int column = 0; column < field_lgth; column++)
            {
                for (int row = 0; row < field_lgth; row++)
                {
                    ++NumsRepetitions[Field2D[row, column] - 1];
                }
                CheckConditions(NumsRepetitions, ref result, INLINE);
                /* очищаем массив NumsRepetitions*/
                for (int i = 0; i < 13; i++)
                {
                    NumsRepetitions[i] = 0;
                }
            }
            /* ПРОВЕРЯЕМ ДИАГОНАЛИ в направлении от верхнего левого к нижнему правому углу (главная и параллельно ей) */
            //главная диагональ и ниже
            for (int row = 0; row < field_lgth - 1; row++)
            {
                int i = row;
                int j = 0;
                //цикл while - проход одной диагонали
                while (i < field_lgth && j < field_lgth)
                {
                    ++NumsRepetitions[Field2D[i, j]];
                    ++i;
                    ++j;
                }

                CheckConditions(NumsRepetitions, ref result, BIAS);
                /* очищаем массив NumsRepetitions*/
                for (int k = 0; k < 13; k++)
                {
                    NumsRepetitions[k] = 0;
                }
            }
            //выше главной диагонали
            for (int column = 1; column < field_lgth - 1; column++)
            {
                int i = 0;
                int j = column;
                //цикл while - проход одной диагонали
                while (i < field_lgth && j < field_lgth)
                {
                    ++NumsRepetitions[Field2D[i, j]];
                    ++i;
                    ++j;
                }

                CheckConditions(NumsRepetitions, ref result, BIAS);
                /* очищаем массив NumsRepetitions*/
                for (int k = 0; k < 13; k++)
                {
                    NumsRepetitions[k] = 0;
                }
            }
            /* ПРОВЕРЯЕМ ДИАГОНАЛИ побочную и параллельные ей*/
            //побочная и выше ее
            for (int column = 1; column < field_lgth; column++)
            {
                int i = 0;
                int j = column;
                //цикл while - проход одной диагонали
                while (i < field_lgth && j >= 0)
                {
                    ++NumsRepetitions[Field2D[i, j]];
                    ++i;
                    --j;
                }

                CheckConditions(NumsRepetitions, ref result, BIAS);
                /* очищаем массив NumsRepetitions*/
                for (int k = 0; k < 13; k++)
                {
                    NumsRepetitions[k] = 0;
                }
            }
            //ниже побочной
            for (int row = 1; row < field_lgth - 1; row++)
            {
                int i = row;
                int j = field_lgth - 1;
                //цикл while - проход одной диагонали
                while (i < field_lgth && j >= 0)
                {
                    ++NumsRepetitions[Field2D[i, j]];
                    ++i;
                    --j;
                }

                CheckConditions(NumsRepetitions, ref result, BIAS);
                /* очищаем массив NumsRepetitions*/
                for (int k = 0; k < 13; k++)
                {
                    NumsRepetitions[k] = 0;
                }
            }
            //конец проверки 
            //Считаем сумму очков
            result.Sum = result.INLINE_2EqNums * Scores.INLINE_2EqNums + result.INLINE_3EqNums * Scores.INLINE_3EqNums +
                result.INLINE_4EqNums * Scores.INLINE_4EqNums + result.INLINE_2PairsOfEqNums * Scores.INLINE_2PairsOfEqNums +
                result.INLINE_3EqNums_plus_2EqNums * Scores.INLINE_3EqNums_plus_2EqNums + result.INLINE_5ConsecutiveNums * Scores.INLINE_5ConsecutiveNums +
                result.INLINE_Three_1_Two_13 * Scores.INLINE_Three_1_Two_13 + result.INLINE_1_10_11_12_13 * Scores.INLINE_1_10_11_12_13 +
                result.INLINE_4Ones * Scores.INLINE_4Ones;
            result.Sum += result.BIAS_2EqNums * Scores.BIAS_2EqNums + result.BIAS_3EqNums * Scores.BIAS_3EqNums + result.BIAS_4EqNums * Scores.BIAS_4EqNums +
                result.BIAS_2PairsOfEqNums * Scores.BIAS_2PairsOfEqNums + result.BIAS_3EqNums_plus_2EqNums * Scores.BIAS_3EqNums_plus_2EqNums +
                result.BIAS_5ConsecutiveNums * Scores.BIAS_5ConsecutiveNums + result.BIAS_Three_1_Two_13 * Scores.BIAS_Three_1_Two_13 +
                result.BIAS_1_10_11_12_13 * Scores.BIAS_1_10_11_12_13 + result.BIAS_4Ones * Scores.BIAS_4Ones;           
     
            return JsonConvert.SerializeObject(result);
        }

        private static void CheckConditions(int[] NumsRepetitions, ref Results result, string Placing)
        {
            bool HasTwoEqNums = false; //встречалась ли пара одинаковых числе в этой строке/стб/диаг?
            bool HasThreeEqNums = false; //встречалась ли тройка одинаковых числе в этой строке/стб/диаг? 
            byte ConsecutiveNums_count = 0;
            //ДЛЯ СТРОК ИЛИ СТОЛБЦОВ (Placing == INLINE)
            if (Placing == INLINE)
            {
                /* Проходим по заполненному NumsRepetitions, проверяем условия */
                for (int i = 0; i < 13; i++)
                {
                    // стоит ли в ряду последовательных чисел?
                    if (NumsRepetitions[i] != 0)
                    {
                        ++ConsecutiveNums_count;
                        if (ConsecutiveNums_count == 5)
                            ++result.INLINE_5ConsecutiveNums;
                    }
                    else ConsecutiveNums_count = 0;
                    //число повторилось в строке дважды
                    if (NumsRepetitions[i] == 2)
                    {
                        if (HasTwoEqNums == true)
                        {
                            ++result.INLINE_2PairsOfEqNums;
                            --result.INLINE_2EqNums;
                            continue;
                        }
                        if (HasThreeEqNums == true)
                        {
                            ++result.INLINE_3EqNums_plus_2EqNums;
                            --result.INLINE_3EqNums;
                            continue;
                        }
                        HasTwoEqNums = true;
                        ++result.INLINE_2EqNums;
                        continue;
                    }
                    //число повторилось в строке трижды
                    if (NumsRepetitions[i] == 3)
                    {
                        if (HasTwoEqNums == true)
                        {
                            ++result.INLINE_3EqNums_plus_2EqNums;
                            --result.INLINE_2EqNums;
                            continue;
                        }
                        HasThreeEqNums = true;
                        ++result.INLINE_3EqNums;
                        continue;
                    }
                    //число повторилось в строке четырежды
                    if (NumsRepetitions[i] == 4)
                    {
                        if (i == 0)
                        {
                            ++result.INLINE_4Ones;
                        }
                        else
                            ++result.INLINE_4EqNums;
                    }
                }
                // проверяем условия, не требующие прохода всего NumsRepetitions
                // 3 единицы + 2 "13" 
                if (NumsRepetitions[0] == 3 && NumsRepetitions[12] == 2)
                {
                    ++result.INLINE_Three_1_Two_13;
                }
                //"1", "10", "11", "12", "13" 
                if (NumsRepetitions[0] != 0 && NumsRepetitions[9] != 0 && NumsRepetitions[10] != 0
                    && NumsRepetitions[11] != 0 && NumsRepetitions[12] != 0)
                {
                    ++result.INLINE_1_10_11_12_13;
                }
            }

            //ДЛЯ ДИАГОНАЛЕЙ
            if (Placing == BIAS)
            {
                /* Проходим по заполненному NumsRepetitions, проверяем условия */
                for (int i = 0; i < 13; i++)
                {
                    // стоит ли в ряду последовательных чисел?
                    if (NumsRepetitions[i] != 0)
                    {
                        ++ConsecutiveNums_count;
                        if (ConsecutiveNums_count == 5)
                            ++result.BIAS_5ConsecutiveNums;
                    }
                    else ConsecutiveNums_count = 0;
                    //число повторилось в строке дважды
                    if (NumsRepetitions[i] == 2)
                    {
                        if (HasTwoEqNums == true)
                        {
                            ++result.BIAS_2PairsOfEqNums;
                            --result.BIAS_2EqNums;
                            continue;
                        }
                        if (HasThreeEqNums == true)
                        {
                            ++result.BIAS_3EqNums_plus_2EqNums;
                            --result.BIAS_3EqNums;
                            continue;
                        }
                        HasTwoEqNums = true;
                        ++result.BIAS_2EqNums;
                        continue;
                    }
                    //число повторилось в строке трижды
                    if (NumsRepetitions[i] == 3)
                    {
                        if (HasTwoEqNums == true)
                        {
                            ++result.BIAS_3EqNums_plus_2EqNums;
                            --result.BIAS_2EqNums;
                            continue;
                        }
                        HasThreeEqNums = true;
                        ++result.BIAS_3EqNums;
                        continue;
                    }
                    //число повторилось в строке четырежды
                    if (NumsRepetitions[i] == 4)
                    {
                        if (i == 0)
                        {
                            ++result.BIAS_4Ones;
                        }
                        else
                            ++result.BIAS_4EqNums;
                    }
                }
                // проверяем условия, не требующие прохода всего NumsRepetitions
                // 3 единицы + 2 "13" 
                if (NumsRepetitions[0] == 3 && NumsRepetitions[12] == 2)
                {
                    ++result.BIAS_Three_1_Two_13;
                }
                //"1", "10", "11", "12", "13" 
                if (NumsRepetitions[0] != 0 && NumsRepetitions[9] != 0 && NumsRepetitions[10] != 0
                    && NumsRepetitions[11] != 0 && NumsRepetitions[12] != 0)
                {
                    ++result.BIAS_1_10_11_12_13;
                }
            }
        }

        private static int[,] ReshapeField(int[] field, int field_lgth)
        {
            int[,] result = new int[field_lgth, field_lgth];
            for (int i=0; i<field_lgth; i++)
            {
                for(int j=0; j<field_lgth; j++)
                {
                    result[i, j] = field[i * field_lgth + j];
                }
            }
            return result;
        }
    }

    
    internal struct Results
    {
        /* Описывает результаты игры для одного игрока */        
        public int Sum; //Сумма очков
        /* По каким пунктам были набраны очки; сколько раз в каждом пункте */
        //в строке или столбце        
        public int INLINE_2EqNums; //2 одинаковых числа        
        public int INLINE_3EqNums; //3 одинаковых числа
        public int INLINE_4EqNums; //4 одинаковых числа
        public int INLINE_2PairsOfEqNums; // 2 пары одинаковых чисел
        public int INLINE_3EqNums_plus_2EqNums; //3+2 одинаковых чисел
        public int INLINE_5ConsecutiveNums; //5 послед.чисел в любом порядке
        public int INLINE_Three_1_Two_13;//3 единицы, 2 "13"
        public int INLINE_1_10_11_12_13; //"1", "10", "11", "12", "13" в любом порядке
        public int INLINE_4Ones; // четыре единицы
        //по диагонали
        public int BIAS_2EqNums; //2 одинаковых числа
        public int BIAS_3EqNums; //3 одинаковых числа
        public int BIAS_4EqNums; //4 одинаковых числа
        public int BIAS_2PairsOfEqNums; // 2 пары одинаковых чисел
        public int BIAS_3EqNums_plus_2EqNums; //3+2 одинаковых чисел
        public int BIAS_5ConsecutiveNums; //5 послед.чисел в любом порядке
        public int BIAS_Three_1_Two_13;//3 единицы, 2 "13"
        public int BIAS_1_10_11_12_13; //"1", "10", "11", "12", "13" в любом порядке
        public int BIAS_4Ones; // четыре единицы        
    }

    internal struct Scores
    {
        /* Кол-во очков, дающихся за выолнение каждого условия */
        public const int INLINE_2EqNums = 10; //2 одинаковых числа
        public const int INLINE_3EqNums = 40; //3 одинаковых числа
        public const int INLINE_4EqNums = 160; //4 одинаковых числа
        public const int INLINE_2PairsOfEqNums = 20; // 2 пары одинаковых чисел
        public const int INLINE_3EqNums_plus_2EqNums = 80; //3+2 одинаковых чисел
        public const int INLINE_5ConsecutiveNums = 50; //5 послед.чисел в любом порядке
        public const int INLINE_Three_1_Two_13 = 100;//3 единицы, 2 "13"
        public const int INLINE_1_10_11_12_13 = 150; //"1", "10", "11", "12", "13" в любом порядке
        public const int INLINE_4Ones = 200; // четыре единицы
        //по диагонали
        public const int BIAS_2EqNums = 20; //2 одинаковых числа
        public const int BIAS_3EqNums = 50; //3 одинаковых числа
        public const int BIAS_4EqNums = 170; //4 одинаковых числа
        public const int BIAS_2PairsOfEqNums = 30; // 2 пары одинаковых чисел
        public const int BIAS_3EqNums_plus_2EqNums = 90; //3+2 одинаковых чисел
        public const int BIAS_5ConsecutiveNums = 60; //5 послед.чисел в любом порядке
        public const int BIAS_Three_1_Two_13 = 110;//3 единицы, 2 "13"
        public const int BIAS_1_10_11_12_13 = 160; //"1", "10", "11", "12", "13" в любом порядке
        public const int BIAS_4Ones = 210; // четыре единицы
    }
}
