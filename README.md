# itheimalearn

黑马程序员 LeetCode 刷题训练记录，按题型分类存放。

---

## 目录结构

```
itheimalearn/
└── leetcode_train/
    ├── question242.py                    # 242. 有效的字母异位词
    │
    ├── 1-39/                             # 题号 1 ~ 39（21 道题）
    │   ├── question1.py                  # 1. 两数之和
    │   ├── question2.py                  # 2. 两数相加（链表）
    │   ├── question3.py                  # 3. 无重复字符的最长子串
    │   ├── question7.py                  # 7. 整数反转
    │   ├── question8.py                  # 8. 字符串转换整数 (atoi)
    │   ├── question9.py                  # 9. 回文数
    │   ├── question10.py                 # 10. 正则表达式匹配
    │   ├── question11.py                 # 11. 盛最多水的容器
    │   ├── question12.py                 # 12. 整数转罗马数字
    │   ├── question13.py                 # 13. 罗马数字转整数
    │   ├── question14.py                 # 14. 最长公共前缀
    │   ├── question15.py                 # 15. 三数之和
    │   ├── question16.py                 # 16. 最接近的三数之和
    │   ├── question17.py                 # 17. 电话号码的字母组合
    │   ├── question19.py                 # 19. 删除链表的倒数第 N 个结点
    │   ├── question20.py                 # 20. 有效的括号
    │   ├── question21.py                 # 21. 合并两个有序链表
    │   ├── question22.py                 # 22. 括号生成
    │   ├── question23.py                 # 23. 合并 K 个升序链表
    │   ├── question24.py                 # 24. 两两交换链表中的节点
    │   └── question25.py                 # 25. K 个一组翻转链表
    │
    ├── 40-79/                            # 题号 40 ~ 79（4 道题）
    │   ├── question48.py                 # 48. 旋转图像
    │   ├── question49.py                 # 49. 字母异位词分组
    │   ├── question56.py                 # 56. 合并区间
    │   └── question57.py                 # 57. 插入区间
    │
    ├── 二分查找/
    │   ├── question33.py                 # 33. 搜索旋转排序数组
    │   ├── question34.py                 # 34. 在排序数组中查找元素的第一个和最后一个位置
    │   └── question35.py                 # 35. 搜索插入位置
    │
    ├── 数组/
    │   ├── question1.py                  # 1. 两数之和
    │   ├── question4.py                  # 4. 寻找两个正序数组的中位数
    │   ├── question11.py                 # 11. 盛最多水的容器
    │   ├── question14.py                 # 14. 最长公共前缀
    │   ├── question15.py                 # 15. 三数之和
    │   ├── question73.py                 # 73. 矩阵置零
    │   ├── question74.py                 # 74. 搜索二维矩阵
    │   ├── question75.py                 # 75. 颜色分类（荷兰国旗）
    │   ├── question567.py                # 567. 字符串的排列
    │   └── question575.py                # 575. 分糖果
    │
    ├── 数学/                             # 数学 & 位运算 & 模拟（37 道题）
    │   ├── question60.py                 # 60. 排列序列
    │   ├── question62.py                 # 62. 不同路径（组合数学）
    │   ├── question66.py                 # 66. 加一
    │   ├── qusetion67.py                 # 67. 二进制求和 [注：文件名拼写待修正]
    │   ├── question69.py                 # 69. x 的平方根（二分 / 牛顿迭代）
    │   ├── question70.py                 # 70. 爬楼梯（斐波那契/DP）
    │   ├── question89.py                 # 89. 格雷编码
    │   ├── question96.py                 # 96. 不同的二叉搜索树
    │   ├── question149.py                # 149. 直线上最多的点数
    │   ├── question150.py                # 150. 逆波兰表达式求值
    │   ├── question166.py                # 166. 分数到小数
    │   ├── question168.py                # 168. Excel 表列名称
    │   ├── question171.py                # 171. Excel 表列序号
    │   ├── question172.py                # 172. 阶乘后的零
    │   ├── question189.py                # 189. 轮转数组
    │   ├── question202.py                # 202. 快乐数
    │   ├── question204.py                # 204. 计数质数
    │   ├── question223.py                # 223. 矩形面积
    │   ├── question224.py                # 224. 基本计算器
    │   ├── question227.py                # 227. 基本计算器 II
    │   ├── question231.py                # 231. 2 的幂
    │   ├── question233.py                # 233. 数字 1 的个数
    │   ├── question241.py                # 241. 为运算表达式设计优先级
    │   ├── question258.py                # 258. 各位相加
    │   ├── question263.py                # 263. 丑数
    │   ├── question264.py                # 264. 丑数 II
    │   ├── question268.py                # 268. 丢失的数字
    │   ├── question273.py                # 273. 整数转换英文表示
    │   ├── question279.py                # 279. 完全平方数
    │   ├── question313.py                # 313. 超级丑数
    │   ├── question371.py                # 371. 两整数之和（位运算）
    │   ├── question372.py                # 372. 超级次方
    │   ├── question390.py                # 390. 消除游戏（数学模拟）
    │   ├── question391.py                # 391. 完美矩形
    │   ├── question392.py                # 392. 判断子序列（含进阶跳表）
    │   ├── question396.py                # 396. 旋转函数
    │   ├── question398.py                # 398. 随机数索引（蓄水池抽样）
    │   ├── question400.py                # 400. 第 N 位数字
    │   └── question405.py                # 405. 数字转换为十六进制数
    │
    ├── data_structure/                   # 公共数据结构定义
    │   ├── __init__.py
    │   ├── ListNode_defined.py           # 链表节点定义
    │   └── treenode_defined.py           # 二叉树节点定义
    │
    └── 每日一题/
        └── 7月/
            ├── question1260.py           # 1260. 二维网格迁移
            ├── question3963.py           # 每日一题
            ├── question3978.py           # 每日一题
            ├── question3979.py           # 每日一题
            ├── question3980.py           # 每日一题
            └── question3981.py           # 每日一题
```

---

## 统计

| 分类 | 题数 | 路径 |
|------|------|------|
| 基础入门 (1-39) | 21 | `leetcode_train/1-39/` |
| 中等进阶 (40-79) | 4 | `leetcode_train/40-79/` |
| 二分查找 | 3 | `leetcode_train/二分查找/` |
| 数组 | 10 | `leetcode_train/数组/` |
| 数学 & 位运算 | 37 | `leetcode_train/数学/` |
| 每日一题 (7月) | 6 | `leetcode_train/每日一题/7月/` |
| 数据结构定义 | 2 | `leetcode_train/data_structure/` |
| 散题 | 1 | `leetcode_train/question242.py` |
| **合计** | **84** | |

---

## 技术要点

- **语言**：Python 3
- **节点定义**：链表（`ListNode`）、二叉树（`TreeNode`）统一在 `data_structure/` 中引用
- **经典算法覆盖**：
  - 双指针（两数之和、三数之和、盛水容器等）
  - 二分查找（搜索旋转数组、搜索二维矩阵）
  - 链表操作（合并、翻转、删除倒数节点）
  - 数学推导（消除游戏、丑数、位运算、阶乘尾零）
  - 栈与计算器（基本计算器 I/II、逆波兰表达式）
  - 进阶优化（子序列跳表预处理、蓄水池抽样、荷兰国旗三指针）
