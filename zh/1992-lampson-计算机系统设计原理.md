# 计算机系统设计原理

**Principles for Computer System Design**

> 巴特勒·兰普森(Butler Lampson)
> 1992 年 ACM 图灵奖演讲
> 演讲日期:1993 年 2 月 17 日
> 译自 `1283920.2159562.pdf`(个人学习用途)

> 在过去十年里,关于如何构建计算机系统,我们学到的东西少得令人沮丧。但我们确实学到了一些关于如何更精确地完成这项工作的知识:通过编写更精确的规范(specifications),并更精确地证明实现(implementation)符合其规范。这些方法在智力挑战和实际应用上都极具价值。我将解释其中最有效的方法,并用两个例子来说明:
> **连接建立**:在不可靠的网络上发送可靠的消息。
> **事务**:将一系列小的动作组合成一个大的原子动作。

---

## 计算机系统设计原理 (Principles for Computer System Design)

*   10 年前:《计算机系统设计之提示》(*Hints for Computer System Design*)〔译注1〕
*   自那以后学到的并不多——令人失望
*   我们不是站在彼此的肩膀上,而是踩在彼此的脚趾上。(Hamming)〔译注2〕
*   一件新事物:如何更精确地构建系统
*   如果你觉得系统昂贵,试试混乱。(If you think systems are expensive, try chaos.)

## 合作者 (Collaborators)

*   **Bob Taylor**, **Chuck Thacker**〔译注3〕
    *   工作站:Alto, Dorado, Firefly
    *   网络:AN1, AN2
*   **Charles Simonyi**〔译注4〕
    *   Bravo 所见即所得(WYSIWYG)编辑器
*   **Nancy Lynch**〔译注5〕
    *   可靠消息
*   **Howard Sturgis**〔译注6〕
    *   事务
*   **Martin Abadi**, **Mike Burrows**, **Morrie Gasser**, **Andy Goldstein**, **Charlie Kaufman**, **Ted Wobber**
    *   安全

## 从接口到规范 (From Interfaces to Specifications)

*   使模块化(modularity)变得精确
*   分而治之 (Divide and conquer, 罗马格言)
    *   设计
    *   正确性
    *   文档
*   递归地进行
    *   任何想法在递归化后都会变得更好 (Randell)〔译注7〕
    *   **精化 (Refinement)**:一个人的实现是另一个人的规范。(改编自 Perlis)〔译注8〕
    *   **组合 (Composition)**:在一个规范中使用另一个规范的动作。

## 规范化一个带状态的系统 (Specifying a System with State)

*   **安全性 (Safety property)**:坏事永远不会发生
    *   由状态机定义:
        *   **状态 (state)**:一组值,通常分为命名的变量
        *   **动作 (actions)**:状态的命名变化
*   **活性 (Liveness property)**:好事最终会发生
*   这些定义了**行为 (behavior)**:所有可能的动作序列
*   带状态系统的例子:
    *   数据抽象
    *   并发系统
    *   分布式系统
*   你无法从外部观察系统的实际状态。
*   你只能看到动作的结果。

## 可编辑的格式化文本 (Editable Formatted Text)

**状态 (State)**
*   `text`: `(Char, Property)` 的序列

**动作 (Actions)**
*   `get(2)` 返回 `('e', (Times-Roman, ...))`
*   `replace(3, 5, 2, 3, a p p l e )`

`H e l l o` -> `H e l p`
`H e l l o` -> `look(0, 5, italic := true)` -> *`H e l l o`*

*   这个接口曾用于 Bravo 编辑器。
*   其实现大约有 2 万行代码。

## 如何编写规范 (How to Write a Spec)

*   **弄清楚状态是什么**
    *   选择状态是为了使规范清晰,而不是为了匹配代码。
*   **描述动作**
    *   它们对状态做了什么
    *   它们返回什么
*   **有用的提示**
    *   **记号 (Notation)** 很重要;它能帮助你思考正在发生的事情。
    *   发明合适的词汇。
    *   动作越少越好。
    *   少即是多 (Less is more)。
    *   **非确定性 (Non-determinism)** 越多越好;它允许更多的实现方式。
    *   我很抱歉给你写了这么长的信;我没有时间写一封短的。(Pascal)〔译注9〕

## 可靠消息 (Reliable Messages)

[图示:发送者(Sender)通过不可靠信道(C)向接收者(Receiver)发送消息]

*   `put(m)`
*   `get(m)`
*   `getAck(a)`
*   状态: `q`, `status`
*   信道动作: `crash`, `lose(B)`, `recover`

## 可靠消息的规范 (Spec for Reliable Messages)

*   `q`: `sequence[M]`
*   `status`: `{OK, lost, ?}`
*   `recs/r`: `Boolean`

| 名称 | 守卫 (Guard) | 效果 (Effect) |
|---|---|---|
| **`put(m)`** | | 将 `m` 追加到 `q`, `status := ?` |
| **`getAck(a)`** | `status = a` | `status := lost` |
| **`get(m)`** | `m` 是 `q` 的首个元素 | 移除 `q` 的头部; 如果 `q = <>`, `status := ?` 那么 `status := OK` |
| **`lose`** | | 从 `q` 中删除某些元素; 如果是最后一个则 `status := lost`, 或者 `status := lost` |
| **`recs` 或 `recr`** | | `status := lost`, `recs/r := false` (正在恢复的简写) |

## “实现”意味着什么? (What “Implements” Means?)

*   将动作分为**外部 (external)**和**内部 (internal)**。
*   Y 实现 X,如果:
    1.  Y 的每一个外部行为都是 X 的一个外部行为,且
    2.  Y 的活性属性蕴含 X 的活性属性。
*   这表达了这样一个想法:如果仅通过观察外部动作无法区分 Y 和 X,那么 Y 就实现了 X。

## 证明 Y 实现 X (Proving that Y implements X)

*   定义一个从 Y 的状态到 X 的状态的**抽象函数 (abstraction function)** `f`。
*   证明 Y 模拟了 X:
    1.  `f` 将 Y 的初始状态映射到 X 的初始状态。
    2.  对于每一个 Y 动作和每一个状态 `y`,存在一个在外部表现相同的 X 动作序列,使得图表可交换 (commutes)。

[图示: 状态 y 通过 Y-action 到达 y', 对应 f(y) 通过 X-actions 到达 f(y')]

*   **这总是有效的!**

## 延迟决策规范:示例 (Delayed-Decision Spec: Example)

*   实现者希望规范尽可能具有非确定性,以给予他更多的自由,并使证明正确性更容易。
*   [图示展示了在崩溃和恢复过程中,消息状态的标记与丢弃过程]

## 通用协议 G (A Generic Protocol G)

[第 13-16 页展示了协议 G 的四个阶段,涉及发送者状态、接收者状态以及不可靠信道]
*   涉及变量: `lasts`, `msg`, `lastr`, `sr`, `rs`, `gs`, `gr` 等。

## 运行中的 G (G at Work)

[第 17 页展示了协议 G 在处理崩溃(crash)和恢复(recover)时的具体运行示例]

## G 的抽象函数 (Abstraction Function for G)

*   `old-q`: 如果 `msg != nil` 且 (`lasts = nil` 或 `lasts ∈ gr`),则为 `<msg>`,否则为 `<>`。
*   `q`: `old-q + cur-q`
*   `status`:
    *   `?`: 如果 `cur-q != <>`
    *   `OK`: 如果 `lasts = lastr != nil`
    *   `lost`: 如果 `lasts ∉ (gr ∪ {lastr})` 或 `lasts = nil`

## 握手协议 H (The Handshake Protocol H)

[第 19-24 页详细展示了握手协议 H 的六个步骤,涉及标识符(identifiers)的分配、消息传输、确认和清理]

## H 的抽象函数 (Abstraction Function for H)

| G | H |
|---|---|
| `gs` | `rs` 中的 `i` (满足 `(js, i)`) |
| `gr` | `{ir} - {nil}` |
| `sr` 和 `rs` | `sr` 和 `rs` 中的 `(I, M)` 和 `(I, A)` 消息 |

*   一个高效的程序是逻辑边缘政策(logical brinksmanship)的一次练习。(Dijkstra)〔译注10〕

## 可靠消息:总结 (Reliable Messages: Summary)

*   **想法**
    *   消息上的标识符
    *   有效标识符集,发送者 ⊆ 接收者
    *   清理 (Cleanup)
*   规范很简单。
*   由于崩溃的存在,实现非常微妙。
*   抽象函数揭示了它们的秘密。
*   这种微妙性可以以精确的方式进行分解。

## 原子动作 (Atomic Actions)

*   `S`: 状态
*   `do(a): Val`
*   守卫: (无)
*   效果: `(S, val) := a(S)`

*   分布式系统就是这样一个系统:因为一台我甚至从未听说过的计算机出了故障,导致我无法完成自己的工作。(Lamport)〔译注11〕

## 事务:一次一个动作 (Transactions: One Action at a Time)

*   `S`, `s`: 状态
*   `commit`: `S := s`
*   `crash`: `s := S`
*   [图示展示了在 commit 之前发生 crash 会导致状态回滚]

## 服务器故障 (Server Failures)

*   引入辅助状态 `φ`: `{nil, run}`
*   `begin`: `φ := run`
*   `commit`: `S := s, φ := nil`
*   `crash`: `s := S, φ := nil`
*   注意我们清理了辅助状态 `φ`。

## 增量状态变更:日志 (Incremental State Changes: Logs)

*   `L`, `l`: 动作序列 (SEQ Action)
*   `S = S + L`
*   `do(a)`: `(s, val) := a(s), l +:= a`
*   `commit`: `L := l, φ := nil`
*   `crash`: `l := L, s := S + L, φ := nil`

## 增量状态变更:日志 (续) (Incremental State Changes: Logs (2))

*   `apply(a)`: `S := S + a, l := tail(l)`
*   `cleanLog`: `L := <>`
*   [图示展示了日志的追加、应用和清理过程]

## 增量日志变更 (Incremental Log Changes)

*   引入 `Φ`, `φ`: `{nil, run*, commit}`
*   `flush`: 将 `l` 的一部分复制到 `L`
*   `commit`: `Φ := φ := commit`
*   `cleanup`: `L := <>`

## 分布式状态与日志 (Distributed State and Log)

*   `Si`, `si`, `Li`, `li`, `Φi`, `φi`
*   `S`, `L`, `Φ` 是各部分的乘积。
*   涉及 `preparei`, `commit` 等动作。

## 高可用性 (High Availability)

*   `Φ = commit` 是一个可能的单点故障。
*   通常的两阶段提交 (2PC) 确实限制了可用性。
*   如果数据是副本化的,那么非副本化的提交就是一个弱点。
*   通过使用高可用共识算法来处理 `Φ`。
*   Lamport 的 **Paxos** 算法是目前已知最好的。〔译注12〕

## 事务:总结 (Transactions: Summary)

*   **想法**
    *   日志 (Logs)
    *   提交记录 (Commit records)
    *   关键点的稳定写入:prepare 和 commit
    *   延迟清理
*   规范很简单。
*   由于崩溃的存在,实现非常微妙。
*   抽象函数揭示了它们的秘密。
*   这种微妙性可以一步步添加。

## 如何编写规范 (复用) (How to Write a Spec)

[内容同第 7 页,强调状态选择、动作描述、记号重要性、少即是多、非确定性]

## 安全:访问控制模型 (Security: The Access Control Model)

*   **守卫 (Guards)** 控制对有价值资源的访问。
*   主体 (Principal) 发起请求,引用监视器 (Reference monitor) 根据规则检查,决定是否允许对对象 (Object) 执行操作。
*   规则控制每个主体和对象允许的操作。

## 分布式系统 (A Distributed System)

*   [图示: 工作站上的 Excel 应用程序通过操作系统向服务器上的 NFS 服务器发送请求]

## 主体 (Principals)

*   **认证 (Authentication)**: 谁发送了消息?
*   **授权 (Authorization)**: 谁是被信任的?
*   **主体 (Principal)** —— “谁”的抽象:
    *   人: Lampson, Taylor
    *   机器: VaxSN12648, Jumbo
    *   服务: SRC-NFS, X-server
    *   组: SRC, DEC-Employees
    *   信道: Key #7438

## 主体理论 (Theory of Principals)

*   `P says s`: 主体 P 声称陈述 s
*   `A => B`: 主体 A 代表 (speaks for) B
    *   如果 A 说了某事,B 也就说了。所以 A 比 B 更强。
*   安全信道 `C`: 直接声称陈述
    *   如果 P 是 C 上唯一的发送者,则 `C => P`。
*   示例: `Lampson => SRC`, `Key #7438 => Lampson`

## 权限传递 (Handing Off Authority)

*   **传递规则 (Handoff rule)**: 如果 `A says B => A`, 那么 `B => A`。
*   如果 A 是胜任的且可触达的,这就是合理的。
*   示例: `SRC says Lampson => SRC`
*   计算机科学中的任何问题都可以通过增加一个间接层来解决。(Wheeler)〔译注13〕

## 向服务器进行认证 (Authenticating to the Server)

[第 42 页展示了从登录用户到工作站再到服务器的认证链,涉及密钥 `Kbwl`, `Kws`, `Kca` 等]

## 访问控制 (Access Control)

*   **检查访问**: 给定请求 `Q says read O` 和 ACL `P may read O`, 检查 `Q => P`。
*   **审计 (Auditing)**: 每一步都由签名陈述或规则来证明。

## 认证信道 (Authenticating a Channel)

*   认证 —— 谁可以在信道上发送消息。
*   `C => P`; C 是信道,P 是发送者。
*   为了获得新的 `C => P` 事实,必须信任某个主体,即**认证机构 (certification authority, CA)**。
*   最简单的情况:信任 `Kca` 来认证任何名称。

## 认证信道:示例 (Authenticated Channels: Example)

[第 45 页展示了认证链的完整示例,涉及 `Kca says Kbwl => bwl` 等]

## 组与组凭证 (Groups and Group Credentials)

*   定义组: 组是一个主体; 其成员代表该组。
*   证明组成员身份: 使用证书 (certificates)。

## 认证一个组 (Authenticating a Group)

[第 47 页展示了涉及组身份的认证示例]

## 安全:总结 (Security: Summary)

*   **想法**
    *   主体 (Principals)
    *   信道作为主体
    *   “代表” (Speaks for) 关系
    *   权限传递
*   给出精确的规则。
*   应用它们以覆盖多种情况。

## 参考文献 (References)

*   **提示**: Lampson, *Hints for Computer System Design*, 1984.
*   **规范**: Lamport, *A simple approach to specifying concurrent systems*, 1989.
*   **事务**: Gray and Reuter, *Transaction Processing: Concepts and Techniques*, 1993.
*   **安全**: Lampson et al., *Authentication in distributed systems: Theory and practice*, 1992.

## 合作者 (续) (Collaborators)

*   **Charles Simonyi**, **Bob Sproull**
*   **Mel Pirtle**, **Peter Deutsch**, **Chuck Geschke**, **Jim Mitchell**, **Ed Satterthwaite**, **Jim Horning**, **Ron Rider**, **Gary Starkweather**, **Severo Ornstein**
*   项目: Bravo 编辑器, Alto 操作系统, Dover 激光打印机, Interpress 页面描述语言, 940 项目, QSPL/Mesa/Euclid 语言等。

## 合作者 (续) (Collaborators)

*   **Roy Levin**: Wildflower (Star 工作站原型), Vesta (软件配置)
*   **Andrew Birrell**, **Roger Needham**, **Mike Schroeder**: 全局名称服务与认证
*   **Eric Schmidt**: 系统模型
*   **Rod Burstall**: Pebble 语言

---

## 译注

**文本与翻译说明**

1. 本文档译自 Butler Lampson 1992 年图灵奖演讲的幻灯片稿。虽然 Lampson 的图灵奖年份是 1992 年,但实际演讲日期为 1993 年 2 月 17 日。
2. 幻灯片中包含大量技术图示和状态机描述,译文尽可能保留了原稿的结构和逻辑。

**背景与文化注**

1. 〔译注1〕**Hints for Computer System Design**: Lampson 1983 年在 SOSP 发表的经典论文,总结了他在 Xerox PARC 期间的设计经验。
2. 〔译注2〕**Hamming**: Richard Hamming, 1968 年图灵奖得主。这句话是计算机科学界的著名自嘲,对比了物理学界“站在巨人肩膀上”的传承。
3. 〔译注3〕**Bob Taylor, Chuck Thacker**: 两人均为 Xerox PARC 的核心人物。Taylor 是 CSL 实验室主任,Thacker 是 Alto 电脑的主设计师(2009 年图灵奖得主)。
4. 〔译注4〕**Charles Simonyi**: 匈牙利裔程序员,在 Xerox PARC 开发了 Bravo,后加入微软领导开发了 Word 和 Excel,被称为“意图编程”之父。
5. 〔译注5〕**Nancy Lynch**: 分布式计算理论奠基人,以 I/O 自动机模型和 FLP 不可能性证明闻名。
6. 〔译注6〕**Howard Sturgis**: Xerox PARC 研究员,与 Lampson 共同提出了事务处理中的原子性写入等核心概念。
7. 〔译注7〕**Randell**: Brian Randell, 英国计算机科学家,在软件可靠性和系统架构方面有重要贡献。
8. 〔译注8〕**Perlis**: Alan Perlis, 首届图灵奖(1966)得主。原话通常引用为 "One man's constant is another man's variable"。
9. 〔译注9〕**Pascal**: 布莱兹·帕斯卡, 17 世纪法国数学家、物理学家。这句名言常被引用以说明简洁之难。
10. 〔译注10〕**Dijkstra**: Edsger Dijkstra, 1972 年图灵奖得主。
11. 〔译注11〕**Lamport**: Leslie Lamport, 2013 年图灵奖得主,分布式系统领域的泰斗。
12. 〔译注12〕**Paxos**: Lamport 提出的共识算法。在 1993 年当时,Paxos 还是一个相对较新的概念(论文初稿完成于 1989 年,但直到 1998 年才正式发表)。
13. 〔译注13〕**Wheeler**: David Wheeler, 英国计算机科学家, 提出了子程序(subroutine)的概念。这句名言(Fundamental theorem of software engineering)常被归于他名下。

**OCR 与印刷勘误**

1. 原始 PDF 文本提取中,部分数学符号和箭头(如 `=>`, `:=`)在转换时可能存在格式微调,译文已根据上下文语义校正。
2. 第 17 页和第 32 页等包含复杂状态演化图示的页面,在 Markdown 中以文字描述和列表形式进行了简化呈现。
