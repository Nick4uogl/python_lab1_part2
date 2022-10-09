class BinaryTree:

    def __init__(self, product_price, product_code):
        self.right = None
        self.left = None
        self.product_price = product_price
        self.product_code = product_code

    def insert(self, product_price, product_code):
        if not self.product_code:
            self.product_code = product_code
            self.product_price = product_price
            return

        if self.product_code == product_code:
            return

        if product_code < self.product_code:
            if self.left:
                self.left.insert(product_price, product_code)
                return
            self.left = BinaryTree(product_price, product_code)
            return

        if self.right:
            self.right.insert(product_price, product_code)
            return
        self.right = BinaryTree(product_price, product_code)

    def sum_prices(self, root):
        if not root:
            return 0
        return root.product_price + root.sum_prices(root.right) + root.sum_prices(root.left)

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.product_code is not None:
            vals.append({"product_code": self.product_code, "product_price": self.product_price})
        if self.right is not None:
            self.right.inorder(vals)
        return vals


product_tree = BinaryTree(12, 5)
product_tree.insert(13, 3)
product_tree.insert(13, 7)
product_tree.insert(13, 9)
product_tree.insert(13, 1)
print(product_tree.sum_prices(product_tree))
print(product_tree.inorder([]))
