class BeautyProduct:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to cart.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product '{product.name}' removed from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        print("Shopping Cart:")
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}")

class OnlineShopping:
    def __init__(self):
        self.cart = ShoppingCart()
        self.products = [
            BeautyProduct(1, "Foundation", 150.00),
            BeautyProduct(2, "Mascara", 800.99),
            BeautyProduct(3, "Lipstick", 120.99),
            BeautyProduct(4, "Eyeshadow", 180.99),
            BeautyProduct(5, "Blush", 100.99)
        ]

    def display_products(self):
        print("Available Beauty Products:")
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}")

    def run(self):
        while True:
            print("\n1. Display Products")
            print("2. Add Product to Cart")
            print("3. Remove Product from Cart")
            print("4. View Cart")
            print("5. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_products()
            elif choice == "2":
                product_id = int(input("Enter product ID: "))
                for product in self.products:
                    if product.product_id == product_id:
                        self.cart.add_product(product)
                        break
                else:
                    print("Product not found.")
            elif choice == "3":
                product_id = int(input("Enter product ID: "))
                self.cart.remove_product(product_id)
            elif choice == "4":
                self.cart.view_cart()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    online_shopping = OnlineShopping()
    online_shopping.run()