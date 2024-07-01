import sys
import os

from collections import defaultdict, Counter

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.lc_libs import write_solution_python, write_solution_golang, write_solution_java, write_solution_cpp, \
    write_solution_typescript

default_test_list = [
    # problem 1
    "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:",

    # problem 23
    "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         "
    "self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self,"
    " lists: List[Optional[ListNode]]) -> Optional[ListNode]:",

    # problem 1656
    "class OrderedStream:\n\n    def __init__(self, n: int):\n\n\n    def insert(self, idKey: int, value: str) ->"
    " List[str]:\n\n\n\n# Your OrderedStream object will be instantiated and called as such:\n#"
    " obj = OrderedStream(n)\n# param_1 = obj.insert(idKey,value)",

    # problem 2166
    "class Bitset:\n\n    def __init__(self, size: int):\n\n\n    def fix(self, idx: int) -> None:\n\n\n    "
    "def unfix(self, idx: int) -> None:\n\n\n    def flip(self) -> None:\n\n\n    def all(self) -> bool:\n\n\n"
    "    def one(self) -> bool:\n\n\n    def count(self) -> int:\n\n\n    def toString(self) -> str:\n\n\n\n"
    "# Your Bitset object will be instantiated and called as such:\n# obj = Bitset(size)\n# obj.fix(idx)\n"
    "# obj.unfix(idx)\n# obj.flip()\n# param_4 = obj.all()\n# param_5 = obj.one()\n"
    "# param_6 = obj.count()\n# param_7 = obj.toString()",

    # problem 919
    "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):"
    "\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass CBTInserter:\n\n"
    "    def __init__(self, root: Optional[TreeNode]):\n\n\n    def insert(self, val: int) -> int:\n\n\n"
    "    def get_root(self) -> Optional[TreeNode]:\n\n\n\n# Your CBTInserter object will be instantiated and"
    " called as such:\n# obj = CBTInserter(root)\n# param_1 = obj.insert(val)\n# param_2 = obj.get_root()",

    # problem 449
    "# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, x):\n#         "
    "self.val = x\n#         self.left = None\n#         self.right = None\n\nclass Codec:\n\n    "
    "def serialize(self, root):\n        \"\"\"Encodes a tree to a single string.\n        \n        "
    ":type root: TreeNode\n        :rtype: str\n        \"\"\"\n        \n\n    def deserialize(self, data):\n"
    "        \"\"\"Decodes your encoded data to tree.\n        \n        :type data: str\n        :rtype: TreeNode\n"
    "        \"\"\"\n        \n\n# Your Codec object will be instantiated and called as such:\n"
    "# ser = Codec()\n# deser = Codec()\n# ans = deser.deserialize(ser.serialize(root))",

    # problem 133
    "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        "
    "self.val = val\n        self.neighbors = neighbors if neighbors is not None else []\n\"\"\"\n\n"
    "from typing import Optional\nclass Solution:\n    def cloneGraph(self, node: Optional['Node'])"
    " -> Optional['Node']:\n        ",

    # problem 2671
    "class FrequencyTracker:\n\n    def __init__(self):\n\n\n    def add(self, number: int) -> None:\n\n\n    "
    "def deleteOne(self, number: int) -> None:\n\n\n    def hasFrequency(self, frequency: int) -> bool:\n\n\n\n"
    "# Your FrequencyTracker object will be instantiated and called as such:\n# obj = FrequencyTracker()\n"
    "# obj.add(number)\n# obj.deleteOne(number)\n# param_3 = obj.hasFrequency(frequency)",

    # problem 284
    "# Below is the interface for Iterator, which is already defined for you.\n#\n# class Iterator:\n"
    "#     def __init__(self, nums):\n#         \"\"\"\n#         Initializes an iterator object to the "
    "beginning of a list.\n#         :type nums: List[int]\n#         \"\"\"\n#\n#     def hasNext(self):\n#"
    "         \"\"\"\n#         Returns true if the iteration has more elements.\n#         :rtype: bool\n#         "
    "\"\"\"\n#\n#     def next(self):\n#         \"\"\"\n#         Returns the next element in the iteration.\n"
    "#         :rtype: int\n#         \"\"\"\n\nclass PeekingIterator:\n    def __init__(self, iterator):\n        "
    "\"\"\"\n        Initialize your data structure here.\n        :type iterator: Iterator\n        \"\"\"\n        "
    "\n\n    def peek(self):\n        \"\"\"\n        Returns the next element in the iteration without advancing the "
    "iterator.\n        :rtype: int\n        \"\"\"\n        \n\n    def next(self):\n        \"\"\"\n        "
    ":rtype: int\n        \"\"\"\n        \n\n    def hasNext(self):\n        \"\"\"\n        :rtype: bool\n        "
    "\"\"\"\n        \n\n# Your PeekingIterator object will be instantiated and called as such:\n"
    "# iter = PeekingIterator(Iterator(nums))\n# while iter.hasNext():\n#     val = iter.peek()   # Get the next "
    "element but not advance the iterator.\n#     iter.next()         # Should return the same value as [val].",

    # problem 73
    "class Solution(object):\n    def setZeroes(self, matrix):\n        \"\"\"\n        :type matrix: List[List["
    "int]]\n        :rtype: None Do not return anything, modify matrix in-place instead.\n        \"\"\"",

    # problem 1382
    "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, "
    "right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass "
    "Solution:\n    def balanceBST(self, root: TreeNode) -> TreeNode:\n",

    # problem 382
    "# Definition for singly-linked list.\n# class ListNode(object):\n#     def __init__(self, val=0, next=None):\n#  "
    "       self.val = val\n#         self.next = next\nclass Solution(object):\n\n    def __init__(self, head):\n    "
    "    \"\"\"\n        :type head: Optional[ListNode]\n        \"\"\"\n\n\n    def getRandom(self):\n        "
    "\"\"\"\n        :rtype: int\n        \"\"\"\n\n\n\n# Your Solution object will be instantiated and called as "
    "such:\n# obj = Solution(head)\n# param_1 = obj.getRandom()",
]

submit_test_list = [
    "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):"
    "\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    "
    "def countNodes(self, root: Optional[TreeNode]) -> int:\n        def depth(node):\n            h = 0\n            "
    "while node:\n                node = node.left\n                h += 1\n            return h\n\n        "
    "if not root:\n            return 0\n        left, right = depth(root.left), depth(root.right)\n        "
    "if left == right:\n            return self.countNodes(root.right) + (1 << right)\n        else:\n            "
    "return self.countNodes(root.left) + (1 << right)\n",

    "class Solution:\n    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:\n        "
    "m, n = len(obstacleGrid), len(obstacleGrid[0])\n        dp = [0] * n\n        dp[0] = 1\n        "
    "for i in range(m):\n            for j in range(n):\n                if obstacleGrid[i][j] == 1:\n              "
    "      dp[j] = -1\n                elif j > 0:\n                    dp[j] = dp[j - 1] if dp[j] == -1 else (dp[j]"
    " if dp[j - 1] == -1 else dp[j] + dp[j - 1])\n        return dp[-1] if dp[-1] > 0 else 0\n",

    "class Solution:\n    def change(self, amount: int, coins: List[int]) -> int:\n        dp = [0] * (amount + 1)\n"
    "        dp[0] = 1\n        for c in coins:\n            for i in range(c, amount + 1):\n                "
    "dp[i] += dp[i - c]\n        return dp[-1]\n",
]

golang_test_list = [
    "type ParkingSystem struct {\n\n}\n\n\nfunc Constructor(big int, medium int, small int) ParkingSystem {\n\n}\n\n\n"
    "func (this *ParkingSystem) AddCar(carType int) bool {\n\n}\n\n\n/**"
    "\n * Your ParkingSystem object will be instantiated and called as such:\n"
    " * obj := Constructor(big, medium, small);\n * param_1 := obj.AddCar(carType);\n */",

    "func twoSum(nums []int, target int) []int {\n\n}",

    "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n"
    " * }\n */\nfunc swapPairs(head *ListNode) *ListNode {\n\n}",

    "type OrderedStream struct {\n\n}\n\n\nfunc Constructor(n int) OrderedStream {\n\n}\n\n\n"
    "func (this *OrderedStream) Insert(idKey int, value string) []string {\n\n}\n\n\n"
    "/**\n"
    " * Your OrderedStream object will be instantiated and called as such:\n"
    " * obj := Constructor(n);\n"
    " * param_1 := obj.Insert(idKey,value);\n"
    " */"
]

problems = defaultdict(list)
problems["1"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "class Solution {\n    public int[] twoSum(int[] nums, int target) {\n\n    }\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "class Solution(object):\n    def twoSum(self, nums, target):\n        \"\"\"\n        :type nums: List[int]\n        :type target: int\n        :rtype: List[int]\n        \"\"\""
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* twoSum(int* nums, int numsSize, int target, int* returnSize) {\n    \n}"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "public class Solution {\n    public int[] TwoSum(int[] nums, int target) {\n\n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * @param {number[]} nums\n * @param {number} target\n * @return {number[]}\n */\nvar twoSum = function(nums, target) {\n\n};"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "function twoSum(nums: number[], target: number): number[] {\n    \n};"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param Integer $target\n     * @return Integer[]\n     */\n    function twoSum($nums, $target) {\n\n    }\n}"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "class Solution {\n    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {\n\n    }\n}"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "class Solution {\n    fun twoSum(nums: IntArray, target: Int): IntArray {\n\n    }\n}"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "class Solution {\n  List<int> twoSum(List<int> nums, int target) {\n    \n  }\n}"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "func twoSum(nums []int, target int) []int {\n\n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer[]}\ndef two_sum(nums, target)\n\nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "object Solution {\n    def twoSum(nums: Array[Int], target: Int): Array[Int] = {\n\n    }\n}"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "impl Solution {\n    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {\n\n    }\n}"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "(define/contract (two-sum nums target)\n  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))\n  )"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].\ntwo_sum(Nums, Target) ->\n  ."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "defmodule Solution do\n  @spec two_sum(nums :: [integer], target :: integer) :: [integer]\n  def two_sum(nums, target) do\n    \n  end\nend"
    }
]
problems["23"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n\n    }\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n\n    }\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "# Definition for singly-linked list.\n# class ListNode(object):\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution(object):\n    def mergeKLists(self, lists):\n        \"\"\"\n        :type lists: List[ListNode]\n        :rtype: ListNode\n        \"\"\"\n        "
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     struct ListNode *next;\n * };\n */\nstruct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {\n    \n}"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next = next;\n *     }\n * }\n */\npublic class Solution {\n    public ListNode MergeKLists(ListNode[] lists) {\n\n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode[]} lists\n * @return {ListNode}\n */\nvar mergeKLists = function(lists) {\n\n};"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * Definition for singly-linked list.\n * class ListNode {\n *     val: number\n *     next: ListNode | null\n *     constructor(val?: number, next?: ListNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *     }\n * }\n */\n\nfunction mergeKLists(lists: Array<ListNode | null>): ListNode | null {\n    \n};"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *     public $val = 0;\n *     public $next = null;\n *     function __construct($val = 0, $next = null) {\n *         $this->val = $val;\n *         $this->next = $next;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param ListNode[] $lists\n     * @return ListNode\n     */\n    function mergeKLists($lists) {\n\n    }\n}"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     public var val: Int\n *     public var next: ListNode?\n *     public init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int) { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }\n * }\n */\nclass Solution {\n    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {\n\n    }\n}"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "/**\n * Example:\n * var li = ListNode(5)\n * var v = li.`val`\n * Definition for singly-linked list.\n * class ListNode(var `val`: Int) {\n *     var next: ListNode? = null\n * }\n */\nclass Solution {\n    fun mergeKLists(lists: Array<ListNode?>): ListNode? {\n\n    }\n}"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "/**\n * Definition for singly-linked list.\n * class ListNode {\n *   int val;\n *   ListNode? next;\n *   ListNode([this.val = 0, this.next]);\n * }\n */\nclass Solution {\n  ListNode? mergeKLists(List<ListNode?> lists) {\n    \n  }\n}"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc mergeKLists(lists []*ListNode) *ListNode {\n\n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\n# @param {ListNode[]} lists\n# @return {ListNode}\ndef merge_k_lists(lists)\n\nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "/**\n * Definition for singly-linked list.\n * class ListNode(_x: Int = 0, _next: ListNode = null) {\n *   var next: ListNode = _next\n *   var x: Int = _x\n * }\n */\nobject Solution {\n    def mergeKLists(lists: Array[ListNode]): ListNode = {\n\n    }\n}"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "// Definition for singly-linked list.\n// #[derive(PartialEq, Eq, Clone, Debug)]\n// pub struct ListNode {\n//   pub val: i32,\n//   pub next: Option<Box<ListNode>>\n// }\n//\n// impl ListNode {\n//   #[inline]\n//   fn new(val: i32) -> Self {\n//     ListNode {\n//       next: None,\n//       val\n//     }\n//   }\n// }\nimpl Solution {\n    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {\n\n    }\n}"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "; Definition for singly-linked list:\n#|\n\n; val : integer?\n; next : (or/c list-node? #f)\n(struct list-node\n  (val next) #:mutable #:transparent)\n\n; constructor\n(define (make-list-node [val 0])\n  (list-node val #f))\n\n|#\n\n(define/contract (merge-k-lists lists)\n  (-> (listof (or/c list-node? #f)) (or/c list-node? #f))\n  )"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "%% Definition for singly-linked list.\n%%\n%% -record(list_node, {val = 0 :: integer(),\n%%                     next = null :: 'null' | #list_node{}}).\n\n-spec merge_k_lists(Lists :: [#list_node{} | null]) -> #list_node{} | null.\nmerge_k_lists(Lists) ->\n  ."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "# Definition for singly-linked list.\n#\n# defmodule ListNode do\n#   @type t :: %__MODULE__{\n#           val: integer,\n#           next: ListNode.t() | nil\n#         }\n#   defstruct val: 0, next: nil\n# end\n\ndefmodule Solution do\n  @spec merge_k_lists(lists :: [ListNode.t | nil]) :: ListNode.t | nil\n  def merge_k_lists(lists) do\n    \n  end\nend"
    }
]
problems["1656"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "class OrderedStream {\npublic:\n    OrderedStream(int n) {\n\n    }\n    \n    vector<string> insert(int idKey, string value) {\n\n    }\n};\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * OrderedStream* obj = new OrderedStream(n);\n * vector<string> param_1 = obj->insert(idKey,value);\n */"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "class OrderedStream {\n\n    public OrderedStream(int n) {\n\n    }\n    \n    public List<String> insert(int idKey, String value) {\n\n    }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * OrderedStream obj = new OrderedStream(n);\n * List<String> param_1 = obj.insert(idKey,value);\n */"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "class OrderedStream(object):\n\n    def __init__(self, n):\n        \"\"\"\n        :type n: int\n        \"\"\"\n\n\n    def insert(self, idKey, value):\n        \"\"\"\n        :type idKey: int\n        :type value: str\n        :rtype: List[str]\n        \"\"\"\n\n\n\n# Your OrderedStream object will be instantiated and called as such:\n# obj = OrderedStream(n)\n# param_1 = obj.insert(idKey,value)"
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "class OrderedStream:\n\n    def __init__(self, n: int):\n\n\n    def insert(self, idKey: int, value: str) -> List[str]:\n\n\n\n# Your OrderedStream object will be instantiated and called as such:\n# obj = OrderedStream(n)\n# param_1 = obj.insert(idKey,value)"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "\n\n\ntypedef struct {\n    \n} OrderedStream;\n\n\nOrderedStream* orderedStreamCreate(int n) {\n    \n}\n\nchar** orderedStreamInsert(OrderedStream* obj, int idKey, char* value, int* retSize) {\n    \n}\n\nvoid orderedStreamFree(OrderedStream* obj) {\n    \n}\n\n/**\n * Your OrderedStream struct will be instantiated and called as such:\n * OrderedStream* obj = orderedStreamCreate(n);\n * char** param_1 = orderedStreamInsert(obj, idKey, value, retSize);\n \n * orderedStreamFree(obj);\n*/"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "public class OrderedStream {\n\n    public OrderedStream(int n) {\n\n    }\n    \n    public IList<string> Insert(int idKey, string value) {\n\n    }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * OrderedStream obj = new OrderedStream(n);\n * IList<string> param_1 = obj.Insert(idKey,value);\n */"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * @param {number} n\n */\nvar OrderedStream = function(n) {\n\n};\n\n/** \n * @param {number} idKey \n * @param {string} value\n * @return {string[]}\n */\nOrderedStream.prototype.insert = function(idKey, value) {\n\n};\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * var obj = new OrderedStream(n)\n * var param_1 = obj.insert(idKey,value)\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "class OrderedStream {\n    constructor(n: number) {\n        \n    }\n\n    insert(idKey: number, value: string): string[] {\n        \n    }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * var obj = new OrderedStream(n)\n * var param_1 = obj.insert(idKey,value)\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "class OrderedStream {\n    /**\n     * @param Integer $n\n     */\n    function __construct($n) {\n\n    }\n\n    /**\n     * @param Integer $idKey\n     * @param String $value\n     * @return String[]\n     */\n    function insert($idKey, $value) {\n\n    }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * $obj = OrderedStream($n);\n * $ret_1 = $obj->insert($idKey, $value);\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "\nclass OrderedStream {\n\n    init(_ n: Int) {\n\n    }\n    \n    func insert(_ idKey: Int, _ value: String) -> [String] {\n\n    }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * let obj = OrderedStream(n)\n * let ret_1: [String] = obj.insert(idKey, value)\n */"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "class OrderedStream(n: Int) {\n\n    fun insert(idKey: Int, value: String): List<String> {\n\n    }\n\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * var obj = OrderedStream(n)\n * var param_1 = obj.insert(idKey,value)\n */"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "class OrderedStream {\n\n  OrderedStream(int n) {\n    \n  }\n  \n  List<String> insert(int idKey, String value) {\n    \n  }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * OrderedStream obj = OrderedStream(n);\n * List<String> param1 = obj.insert(idKey,value);\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "type OrderedStream struct {\n\n}\n\n\nfunc Constructor(n int) OrderedStream {\n\n}\n\n\nfunc (this *OrderedStream) Insert(idKey int, value string) []string {\n\n}\n\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * obj := Constructor(n);\n * param_1 := obj.Insert(idKey,value);\n */"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "class OrderedStream\n\n=begin\n    :type n: Integer\n=end\n    def initialize(n)\n        \n    end\n\n\n=begin\n    :type id_key: Integer\n    :type value: String\n    :rtype: String[]\n=end\n    def insert(id_key, value)\n        \n    end\n\n\nend\n\n# Your OrderedStream object will be instantiated and called as such:\n# obj = OrderedStream.new(n)\n# param_1 = obj.insert(id_key, value)"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "class OrderedStream(_n: Int) {\n\n    def insert(idKey: Int, value: String): List[String] = {\n        \n    }\n\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * val obj = new OrderedStream(n)\n * val param_1 = obj.insert(idKey,value)\n */"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "struct OrderedStream {\n\n}\n\n\n/**\n * `&self` means the method takes an immutable reference.\n * If you need a mutable reference, change it to `&mut self` instead.\n */\nimpl OrderedStream {\n\n    fn new(n: i32) -> Self {\n\n    }\n    \n    fn insert(&self, id_key: i32, value: String) -> Vec<String> {\n\n    }\n}\n\n/**\n * Your OrderedStream object will be instantiated and called as such:\n * let obj = OrderedStream::new(n);\n * let ret_1: Vec<String> = obj.insert(idKey, value);\n */"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "(define ordered-stream%\n  (class object%\n    (super-new)\n    \n    ; n : exact-integer?\n    (init-field\n      n)\n    \n    ; insert : exact-integer? string? -> (listof string?)\n    (define/public (insert id-key value)\n      )))\n\n;; Your ordered-stream% object will be instantiated and called as such:\n;; (define obj (new ordered-stream% [n n]))\n;; (define param_1 (send obj insert id-key value))"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "-spec ordered_stream_init_(N :: integer()) -> any().\nordered_stream_init_(N) ->\n  .\n\n-spec ordered_stream_insert(IdKey :: integer(), Value :: unicode:unicode_binary()) -> [unicode:unicode_binary()].\nordered_stream_insert(IdKey, Value) ->\n  .\n\n\n%% Your functions will be called as such:\n%% ordered_stream_init_(N),\n%% Param_1 = ordered_stream_insert(IdKey, Value),\n\n%% ordered_stream_init_ will be called before every test case, in which you can do some necessary initializations."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "defmodule OrderedStream do\n  @spec init_(n :: integer) :: any\n  def init_(n) do\n    \n  end\n\n  @spec insert(id_key :: integer, value :: String.t) :: [String.t]\n  def insert(id_key, value) do\n    \n  end\nend\n\n# Your functions will be called as such:\n# OrderedStream.init_(n)\n# param_1 = OrderedStream.insert(id_key, value)\n\n# OrderedStream.init_ will be called before every test case, in which you can do some necessary initializations."
    }
]
problems["2166"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "class Bitset {\npublic:\n    Bitset(int size) {\n\n    }\n    \n    void fix(int idx) {\n\n    }\n    \n    void unfix(int idx) {\n\n    }\n    \n    void flip() {\n\n    }\n    \n    bool all() {\n\n    }\n    \n    bool one() {\n\n    }\n    \n    int count() {\n\n    }\n    \n    string toString() {\n\n    }\n};\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * Bitset* obj = new Bitset(size);\n * obj->fix(idx);\n * obj->unfix(idx);\n * obj->flip();\n * bool param_4 = obj->all();\n * bool param_5 = obj->one();\n * int param_6 = obj->count();\n * string param_7 = obj->toString();\n */"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "class Bitset {\n\n    public Bitset(int size) {\n\n    }\n    \n    public void fix(int idx) {\n\n    }\n    \n    public void unfix(int idx) {\n\n    }\n    \n    public void flip() {\n\n    }\n    \n    public boolean all() {\n\n    }\n    \n    public boolean one() {\n\n    }\n    \n    public int count() {\n\n    }\n    \n    public String toString() {\n\n    }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * Bitset obj = new Bitset(size);\n * obj.fix(idx);\n * obj.unfix(idx);\n * obj.flip();\n * boolean param_4 = obj.all();\n * boolean param_5 = obj.one();\n * int param_6 = obj.count();\n * String param_7 = obj.toString();\n */"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "class Bitset(object):\n\n    def __init__(self, size):\n        \"\"\"\n        :type size: int\n        \"\"\"\n\n\n    def fix(self, idx):\n        \"\"\"\n        :type idx: int\n        :rtype: None\n        \"\"\"\n\n\n    def unfix(self, idx):\n        \"\"\"\n        :type idx: int\n        :rtype: None\n        \"\"\"\n\n\n    def flip(self):\n        \"\"\"\n        :rtype: None\n        \"\"\"\n\n\n    def all(self):\n        \"\"\"\n        :rtype: bool\n        \"\"\"\n\n\n    def one(self):\n        \"\"\"\n        :rtype: bool\n        \"\"\"\n\n\n    def count(self):\n        \"\"\"\n        :rtype: int\n        \"\"\"\n\n\n    def toString(self):\n        \"\"\"\n        :rtype: str\n        \"\"\"\n\n\n\n# Your Bitset object will be instantiated and called as such:\n# obj = Bitset(size)\n# obj.fix(idx)\n# obj.unfix(idx)\n# obj.flip()\n# param_4 = obj.all()\n# param_5 = obj.one()\n# param_6 = obj.count()\n# param_7 = obj.toString()"
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "class Bitset:\n\n    def __init__(self, size: int):\n\n\n    def fix(self, idx: int) -> None:\n\n\n    def unfix(self, idx: int) -> None:\n\n\n    def flip(self) -> None:\n\n\n    def all(self) -> bool:\n\n\n    def one(self) -> bool:\n\n\n    def count(self) -> int:\n\n\n    def toString(self) -> str:\n\n\n\n# Your Bitset object will be instantiated and called as such:\n# obj = Bitset(size)\n# obj.fix(idx)\n# obj.unfix(idx)\n# obj.flip()\n# param_4 = obj.all()\n# param_5 = obj.one()\n# param_6 = obj.count()\n# param_7 = obj.toString()"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "\n\n\ntypedef struct {\n    \n} Bitset;\n\n\nBitset* bitsetCreate(int size) {\n    \n}\n\nvoid bitsetFix(Bitset* obj, int idx) {\n    \n}\n\nvoid bitsetUnfix(Bitset* obj, int idx) {\n    \n}\n\nvoid bitsetFlip(Bitset* obj) {\n    \n}\n\nbool bitsetAll(Bitset* obj) {\n    \n}\n\nbool bitsetOne(Bitset* obj) {\n    \n}\n\nint bitsetCount(Bitset* obj) {\n    \n}\n\nchar* bitsetToString(Bitset* obj) {\n    \n}\n\nvoid bitsetFree(Bitset* obj) {\n    \n}\n\n/**\n * Your Bitset struct will be instantiated and called as such:\n * Bitset* obj = bitsetCreate(size);\n * bitsetFix(obj, idx);\n \n * bitsetUnfix(obj, idx);\n \n * bitsetFlip(obj);\n \n * bool param_4 = bitsetAll(obj);\n \n * bool param_5 = bitsetOne(obj);\n \n * int param_6 = bitsetCount(obj);\n \n * char* param_7 = bitsetToString(obj);\n \n * bitsetFree(obj);\n*/"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "public class Bitset {\n\n    public Bitset(int size) {\n\n    }\n    \n    public void Fix(int idx) {\n\n    }\n    \n    public void Unfix(int idx) {\n\n    }\n    \n    public void Flip() {\n\n    }\n    \n    public bool All() {\n\n    }\n    \n    public bool One() {\n\n    }\n    \n    public int Count() {\n\n    }\n    \n    public string ToString() {\n\n    }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * Bitset obj = new Bitset(size);\n * obj.Fix(idx);\n * obj.Unfix(idx);\n * obj.Flip();\n * bool param_4 = obj.All();\n * bool param_5 = obj.One();\n * int param_6 = obj.Count();\n * string param_7 = obj.ToString();\n */"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * @param {number} size\n */\nvar Bitset = function(size) {\n\n};\n\n/** \n * @param {number} idx\n * @return {void}\n */\nBitset.prototype.fix = function(idx) {\n\n};\n\n/** \n * @param {number} idx\n * @return {void}\n */\nBitset.prototype.unfix = function(idx) {\n\n};\n\n/**\n * @return {void}\n */\nBitset.prototype.flip = function() {\n\n};\n\n/**\n * @return {boolean}\n */\nBitset.prototype.all = function() {\n\n};\n\n/**\n * @return {boolean}\n */\nBitset.prototype.one = function() {\n\n};\n\n/**\n * @return {number}\n */\nBitset.prototype.count = function() {\n\n};\n\n/**\n * @return {string}\n */\nBitset.prototype.toString = function() {\n\n};\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * var obj = new Bitset(size)\n * obj.fix(idx)\n * obj.unfix(idx)\n * obj.flip()\n * var param_4 = obj.all()\n * var param_5 = obj.one()\n * var param_6 = obj.count()\n * var param_7 = obj.toString()\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "class Bitset {\n    constructor(size: number) {\n        \n    }\n\n    fix(idx: number): void {\n        \n    }\n\n    unfix(idx: number): void {\n        \n    }\n\n    flip(): void {\n        \n    }\n\n    all(): boolean {\n        \n    }\n\n    one(): boolean {\n        \n    }\n\n    count(): number {\n        \n    }\n\n    toString(): string {\n        \n    }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * var obj = new Bitset(size)\n * obj.fix(idx)\n * obj.unfix(idx)\n * obj.flip()\n * var param_4 = obj.all()\n * var param_5 = obj.one()\n * var param_6 = obj.count()\n * var param_7 = obj.toString()\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "class Bitset {\n    /**\n     * @param Integer $size\n     */\n    function __construct($size) {\n\n    }\n\n    /**\n     * @param Integer $idx\n     * @return NULL\n     */\n    function fix($idx) {\n\n    }\n\n    /**\n     * @param Integer $idx\n     * @return NULL\n     */\n    function unfix($idx) {\n\n    }\n\n    /**\n     * @return NULL\n     */\n    function flip() {\n\n    }\n\n    /**\n     * @return Boolean\n     */\n    function all() {\n\n    }\n\n    /**\n     * @return Boolean\n     */\n    function one() {\n\n    }\n\n    /**\n     * @return Integer\n     */\n    function count() {\n\n    }\n\n    /**\n     * @return String\n     */\n    function toString() {\n\n    }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * $obj = Bitset($size);\n * $obj->fix($idx);\n * $obj->unfix($idx);\n * $obj->flip();\n * $ret_4 = $obj->all();\n * $ret_5 = $obj->one();\n * $ret_6 = $obj->count();\n * $ret_7 = $obj->toString();\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "\nclass Bitset {\n\n    init(_ size: Int) {\n\n    }\n    \n    func fix(_ idx: Int) {\n\n    }\n    \n    func unfix(_ idx: Int) {\n\n    }\n    \n    func flip() {\n\n    }\n    \n    func all() -> Bool {\n\n    }\n    \n    func one() -> Bool {\n\n    }\n    \n    func count() -> Int {\n\n    }\n    \n    func toString() -> String {\n\n    }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * let obj = Bitset(size)\n * obj.fix(idx)\n * obj.unfix(idx)\n * obj.flip()\n * let ret_4: Bool = obj.all()\n * let ret_5: Bool = obj.one()\n * let ret_6: Int = obj.count()\n * let ret_7: String = obj.toString()\n */"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "class Bitset(size: Int) {\n\n    fun fix(idx: Int) {\n\n    }\n\n    fun unfix(idx: Int) {\n\n    }\n\n    fun flip() {\n\n    }\n\n    fun all(): Boolean {\n\n    }\n\n    fun one(): Boolean {\n\n    }\n\n    fun count(): Int {\n\n    }\n\n    fun toString(): String {\n\n    }\n\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * var obj = Bitset(size)\n * obj.fix(idx)\n * obj.unfix(idx)\n * obj.flip()\n * var param_4 = obj.all()\n * var param_5 = obj.one()\n * var param_6 = obj.count()\n * var param_7 = obj.toString()\n */"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "class Bitset {\n\n  Bitset(int size) {\n    \n  }\n  \n  void fix(int idx) {\n    \n  }\n  \n  void unfix(int idx) {\n    \n  }\n  \n  void flip() {\n    \n  }\n  \n  bool all() {\n    \n  }\n  \n  bool one() {\n    \n  }\n  \n  int count() {\n    \n  }\n  \n  String toString() {\n    \n  }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * Bitset obj = Bitset(size);\n * obj.fix(idx);\n * obj.unfix(idx);\n * obj.flip();\n * bool param4 = obj.all();\n * bool param5 = obj.one();\n * int param6 = obj.count();\n * String param7 = obj.toString();\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "type Bitset struct {\n\n}\n\n\nfunc Constructor(size int) Bitset {\n\n}\n\n\nfunc (this *Bitset) Fix(idx int)  {\n\n}\n\n\nfunc (this *Bitset) Unfix(idx int)  {\n\n}\n\n\nfunc (this *Bitset) Flip()  {\n\n}\n\n\nfunc (this *Bitset) All() bool {\n\n}\n\n\nfunc (this *Bitset) One() bool {\n\n}\n\n\nfunc (this *Bitset) Count() int {\n\n}\n\n\nfunc (this *Bitset) ToString() string {\n\n}\n\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * obj := Constructor(size);\n * obj.Fix(idx);\n * obj.Unfix(idx);\n * obj.Flip();\n * param_4 := obj.All();\n * param_5 := obj.One();\n * param_6 := obj.Count();\n * param_7 := obj.ToString();\n */"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "class Bitset\n\n=begin\n    :type size: Integer\n=end\n    def initialize(size)\n        \n    end\n\n\n=begin\n    :type idx: Integer\n    :rtype: Void\n=end\n    def fix(idx)\n        \n    end\n\n\n=begin\n    :type idx: Integer\n    :rtype: Void\n=end\n    def unfix(idx)\n        \n    end\n\n\n=begin\n    :rtype: Void\n=end\n    def flip()\n        \n    end\n\n\n=begin\n    :rtype: Boolean\n=end\n    def all()\n        \n    end\n\n\n=begin\n    :rtype: Boolean\n=end\n    def one()\n        \n    end\n\n\n=begin\n    :rtype: Integer\n=end\n    def count()\n        \n    end\n\n\n=begin\n    :rtype: String\n=end\n    def to_string()\n        \n    end\n\n\nend\n\n# Your Bitset object will be instantiated and called as such:\n# obj = Bitset.new(size)\n# obj.fix(idx)\n# obj.unfix(idx)\n# obj.flip()\n# param_4 = obj.all()\n# param_5 = obj.one()\n# param_6 = obj.count()\n# param_7 = obj.to_string()"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "class Bitset(_size: Int) {\n\n    def fix(idx: Int): Unit = {\n        \n    }\n\n    def unfix(idx: Int): Unit = {\n        \n    }\n\n    def flip(): Unit = {\n        \n    }\n\n    def all(): Boolean = {\n        \n    }\n\n    def one(): Boolean = {\n        \n    }\n\n    def count(): Int = {\n        \n    }\n\n    def toString(): String = {\n        \n    }\n\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * val obj = new Bitset(size)\n * obj.fix(idx)\n * obj.unfix(idx)\n * obj.flip()\n * val param_4 = obj.all()\n * val param_5 = obj.one()\n * val param_6 = obj.count()\n * val param_7 = obj.toString()\n */"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "struct Bitset {\n\n}\n\n\n/**\n * `&self` means the method takes an immutable reference.\n * If you need a mutable reference, change it to `&mut self` instead.\n */\nimpl Bitset {\n\n    fn new(size: i32) -> Self {\n\n    }\n    \n    fn fix(&self, idx: i32) {\n\n    }\n    \n    fn unfix(&self, idx: i32) {\n\n    }\n    \n    fn flip(&self) {\n\n    }\n    \n    fn all(&self) -> bool {\n\n    }\n    \n    fn one(&self) -> bool {\n\n    }\n    \n    fn count(&self) -> i32 {\n\n    }\n    \n    fn to_string(&self) -> String {\n\n    }\n}\n\n/**\n * Your Bitset object will be instantiated and called as such:\n * let obj = Bitset::new(size);\n * obj.fix(idx);\n * obj.unfix(idx);\n * obj.flip();\n * let ret_4: bool = obj.all();\n * let ret_5: bool = obj.one();\n * let ret_6: i32 = obj.count();\n * let ret_7: String = obj.to_string();\n */"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "(define bitset%\n  (class object%\n    (super-new)\n    \n    ; size : exact-integer?\n    (init-field\n      size)\n    \n    ; fix : exact-integer? -> void?\n    (define/public (fix idx)\n      )\n    ; unfix : exact-integer? -> void?\n    (define/public (unfix idx)\n      )\n    ; flip : -> void?\n    (define/public (flip)\n      )\n    ; all : -> boolean?\n    (define/public (all)\n      )\n    ; one : -> boolean?\n    (define/public (one)\n      )\n    ; count : -> exact-integer?\n    (define/public (count)\n      )\n    ; to-string : -> string?\n    (define/public (to-string)\n      )))\n\n;; Your bitset% object will be instantiated and called as such:\n;; (define obj (new bitset% [size size]))\n;; (send obj fix idx)\n;; (send obj unfix idx)\n;; (send obj flip)\n;; (define param_4 (send obj all))\n;; (define param_5 (send obj one))\n;; (define param_6 (send obj count))\n;; (define param_7 (send obj to-string))"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "-spec bitset_init_(Size :: integer()) -> any().\nbitset_init_(Size) ->\n  .\n\n-spec bitset_fix(Idx :: integer()) -> any().\nbitset_fix(Idx) ->\n  .\n\n-spec bitset_unfix(Idx :: integer()) -> any().\nbitset_unfix(Idx) ->\n  .\n\n-spec bitset_flip() -> any().\nbitset_flip() ->\n  .\n\n-spec bitset_all() -> boolean().\nbitset_all() ->\n  .\n\n-spec bitset_one() -> boolean().\nbitset_one() ->\n  .\n\n-spec bitset_count() -> integer().\nbitset_count() ->\n  .\n\n-spec bitset_to_string() -> unicode:unicode_binary().\nbitset_to_string() ->\n  .\n\n\n%% Your functions will be called as such:\n%% bitset_init_(Size),\n%% bitset_fix(Idx),\n%% bitset_unfix(Idx),\n%% bitset_flip(),\n%% Param_4 = bitset_all(),\n%% Param_5 = bitset_one(),\n%% Param_6 = bitset_count(),\n%% Param_7 = bitset_to_string(),\n\n%% bitset_init_ will be called before every test case, in which you can do some necessary initializations."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "defmodule Bitset do\n  @spec init_(size :: integer) :: any\n  def init_(size) do\n    \n  end\n\n  @spec fix(idx :: integer) :: any\n  def fix(idx) do\n    \n  end\n\n  @spec unfix(idx :: integer) :: any\n  def unfix(idx) do\n    \n  end\n\n  @spec flip() :: any\n  def flip() do\n    \n  end\n\n  @spec all() :: boolean\n  def all() do\n    \n  end\n\n  @spec one() :: boolean\n  def one() do\n    \n  end\n\n  @spec count() :: integer\n  def count() do\n    \n  end\n\n  @spec to_string() :: String.t\n  def to_string() do\n    \n  end\nend\n\n# Your functions will be called as such:\n# Bitset.init_(size)\n# Bitset.fix(idx)\n# Bitset.unfix(idx)\n# Bitset.flip()\n# param_4 = Bitset.all()\n# param_5 = Bitset.one()\n# param_6 = Bitset.count()\n# param_7 = Bitset.to_string()\n\n# Bitset.init_ will be called before every test case, in which you can do some necessary initializations."
    }
]
problems["919"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass CBTInserter {\npublic:\n    CBTInserter(TreeNode* root) {\n\n    }\n    \n    int insert(int val) {\n\n    }\n    \n    TreeNode* get_root() {\n\n    }\n};\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * CBTInserter* obj = new CBTInserter(root);\n * int param_1 = obj->insert(val);\n * TreeNode* param_2 = obj->get_root();\n */"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass CBTInserter {\n\n    public CBTInserter(TreeNode root) {\n\n    }\n    \n    public int insert(int val) {\n\n    }\n    \n    public TreeNode get_root() {\n\n    }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * CBTInserter obj = new CBTInserter(root);\n * int param_1 = obj.insert(val);\n * TreeNode param_2 = obj.get_root();\n */"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass CBTInserter(object):\n\n    def __init__(self, root):\n        \"\"\"\n        :type root: TreeNode\n        \"\"\"\n        \n\n    def insert(self, val):\n        \"\"\"\n        :type val: int\n        :rtype: int\n        \"\"\"\n        \n\n    def get_root(self):\n        \"\"\"\n        :rtype: TreeNode\n        \"\"\"\n        \n\n\n# Your CBTInserter object will be instantiated and called as such:\n# obj = CBTInserter(root)\n# param_1 = obj.insert(val)\n# param_2 = obj.get_root()"
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass CBTInserter:\n\n    def __init__(self, root: Optional[TreeNode]):\n\n\n    def insert(self, val: int) -> int:\n\n\n    def get_root(self) -> Optional[TreeNode]:\n\n\n\n# Your CBTInserter object will be instantiated and called as such:\n# obj = CBTInserter(root)\n# param_1 = obj.insert(val)\n# param_2 = obj.get_root()"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n */\n\n\n\ntypedef struct {\n    \n} CBTInserter;\n\n\nCBTInserter* cBTInserterCreate(struct TreeNode* root) {\n    \n}\n\nint cBTInserterInsert(CBTInserter* obj, int val) {\n    \n}\n\nstruct TreeNode* cBTInserterGet_root(CBTInserter* obj) {\n    \n}\n\nvoid cBTInserterFree(CBTInserter* obj) {\n    \n}\n\n/**\n * Your CBTInserter struct will be instantiated and called as such:\n * CBTInserter* obj = cBTInserterCreate(root);\n * int param_1 = cBTInserterInsert(obj, val);\n \n * struct TreeNode* param_2 = cBTInserterGet_root(obj);\n \n * cBTInserterFree(obj);\n*/"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\npublic class CBTInserter {\n\n    public CBTInserter(TreeNode root) {\n\n    }\n    \n    public int Insert(int val) {\n\n    }\n    \n    public TreeNode Get_root() {\n\n    }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * CBTInserter obj = new CBTInserter(root);\n * int param_1 = obj.Insert(val);\n * TreeNode param_2 = obj.Get_root();\n */"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n */\nvar CBTInserter = function(root) {\n\n};\n\n/** \n * @param {number} val\n * @return {number}\n */\nCBTInserter.prototype.insert = function(val) {\n\n};\n\n/**\n * @return {TreeNode}\n */\nCBTInserter.prototype.get_root = function() {\n\n};\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * var obj = new CBTInserter(root)\n * var param_1 = obj.insert(val)\n * var param_2 = obj.get_root()\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     val: number\n *     left: TreeNode | null\n *     right: TreeNode | null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left = (left===undefined ? null : left)\n *         this.right = (right===undefined ? null : right)\n *     }\n * }\n */\n\nclass CBTInserter {\n    constructor(root: TreeNode | null) {\n        \n    }\n\n    insert(val: number): number {\n        \n    }\n\n    get_root(): TreeNode | null {\n        \n    }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * var obj = new CBTInserter(root)\n * var param_1 = obj.insert(val)\n * var param_2 = obj.get_root()\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     public $val = null;\n *     public $left = null;\n *     public $right = null;\n *     function __construct($val = 0, $left = null, $right = null) {\n *         $this->val = $val;\n *         $this->left = $left;\n *         $this->right = $right;\n *     }\n * }\n */\nclass CBTInserter {\n    /**\n     * @param TreeNode $root\n     */\n    function __construct($root) {\n\n    }\n\n    /**\n     * @param Integer $val\n     * @return Integer\n     */\n    function insert($val) {\n\n    }\n\n    /**\n     * @return TreeNode\n     */\n    function get_root() {\n\n    }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * $obj = CBTInserter($root);\n * $ret_1 = $obj->insert($val);\n * $ret_2 = $obj->get_root();\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     public var val: Int\n *     public var left: TreeNode?\n *     public var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil; self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n *         self.right = right\n *     }\n * }\n */\n\nclass CBTInserter {\n\n    init(_ root: TreeNode?) {\n\n    }\n    \n    func insert(_ val: Int) -> Int {\n\n    }\n    \n    func get_root() -> TreeNode? {\n\n    }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * let obj = CBTInserter(root)\n * let ret_1: Int = obj.insert(val)\n * let ret_2: TreeNode? = obj.get_root()\n */"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "/**\n * Example:\n * var ti = TreeNode(5)\n * var v = ti.`val`\n * Definition for a binary tree node.\n * class TreeNode(var `val`: Int) {\n *     var left: TreeNode? = null\n *     var right: TreeNode? = null\n * }\n */\nclass CBTInserter(root: TreeNode?) {\n\n    fun insert(`val`: Int): Int {\n\n    }\n\n    fun get_root(): TreeNode? {\n\n    }\n\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * var obj = CBTInserter(root)\n * var param_1 = obj.insert(`val`)\n * var param_2 = obj.get_root()\n */"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *   int val;\n *   TreeNode? left;\n *   TreeNode? right;\n *   TreeNode([this.val = 0, this.left, this.right]);\n * }\n */\nclass CBTInserter {\n\n  CBTInserter(TreeNode? root) {\n    \n  }\n  \n  int insert(int val) {\n    \n  }\n  \n  TreeNode? get_root() {\n    \n  }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * CBTInserter obj = CBTInserter(root);\n * int param1 = obj.insert(val);\n * TreeNode? param2 = obj.get_root();\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\ntype CBTInserter struct {\n\n}\n\n\nfunc Constructor(root *TreeNode) CBTInserter {\n\n}\n\n\nfunc (this *CBTInserter) Insert(val int) int {\n\n}\n\n\nfunc (this *CBTInserter) Get_root() *TreeNode {\n\n}\n\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * obj := Constructor(root);\n * param_1 := obj.Insert(val);\n * param_2 := obj.Get_root();\n */"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\nclass CBTInserter\n\n=begin\n    :type root: TreeNode\n=end\n    def initialize(root)\n\n    end\n\n\n=begin\n    :type val: Integer\n    :rtype: Integer\n=end\n    def insert(val)\n\n    end\n\n\n=begin\n    :rtype: TreeNode\n=end\n    def get_root()\n\n    end\n\n\nend\n\n# Your CBTInserter object will be instantiated and called as such:\n# obj = CBTInserter.new(root)\n# param_1 = obj.insert(val)\n# param_2 = obj.get_root()"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {\n *   var value: Int = _value\n *   var left: TreeNode = _left\n *   var right: TreeNode = _right\n * }\n */\nclass CBTInserter(_root: TreeNode) {\n\n    def insert(`val`: Int): Int = {\n\n    }\n\n    def get_root(): TreeNode = {\n\n    }\n\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * var obj = new CBTInserter(root)\n * var param_1 = obj.insert(`val`)\n * var param_2 = obj.get_root()\n */"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "// Definition for a binary tree node.\n// #[derive(Debug, PartialEq, Eq)]\n// pub struct TreeNode {\n//   pub val: i32,\n//   pub left: Option<Rc<RefCell<TreeNode>>>,\n//   pub right: Option<Rc<RefCell<TreeNode>>>,\n// }\n//\n// impl TreeNode {\n//   #[inline]\n//   pub fn new(val: i32) -> Self {\n//     TreeNode {\n//       val,\n//       left: None,\n//       right: None\n//     }\n//   }\n// }\nstruct CBTInserter {\n\n}\n\n\n/**\n * `&self` means the method takes an immutable reference.\n * If you need a mutable reference, change it to `&mut self` instead.\n */\nimpl CBTInserter {\n\n    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {\n\n    }\n    \n    fn insert(&self, val: i32) -> i32 {\n\n    }\n    \n    fn get_root(&self) -> Option<Rc<RefCell<TreeNode>>> {\n\n    }\n}\n\n/**\n * Your CBTInserter object will be instantiated and called as such:\n * let obj = CBTInserter::new(root);\n * let ret_1: i32 = obj.insert(val);\n * let ret_2: Option<Rc<RefCell<TreeNode>>> = obj.get_root();\n */"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "; Definition for a binary tree node.\n#|\n\n; val : integer?\n; left : (or/c tree-node? #f)\n; right : (or/c tree-node? #f)\n(struct tree-node\n  (val left right) #:mutable #:transparent)\n\n; constructor\n(define (make-tree-node [val 0])\n  (tree-node val #f #f))\n\n|#\n\n(define cbt-inserter%\n  (class object%\n    (super-new)\n    \n    ; root : (or/c tree-node? #f)\n    (init-field\n      root)\n    \n    ; insert : exact-integer? -> exact-integer?\n    (define/public (insert val)\n      )\n    ; get_root : -> (or/c tree-node? #f)\n    (define/public (get_root)\n      )))\n\n;; Your cbt-inserter% object will be instantiated and called as such:\n;; (define obj (new cbt-inserter% [root root]))\n;; (define param_1 (send obj insert val))\n;; (define param_2 (send obj get_root))"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "%% Definition for a binary tree node.\n%%\n%% -record(tree_node, {val = 0 :: integer(),\n%%                     left = null  :: 'null' | #tree_node{},\n%%                     right = null :: 'null' | #tree_node{}}).\n\n-spec cbt_inserter_init_(Root :: #tree_node{} | null) -> any().\ncbt_inserter_init_(Root) ->\n  .\n\n-spec cbt_inserter_insert(Val :: integer()) -> integer().\ncbt_inserter_insert(Val) ->\n  .\n\n-spec cbt_inserter_get_root() -> #tree_node{} | null.\ncbt_inserter_get_root() ->\n  .\n\n\n%% Your functions will be called as such:\n%% cbt_inserter_init_(Root),\n%% Param_1 = cbt_inserter_insert(Val),\n%% Param_2 = cbt_inserter_get_root(),\n\n%% cbt_inserter_init_ will be called before every test case, in which you can do some necessary initializations."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "# Definition for a binary tree node.\n#\n# defmodule TreeNode do\n#   @type t :: %__MODULE__{\n#           val: integer,\n#           left: TreeNode.t() | nil,\n#           right: TreeNode.t() | nil\n#         }\n#   defstruct val: 0, left: nil, right: nil\n# end\n\ndefmodule CBTInserter do\n  @spec init_(root :: TreeNode.t | nil) :: any\n  def init_(root) do\n    \n  end\n\n  @spec insert(val :: integer) :: integer\n  def insert(val) do\n    \n  end\n\n  @spec get_root() :: TreeNode.t | nil\n  def get_root() do\n    \n  end\nend\n\n# Your functions will be called as such:\n# CBTInserter.init_(root)\n# param_1 = CBTInserter.insert(val)\n# param_2 = CBTInserter.get_root()\n\n# CBTInserter.init_ will be called before every test case, in which you can do some necessary initializations."
    }
]
problems["449"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n * };\n */\nclass Codec {\npublic:\n\n    // Encodes a tree to a single string.\n    string serialize(TreeNode* root) {\n        \n    }\n\n    // Decodes your encoded data to tree.\n    TreeNode* deserialize(string data) {\n        \n    }\n};\n\n// Your Codec object will be instantiated and called as such:\n// Codec* ser = new Codec();\n// Codec* deser = new Codec();\n// string tree = ser->serialize(root);\n// TreeNode* ans = deser->deserialize(tree);\n// return ans;"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode(int x) { val = x; }\n * }\n */\npublic class Codec {\n\n    // Encodes a tree to a single string.\n    public String serialize(TreeNode root) {\n        \n    }\n\n    // Decodes your encoded data to tree.\n    public TreeNode deserialize(String data) {\n        \n    }\n}\n\n// Your Codec object will be instantiated and called as such:\n// Codec ser = new Codec();\n// Codec deser = new Codec();\n// String tree = ser.serialize(root);\n// TreeNode ans = deser.deserialize(tree);\n// return ans;"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, x):\n#         self.val = x\n#         self.left = None\n#         self.right = None\n\nclass Codec:\n\n    def serialize(self, root):\n        \"\"\"Encodes a tree to a single string.\n        \n        :type root: TreeNode\n        :rtype: str\n        \"\"\"\n        \n\n    def deserialize(self, data):\n        \"\"\"Decodes your encoded data to tree.\n        \n        :type data: str\n        :rtype: TreeNode\n        \"\"\"\n        \n\n# Your Codec object will be instantiated and called as such:\n# ser = Codec()\n# deser = Codec()\n# tree = ser.serialize(root)\n# ans = deser.deserialize(tree)\n# return ans"
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, x):\n#         self.val = x\n#         self.left = None\n#         self.right = None\n\nclass Codec:\n\n    def serialize(self, root: Optional[TreeNode]) -> str:\n        \"\"\"Encodes a tree to a single string.\n        \"\"\"\n        \n\n    def deserialize(self, data: str) -> Optional[TreeNode]:\n        \"\"\"Decodes your encoded data to tree.\n        \"\"\"\n        \n\n# Your Codec object will be instantiated and called as such:\n# Your Codec object will be instantiated and called as such:\n# ser = Codec()\n# deser = Codec()\n# tree = ser.serialize(root)\n# ans = deser.deserialize(tree)\n# return ans"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n */\n/** Encodes a tree to a single string. */\nchar* serialize(struct TreeNode* root) {\n    \n}\n\n/** Decodes your encoded data to tree. */\nstruct TreeNode* deserialize(char* data) {\n    \n}\n\n// Your functions will be called as such:\n// char* data = serialize(root);\n// deserialize(data);"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode right;\n *     public TreeNode(int x) { val = x; }\n * }\n */\npublic class Codec {\n\n    // Encodes a tree to a single string.\n    public string serialize(TreeNode root) {\n        \n    }\n\n    // Decodes your encoded data to tree.\n    public TreeNode deserialize(string data) {\n        \n    }\n}\n\n// Your Codec object will be instantiated and called as such:\n// Codec ser = new Codec();\n// Codec deser = new Codec();\n// String tree = ser.serialize(root);\n// TreeNode ans = deser.deserialize(tree);\n// return ans;"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * Definition for a binary tree node.\n * function TreeNode(val) {\n *     this.val = val;\n *     this.left = this.right = null;\n * }\n */\n\n/**\n * Encodes a tree to a single string.\n *\n * @param {TreeNode} root\n * @return {string}\n */\nvar serialize = function(root) {\n    \n};\n\n/**\n * Decodes your encoded data to tree.\n *\n * @param {string} data\n * @return {TreeNode}\n */\nvar deserialize = function(data) {\n    \n};\n\n/**\n * Your functions will be called as such:\n * deserialize(serialize(root));\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     val: number\n *     left: TreeNode | null\n *     right: TreeNode | null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left = (left===undefined ? null : left)\n *         this.right = (right===undefined ? null : right)\n *     }\n * }\n */\n\n/*\n * Encodes a tree to a single string.\n */\nfunction serialize(root: TreeNode | null): string {\n\n};\n\n/*\n * Decodes your encoded data to tree.\n */\nfunction deserialize(data: string): TreeNode | null {\n\n};\n\n\n/**\n * Your functions will be called as such:\n * deserialize(serialize(root));\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     public $val = null;\n *     public $left = null;\n *     public $right = null;\n *     function __construct($value) { $this->val = $value; }\n * }\n */\n\nclass Codec {\n    function __construct() {\n        \n    }\n  \n    /**\n     * @param TreeNode $root\n     * @return String\n     */\n    function serialize($root) {\n        \n    }\n  \n    /**\n     * @param String $data\n     * @return TreeNode\n     */\n    function deserialize($data) {\n        \n    }\n}\n\n/**\n * Your Codec object will be instantiated and called as such:\n * $ser = new Codec();\n * $tree = $ser->serialize($param_1);\n * $deser = new Codec();\n * $ret = $deser->deserialize($tree);\n * return $ret;\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     public var val: Int\n *     public var left: TreeNode?\n *     public var right: TreeNode?\n *     public init(_ val: Int) {\n *         self.val = val\n *         self.left = nil\n *         self.right = nil\n *     }\n * }\n */\n\nclass Codec {\n    // Encodes a tree to a single string.\n    func serialize(_ root: TreeNode?) -> String {\n        \n    }\n    \n    // Decodes your encoded data to tree.\n    func deserialize(_ data: String) -> TreeNode? {\n        \n    }\n}\n\n/**\n * Your Codec object will be instantiated and called as such:\n * let ser = Codec()\n * let deser = Codec()\n * let tree: String = ser.serialize(root)\n * let ans = deser.deserialize(tree)\n * return ans\n*/"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode(var `val`: Int) {\n *     var left: TreeNode? = null\n *     var right: TreeNode? = null\n * }\n */\n\nclass Codec() {\n\t// Encodes a tree to a single string.\n    fun serialize(root: TreeNode?): String {\n        \n    }\n\n    // Decodes your encoded data to tree.\n    fun deserialize(data: String): TreeNode? {\n        \n    }\n}\n\n/**\n * Your Codec object will be instantiated and called as such:\n * val ser = Codec()\n * val deser = Codec()\n * val tree: String = ser.serialize(root)\n * val ans = deser.deserialize(tree)\n * return ans\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\n\ntype Codec struct {\n    \n}\n\nfunc Constructor() Codec {\n    \n}\n\n// Serializes a tree to a single string.\nfunc (this *Codec) serialize(root *TreeNode) string {\n    \n}\n\n// Deserializes your encoded data to tree.\nfunc (this *Codec) deserialize(data string) *TreeNode {    \n    \n}\n\n\n/**\n * Your Codec object will be instantiated and called as such:\n * ser := Constructor()\n * deser := Constructor()\n * tree := ser.serialize(root)\n * ans := deser.deserialize(tree)\n * return ans\n */"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val)\n#         @val = val\n#         @left, @right = nil, nil\n#     end\n# end\n\n# Encodes a tree to a single string.\n#\n# @param {TreeNode} root\n# @return {string}\ndef serialize(root)\n    \nend\n\n# Decodes your encoded data to tree.\n#\n# @param {string} data\n# @return {TreeNode}\ndef deserialize(data)\n    \nend\n\n\n# Your functions will be called as such:\n# deserialize(serialize(data))"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode(var _value: Int) {\n *   var value: Int = _value\n *   var left: TreeNode = null\n *   var right: TreeNode = null\n * }\n */\n\nclass Codec {\n    // Encodes a tree to a single string.\n    def serialize(root: TreeNode): String = {\n        \n    }\n    \n    // Decodes your encoded data to tree.\n    def deserialize(data: String): TreeNode = {\n        \n    }\n}\n\n/**\n * Your Codec object will be instantiated and called as such:\n * val ser = new Codec()\n * val deser = new Codec()\n * val tree: String = ser.serialize(root)\n * val ans = deser.deserialize(tree)\n * return ans\n */"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "// Definition for a binary tree node.\n// #[derive(Debug, PartialEq, Eq)]\n// pub struct TreeNode {\n//   pub val: i32,\n//   pub left: Option<Rc<RefCell<TreeNode>>>,\n//   pub right: Option<Rc<RefCell<TreeNode>>>,\n// }\n// \n// impl TreeNode {\n//   #[inline]\n//   pub fn new(val: i32) -> Self {\n//     TreeNode {\n//       val,\n//       left: None,\n//       right: None\n//     }\n//   }\n// }\nuse std::rc::Rc;\nuse std::cell::RefCell;\nstruct Codec {\n\t\n}\n\n/** \n * `&self` means the method takes an immutable reference.\n * If you need a mutable reference, change it to `&mut self` instead.\n */\nimpl Codec {\n    fn new() -> Self {\n        \n    }\n\n    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {\n        \n    }\n\t\n    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {\n        \n    }\n}\n\n/**\n * Your Codec object will be instantiated and called as such:\n * let obj = Codec::new();\n * let data: String = obj.serialize(strs);\n * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);\n */"
    }
]
problems["133"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/*\n// Definition for a Node.\nclass Node {\npublic:\n    int val;\n    vector<Node*> neighbors;\n    Node() {\n        val = 0;\n        neighbors = vector<Node*>();\n    }\n    Node(int _val) {\n        val = _val;\n        neighbors = vector<Node*>();\n    }\n    Node(int _val, vector<Node*> _neighbors) {\n        val = _val;\n        neighbors = _neighbors;\n    }\n};\n*/\n\nclass Solution {\npublic:\n    Node* cloneGraph(Node* node) {\n        \n    }\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "/*\n// Definition for a Node.\nclass Node {\n    public int val;\n    public List<Node> neighbors;\n    public Node() {\n        val = 0;\n        neighbors = new ArrayList<Node>();\n    }\n    public Node(int _val) {\n        val = _val;\n        neighbors = new ArrayList<Node>();\n    }\n    public Node(int _val, ArrayList<Node> _neighbors) {\n        val = _val;\n        neighbors = _neighbors;\n    }\n}\n*/\n\nclass Solution {\n    public Node cloneGraph(Node node) {\n        \n    }\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "\"\"\"\n# Definition for a Node.\nclass Node(object):\n    def __init__(self, val = 0, neighbors = None):\n        self.val = val\n        self.neighbors = neighbors if neighbors is not None else []\n\"\"\"\n\nclass Solution(object):\n    def cloneGraph(self, node):\n        \"\"\"\n        :type node: Node\n        :rtype: Node\n        \"\"\"\n        "
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "\"\"\"\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        self.val = val\n        self.neighbors = neighbors if neighbors is not None else []\n\"\"\"\n\nfrom typing import Optional\nclass Solution:\n    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:\n        "
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Definition for a Node.\n * struct Node {\n *     int val;\n *     int numNeighbors;\n *     struct Node** neighbors;\n * };\n */\n\nstruct Node *cloneGraph(struct Node *s) {\n\t\n}"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "/*\n// Definition for a Node.\npublic class Node {\n    public int val;\n    public IList<Node> neighbors;\n\n    public Node() {\n        val = 0;\n        neighbors = new List<Node>();\n    }\n\n    public Node(int _val) {\n        val = _val;\n        neighbors = new List<Node>();\n    }\n\n    public Node(int _val, List<Node> _neighbors) {\n        val = _val;\n        neighbors = _neighbors;\n    }\n}\n*/\n\npublic class Solution {\n    public Node CloneGraph(Node node) {\n        \n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * // Definition for a Node.\n * function Node(val, neighbors) {\n *    this.val = val === undefined ? 0 : val;\n *    this.neighbors = neighbors === undefined ? [] : neighbors;\n * };\n */\n\n/**\n * @param {Node} node\n * @return {Node}\n */\nvar cloneGraph = function(node) {\n    \n};"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * Definition for Node.\n * class Node {\n *     val: number\n *     neighbors: Node[]\n *     constructor(val?: number, neighbors?: Node[]) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.neighbors = (neighbors===undefined ? [] : neighbors)\n *     }\n * }\n */\n\nfunction cloneGraph(node: Node | null): Node | null {\n\t\n};"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "/**\n * Definition for a Node.\n * class Node {\n *     public $val = null;\n *     public $neighbors = null;\n *     function __construct($val = 0) {\n *         $this->val = $val;\n *         $this->neighbors = array();\n *     }\n * }\n */\n\nclass Solution {\n    /**\n     * @param Node $node\n     * @return Node\n     */\n    function cloneGraph($node) {\n        \n    }\n}"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "/**\n * Definition for a Node.\n * public class Node {\n *     public var val: Int\n *     public var neighbors: [Node?]\n *     public init(_ val: Int) {\n *         self.val = val\n *         self.neighbors = []\n *     }\n * }\n */\n\nclass Solution {\n    func cloneGraph(_ node: Node?) -> Node? {\n        \n    }\n}"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "/**\n * Definition for a Node.\n * class Node(var `val`: Int) {\n *     var neighbors: ArrayList<Node?> = ArrayList<Node?>()\n * }\n */\n\nclass Solution {\n    fun cloneGraph(node: Node?): Node? {\n        \n    }\n}"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/**\n * Definition for a Node.\n * type Node struct {\n *     Val int\n *     Neighbors []*Node\n * }\n */\n\nfunc cloneGraph(node *Node) *Node {\n    \n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Definition for a Node.\n# class Node\n#     attr_accessor :val, :neighbors\n#     def initialize(val = 0, neighbors = nil)\n#\t\t  @val = val\n#\t\t  neighbors = [] if neighbors.nil?\n#         @neighbors = neighbors\n#     end\n# end\n\n# @param {Node} node\n# @return {Node}\ndef cloneGraph(node)\n    \nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "/**\n * Definition for a Node.\n * class Node(var _value: Int) {\n *   var value: Int = _value\n *   var neighbors: List[Node] = List()\n * }\n */\n\nobject Solution {\n    def cloneGraph(graph: Node): Node = {\n        \n    }\n}"
    }
]
problems["2671"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "class FrequencyTracker {\npublic:\n    FrequencyTracker() {\n\n    }\n    \n    void add(int number) {\n\n    }\n    \n    void deleteOne(int number) {\n\n    }\n    \n    bool hasFrequency(int frequency) {\n\n    }\n};\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * FrequencyTracker* obj = new FrequencyTracker();\n * obj->add(number);\n * obj->deleteOne(number);\n * bool param_3 = obj->hasFrequency(frequency);\n */"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "class FrequencyTracker {\n\n    public FrequencyTracker() {\n\n    }\n    \n    public void add(int number) {\n\n    }\n    \n    public void deleteOne(int number) {\n\n    }\n    \n    public boolean hasFrequency(int frequency) {\n\n    }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * FrequencyTracker obj = new FrequencyTracker();\n * obj.add(number);\n * obj.deleteOne(number);\n * boolean param_3 = obj.hasFrequency(frequency);\n */"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "class FrequencyTracker(object):\n\n    def __init__(self):\n\n\n    def add(self, number):\n        \"\"\"\n        :type number: int\n        :rtype: None\n        \"\"\"\n\n\n    def deleteOne(self, number):\n        \"\"\"\n        :type number: int\n        :rtype: None\n        \"\"\"\n\n\n    def hasFrequency(self, frequency):\n        \"\"\"\n        :type frequency: int\n        :rtype: bool\n        \"\"\"\n\n\n\n# Your FrequencyTracker object will be instantiated and called as such:\n# obj = FrequencyTracker()\n# obj.add(number)\n# obj.deleteOne(number)\n# param_3 = obj.hasFrequency(frequency)"
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "class FrequencyTracker:\n\n    def __init__(self):\n\n\n    def add(self, number: int) -> None:\n\n\n    def deleteOne(self, number: int) -> None:\n\n\n    def hasFrequency(self, frequency: int) -> bool:\n\n\n\n# Your FrequencyTracker object will be instantiated and called as such:\n# obj = FrequencyTracker()\n# obj.add(number)\n# obj.deleteOne(number)\n# param_3 = obj.hasFrequency(frequency)"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "\n\n\ntypedef struct {\n    \n} FrequencyTracker;\n\n\nFrequencyTracker* frequencyTrackerCreate() {\n    \n}\n\nvoid frequencyTrackerAdd(FrequencyTracker* obj, int number) {\n  \n}\n\nvoid frequencyTrackerDeleteOne(FrequencyTracker* obj, int number) {\n  \n}\n\nbool frequencyTrackerHasFrequency(FrequencyTracker* obj, int frequency) {\n  \n}\n\nvoid frequencyTrackerFree(FrequencyTracker* obj) {\n    \n}\n\n/**\n * Your FrequencyTracker struct will be instantiated and called as such:\n * FrequencyTracker* obj = frequencyTrackerCreate();\n * frequencyTrackerAdd(obj, number);\n \n * frequencyTrackerDeleteOne(obj, number);\n \n * bool param_3 = frequencyTrackerHasFrequency(obj, frequency);\n \n * frequencyTrackerFree(obj);\n*/"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "public class FrequencyTracker {\n\n    public FrequencyTracker() {\n\n    }\n    \n    public void Add(int number) {\n\n    }\n    \n    public void DeleteOne(int number) {\n\n    }\n    \n    public bool HasFrequency(int frequency) {\n\n    }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * FrequencyTracker obj = new FrequencyTracker();\n * obj.Add(number);\n * obj.DeleteOne(number);\n * bool param_3 = obj.HasFrequency(frequency);\n */"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "\nvar FrequencyTracker = function() {\n\n};\n\n/** \n * @param {number} number\n * @return {void}\n */\nFrequencyTracker.prototype.add = function(number) {\n\n};\n\n/** \n * @param {number} number\n * @return {void}\n */\nFrequencyTracker.prototype.deleteOne = function(number) {\n\n};\n\n/** \n * @param {number} frequency\n * @return {boolean}\n */\nFrequencyTracker.prototype.hasFrequency = function(frequency) {\n\n};\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * var obj = new FrequencyTracker()\n * obj.add(number)\n * obj.deleteOne(number)\n * var param_3 = obj.hasFrequency(frequency)\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "class FrequencyTracker {\n    constructor() {\n\n    }\n\n    add(number: number): void {\n\n    }\n\n    deleteOne(number: number): void {\n\n    }\n\n    hasFrequency(frequency: number): boolean {\n\n    }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * var obj = new FrequencyTracker()\n * obj.add(number)\n * obj.deleteOne(number)\n * var param_3 = obj.hasFrequency(frequency)\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "class FrequencyTracker {\n    /**\n     */\n    function __construct() {\n\n    }\n\n    /**\n     * @param Integer $number\n     * @return NULL\n     */\n    function add($number) {\n\n    }\n\n    /**\n     * @param Integer $number\n     * @return NULL\n     */\n    function deleteOne($number) {\n\n    }\n\n    /**\n     * @param Integer $frequency\n     * @return Boolean\n     */\n    function hasFrequency($frequency) {\n\n    }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * $obj = FrequencyTracker();\n * $obj->add($number);\n * $obj->deleteOne($number);\n * $ret_3 = $obj->hasFrequency($frequency);\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "\nclass FrequencyTracker {\n\n    init() {\n\n    }\n    \n    func add(_ number: Int) {\n\n    }\n    \n    func deleteOne(_ number: Int) {\n\n    }\n    \n    func hasFrequency(_ frequency: Int) -> Bool {\n\n    }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * let obj = FrequencyTracker()\n * obj.add(number)\n * obj.deleteOne(number)\n * let ret_3: Bool = obj.hasFrequency(frequency)\n */"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "class FrequencyTracker() {\n\n    fun add(number: Int) {\n\n    }\n\n    fun deleteOne(number: Int) {\n\n    }\n\n    fun hasFrequency(frequency: Int): Boolean {\n\n    }\n\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * var obj = FrequencyTracker()\n * obj.add(number)\n * obj.deleteOne(number)\n * var param_3 = obj.hasFrequency(frequency)\n */"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "class FrequencyTracker {\n\n  FrequencyTracker() {\n\n  }\n  \n  void add(int number) {\n\n  }\n  \n  void deleteOne(int number) {\n\n  }\n  \n  bool hasFrequency(int frequency) {\n\n  }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * FrequencyTracker obj = FrequencyTracker();\n * obj.add(number);\n * obj.deleteOne(number);\n * bool param3 = obj.hasFrequency(frequency);\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "type FrequencyTracker struct {\n\n}\n\n\nfunc Constructor() FrequencyTracker {\n\n}\n\n\nfunc (this *FrequencyTracker) Add(number int)  {\n\n}\n\n\nfunc (this *FrequencyTracker) DeleteOne(number int)  {\n\n}\n\n\nfunc (this *FrequencyTracker) HasFrequency(frequency int) bool {\n\n}\n\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * obj := Constructor();\n * obj.Add(number);\n * obj.DeleteOne(number);\n * param_3 := obj.HasFrequency(frequency);\n */"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "class FrequencyTracker\n    def initialize()\n        \n    end\n\n\n=begin\n    :type number: Integer\n    :rtype: Void\n=end\n    def add(number)\n        \n    end\n\n\n=begin\n    :type number: Integer\n    :rtype: Void\n=end\n    def delete_one(number)\n        \n    end\n\n\n=begin\n    :type frequency: Integer\n    :rtype: Boolean\n=end\n    def has_frequency(frequency)\n        \n    end\n\n\nend\n\n# Your FrequencyTracker object will be instantiated and called as such:\n# obj = FrequencyTracker.new()\n# obj.add(number)\n# obj.delete_one(number)\n# param_3 = obj.has_frequency(frequency)"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "class FrequencyTracker() {\n\n    def add(number: Int): Unit = {\n        \n    }\n\n    def deleteOne(number: Int): Unit = {\n        \n    }\n\n    def hasFrequency(frequency: Int): Boolean = {\n        \n    }\n\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * val obj = new FrequencyTracker()\n * obj.add(number)\n * obj.deleteOne(number)\n * val param_3 = obj.hasFrequency(frequency)\n */"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "struct FrequencyTracker {\n\n}\n\n\n/**\n * `&self` means the method takes an immutable reference.\n * If you need a mutable reference, change it to `&mut self` instead.\n */\nimpl FrequencyTracker {\n\n    fn new() -> Self {\n\n    }\n    \n    fn add(&self, number: i32) {\n\n    }\n    \n    fn delete_one(&self, number: i32) {\n\n    }\n    \n    fn has_frequency(&self, frequency: i32) -> bool {\n\n    }\n}\n\n/**\n * Your FrequencyTracker object will be instantiated and called as such:\n * let obj = FrequencyTracker::new();\n * obj.add(number);\n * obj.delete_one(number);\n * let ret_3: bool = obj.has_frequency(frequency);\n */"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "(define frequency-tracker%\n  (class object%\n    (super-new)\n    \n    (init-field)\n    \n    ; add : exact-integer? -> void?\n    (define/public (add number)\n\n      )\n    ; delete-one : exact-integer? -> void?\n    (define/public (delete-one number)\n\n      )\n    ; has-frequency : exact-integer? -> boolean?\n    (define/public (has-frequency frequency)\n\n      )))\n\n;; Your frequency-tracker% object will be instantiated and called as such:\n;; (define obj (new frequency-tracker%))\n;; (send obj add number)\n;; (send obj delete-one number)\n;; (define param_3 (send obj has-frequency frequency))"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "-spec frequency_tracker_init_() -> any().\nfrequency_tracker_init_() ->\n  .\n\n-spec frequency_tracker_add(Number :: integer()) -> any().\nfrequency_tracker_add(Number) ->\n  .\n\n-spec frequency_tracker_delete_one(Number :: integer()) -> any().\nfrequency_tracker_delete_one(Number) ->\n  .\n\n-spec frequency_tracker_has_frequency(Frequency :: integer()) -> boolean().\nfrequency_tracker_has_frequency(Frequency) ->\n  .\n\n\n%% Your functions will be called as such:\n%% frequency_tracker_init_(),\n%% frequency_tracker_add(Number),\n%% frequency_tracker_delete_one(Number),\n%% Param_3 = frequency_tracker_has_frequency(Frequency),\n\n%% frequency_tracker_init_ will be called before every test case, in which you can do some necessary initializations."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "defmodule FrequencyTracker do\n  @spec init_() :: any\n  def init_() do\n\n  end\n\n  @spec add(number :: integer) :: any\n  def add(number) do\n\n  end\n\n  @spec delete_one(number :: integer) :: any\n  def delete_one(number) do\n\n  end\n\n  @spec has_frequency(frequency :: integer) :: boolean\n  def has_frequency(frequency) do\n\n  end\nend\n\n# Your functions will be called as such:\n# FrequencyTracker.init_()\n# FrequencyTracker.add(number)\n# FrequencyTracker.delete_one(number)\n# param_3 = FrequencyTracker.has_frequency(frequency)\n\n# FrequencyTracker.init_ will be called before every test case, in which you can do some necessary initializations."
    }
]
problems["284"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/*\n * Below is the interface for Iterator, which is already defined for you.\n * **DO NOT** modify the interface for Iterator.\n *\n *  class Iterator {\n *\t\tstruct Data;\n * \t\tData* data;\n *  public:\n *\t\tIterator(const vector<int>& nums);\n * \t\tIterator(const Iterator& iter);\n *\n * \t\t// Returns the next element in the iteration.\n *\t\tint next();\n *\n *\t\t// Returns true if the iteration has more elements.\n *\t\tbool hasNext() const;\n *\t};\n */\n\nclass PeekingIterator : public Iterator {\npublic:\n\tPeekingIterator(const vector<int>& nums) : Iterator(nums) {\n\t    // Initialize any member here.\n\t    // **DO NOT** save a copy of nums and manipulate it directly.\n\t    // You should only use the Iterator interface methods.\n\t    \n\t}\n\t\n    // Returns the next element in the iteration without advancing the iterator.\n\tint peek() {\n        \n\t}\n\t\n\t// hasNext() and next() should behave the same as in the Iterator interface.\n\t// Override them if needed.\n\tint next() {\n\t    \n\t}\n\t\n\tbool hasNext() const {\n\t    \n\t}\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "// Java Iterator interface reference:\n// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html\n\nclass PeekingIterator implements Iterator<Integer> {\n\tpublic PeekingIterator(Iterator<Integer> iterator) {\n\t    // initialize any member here.\n\t    \n\t}\n\t\n    // Returns the next element in the iteration without advancing the iterator.\n\tpublic Integer peek() {\n        \n\t}\n\t\n\t// hasNext() and next() should behave the same as in the Iterator interface.\n\t// Override them if needed.\n\t@Override\n\tpublic Integer next() {\n\t    \n\t}\n\t\n\t@Override\n\tpublic boolean hasNext() {\n\t    \n\t}\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "# Below is the interface for Iterator, which is already defined for you.\n#\n# class Iterator(object):\n#     def __init__(self, nums):\n#         \"\"\"\n#         Initializes an iterator object to the beginning of a list.\n#         :type nums: List[int]\n#         \"\"\"\n#\n#     def hasNext(self):\n#         \"\"\"\n#         Returns true if the iteration has more elements.\n#         :rtype: bool\n#         \"\"\"\n#\n#     def next(self):\n#         \"\"\"\n#         Returns the next element in the iteration.\n#         :rtype: int\n#         \"\"\"\n\nclass PeekingIterator(object):\n    def __init__(self, iterator):\n        \"\"\"\n        Initialize your data structure here.\n        :type iterator: Iterator\n        \"\"\"\n        \n\n    def peek(self):\n        \"\"\"\n        Returns the next element in the iteration without advancing the iterator.\n        :rtype: int\n        \"\"\"\n        \n\n    def next(self):\n        \"\"\"\n        :rtype: int\n        \"\"\"\n        \n\n    def hasNext(self):\n        \"\"\"\n        :rtype: bool\n        \"\"\"\n        \n\n# Your PeekingIterator object will be instantiated and called as such:\n# iter = PeekingIterator(Iterator(nums))\n# while iter.hasNext():\n#     val = iter.peek()   # Get the next element but not advance the iterator.\n#     iter.next()         # Should return the same value as [val]."
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "# Below is the interface for Iterator, which is already defined for you.\n#\n# class Iterator:\n#     def __init__(self, nums):\n#         \"\"\"\n#         Initializes an iterator object to the beginning of a list.\n#         :type nums: List[int]\n#         \"\"\"\n#\n#     def hasNext(self):\n#         \"\"\"\n#         Returns true if the iteration has more elements.\n#         :rtype: bool\n#         \"\"\"\n#\n#     def next(self):\n#         \"\"\"\n#         Returns the next element in the iteration.\n#         :rtype: int\n#         \"\"\"\n\nclass PeekingIterator:\n    def __init__(self, iterator):\n        \"\"\"\n        Initialize your data structure here.\n        :type iterator: Iterator\n        \"\"\"\n        \n\n    def peek(self):\n        \"\"\"\n        Returns the next element in the iteration without advancing the iterator.\n        :rtype: int\n        \"\"\"\n        \n\n    def next(self):\n        \"\"\"\n        :rtype: int\n        \"\"\"\n        \n\n    def hasNext(self):\n        \"\"\"\n        :rtype: bool\n        \"\"\"\n        \n\n# Your PeekingIterator object will be instantiated and called as such:\n# iter = PeekingIterator(Iterator(nums))\n# while iter.hasNext():\n#     val = iter.peek()   # Get the next element but not advance the iterator.\n#     iter.next()         # Should return the same value as [val]."
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/*\n *\tstruct Iterator {\n *\t\t// Returns true if the iteration has more elements.\n *\t\tbool (*hasNext)();\n *\n * \t\t// Returns the next element in the iteration.\n *\t\tint (*next)();\n *\t};\n */\n\nstruct PeekingIterator {\n    \n};\n\nstruct PeekingIterator* Constructor(struct Iterator* iter) {\n    struct PeekingIterator* piter = malloc(sizeof(struct PeekingIterator));\n    piter->iterator = iter;\n    piter->hasPeeked = false;\n    return piter;\n}\n\nint peek(struct PeekingIterator* obj) {\n    \n}\n\nint next(struct PeekingIterator* obj) {\n    \n}\n\nbool hasNext(struct PeekingIterator* obj) {\n    \n}\n\n/**\n * Your PeekingIterator struct will be instantiated and called as such:\n * PeekingIterator* obj = peekingIteratorCreate(arr, arrSize);\n * int param_1 = peek(obj);\n * int param_2 = next(obj);\n * bool param_3 = hasNext(obj);\n * peekingIteratorFree(obj);\n*/"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "// C# IEnumerator interface reference:\n// https://docs.microsoft.com/en-us/dotnet/api/system.collections.ienumerator?view=netframework-4.8\n\nclass PeekingIterator {\n    // iterators refers to the first element of the array.\n    public PeekingIterator(IEnumerator<int> iterator) {\n        // initialize any member here.\n    }\n    \n    // Returns the next element in the iteration without advancing the iterator.\n    public int Peek() {\n        \n    }\n    \n    // Returns the next element in the iteration and advances the iterator.\n    public int Next() {\n        \n    }\n    \n    // Returns false if the iterator is refering to the end of the array of true otherwise.\n    public bool HasNext() {\n\t\t\n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * // This is the Iterator's API interface.\n * // You should not implement it, or speculate about its implementation.\n * function Iterator() {\n *    @ return {number}\n *    this.next = function() { // return the next number of the iterator\n *       ...\n *    }; \n *\n *    @return {boolean}\n *    this.hasNext = function() { // return true if it still has numbers\n *       ...\n *    };\n * };\n */\n\n/**\n * @param {Iterator} iterator\n */\nvar PeekingIterator = function(iterator) {\n    \n};\n\n/**\n * @return {number}\n */\nPeekingIterator.prototype.peek = function() {\n    \n};\n\n/**\n * @return {number}\n */\nPeekingIterator.prototype.next = function() {\n    \n};\n\n/**\n * @return {boolean}\n */\nPeekingIterator.prototype.hasNext = function() {\n    \n};\n\n/** \n * Your PeekingIterator object will be instantiated and called as such:\n * var obj = new PeekingIterator(arr)\n * var param_1 = obj.peek()\n * var param_2 = obj.next()\n * var param_3 = obj.hasNext()\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * // This is the Iterator's API interface.\n * // You should not implement it, or speculate about its implementation\n * class Iterator {\n *      hasNext(): boolean {}\n *\n *      next(): number {}\n * }\n */\n\nclass PeekingIterator {\n    constructor(iterator: Iterator) {\n\n    }\n\n    peek(): number {\n\n    }\n\n    next(): number {\n\n    }\n\n    hasNext(): boolean {\n\n    }\n}\n\n/**\n * Your PeekingIterator object will be instantiated and called as such:\n * var obj = new PeekingIterator(iterator)\n * var param_1 = obj.peek()\n * var param_2 = obj.next()\n * var param_3 = obj.hasNext()\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "// PHP ArrayIterator reference:\n// https://www.php.net/arrayiterator\n\nclass PeekingIterator {\n    /**\n     * @param ArrayIterator $arr\n     */\n    function __construct($arr) {\n        \n    }\n    \n    /**\n     * @return Integer\n     */\n    function next() {\n        \n    }\n    \n    /**\n     * @return Integer\n     */\n    function peek() {\n        \n    }\n    \n    /**\n     * @return Boolean\n     */\n    function hasNext() {\n        \n    }\n}\n\n/**\n * Your PeekingIterator object will be instantiated and called as such:\n * $obj = PeekingIterator($arr);\n * $ret_1 = $obj->next();\n * $ret_2 = $obj->peek();\n * $ret_3 = $obj->hasNext();\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "// Swift IndexingIterator refernence:\n// https://developer.apple.com/documentation/swift/indexingiterator\n\nclass PeekingIterator {\n    init(_ arr: IndexingIterator<Array<Int>>) {\n        \n    }\n    \n    func next() -> Int {\n        \n    }\n    \n    func peek() -> Int {\n        \n    }\n    \n    func hasNext() -> Bool {\n        \n    }\n}\n\n/**\n * Your PeekingIterator object will be instantiated and called as such:\n * let obj = PeekingIterator(arr)\n * let ret_1: Int = obj.next()\n * let ret_2: Int = obj.peek()\n * let ret_3: Bool = obj.hasNext()\n */"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "// Kotlin Iterator reference:\n// https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/\n\nclass PeekingIterator(iterator:Iterator<Int>):Iterator<Int> {\n    fun peek(): Int {\n    \t\n    }\n    \n    override fun next(): Int {\n        \n    }\n    \n    override fun hasNext(): Boolean {\n        \n    }\n}\n\n/**\n * Your PeekingIterator object will be instantiated and called as such:\n * var obj = PeekingIterator(arr)\n * var param_1 = obj.next()\n * var param_2 = obj.peek()\n * var param_3 = obj.hasNext()\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/*   Below is the interface for Iterator, which is already defined for you.\n *\n *   type Iterator struct {\n *       \n *   }\n *\n *   func (this *Iterator) hasNext() bool {\n *\t\t// Returns true if the iteration has more elements.\n *   }\n *\n *   func (this *Iterator) next() int {\n *\t\t// Returns the next element in the iteration.\n *   }\n */\n\ntype PeekingIterator struct {\n    \n}\n\nfunc Constructor(iter *Iterator) *PeekingIterator {\n    \n}\n\nfunc (this *PeekingIterator) hasNext() bool {\n    \n}\n\nfunc (this *PeekingIterator) next() int {\n    \n}\n\nfunc (this *PeekingIterator) peek() int {\n    \n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Below is the interface for Iterator, which is already defined for you.\n#\n# class Iterator\n# \tdef initialize(v)\n#   \n#   end\n#\n#   def hasNext()\n#\t\tReturns true if the iteration has more elements.\n#   end\n#\n#   def next()\n#   \tReturns the next element in the iteration.\n#   end\n# end\n\nclass PeekingIterator\n    # @param {Iterator} iter\n    def initialize(iter)\n    \t\n    end\n    \n    # Returns true if the iteration has more elements.\n    # @return {boolean}\n    def hasNext()\n    \t\n    end\n    \n    # Returns the next element in the iteration.\n    # @return {integer}\n    def next()\n    \t\n    end\n    \n    # Returns the next element in the iteration without advancing the iterator.\n    # @return {integer}\n    def peek()\n    \t\n    end\nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "// Scala Iterator reference:\n// https://www.scala-lang.org/api/2.12.2/scala/collection/Iterator.html\n\nclass PeekingIterator(_iterator: Iterator[Int]) {\n    def peek(): Int = {\n        \n    }\n    \n    def next(): Int = {\n        \n    }\n    \n    def hasNext(): Boolean = {\n        \n    }\n}\n\n/**\n * Your PeekingIterator object will be instantiated and called as such:\n * var obj = new PeekingIterator(arr)\n * var param_1 = obj.next()\n * var param_2 = obj.peek()\n * var param_3 = obj.hasNext()\n */"
    }
]
problems["73"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "class Solution {\npublic:\n    void setZeroes(vector<vector<int>>& matrix) {\n\n    }\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "class Solution {\n    public void setZeroes(int[][] matrix) {\n\n    }\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "class Solution(object):\n    def setZeroes(self, matrix):\n        \"\"\"\n        :type matrix: List[List[int]]\n        :rtype: None Do not return anything, modify matrix in-place instead.\n        \"\"\""
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "class Solution:\n    def setZeroes(self, matrix: List[List[int]]) -> None:\n        \"\"\"\n        Do not return anything, modify matrix in-place instead.\n        \"\"\""
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {\n    \n}"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "public class Solution {\n    public void SetZeroes(int[][] matrix) {\n\n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * @param {number[][]} matrix\n * @return {void} Do not return anything, modify matrix in-place instead.\n */\nvar setZeroes = function(matrix) {\n\n};"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n Do not return anything, modify matrix in-place instead.\n */\nfunction setZeroes(matrix: number[][]): void {\n    \n};"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "class Solution {\n\n    /**\n     * @param Integer[][] $matrix\n     * @return NULL\n     */\n    function setZeroes(&$matrix) {\n\n    }\n}"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "class Solution {\n    func setZeroes(_ matrix: inout [[Int]]) {\n\n    }\n}"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "class Solution {\n    fun setZeroes(matrix: Array<IntArray>): Unit {\n\n    }\n}"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "class Solution {\n  void setZeroes(List<List<int>> matrix) {\n    \n  }\n}"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "func setZeroes(matrix [][]int)  {\n\n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# @param {Integer[][]} matrix\n# @return {Void} Do not return anything, modify matrix in-place instead.\ndef set_zeroes(matrix)\n\nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "object Solution {\n    def setZeroes(matrix: Array[Array[Int]]): Unit = {\n        \n    }\n}"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "impl Solution {\n    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {\n\n    }\n}"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "(define/contract (set-zeroes matrix)\n  (-> (listof (listof exact-integer?)) void?)\n\n  )"
    }
]
problems["1382"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution {\npublic:\n    TreeNode* balanceBST(TreeNode* root) {\n\n    }\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution {\n    public TreeNode balanceBST(TreeNode root) {\n\n    }\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n    def balanceBST(self, root):\n        \"\"\"\n        :type root: TreeNode\n        :rtype: TreeNode\n        \"\"\"\n        "
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def balanceBST(self, root: TreeNode) -> TreeNode:\n        "
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n */\nstruct TreeNode* balanceBST(struct TreeNode* root) {\n    \n}"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\npublic class Solution {\n    public TreeNode BalanceBST(TreeNode root) {\n\n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {TreeNode}\n */\nvar balanceBST = function(root) {\n\n};"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     val: number\n *     left: TreeNode | null\n *     right: TreeNode | null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left = (left===undefined ? null : left)\n *         this.right = (right===undefined ? null : right)\n *     }\n * }\n */\n\nfunction balanceBST(root: TreeNode | null): TreeNode | null {\n    \n};"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     public $val = null;\n *     public $left = null;\n *     public $right = null;\n *     function __construct($val = 0, $left = null, $right = null) {\n *         $this->val = $val;\n *         $this->left = $left;\n *         $this->right = $right;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param TreeNode $root\n     * @return TreeNode\n     */\n    function balanceBST($root) {\n\n    }\n}"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     public var val: Int\n *     public var left: TreeNode?\n *     public var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil; self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n *         self.right = right\n *     }\n * }\n */\nclass Solution {\n    func balanceBST(_ root: TreeNode?) -> TreeNode? {\n\n    }\n}"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "/**\n * Example:\n * var ti = TreeNode(5)\n * var v = ti.`val`\n * Definition for a binary tree node.\n * class TreeNode(var `val`: Int) {\n *     var left: TreeNode? = null\n *     var right: TreeNode? = null\n * }\n */\nclass Solution {\n    fun balanceBST(root: TreeNode?): TreeNode? {\n\n    }\n}"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *   int val;\n *   TreeNode? left;\n *   TreeNode? right;\n *   TreeNode([this.val = 0, this.left, this.right]);\n * }\n */\nclass Solution {\n  TreeNode? balanceBST(TreeNode? root) {\n    \n  }\n}"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc balanceBST(root *TreeNode) *TreeNode {\n\n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n#         @val = val\n#         @left = left\n#         @right = right\n#     end\n# end\n# @param {TreeNode} root\n# @return {TreeNode}\ndef balance_bst(root)\n\nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "/**\n * Definition for a binary tree node.\n * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {\n *   var value: Int = _value\n *   var left: TreeNode = _left\n *   var right: TreeNode = _right\n * }\n */\nobject Solution {\n    def balanceBST(root: TreeNode): TreeNode = {\n\n    }\n}"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "// Definition for a binary tree node.\n// #[derive(Debug, PartialEq, Eq)]\n// pub struct TreeNode {\n//   pub val: i32,\n//   pub left: Option<Rc<RefCell<TreeNode>>>,\n//   pub right: Option<Rc<RefCell<TreeNode>>>,\n// }\n//\n// impl TreeNode {\n//   #[inline]\n//   pub fn new(val: i32) -> Self {\n//     TreeNode {\n//       val,\n//       left: None,\n//       right: None\n//     }\n//   }\n// }\nuse std::rc::Rc;\nuse std::cell::RefCell;\nimpl Solution {\n    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {\n\n    }\n}"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "; Definition for a binary tree node.\n#|\n\n; val : integer?\n; left : (or/c tree-node? #f)\n; right : (or/c tree-node? #f)\n(struct tree-node\n  (val left right) #:mutable #:transparent)\n\n; constructor\n(define (make-tree-node [val 0])\n  (tree-node val #f #f))\n\n|#\n\n(define/contract (balance-bst root)\n  (-> (or/c tree-node? #f) (or/c tree-node? #f))\n  )"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "%% Definition for a binary tree node.\n%%\n%% -record(tree_node, {val = 0 :: integer(),\n%%                     left = null  :: 'null' | #tree_node{},\n%%                     right = null :: 'null' | #tree_node{}}).\n\n-spec balance_bst(Root :: #tree_node{} | null) -> #tree_node{} | null.\nbalance_bst(Root) ->\n  ."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "# Definition for a binary tree node.\n#\n# defmodule TreeNode do\n#   @type t :: %__MODULE__{\n#           val: integer,\n#           left: TreeNode.t() | nil,\n#           right: TreeNode.t() | nil\n#         }\n#   defstruct val: 0, left: nil, right: nil\n# end\n\ndefmodule Solution do\n  @spec balance_bst(root :: TreeNode.t | nil) :: TreeNode.t | nil\n  def balance_bst(root) do\n    \n  end\nend"
    }
]
problems["382"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\npublic:\n    Solution(ListNode* head) {\n\n    }\n    \n    int getRandom() {\n\n    }\n};\n\n/**\n * Your Solution object will be instantiated and called as such:\n * Solution* obj = new Solution(head);\n * int param_1 = obj->getRandom();\n */"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\nclass Solution {\n\n    public Solution(ListNode head) {\n\n    }\n    \n    public int getRandom() {\n\n    }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * Solution obj = new Solution(head);\n * int param_1 = obj.getRandom();\n */"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "# Definition for singly-linked list.\n# class ListNode(object):\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution(object):\n\n    def __init__(self, head):\n        \"\"\"\n        :type head: Optional[ListNode]\n        \"\"\"\n\n\n    def getRandom(self):\n        \"\"\"\n        :rtype: int\n        \"\"\"\n\n\n\n# Your Solution object will be instantiated and called as such:\n# obj = Solution(head)\n# param_1 = obj.getRandom()"
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n\n    def __init__(self, head: Optional[ListNode]):\n\n\n    def getRandom(self) -> int:\n\n\n\n# Your Solution object will be instantiated and called as such:\n# obj = Solution(head)\n# param_1 = obj.getRandom()"
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     struct ListNode *next;\n * };\n */\n\n\n\ntypedef struct {\n    \n} Solution;\n\n\nSolution* solutionCreate(struct ListNode* head) {\n    \n}\n\nint solutionGetRandom(Solution* obj) {\n    \n}\n\nvoid solutionFree(Solution* obj) {\n    \n}\n\n/**\n * Your Solution struct will be instantiated and called as such:\n * Solution* obj = solutionCreate(head);\n * int param_1 = solutionGetRandom(obj);\n \n * solutionFree(obj);\n*/"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next = next;\n *     }\n * }\n */\npublic class Solution {\n\n    public Solution(ListNode head) {\n\n    }\n    \n    public int GetRandom() {\n\n    }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * Solution obj = new Solution(head);\n * int param_1 = obj.GetRandom();\n */"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n */\nvar Solution = function(head) {\n\n};\n\n/**\n * @return {number}\n */\nSolution.prototype.getRandom = function() {\n\n};\n\n/**\n * Your Solution object will be instantiated and called as such:\n * var obj = new Solution(head)\n * var param_1 = obj.getRandom()\n */"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n * Definition for singly-linked list.\n * class ListNode {\n *     val: number\n *     next: ListNode | null\n *     constructor(val?: number, next?: ListNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *     }\n * }\n */\n\nclass Solution {\n    constructor(head: ListNode | null) {\n        \n    }\n\n    getRandom(): number {\n        \n    }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * var obj = new Solution(head)\n * var param_1 = obj.getRandom()\n */"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *     public $val = 0;\n *     public $next = null;\n *     function __construct($val = 0, $next = null) {\n *         $this->val = $val;\n *         $this->next = $next;\n *     }\n * }\n */\nclass Solution {\n    /**\n     * @param ListNode $head\n     */\n    function __construct($head) {\n\n    }\n\n    /**\n     * @return Integer\n     */\n    function getRandom() {\n\n    }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * $obj = Solution($head);\n * $ret_1 = $obj->getRandom();\n */"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     public var val: Int\n *     public var next: ListNode?\n *     public init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int) { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }\n * }\n */\n\nclass Solution {\n\n    init(_ head: ListNode?) {\n\n    }\n    \n    func getRandom() -> Int {\n\n    }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * let obj = Solution(head)\n * let ret_1: Int = obj.getRandom()\n */"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "/**\n * Example:\n * var li = ListNode(5)\n * var v = li.`val`\n * Definition for singly-linked list.\n * class ListNode(var `val`: Int) {\n *     var next: ListNode? = null\n * }\n */\nclass Solution(head: ListNode?) {\n\n    fun getRandom(): Int {\n\n    }\n\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * var obj = Solution(head)\n * var param_1 = obj.getRandom()\n */"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "/**\n * Definition for singly-linked list.\n * class ListNode {\n *   int val;\n *   ListNode? next;\n *   ListNode([this.val = 0, this.next]);\n * }\n */\nclass Solution {\n\n  Solution(ListNode? head) {\n    \n  }\n  \n  int getRandom() {\n    \n  }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * Solution obj = Solution(head);\n * int param1 = obj.getRandom();\n */"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\ntype Solution struct {\n\n}\n\n\nfunc Constructor(head *ListNode) Solution {\n\n}\n\n\nfunc (this *Solution) GetRandom() int {\n\n}\n\n\n/**\n * Your Solution object will be instantiated and called as such:\n * obj := Constructor(head);\n * param_1 := obj.GetRandom();\n */"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val = val\n#         @next = _next\n#     end\n# end\nclass Solution\n\n=begin\n    :type head: ListNode\n=end\n    def initialize(head)\n        \n    end\n\n\n=begin\n    :rtype: Integer\n=end\n    def get_random()\n        \n    end\n\n\nend\n\n# Your Solution object will be instantiated and called as such:\n# obj = Solution.new(head)\n# param_1 = obj.get_random()"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "/**\n * Definition for singly-linked list.\n * class ListNode(_x: Int = 0, _next: ListNode = null) {\n *   var next: ListNode = _next\n *   var x: Int = _x\n * }\n */\nclass Solution(_head: ListNode) {\n\n    def getRandom(): Int = {\n        \n    }\n\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * val obj = new Solution(head)\n * val param_1 = obj.getRandom()\n */"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "// Definition for singly-linked list.\n// #[derive(PartialEq, Eq, Clone, Debug)]\n// pub struct ListNode {\n//   pub val: i32,\n//   pub next: Option<Box<ListNode>>\n// }\n//\n// impl ListNode {\n//   #[inline]\n//   fn new(val: i32) -> Self {\n//     ListNode {\n//       next: None,\n//       val\n//     }\n//   }\n// }\nstruct Solution {\n\n}\n\n\n/**\n * `&self` means the method takes an immutable reference.\n * If you need a mutable reference, change it to `&mut self` instead.\n */\nimpl Solution {\n\n    fn new(head: Option<Box<ListNode>>) -> Self {\n\n    }\n    \n    fn get_random(&self) -> i32 {\n\n    }\n}\n\n/**\n * Your Solution object will be instantiated and called as such:\n * let obj = Solution::new(head);\n * let ret_1: i32 = obj.get_random();\n */"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "; Definition for singly-linked list:\n#|\n\n; val : integer?\n; next : (or/c list-node? #f)\n(struct list-node\n  (val next) #:mutable #:transparent)\n\n; constructor\n(define (make-list-node [val 0])\n  (list-node val #f))\n\n|#\n\n(define solution%\n  (class object%\n    (super-new)\n    \n    ; head : (or/c list-node? #f)\n    (init-field\n      head)\n    \n    ; get-random : -> exact-integer?\n    (define/public (get-random)\n      )))\n\n;; Your solution% object will be instantiated and called as such:\n;; (define obj (new solution% [head head]))\n;; (define param_1 (send obj get-random))"
    },
    {
        "lang": "Erlang",
        "langSlug": "erlang",
        "code": "%% Definition for singly-linked list.\n%%\n%% -record(list_node, {val = 0 :: integer(),\n%%                     next = null :: 'null' | #list_node{}}).\n\n-spec solution_init_(Head :: #list_node{} | null) -> any().\nsolution_init_(Head) ->\n  .\n\n-spec solution_get_random() -> integer().\nsolution_get_random() ->\n  .\n\n\n%% Your functions will be called as such:\n%% solution_init_(Head),\n%% Param_1 = solution_get_random(),\n\n%% solution_init_ will be called before every test case, in which you can do some necessary initializations."
    },
    {
        "lang": "Elixir",
        "langSlug": "elixir",
        "code": "# Definition for singly-linked list.\n#\n# defmodule ListNode do\n#   @type t :: %__MODULE__{\n#           val: integer,\n#           next: ListNode.t() | nil\n#         }\n#   defstruct val: 0, next: nil\n# end\n\ndefmodule Solution do\n  @spec init_(head :: ListNode.t | nil) :: any\n  def init_(head) do\n    \n  end\n\n  @spec get_random() :: integer\n  def get_random() do\n    \n  end\nend\n\n# Your functions will be called as such:\n# Solution.init_(head)\n# param_1 = Solution.get_random()\n\n# Solution.init_ will be called before every test case, in which you can do some necessary initializations."
    }
]

problems["283"] = [
    {
        "lang": "C++",
        "langSlug": "cpp",
        "code": "class Solution {\npublic:\n    void moveZeroes(vector<int>& nums) {\n\n    }\n};"
    },
    {
        "lang": "Java",
        "langSlug": "java",
        "code": "class Solution {\n    public void moveZeroes(int[] nums) {\n\n    }\n}"
    },
    {
        "lang": "Python",
        "langSlug": "python",
        "code": "class Solution(object):\n    def moveZeroes(self, nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: None Do not return anything, modify nums in-place instead.\n        \"\"\""
    },
    {
        "lang": "Python3",
        "langSlug": "python3",
        "code": "class Solution:\n    def moveZeroes(self, nums: List[int]) -> None:\n        \"\"\"\n        Do not return anything, modify nums in-place instead.\n        \"\"\""
    },
    {
        "lang": "C",
        "langSlug": "c",
        "code": "void moveZeroes(int* nums, int numsSize) {\n    \n}"
    },
    {
        "lang": "C#",
        "langSlug": "csharp",
        "code": "public class Solution {\n    public void MoveZeroes(int[] nums) {\n\n    }\n}"
    },
    {
        "lang": "JavaScript",
        "langSlug": "javascript",
        "code": "/**\n * @param {number[]} nums\n * @return {void} Do not return anything, modify nums in-place instead.\n */\nvar moveZeroes = function(nums) {\n\n};"
    },
    {
        "lang": "TypeScript",
        "langSlug": "typescript",
        "code": "/**\n Do not return anything, modify nums in-place instead.\n */\nfunction moveZeroes(nums: number[]): void {\n    \n};"
    },
    {
        "lang": "PHP",
        "langSlug": "php",
        "code": "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return NULL\n     */\n    function moveZeroes(&$nums) {\n\n    }\n}"
    },
    {
        "lang": "Swift",
        "langSlug": "swift",
        "code": "class Solution {\n    func moveZeroes(_ nums: inout [Int]) {\n\n    }\n}"
    },
    {
        "lang": "Kotlin",
        "langSlug": "kotlin",
        "code": "class Solution {\n    fun moveZeroes(nums: IntArray): Unit {\n\n    }\n}"
    },
    {
        "lang": "Dart",
        "langSlug": "dart",
        "code": "class Solution {\n  void moveZeroes(List<int> nums) {\n    \n  }\n}"
    },
    {
        "lang": "Go",
        "langSlug": "golang",
        "code": "func moveZeroes(nums []int)  {\n\n}"
    },
    {
        "lang": "Ruby",
        "langSlug": "ruby",
        "code": "# @param {Integer[]} nums\n# @return {Void} Do not return anything, modify nums in-place instead.\ndef move_zeroes(nums)\n\nend"
    },
    {
        "lang": "Scala",
        "langSlug": "scala",
        "code": "object Solution {\n    def moveZeroes(nums: Array[Int]): Unit = {\n\n    }\n}"
    },
    {
        "lang": "Rust",
        "langSlug": "rust",
        "code": "impl Solution {\n    pub fn move_zeroes(nums: &mut Vec<i32>) {\n\n    }\n}"
    },
    {
        "lang": "Racket",
        "langSlug": "racket",
        "code": "(define/contract (move-zeroes nums)\n  (-> (listof exact-integer?) void?)\n\n  )"
    }
]

if __name__ == '__main__':
    # for idx, test in enumerate(default_test_list):
    #     res = write_solution_python(test)
    #     with open(f"tmp_default{idx}.py", "w") as f:
    #         f.writelines(res)

    # for idx, test in enumerate(submit_test_list):
    #     res = write_solution_python(test, False)
    #     with open(f"tmp_submit{idx}.py", "w") as f:
    #         f.writelines(res)

    # for idx, test in enumerate(golang_test_list):
    #     res = write_solution_golang(test, None, str(idx))
    #     with open(f"tmp_solution{idx}.go", "w") as f:
    #         f.writelines(res)

    # for problem, code_templates in problems.values():
    #     pass

    code_counter = Counter()
    for test_problem, codes in problems.items():
        for code in codes:
            lang = code["langSlug"]
            match lang:
                case "cpp":
                    with open(f"tmp_Solution{code_counter[lang]}.cpp", "w", encoding="utf-8") as f:
                        f.writelines(write_solution_cpp(code["code"], None, test_problem))
                    code_counter[lang] += 1
                case "java":
                    with open(f"tmp_Solution{code_counter[lang]}.java", "w", encoding="utf-8") as f:
                        f.writelines(write_solution_java(code["code"], None, test_problem))
                    code_counter[lang] += 1
                case "golang":
                    with open(f"tmp_solution{code_counter[lang]}.go", "w", encoding="utf-8") as f:
                        f.writelines(write_solution_golang(code["code"], None, test_problem))
                    code_counter[lang] += 1
                case "typescript":
                    with open(f"tmp_solution{code_counter[lang]}.ts", "w", encoding="utf-8") as f:
                        f.writelines(write_solution_typescript(code["code"], None, test_problem))
                    code_counter[lang] += 1
                case _:
                    pass
        break
    sys.exit()
