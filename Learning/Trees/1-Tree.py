class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChildren(self, child):
        if child not in self.children:
            child.parent = self
            self.children.append(child)
            return True
        return False
    
    def getLevel(self):
        level = 0
        iterator = self
        while iterator.parent:
            level += 1
            iterator = iterator.parent
        return level
    
    def printTree(self):
        prefix = (" " * self.getLevel() * 3) + "|__" if self.parent else ""
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                child.printTree()



if __name__ == "__main__":
    
    root = TreeNode("Life")
    
    house1 = TreeNode("House 1")
    house1.addChildren(TreeNode("Me"))
    house1.addChildren(TreeNode("Identity"))
    
    house2 = TreeNode("House 2")
    house2.addChildren(TreeNode("Possessions"))
    house2.addChildren(TreeNode("Values"))
    house2.addChildren(TreeNode("Income"))
    
    house3 = TreeNode("House 3")
    house3.addChildren(TreeNode("Communication"))
    house3.addChildren(TreeNode("Siblings"))
    house3.addChildren(TreeNode("Learning"))
    
    house4 = TreeNode("House 4")
    house4.addChildren(TreeNode("Home"))
    house4.addChildren(TreeNode("Family"))
    house4.addChildren(TreeNode("Roots"))
    
    house5 = TreeNode("House 5")
    house5.addChildren(TreeNode("Creativity"))
    house5.addChildren(TreeNode("Children"))
    house5.addChildren(TreeNode("Pleasure"))
    
    house6 = TreeNode("House 6")
    house6.addChildren(TreeNode("Work"))
    house6.addChildren(TreeNode("Service"))
    house6.addChildren(TreeNode("Routine"))
    
    house7 = TreeNode("House 7")
    house7.addChildren(TreeNode("Partner"))
    house7.addChildren(TreeNode("Relationships"))
    house7.addChildren(TreeNode("Marriage"))
    
    house8 = TreeNode("House 8")
    house8.addChildren(TreeNode("Transformation"))
    house8.addChildren(TreeNode("Sexuality"))
    house8.addChildren(TreeNode("Inheritance"))
    
    house9 = TreeNode("House 9")
    house9.addChildren(TreeNode("Philosophy"))
    house9.addChildren(TreeNode("Travel"))
    house9.addChildren(TreeNode("Higher Education"))
    
    house10 = TreeNode("House 10")
    house10.addChildren(TreeNode("Career"))
    house10.addChildren(TreeNode("Reputation"))
    house10.addChildren(TreeNode("Achievements"))
    
    house11 = TreeNode("House 11")
    house11.addChildren(TreeNode("Friends"))
    house11.addChildren(TreeNode("Groups"))
    house11.addChildren(TreeNode("Hopes"))
    
    house12 = TreeNode("House 12")
    house12.addChildren(TreeNode("Subconscious"))
    house12.addChildren(TreeNode("Spirituality"))
    house12.addChildren(TreeNode("Sacrifice"))
    
    root.addChildren(house1)
    root.addChildren(house2)
    root.addChildren(house3)
    root.addChildren(house4)
    root.addChildren(house5)
    root.addChildren(house6)
    root.addChildren(house7)
    root.addChildren(house8)
    root.addChildren(house9)
    root.addChildren(house10)
    root.addChildren(house11)
    root.addChildren(house12)
    
    root.printTree()
