# Задание 1
def twoSum(nums, target):
    '''
    Функция принимает в качестве аргументов список целочисленных значений nums и целое число target,
    возвращает два индекса, соответствующие тем элементам списка lst, которые в сумме дают target.
    Если таких индексов несколько, то необходимо вернуть список списков пар индексов.
    Если таких индексов нет, то необходимо вернуть пустой список.

    >>> twoSum([3, 3, 5, 8, 9], 6)
    [0, 1]

    >>> twoSum([1, 2, 3, 4, 5, 6, 7, 8], 11)
    [[2, 7], [3, 6], [4, 5]]

    >>> twoSum([-2, 5, 9, -7, 20], 100)
    []
    '''
    pass

    def twoSum(nums: list, target: int) -> list:
    seen = [] 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                seen.append([i, j])
    if len(seen) == 1:
        return seen [0]
    return seen

# Задание 2
class Complex:
    '''
    Класс Complex является интерфейсом для создания комплексных чисел, которые в математике 
    представленны в форме (re + img * j) или парой чисел (re, img), где re - действительная часть, img - мнимая.
    '''

    def __init__(self, re=0, img=0):

        '''
        Конструктор класса - метод, который вызывается при создании обьекта (эксземпляра) класса.
        Здесь требуется создать два атрибута уровня объекта, которые будут являтся действ. и мнимой частью вашего комплексного числа
        '''
        self.re = re
        self.img = img

    def __str__(self):
        '''
        Строковое отображение объектов класса.
        Данный метод должен возвращать строку, которая, например, отобразится при вызове функции 
        print с объектом класса в качестве аргумента

        >>> complex1 = Complex(3, 1)
        >>> print(complex1)
        3 + j

        >>> complex2 = Complex(10, -23)
        >>> print(complex2)
        10 - 23j
        '''
        Complex = ''
        Complex += str(self.re)
        if self.img != 0:
            if self.img > 0:
                Complex += ' + '
            else :
                Complex += ' - '
            if abs(self.img) != 1:
                Complex += str(abs(self.img))
            Complex += 'j'
        return Complex

    def __repr__(self):
        '''
        Вызывается встроенной функцией repr; возвращает "сырые" данные в виде строки, использующиеся для внутреннего представления в python.

        >>> complex1 = Complex(2, 3)
        >>> complex1
        Complex(2, 3)
        '''
        re, img = self.re, self.img
        if re == int(re):
            re = int(re)
        if img == int(img):
            img = int(img)
        return "Complex({}, {})".format(re, img)

    def __add__(self, other):
        '''
        Переопределение оператора '+'

        >>> complex1, complex2 = Complex(3, 1), Complex(5)
        >>> complex1 + complex2
        Complex(8, 1)
        >>> print(complex1 + complex2)
        8 + j

        >>> Complex(5, 2) + 1
        Complex(6, 2)

        >>> Complex(6, 1) + 5.1
        Complex(11.1, 1)

        >>> Complex(-7, -2) + "hello_raise"
        TypeError: unsupported operand type(s) for +: 'Complex' and 'str'
        '''
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.img + other.img)
        if isinstance(other, (int, float)):
            return Complex(self.re + other, self.img)
        raise TypeError: unsupported operand type(s) for +: 'Complex' and 'str'

    def __mul__(self, other):
        '''
        Переопределение оператора '*' 
        >>> Complex(3, 1) * Complex(10, 10)
        Complex(20, 40)

        >>> Complex(5, 10) * 2
        Complex(10, 20)

        >>> Complex(4, 4) * 2.5
        Complex(10, 10)

        >>> Complex(6, 7) * 'hello_raise'
        TypeError: unsupported operand type(s) for *: 'Complex' and 'str'
        '''
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.img * other.img, self.re * other.img + self.img * other.re)
        if isinstance(other, (int, float)):
            return Complex(self.re * other, self.img * other)
        raise TypeError: unsupported operand type(s) for *: 'Complex' and 'str'
    
    def __sub__(self, other):
        '''
        Переопределение оператора '-'
        >>> Complex(3, 1) - Complex(2, 4)
        Complex(1, -3)

        >>> Complex(3, 1) - 1.8
        Complex(1.2, 1)

        >>> Complex(3, 1) - 1
        Complex(2, 1)

        >>> Complex(6, 7) - 'hello_raise'
        TypeError: unsupported operand type(s) for -: 'Complex' and 'str'
        '''
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.img - other.img)
        if isinstance(other, (int, float)):
            return Complex(self.re - other, self.img)
        raise TypeError: unsupported operand type(s) for -: 'Complex' and 'str'

    def __truediv__(self, other):
        '''
        Переопределение оператора '/' 
        >>> Complex(3, 1) / Complex(2, 4)
        Complex(0.5, -0.5)

        >>> Complex(3, 1) / 2
        Complex(1.5, 0.5)

        >>> Complex(2, 4) / 2.5
        Complex(0.8, 1.6)

        >>> Complex(6, 7) / 'hello_raise'
        TypeError: unsupported operand type(s) for /: 'Complex' and 'str'
        '''
        if isinstance(other, Complex):
            d = other.re**2 + other.img**2
            return Complex((self.re * other.re + self.img * other.img) / d, (self.img * other.re - self.re*other.img) / d)
        if isinstance(other, (int, float)):
            return Complex(self.re / other, self.img / other)
        raise TypeError: unsupported operand type(s) for /: 'Complex' and 'str'

    def __abs__(self):
        '''
        Данный метод возвращает модуль комплексного числа
        >>> abs(Complex(3, 4))
        5.0
        '''
        return (self.re**2 + self.img**2)**(0.5)
