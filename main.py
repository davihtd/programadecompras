from Ownable import Ownable  # Importa el módulo Ownable en todas las clases que requieran derechos de propietario

class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.contents = []

    def add_to_cart(self, product, quantity):
        # Implementa la lógica para agregar productos al carrito
        # Por ejemplo:
        item = {
            "product": product,
            "quantity": quantity,
            "price": product.price  # Asume que el producto tiene un atributo "price"
        }
        self.contents.append(item)

    def check_out(self):
        total_amount = 0

        # Calcular el precio total del carrito
        for item in self.contents:
            total_amount += item["price"] * item["quantity"]

        # Transferir el precio total al monedero del propietario del carrito
        self.owner.transfer_funds(total_amount)

        # Transferir la propiedad de los productos al propietario del carrito
        for item in self.contents:
            item["owner"] = self.owner

        # Vaciar el contenido del carrito
        self.contents = []

        return total_amount
