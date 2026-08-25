# 左右概周期性的等价性

**Equivalence of Left and Right Almost Periodicity**

> 作者:艾伦·图灵(A. M. Turing)〔译注1〕
> 原载 *Journal of the London Mathematical Society*, Vol. 10(1935),pp. 284–285(本文于 1935 年 4 月 23 日收到,1935 年 4 月 25 日宣读)
> 译自 `papers/Pure Mathematics. 2-North Holland (1992).pdf` 第 23–24 页(书页 1–2)(个人学习用途)

在《群中的概周期函数》("Almost periodic functions in a group")一文中,J. v. 诺依曼†〔译注2〕曾独立地使用了左周期性与右周期性这两个概念。我将证明二者是等价的。

f(x) 是一个复值函数,其变元 x 取遍任意群 $\mathfrak{G}$。〔译注3〕若对每个 $\varepsilon > 0$,都存在 $\mathfrak{G}$ 中有限个元素 $b_1, \ldots, b_m$,使得对 $\mathfrak{G}$ 中每个 $t$,都存在一个 $\mu = \mu(t)$ 满足

$$|f(xt) - f(xb_\mu)| < \varepsilon \qquad \text{对所有 } x \in \mathfrak{G}, \tag{D}$$

则称 $f(x)$ 为**右概周期的**(right almost periodic,缩写 r.a.p.)。

把不等式 (D) 换成

$$|f(tx) - f(b_\mu x)| < \varepsilon, \tag{D$'$}$$

就得到左概周期性的定义。

设 $f(x)$ 是 r.a.p. 的。要证 $f(x)$ 是 l.a.p. 的,只需证明:对每个 $\varepsilon > 0$,存在 $\mathfrak{G}$ 中有限个元素 $c_1, \ldots, c_n$,使得对 $\mathfrak{G}$ 中每个 $s$,都存在一个 $\nu = \nu(s)$ 满足

$$|f(sb_\pi) - f(c_\nu b_\pi)| < \varepsilon \qquad \text{对每个 } \pi; \tag{K}$$

因为这时,由 $f(x)$ 的 r.a.p. 性质,

$$|f(sb_\mu) - f(st)| < \varepsilon,$$
$$|f(c_\nu b_\mu) - f(c_\nu t)| < \varepsilon,$$

其中 $\mu = \mu(t)$。在不等式 (K) 中取 $\pi = \mu(t)$,便得

$$|f(st) - f(c_\nu t)| < 3\varepsilon \qquad \text{对每个 } t,$$

即 $f(x)$ 是 l.a.p. 的。

为证元素 $c_1, \ldots, c_n$ 的存在性,我们引入一个 $m$ 个复维数的空间 $R$。考虑 $R$ 中由这样的点 $P_x$ 组成的集 $S$:其坐标为 $[\,f(xb_1), \ldots, f(xb_m)\,]$($x$ 取遍 $\mathfrak{G}$)。$f(x)$ 既是 r.a.p. 的就是有界的\*;因此 $S$ 有界,可以用有限个直径为 $\varepsilon$ 的球覆盖,每个球都含有 $S$ 的某个点。设用这种方式得到的 $S$ 中元素的有限集为 $P_{c_1}, \ldots, P_{c_n}$;那么对 $\mathfrak{G}$ 中每个 $s$,存在 $\nu = \nu(s)$ 使得 $P_s$ 与 $P_{c_\nu}$ 的距离小于 $\varepsilon$;于是,对每个 $\mu$,

$$|f(sb_\mu) - f(c_\nu b_\mu)| < \varepsilon,$$

即 $c_1, \ldots, c_n$ 具有所需的性质。

这样,$f(x)$ 是 r.a.p. 的就蕴涵 $f(x)$ 是 l.a.p. 的;反过来同理可证,或者利用逆群即可。〔译注4〕于是,v. 诺依曼的理论现在便可用来证明每个 l.a.p. 函数都有唯一的左平均值。〔译注5〕

群中 a.p. 函数的理论现在可以搬到允许群作传递变换的对象集上。〔译注6〕设 $\Omega$ 是一个允许群 $\mathfrak{G}$ 作(左)变换的对象集。用小写哥特字母表示 $\Omega$ 的元素。于是,$\Omega$ 上的函数 $f(\mathfrak{r})$ 对应于 $\mathfrak{G}$ 上的一个函数 $f(x)$,定义为 $f(x) = f(\mathfrak{r})$,只要 $x\mathfrak{t} = \mathfrak{r}$,其中 $\mathfrak{t}$ 是 $\Omega$ 中某个固定的元素。若 $f(x)$ 是 l.a.p. 的,则称 $f(\mathfrak{r})$ 是 a.p. 的,从而它有唯一的左平均值。

King's College,
Cambridge.

---

\* 在 (D) 中取 $x = e$,得 $|f(t) - f(b_\mu)| < \varepsilon$。于是

$$|f(t)| < \varepsilon + \max\{|f(b_1)|, \ldots, |f(b_m)|\}.$$

† J. v. Neumann, *Trans. American Math. Soc.*, 36 (1934), 445–492.

## 译注

### 文本与翻译说明

1. 原文为纯扫描图像(无文本层),全部文字经 150–1200 dpi 分档渲染后由 RapidOCR 逐页识别,公式再以局部放大与词框定位逐字核对;数学内容依据 OCR 碎片与数学上下文复原,凡不确定处均在下节"OCR 与印刷勘误"中逐条列出。
2. 原文两条显示不等式以字母 (D)、(D′)、(K) 编号,译文照录;正文中的 r.a.p./l.a.p. 缩写亦照录(右概周期/左概周期)。
3. 原书编者在翻印页的右缘(本篇两页则排在页脚)加有方括号行号标记 [1]、[2],属编者批注用的行号,不是论文内容,译文未保留;原刊页眉("EQUIVALENCE OF LEFT AND RIGHT ALMOST PERIODICITY." 及页码 285)亦不再出现。
4. 首页左上角扫出一个"187"字样,当为馆藏戳记或翻印伪迹,与正文无关,未予翻译。
5. 本篇术语沿用本卷《导论》译文:概周期函数(almost periodic)、左/右概周期性、左平均值(left mean)。

### 背景与文化注

〔译注1〕艾伦·马西森·图灵(Alan Mathison Turing,1912–1954),时任剑桥大学国王学院研究员(fellow)。本篇是他的第一篇发表论文(时年 22 岁);布里顿在本卷《导论》中称之为"一项小规模的发现",但能注意到连冯·诺依曼都未曾察觉的漏洞,是一个充满希望的开端。

〔译注2〕J. v. 诺依曼即约翰·冯·诺依曼(John von Neumann,1903–1957),姓氏缩写中的 "v." 为其姓名中 "von" 的缩写习惯。他于 1934 年在《美国数学会汇刊》发表《群中的概周期函数》,把玻尔(Harald Bohr)的概周期函数理论推广到任意群上,并分别用"左""右"两种平移方式建立了概周期性与不变平均值的理论。图灵这篇短文指出:对同一个函数而言,这两种定义实际上等价,从而使冯·诺依曼理论中"左""右"两套平行结论合而为一。

〔译注3〕原文的群用哥特字母 $\mathfrak{G}$(手写体花字)表示,OCR 一律误读为 "@"、"("、"6" 等;译文以 $\mathfrak{G}$ 恢复。原文说"$f(x)$ 是复值函数,变元 $x$ 取遍任意群",即抽象群上的复值函数——这正是冯·诺依曼 1934 年论文的框架。

〔译注4〕"反过来同理可证,或者利用逆群即可":若 $f$ 在 $\mathfrak{G}$ 上 r.a.p.,则在逆群 $\mathfrak{G}^{-1}$(乘法反序)上右平移变成左平移,故反向论断可由已证方向直接读出。

〔译注5〕"左平均值"(left mean):冯·诺依曼对群上的概周期函数构造了唯一的左、右平移不变平均 $M\{f\}$,这是后来"顺从群"(amenable group)理论与哈尔测度思想的先声。图灵在此指出,等价性一经证明,每个 l.a.p. 函数也就有唯一的左平均值,冯·诺依曼的理论无需区分左右各写一遍。

〔译注6〕"允许群作传递变换的对象集":即群 $\mathfrak{G}$ 传递地作用其上的集合 $\Omega$(如齐性空间)。通过取定基点 $\mathfrak{t} \in \Omega$、沿轨道 $x \mapsto x\mathfrak{t}$ 拉回,$\Omega$ 上的函数论便化归为群上的函数论;文末的定义 $f(x) = f(\mathfrak{r})$(当 $x\mathfrak{t} = \mathfrak{r}$)正是这一拉回。原文此段中 $\Omega$ 的元素以小写哥特字母($\mathfrak{r}$、$\mathfrak{t}$)书写,OCR 完全无法辨认,译文字母系按数学惯例复原(见勘误第 3 条)。

### OCR 与印刷勘误

复原过程中 OCR 的典型误读及处理如下(不确定度:低 = 多次多分辨率读数一致且有数学旁证;中 = 依赖上下文推断;高 = 无法完全确认):

1. **(K) 中的下标变量 π(不确定度:低)** —— (K) 行末的 "for each π" 在各次识别中分别作 "for each 7r"、"for each Tr"、"for each vr"、"for each π";同一字母在次页 "Putting π = μ(t) in the inequality (K)" 中再次出现且同样被读作 π 形。故 (K) 的跑动指标确为希腊字母 π(遍历 $1, \ldots, m$),而与 $b_\mu$ 之 $\mu$、$c_\nu$ 之 $\nu$ 区分。次页 "hence, for each μ" 处同一位置则印作 μ,两处不一致应属原文本色,译文照录。
2. **(D′) 的下标(不确定度:低)** —— 原行识别为 "|f(ta) − f(b,x)| < e",下标无法直接读出;按与 (D) 的对称性(左乘定义中同一组元素 $b_1, \ldots, b_m$)复原为 $f(b_\mu x)$。
3. **末段哥特字母(不确定度:中)** —— "Represent the elements of Ω by small Gothic letters" 之后,$\Omega$ 的元素字母 OCR 或读作 "y" 或整体丢失。条件式识别为 "whenever yt = y";按传递作用的拉回构造,复原为 "$x\mathfrak{t} = \mathfrak{r}$"($\mathfrak{t}$ 为固定基点)。若原刊此处字母与此不同,以原刊为准。
4. **脚注 \* 的不等式(不确定度:低)** —— 原行 "I,f() I <(+max {1f(b)), .., If(b.)1}" 复原为 $|f(t)| < \varepsilon + \max\{|f(b_1)|, \ldots, |f(b_m)|\}$(加号前的 ε 被 OCR 并入括号)。
5. **页脚两注的 OCR 噪声** —— "* Rcccived 23 April, 1935; rcad 25 April, 1935." 即 "Received 23 April, 1935; read 25 April, 1935.";参考文献注中 "T'rans.Amcrrcan Wah.Soc., 30 (1934),44o-49g" 应为 "Trans. American Math. Soc., 36 (1934), 445–492"(卷号 36 与页码 445–492 在另一档分辨率下读出,且与文献记录相符)。
6. **若干字母级混读** —— 正文中 c/x、l/1、I/( 屡有互换(如 "f(c)" 与 "f(x)"、"1.a.p." 与 "l.a.p."),均按上下文统一; "(6" 一律为群符号 $\mathfrak{G}$ 的误读。
