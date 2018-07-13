class AVLTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = AVLTreeNode(value)
        else:
            self.root.add(value)


class AVLTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

    def add(self, value):
        if value < self.value:
            # go left
            if self.left:
                self.left.add(value)
            else:
                self.left = AVLTreeNode(value)
            if not self.right or self.right.height < self.left.height:
                self.height = self.left.height + 1
        else:
            # go right
            if self.right:
                self.right.add(value)
            else:
                self.right = AVLTreeNode(value)
            if not self.left or self.right.height > self.left.height:
                self.height = self.right.height + 1
        self.balance()

    def balance(self):
        right_height = self.right.height if self.right else 0
        left_height = self.left.height if self.left else 0

        if left_height > right_height + 1:
            left_right_height = self.left.right.height if self.left.right else 0
            left_left_height = self.left.left.height if self.left.left else 0

            if left_right_height > left_left_height:
                self.left.rotate_right()
            self.rotate_left()
        elif right_height > left_height + 1:
            right_right_height = self.right.right.height if self.right.right else 0
            right_left_height = self.right.left.height if self.right.left else 0

            if right_left_height > right_right_height:
                self.right.rotate_left()
            self.rotate_right()

    def rotate_right(self):
        value_before = self.value
        left_before = self.left
        self.value = self.right.value
        self.left = self.right
        self.right = self.right.right
        self.left.right = self.left.left
        self.left.left = left_before
        self.left.value = value_before
        self.left.update_in_new_loc()
        self.update_in_new_loc()

    def rotate_left(self):
        value_before = self.value
        right_before = self.right
        self.value = self.left.value
        self.right = self.left
        self.left = self.left.left
        self.right.left = self.right.right
        self.right.right = right_before
        self.right.value = value_before
        self.right.update_in_new_loc()
        self.update_in_new_loc()

    def update_in_new_loc(self):
        if not self.right and not self.left:
            self.height = 1
        elif not self.right or self.left and \
                self.right.height < self.left.height:
            self.height = self.left.height + 1
        else:
            self.height = self.right.height + 1
