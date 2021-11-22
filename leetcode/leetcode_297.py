class Codec:

    def serialize(self, root):
        if not root:
            return ""
        q = collections.deque([root])
        length = 0
        output = [root.val]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                length += 1
                if node.left!=None:
                    q.append(node.left)
                    output.append(node.left.val)
                else:
                    output.append(node.left)
                if node.right != None:
                    q.append(node.right)
                    output.append(node.right.val)
                else:
                    output.append(node.right)
        output = ' '.join(list(map(str,output)))
        
        return output      
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if not data:
            return 
        data = collections.deque(data.split())
        root = TreeNode(val = int(data.popleft()), left = None, right = None)
       
        tempt =  collections.deque([root])
        while data:
            for _ in range(len(tempt)):
                node = tempt.popleft()
                left_val = data.popleft()
                if left_val != "None":
                    left_val = TreeNode(val = int(left_val), left = None, right = None)
                    tempt.append(left_val)
                else:
                    left_val = None
                right_val = data.popleft()
                if right_val != "None":
                    right_val = TreeNode(val = int(right_val), left = None, right = None)
                    tempt.append(right_val)
                else:
                    right_val = None
                node.left, node.right = left_val, right_val  # even though lef_val or right_val == None, it ok   
            
        return root
