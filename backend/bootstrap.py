import time


class Payment(object):
    authorization_number = None
    amount = None
    invoice = None
    order = None
    payment_method = None
    paid_at = None

    def __init__(self, attributes={}):
        self.authorization_number = attributes.get('attributes', None)
        self.amount = attributes.get('amount', None)
        self.invoice = attributes.get('invoice', None)
        self.order = attributes.get('order', None)
        self.payment_method = attributes.get('payment_method', None)

    def pay(self, paid_at=time.time()):
        self.amount = self.order.total_amount
        self.authorization_number = int(time.time())
        attributes = dict(
            billing_address=self.order.address,
            shipping_address=self.order.address,
            order=self.order
        )
        self.invoice = Invoice(attributes=attributes)
        self.paid_at = paid_at
        self.order.close(self.paid_at)

    def is_paid(self):
        return self.paid_at != None


class Invoice():
    billing_address = None
    shipping_address = None
    order = None

    def __init__(self, attributes={}):
        self.billing_address = attributes.get('billing_address', None)
        self.shipping_address = attributes.get('shipping_address', None)
        self.order = attributes.get('order', None)

#Processar o pedido
class Order():
    customer = None
    items = None
    payment = None
    address = None
    closed_at = None

    def __init__(self, customer, attributes={}):
        self.customer = customer
        self.items = []
        self.order_item_class = attributes.get('order_item_class', OrderItem)
        self.address = attributes.get('address', Address(zipcode='45678-979'))

    def add_product(self, product):
    
        self.item = product
        if item == "Inscrito":
            self.items.append(Subscription(order=self))
        elif item == "Livro":
            self.items.append(Book(order=self))
        elif item == "Fisico":
            self.items.append(Physical(order=self))
        elif item == "Midia":
            self.items.append(Midia(order=self))

    def total_amount(self):
        total = 0
        for item in items:
            total += item.total

        return total

    def close(self, closed_at=time.time()):
        self.closed_at = closed_at

    # remember: you can create new methods inside those classes to help you create a better design
    
class OrderItem():
    order = None
    product = None

    def __init__(self, order, product):
        self.__init__(self, order, Product("Produto"))
    def total(self):
        return 10

class Book(OrderItem):
    def __init__(self, order):
        OrderItem.__init__(self, order, Book("Livro"))

    def send(self):
        ShippingLabel('Este item é isento de impostos conforme disposto na Constituicao Art. 150, VI, d.').generateLabel()

class Midia(OrderItem):
    def __init__(self, order):
        OrderItem.__init__(self, order, Midia("Midia"))

    def send(self):
        # Need to implement sender and reciver message
        Notify('conceder voucher').send()
 
class Physical(OrderItem):

    def __init__(self, order):
        OrderItem.__init__(self, order, Physical("Fisico"))

    def send(self):
        ShippingLabel('info').generateLabel()

class Subscription(OrderItem):
    def __init__(self, order):
        OrderItem.__init__(self, order, Subscription("Inscrito"))
    def send(self):
        Membership(self.order.customer.email).activate()
        Notify('info').send()
#Fazer o pedido 

     
      
#Adicionar o ShippingLabel, Notificação e Envio de Email.
class ShippingLabel():
    value = None
    def __init__ (self, value):
        self.value = value
    def generateLabel(self):
        print("%d") %(self)
class Notify():
    text = None
    def __init__ (self, text):
        self.text = text
    def send(self):
        sendEmail.send(self)
class sendEmail():
    queuedArray = []
    @staticmethod
    def send(text):
        sendEmail.queuedArray.append(text)
#Adicionar o ShippingLabel, Notificação e Envio de Email.


        
class Product(object):
    # type to distinguish: physical, book, digital, membership...
    name = None
    type = None
    def __init__(self, name, type):
        self.name = name
        self.type = type
class Address():
    zipcode = None

    def __init__(self, zipcode):
        self.zipcode = zipcode
class CreditCard():
    @staticmethod
    def fetch_by_hashed(code):
        return CreditCard()
class Customer():
    pass
class Membership():
    pass


