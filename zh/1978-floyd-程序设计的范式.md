# 程序设计的范式

**The Paradigms of Programming**

> 罗伯特·弗洛伊德(Robert W. Floyd)
> 1978 年 ACM 图灵奖演讲
> 原载 *Communications of the ACM*, Vol. 22, No. 8 (1979 年 8 月), pp. 455–460
> 译自 ACM DL 扫描件 `1283920.1283934.pdf`(个人学习用途)

[1978 年 ACM 图灵奖由奖项委员会主席 Walter Carlson 在 12 月 4 日于华盛顿举行的 ACM 年度会议上授予罗伯特·W·弗洛伊德(Robert W. Floyd)。在评选中,通用技术成就奖小组委员会(原图灵奖小组委员会)表彰弗洛伊德教授“助力创建了计算机科学的以下重要子领域:解析理论、编程语言语义、自动程序验证、自动程序综合以及算法分析”。

弗洛伊德教授分别于 1953 年和 1958 年获得芝加哥大学的文学学士(A.B.)和理学学士(B.S.)学位,他是一位自学成才的计算机科学家。他的计算研究始于 1956 年,当时他作为 IBM 650 的夜间操作员,在装载卡片斗的间隙找时间学习编程。

弗洛伊德实现了最早的 Algol 60 编译器之一,并于 1962 年完成了该项目。在此过程中,他开展了一些早期的编译器优化工作。随后,在 1965 年之前的几年里,弗洛伊德将编程语言的解析工作系统化。为此,他开创了优先法(precedence method)、有界上下文法(bounded context method)和产生式语言法(production language method)进行解析。

1966 年,弗洛伊德教授提出了一种证明程序正确性的数学方法。多年来,他提供了许多快速实用的算法。其中包括:(1) 用于原地排序的堆排序(tree-sort)算法〔译注3〕,(2) 寻找网络最短路径的算法,以及 (3) 寻找中位数和凸包的算法。此外,弗洛伊德还确定了数字加法的极限速度以及在计算机内存中置换信息的极限速度。他在机械定理证明和自动拼写检查器方面的贡献也数不胜数。

近年来,弗洛伊德教授一直致力于设计和实现一种主要供学生使用的编程语言。它将适用于向初学者系统地教授结构化程序设计,并且其功能将近乎通用。]

---

**Paradigm**(pae.radim, - d a i m ) . . . [源自法语 *paradigme*,源自拉丁语 *paradigma*,源自希腊语 *παράδειγμα* 模式,范例,源自 *παραδεικνύναι* 并列展示,并排显示……]
1. 一种模式,典范,例子。
1752 J. Gill *Trinity* v. 91
万物皆依其原型(archetype)、范式(paradigm)、典范(exemplar)与理念(idea)而造。
——摘自《牛津英语词典》

今天,我想谈谈程序设计的范式(paradigms),它们如何影响我们作为计算机程序设计者的成功,应当如何教授它们,以及它们应当如何在我们的编程语言中得以体现。

一个熟悉的程序设计范式例子是结构化程序设计(structured programming)技术,它似乎是当前大多数程序设计方法论论述中的主导范式。结构化程序设计由 Dijkstra [6]、Wirth [27, 29] 和 Parnas [21] 等人阐述,包含两个阶段。

在第一阶段,即自顶向下设计(top-down design)或逐步求精(stepwise refinement)阶段,问题被分解为极少数更简单的子问题。例如,在编写联立线性方程组的求解程序时,第一层分解可能是将其分为消元使方程组三角化阶段,以及随后的三角化系统回代阶段。这种逐渐分解的过程持续进行,直到出现的子问题简单到可以直接处理。在线性方程组的例子中,回代过程将进一步分解为一个逆向迭代过程,该过程从第 $i$ 个方程中求出并存储第 $i$ 个变量的值。进一步的分解将产生一个完全详细的算法。

结构化程序设计范式的第二阶段涉及从底层机器的具体对象和函数向上构建,直到达到自顶向下设计产生的模块中所使用的更抽象的对象和函数。在线性方程组的例子中,如果方程的系数是单变量的有理函数,我们可能首先设计多精度算术表示及其过程,然后在此基础上构建具有自身算术过程的多项式表示,等等。这种方法被称为抽象层次(levels of abstraction)法或信息隐藏(information hiding)法。

结构化程序设计范式绝非被普遍接受。其最坚定的拥护者也会承认,它本身不足以使所有难题变简单。其他更专门的高级范式,如分支定界(branch-and-bound) [17, 20] 或分治(divide-and-conquer) [1, 11] 技术,仍然至关重要。然而,结构化程序设计范式确实起到了扩展设计能力的作用,允许构建那些如果没有方法论支持就无法高效且可靠地设计的复杂程序。

我相信,计算机程序设计的现状反映了我们在范式储备上的不足、对现有范式知识的匮乏、教授编程范式方式的落后,以及我们的编程语言在支持(或未能支持)其用户群体的范式方面的缺陷。

Robert Balzer [3] 最近用这样的话描述了计算机程序设计的现状:“众所周知,软件正处于萧条状态。它不可靠、交付延迟、对变化反应迟钝、效率低下且昂贵。此外,由于它目前是劳动密集型的,随着需求增加和劳动力成本上升,情况将进一步恶化。”如果这听起来像十多年前著名的“软件危机”,那么我们已经处于这种状态十到十五年这一事实表明,“软件萧条”(software depression)是一个更贴切的词。

托马斯·库恩(Thomas S. Kuhn)在《科学革命的结构》[16]〔译注4〕中,将过去几个世纪的科学革命描述为由主导范式的改变所引发。库恩的一些观察似乎适用于我们的领域。关于向学生展示当前科学知识的科学教科书,库恩写道:

> 例如,这些教材往往暗示,科学的内容完全由其书页中所描述的观察、定律和理论所体现。

同样,大多数关于计算机程序设计的教材都暗示,编程的内容就是其书页中所描述的算法知识和语言定义。

库恩还写道:

> 对范式的研究……主要是为了让学生准备好成为他随后将在其中执业的特定科学共同体的一员。因为他在那里加入的是从同样具体的模型中学习其领域基础的人,他随后的执业将很少在基本原理上引发公开的分歧……

在计算机科学中,人们可以看到几个这样的共同体,每个共同体都说着自己的语言并使用自己的范式。事实上,编程语言通常鼓励使用某些范式而阻碍使用其他范式。存在定义明确的 Lisp 编程流派、APL 编程流派、Algol 编程流派等等。有些人将数据流视为程序的主要结构信息,而有些人则认为是控制流。递归与迭代、数据结构的复制与共享、传名调用与传值调用,都各有拥趸。

库恩再次写道:

> 旧的学派逐渐消失。它们的消失部分是由于其成员转向了新的范式。但总有一些人固守一种或另一种旧观点,他们被简单地排除在专业领域之外,此后该领域便不再理会他们的工作。

在计算领域,没有这种将人排除在专业领域之外的机制。我怀疑他们主要变成了软件开发的管理人员。

Balzer 在他针对软件构建现状的悲叹中,接着预言自动程序设计将拯救我们。我祝愿自动程序员们成功,但在他们清理完马厩之前,我们最好的希望是提高我们自己的能力。我相信,我们改善编程普遍实践的最佳机会在于关注我们的范式。

在 20 世纪 60 年代早期,上下文无关语言的解析在编译器开发和自然语言学中都是一个紧迫的重要问题。已发表的算法通常既慢又不正确。据称 John Cocke 没费什么力气就发现了一个快速而简单的算法 [2],该算法基于一个现在已成为标准的范式,即动态规划(dynamic programming) [1] 的计算形式。动态规划范式通过首先迭代地解决所有较小输入的子问题,来解决给定输入的问题。Cocke 的算法相继找到了输入的所有子串的所有解析。在这个概念框架下,问题变得近乎平庸。由此产生的算法是第一个统一在多项式时间内运行的算法。

大约在同一时间,在几个不正确的自顶向下解析器发表之后,我通过发明一种范式来攻击设计正确解析器的问题:寻找一种处理器的分层组织,类似于雇佣和解雇下属的人类组织,它可以解决该问题,然后模拟这个组织的决策行为 [8]。对这种多重递归过程的模拟引导我使用递归协程(recursive coroutines)作为一种控制结构。后来我发现,其他处理困难组合问题的程序员,例如 Gelernter 及其几何定理证明机 [10],显然也发明了同样的控制结构。

John Cocke 的经历和我的经历说明,编程的持续进步可能需要不断发明、完善和传播新的范式。

一个有效完善范式的例子是 Shortliffe 和 Davis 在 MYCIN [24] 程序上的工作,该程序能熟练地诊断细菌感染并推荐药物。MYCIN 是一个基于规则的系统(rule-based system),基于一大组独立的规则,每条规则都有一个可测试的适用条件,以及当条件满足时产生的一个简单的结果动作。Davis 的 TEIRESIAS [5] 程序修改了 MYCIN,允许专家用户改进 MYCIN 的性能。TEIRESIAS 程序通过从不理想的结果向后追溯责任,穿过允许该结果发生的规则和条件,直到找到一条从有效假设产生无效结果的不合格规则,从而完善了该范式。通过这种手段,让一位不是程序员的医学专家改进 MYCIN 的诊断能力在技术上变得可行。虽然 MYCIN 中没有任何东西是不能用传统的带有条件转移的决策分支树来编码的,但正是基于规则的范式的使用,及其随后用于自我修改的完善,使得程序的交互式改进成为可能。

如果编程艺术的普遍进步需要不断发明和完善范式,那么个体程序员艺术的进步则要求他扩大自己的范式库。在我自己设计困难算法的经验中,我发现某种技术对扩展我自己的能力最有帮助。在解决了一个具有挑战性的问题后,我从头开始再次解决它,仅追溯早期解决方案的洞察力。我重复这一过程,直到解决方案尽可能清晰直接。然后,我寻找一个攻击类似问题的通用规则,这个规则本可以引导我在第一次就以最高效的方式处理给定的问题。通常,这样的规则具有永久的价值。通过寻找这样的通用规则,我从之前提到的基于递归协程的解析算法引导到了编写非确定性程序(nondeterministic programs) [9] 的通用方法,这些程序随后通过宏展开转换为传统的确定性程序。这一范式后来在人工智能中计算机解决问题这一显然不相关的领域找到了用途,并体现在编程语言 PLANNER [12, 13]、MICROPLANNER [25] 和 QA4 [23] 中。

个体程序员获取新范式可能会受到阅读他人程序的鼓励,但这受到一个限制:一个人的同事很可能是因为与本地范式集兼容而被选中的。这一点的证据是,我们的行业经常打广告招募的不是程序员,而是 Fortran 程序员或 Cobol 程序员。Fortran 的规则可以在几小时内学会;相关的范式则需要长得多的时间去学习,以及去摒弃。

接触在异域惯例下编写的程序可能会有所帮助。今年在麻省理工学院(MIT)休假期间,我看到了许多 Lisp 程序员获得的编程能力的例子,这些能力源于拥有单一的数据结构,该结构也被用作程序中出现的所有函数和操作的统一语法结构,并具有将程序作为数据处理的能力。虽然我之前的热情一直在于像 Algol 家族这样语法丰富的语言,但我现在清晰而具体地看到了闵斯基(Minsky) 1970 年图灵奖演讲 [19] 的力量,他在演讲中辩称,Lisp 结构的统一性和自我引用的力量赋予了程序员一些能力,其内容非常值得牺牲视觉形式。我希望能达成这些方法的某种适当综合。

现在和 1956 年我进入计算领域时一样,每个人都想设计一种新的编程语言。正如斯坦福大学研究生办公室墙上写的:“我宁愿编写程序来帮我写程序,也不愿写程序。”在评估每年的新编程语言产出时,根据它们允许和鼓励使用有效编程范式的程度对其进行分类是有帮助的。当我们明确我们的范式时,我们会发现它们数量巨大。Cordell Green [11] 发现,机械生成简单的搜索和排序算法(如归并排序和快速排序)需要一百多条规则,其中大多数可能是大多数程序员熟悉的范式。通常,我们的编程语言在甚至使用熟悉的低级范式方面没有给我们提供任何帮助,甚至阻碍了我们。下面是一些例子。

假设我们正在模拟一个捕食者-猎物系统(predator-prey system)——也许是狼和兔子。我们有两个方程:

$$W' = f(W, R)$$
$$R' = g(W, R)$$

它们给出了一个时间段结束时狼和兔子的数量,作为该时段开始时数量的函数。

初学者常犯的一个错误是写成:

```pascal
FOR I := ... DO
BEGIN
  W := f(W, R);
  R := g(W, R)
END
```

其中 $g$ 被错误地使用修改后的 $W$ 值进行评估。为了使程序正常工作,我们必须写成:

```pascal
FOR I := ... DO
BEGIN
  REAL TEMP;
  TEMP := f(W, R);
  R := g(W, R);
  W := TEMP
END
```

初学者认为我们不应该被迫这样做是正确的。我们最常见的范式之一,如在捕食者-猎物模拟中,是向状态向量的分量同时赋值(simultaneous assignment)新值。然而,几乎没有任何语言具有同时赋值运算符。相反,我们必须经历机械的、浪费时间的且容易出错的操作,即引入一个或多个临时变量并通过它们转移新值。

再看这个看起来很简单的问题:

> 读取文本行,直到发现一个完全空白的行。消除单词之间多余的空格。打印文本,每行三十个字符,不要在行间断开单词。

因为输入和输出都自然地使用多层迭代来表达,且因为输入迭代与输出迭代不嵌套,这个问题在大多数编程语言中出人意料地难以编程 [14]。初学者花费的时间是教员预期的三到四倍,最终要么搞出一团乱麻,要么使用显式增量和条件执行来模拟某些所需迭代的自制控制结构。

这个问题通过分解为三个通信协程(communicating coroutines) [4] 来自然地表述,分别用于字符流的输入、转换和输出。然而,除了模拟语言外,我们的编程语言中很少有足够的协程控制结构来允许以自然的方式对该问题进行编程。

当一种语言使某种范式变得方便时,我会说该语言支持(supports)该范式。当一种语言使某种范式可行但不方便时,我会说该语言弱支持(weakly supports)该范式。正如前两个例子所示,我们的大多数语言仅弱支持同时赋值,且根本不支持协程,尽管所需的机制比十七年前在 Algol 家族语言中实现的递归传名调用过程要简单得多,也更有用。

甚至结构化程序设计范式充其量也只是被我们的许多编程语言弱支持。为了按照设计思路写下联立方程求解器,人们应该能够写成:

```pascal
MAIN__PROGRAM:
BEGIN
  TRIANGULARIZE;
  BACK__SUBSTITUTE
END;

BACK__SUBSTITUTE:
  FOR I := N STEP -1 UNTIL 1 DO
    SOLVE__FOR__VARIABLE(I);

SOLVE__FOR__VARIABLE(I):
  ---
  ---

TRIANGULARIZE:
  ---
  ---

Procedures for multiple-precision arithmetic
Procedures for rational-function arithmetic
Declarations of arrays
```

在大多数当前语言中,人们不能按此顺序呈现主程序、过程和数据声明。通常需要进行一些初步的人工文本重排,而这种重排本应是易于机械化的。此外,在多个多精度过程中使用的任何变量对于可以进行多精度算术的程序的每个部分都必须是全局的,从而允许意外修改,这违反了信息隐藏原则。最后,将问题详细分解为过程层次结构通常会导致非常低效的代码,尽管大多数过程仅从一处调用,本可以通过宏展开高效实现。

比结构化程序设计范式抽象层次更高的范式是构建语言层次结构,其中最高层语言中的程序操作最抽象的对象,并被翻译成下一层语言中的程序。例子包括在 Lisp、Fortran 和其他语言之上构建的众多公式处理语言。我们的大多数低层语言未能完全支持此类超结构。例如,它们的错误诊断系统通常是固定不变的,因此诊断消息只有通过参考低层翻译后的程序才能理解。

我相信,编程作为一种手艺的持续进步要求开发和传播支持其用户群体主要范式的语言。语言的设计应先列举这些范式,包括研究由于不支持范式的阻碍而导致的编程缺陷。只要我谈到的范式以及许多其他范式仍然不受支持或仅受弱支持,我就对我们语言的扩展(如 Pascal 的变体记录和幂集 [15, 28])感到不满意。如果曾经有一门编程语言设计的科学,它可能在很大程度上由将语言与其支持的设计方法相匹配所组成。

我不想暗示对范式的支持仅限于我们的编程语言本身。我们编程的整个环境,包括诊断系统、文件系统、编辑器等,都可以被分析为支持或未能支持程序设计方法的频谱。有希望的是,这一点正得到认可。例如,法国 IRIA〔译注12〕及其他地方最近的工作已经实现了能够感知所编辑程序结构的编辑器 [7, 18, 26]。任何尝试过哪怕是像更改程序中作为标识符出现的每一个 X 而不无意中更改所有其他 X 这样简单任务的人,都会对此表示赞赏。

现在我想谈谈我们作为计算机程序设计所教授的内容。闵斯基在其图灵奖演讲 [19] 中对形式重于内容的病态痴迷表示哀悼,这种痴迷的一部分体现在我们对教学内容的典型选择中。如果我问另一位教授他在编程入门课程中教什么,无论他自豪地回答“Pascal”还是羞怯地回答“FORTRAN”,我都知道他教的是语法、一套语义规则和一些现成的算法,而让学生自己去发现某种设计过程。即使是基于结构化程序设计范式的教材,虽然在最高层(我们可以称之为程序设计的“故事”层)给出了指导,但在中间层(我们可以称之为“段落”层)往往不提供任何帮助。

我相信,显式地教授一套适用于程序设计所有层次的系统方法是可能的,并且接受过此类训练的学生比那些完全通过研究现成程序进行传统教学的学生具有巨大的领先优势。

我们可以教授的内容示例如下。

当我向学生介绍编程语言的输入功能时,我介绍了一个交互式输入的标准范式,以一个我称之为 `PROMPT__READ__CHECK__ECHO` 的宏指令形式出现,它持续读取直到输入数据满足有效性测试,然后在输出文件中回显它。这个宏在某种程度上本身就是迭代和输入的范式。同时,由于它读取的次数比说“无效数据”的次数多一次,它实例化了一个更通用的、之前教过的执行“n 次半”的循环范式。

`PROMPT__READ__CHECK__ECHO`: 参数是一个字符串 `PROMPT`,一个待读取的变量 `V`,以及一个表征错误数据的条件 `BAD`;
```pascal
PRINT__ON__TERMINAL(PROMPT);
READ__FROM__TERMINAL(V);
WHILE BAD(V) DO
BEGIN
  PRINT__ON__TERMINAL("Invalid data");
  READ__FROM__TERMINAL(V)
END;
PRINT__ON__FILE(V)
```

它还在更高层次上实例化了程序员对程序用户的责任,包括每个程序组件都应受到保护,免受该组件未设计的输入影响的想法。

Howard Shrobe 和 MIT 程序员学徒(Programmer's Apprentice)小组 [22] 的其他成员成功地向他们的初学者教授了一个具有广泛用途的范式,他们称之为生成/过滤/累积(generate/filter/accumulate)。学生们学会将许多表面上不同的问题识别为由枚举集合元素、过滤出子集以及累积子集中元素的某些函数所组成。学生们使用的 MACLISP 语言 [18] 支持该范式;学生只需提供生成器、过滤器和累加器。

我之前提到的捕食者-猎物模拟也是一个通用范式——状态机范式(state-machine paradigm)的实例。状态机范式通常涉及通过一组存储变量的值来表示计算状态。如果状态复杂,转移函数需要一个处理同时赋值的设计范式,特别是因为大多数语言仅弱支持同时赋值。为了说明,假设我们要计算:

$$\frac{\pi}{6} = \arcsin\left(\frac{1}{2}\right) = \frac{1}{2 \cdot 1} + \frac{1}{2^3 \cdot 2 \cdot 3} + \frac{1 \cdot 3}{2^5 \cdot 2 \cdot 4 \cdot 5} + \frac{1 \cdot 3 \cdot 5}{2^7 \cdot 2 \cdot 4 \cdot 6 \cdot 7} + \dots$$

其中我圈出了每个加数中对计算右侧下一个加数有用的部分。在不描述此类过程的完整设计范式的情况下,状态转移设计的一部分是系统地找到一种方法,从

$$Q = \frac{1 \cdot 3}{2^5 \cdot 2 \cdot 4}, \quad C = 5, \quad S = \frac{1}{2} + \dots + \frac{1 \cdot 3}{2^5 \cdot 2 \cdot 4 \cdot 5}$$

得到

$$Q' = \frac{1 \cdot 3 \cdot 5}{2^7 \cdot 2 \cdot 4 \cdot 6}, \quad C' = 7, \quad S' = \frac{1}{2} + \dots + \frac{1 \cdot 3 \cdot 5}{2^7 \cdot 2 \cdot 4 \cdot 6 \cdot 7}$$

经验丰富的程序员已经内化了这一步,在除最复杂情况外的所有情况下都是无意识地完成的。对于初学者来说,显式地看到该范式使他能够攻击比没有帮助时更复杂的状态机问题,并且更重要的是,鼓励他自己识别其他有用的范式。

在计算机程序设计教材中可以找到的大多数经典算法都可以被视为更广泛范式的实例。辛普森法则(Simpson's rule)是外推至极限的一个实例。高斯消元法是通过递归下降解决问题并转换为迭代形式的实例。归并排序是分治范式的一个实例。对于每一个这样的经典算法,人们都可以问:“我该如何发明这个?”,并找回本应同样经典的范式。

总而言之,我给严肃程序员的信息是:花一部分工作时间检查和完善你自己的方法。尽管程序员总是在为赶上未来或过去的截止日期而奋斗,但方法论上的抽象是一项明智的长期投资。

对于编程教师,我更要说:尽可能充分地识别你使用的范式,然后显式地教授它们。当 Fortran 取代拉丁语和梵语成为典型的死语言时,它们将为你的学生服务。

对于编程语言的设计者,我说:除非你能支持我编程时使用的范式,或者至少支持我将你的语言扩展为支持我编程方法的语言,否则我不需要你闪亮的新语言;就像旧车或旧房子一样,旧语言有我已经学会忍受的局限性。要说服我你的语言的优点,你必须向我展示如何在其中构建程序。我不想阻碍新语言的设计;我想鼓励语言设计者成为设计过程细节的严肃研究者。

感谢 ACM 的成员们,提名我进入由我的前任图灵奖演讲者组成的杰出人物行列。没有人能在没有帮助的情况下达到这个位置。我欠许多人感激之情,特别是四个人:Ben Mittman,他在我职业生涯早期帮助并鼓励我追求我对计算兴趣中科学和学术的一面;Herb Simon,我们专业的文艺复兴人,他的谈话本身就是一种教育;已故的 George Forsythe,他为我提供了计算教学的范式;以及我的同事 Donald Knuth,他树立了一个杰出的知识诚信典范。我也很幸运拥有许多优秀的的研究生,我认为我从他们身上学到的和教给他们的一样多。

对你们所有人,我深表感激并深感荣幸。

---

## 参考文献

1. Aho, A.V., Hopcroft, J.E., and Ullman, J.D. *The Design and Analysis of Computer Algorithms*. Addison-Wesley, Reading, Mass. 1974.
2. Aho, A.V., and Ullman, J.D. *The Theory of Parsing, Translation, and Compiling, Vol. 1: Parsing*. Prentice-Hall, Englewood Cliffs, New Jersey, 1972.
3. Balzer, R. Imprecise program specification. Report ISI/RR-75-36, Inform. Sciences Inst., Dec. 1975.
4. Conway, M.E. Design of a separable transition-diagram compiler. *Comm. ACM 6*, 7 (July 1963), 396–408.
5. Davis, R. Interactive transfer of expertise: acquisition of new inference rules. *Proc. Int. Joint Conf. on Artif. Intell.*, MIT, Cambridge, Mass., August 1977, pp. 321–328.
6. Dijkstra, E.W. Notes on structured programming. In *Structured Programming*, O.J. Dahl, E.W. Dijkstra, and C.A.R. Hoare, Academic Press, New York, 1972, pp. 1–82.
7. Donzeau-Gouge, V., Huet, G., Kahn, G., Lang, B., and Levy, J.J. A structure oriented program editor: A first step towards computer assisted programming. Res. Rep. 114, IRIA, Paris, April 1975.
8. Floyd, R.W. The syntax of programming languages—a survey. *IEEE EC-13*, 4 (Aug. 1964), 346–353.
9. Floyd, R.W. Nondeterministic algorithms. *J. ACM 14*, 4 (Oct. 1967), 636–644.
10. Gelernter. Realization of a geometry-theorem proving machine. In *Computers and Thought*, E. Feigenbaum and J. Feldman, Eds., McGraw-Hill, New York, 1963, pp. 134–152.
11. Green, C.C., and Barstow, D. On program synthesis knowledge. *Artif. Intell. 10*, 3 (June 1978), 241–279.
12. Hewitt, C. PLANNER: A language for proving theorems in robots. *Proc. Int. Joint Conf. on Artif. Intell.*, Washington, D.C., 1969.
13. Hewitt, C. Description and theoretical analysis (using schemata) of PLANNER... AI TR-258, MIT, Cambridge, Mass., April 1972.
14. Hoare, C.A.R. Communicating sequential processes. *Comm. ACM 21*, 8 (Aug. 1978), 666–677.
15. Jensen, K., and Wirth, N. *Pascal User Manual and Report*. Springer-Verlag, New York, 1978.
16. Kuhn, T.S. *The Structure of Scientific Revolutions*. Univ. of Chicago Press, Chicago, Ill., 1970.
17. Lawler, E., and Wood, D. Branch and bound methods: A survey. *Operations Res. 14*, 4 (July-Aug. 1966), 699–719.
18. *MACLISP Manual*. MIT, Cambridge, Mass., July 1978.
19. Minsky, M. Form and content in computer science. *Comm. ACM 17*, 2 (April 1970), 197–215.
20. Nilsson, N.J. *Problem Solving Methods in Artificial Intelligence*. McGraw-Hill, New York, 1971.
21. Parnas, D. On the criteria for decomposing systems into modules. *Comm. ACM 15*, 12 (Dec. 1972), 1053–1058.
22. Rich, C., and Shrobe, H. Initial report on a LISP programmer's apprentice. *IEEE J. Software Eng. SE-4*, 6 (Nov. 1978), 456–467.
23. Rulifson, J.F., Derkson, J.A., and Waldinger, R.J. QA4: A procedural calculus for intuitive reasoning. Tech. Note 73, Stanford Res. Inst., Menlo Park, Calif., Nov. 1972.
24. Shortliffe, E.H. *Computer-based Medical Consultations: MYCIN*. American Elsevier, New York, 1976.
25. Sussman, G.J., Winograd, T., and Charniak, C. *MICROPLANNER reference manual*. AI Memo 203A, MIT, Cambridge, Mass., 1972.
26. Teitelman, W., et al. *INTERLISP manual*. Xerox Palo Alto Res. Ctr., 1974.
27. Wirth, N. Program development by stepwise refinement. *Comm. ACM 14*, (April 1971), 221–227.
28. Wirth, N. The programming language Pascal. *Acta Informatica 1*, 1 (1971), 35–63.
29. Wirth, N. *Systematic Programming, an Introduction*. Prentice-Hall, Englewood Cliffs, New Jersey, 1973.

---

## 译注

**文本与翻译说明**

1. 罗伯特·弗洛伊德(Robert W. Floyd, 1936–2001),1978 年图灵奖得主。他在解析理论、编程语言语义、自动程序验证等领域做出了奠基性贡献。著名的 Floyd-Hoare 逻辑即以他与 C.A.R. Hoare 命名。
2. 本文标题中的 "Paradigm" 一词,弗洛伊德明确借用了托马斯·库恩在《科学革命的结构》中的用法。在中文语境下,通常译为“范式”。

**背景与文化注**(译者补注,原文无)

3. 〔译注3〕 **tree-sort**: 弗洛伊德在此指的是他 1964 年发表的堆排序(Heapsort)算法的早期版本。虽然他在文中称之为 "tree-sort",但在现代算法教材中,这通常被称为堆排序。
4. 〔译注4〕 **《科学革命的结构》**: 托马斯·库恩(Thomas Kuhn) 1962 年出版的名著,提出了“范式转移”(paradigm shift)的概念,深刻影响了科学哲学和科学史研究。
5. **软件萧条(software depression)**: 弗洛伊德在此幽默地对比了当时流行的“软件危机”(software crisis)说法。他认为既然这种糟糕状态已经持续了十多年,就不再是暂时的“危机”,而是长期的“萧条”。
6. **John Cocke**: 1987 年图灵奖得主,编译器优化和 RISC 架构的先驱。文中提到的算法即著名的 CYK 算法(Cocke-Younger-Kasami)的一部分。
7. **MYCIN**: 20 世纪 70 年代在斯坦福大学开发的早期专家系统,用于诊断血液感染。它是基于规则的系统的代表作。
8. **PLANNER/MICROPLANNER/QA4**: 20 世纪 70 年代初开发的一系列人工智能编程语言,引入了非确定性编程和基于目标的搜索等概念。
9. **闵斯基(Marvin Minsky)**: 1969 年图灵奖得主,人工智能先驱。弗洛伊德提到的 1970 年演讲《计算机科学的形式与内容》批评了当时计算机科学过于关注形式化语法而忽视实际内容的倾向。
10. **捕食者-猎物系统**: 即 Lotka-Volterra 模型,用于描述生态系统中两个物种(如狼和兔子)相互作用的数学模型。
11. **同时赋值(simultaneous assignment)**: 弗洛伊德指出,在处理状态转移时,同时更新多个变量的值是一个非常自然的范式,但当时的编程语言(如 Fortran, Algol)大多不支持,需要通过临时变量手动实现。
12. 〔译注12〕 **IRIA**: 法国国家信息与自动化研究所(Institut de Recherche en Informatique et en Automatique),现名为 Inria。
13. **辛普森法则(Simpson's rule)**: 数值积分的一种方法。
14. **高斯消元法(Gaussian elimination)**: 求解线性方程组的经典算法。
15. **Ben Mittman, Herb Simon, George Forsythe, Donald Knuth**: 弗洛伊德在致谢中提到的四位重要人物。Herb Simon(赫伯特·西蒙)是 1975 年图灵奖得主,也是诺贝尔经济学奖得主;George Forsythe 是斯坦福大学计算机科学系的创始人;Donald Knuth(高德纳)是 1974 年图灵奖得主,《计算机程序设计艺术》的作者。

**OCR 与印刷勘误**

16. 扫描件中部分数学公式和代码块存在 OCR 识别错误(如 `pae.radim` 应为 `paradigm` 的音标表示,`pae.radim, - d a i m` 系 OCR 误读了音标符号)。译文已对照原刊页面图像进行了校正。
17. 原文第 459 页公式中的圆圈标记在 OCR 文本中丢失,译文通过 LaTeX 公式还原了其数学逻辑。
18. 参考文献 [3] 中的作者名 "Baker" 应为 "Balzer",系原刊印刷或 OCR 错误,已校正。
