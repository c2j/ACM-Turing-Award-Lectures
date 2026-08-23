# 人工智能中的通用性

**Generality in Artificial Intelligence**

> 约翰·麦卡锡(John McCarthy)〔译注1〕
> 1971 年 ACM 图灵奖(演讲文稿作于 1987 年)
> 原载 *Communications of the ACM*, Vol. 30, No. 12 (1987 年 12 月), pp. 1030–1035
> 译自 ACM DL 扫描件 `1283920.1283926.pdf`(个人学习用途)

> 约翰·麦卡锡于 1971 年发表的图灵奖演讲从未正式出版。下文是作者于 1986 年撰写的后记,旨在反映原演讲的风貌,并结合过去 15 年的发展进行评述。

## 后记

我在 1971 年的图灵奖演讲题目是“人工智能中的通用性”。事实证明,这个主题过于宏大,以至于我发现当时无法以令人满意的书面形式表达我的想法。如果当时选择回顾以往的工作而不是尝试创新的话,情况可能会好一些,但那在当时并不符合我的习惯。

我很感谢 ACM 给我再次尝试的机会。对我们的科学来说不幸的是,但对本项目来说或许是幸运的是,人工智能(AI)中的通用性问题几乎和以往一样悬而未决,尽管我们现在有了许多 1971 年尚不具备的想法。本文在很大程度上依赖于这些想法,但它远非一份完整的 1986 年实现通用性方法的综述。对想法的讨论篇幅与其说取决于客观标准,不如说取决于我对它们的熟悉程度。

在 1971 年甚至 1958 年,AI 程序缺乏通用性是显而易见的。现在这一点依然显而易见,而且有了更多细节。第一个明显的症状是,对程序想法的一个微小补充往往涉及从数据结构开始的彻底重写。在数据结构模块化方面已经取得了一些进展,但如果不重写,搜索策略的微小修改甚至更难实现。

另一个症状是,没有人知道如何建立一个通用的常识知识(common sense knowledge)〔译注2〕数据库,供任何需要这些知识的程序使用。除了其他信息外,这样的数据库还将包含机器人需要了解的关于移动物体的效果、一个人对其家庭的预期了解以及关于买卖的事实。这并不取决于知识是用逻辑语言还是其他形式化方法来表达。当我们采用逻辑方法研究 AI 时,缺乏通用性表现为我们设计的用于表达常识知识的公理在通用常识数据库中的适用性过于受限。在我看来,获得一种用于表达通用常识知识以纳入通用数据库的语言,是 AI 通用性问题的关键。

以下是 1971 年前后提出的一些实现通用性的想法。我再次声明,这并非详尽无遗。

## 以程序表示行为

Friedberg [7, 8] 讨论了一种完全通用的表示行为的方法,并提供了一种通过学习来改进行为的方法。即行为由计算机程序表示,学习通过对程序进行随机修改并测试修改后的程序来实现。Friedberg 的方法仅成功学习了如何将一个比特从一个存储单元移动到另一个存储单元,而他通过降低成功运行中涉及的指令被修改的概率来奖励这些指令的方案,被 Simon [24] 证明不如彻底测试每个程序并完全废弃任何不完美的程序。似乎没有人尝试跟进通过修改整个程序进行学习的想法。

Friedberg 方法的缺陷在于,虽然用程序表示行为是完全通用的,但通过对程序进行微小修改来修改行为却是非常特殊的。行为上的微小概念修改通常并不表现为程序的微小修改,特别是如果使用机器语言程序,并且认为程序文本的任何一个微小修改都具有相同的可能性。

或许值得尝试一些更类似于遗传进化的方法;制作子程序的副本,修改其中一些副本而保留其他副本。然后学习系统将实验将原始子程序的某些调用更改为修改后子程序的调用是否有利。很可能即使这样也行不通,除非通过调用略微修改的子程序可以获得相关的行为微小修改。可能还需要提供对子程序参数数量的修改。

虽然 Friedberg 的问题是从经验中学习,但当目标是结合不同的知识或制作修改知识的程序时,所有以程序表示知识的方案都面临类似的困难。

## 通用问题求解器 (GPS) 及其后继者

AI 中的一种通用性包含独立于问题领域的寻找解的方法。Allen Newell、Herbert Simon 及其同事和学生开创了这种方法并继续追求它。

Newell 等人最初在 1957 年提出了 GPS [18]〔译注3〕。最初的想法是将某些通用类别的问题表示为通过一组允许的规则将一个表达式转换为另一个表达式的问题。在 [20] 中甚至建议,改进 GPS 可以被视为此类问题。在我看来,GPS 作为通用问题求解器是不成功的,因为问题通常不采取这种形式,而且解决问题和实现目标所需的大部分知识不能简单地以转换表达式规则的形式表示。然而,GPS 是第一个将目标和子问题的解结构与特定领域分离的系统。

如果 GPS 真的能做到通用,也许 Newell 和 Simon 关于 AI 迅速成功的预言就会实现。Newell 目前提出的通用问题表示候选者 [22] 是 SOAR,据我理解,它关注的是将一个状态转换为另一个状态,其中状态不需要由表达式表示。

## 产生式系统

第一批产生式系统(production systems)〔译注4〕是由 Newell 和 Simon 在 20 世纪 50 年代完成的,该想法记录在 [21] 中。通过对所有类型的问题使用相同的目标寻求机制,仅更改特定的产生式,从而实现了一种通用性。早期的产生式系统已经发展成为目前激增的专家系统外壳。

产生式系统以事实和规则的形式表示知识,规则之间几乎总是有明显的语法区别。事实通常对应于逻辑公式的基项实例(ground instances),即对应于应用于常量表达式的谓词符号。与基于逻辑的系统不同,这些事实不包含变量或量词。新事实通过推理、观察和用户输入产生。变量保留给规则,规则通常采取“模式-动作”(pattern-action)形式。规则由程序员或“知识工程师”放入系统中,在大多数系统中不能通过系统的动作产生。作为接受这些限制的交换,产生式系统程序员得到了一个相对较快的程序。

产生式系统程序很少使用该领域的基础知识。例如,MYCIN [2] 有许多关于如何根据症状和实验室测试结果推断哪种细菌引起疾病的规则。然而,它的形式化方法无法表达细菌是在体内生长的生物这一事实。事实上,MYCIN 无法表示随时间发生的过程,尽管其他产生式系统可以在下一节将要描述的情境演算水平上表示过程。

产生式系统模式匹配的结果是用常量替换模式部分中的变量。因此,产生式系统不会推断通用命题。例如,考虑这样一个定义:如果一个容器被密封以防止细菌进入,且其中的所有细菌都已死亡,则该容器是无菌的。产生式系统(或逻辑程序)只能通过用特定细菌替换变量来使用这一事实。因此,它无法推论加热密封容器会使其灭菌(假设加热的细菌会死亡),因为它无法对容器中未列举的细菌集合进行推理。这些问题在 [14] 中有进一步讨论。

## 以逻辑表示知识

在 1958 年,我似乎觉得行为的微小修改最常表现为对世界信念的微小修改,这需要一个显式表示信念的系统。

> 如果想让机器能够发现一种抽象,那么机器似乎最有可能必须能够以某种相对简单的方式表示这种抽象。[11, p. 78]

1960 年提高通用性的想法是使用逻辑以一种独立于随后可能使用事实的方式来表达事实。当时和现在看来,人类主要通过陈述句而不是编程语言进行交流,这是出于良好的客观原因,无论交流者是人类、半人马座阿尔法星的生物还是计算机程序,这些原因都适用。此外,陈述性信息的优势也适用于内部表示。陈述性信息的优势在于通用性。两个物体碰撞时会发出声音这一事实,在特定情况下可用于制造声音、避免制造声音、解释声音或解释声音的缺失。(我猜那些车没撞上,因为虽然我听到了刹车声,但我没听到撞击声。)

一旦决定构建一个以陈述方式表示信息的 AI 系统,仍需决定允许哪种陈述性语言。最简单的系统仅允许应用于常量符号的常量谓词,例如 $on(Block1, Block2)$。接下来,可以允许由函数符号、常量和谓词符号构建的任意常量项,例如 $location(Block1) = top(Block2)$。Prolog 数据库允许包含自由变量的任意 Horn 子句,例如 $P(x, y) \land Q(y, z) \supset R(x, z)$,用标准逻辑符号表示 Prolog。除此之外是完整的一阶逻辑,包括存在量词和全称量词以及任意一阶公式。在一阶逻辑中,理论的表达能力取决于允许变量范围的域。重要的表达能力来自使用集合论,它包含理论中任何对象的集合表达式。

表达能力的每一次提高都以推理和问题求解程序所需的复杂性为代价。换句话说,接受对陈述性信息表达能力的限制可以简化搜索过程。Prolog 代表了这一连续体中的一个局部最优解,因为 Horn 子句具有中等表达能力,但可以由逻辑问题求解器直接解释。

通常接受的一个主要限制是将新事实的推导限制在不含变量的公式中,即用常量替换变量,然后进行命题推理。看来人类的大多数日常活动仅涉及此类推理。原则上,Prolog 略微超出了这一点,因为 Prolog 程序发现的作为变量值的表达式本身可以包含自由变量。然而,除了中间结果外,这种功能很少使用。

如果没有比 Prolog 允许的更多的谓词演算,就无法进行全称泛化(universal generalization)。考虑罐装的原理。我们说如果一个容器是密封的且其中的所有细菌都已死亡,则该容器是无菌的。这可以表示为 Prolog 程序的一个片段,如下所示:

```prolog
sterile(X) :- sealed(X), not alive-bacterium(Y, X).
alive-bacterium(Y, X) :- in(Y, X), bacterium(Y), alive(Y).
```

然而,直接包含此片段的 Prolog 程序只能通过单独杀死每个细菌来使容器灭菌,并且需要程序的其他部分相继生成细菌的名称。它不能用于发现或合理化罐装——密封容器然后加热以一次性杀死所有细菌。合理化罐装的推理以本质的方式涉及量词的使用。

我个人的观点是,推理和问题求解程序最终将不得不允许充分使用量词和集合,并拥有足够强大的控制方法来使用它们而不会产生组合爆炸。

虽然 1958 年的想法很受欢迎,但在随后的几年里很少有人尝试在程序中体现它,主要的一个是 Black 1964 年的哈佛博士论文。我把大部分时间花在我认为的初步项目上,主要是 LISP〔译注5〕。我不尝试实现的主要原因是我首先想学习如何用逻辑表达常识知识。这仍然是我的目标。如果追求非逻辑方法的人在实现通用性方面取得了显著成功,我可能会灰心丧气而不再继续追求它。

McCarthy 和 Hayes [12] 区分了 AI 问题的认识论(epistemological)和启发式(heuristic)方面,并断言认识论更容易研究通用性。区别在于,当可用事实推导出某种策略适合实现目标时,认识论就完成了;而启发式问题涉及寻找合适策略的搜索。

[11] 中隐含了通用常识数据库的想法。人类拥有的常识信息将被写成逻辑句子并包含在数据库中。任何寻求目标的程序都可以查阅数据库以获取决定如何实现其目标所需的事实。数据库中特别突出的是关于动作效果的事实。研究得最多的例子是关于机器人试图将物体从一个位置移动到另一个位置的效果的事实集。这在 20 世纪 60 年代导致了情境演算(situation calculus) [12]〔译注6〕,旨在提供一种独立于问题表达动作后果的方法。

情境演算的基本形式是

$$s' = result(e, s),$$

它断言 $s'$ 是在情境 $s$ 中发生事件 $e$ 时产生的情境。以下是一些用于移动和粉刷积木的情境演算公理。

**受限动作结果公理 (Qualified Result-of-Action Axioms)**
$$\forall x l s. clear(top(x), s) \land clear(l, s) \land \neg tooheavy(x) \supset loc(x, result(move(x, l), s)) = l.$$
$$\forall x c s. color(x, result(paint(x, c), s)) = c.$$

**框架公理 (Frame Axioms)**
$$\forall x y l s. color(y, result(move(x, l), s)) = color(y, s).$$
$$\forall x y l s. y \neq x \supset loc(y, result(move(x, l), s)) = loc(y, s).$$
$$\forall x y c s. loc(x, result(paint(y, c), s)) = loc(x, s).$$
$$\forall x y c s. y \neq x \supset color(x, result(paint(y, c), s)) = color(x, s).$$

请注意,执行动作的所有限制在前提中都是显式的,并且显式包含了关于动作执行时不发生变化的陈述(称为框架公理)。如果没有这些陈述,就不可能推断出关于 $result(e2, result(e1, s))$ 的太多信息,因为我们不知道在 $result(e1, s)$ 中是否满足了事件 $e2$ 产生预期结果的前提。

进一步注意,情境演算仅适用于对离散事件进行推理是合理的情况,每个事件都会产生一个新的总情境。连续事件和并发事件不包括在内。

不幸的是,即使对于满足其限制的问题,按提议的方式使用情境演算也不是很可行。首先,使用通用定理证明器使程序运行太慢,因为 1969 年的定理证明器 [9] 无法控制搜索。这导致了 STRIPS [6],它将逻辑的使用减少到情境内的推理。不幸的是,STRIPS 的形式化比完整的情境演算要特殊得多。公理中包含的事实必须精心选择,以避免由于未能删除在动作产生的情境中不再为真的句子而产生矛盾。

## 非单调性

情境演算公理的第二个问题是它们仍然不够通用。这就是资格问题(qualification problem)〔译注7〕,直到 20 世纪 70 年代后期才发现一种可能的解决方法。考虑在常识数据库中放入一条断言鸟会飞的公理。显然,这条公理必须以某种方式加以限制,因为企鹅、死鸟和脚被浇筑在混凝土里的鸟不会飞。公理的仔细构建可能成功地包括企鹅和死鸟的例外,但显然我们可以随心所欲地想出尽可能多的额外例外,比如脚被浇筑在混凝土里的鸟。形式化非单调推理(见 [4]、[15]-[17] 和 [23])提供了一种形式化的方法来表示鸟除非有异常情况否则会飞,并推论仅考虑其存在遵循所考虑事实的异常情况。

非单调性大大增加了在情境演算中表达关于事件效果的通用知识的可能性。它还提供了一种解决框架问题(frame problem)〔译注8〕的方法,这是 [12] 中已经指出的通用性的另一个障碍。框架问题(这个术语有多种用法,但我最先使用它)发生在有多个可用动作时,每个动作都会改变情境的某些特征。某种程度上必须说明一个动作仅改变它直接涉及的情境特征。当有一组固定的动作和特征时,可以显式说明哪些特征不受动作影响,尽管这可能需要很多公理。然而,如果我们想象数据库中可能会增加情境的额外特征和额外动作,我们就面临动作公理化永远无法完成的问题。McCarthy [16] 指出了如何使用限定推理(circumscription)〔译注9〕来处理这个问题,但 Lifschitz [10] 表明限定推理需要改进并为此提出了建议。

以下是一些取自 [16] 的使用限定推理移动和粉刷积木的情境演算公理。

**关于位置和移动物体效果的公理**
$$\forall x e s. \neg ab(aspect1(x, e, s)) \supset loc(x, result(e, s)) = loc(x, s).$$
$$\forall x l s. ab(aspect1(x, move(x, l), s)).$$
$$\forall x l s. \neg ab(aspect3(x, l, s)) \supset loc(x, result(move(x, l), s)) = l.$$

**关于颜色和粉刷的公理**
$$\forall x e s. \neg ab(aspect2(x, e, s)) \supset color(x, result(e, s)) = color(x, s).$$
$$\forall x c s. ab(aspect2(x, paint(x, c), s)).$$
$$\forall x c s. \neg ab(aspect4(x, c, s)) \supset color(x, result(paint(x, c), s)) = c.$$

这处理了资格问题,因为以后可以添加任何可以想象的阻止移动或粉刷的条件,并断言其暗示相应的 $ab aspect \dots$。它处理了框架问题,因为我们不必说明移动不影响颜色,粉刷不影响位置。

即使有了形式化的非单调推理,通用常识数据库似乎仍然难以捉摸。问题在于编写满足我们关于纳入现象通用事实概念的公理。每当我们初步确定一些公理时,我们都能想到它们不适用的情况,从而需要泛化。此外,想到的困难往往是临时凑合的(ad hoc),比如脚被浇筑在混凝土里的鸟。

## 具象化

对知识、信念或目标的推理需要扩展所推理对象的域。例如,一个对目标进行反向链接的程序直接将它们用作句子: $on(Block1, Block2)$;也就是说,符号 $on$ 被用作语言的谓词常量。然而,一个想要直接说明 $on(Block1, Block2)$ 应该推迟到 $on(Block2, Block3)$ 实现之后再进行的程序需要一个像 $precedes(on(Block2, Block3), on(Block1, Block2))$ 这样的句子,如果这是一阶逻辑的句子,那么符号 $on$ 必须被视为函数符号,而 $on(Block1, Block2)$ 被视为一阶语言中的对象。

这种从句子和其他实体中制造对象的过程称为具象化(reification)〔译注10〕。它对于表达能力是必要的,但同样会导致推理的复杂化。这在 [13] 中有讨论。

## 语境概念的形式化

每当我们编写一条公理时,批评者都可以说该公理仅在特定语境(context)中为真。只要稍加巧妙,批评者通常可以设计出一个更通用的语境,在该语境中公理的精确形式并不成立。观察语言所反映的人类推理强调了这一点。考虑将“在……上”公理化,以便从句子“书在桌子上”所表达的信息中得出适当的结论。批评者可能会提议对“在……上”的精确含义进行争论,发明关于书和桌子之间可以有什么,或者航天器中必须有多少重力才能使用“在……上”这个词,以及离心力是否算数的困难。因此,我们遇到了关于概念在完全通用性下意味着什么的苏格拉底式谜题,并遇到了生活中从未出现的反例。根本不存在一个最通用的语境。

相反,如果我们以相当高的通用性水平进行公理化,公理往往比特殊情况下方便使用的公理更长。因此,人类发现说“书在桌子上”很有用,省略了对时间和书及桌子的精确识别。无论通用常识知识是用逻辑、程序还是其他形式化方法表达,这种关于通用程度的问题都会出现。(有些人提议知识在内部仅以例子的形式表达,但使用类比和相似性的强大机制允许它们更通用的使用。我祝愿他们在制定关于这些机制是什么的精确提议方面好运。)

一种可能的出路涉及将语境概念形式化,并将其与非单调推理的限定推理方法相结合。我们在公理的函数和谓词中添加一个语境参数。每条公理都对某个语境做出断言。进一步的公理告诉我们,除非断言了例外,否则事实由更受限的语境继承。每个断言也被非单调地假设适用于任何特定的更通用语境,但同样存在例外。例如,关于鸟飞行的规则隐含地假设存在可以飞行的空气。在更通用的语境中,这可能不被假设。仍需确定向更通用语境的继承与向更具体语境的继承有何不同。

假设每当计算机内存中出现句子 $p$ 时,我们将其视为处于特定语境中,并作为句子 $holds(p, C)$ 的缩写,其中 $C$ 是语境的名称。有些语境非常具体,因此华生在福尔摩斯故事的语境中是一名医生,而在一部关于心理学史的悲剧歌剧中是一名男中音心理学家。

存在一种关系 $c1 \le c2$,表示语境 $c2$ 比语境 $c1$ 更通用。我们允许像 $holds(c1 \le c2, c0)$ 这样的句子,以便即使是涉及语境的陈述也可以有语境。该理论不会提供任何“最通用语境”,就像策梅洛-弗兰克尔集合论不提供最通用集合一样。

使用语境的逻辑系统可能提供进入和离开语境的操作,产生我们可能称之为超自然演绎(ultranatural deduction)的东西,允许如下推理序列:

```
holds(p, C)
ENTER C
p
.
.
q
LEAVE C
holds(q, C).
```

这类似于通常的逻辑自然演绎系统,但由于超出本演讲范围的原因,将语境视为等同于假设集(甚至不是无限假设集)可能是不正确的。

所有这些都模糊得令人不快,但比起 1971 年能说的要多得多。

## 参考文献

1. Black, F. A deductive question answering system. Ph.D. dissertation, Harvard Univ., Cambridge, Mass., 1964.
2. Buchanan, B. G., and Shortliffe, E. H., Eds. *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*. American Elsevier, New York, 1984.
3. Davis, R., Buchanan, B., and Shortliffe, E. Production rules as a representation for a knowledge-based consultation program. *Artif. Intell.* 8, 1 (Feb. 1977).
4. Doyle, J. Truth maintenance systems for problem solving. In *Proceedings of the 5th International Joint Conference on Artificial Intelligence*. 1977, p. 247.
5. Ernst, G. W., and Newell, A. *GPS: A Case Study in Generality and Problem Solving*. Academic Press, Orlando, Fla., 1969.
6. Fikes, R. and Nilsson, N. STRIPS: A new approach to the application of theorem proving to problem solving. *Artif. Intell.* 2, 3, 4 (Jan. 1971), 189–208.
7. Friedberg, R. M. A learning machine. *IBM J. Res.* 2, 1 (Jan. 1958), 2–13.
8. Friedberg, R. M., Dunham, B., and North, J. H. A learning machine, p. II. *IBM J. Res.* 3, 3 (July, 1959), 282–287.
9. Green, C. Theorem-proving by resolution as a basis for question answering systems. In *Machine Intelligence 4*, B. Meltzer and D. Michie, Eds. University of Edinburgh Press, Edinburgh, 1969, pp. 183–205.
10. Lifschitz, V. Computing circumscription. In *Proceedings of the 9th International Joint Conference on Artificial Intelligence*, vol. 1, 1985, pp. 121–127.
11. McCarthy, J. Programs with common sense. In *Proceedings of the Teddington Conference on the Mechanization of Thought Processes*. Her Majesty's Stationery Office, London. Reprinted in *Semantic Information Processing*, M. Minsky, Ed. M.I.T. Press, Cambridge, Mass., 1960.
12. McCarthy, J., and Hayes, P. J. Some philosophical problems from the standpoint of artificial intelligence. In *Machine Intelligence 4*, D. Michie, Ed. American Elsevier, New York, N.Y., 1969.
13. McCarthy, J. First order theories of individual concepts and propositions. In *Machine Intelligence 9*, D. Michie, Ed. University of Edinburgh Press, Edinburgh, 1979.
14. McCarthy, J. Some expert systems need common sense. In *Computer Culture: The Scientific, Intellectual and Social Impact of the Computer*, vol. 426, Pagels, Ed. Annals of the New York Academy of Sciences, New York, 1983.
15. McCarthy, J. Circumscription—A form of non-monotonic reasoning. *Artif. Intell.* 13, 1, 2 (Apr. 1980).
16. McCarthy, J. Applications of circumscription to formalizing common sense knowledge. *Artif. Intell.* (Apr. 1986).
17. McDermott, D., and Doyle, J. Non-monotonic logic I. *Artif. Intell.* 13, 1, 2 (1980), 41–72.
18. Newell, A., Shaw, J. C., and Simon, H. A. Preliminary description of general problem solving program—I (GPS-I). CIP Working Paper 7, Carnegie-Mellon Univ., Dec. 1957.
19. Newell, A., Shaw, J. C., and Simon, H. A. Report on a general problem-solving program for a computer. In *Information Processing: Proceedings of the International Conference on Information Processing (Paris)*. UNESCO, 1960, pp. 256–264. (RAND P-1584, and reprinted in *Computers and Automation*, July 1959.)
20. Newell, A., Shaw, J. C., and Simon, H. A. A variety of intelligent learning in a General Problem Solver. In M. C. Yovits and S. Cameron, Eds. *Self-Organizing Systems*, Pergamon Press, Elmsford, N.Y., 1960, pp. 153–189.
21. Newell, A., and Simon, H. A. *Human Problem Solving*. Prentice-Hall, Englewood Cliffs, N.J., 1972.
22. Laird, J. E., Newell, A., and Rosenbloom, P. S. Soar: An architecture for general intelligence. To be published.
23. Reiter, R. A logic for default reasoning. *Artif. Intell.* 13, 1, 2 (Apr. 1980).
24. Simon, H. Still unsubstantiated rumor, 1960.

作者当时地址: John McCarthy, Department of Computer Science, Stanford University, Stanford, CA 94305-2095.

---

## 译注

**文本与翻译说明**

1. 〔译注1〕 **约翰·麦卡锡 (John McCarthy)**:1971 年图灵奖得主,被誉为“人工智能之父”之一。他于 1955 年共同发起了达特茅斯会议(Dartmouth Conference),并在会议提案中首次提出了“人工智能”(Artificial Intelligence)这一术语。他是 LISP 语言的发明者,也是分时系统(time-sharing)和建议获取者(Advice Taker)构想的提出者。麦卡锡于 1971 年获得图灵奖,但当时并未提交演讲文稿。本文是他为 1987 年出版的图灵奖二十周年纪念集《图灵奖演讲集:前二十年》(*ACM Turing Award Lectures: The First Twenty Years*)撰写的总结与回顾。

**背景与文化注**(译者补注,原文无)

2. 〔译注2〕 **常识知识 (Common sense knowledge)**:在 AI 领域,指人类日常生活中习以为常、无需显式学习即可掌握的基础知识(如“物体松手会下落”、“水是湿的”)。麦卡锡是“常识推理”研究的先驱,他认为 AI 的核心挑战在于如何让机器具备这种常识。
3. 〔译注3〕 **GPS (General Problem Solver, 通用问题求解器)**:由 Newell、Shaw 和 Simon 于 1957 年开发的程序,旨在模拟人类解决问题的通用策略(如手段-目的分析)。它是 AI 史上第一个尝试将问题求解方法与具体领域知识分离的系统。
4. 〔译注4〕 **产生式系统 (Production Systems)**:一种基于规则的知识表示模型,通常由一组“如果-那么”(IF-THEN)规则、一个事实库和一个推理机组成。它是早期专家系统的核心技术。
5. 〔译注5〕 **LISP**:麦卡锡于 1958 年发明的编程语言,是 AI 研究中最古老且影响最深远的语言之一。它引入了许多现代编程语言的特性,如递归、高阶函数、垃圾回收等。
6. 〔译注6〕 **情境演算 (Situation calculus)**:麦卡锡和 Hayes 于 1969 年提出的一种逻辑形式化方法,用于描述动作及其对世界状态(情境)的影响。它是 AI 规划和知识表示的基础工具。
7. 〔译注7〕 **资格问题 (Qualification problem)**:指在描述一个动作的效果时,几乎不可能列举出所有可能导致动作失败的前提条件(如“启动汽车”的前提不仅是有钥匙、有油,还包括电池没坏、排气管没被堵住等)。
8. 〔译注8〕 **框架问题 (Frame problem)**:指在逻辑系统中,如何简洁地表达动作发生后**哪些事实保持不变**。麦卡锡于 1969 年首次明确提出这一问题,它成为 AI 知识表示领域最著名的难题之一。
9. 〔译注9〕 **限定推理 (Circumscription)**:麦卡锡提出的一种非单调推理形式,通过限制谓词的扩展(即假设除了已知的事实外,没有其他异常情况)来解决资格问题和框架问题。
10. 〔译注10〕 **具象化 (Reification)**:在逻辑中,指将原本属于语言层面的实体(如谓词、句子)当作领域中的对象来处理,从而允许对这些实体本身进行推理。
11. **建议获取者 (Advice Taker)**:麦卡锡在 1958 年提出的一个构想,即一个能够通过接受逻辑语句形式的“建议”来学习和改进其行为的程序。这是逻辑 AI 进路的开端。

**OCR 与印刷勘误**

12. 扫描件中逻辑公式中的符号(如 $\forall$, $\supset$, $\neg$)在 OCR 提取时多有遗漏或误识,本译文均对照原刊页面图像逐一还原。
13. 参考文献 24 中 "Still unsubstantiated rumor" 疑为麦卡锡对 Simon 某次未发表言论的幽默引用。
