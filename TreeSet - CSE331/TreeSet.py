import math
class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """
    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.comp = comp
        self.size = 0
        self.h = 0
        self.root = None
        # added stuff below

    def __len__(self): #returns size of tree
        return self.size

    def height(self): #returns the height of tree
        if self == None:
            return -1

        return self.h

    def insert(self, item): #inserts item into tree
        node = TreeNode(item)
        if self.size == 0: #if empty tree, just place as root
            self.size = 1
            self.root = node
            return True
        CurrentNode = self.root #if not go thru and find where to place
        while True:
            if self.comp(CurrentNode.data,item) > 0: #if a is less than b
                if CurrentNode.left is not None:
                    CurrentNode = CurrentNode.left
                else:
                    CurrentNode.left = node
                    self.size += 1
                    self.__balance__()
                    return True
            elif self.comp(CurrentNode.data,item) < 0: #if b is less than a
                if CurrentNode.right is not None:
                    CurrentNode = CurrentNode.right
                else:
                    CurrentNode.right = node
                    self.size += 1
                    self.__balance__()
                    return True
            else:
                return False

    def remove(self, item):
        toRemove = self.__get__(item) #gives item to remove
        if toRemove and (self.__remove__(toRemove)):
            toRemove = None
            self.__balance__() #uses balance
            return True
        return False #if unable to return false


    def __contains__(self, item): #checks if tree contains item
        Currentnode = self.root
        while True:
            if Currentnode == None: #if empty return false
                return False
            elif self.comp(Currentnode.data,item) > 0: #uses compare to navigate tree, if a is less than b
                Currentnode = Currentnode.left
            elif self.comp(Currentnode.data, item) < 0: #uses compare to navigate tree, if b is less than a
                Currentnode = Currentnode.right
            else: #if found return true
                return True




    def first(self): #return first value
        if self.size == 0: #if empty throw error
    	    raise KeyError
        else: #call minNode, use to get smallest which is the first value
            return self.__getMinNode__(self.root).data


    def last(self): #return last value
        if self.size ==0: #if empty throw error
    	    raise KeyError
        else: #call maxNode, use to get largest which is the last value
            return self.__getMaxNode__(self.root).data

    def clear(self): #clears the tree
        self.left = None
        self.right = None
        self.data = None
        self.size = 0
        pass

    def __iter__(self): #iterates thur the tree, uses iterarte
        for x in self.__iterate__(self.root):
            yield x

    def __iterate__(self,node):
        if node.left: #goes thru until there are no more lefts
            for l in self.__iterate__(node.left): #recursively yield
                yield l
        yield node.data
        if node.right: #goes thru until there are no more rights
            for r in self.__iterate__(node.right): #recursively yield
                yield r


    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    # Helper functions
    # You can add additional functions here
    def __get__(self,item): #removes node with value of item or none
        Currentnode = self.root
        while True:
            if Currentnode == None: #if empty
                return None
            elif self.comp(Currentnode.data,item) > 0: #if a is less than b
                Currentnode = Currentnode.left
            elif self.comp(Currentnode.data, item) < 0: #if b is less than a
                Currentnode = Currentnode.right
            else:
                return Currentnode
    def __getMinNode__(self,node): #return smallest min node
        if node.left == None:
            return node
        return self.__getMinNode__(node.left);
    def __getMaxNode__(self,node): #return largest max node
        if node.right == None:
            return node
        return self.__getMaxNode__(node.right)
    def __getParent__(self,item): #returns parent node
        Currentnode = self.root
        while True:
            curNodeComp = self.comp(Currentnode.data, item)
            if(curNodeComp > 0): #a is less than b
                if(Currentnode.left == None):
                    return None
                elif(self.comp(Currentnode.left.data, item) == 0):
                    return Currentnode
                else:
                    Currentnode = Currentnode.left
            elif(curNodeComp < 0): #a is greater than b
                if (Currentnode.right == None):
                    return None
                elif (self.comp(Currentnode.right.data, item) == 0):
                    return Currentnode
                else:
                    Currentnode = Currentnode.right
            else: #if equal
                return None

    def __remove__(self,node): #used to remove
        if not node.left and not node.right: #if neither left/right
            parent = self.__getParent__(node.data)
            if not parent: #Node to remove is the root
                self.root = None
                self.first = None
                self.last = None
            elif(parent.left and parent.left.data == node.data):
                parent.left = None
            else:
                parent.right = None
            self.size -= 1 #fix size
            return True
        elif not node.left: #delete from right
            node.data = node.right.data
            node.right = None
            self.size -= 1 #fix size
            return True
        elif not node.right: #delete from left
            node.data = node.left.data
            node.left = None
            self.size -= 1 #fix size
            return True
        else: #need to find sucessor, use it to delete
            successor = self.__getMinNode__(node.right)
            temp = successor.data
            successor.data = node.data
            node.data = temp
            if self.__remove__(successor):
                self.size -= 1 #fix size
                return True
            return False #if unable return false


    def __balance__(self):
        pseudoRoot = TreeNode("pseudo")
        pseudoRoot.right = self.root
        tail = pseudoRoot
        rest = tail.right
        #Convert the current unbalanced tree into a "vine" with only right nodes
        #psuedoRoot becomes the new root with all other nodes on the right
        while rest is not None:
            if rest.left is None: #make all right nodes, vine
                tail = rest
                rest = rest.right
            else:
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp

        #Convert the vine back into a tree
        leaves = int(self.size + 1 - 2**math.floor(math.log(self.size + 1, 2)))
        self.__compress__(pseudoRoot,leaves)
        size = self.size - leaves
        while size > 1:
            self.__compress__(pseudoRoot,size/2)
            size = size/2
        self.root = pseudoRoot.right
        self.h = math.ceil(math.log(self.size + 1,2))

    def __compress__(self,root,count): #compress leaves back into tree
        scanner = root
        for i in range(0, count):
            child = scanner.right
            scanner.right = child.right
            scanner = scanner.right
            child.right = scanner.left
            scanner.left = child



class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """
    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)