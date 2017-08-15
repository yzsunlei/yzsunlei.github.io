/**
 * Created by lei.sun on 2017/8/13.
 */
function Node(data, left, right) {
   this.data = data;
   this.count = 1;
   this.left = left;
   this.right = right;
   this.show = show;
   this.getmin = getmin;
   this.getmax = getmax;
   this.find = find;
}

function show() {
   return this.data;
}

// 二叉树
function BST() {
   this.root = null;
   this.insert = insert;
   this.inOrder = inOrder;
   this.preOrder = preOrder;
   this.postOrder = postOrder;
   this.getmin = getmin;
   this.getmax = getmax;
   this.find = find;
   this.remove = remove;
   this.removeNode = removeNode;
   this.getSmallest = getSmallest;
}

function insert(data) {
   var n = new Node(data, null, null);
   if (this.root == null) {
      this.root = n;
   } else {
      var current = this.root;
      var parent;
      while (true) {
         parent = current;
         if (data < current.data) {
            current = current.left;
            if (current == null) {
               parent.left = n;
               break;
            }
         } else {
            current = current.right;
            if (current == null) {
               parent.right = n;
               break;
            }
         }
      }
   }
}

// 中序遍历
function inOrder(node) {
   if (!(node == null)) {
      inOrder(node.left);
      console.log(node.show() + " ");
      inOrder(node.right);
   }
}

// 先序遍历
function preOrder(node) {
   if (!(node == null)) {
      console.log(node.show() + " ");
      preOrder(node.left);
      preOrder(node.right);
   }
}

// 后序遍历
function postOrder(node) {
   if (!(node == null)) {
      postOrder(node.left);
      postOrder(node.right);
      console.log(node.show() + " ");
   }
}

function getmin() {
   var current = this.root;
   while (!(current.left == null)) {
      current = current.left;
   }
   return current.data;
}

function getmax() {
   var current = this.root;
   while (!(current.right == null)) {
      current = current.right;
   }
   return current.data;
}

function find(data) {
   var current = this.root;
   while (current.data != data) {
      if (data < current.data) {
         current = current.left;
      } else {
         current = current.right;
      }
      if (current == null) {
         return null;
      }
   }
   return current;
}

function getSmallest(node) {
   if (node.left == null) {
      return node;
   } else {
      return getSmallest(node.left);
   }
}

function remove(data) {
   root = removeNode(this.root, data);
}

function removeNode(node, data) {
   if (node == null) {
      return null;
   }
   if (data == node.data) {
      // node has no children
      if (node.left == null && node.right == null) {
         return null;
      }
      // node has no left child
      if (node.left == null) {
         return node.right;
      }
      // node has no right child
      if (node.right == null) {
         return node.left;
      }
      // node has two children
      var tempNode = getSmallest(node.right);
      node.data = tempNode.data;
      node.right = removeNode(node.right, tempNode.data);
      return node;
   } else if (data < node.data) {
      node.left = removeNode(node.left, data);
      return node;
   } else {
      node.right = removeNode(node.right, data);
      return node;
   }
}

function prArray(arr) {
   console.log(arr[0].toString + ' ');
   for (var i = 1; i < arr.length; ++i) {
      console.log(arr[i].toString() + ' ');
      if ( i % 10 == 0) {
         console.log("\n");
      }
   }
}

// test
var nums = new BST();
nums.insert(23);
nums.insert(45);
nums.insert(16);
nums.insert(37);
nums.insert(3);
nums.insert(99);
nums.insert(22);
console.log("Inorder traversal: ");
inOrder(nums.root);
console.log("\n");
console.log("Preorder traversal: ");
preOrder(nums.root);
console.log("\n");
console.log("Postorder traversal: ");
postOrder(nums.root);
console.log("\n");
var min = nums.getmin();
console.log("The minimum value of the BST is: " + min);
var max = nums.getmax();
console.log("The maximum value of the BST is: " + max);
inOrder(nums.root);
console.log("\n");
// console.log("Enter a value to search for: ");
// var value = parseInt(readline());
// var found = nums.find(value);
// if (found != null) {
//    console.log("Found " + value + " in the BST.");
// } else {
//    console.log(value + " was not found in the BST.");
// }
// inOrder(nums.root);
// console.log("\n");
// var num = parseInt(readline());
// nums.remove(num);
// inOrder(nums.root);
