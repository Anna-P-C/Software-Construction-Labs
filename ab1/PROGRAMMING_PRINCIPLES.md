## Inheritance
Клас SmallHouse наслідує базовий клас House, що дозволяє перевикористовувати логіку розрахунку ціни та зберігання характеристик без дублювання коду.

[SmallHouse class](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L12-L15)

Використання super().__init__ для ініціалізації базового класу.

## Encapsulation

Для захисту цілісності даних використано приватні та захищені атрибути. Це обмежує можливість несанкціонованої зміни фінансового стану об'єкта або параметрів будинку ззовні.

Поля:
[Private attributes](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L27-L28)-атрибути __money та __house доступні лише всередині класу Human.

Методи:
[Private method __make_deal](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L40-L44)-внутрішня логіка проведення транзакції прихована від користувача.

## Single Responsibility Principle 

Кожен клас має одну чітко визначену сферу відповідальності:

[House class](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L1-L9)-відповідає лише за опис нерухомості та формулу розрахунку її вартості.

Human class — фокусується виключно на діях людини та управлінні власним бюджетом.

## DRY (Don't Repeat Yourself)

Логіка завершення покупки винесена в окремий метод __make_deal.

Метод покупки:
[buy_house](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L51-L57)

Метод угоди:
[__make_deal](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L40-L44)

Це дозволяє уникнути дублювання коду.

## KISS

Метод розрахунку фінальної ціни реалізований максимально прямолінійно.

[final_price](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L7-L9)-використовується проста математична формула без зайвих розгалужень та складних структур даних.

Код легко читається та підтримується.

## Code Smells

### Direct access to protected attributes

У методі info класу Human відбувається пряме звернення до захищених атрибутів класу House (_area та _price)

[info method](https://github.com/Anna-P-C/Software-Construction-Labs/blob/99cd951dd1bac0bf3c0076f817f6b1bef2b9f27a/ab1/house_project.py#L30-L33)

Це порушує принцип інкапсуляції, оскільки доступ відбувається напряму до внутрішніх атрибутів іншого класу.
