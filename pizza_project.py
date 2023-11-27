import random
import click
import functools

def log(pattern):
    assert isinstance(pattern, str)
    def actual_decorator(func):
        @functools.wraps(func)
        def decor(*args, **kwargs):
            time_exec = random.randint(7, 20)
            print(f"{func.__name__} {pattern.format(time_exec)}")
            return func(*args, **kwargs)
        return decor
    return actual_decorator

class Pizza:

    pizza_recipes = {
        'Margherita': ['🧀', ['tomato sause', 'mozzarella', 'tomatoes']
                       ],
        'Peperroni': ['🍕', ['tomato sause', 'mozzarella', 'peperroni']
                      ],
        'Hawaiian': ['🍍', ['tomato sause', 'mozzarella', 'chicken', 'pineapples']
                     ]
    }

    def __init__(self, name, size, order_type='delivery'):
        """
        initializes all parameters of the pizza ordered
        """
        self.name = name
        if size not in ['S', 'M', 'L', 'XL']:
            raise ValueError("Invalid pizza size!")
        self.size = size
        self.bake_time, self.delivery_time = None, None
        self.pizza_dict()
        self.order_type = order_type

    def __call__(self):
        self.set_process()

    @log('👨‍🍳 Испекли за {} минут!')
    def bake(self):
        """Готовит пиццу"""

    @log('Отдали заказ за {} минут!')
    def give_away(self):
        """Самовывоз"""

    @log('🚗 Привезли заказ за {} минут!')
    def delivery(self):
        """Доставка"""
        self.delivery_time = random.randint(15, 60)

    def set_process(self) -> None:
        self.bake()
        if self.order_type == 'delivery':
            self.delivery()
        else:
            self.give_away()

    def pizza_dict(self) -> None:
        """
        method listing all the recipes of pizzas
        """
        print(f"Пицца {self.name} размера {self.size}.")
        print(f"Ингредиенты:")
        for i, component in enumerate(self.pizza_recipes[self.name][1]):
            print(f'{i}. {component}')
        print("----------------")

    def __eq__(self, other):
        """
        reinitizalize objects comparison
        :param other: another instance of Pizza class
        :return: True if objects are equal, False otherwise
        """
        if not isinstance(other, Pizza):
            raise TypeError("Invalid right operand type!")
        return self.size == other.size and self.name == other.name

@click.group()
def cli():
    pass


@cli.command()
def menu() -> None:
    """"""
    pizza_recipes = Pizza.pizza_recipes
    for pizza_name, descr in pizza_recipes.items():
        click.echo(f'{pizza_name} {descr[0]}:')
        for i, component in enumerate(descr[1]):
            click.echo(f'{i}. {component}')
        click.echo()


def simple_menu() -> None:
    """"""
    pizza_recipes = Pizza.pizza_recipes
    for pizza_name, descr in pizza_recipes.items():
        print(f'{pizza_name} {descr[0]}:')
        for i, component in enumerate(descr[1]):
            print(f'{i}. {component}')


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1, default='S', required=False)
def order(pizza: str, delivery: bool, size: str) -> None:
    """either """
    pizza = pizza.capitalize()
    if pizza not in Pizza.pizza_recipes:
        print("Пожалуйста, выберите пиццу из меню:")
        simple_menu()
    else:
        my_status = 'delivery' * delivery + 'in restaurant' * (not delivery)

        new_pizza = Pizza(pizza, size, order_type=my_status)
        new_pizza()

if __name__ == '__main__':
    cli()
