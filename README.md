# Python-Pro-Homeworks
Homeworks from Python Pro developer course from Prog Academy


Homework 01

1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.

2. Створіть клас ""Покупець"". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.

3. Створіть клас ""Замовлення"". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str() для коректного виведення інформації про це замовлення.


Homework 02

1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).

2. На його основі створіть клас Студент (перевизначте метод виведення інформації).

3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент. Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.  Визначте для Групи метод str() для повернення списку студентів у вигляді рядка."


Homework 03

1. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити від'ємну або нульову вартість товару викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів, викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).
Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.


Homework 04

1. Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям. Переконайтеся у працездатності проєктів.


Homework 05

1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота). Реалізуйте метод порівняння прямокутників за площею.
Також реалізуйте методи складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте).
Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).

2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.


Homework 06

1. Доповніть клас Група (завдання Лекції 2) можливістю підтримки ітераційного протоколу.

2. Модифікуєте клас Замовлення (завдання Лекції 1), додавши реалізацію протоколу послідовностей та ітераційного протоколу.


Homework 07

1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
 Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на завершення.
 
2. Реалізуйте свій аналог генераторної функції range().

3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.

4. Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.


Homework 08

1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача.
 Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовностю.
 Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
 
2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.

3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.


Homework 09

1. Створіть декоратор, який підраховуватиме, скільки разів була викликана функція, що декорується.

2. Створіть декоратор, який зареєструє декоровану функцію в списку функцій для обробки послідовності.

3. Припустимо, у класі визначено метод __str__, який повертає рядок виходячи з класу. Створіть такий декоратор для цього методу, щоб отриманий рядок зберігався у текстовий файл, ім'я якого збігається з ім'ям класу, метод якого ви прикрашали.

4. Створіть декоратор із параметрами для проведення хронометражу роботи тієї чи іншої функції. Параметрами повинні виступати те, скільки разів потрібно запустити функцію, що декорується, і в який файл зберегти результати хронометражу. Мета - провести хронометраж функції, що декорується."

5. Створіть декоратор, який зареєструє клас, що декорується, у списку класів.

6. Створіть декоратор класу із параметром. Параметром має бути рядок, який повинен дописуватися (ліворуч) до результату роботи методу __str__.

7. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які будуть його параметрами.


Homework 10

1. Створіть дескриптор, який робитиме поля класу керовані ним доступними лише читання.

2. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел. Тобто, якщо тому чи іншому полю спробувати присвоїти, наприклад, рядок, то має бути збуджений виняток.

3. Реалізуйте властивість класу, яка має наступне функціоналом: під час встановлення значення цієї властивості у файл із заздалегідь визначеною назвою повинен зберігатися час (коли встановлювали значення властивості) та встановлене значення.

4. Реалізуйте метаклас, який має наступний функціонал: при його використанні у файл із заздалегідь визначеною назвою потрібно зберегти ім'я класу та список його полів.

5. Створіть ABC клас із абстрактним методом перевірки цілого числа на простоту. Тобто якщо параметром цього методу є ціле число і воно просте, то метод повинен повернути True, а в іншому випадку False.

6. Створіть його клас наслідуючий.

7. Створіть клас, який не успадковує ABC клас, але володіє потрібним методом. Зареєструйте його як віртуальний підклас.

8. Перевірте працездатність проекту.
