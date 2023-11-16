import random
import click


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
        self.size = size
        self.bake_time, self.delivery_time = None, None
        self.pizza_dict()
        self.order_type = order_type
        self.set_process()

    def set_process(self) -> None:
        self.bake_time = random.randint(5, 20)
        if self.order_type == 'delivery':
            self.delivery_time = random.randint(15, 60)

    def pizza_dict(self) -> None:
        """
        method listing all the recipes of pizzas
        """
        print(f"Пицца {self.name} размера {self.size}.")
        print(f"Ингредиенты:")
        for i, component in enumerate(self.pizza_recipes[self.name][1]):
            print(f'{i}. {component}')
        print("----------------")


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
        click.echo(f"👨‍🍳 Приготовили за {new_pizza.bake_time} мин!")
        if new_pizza.order_type == 'delivery':
            click.echo(f"🚗 Доставили за {new_pizza.delivery_time} мин!")


if __name__ == '__main__':
    cli()
