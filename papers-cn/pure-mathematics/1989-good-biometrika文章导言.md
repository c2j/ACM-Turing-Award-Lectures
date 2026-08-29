# 为《Biometrika》第66卷（1979）所载文章作的导言

**Introductory Remarks for the Article in Biometrika 66 (1979), "A. M. Turing's Statistical Work in World War II"**

> 作者：I. J. 古德（I. J. Good）〔译注1〕
> 原载：专为本卷（*Collected Works of A.M. Turing: Pure Mathematics*，North-Holland，1992）撰写，书页 211–224；撰于 1989 年〔译注2〕
> 译自 `papers/Pure Mathematics. 2-North Holland $1992$.pdf` 第 233–246 页（个人学习用途）

## (i)

要在历史视角下相当充分地评估图灵在第二次世界大战期间、与谜机（Enigma）密码分析相关的统计思想，就有必要了解一些背景，以及他的这些思想后来的若干发展。给出全部细节太占篇幅，所以我将大量使用征引。

图灵不曾发表这些战时统计思想，因为战后他忙于在计算机科学与人工智能的最底层创业。我被他的统计思想对其他应用的重要性所打动，把它们当中的一些发展起来并在不同场合发表。我的拖延多半缘于战时的态度：一切都属机密——从霍勒里斯卡片，到序贯统计，到经验贝叶斯，到马尔可夫链，到决策理论，到电子计算机。这种极端的保密标准在战后才逐渐松动。

我将以关于谜机的几点评论作为这篇导言的开头。

## (ii)

谜机是一台密码编制机（而非密码分析机），用于对 26 个字母的字母表上的报文加密。要加密一个字母，你在 26 键键盘上按下一个键，密文字母由一只点亮的小灯泡指示出来。这样的灯泡有 26 只，它们的几何排列也构成一个键盘。机器内含若干内部永久接线的轮子，通常是三个；每次加密一个字母，其中至少一只前进一格——实际上"右手边"那只每步都进一格，其余的只是偶尔进位，颇像里程计。由于轮子的运动，机器的状态在一份报文的加密过程中不断变化。对机器的任何一个给定状态，它实现的是一个简单代换；所以倘若轮子不动，这台机器将毫无安全性可言。若在机器的某个给定状态下，字母甲加密为乙，则在同一状态下乙亦加密为甲。〔译注3〕这一互反性质给机器的合法用户带来方便，因为它意味着解密与加密用的是同一套手续，从而减少加密与"合法"解密的差错机会；但这性质对密码分析家同样有用。关于谜机更完整的描述，例如见 Rejewski (1981)。

谜机在二战之前已被多家商业机构使用。出于一个奇怪的巧合，我最早是在 1941 年听说这件事的，说话人是一位退休银行家，名叫伯伯里（Burbury），战时他常坐在比格利附近一家旅馆里我的餐桌旁——我当时临时驻扎在那里。他没有用"Enigma"这个名字。（这位伯伯里是 S. H. Burbury 的侄子——后者即"伯伯里—玻尔兹曼分子无序"假说的那位 Burbury：见 Brush (1983, pp. 89, 92)。）德军于 1929 年采用了谜机的一个更安全的版本（Garliński 1979, p. 12）。当然，那些轮子（转子）的接线已不同于商用型号。更多的安全性来自加装的一块插接板（plugboard，或称 steckerboard），插接线定期更换（至少到 1941 年，海军用法是每天一换）。任何给定插接的效果是定义一个简单代换，它既作用于进入轮组的明文字母，也作用于从轮组出来、尚未成为密文的字母。插接板的设计使字母得以两两配对：例如若 Q 被插接（steckered）到 X，则 X 也被插接到 Q。于是插接板的简单代换是互反（幂等）的，并不破坏谜机本身的互反性质。

对"本土水域"（Home Waters）通信（区别于地中海通信），操作员先从一本叫 Kennbuch 的表中选出一个三元组，比如说 XQV，作为系统识别符（discriminator）。接着他把三个轮子拨到位置 \(G_1 G_2 G_3\)——称为 Grundstellung，属于每日密钥的一部分；然后在这个轮子初始位置上，把他自己选定的一组 \(M_1 M_2 M_3\)（真实报文所用设置）加密，得到比如 LRP。随后，XQV 与 LRP 这六个字母经下述手续进一步加密——这道手续不使用谜机（所以为避免混淆，我在这里用"encrypted"一词而不是"enciphered"）：先把六个字母错行叠写如 (a)；再随手挑两个字母填满一个二乘四矩形如 (b)；然后借助一本秘密印制的双字表把四个纵向双字 XL、QL、VR 与 AP 加密，得比如 (c)；最后 PTOW XUBN 就是加密报文的开头两组，即所谓指示组（indicator groups）。双字表共有十本，用哪一本也是每日密钥的一部分。

| (a) | (b) | (c) |
|:---:|:---:|:---:|
| XL | XQVA | PTOW |
| LRP | LLRP | XUBN |

每本双字表都是互反的；例如若 XL 变成 PX，则 PX 也会变成 XL。这对加密者与密码分析家又都有帮助。

地中海通信的指示系统与 Rejewski (1981, p. 217) 所描述的那一套大体相同。

战争进行到一定阶段时，我们已能根据此前破解每日密钥的成功，部分地重构出双字表。在一次夜班里我发现：利用那两个哑字母的"人为随机"选择，凭大约三十份报文，就能用分班打分识别出当时用的是哪本双字表。

对德军使用谜机的最早一次密码分析突破，是三位波兰数学家取得的，尤其是雷耶夫斯基（Rejewski）1932 或 1933 年的辉煌工作。对他们事迹的描述见 Rejewski (1981)。在这一成功之时，谜机有三个轮子，可以按六种可能顺序中的任一种装入，轮序一次固定三个月。（每种轮序有 \(26^3\) 种可能的轮子位置。）波兰人的破译工作得到了法国特工机构古斯塔夫·贝特朗（Gustave Bertrand）所供"情报"材料的极大帮助。Rejewski (1981, p. 221) 说这份情报是"破解机器秘密的决定性因素"。贝特朗是从德国密码机关成员汉斯-蒂洛·施密特（Hans-Thilo Schmidt，代号 Asche）手里买来的。卡恩（Kahn 1983）称汉斯-蒂洛是"对第二次世界大战影响最大的间谍"。汉斯-蒂洛因其对人类的服务于 1943 年被纳粹枪决。出卖他的是法国特工机构的 R. S. 莱穆瓦纳（Lemoine），此人是为了保住自己的性命（Kahn 1983, pp. 76–88）。汉斯-蒂洛的兄弟是鲁道夫·施密特（Rudolf Schmidt），一位高级将领；哥哥被出卖后，他被希特勒降职。看来希特勒大概怀疑"帮助文明"是一种家族特征。〔译注4〕

1938 年 9 月与 12 月（据 Calvocoressi 1980, p. 38），德国人引入了两项变更，其一是把轮库里的轮子从三个增加到五个。于是轮序可能有 \(5 \times 4 \times 3 = 60\) 种。为单份报文指示轮子设置的方法也改了。大约同时，不被插接的字母（自插字母，self-steckers）的数目从 12 减到 6。可能的插接数目现在是 \(26!/(10!\,6!\,2^{10}) = 1.51 \times 10^{14}\)，比没有自插字母时还要大。波兰人查明做出了哪些变更，并查出了两只新轮子的接线；但他们没有设施按日常规应对这些变更，于是决定把自己的一切方法与成果交给英国人和法国人。他们设法在 1939 年 7 月下旬完成了移交，距波兰沦陷只有几个星期。倘若德国人把这次安全升级推迟一些，波兰人的这份礼物也许就来不及送出了！

## (iii)

我于 1941 年 5 月 27 日到达布莱奇利镇上的政府代码与密码学校（正是俾斯麦号被击沉的那一天），其时图灵正主管海军谜机的密码分析。当时它的轮库里已有八只接线为已知的轮子，因而有 \(8 \times 7 \times 6 = 336\) 种可能的轮序。轮序每两天一换。进攻方法之一是鲁日茨基（Różycki）的"时钟法"（Rejewski 1981, p. 223; Good 1981），图灵用像样的概率方法对它作了改进。（他的一个想法涉及再生马尔可夫链，由 Good 1973 esp. p. 936 加以发展。）精加工后的时钟法就叫 Banburismus，后附文章的第 4 节提到过它。我写那篇文章时并不知道波兰人也用过时钟法。Banburismus 这种博弈要把大量概率信息碎片拼合起来，有点像 DNA 序列的重构。在十来个玩手里玩得最好的是休·亚历山大（Hugh Alexander），英国国际象棋冠军；图灵转去搞语音保密之后，他接任了海军谜机处处长。

"需要知道"（need to know）的保密原则在布莱切利执行得相当严格，但有一次好奇心占了上风，我问图灵："我们究竟是怎么弄清轮子接线的？"——尽管我的 Banburismus 工作并不需要这个知识。（应当记住：密码编制者总得假定一台密码机的永久性特征已为密码分析者所知；例如，〔此处扫描佚失一行，大意谓：我们并非依靠缴获整机才得知接线〕。）那是我多年来头一次也是唯一一次对波兰人的贡献略知一二，直到战后许多年才再有耳闻。

要是没有强有力的密码分析机器，我们要持续读取海军谜机是根本不现实的。用于这一目的的主要机器叫作炸弹机（Bombe），它也被用于其他一切谜机通信。它是波兰人所发明的一台密码分析机器的大幅改进型。它是电磁式而非电子式的，不要与电子计算机器"巨人"（Colossus）混淆。关于巨人的资料，例如见 Randell (1980) 与 Good (1980)。巨人与现代电子计算机的共同点要多得多。它被用来对付一种德国电传打字密码机，我们管它叫"鱼"（Fish；Sägefisch、Geheimschreiber、Schlüsselzusatz、SZ40、SZ42，洛伦兹公司造）。鱼有各种链路或"种"，如金枪鱼（Tunny）、鲷鱼（Bream）与水母（Jellyfish）。鱼与谜机全然不同，用于级别更高的通信（Hinsley 1984, Vol. 3, Part 1, pp. 477–482；他说，就影响的重要性而言，破译水母是该学校 1944 年最重要的密码分析成就）。巨人并不用来对付谜机——尽管 Rejewski (1981) 倒数第二段给人的印象与此相反。图灵对鱼的破译有过早期贡献；但我相信，除了正确建议由邮局多利斯希尔研究所的托马斯·H. 弗劳尔斯（Thomas H. Flowers）领衔工程之外，他并未直接参与巨人的设计。巨人建成后图灵也不是它的用户。但他对炸弹机设计的影响很大，这也许是他对谜机密码分析最重要的贡献。

1942 年 2 月，U 潜艇开始使用四轮谜机；此后直到那年 12 月 13 日，我们再没有读过 U 艇报文。从那天起我们又能读 U 艇报文了（Hinsley 1981, Vol. 2, p. 548）。据 Calvocoressi (1980, pp. 104, 126)，图灵在新一轮突破中起了主要作用，但实际上图灵并没有参与那次行动。这消息是我最近从肖恩·威利（Shaun Wylie）那里得到的：他在 8 号棚一直待到 1943 年 9 月，而我那年六七月间调离。我们俩都被调到 M. H. A. 纽曼的部门去搞鱼。

关于 U 艇通信的更多细节见 Hinsley (1981, Vol. 2, pp. 547–572 与 pp. 747–752)。读取 U 艇通信的价值打了折扣，因为在直到 1943 年 6 月的多数时间里，德国海军密码分析处（B-Dienst）一直在读英国海军第 3 号密码——B-Dienst 称之为护航队密码。当双方的密码分析者都有战果时，大西洋之战在某种程度上就像下棋而不是克里格暗棋（Kriegspiel）。只不过哪一方都不知道对方知道多少。

图灵的炸弹机构想，是把"从逻辑矛盾可以推出一切命题，无论真假"这条原理加以改造——维特根斯坦在与图灵的争论中认为这条原理无足轻重（Hodges 1983, p. 154）。也许图灵有这个想法的原因之一，是要回溯性地赢下与维特根斯坦的那场争论；不过这只是趣谈。改造之处在于：在适当的语境下，从一个错误假设出发，可以很有希望地推出大量互相矛盾的后果。这一想法使炸弹机的运行时间缩短到原来的二十六分之一。话剧《破解密码》〔Breaking the Code〕提到了这一事实；该剧讲的是图灵的一生，根据霍奇斯的书改编。图灵的这个想法帮助打赢了战争；但若有现代电子学可用，它本是多余的。〔译注5〕

"对角线板"（diagonal board）大大提高了炸弹机的效率。这件利用谜机及其插接板互反性质的装置是韦尔什曼提议的，见 Welchman (1982)。

关于谜机以及密码分析对战事影响的更多信息，见参考文献所列另一些书。我相信刘温（Lewin 1978）在中等篇幅的书里给出了最准确的叙述之一。卡恩（Kahn 1983, p. 218）在一篇 1979 年发表的书评的重印本里说："迈克尔·霍华德——牛津大学奇切利战争史教授——说得对：这是自切斯特·威尔莫特写《欧洲的争夺战》以来四分之一世纪里出现的关于第二次世界大战的最重要著作。"（不过刘温把我的地址写成西弗吉尼亚大学，那是错的。）

## (iv)

重印自《Biometrika》的后附文章中所描述的观念，多数是图灵围绕 Banburismus 发明、发现或再发现的。（请先读该文第 2、3、4 节，再来读这篇导言的其余部分。）

从数学观点看，贝叶斯因子的概念只是拉普拉斯与泊松早已熟悉的观念的一个小小变形；可是与几率、对数几率、证据权重这套术语结合起来，它对未经训练的直觉的吸引力是直接的。贝叶斯因子的想法可以很容易地讲给街头的普通人听。

图灵给证据权重起的名称是"分班总量"（decibannage）或"得分"（score）。

在后附文章里我提到 C. S. 皮尔士于 1878 年曾在技术意义上使用"证据权重"一词。那只出现在一则短评里；细读皮尔士那篇写得晦涩的文章可知，他处理的是假设 H 的先验概率等于 1/2 的特殊情形。更完整的解释见我对巴纳德的回应，载 Good (1988)。

图灵没有为证据权重设计记号，虽然他有一次说过：数学之需要好记号，甚于需要新定理。他的意思大概是：任何已证的定理迟早会被别人发现，而坏的记号（如同坏的术语）却容易盘根错节地固化下来。无论如何，我把图灵这话记在心里，并在 Good (1960 A, B, C)——或许更早——引入了记号 \(W(H : E)\) 与 \(W(H : E | G)\)，连同那条几乎自明的可加性质：

$$W(H : E \,\&\, F) = W(H : E) + W(H : F | E),$$

其中 \(W(H : E|G)\) 表示"一路假定 G（给定 G）之下，E 提供的关于 H 的证据权重"。〔译注6〕

成功地运用证据权重对付谜机，以及那不起眼的分班、加倍不起眼的半分班帮着把"一号刑事疯子"从世界上清除掉，使我对这个题目有些着迷，一再回到它上面，如狗转身吃回自己所吐的（《箴言》26:11）。（见 Good 1983 A 两部索引中的 "Weight of evidence" 条目。）我完全相信这个技术性概念〔此处佚失数字，大意谓：是根本性的〕，而且它也在同一意义上被明斯基与塞尔弗里奇（Minsky & Selfridge, 1961）独立提出过。这一概念在医学、法律与统计学中都居于逻辑上的基础地位（例如 Good & Card 1971；Spiegelhalter & Knill-Jones 1984；Good 1986；Bernstein et al. 1989）。这个概念可以由自然的期望性质（desiderata）唯一地导出，曾以种种方式、并且越来越简单地被证明：Good (1968, 附录 A; 1984; 1989 A, B)。但要让哲学家们听进去是一场艰难的爬坡战。这里给出最简单的证明。它基于假设：\(W(H : E)\) 只依赖于 \(x = P(E|H)\) 与 \(y = P(E|\bar{H})\)，比如说 \(W(H : E) = f(x, y)\)。（背景信息视为当然，不在记号中写出。）设 F 与 H、E 无关。那么必须有 \(W(H : E \,\&\, F) = W(H : E)\)。于是对一切 λ 有 \(f(\lambda x, \lambda y) = f(x, y)\)，故 \(f(x, y)\) 是 \(x/y\) 的函数。我们必须取对数，才能为"权重"一词辩护。证毕。

我猜想理论科学家、医生、治安法官与侦探可以训练出这样的本领：对贝叶斯因子或证据权重作出有用的主观估计；但据我所知，检验这一猜想的细致实验还没有做过。也许会发现有些人惯于高估、有些人惯于低估证据权重，而且一厢情愿当然也会影响判断。（比较 Good & Card 1971, p. 187。）也许亚历山大在 Banburismus 上的本事，部分由于他有异乎寻常客观的判断力，外加出众的精力、决心与智力。

更一般地说，运用主观概率论时所使用的判断，不必限于对单个概率的（不等式）判断（Good 1983 A, p. 76）。可以对概率的比值（以及比值之间的不等式）作判断，包括贝叶斯因子、几率、证据权重、效用、效用比、期望效用与"因果倾向"（下文提及）。

在两个假设之间作判别时，由于证据权重具有可加性，很自然把它看作一种"准效用"。于是当真实的期望效用不便估计时，可以拿期望证据权重量顶替期望效用。（唐纳德·米基指出，这好比一个眼下赚不到钱的投资人，却获得了日后可能派上用场的知识。）期望证据权重有许多名字，其一为交叉熵。熵与交叉熵的应用多得不计其数。欲知其中一些，以及对 E. T. Jaynes、H. Jeffreys、S. Kullback、D. V. Lindley、J. Rothstein、S. Watanabe 等人的征引，见 Good (1983 A) 的索引。

《Biometrika》文章第 7 节那条关于正态分布证据权重之方差的定理表明，它的散布宽得出人意料。如前所述，这结果应用于雷达时是"令人不安"的；但用"骇人"来形容或许更为贴切。

《Biometrika》文章第 8 节里图灵那条听来惊人的小定理——不利于真假设的贝叶斯因子的期望为 1（在第 74 页作了推广）——一经点破，证明便是平凡的。一个简单推论是：如果借助某个实验有可能削弱一个假设，那么也有可能从同一实验获得有利于它的证据。这个几乎自明的命题（不经那条小定理也能轻易证明）有时被哲学家与统计学家默认否认，他们说：你能反驳一个理论或零假设，却不能支持它。对贝叶斯派而言，清楚的是：常常有可能得到巨大的证据权重，反对一个即使嵌在复合假设之中的简单假设〔此处佚失一行，按文意补足〕；而当它为真时，却往往难以获得多少支持。

证据权重的术语与记号，对于用概率定义"一个事件 F 致使较晚事件 E 发生的倾向"这一哲学问题颇有启发。（这与 F 实际上造成 E 的程度完全是两回事。）凡是熟悉证据权重概念的人，脑中可能立刻蹦出四个候选定义：\(W(E : F | U)\)、\(W(\bar{F} : E | U)\)、\(W(E : \bar{F} | U)\) 与 \(W(F : E | U)\)，其中横线表示否定，U 表示 F 发生前夕宇宙的状态。（有人可能会忘记提到 U。）其中前三个可以容易地排除掉（Good 1988），剩下的是"F 不发生时反对 F 的证据权重"——这是一个有待解释项（explicandum），最早经由依赖因果网络的论证达到（Good 1961/1962）。例如，在 F 是 E 的充分原因的极端情形下，该倾向为无穷，因为那时 \(P(E|F \cdot U)/P(E|\bar{F} \cdot U) = \infty\)，除非无论 F 是否发生、E 都几乎必然（在那种情况下，"F 是 E 的充分原因"这个前提就好比假设吃爆米花会使太阳明天升起一样）。〔译注7〕

在我的可释性（explicativity）即解释力的工作（Good 1977）中，我又发觉用记号 \(W(H : E | F)\) 很方便。关于证据权重的更多文献见 Good (1983 A) 的两个索引；一篇综述（有待更新）见 Good (1983 B)。

## (v)

经验贝叶斯方法可以分为参数法（相当明显）与非参数法（精巧）。图灵在一个有趣的特殊情形中预示了非参数经验贝叶斯思想，但他并不总是因此获得应有的声誉。（又见 von Mises 1942。）这项工作在《Biometrika》文章的第 11 节提到。那里给出的公式几乎等价于罗宾斯（Robbins 1956）的公式 (19)。让我着迷的是哲学层面的：可以在只对先验作弱的定性假设的情况下使用贝叶斯论证。罗宾斯无疑是这个领域的先驱之一，尽管基本想法此前已被预示。

由图灵的工作得出的下面这条简单推论很有意思（Good 1953, 1969）：下一个抽到的"动物"（或词）属于一个新"种"（或是新词）的概率，当 \(n_1 > 20\) 时接近 \(n_1/N\)。换句话说，已有的 N 个动物（或词）样本的覆盖约为 \(1 - n_1/N\)。未来样本期望覆盖的估计也有意思，见 Good & Toulmin (1956)。

1941 或 1942 年的某一天，我在伦敦遇见乔治·巴纳德（George A. Barnard），告诉他我们在序贯地使用贝叶斯因子及其对数，以在两个假设之间作判别；当然我没有提及应用。巴纳德说，说来也巧，供应部正把一个类似的方法用于质量控制，在批次（lots）之间而非假设之间作判别。那其实是同一个方法，因为选取一批可以看作接受一个假设。巴纳德已不记得我们的会面，我却记得清清楚楚——可能因为我当时担心这场讨论会被一些缺乏统计理论判断力的人视为泄密。倘若巴纳德那时还没有在用这个想法，我这句话可谓落到了沃土之上！序贯分析的概念及其重要应用，图灵、巴纳德与沃尔德三人都应分享荣誉。

## 补充参考文献*

BEESLY, Patrick
1977 *Very Special Intelligence* (Hamish Hamilton, London)

BENNETT, Ralph
1979 *Ultra in the West* (Charles Scribner's Sons, New York)

BERNSTEIN, L.H., I.J. GOOD, G.I. HOLTZMAN, M.L. DEATON and J. BABB
1989 Diagnosis of acute myocardial infarction from two measurements of creatine kinase isoenzyme MB with use of nonparametric probability estimation. *Clinical Chemistry (USA)* **35** (3), 444–447

BRUSH, S.G.
1983 *Statistical Physics and the Atomic Theory of Matter, from Boyle and Newton to Landau and Onsager* (Princeton Univ. Press, Princeton, NJ)

CALVOCORESSI, Peter
1980 *Top Secret Ultra* (Ballantine Books, New York)

CAVE-BROWN, A.
1975 *Bodyguard of Lies* (Harper & Row, New York)

GARLINSKI, J.
1979 *The Enigma War* (Charles Scribner's Sons, New York)

GOOD, I.J.
1960A The paradox of confirmation. *British J. Philos. Sci.* **11**, 145–149
1960B Weight of evidence, corroboration, explanatory power, information, and the utility of experiments. *J. Roy. Statist. Soc. Ser. B* **22**, 319–331
1960C Effective sampling rates for signal detection: or can the Gaussian model be salvaged? *Inform. and Control* **3**, 116–140
1961/62 A causal calculus. *British J. Philos. Sci.* **11** (1961) 305–318; **12** (1961) 43–51; **13** (1962) 88（重印于 GOOD 1983 A）
1968 Corroboration, explanation, evolving probability, simplicity, and a sharpened razor. *British J. Philos. Sci.* **19**, 123–143
1973 The joint probability generating function for run-lengths in regenerative binary Markov chains, with applications. *Ann. Statist.* **1**, 933–939
1977 Explicativity: a mathematical theory of explanation with statistical applications. *Proc. Roy. Soc. London Ser. A* **354**, 303–330（大部分重印于 GOOD 1983 A）
1980 Pioneering work on computers at Bletchley. In: N. METROPOLIS, J. HOWLETT and G.-C. ROTA (Eds.), *A History of Computing in the Twentieth Century* (Academic Press, New York) 31–45
1981 Contribution to the discussion of Rejewski (1981). *Ann. Hist. Comput.* **3**, 232–234
1983A *Good Thinking: The Foundations of Probability and its Applications* (Univ. of Minnesota Press, Minneapolis, MN)
1983B Weight of evidence: a brief survey. In: J.M. BERNARDO, M.H. DEGROOT, D.V. LINDLEY and A.F.M. SMITH (Eds.), *Bayesian Statistics 2: Proceedings of the Second Valencia International Meeting September 6/10, 1983* (North-Holland, New York, 1985) 249–269（含讨论）
1984 The best explicatum for weight of evidence. *J. Statist. Comput. Simulation* **19** (C197), 294–299; **20**, 89
1986 The whole truth. *Inst. Math. Statist. Bull.* **15**, 366–373
1988 The interface between statistics and philosophy of science. *Statist. Sci.* **3**, 386–412（含讨论）
1989A Yet another argument for the explication of weight of evidence. *J. Statist. Comput. Simulation* **31** (C312), 58–59
1989B Weight of evidence and a compelling metaprinciple. *J. Statist. Comput. Simulation* **31** (C319) 121–123

GOOD, I.J. and W.I. CARD
1971 The diagnostic process with special reference to errors. *Methods Inform. Medicine* **10**, 176–188

HINSLEY, F.H.
1979/81/84 *British Intelligence in the Second World War*, three volumes (Her Majesty's Stationary Office, London)（此为"官方"战史）

HODGES, A.
1983 *Alan Turing: the Enigma* (Burnett Books, London)

JOHNSON, Brian
1978 *The Secret War* (British Broadcasting Corporation, London) Chapter 6

KAHN, David
1983 *Kahn on Codes: Secrets of the New Cryptology* (Macmillan, New York)

KOZACZUK, W.
1984 *Enigma: how the German Machine Cipher was Broken and how it was Read by the Allies in World War Two* (Arms and Armour Press, London)

LEWIN, Ronald
1978 *Ultra Goes to War* (McGraw-Hill, New York)

MINSKY, M. and O.G. SELFRIDGE
1961 Learning in random nets. In: Colin CHERRY (Ed.), *Information Theory* (Butterworths, London) 335–347

RANDELL, Brian
1980 The Colossus. In: N. METROPOLIS, J. HOWLETT and G.-C. ROTA (Eds.), *A History of Computing in the Twentieth Century* (Academic Press, New York) 47–92

REJEWSKI, M.
1981 How Polish mathematicians deciphered the Enigma. *Ann. Hist. Comput.* **3**, 213–234（含讨论）（此系 Joan STEPENSKE 自波兰文所译；另一译文出自 C. KASPAREK，见 KOZACZUK (1984) 附录 D）

ROBBINS, H.E.
1956 An empirical Bayes approach to statistics. In: *Proceedings of the Third Berkeley Symposium Math. Statist. Probab.* **1**, 157–163

SPIEGELHALTER, D.J. and R.P. KNILL-JONES
1984 Statistical and knowledge-based approaches to clinical decision-support systems, with an application in gastroenterology. *J. Roy. Statist. Soc. Ser. A* **147**, 35–77

STEVENSON, William
1976 *A Man Called Intrepid* (Harcourt Brace Jovanovich, New York)

VON MISES, R.
1942 On the correct use of Bayes's formula. *Ann. Math. Statist.* **13**, 156–165

WELCHMAN, G.
1982 *The Hut Six Story* (McGraw-Hill, New York)

WINTERBOTHAM, F.W.
1974 *Very Special Intelligence* (Hamish Hamilton, London)

\* 《Biometrika》文章中已给出的参考文献，此处不再重复。

## 译注

### 文本与翻译说明

〔译注2〕本文系古德专为本书撰写，故原刊信息即本书版本信息（书页 211–224）；文末"补充参考文献"只收前篇《Biometrika》文章未列的条目，体例照录原文（作者—年份—题名—出版项）。

〔译注6〕正文段落编号 (i)–(v)；(ii) 中报文加密流程的示例 (a)(b)(c) 以表格照录。术语约定：discriminator＝识别符；Grundstellung＝基准位置（德文保留）；Kennbuch＝密钥簿（德文保留）；stecker/插接板＝插接；indicator groups＝指示组；digraph＝双字；wheel order＝轮序；barrier 等 1950 年论文术语不涉本篇。decibannage 音意兼译"分班总量"。

### 背景与文化注

〔译注1〕I. J. 古德生平见前篇译注1。本篇写作时（1989）他在弗吉尼亚理工统计系任大学教授（University Professor）。

〔译注8〕谜机（Enigma）：德国谢尔比乌斯（Arthur Scherbius）设计的转轮密码机，1920 年代商用，魏玛时期起为德军采用；其互反性源于反射轮（reflector），插接板进一步扩大密钥空间。波兰方面最早破解的是雷耶夫斯基（Marian Rejewski）、鲁日茨基（Jerzy Różycki）与齐加尔斯基（Henryk Zygalski）三人；1939 年 7 月波方在 Pyry 林中向英法移交成果，史称"波兰人的礼物"。汉斯-蒂洛·施密特案是战期间谍史上著名一例：法国特工莱穆瓦纳被捕后供出接头人，导致施密特被处决；其兄鲁道夫·施密特陆军上将因此失宠。卡恩（David Kahn）《卡恩论密码》中的评语即出于此。

〔译注5〕维特根斯坦与图灵 1939 年在剑桥就"数学基础"对谈，图灵是课上唯一的专业数学家；《破解密码》（Breaking the Code，休·怀特莫尔编剧，1986 年首演，后拍成电视电影）据此及霍奇斯传记写成。"一号刑事疯子"（Criminal Lunatic #1）是古德对希特勒的戏称。克里格暗棋（Kriegspiel）是看不见对方棋子的国际象棋变体——喻双方都只能凭部分信息推断对方所知。俾斯麦号于 1941 年 5 月 27 日被皇家海军击沉，古德以此记住入职日。休·亚历山大（1909–1974）两度英国国际象棋冠军，战后成为计算机先驱之一。M. H. A. 纽曼（Max Newman）是拓扑学家，战时"鱼"组组长，战后主持曼彻斯特计算机项目。汤米·弗劳尔斯为巨人机总工程师；韦尔什曼（Gordon Welchman）与对角线板见其所著《六号棚的故事》。巴纳德（George Barnard）为英国统计学家，序贯分析的独立先驱；供应部（Ministry of Supply）主管军需生产，其质量控制正需抽样验收。罗宾斯（Herbert Robbins）1956 年奠基经验贝叶斯；von Mises 1942 一文是其先声。

〔译注9〕"伯伯里—玻尔兹曼分子无序假说"：S. H. Burbury（1831–1911），英国律师出身的物理学家，与玻尔兹曼就统计力学中"分子无序"概念往复论辩（见 Brush 1983）。那位退休银行家是他的侄子——古德以此说明自己早在 1941 年就从民间渠道得知 Enigma 曾是商用机器。

〔译注10〕"街头的普通人"（the woman in the street）直译自英语习语（the man/woman in the street），意为普通路人。

### OCR 与印刷勘误

〔译注11〕除随文以〔〕标注者外：(1) (ii) 节互反性质句中两个具体字母佚失，译文以"甲／乙"代之；(2) Grundstellung 位置 OCR 作 "GG2G3"，当作 \(G_1G_2G_3\)；报文设置 OCR 作 "M,M2M"，当作 \(M_1M_2M_3\)；(3) 示例矩形左上角 OCR 作 "40x"，对照正文四个纵向双字当作 XL；(4) "\(26!/(10!6!21°)\)" 当为 \(26!/(10!\,6!\,2^{10})\)；"\(26?\) possible settings" 当为 \(26^3\)；(5) (iii) 节"密码编制者总得假定……"后一行几乎全佚，仅存句尾 "capture of an Enigma machine"，译文按文意补足并加〔〕；(6) "Rozycki" 当作 Różycki；(7) (iv) 节图灵小定理一句中部佚失（"that the ... generalized on p.74"），按 1979 年文章第 8 节补足；(8) "enormous weight of" 与 "embedded in a composite hypothesis" 之间佚失约一行，按文意补足；(9) 因果倾向四候选定义的上横线（否定号）在扫描中不可辨，横线位置无从恢复；存活定义按正文语义（"F 不发生时反对 F 的证据权重"）译出；(10) 充分原因例中分母 OCR 与分子同形，按文意改作 \(P(E|\bar{F} \cdot U)\)；(11) "I am totally convinced that the technical ... was independently proposed" 之间佚失数字，按文意补足；(12) 姓氏小型大写（如 REJEWSKI、GOON→Good）径改；(13) 第 246 页（书页 225 起）为空白隔页，本篇至此为止。
