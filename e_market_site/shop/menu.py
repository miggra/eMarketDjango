from django.conf import settings


home_page = {'title': "Главная",
            'url_name': 'shop:index',
            'position' : 'left'}
cart = {'title': "Корзина",
        'url_name': 'cart:cart_detail',
        'position' : 'right'}
user_office = {'title': "Личный кабинет",
                'url_name': 'user_office:profile', 
                'position' : 'left'}
login = {'title': "Вход",
        'url_name': 'accounts:login',
        'position' : 'left'}

seller_items = [home_page, user_office]
customer_items =[home_page, user_office, cart]
unauthenticated_items = [home_page, login, cart]

def add_items(main_dictionary, list_to_add):
    for item in list_to_add:
        main_dictionary[item['title']] = item

class Menu():
    def __init__(self, request):
        self.session = request.session
        items = self.session.get(settings.MENU_SESSION_ID)
        if not items:
            user = request.user
            if  not request.user.is_authenticated:
                items = unauthenticated_items
            else:
                if user.groups.filter(name='Sellers').exists():
                    items = seller_items
                if user.groups.filter(name='Customers').exists():
                    items = customer_items 
        self.items = items
        

            

