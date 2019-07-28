<p align="right">参考 剑指offer(第二版) 何海涛</p>

## 题目练习：序号与剑指offer题目对应
- [数组](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/num_list/)
- [二进制](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/binary/)
- [循环 vs 递归](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/recursive_vs_circle/)
- [字符串](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/string/)
- [链表](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/linked_list/)
- [栈和队列](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/stack_and_queue/)
- [树](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/tree/)
- [单例模式](https://github.com/syntomic/Languages_and_Algorithms/tree/master/interview/singleton/)

## 面试的流程：每一轮面试需要注意的问题

- 面试形式
    - 电话面试
        - 形象化的语言把细节说清楚
    - 共享桌面远程面试
        - 思考清楚在开始编码
        - 良好的代码命名和缩进对齐习惯
        - 单元测试：先写单元测试用例
        - 调试：设置断点， 单步跟踪，查看内存，分析调用栈
    - 现场面试
        - 规划好路线及出行时间
        - 准备得体的衣服
        - 注意面试流程
        - 准备几个问题

- 面试的3个环节
    - 行为面试
        - 项目经历
            - Situation: 简短的项目背景
            - Task: 自己完成的任务
            - Action: 怎么完成的任务
            - Result: 自己的贡献
        - 问题
            - 最大问题及如何解决
            - 学到了什么
            - 团队冲突以及解决方法
        - 技能
            - 了解
            - 熟悉
            - 精通

        [//]: (为什么跳槽)
   - 技术面试
       - [扎实的基础知识](#basic)：编程语言，数据结构，算法
       - [高质量代码](#quality)：基本功能，边界条件，特殊输入
       - [清晰的思路](#ideal)：画图，举例，分解 
       - [优化效率的能力](#efficiency)：分析效率，数据结构优缺点，常用算法
       - [优秀的综合能力](#ability)：沟通与学习，知识迁移，抽象建模，发散思维
   - 应聘者提问
       - 技术面试不要问薪水
       - 不要立即打听面试结果
       - 与职位相关或项目相关：做好准备工作，留意面试官说过的话

## <span id="basic">面试需要的基础知识</span>
- 操作系统
    - 内存管理
        - 溢出
    - 文件操作
    - 网络相关
    - 程序性能
    - 进程与线程
    - 程序安全

- 编程语言
    - 基本概念的理解
    - 实现准备好的代码，分析代码运行结果
    - 写代码：注意边值条件

- 数据结构
    - 数组：连续储存，时间效率高，空间上采用动态数组
        - 举例寻找规律
        - 排序想到二分法
    - 字符串：字符串操作
        - python的强项
    - 链表：动态分配，空间效率高
        - 注意变量的操作
    - 树
        - 几种遍历方法的实现
        - 宽度优先采用辅助队列
        - 搜索利用BST，AVL，红黑树，B(B+)树
        - 最大最小、优先队列可以考虑堆
    - 栈：LIFO
    - 队列：FIFO，宽度优先
    - 图：二元关系，拓扑关系

- 算法和数据操作
    - 枚举法
    - 递归和循环
        - 递归：重复计算，调用栈溢出
    - 查找和排序
        - 顺序查找，二分查找，哈希表查找，二叉排序树查找
        - 插入排序，冒泡排序，归并排序，快速排序，桶排序
    - 回溯法 
    - 动态规划与贪婪算法
        - 动态规划：从上往下分析问题(分解，组合)；从下往上求解问题(避免重复)
        - 贪婪算法：数学分析
    - 位运算
        - 底层运算，速度快
        - 与，或，异或，左移，右移

## <span id="quality">高质量代码：规范性，完整性，鲁棒性</span>

- 代码的规范性
    - 清晰的书写
    - 清晰的布局
    - 合理的命名

- 代码的完整性：永远不变的就是需求会一直改变
    - 功能测试
    - 边界测试
    - 负面测试
    - 错误处理
    - 考虑扩展

- 代码的鲁棒性(Robust)
    - 防御性编程
    - 处理无效输入

## <span id="idea">解决面试题的思路</span>

- 画图让抽象问题形象化
- 举例让抽象问题具体化
- 分解让复杂问题简单化
    - Merge and sort

## <span id="efficiency">优化空间和时间效率</span>

- 时间效率：优化效率，追求完美
    - 编程习惯
    - 重复计算
    - 数据结构和算法功底
    - 敏捷的思维能力和追求完美的激情

- 时间效率与空间效率的平衡
    - 空间换时间：摩尔定律
    - 鱼与熊掌：嵌入式系统

## <span id="ability">面试中的各项能力：表现学习，沟通能力，培养知识迁移，抽象建模，发散思维能力</span>

- 沟通能力和学习能力
    - 沟通能力：语言详略得当，重点突出，观点明确
    - 学习能力：更上时代的步伐
    - 提问能力：hardest part
        - 把问题弄清楚

- 知识迁移能力
    - 经典问题变换
    - 循序渐进
    - 举一反三

- 抽象建模
    - 选择合适的数据结构表述问题
    - 分析模型中的内在规律，并用编程语言实现

- 发散思维能力
    - 不同的方向，侧面，层次
    - 探索，转换，迁移，组合，分解
    - 灵活性和变通性，知识广度和深度