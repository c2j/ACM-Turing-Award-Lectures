# 注释与摘要

**Notes and Summaries**

> 作者:J. L. 布里顿(J. L. Britton)〔译注1〕
> 译自《图灵文集·纯数学》卷 pp. 225–273(个人学习用途)

以下按本卷论文顺序,给出编者对各篇的注释与(部分论文的)技术性摘要。方括号编号〔n〕对应原文页边所注的注释号。

## 左右概周期性的等价性(1935)

### 注释

〔1〕于是,f 是右概周期的(r.a.p.),当且仅当平移函数族

$$x \mapsto f(xa)\quad(a \in G)$$

在范数 $\|g\| = \sup_{x \in G} |g(x)|$ 之下是完全有界的。

〔2〕(a) 若 f 是左概周期的(l.a.p.),则左平均 L(f) 满足如下条件:对一切 $\varepsilon > 0$,存在 $n$、$c_i$、$a_i$($i = 1, \ldots, n$),使得 $c_i > 0$,$\sum c_i = 1$,且对 G 中一切 x 有

$$\left| \sum_i c_i f(a_i x) - L(f) \right| < \varepsilon 。$$

(b) 关于紧群情形的概周期函数与冯·诺依曼平均的讨论,见 Loomis(1953)第八章。〔译注2〕

## 李群的有限逼近(1938 A)

### 摘要

设 G 是一个抽象群,同时又是度量空间,满足

$$D(ax, ay) = D(x, y) = D(xa, ya)$$

对 G 中一切 $x, y, a$ 成立。(此时 G 是拓扑群。)例如,任何每一点都有可数邻域基的紧致 Hausdorff 拓扑群都具有这样的度量。

设 $\varepsilon > 0$。有限群 H(其乘积记作 $x \circ y$)称为 G 的 **ε-逼近**,若 H 是 G 的子集,且

(i) 每个 $x \in G$ 与某个 $r(x) \in H$ 的距离不超过 ε;

(ii) $a, b \in H$ 蕴含 $D(a \circ b, ab) < \varepsilon$。

若 G 对每个 $\varepsilon > 0$ 都有 ε-逼近,则称 G **可逼近**。

注意:可逼近群是完全有界的。

**定理 1.** 设 G 是可逼近群,带有忠实的连续表示〔译注3〕——即由复矩阵给出的、次数为 n 的表示——且 G 可用带忠实 n 次表示的有限群逼近。

**定理 2.** 设 G 是连通李群。若 G 可逼近,则 G 紧致且阿贝尔。

### 注释

〔1〕所谓"度量的群"(metrical group),应是指一个抽象群兼度量空间,其中乘积与逆运算连续。稍后即可看出,本文中唯一值得关心的度量的群是那些满足

$$D(xa, ya) = D(x, y) = D(ax, ay)$$

者。

〔2〕原文作 "Let H_ε",应读作 "For ε > 0 let H"。

〔3〕原文作 ">",应为 "<"。

〔4〕回忆:度量空间称为**完全有界**,若对每个 $\varepsilon > 0$,存在有限个半径为 ε 的开球覆盖该空间。度量空间紧致当且仅当它完备且完全有界。实际上,鉴于待证的结果,一开始就假定 G 紧致几乎不损失一般性。

〔5〕"such that" 之后应插入 "for all x in G"。

〔6〕为后文记:D(e∘e, e) < ε。

〔7〕矩阵取自复数域 C。"true"(真)意为"忠实"(faithful)。〔译注4〕

给定紧群或抽象有限群 G 的任意特征标 χ,可以写成 $\chi = \sum_{i=1}^{s} n_i \chi^{(i)}$,其中 $n_i > 0$ 为整数,而 $\chi^{(i)}$($i = 1, \ldots, s$)是 G 的两两不同的不可约特征标(但一般并非全部不可约特征标)。若对每个 i 都有 $n_i$ 等于 $\chi^{(i)}$ 的次数 $d_i$,则称 χ 是**规格化的**(normalized);χ 如上表出时的**规格化**指的是 $\sum_{i=1}^{s} d_i \chi^{(i)}$。若 χ 忠实,则其规格化亦忠实。实际将证明的不是定理 1,而是它的下述修改形式。

**定理 1′.** 设 G 是可逼近群,带有忠实连续表示 σ。令 σ′ 为 σ 的一个规格化,次数为 n;于是 σ′ 规格化且忠实。则 G 可用带忠实 n 次表示的有限群逼近。

〔8〕此处原文略有误导;所需论证如下:$D(ca_i, cr(a_i)) < \eta$,故 $|f(ca_i) - f(cr(a_i))| < \Delta$;$D(cr(a_i), c \circ r(a_i)) < \eta$,故 $|f(c \circ r(a_i)) - f(cr(a_i))| < \Delta$。从而 $|f(ca_i) - f(c \circ r(a_i))| < 2\Delta$。

〔9〕设 χ 是紧群 G 的任一特征标,如〔7〕那样写成和式。令 $W(\chi) = \int_G \chi(xy)\overline{\chi(y)}\,dy$,则

$$W(\chi)(x) = \sum_i \frac{d_i}{n}\,\chi^{(i)}(x),$$

其中 $d_i$ 是 $\chi^{(i)}$ 的次数。这一般不等于 $\chi(x)$;但若对所有 i 有 $n_i = d_i$,即 χ 已规格化,则两者相等。因此为了使式(7)成立,必须把给定的表示换成它的一个规格化;见上文〔7〕。

〔10〕为后文需要:α 小于某常数(此处 OCR 残损,原意约为 $\tfrac{1}{50}$ 一类的小量)。〔译注5〕

〔11〕这由函数 $g(x, y) = \chi(xy)\overline{\chi(y)}$ 在紧空间 $G \times G$ 上的一致连续性得出。

〔12〕令 $f(y) = \chi(ay)\overline{\chi(y)}$。若 $D(y, y') < \eta$,则 $D(ay, ay') < 2\eta$,故由(11)有 $|f(y) - f(y')| < \alpha/(50n)$。于是由引理,

$$\left| h^{-1} \sum_{b \in H_n} f(b) - \int_G f(y)\,dy \right| \le 2\alpha/(50n)。$$

〔13〕由 $D(a \circ b, ab) < \eta < 4\eta$ 及(10),得 $|\chi(a \circ b) - \chi(ab)| < \alpha/(50n^2)$。

〔14〕按(12)的定义,$|\sigma(b)| \le n$。〔译注6〕

〔15〕右端应除以 $\chi^{(j)}$ 的次数 $d_j$。

〔16〕由此处直到不等式(21),给出的论证应修正如下(中间步骤含大量求和与特征标展开,OCR 残损严重,大意如下):把各特征标按不可约分量展开并重新配项,令 $J_\chi = |\alpha_\chi/d_\chi - 1|$,则式(19)化为

$$\left| \sum_\mu J_\mu \chi^{(\mu)}(a) \right| < \alpha/(8n),$$

从而 $\sum J_\mu^2 < \alpha^2/(64n^2)$。定义 $\theta(a) = \sum_X c_X \chi^{(X)}(a)$,其中对每个 X,$c_X$ 取 0 或 $d_X$(选择方式在下文确定);则 θ 是 $H_n$ 的一个特征标,并且可得式(20)(除一处显然的排印错误外)。其次,

$$h^{-1} \sum_{b} |\theta(b) - \sigma(b)|^2 = \sum_X |c_X - \alpha_X|^2 。$$

若 $|\alpha_X/d_X| \le \tfrac{1}{2}$,则 $|\alpha_X/d_X - 1| \ge \tfrac{1}{2}$,故 $J_X \ge |\alpha_X|$;此时定义 $c_X = 0$。

〔17续〕若 $|\alpha_X/d_X| > \tfrac{1}{2}$,则 $J_X \ge |\alpha_X - d_X|$,故 $|\alpha_X - d_X| \le 2J_X$;此处定义 $c_X = d_X$。于是

$$h^{-1} \sum_b |\theta(b) - \sigma(b)|^2 = \sum_X |\alpha_X|^2 + \sum_{c_X = d_X} |d_X - \alpha_X|^2 \le \sum 4J_X^2 < \frac{\alpha^2}{16n^2},$$

此即(21)。〔译注7〕

〔17〕尽管对 H 中每个 b 都有 $|\sigma(b)| \le n$,在这一步却完全看不出 $|\theta(b)| \le n$ 为何成立。

应当感谢已故的 J. Frank Adams 在此处挽救了论证,如下:(利用三角不等式与已证的均方估计)

$$h^{-1} \sum_{b \in H_n} |\theta(b)|^2 \le \left(h^{-1}\sum_b |\theta(b) - \sigma(b)|^2\right) + \left(h^{-1}\sum_b |\sigma(b)|^2\right) \le \frac{\alpha^2}{4n} + n,$$

从而

$$\left| h^{-1} \sum_{b \in H_n} \big(\theta(a \circ b)\theta(b) - \sigma(a \circ b)\sigma(b)\big) \right| \le \frac{\alpha^2}{16n^2} + \frac{1}{2}\alpha,$$

又有 $|\theta(a) - \chi(a)| < \alpha^2/(16n^2) + \tfrac{1}{2}\alpha + \alpha/(10n) < \alpha$(因 $n \ge 1$ 且 $0 < \alpha < 1$)。

〔18〕$D(e_n \circ e, e) < \eta$,故 $|\chi(e_n \circ e) - \chi(e)| < \alpha/(50n^2)$。而 $|\sigma(e_n) - \chi(e_n \circ e)| < \alpha$,故 $|\theta(e_n) - \chi(e)| < \alpha + \alpha/(50n^2) \le \alpha' < 1$。$\sigma(e_n)$ 是整数而 $\chi(e) = n$,故 $\theta(e_n) = \chi(e) = n$。设 $a \in H_n$ 且 $D(a, e) \ge \tfrac{1}{2}\varepsilon$,则 $|\chi(a) - n| > \alpha$,又 $|\theta(a) - \chi(a)| < \alpha$,故 $\theta(a) \ne n = \theta(e_n)$;于是 a 不属于 N。

〔19〕$N = \{a \in H_n : \theta(a) = \theta(e_n)\}$ 是 $H_n$ 的自共轭(正规)子群,因为 θ 作为不可约特征标之和是 $H_n$ 的特征标。

〔20〕"coset of N" 应读作 "coset of N in $H_n$"。

〔21〕K 同构于 $H_n/N$。

〔22〕回忆:若 $x \in G$,存在 $r(x) \in H_n$ 使 $D(x, r(x)) < \varepsilon$。

〔23〕$D(ab, u(a)u(b)) \le D(ab, av(b)) + D(av(b), u(a)u(b)) < 2(\tfrac{1}{2}\varepsilon + \eta)$。

〔24〕从下文看,"连通"似乎被当作李群定义的一部分。

〔25〕$D(xy, yx) \le D(ada'd', aa') + D(aa', a'a) + D(a'a, a'd'ad)$。因 $a' \circ a = a \circ a'$,中间一项小于 $2\varepsilon$。又一般地有 $D(s_1 s_2 s_3, t_1 t_2 t_3) \le \sum_i D(s_i, t_i)$。故

$$D(xy, yx) < 4\varepsilon + 2\varepsilon + 4\varepsilon = 10\varepsilon 。$$

〔26〕此处似有一处缺口。令 $J = \bigcup_{x \in G} \{x\} \times Nx$。则 $E \subset J \subset G \times G$。若 J 可测,则该不等式可由 Fubini 定理得出;因为

$$m(E) = \int \{ x : (\downarrow_x N dy) \} dx = \int m(N)\,dx 。$$

J 或 J 的某种适当变形的可测性尚需证明。〔译注8〕

## 群的扩张(1938 B)

### 摘要

在本摘要中,M 是一个群,$\Omega$ 是它的自同构群,S 是内自同构群。M 是某个群 G 的正规子群。$\chi\colon G \to \Omega$,$a \mapsto \chi_a$,是一个同态,且 $\chi(M) \subseteq S$;于是 χ 诱导同态 $\bar{\chi}\colon G/M \to \Omega/S$。〔译注9〕若 E 是 M 经由某商群的扩张,则有一个同态 $H\colon E/M \to \Omega/S$,$gM \mapsto \bar{g}S$,其中 $\bar{g}$ 定义为 $\bar{g}(n) = g^{-1}ng$($n \in M$)。若存在同构 $\Lambda\colon G/M \to E/M$ 使 $H = \bar{\chi} \circ \Lambda$,则称该扩张**实现**(realize)$\bar{\chi}$。

第一个主要结果是定理 1 的推论。

设 F 是自由群。则实现 χ 的、M 经由 $F/R$ 的扩张存在,当且仅当存在同态 $\alpha\colon F \to M$,使得 $\chi_{\alpha(a)}(\alpha(r)) = \alpha(a^{-1}ra)$ 且 $\chi_b(b) = \alpha(r)^{-1}b\,\alpha(r)$ 对一切 $a \in F$、$r \in R$、$b \in M$ 成立。〔译注10〕

接下来是下述定理。

**定理 2.** 设 G 是由 $e_1, \ldots, e_l$ 生成的自由群。设有元素 $r_1, \ldots, r_l$ 属于 R,使它们在 G 中生成的正规子群就是 R。又设有满足 $\chi_{r_i}(b) = r_i b r_i^{-1}$ 的相应元素,使对一切 $i = 1, \ldots, l$ 相容。则在 M 的中心 $Z(M)$ 中存在 $s_1, \ldots, s_l$,使下述条件成立:

(*) 若在 G 中有 $\prod a_i^{-1} r_i^{t_i} a_i = 1$(每个 $t_i = \pm 1$),则

$$\prod \chi_{a_i}(r_i^{s_i} s_i^{\epsilon_i}) = 1 。$$

〔译注11〕

作者随后利用赖德迈斯特(Reidemeister)关于子群的生成元与关系的工作,把定理 2 加以简化。

设 G、M 如定理 2。在每个傍系 $aR$ 中选取一个代表,记作 $v_a$ 或 $v(a)$;取 $v_1 = 1$。对 $a$ 属于相应的代表集,令 $\rho_a = v_a^{-1}a$。令 $E_{i,a}$ 表示有序对 $(i, a)$,$i = 1, \ldots, l$;$E_i$ 即 $E_{i,1}$。设 Φ 是以诸 $E_{i,a}$ 为生成元的自由群,并定义同态 $\tau\colon \Phi \to M$(定义式此处原文排印倒置,残损不可辨)。〔译注12〕可以给出一个构造,对每个 c 给出 Φ 中元素 $R_c$,使 $\tau(R_c) = r_c$。由于 $r_{e_i} = r_i$,我们有 $\tau(R_{u_i}E_i^{-1}) = 1$。

本文的主要结果是下一个定理。

**定理 4.** 在定理 2 中,可以把条件(*)换成如下条件:设 $\theta\colon \Phi \to M$ 是使 $\theta(E_{i,a}) = \chi_a(\cdots)$ 的同态,则对所有形如 $R_{ca}s_iE_i^{-1}$ 的 X 必须有 $\theta(X) = 1$。〔译注12〕

最后给出一个简单应用:

**定理 5.** 设 S 是群 M 的内自同构群,并令 $A = \operatorname{Aut} M$。设 $n \ge 2$ 为整数,$\sigma \in A$。假定傍系 $\sigma S$ 在 $A/S$ 中的阶为 n,于是存在 $r^* \in M$,使 $\sigma^n(b) = r^{*-1} b r^*$ 对一切 $b \in M$ 成立。则存在 M 经由 n 阶循环群 $\langle a \rangle$ 的、实现同态 $\langle a \rangle \to A/S$(其中 $a \mapsto \sigma S$)的扩张,当且仅当存在属于中心的元素 ζ 使

$$\zeta\sigma^{-1} = \zeta(r^*)\,r^{*-1} 。$$

〔译注12〕

**按:** 定理 4 的陈述存疑。它可能是对的,但所给的证明不充分。可以证明一个较弱的版本(该版本陈述一行在此完全残损,无法复原)。〔译注12〕

### 注释

〔1〕图灵的约定是:两个自同构 α、β 之积先作用 α 再作用 β。因此傍系 $gS$ 对应于傍系 $\bar{g}S$,其中 $\bar{g}(n) = g^{-1}ng$,$g \in G$,$n \in M$。

〔2〕如今我们或许更愿意说:χ(或 $y \mapsto \chi(y)$,或 $y \cdot \chi(y)$)是(到 $\Omega/S$ 的)一个同态。

〔3〕"χa" 应读作 "$a \mapsto \chi_a$";同样,"α(r)"、"m(r)" 应分别读作 "$r \mapsto \alpha(r)$"、"$r \mapsto m(r)$"。

〔4〕也就是说,$y \mapsto \chi(y)$ 是同态 $F/R \to \Omega(M)/S(M)$,其中 $\Omega(M)$、$S(M)$ 分别是 M 的自同构群与内自同构群。

〔5〕所谓“M 经由 G′ 的、其中 M 的傍系 α 诱导类 X(α) 的扩张”,是指这样一个扩张 E:存在同构 $\mu\colon G'/R \to G/M$,使得对一切 $g \in G'$ 有 $gS = X(\mu(gR))$(其中 $\bar{g}(n) = g^{-1}ng$ 对一切 $n \in M$)。〔译注10〕

〔6〕值得为后文记下:必要性的证明不用到 (b) 或 (c)。

〔7〕下标 b′ 与 b 应互换。

〔8〕借助映射 $n \mapsto (1, n)$($n \in M$),可把 M 等同于 E 的一个正规子群。

〔9〕另一个附加结论是:存在同构 $F/R \to G'/M$,$fM \mapsto m(f)M$;因 $m(F) \subseteq \ldots$ 它是同态,由条件 (b) 它是满射,而单射性由上一行已证的结果——若 $a$ 属于 E 且 $m(a) \in M$,则 $a \in R$——得出。〔译注10〕

〔10〕要看出这一点,取 $e'_i$ 使 $e_iR = \mu(e'_i)$,其中 μ 是注〔5〕的同构。则

$$e_i/S = X(\mu(e'_i)) = X(e'_i),$$

它包含 $\chi e'_i$;于是 $\chi e'_i$ 是 $e'/$(原文如此)乘以一个依赖于 i 的内自同构 $n_i$ 之积;不失一般性可把 $e'$ 换成 $e'n_i$,于是 $\chi_{e'_i}(n) = e'^{-1}ne'_i$。〔译注10〕

〔11〕用到 G 是自由群这一点。

〔12〕M 的任一傍系 α 可写成 $m(f)M$,其中 f 属于 E。令 $\alpha' = fM$。则 χ 属于 $X(\alpha')$,且由 (a),$m(f)$ 即所求。故 $X(\alpha') = m(f)S$,这正是 α 所诱导的傍系。

〔13〕如前,χ 假定为同态 $F/R \to \Omega/S$。

〔14〕容易看出 $rr'$(记作 $h_{ij}$)落在 M 的中心。但 $s_{ij} = r_i^{-1}h_{ij}r_j$,故 $s_{ij}$ 也在中心里。

〔15〕"$t_j$" 应换成 "j"。〔译注10〕

〔16〕若 M 阿贝尔,毫无困难。当 M 的中心为 1 时,可论证如下。设 $a$ 属于 E,$b$ 属于 M。则(逐行演算,部分残损)

$$\chi_a r_a(b) = \chi_a(\chi_{a^{-1}}(\chi_a(b))) = \chi_a(r_a^{-1} b\, r_a) = \chi_a(r_a^{-1})\,b\,\chi_a(r_a),$$

故 $\chi_{a^{-1}}r_{a} = (\chi_a(v^*))\cdots$。今设 $\prod a_i^{-1}r_i a_i = 1$ 并令 $\beta = \prod \chi_{a_i}(r_i^*)$。则 $\chi_1 = \beta$,故 β 落在中心里,从而 $\beta = 1$。于是,若把每个 $s_i$ 定义为 1,则(7)蕴含(6),所需的扩张遂存在。〔译注10〕

〔17〕集合记号碎片:$\{1, 2, \ldots, l\} \times \ldots$

〔18〕项 "'ce', e" 应换成它的逆。

〔19〕注意 $\rho_{a,e} = \rho_{v(a)}$;并为后文注意 $\rho_{v(a)e_i} = \rho_{v(ae_i)}$。于是(12)的第二个方程是(10)的第一个方程的类似物。(10)经修正的第二个方程的类似物是(下一页)

$$R_{ce^{-1}} = \chi_{c^{-1}}(R_{u(ce)}\cdot eR),$$

而(12)的第三个方程应由此替换。此处方程 $R_{(ce)e} = R_{(ce')e} = R_e$ 容易验证。

〔20〕实际上,(12)诸方程蕴含的是:当 k 为 $e_i$ 或 e 时,

$$R_{ck} = R_{u(c)k}\,\chi_k(R^{-1}R_c) \tag{13}$$

我看不出为何应有 $R_{u(c)} = 1$。(例如,(13′)中取 $k = e_i$ 时,可由(12)的第二个方程以及把 c 换成 vc 后得到的方程推出——注意 $v_{vc} = v_c$。)不过我们确实有 $\rho_e = 1$,故 $R_{ue}P$,即在 $\Phi/P$ 中 $R_u = 1$。若把 $R_u$ 视为已含于(15)之中,则可认为(13)在作者随后的讨论中有效。无论如何,当 $c \in R$ 时(13)与(13′)相同。

〔21〕确切地说,$\tau(R_r) = r$。这可以用(12)作归纳证明。(若 $\gamma_a\colon R \to R$ 定义为 $\gamma_a(r) = a^{-1}ra$,则有 $\gamma_a\tau = \rho_a\chi_a$。)

〔22〕还要注意:χ_c 作用于形如(9)的表达式,所得仍具形式(9)。(写 $A = ac$、$B = bc$;则 $ab^{-1} = AB^{-1}$。)

〔23〕不必假设对所有 c 有 $R_{u,c} = 1$,即有

$$R_{ax} = R_{u(ax)}\,\chi_x(R^{-1}R_a)\qquad\text{对一切 } a, x \text{ 属于 G。} \tag{*}$$

为此,先注意当 x 为 $e_i$ 或 $e'$ 时它成立。设其对 x 与 y 均成立。则

$$R_{ax.y} = R_{u(ax)y}\,\chi_y(R_{u(ax)}R_{ax})。$$

现在 $v(vax) = v(ax)$,故

$$R_{ux.y} = R_{u(axy)}\chi_y(R_{u(ax)}R_{ax})。$$

从这两个方程得

$$R_{ax.y} = R_{ux.y}\,\chi_y(R_{ut})\cdot\chi_{xy}(R_{ax}),$$

而由 $RR_{ax} = \chi_x(R^{-1}R_a)$ 得(*)对 xy 成立。

〔24〕(a) 一个较弱的定理如下。

**定理 3′.** R 同构于 $\Phi/P'$,其中 P′ 是 Φ 的、包含所有形如(9)的元素及所有形如 $\chi_s(R_{a^{-1}r_i a}E_{ia})$ 的元素的最小正规子群。(无需包含 $R_u$。见注〔20〕。)

为证此,先注意每个 $\chi_s$ 使 P′ 不变。在 $\Phi/P'$ 中工作,有下列各式:

(1) $\chi_b(R_\alpha) = R_{b^{-1}\alpha b}$,其中 $\alpha = a^{-1}r_i a$。(因为 $\chi_b(R_\alpha) = \chi_b(E_{i,a}) = E_{i,ab} = R_{b^{-1}a^{-1}r_iab}$。)

(2) 对 $r \in R$、x 属于生成元,有 $R_x = R_x\chi_x(R_r)$。(见注〔20〕。)

(3) 对 $r \in R$,$\chi_x(R_{r^{-1}}) = R^{-1}$。

(4) 若 $\alpha = a^{-1}r_i a$,则 $R_{\alpha^{-1}} = R_{\alpha'}$。($R_\alpha = \chi_{a^{-1}}(R_a) = R_\alpha$,由 (1)。)

(5) 若 $\alpha = a^{-1}r_i a$、$\beta = b^{-1}r_j b$,则 $\chi_s(R_\alpha) = R_{\beta^{-1}\alpha\beta} = R_{\beta'}R_\alpha R_\beta^{-1}$。(这由 (9) 得出。)

(6) 把 β 换成 $\beta^{-1}$,(5) 的结论仍真。($R_\alpha = R_\beta\chi_\beta(R_\alpha)R_\beta^{-1} = \chi_\beta(R_\beta R_\alpha R_\beta^{-1})$。故 $\chi_{\beta^{-1}}(R_\alpha) = RR_\alpha R^{-1}$。)

(7) 把 α 换成 $\alpha^{-1}$,(5)、(6) 的结论仍真。(两边取逆即得。)

(8) …… $R_\alpha, R_\alpha \cdots R_{ax}$。故 $R_{rs} = R_rR_s$,$r, s \in R$。(对 k 归纳,利用……)〔此式残损。〕

由 (8) 我们有同态 $\alpha\colon R \to \Phi/P'$,$r \mapsto R_rP'$。现在 τ 诱导同态 $\tau'\colon \Phi/P' \to R$,且 $\tau'(\alpha(r)) = \tau'(R_rP') = \tau(R_r) = r$。又有 $\alpha(\tau'(E_{i,a}P')) = \alpha(a^{-1}r_i a) = R_{a^{-1}r_i a}P' = E_{i,a}P'$。故 $SR = \Phi/P'$。〔译注10〕

(b) 依编者之见,作者之所以陷入困难,是因为没有严格遵循 REIDEMEISTER(1926)的约定。若他遵循了,就会考虑右傍系 Ra,并写 $a = r_av_a$,写 $u_{ae_i} = r_{a,e_i}$……(作为 Reidemeister 论文的替代,读者可查阅 MAGNUS、KARRAS 与 SOLITAR(1966),定理 2.8。)

我们现在用这一途径建立 R 的一个呈现。设 F 是以符号 $e_i$($i \in I$)为生成元的自由群,R 是由元素 $g_j$($j \in J'$)生成的子群。R 未必正规。取右傍系 Ra 的代表 $a_p$,其中 R 的代表取为 1。令 P 为代表之集。若 p 是一个代表,令 $S_{p,e_i} = pe_ip'^{-1}$。令 $S_{p,e_i}$ 同时表示有序对 $(p, e_i)$。著名的 Reidemeister 重写过程给出:对每个代表 R 中元素的、诸 $e_i$ 上的字 A,有一个诸 $S_{p,e_i}$ 上的字 $\tau(A)$,使对应的字在 R 中等于 A。Reidemeister 定理的一个特例是:R 的一个呈现为

$$\langle S_{p,e_i}\ (p \in P, i \in I):\ S_{p,e_i} = \tau(s_{p,e_i})\ (p \in P, i \in I) \rangle。$$

**推论.** 存在 $J'$ 的子集 J(当 I 与 P 有限时它也有限),使得若 Φ 是以符号 $G_j$($j \in J$)为生成元的自由群,则 R 的一个呈现为

$$\langle G_j\ (j \in J):\ G_j = \nu(g_j)\ (j \in J) \rangle,$$

其中 ν 定义如下:对每个 $S_{p,e_i}$,选一个在 R 中等于它的字 $w(G_j)$,并置 $\nu(S_{p,e_i}) = w(G_j)$。

**推论之证.** 设 B 是以诸 $S_{p,e_i}$ 为生成元的自由群。于是有同态 $\rho\colon B \to R$,$S_{p,e_i} \mapsto s_{p,e_i}$,且 $\rho\tau(r) = r$($r \in R$)。……

(接下页)……这就定义了 J;设 Φ 如推论所述。有同态 $\tau\colon \Phi \to R$,$G_j \mapsto g_j$。又 ν 可扩充为同态 $B \to \Phi$,且有 $\tau\nu = \rho$。因为 $\tau\nu\tau = \rho\tau = 1$,τ 是满射。设 N 是 Φ 的、由 $G_j^{-1}\nu\tau(G_j)$(记作 $\eta_j$,j 取遍 J)生成的正规子群。则 $N \subseteq \operatorname{Ker}\tau$。

实际上 $N = \operatorname{Ker}\tau$:因为若 $\xi \in \operatorname{Ker}\tau$,则 $\xi = w(G_j)$(某个字),且 $\tau(\xi) = 1$,于是 $1 = \nu\tau(\xi) = w(\nu\tau(G_j)) = w(G_j\eta_j) = w(G_j)\eta = \xi\eta$,某个 $\eta \in N$。故 $R \cong \Phi/N$,推论得证。

(c) 我们未能验证定理 3(无论有无关系 $R_u = 1$;见注〔20〕)。由定理 3′,只需证明

$$(**) \qquad R_{a^{-1}r_i a}E_{ia}$$

属于 P。〔译注10〕若考虑其应用(见定理 4),定理 3′ 不如定理 3 好,因为表达式(**)的个数可能无穷(即使 G′ 是有限群而自由群有限生成)。相比之下,(b) 中 R 的呈现($g_j$ 即 $a^{-1}r_i a$)是有限的,故无此缺陷。

〔25〕若把定理 3 换成定理 3′(见注〔24〕),便得到较弱的定理 4′。

**定理 4′.** 陈述与定理 4 相同,只是把“对一切形如(15)的 X”换成“对一切形如 $R_{a^{-1}r_i a}E_{ia}$ 的 X”。

〔26〕只须对 X 为生成元 $E_{i,b}$ 的情形证明,也就是证明 $\theta(\chi_\alpha(E_{i,b})) = \chi_\alpha(\theta(E_{i,b}))$。而这容易验证。

〔27〕一旦确立了这一点,θ 便可看作从(某商群到 M)的同态(一句残损);于是 $\prod \theta(a_i^{-1}r_ja_i) = 1$,即 $\prod \theta(E_{ia}) = 1$,而由(18)这与 (6) 等价。

〔28〕$\chi_{ab^{-1}}(r_j) = \chi_a(\chi_{b^{-1}}(r_j)) = \cdots$(中间步骤残损)……利用 $r = r_j(\cdots)$。〔译注10〕

〔29〕为证其逆,设 (7) 蕴含 (6)。我们要证 $\theta(R_{us}E_i^{-1}) = 1$。现在 $R_{us}E_i^{-1}$ 是诸 E 上的一个字,设为 $w(E_{i,a})$。它在 F 中等于 1,故 $w(a^{-1}r_i a) = 1$。于是 $w(\chi_a(r_i)) = 1$。从而 $\theta(w(E_{i,a})) = w(\theta(E_{i,a})) = 1$,即为所求。

〔30〕定理 5 之证:设 G、M 如 §3 开头。则有同态 $X\colon G/R \to \Omega/S$,$aR \mapsto \beta$;也有同态 $\chi\colon G \to \Omega$。对 $b \in M$,$\chi_{a^{n-1}}(b) = \sigma^{n-1}(b) = r^{*-1}br^*$。于是定理 2 从而定理 4 的假设成立。若扩张存在,则由定理 4 有中心元素使得,其中 $\theta(E_{i,a}) = \chi_a(r_i^a g^{-1})$,有 $\theta(Q_aQ^{-1}) = 1$;故 (21) 成立。反之,若有满足 (21) 的中心元素并置 $\theta(E_{i,a}) = \chi_a(r_i^a g^{-1})$,则可得 $\theta(Q_a) = g\zeta(r^{*-1})$。例如(公式残损)……于是 θ 把元素 (19) 映到 1。故扩张存在。〔译注10〕

〔31〕"A″" 应为 "Aⁿ"。〔译注10〕

〔32〕"A, A², …" 指 $A, A^2, \ldots, A^{n-1}$。

〔33〕如前所见,作者是把定理 5 作为定理 4 的特例推出的,这要用到 §2 的全套机器。其实定理 5 可以直接从定理 2 推出。如注〔30〕所示,定理 2 的假设成立。设 (21) 成立:

$$\prod \chi_a(r_i^a g^{-1})^{s_i} = \prod \zeta(r_i^a g^{-1})^{s_i} = \zeta\big((r_i^ag^{-1})^{\sum s_i}\big) = 1,$$

末一步反复用 (21),并因 $\sum s_i = 0$。由定理 2 扩张存在。反之,若扩张存在,则因 $a^{-1}r_a r a^{-1}\cdots = 1$,由定理 2 有 $\chi_a(r^*g^{-1})(r^*g^{-1})^{-1} = 1$。故 $\zeta(r^*g^{-1}) = r^*g^{-1}$。

## 计算泽塔函数的一种方法(1943)

### 摘要

作者首先给出泽塔函数的一个积分表示如下。令

$$I(s) = \int_L h(z)\,dz,\qquad h(z) = \frac{\exp(i\pi z^2)\,z^{-s}}{\exp(i\pi z) - \exp(-i\pi z)},$$

其中在正实轴上 $\arg z = 0$,而 L 是直线 $z = \tfrac12 + \Lambda\varepsilon$($\Lambda$ 取遍实数,$-\infty$ 到 $\infty$),$\varepsilon = \exp(\tfrac14\pi i)$。于是有(一个联系 $\zeta$ 与 I 的恒等式,式中诸因子含 $\Gamma$ 函数;此行公式残损)。〔译注13〕在临界线 $s = \sigma + it$(即 $\sigma = \tfrac12$)上我们得到

$$\zeta(s)\Gamma(\tfrac12 s)\pi^{-s/2} = -2\,\Re\big(\Gamma(\tfrac12 s)\pi^{-s/2} I(s)\big)。$$

论文的大部分致力于用正实参数 K、μ 给出 I(s) 的估计。为此的一个主要步骤是结果

$$I(s) = \sum_{r=1}^{k} \frac{r^{-s}}{1 - \exp(2\pi r\varepsilon(r-\mu))}\,h(p_k) + R, \tag{1}$$

其中 $p_k = \mu + e_k/k$,而 |R| 小于一个非常复杂的表达式(即原文的式 (5.18))。〔译注13〕

〔在 (5.18) 中,$\bar{t} = t/2\pi$,而 $\sigma$、S、γ 是 $\omega$ 的函数,这里 $\omega = K\bar{t}^{-1/2}$;$y_0, z_0$ 由 $\eta_0 = \xi_0\bar{t}^{-1/2}$、$z_0 = x_0 + iy_0$ 定义(y₁、z₁ 类似)。〕

图灵随后希望限定参数的选取,目的是简化并缩小 |R| 的界,并把 (1) 中的无穷和换成误差很小的有限和。第一步他取 μ 接近 t、K 的某个特定函数 μ₀;若 $k \ge 2$,可取区间 $(\mu_0 - \tfrac12,\, \mu_0 + \tfrac12)$ 内任何 μ。

然后,在对一般情形作些讨论之后,他处理 $\omega \to 0$ 与 $\omega \to \infty$ 两个特殊情形。前一情形 $\mu_0 \to \bar{t}^{1/2}$(数字经 OCR,存疑〔译注13〕),后一情形 $\mu_0 \to k/\sqrt{2}$。

结果表明,级数 $\sum (\varepsilon/r)\,h(p_k)$ 可以用有限和逼近:$\omega \to 0$ 时其误差项为某小量;$\omega \to \infty$ 时为 $\exp(-\tfrac12\pi(2K+1))$。(细节残损。)

(1) 中另一个无穷级数较易用有限和逼近:r < μ 时逼近到 $r^{-s}$,r > μ 时为 0。

参数的一个特定特化(在 $\omega \to 0$ 情形)导出下面的定理;$\omega \to \infty$ 情形未给出显式特化。该定理显然给出了计算 $\zeta(\tfrac12 + it)$ 的实用方法。

**定理.** 存在函数 $I(s)$($s = \sigma + it$),在临界线上满足方程

$$\zeta(s)\Gamma(\tfrac12 s)\pi^{-s/2} = -2\,\Re\big(\Gamma(\tfrac12 s)\pi^{-s/2}I(s)\big),$$

并满足下述条件。设 $\omega = \ldots$,$t > 350$。令 $K = 1.6\omega/\sqrt2$(数字残损)、$\bar{t} = t/2\pi$、$\varepsilon = \exp(i\pi/4)$、$\mu = t^{1/2}$、$p_k = \mu + e_k/k$。则

$$I(s) = \varepsilon\sum_{r=1}^{m-1} r^{-1}\big(h(p_{-1}) + h(p_0) + h(p_1)\big) - \sum r^{-s} - m^{-s}F_m - (m+1)^{-s}F_{m+1} + E,$$

其中 h 是前文定义的函数,$F_r = (1 - \exp(2\pi r\varepsilon(r-\mu)))^{-1}$,$m = [\mu]$,且 $|E| \le 0.0044\,t^{-1/4}$(例如若 $t < 1000$,则 $m - 1 \le 11$)。

若 μ 是整数(从而 $m = \mu$),则 $\varepsilon h(p_0)/k$ 与 $m^{-s}F_m$ 都是无穷。但若以 $F(u)$ 记 $F_r$,则极限

$$\lim_{d \to 0}\big[h(m+d) - m^{-s}F_m(m+d)\big]$$

存在,故这两项可用此极限替换。

条件 $\mu = t^{1/2}$ 可换成 $t^{1/2} - \tfrac12 \le \mu \le t^{1/2} + \tfrac12$,代价是增大数值 0.0044。这使我们在任何计算中都可取 μ 为整数或半奇数。

### 注释

〔1〕所需的变量替换是 $t = z^{-1}$。

〔2〕为计算 $\int \exp(i\pi z^2 + 2\pi iuz - i\pi u)\,dz$,配方得 $\exp(-i\pi(u-\tfrac12)^2)\int \exp(i\pi z'^2)\,dz'$。再令 $z = (1+i)t/(2\pi)^{1/2}$ 并用 $\int \exp(-\tfrac12 t^2)\,dt = (2\pi)^{1/2}$。

〔3〕合适的值是 $k + \tfrac12$,$k = 1, 2, 3, \ldots$ 若 $z = k + \delta$,其中 δ 很小但 $|\delta| \ge \epsilon > 0$,则

$$|1 - \exp(-2\pi iz)| = |1 - \exp(-2\pi i\delta)| \ge 2\pi\epsilon。$$

〔4〕(i) 对奇数整数 $1 + \exp(i\pi s) = 0$。(ii) 该积分在任何区域 $|s| < R$ 中一致收敛:因为若 $z = \lambda i$,$\lambda$ 为大正数,则 $|z^{-s}| < K\lambda^L$(K、L 为常数),$|1 - \exp(-2\pi iz)| \sim \exp(2\pi x)$,而 $K\lambda^L/\exp(2\pi x) < K'\exp(-\tfrac12\lambda)$。故积分对所有 s 都是 s 的解析函数。

〔5〕沿 L 的积分中,先设 z 正实并作变换 $t = \cdots - 2\pi iuz$(符号残损)。L 变成 $-C$,即箭头反向的 C,C 是 Γ(z) 的 Hankel 表示中的围道。于是该积分等于 $-2(2\pi)^{s-1}i\sin(s\pi)\Gamma(1-s)\exp(+is\pi)\cdots$。现在可以去掉对 z 的限制。〔译注13〕

〔6〕即直线 $x = \tfrac12$ 与 $x = -\tfrac12$。

〔7〕$\exp(i\pi u^2)$ 应为 $\exp(-i\pi u^2)$。

〔8〕上一行的积分中,要求 $-\pi < \arg u < \pi$ 还是(另一范围)并无差别;但为了换到 $0 < \cdots$,需要后者。〔译注13〕

〔9〕一般地,

$$\int_{\sigma>1} f(z)\,dz = \int_{\sigma<1} F(z)\,dz。$$

〔10〕在公式 $2^{2z-1}\Gamma(z)\Gamma(z+\tfrac12) = \pi^{1/2}\Gamma(2z)$ 中取 $z = \tfrac34 - \tfrac12 s$(下标残损);在公式 $\Gamma(z)\Gamma(1-z) = \pi/\sin(\pi z)$ 中取 $z = \tfrac12 s$。方程随之得出。

〔11〕右端应把 $I(\tfrac12 s)$ 换成 $-\Gamma(\tfrac12 s)$。(OCR 中 Γ 常呈 F 或 I,此处按文意复原。)

〔12〕把 $\bar{I}(s)$ 换成 $I(s)$。(若在 (2.3) 中以 $\bar{s}$ 代 s 然后对方程取共轭,$I(\bar{s})$ 变成 $I(s)$,其余各项不变。在临界线上 $I(1-\bar{s}) = I(s)$。)

〔13〕(一行完全残损,无法复原。)

〔14〕重要的是这里的 P 应换成 J。

〔15〕对任意实 X 及 $z \in J \cup J'$(公式残损):选取 X 使虚部消失。则 $|A| > \tfrac12\pi$,其中

$$A = \Re\big(2\pi ir\varepsilon(z-\mu)\big) = 2\pi r(x-\mu-y)/\sqrt2 。$$

现在在 P 左侧 A < 0,故 $A < -\tfrac12\pi$,表达式小于 $(1-\exp(-\tfrac12\pi))^{-1} < 1.27$。P 右侧类似。

〔16〕定义 $R_0 = \{\cdots\}$、$H = \{\cdots\}$、H₁,其中 $H = h(z)e^z/(1-e^\zeta)$ 而 $\zeta = 2\pi rc\varepsilon(\xi(z-\mu))\operatorname{sg}(z)$(残损)。写 $J_1 + g = \sum_1 + \sum_2$ 且 $V = \int(\cdots)h$,则 V 即 P 与 J 之间求和的 $\sum r^{-s}$,并且

$$I(s) = -\sum_{r=1}^{k} r^{-s} + \sum_1 + \sum_2 - V + R_0 。$$

正文中 I(s) 的方程由此得出。

〔17〕(3.2)的被积函数等于 $1.27|h(z)\exp[\cdots]|$,其中 ζ 如注〔16〕。

〔18〕我们有 $R_1 = \sum D_r r^{-s}$,其中 $D_r = (1-\exp(2\pi r\varepsilon(r-\mu)))^{-1} - \delta_r$。写 $n = 2\pi r\varepsilon(r-\mu)$,D_r 的值为:

| r 的位置 | $D_r$ |
|---|---|
| J′ 之左 | $\exp(n)/(\exp(n)-1)$ |
| J 与 J′ 之间 | 0 |
| 其余(J 之右) | $\exp(-n)/(\exp(-n)-1)$ |

前面已看到:若 $d(z,P) > \tfrac12 x^{-1}$,则 $|1-\exp[2\pi ur\varepsilon\operatorname{esg}(z)(z-\mu)]|^{-1} < 1.27$。故若 r 在 J′ 左侧,则 $|1-\exp n|^{-1} < 1.27$($n = 2\pi r\varepsilon(r-\mu)$);若 r 在 J 右侧,则 $|1-\exp(-n)|^{-1} < 1.27$——这里须设 $d(m+1, P) > \tfrac12 r^{-1}$。于是对不在 J′ 与 J 之间的 r 有 $|D_r| < 1.27\exp[-\sqrt2\pi x|r-\mu|]$。这就给出正文 |R₁| 的界。

〔19〕这由从 O 到(某点)积分得出。

〔20〕这里用 $\int_0^\infty \exp(-\tfrac12 t^2)\,dt = \sqrt{2\pi}$。

〔21〕设 t > 0,则知 z₀、z₁ 中一个在第一象限另一个在第二象限;z₀、z₁ 中一个在第三象限另一个在第四象限。要求 z₀、z₀(原文如此)在右半平面,便推出 $z_0, z_1, \bar{z}_1, \bar{z}_0$ 分别在第一、二、三、四象限。又有 $\bar{z}' = -z_0$、$0 \le \arg z_0 \le \tfrac12\pi$,而向量 z₀、z₁ 之间的夹角被向量 i 平分。(若干符号残损。)

〔22〕图灵假定 t > 0。

〔23〕(i) 最后一句应为 $\tfrac12\pi > \arg\xi_0 > 0$。(ii) 从此处起记号改变如下(后文第 192 页顶部得到印证):

| 原记号 | 新记号 |
|---|---|
| $z_0, z_1$(带共轭者互换) | $z_0, z_1$(同上互换) |

表中具体对应关系因 OCR 残损不能逐一复原,大意是新旧记号把带横线与不带横线的字母互换。此后这些注释一律使用新记号,除非另有说明。〔译注13〕

〔24〕在图 2 中,b 在第四象限。故按旧记号 $b = z_0 - y(1+i)$。

〔25〕为证 J₁ 位于下半平面的部分对余项 R₀ 的贡献趋于零,需知(旧记号)$|y_0|$ 相对 x 不太大。只须注意 $z_0 + \bar{z}_1$ 的虚部的模大于 z₀ 虚部的模,即 $x > |y_0|$。

〔26〕旧记号下,位于第一象限的 $b‘ = z_0 - \tfrac12 y_0(1+i)$。同样,图 2 的 z₀ 在原记号中是 $z_0$。

〔27〕这些事实由注意 $\arg z_0 \le \pi$ 从而 $|b’| \ge |z_0|$(旧记号)即得。

〔28〕首先,"ξ" 应为 "ξ₀"。现在 $t^{1/2}\eta(\xi_0) = \Re(\varepsilon z_0) = (x_0 - y_0)/\sqrt2$,这正是 z₀ 到直线 J₁ 的垂直距离,故结论成立。

〔29〕这是因为在 J₁ 和 J₂ 上 $|y| \ge |y_0|$。

〔30〕证明不等式 (5.2)、(5.3) 的另一途径如下。设 l 为 J₁ 上从 z₀ 起算的弧长。则在 J₁ 上 $z - z_0 = \pm le$,而

$$\rho'(z)\,dz/dl = 2\pi i(z-z_0)(z-z_1)(\pm\varepsilon)/\bar{z} = 2\pi ile^2(z-z_1)/z = -2\pi l(z-z_1)/z 。$$

今设对某个 d 有 $\Im((z-z_1)/z) \ge d > 0$,则 $\Re\rho'(z)\,dz/dl \le -2\pi ld$。由 §4(a),

$$\int_{J_1} \exp\mathcal{R}\rho(z)\,|dz| \le (4d)^{-1/2}\exp\mathcal{R}\rho(z_0), \tag{5.2'}$$

又因 $|b - z_0| = |y_0|/\sqrt2$,

$$\mathcal{R}\rho(b) \le -(2\pi d)y_0^2 + \mathcal{R}\rho(z_0)。 \tag{5.3'}$$

现在证明可取 $d = \tfrac13$。在 J₁ 上(新记号)$x_0 + y_0 = -x_1 - y_1$、$x_0 - y_0 = x_1 - y_1$,由此(中间代数步骤残损)可得 $(y-x_1)(x-y_1) = (x+y_1)^2 = |z_1|^2 + 2xy_1$。又 $\bar{z}_1/z = (x_1x + yy_1)/|z|^2$ 而 $|zz_1| \ge \Im(z\bar{z}_1) = y_1x + xy_1$。于是 $|z_1|^2\Im(\bar{z}_1/z) = y_1x + xy_1 - |z_1|^2 - 2xy_1 \le |zz_1| - |z|^2$,故 $\Im(\bar{z}_1/z) \le \ldots \le \tfrac13$,从而 $\Im((z-z_1)/z) \ge \tfrac13$。〔译注13〕

〔31〕旧记号:$z_0\bar{z}_1 = -ir$,故可写 $z_0 = a\exp(-i\alpha)$、$\bar{z}_1 = b\exp(i\alpha)$,其中 $ab = t$、$0 < \alpha < \tfrac12\pi$。现在 $z_0 + \bar{z}_1 = re$,故 $a\cos\alpha - b\cos\alpha - a\sin\alpha - b\sin\alpha = 0$。于是 $a^2\cos^2\alpha/t = \cos^2\alpha(\cos\alpha + \sin\alpha)/(\cos\alpha - \sin\alpha) > 1$,即 $x_0^2 > t$。

〔32〕新记号下 $\tau < x^2 < \ldots$,故有 $\mathcal{R}_0\rho'(z) < -2\pi y_0 - \sqrt2\pi K$,它等于 $-2\pi y_1$,因为 $z_0 - z_1 = -\bar{z}_1 - \bar{z} = r$,从而 $y_1 - y = k/\sqrt2$。(此注多处残损。)

〔33〕第二处出现的 $\mathcal{R}\rho(z)$ 应为 $\mathcal{R}\rho(b)$。

〔34〕这由乘积公式 $\sin(\pi z) = \pi z\prod(1 - z^2/n^2)$ 以及在 J′ 与 J₂ 上 $y \le x$ 的事实得出。

〔35〕(5.7)、(5.8) 的另一途径如下((5.8) 中 b 应为 b′)。旧记号:$x_0 + x_1 + y_0 + y_1 = 0$;直线 J′ 的方程为 $y - y_0 = x - x_0$;又因 $z_0z_1$ 实,$x_0y_1 + x_1y_0 = 0$。于是与注〔30〕同样的三个方程,故得 $|z_1|^2\ldots = y_1x + xy_1 - |z_1|^2 - 2xy_1$。写 $x = x_0 + \xi$、$y = y_0 + \eta$,则 $|z|^2\Im(\bar{z}_1/z) = (x+y)(-x_1-y_1)$。当 $z = b$ 时 $x = x_0 - \tfrac12y_0$,故 $\xi = -\tfrac12y_0$、$-x_1 - y_1 = \xi + x_0 + y_0 \ge x + y > 0$,且 $x + y = -x_0 - y_0 < 0$。故 $\bar{z}_1/z < 0$ 而 $(z-z_1)/z > 1$。如前,在新记号下推得

$$\int \exp\rho(z)\,|dz| \le \exp(\rho(z_0)), \tag{5.7'}$$

以及

$$\mathcal{R}\rho(b) \le -\pi y_0^2 + \rho(z_0)。 \tag{5.8'}$$

〔36〕对 J₁ 上的 z 有 $z = b' - l\exp(i\theta)$,$\theta = \arg z$。故 $dz/dl = z/|z|$。

〔37〕写 $b' = x' + iy‘$ 并令 $F(z) = (-2\pi iz(z - t/z)/|z|)$。现在 $z/|z| = b'/|b’|$,而 $F(z) = 4\pi xy/|z| \le 4\pi x'y'/|b'| = F(b')$。

〔38〕(5.10) 的另一途径如下。用旧记号,置 $E = -2\pi i(b'-z_0)(b'-z_1)/|b'|$。现在 $x_0 + x_1 + y_0 + y_1 = 0$、$x_0y_1 + x_1y_0 = 0$,且 $b' = z_0 - \tfrac12y_0(1+i)$。故 $E = (\cdots) = (\cdots)$,其中 $s = x_0/y_0$。因 $s > 0$,有 $\eta(E) \le -\pi y_0\sqrt2$,或用新记号

$$\mathcal{R}(E) \le -\sqrt2\pi y_1。 \tag{5.10'}$$

〔39〕J₁ 可换成 J′,但正如第 191 页将看到的,J′ 已是我们所需要的全部。

〔40〕在 J 上我们有 $\Re\rho(z) \le -\alpha/l + \Re\rho(b')$,其中 $\alpha = \sqrt2\,y\sin\gamma$。特别地取 $z = b'$。回忆 $|b'| \ge |z_0|$(据注〔27〕),式 (5.12) 随之得出。

〔41〕$J' \subset J_1$ 且 (5.10′) 在 J₂ 上成立。在 J′ 上 $z = r\exp(i(\alpha - \theta))$,$0 \le \theta \le 2\alpha + \tfrac12\pi$,$c = r\exp(i\alpha)$。故 $dz/dl = -\bar{z}_1/r$。用旧记号的 $x_0+x_1+y_0+y_1=0$、$x_0y_1+x_1y_0=0$,得 $\mathcal{R}\rho'(z)dz/dl = 2\pi[(x_0-y_0)(x^2-y^2)+2x_0y_0(x+y)-(x^2+y^2)(x_0+y_0)]/r(x_0-y_0)$。现 $r = |c| \le |z_0|$、$x^2-y^2 \le r^2$、$x+y \le \sqrt2 r$,故 $\rho'(z)dz/dl \le \ldots \le -\pi|z_0|$(新记号下亦然)。(中间步骤残损。)

〔42–44〕(三则注释的公式在此整段排印倒置,无法复原;仅末句可辨:)因为 $|b| \le |z|$。〔译注13〕

〔45〕(接上注所在页)在 J 从 c 到 $\tfrac12 c\lambda\exp(-i\pi)$ 的部分上有 $|y| \ge |c| \ge x \ge |c|/\sqrt2$,而在 J′ 其余部分上 $y \le -|c|/\sqrt2$。在前一部分,$|\sin(\pi z)| \ge \cdots$(公式残损,含 $\sin\arg\xi_0$);在后一部分,$|\sin(\pi z)| \ge |\sinh(\pi y)| = \sinh(-\pi y) \ge \sinh(\pi|c|/\sqrt2) \ge \pi|c|/\sqrt2\,\sin\arg\xi_0$。

〔46〕表达式 $-\pi rc\varepsilon(\xi_0 - 2\mu) + 2\pi\bar{t}\arg\xi_0$ 等于 $\sqrt2\pi K\mu + \mathcal{R}\rho(z_0)$。

〔47〕类似地,$-\pi\eta(2\mu - \xi) + 2\pi\bar{t}\arg\xi = -\sqrt2\pi\mu + \mathcal{R}(z)$。

〔48〕第一句应为 $\sqrt2\,\Re e\,\xi_0 > 1$。要得到这些结果,只须用 ξ 满足 $\xi^2 + \omega\xi - 1 = 0$,故当 ω 小时近似地 $\xi = 1 - \omega/\sqrt2$、$\eta = \omega/\sqrt2 - \omega^2$;类似地 $\xi_0 = 1 + \omega/\sqrt2$、$\eta_0 = -\omega/\sqrt2 - \omega^2$。

为后文记住以下各条:$|S| \le 1$;$|z_0| = \bar{t}^{1/2}|\xi| > 0.81\bar{t}^{1/2}$;$y_0 = \bar{t}^{1/2}\eta_0$,故 $|y_0| \ge \bar{t}^{1/2}/\sqrt2$;$y_1 = \bar{t}^{1/2}\eta_1 > \bar{t}^{1/2}(0.29)\omega = 0.29Kc$;$\tan\arg\xi = \omega/\sqrt2 + O(\omega^2)$,故 $\arg\xi = \omega/\sqrt2$ 而 $\operatorname{cosech}\arg\xi = \sqrt2/\omega = (Kc/\sqrt2)^{-1}\cdot 2\pi^{1/2}$。(末一式残损。)

〔49〕在 (5.20) 最后一行,$k/\sqrt2$ 的首次出现应为 $(c/\sqrt2)^{-1}$。要得到 (5.20),用上一注的结果,再用 $\exp(-\tfrac12 nt)$ 可忽略及 $\Delta = \min(\tfrac12, \ldots)$。

〔50〕$\bar{z}_0 + z_0 = z_0 - z_1 = \bar{t}^{1/2}(\xi_0 - \xi_1) = \bar{t}^{1/2}(-i\omega^2 + 4)^{1/2}$。

〔51〕由于 $0 < \arg\xi < \tfrac12\pi$,第一句显然。当 $\omega \to 0$ 时 $2\xi = -\omega\varepsilon + (\omega^2\varepsilon^2 + 4)^{1/2}$,故 $\xi \sim 1 - \tfrac12\omega\varepsilon$。于是 $\omega^{-1}\arg\xi \to 1/(2\sqrt2)$(数字经 OCR,存疑),而 $\mu_0 \sim \bar{t}^{1/2}$。

〔52〕当 $\omega \to 0$ 时 $\tfrac12 + i/\omega^2 \sim i/\varepsilon^2$,$\sigma^{-1}\arg \to 1/(2\sqrt2)$(据注〔51〕),而 $1 - \Re/\varrho + 1/(\sqrt2\omega) \sim 1$。(符号残损。)

〔53〕为证表达式不小于 $\tfrac12$,可如下进行。由二次方程有 $\xi = \tfrac12\omega\varepsilon E$,其中 $E = -1 + (1 + 4i/\omega^2)^{1/2}$。置 $A = 4/\omega^2$、$a+ib = (1+Ai)^{1/2}$、$D = (1+x^2)^{1/2}$、$\delta = D - 1$。则求得 $\tan\arg E = ((\delta+2)i/2 + \sqrt2)/ai/2 = W$,且 $\mathcal{R}(\tfrac12 + i/\varepsilon^2)^{1/2} = \tfrac12(1+\tfrac12\delta)^{1/2}$。要证的是

$$1 - (1+\delta)^{1/2} + (\delta^2+2\delta)^{1/2}(-\tfrac12\pi + \arg E) \ge \tfrac12 。$$

现在 $\tan(\arg E - \tfrac12\pi) = (W-1)/(W+1)$,而 $\alpha = 8W^2/(W^2-1)^2$,故只须证(一行倒置残损)。这是因为该表达式的导数为正(因 W > 1)且在 W = 1 处取值 0。

〔54〕$\tfrac12 K \ge \mu_0 - \xi = K - \Re(z_0 - \mu_0)$。

〔55〕回忆 $A(\mu_0) = B(\mu_0)$。要看出 $A(\mu_0) = \tfrac12\pi r^2$,用(公式残损)…… $\pi KR\,\Im(z_0+z_1) = \pi K^2$。

〔56〕$\Re e(z_0 - \mu)$ 是 z₀ 到直线 P 的距离,即 $d(J', P)$。(其后一句残损。)我们需要(一组不等式,残损):

$$4Kc > \sqrt{(\mu - \mu_0)} > \ldots$$

〔57〕左端应为 $\sum|h(p-k)|$,即 $\sum u_k$(或者等价地把 $u_k$ 定义为 $u_k = |h(p_k)|$)。另外 $\sqrt2\pi(K+1)/k$ 应为 $-\sqrt2\pi(K+1)/k$。

我们设 K 为正。为得此不等式,注意 $|p_{-k}|^2 > \mu^2$。又令 $n = -\pi k/(r\sqrt2)$、$\eta = -\pi(K+1)/(c\sqrt2)$,注意 $|2i\sin(\pi p_{-k})| \ge e^n - e^\eta \ge (1-e^{2\eta})/e^\eta$。

〔58〕令 $n = -\pi(K+1)/(r\sqrt2)$。则待证不等式化为(公式残损)。分母至多 $e^n + e^{-n}$,且由于

$$e^n(1-e^{2\eta})(e^n+e^{-n}) = 1 - e^{4\eta} < 1,$$

只须证 $|p_{-k-1}| < \mu$。这当且仅当 $K + 1 < \sqrt2 r\mu$ 时成立。(*) 现在 $\Im p_{-k-1} < \mu\theta_0$,即 $-\theta_0\mu r\sqrt2 < K+1$。又有 $-\theta_0 < 1$,因为 $(1+\theta_0)^2 + \theta_0^2)(1+2\theta_0) - \alpha$ 在 $\theta_0 = -1$ 时为负。所以只要 $2ru(1+\theta_0) > 1$,就能选到满足 (*) 的整数 K。另一种办法:若愿意假定 $K + 1 > ru/2$,则可避开 (*),因为那样将有 $|p_{-k}| \ge |p_{-k-1}|$,即使删去 $2\theta_0/2$ 这一项不等式也成立。

〔59〕分析类似,但现在显然 $|p_K| \ge |p_{K'+1}|$。一行公式倒置残损。$-(K+1)/c\sqrt2 = \Im p_{-k-1} < \mu\theta_0$,其中 $(1+\theta)^2 + \theta^2)(1+2\theta) - \alpha = 0$。(设 $0 < \theta$;若 $\theta > 0$,则 K 与 K′ 的角色互换。)设 K 是满足此条件的最大整数并定义 $K' = K$。当 $\omega = kt^{-1/2}$ 小时 $\mu \sim t^{-1/2}$(应为 $\bar{t}^{1/2}$),故 $\alpha = t/\mu^2 \sim 1$,从而 $\theta \sim \theta_0$。于是 $E \sim \theta_0(1+i)$,故 E 很小。(其后两行残损。)

〔60〕正文中 $u_k$ 的近似表达式应乘以 $(\mu/\sqrt2)^{-1}$。

由注〔59〕,$p_{-K-1} \sim \mu(1 + \theta(1+i)) = z$。现在

$$|h(p_{-K-1})| \sim |h(z)| = |\exp i\pi z^2 - i|\cdot|z^{-s}|/|2i\sin(\pi z)| 。$$

现在 $|z|^2 \ge \mu^2$ 故 $|z^{-s}| \le (\mu/\sqrt2)^{-1}$。其次

$$|\exp(i\pi z^2)| = \exp(-2\pi\mu^2\theta(1+\theta)),\qquad |z^{-i}| = \exp(t\arg z),$$

而 $\tan\arg z = \theta/(1+\theta) \sim \theta - \theta^2$,故

$$|\exp(i\pi z^2)z^{-i}| \sim \exp(2\pi\mu^2\theta(-1-\theta+\alpha-\alpha\theta)) \sim \exp(-4\pi\mu^2\theta^2) = \exp(-(K+1)^2\cdots)$$

现在 $|2i\sin(\pi z)| \ge |e^n - e^{-n}|$,$n = \pi\mu\theta$,故须假设(一行残损)才能用常数控制 $|2i\sin(\pi z)|^{-1}$。对 $|h(p_{K'+1})|$ 类似(把 θ 换成 $-\theta$)。

〔61〕我们有 $\alpha = t/\mu^2$、$\mu \to K/\sqrt2$、$\alpha = 8/\omega^2$、$\theta \to -\theta$。现在 $-(K+1)/k\sqrt2 = \Im p_{-K-1} < \mu\theta_0$,可设 K 是满足此不等式的最小整数。又有(一行倒置残损)

$$\Re p_{-K-1} = \mu - \frac{K}{\sqrt2} > 0,\quad(k > 2)$$

(符号残损)。故 $p_{-k-1}$ 在第四象限,从而 $|p_{-k-1}| < 1$。因子 $2i\sin(\pi z)$ 可如注〔60〕忽略,因为我们现在有 $|\pi\mu\theta| \sim \pi K/4\sqrt2 \ge c > 0$。

刚才的论证对 $p_{K'+1}$ 行不通,但要界定 $|h(p_{K'+1})|$,用 $\Phi(p_{K'+1}) \le \Phi(p_{-k})$,其中 $\Phi(z) = \exp(i\pi z^2)z^{-i}$;这是因为 $\mu\theta \sim -\mu\theta_1 < 0$ 故 $\Im p_{-k-1} < \mu\theta < \Im p_{-k} \le \Im p_{K'+1}$。正弦因子可忽略,而 $|p_{K'+1}| \le (\mu/\sqrt2)^{-1}$。

〔62〕根是 $u_1 = -K/r$ 与 $u_2 = K'/k$,故 $\Delta = u_2 - u_1 = (K'+K)/K \sim (K'+K+1)/K = \bar{t}/K$,即 $\bar{t} \sim K^2$(残损)。

〔63〕取 $K = K' = 1$。现在 $\alpha = t/\mu^2 = 1$ 故 $\theta = 0$。K 与 K′ 显然满足各自的定义条件。又 $\omega = K\bar{t}^{-1/2} \le \tfrac12$,故 (5.20) 可用。由 (5.20),$|R| < at^{-1/4} + bt^{1/2}\exp(-ct^{1/2})$,$a, b, c$ 为正常数,故 t 充分大时 $|R| < a't^{-1/4}$。

我们看到误差 $|R^*|$ 形如 $cu^{-\alpha} = ct^{-1/4}$,其中 c 是 $k, K, K'$ 的函数,故此时 c 是常数。

剩下考虑在级数 $\sum r^{-s}F_r$ 中把因子 $F_r = (1-\exp E_r)^{-1}$($E_r = 2rure(r-\mu)$)换成 0 或 1 所产生的误差。具体地,把 $F_1, \ldots, F_{m-1}$ 换成 1,把 $F_{m+2}, F_{m+3}, \ldots$ 换成 0,其中 $m < \mu < m+1$。于是代替 $\sum r^{-s}F_r$ 我们取(公式残损)。我们要证此误差的绝对值至多 $c\mu^{-\alpha} = ct^{-1/4}$(c 为某常数)。误差为

$$\sum_{r=1}^{m-1} r^{-s}(F_r - 1) + \sum_{r=m+2}^{\infty} r^{-s}F_r 。$$

我们证明其绝对值至多 $c\mu^{-\alpha}$,c 只依赖于 x。把第二个和用几何级数放大,并对 $1 \le r \le m-1$ 用 $|F_r - 1| \le (\exp T_r - 1)^{-1}$。有 $|S_1| \le \sum(\exp T_r - 1)^{-1} \le h/(\exp T_h - 1) < cu^{-\alpha}$(部分推导残损)…… $|S_2| < c(h+1)^{-1} < c(\mu)^{-1} = c'\mu^{-\alpha}$。

〔64〕结论是:对此情形,

$$S(s) = \sum_{k=-1}^{m-1} \varepsilon r^{-1}h(p_k) - \sum r^{-s} - m^{-s}F_m - (m+1)^{-s}F_{m+1} + E,$$

其中 $m = [\mu]$,而 $|E| \le 0.0044\,t^{-1/4}$。

若 $t < 1000$,则 $m - 1 \le 11$。

回忆在临界线上

$$\zeta(s)\Gamma(\tfrac12 s)\pi^{-s/2} = -2\,\Re\big(\Gamma(\tfrac12 s)\pi^{-s/2}I(s)\big)。$$

同一结论对不取 $\mu = t^{1/2}$ 而取 $t^{1/2} - \tfrac12 \le \mu \le t^{1/2} + \tfrac12$ 也成立。(因为 $0 < \mu_0/\bar{t}^{1/2} - 1 < \tfrac12\omega^2$,有 $|\mu_0 - \bar{t}^{1/2}| < \omega^2\bar{t}^{1/2} = k^2/\sqrt2$。于是若 $|\mu - t^{1/2}| \le \tfrac12$,则 $|\mu - \mu_0| \le \tfrac12 + k^2/\sqrt2 <$ ……。)这将允许我们选 μ 为整数或半奇数。常数 0.0044 则须增大。

## 矩阵过程中的舍入误差(1948)

### 摘要

A 表示 $n \times n$ 矩阵(所有矩阵都是实的)。本文讨论计算 $A^{-1}$ 与求解 $Ax = b$ 的方法,其中 A 非奇异,b 是 $n \times 1$ 矩阵。L 表示单位下三角矩阵,即对角线以上元素为零而对角线上每个元素为 1;U 表示单位上三角矩阵,D 表示对角矩阵。若 A 的诸顺序主子式非奇异——实际上这一条件不损失一般性——则存在唯一的 L、D、U 使 $A = LDU$。

证明方法本身很重要:所需的矩阵 L、D、U 是通过依次考察表达式

$$a_{11}, a_{12}, \ldots, a_{1n};\ a_{21}, \ldots, a_{2n};\ \ldots;\ a_{nn}$$

而逐步确定的。

文中描述了若干计算 $A^{-1}$ 或求解 $Ax = b$ 的方法,但 singled out 以下三种:

**标准(Gauss)消去法**:对 $Ax = b$ 作行变换把 A 化为上三角形(即 DU)。每次行变换对应于左乘一个矩阵 $J_i$。我们有 $J_n \cdots J_1 A = DU$,且若 $J_n \cdots J_1 b = c$,则 $x = (DU)^{-1}c$。此外 $J_n \cdots J_1$ 具有形式 $L^{-1}$,故 $A = LDU$。

**Jordan 法**:与上一方法类似,只是用行变换把 A 化为单位矩阵。此时 $J_n \cdots J_1 A = I$,故 $J_n \cdots J_1 = A^{-1}$。

**非对称 Cholesky 法**:如定理证明中那样求出 L、D、U;实际上更好的做法是求 L 与 DU。然后求 $L^{-1}$ 与 $(DU)^{-1}$。于是 $A^{-1} = (DU)^{-1}L^{-1}$。

写 $M(A) = \max|a_{ij}|$、$N(A) = (\sum a_{ij}^2)^{1/2}$、$B(A) = \max_{x \ne 0}|Ax|/|x|$。文中给出一个统计性论证,提示 $N(A)N(A^{-1})/n$ 可取作矩阵病态程度的度量;$nM(A)M(A^{-1})$ 也被提出(大概是因为对一切 $n\times n$ 矩阵 X 有 $M(X) \le N(X) \le nM(X)$)。粗略地说,若 A 病态,则系数的小百分比误差会导致 $Ax = b$ 解的大百分比误差。

“若矩阵系数从正态总体中随机选取,我们将得到量级为 $n^{1/2}$ 的 N-条件数,以及约大 $\log n$ 倍的 M-条件数。”然而,“实际问题中出现的矩阵绝非这种意义下的随机矩阵”。〔译注14〕

若 A 是对角线以下元素全等于 $-1$ 的单位下三角 $n \times n$ 矩阵,则 $M(A^{-1}) = 2^{n-1}$,$N(A)N(A^{-1}) = n2^{n-2}$。(此行排印倒置,数字按残迹复原。)〔译注14〕

若 B 是 A 的所谓逆,令 $E = I - AB$。若 $M(E) < 1/n$,则

$$M(B - A^{-1}) \le \frac{nM(B)M(E)}{1 - nM(E)}。$$

**§11 Jordan 法中的误差**

(a) 绝对误差。代替 $J_n \cdots J_1 A = I$,我们有 $J_n[\cdots\{J_2(J_1A + S_1) + S_2\}\cdots] + S_N = I$;代替 $J_n \cdots J_1 = A^{-1}$,我们有

$$J_n[\cdots\{J_2(J_1A + S_1) + S_2\}\cdots] + S_N = E 。$$

于是 E 是算得的 $A^{-1}$ 值。设 $M(S_r) \le \varepsilon$、$M(S‘_r) \le \varepsilon’$($r = 1, \ldots, N$),则得(公式部分残损)

$$M(E - A^{-1}) \le n\varepsilon' + \frac{n(n-1)}{2}\varepsilon M(A^{-1}) + \ldots$$

也给出了以 B-度量与 N-度量表示的误差估计。

(b) 统计误差。令 $F = (E - A^{-1})_{ij}$($i, j$ 固定)。设 $S_r$ 的每个元素是均值为零、标准差为 σ 的随机变量,$S‘_r$ 同。我们求得 $F$ 的方差 $\le n^2\sigma^2P + n'^2\sigma^2Q$,其中 P、Q 是 $M(A^{-1})$ 与 n 的多项式(依赖于 $i, j$);这些多项式都显式给出。F 的标准差的首项至多 $nM(A^{-1})^2\sigma$,而 p 为 $O(n^{3/2})$。(末句符号残损。)

**§12 Gauss 消去法中的误差**

这里有误差:(i) 把 A 化为 DU 时:$J_n[\cdots\{J_2(J_1A + S_1) + S_2\}\cdots] + S_N = DU$;(ii) 对 b 作相应的行变换时:$J_n[\cdots\{J_2(J_1b + S‘_1) + S’_2\}\cdots] + S'_N = c$;(iii) 计算 $(DU)^{-1}c$(即 x)时。文中证明,(ii)、(iii) 之下的误差远小于 (i) 之下的误差。由 (i)、(ii) 我们得到

$$|\text{x}_m \text{的误差}| \le O(n^2)M(A^{-1})\varepsilon' + O(n^4)M(A^{-1})^2\varepsilon M(b),$$

其中 $x_m$ 是向量 x 的第 m 个坐标。

**§13 非对称 Cholesky 法中的误差**

令 $W = DU$。设 L、W 的算得值为 $L^*, W^*$;$L^{*-1}, W^{*-1}$ 的算得值为 K、V;VK 的算得值为 E,于是 E 又是 $A^{-1}$ 的算得值。则 $L^*W^* = A - S$、$L^*K = I - S'$、$VW^* = I - S''$ 且 $VK = E - S'''$。设 $M(S) < \varepsilon$、$M(S’) < \varepsilon‘$、$M(S’‘) < \varepsilon’‘$、$M(S’'‘) < \varepsilon’'‘$。则可证明 $M(E - A^{-1}) \le n^2\varepsilon M(A^{-1})^2 + n\varepsilon’ M(A^{-1}) + \varepsilon''‘$。(公式一行倒置,按残迹复原。)

这提示此法优于 Jordan 法或 Gauss 法。

总结论是:用所考虑的三种方法计算 $A^{-1}$ 或求解 $Ax = b$,误差的指数式积累“并非必然”发生。

BODEWIG(1949)的一篇评论对图灵论文中的一两点提出了批评。

### 注释

〔1〕本文中所有矩阵都是实的。图灵只在给定 A 非奇异的情形下关心求解 $Ax = b$。

〔2〕第二个方程中的负号应删去;该方程由 $x = A^{-1}Ax$、$x_j = \sum_{j,k}(A^{-1})_{ju}a_{jk}x_k$ 得出。(下标残损。)

〔3〕若 A 非奇异,则对其行作适当置换后,A 的诸主子式非奇异。故该条件并无实质限制。

〔4〕存在这一定理的更优雅证明,但这无关宏旨:重要的是这种证明的实际方法在后面有用。想法是依次考察表达式 $a_{11}, a_{12}, \ldots, a_{1n}, a_{21}, \ldots, a_{2n}, \ldots, a_{nn}$。

〔5〕此处应为:“现在假设当 $i < i_0$ 时我们已求得 $l_{ij}$、$u_{ij}$、$d_i$ 的值。”

〔6〕$J_i$ 是单位下三角矩阵,且仅在第 i 列上不同于 I。令 $A' = I + \sum_{r=1}^n(I - J_r)$。则对 A′ 施加曾施加于 A 的同样行变换就把 A′ 化为 I。故 $J_{n-i+1}\cdots J_1A' = I$ 而 $A' = L$。

〔7〕乘法共有 $\sum_{m=2}^n 2(m-1)(m+2)$ 次,其中涉及 b 的有 $\sum_{m=2}^n(m-1)$ 次。

〔8〕把诸方程记为 (1)–(5)。我们对 $q \ne i$ 有 $(J_i - I)_{pq} = 0$,对 $p \le i$ 有 $(J_i - I)_{pq} = 0$,且 $\bar{A}^{-1} - A^{-1} = (J_i - I)A^{-1}$。于是……若 $i \le r$ 则 $(J_i - I)A^{-1} = 0$;若 $i > r$ 则等于 $(J_i)_{ri}A_{i+1}^{-1}\cdots$,这就证明了 (1)。其次,若 $j \le r$ 且 $i > j$ 则 $A_{ij} = 0$,故 $i > r$ 时……这就证明了 $i > r$ 情形的 (2)。若 $i > r$,则 $\sum_s (J_s)_{is}A_s^{-1} = \cdots = A^{-1} - A_{ij}$,证明 (3)。(其后数行高度残损:)同一表达式 $\bar{A}^{-1} - A_{ij}$ 等于 $\sum(J_s - I)_{is}A_s^{-1}$(因 $A_s^{-1} = \bar{A}_s^{-1}$)。因此 (4) 看来不对,应代之以刚给出的备选方程之一。顺带注意:$\bar{\bar{A}}$ 不存在。令 $i \ge r$。我们有 $A_{i+1}^{-1} - A_{ir}^{-1} = \sum A^{-1} - A^{-1} = \sum(J_s)_{is}A_s^{-1}$,故

$$A_{i+1}^{-1} = A_{ir}^{-1} + \sum_{s=1}^{r-1}(J_s)_{is}A_s^{-1}。 \tag{6}$$

现在 (5) 由 (6) 与 (2) 得出;而且 (5) 中两处 $A_s^{-1}$ 都可换成 $\bar{A}^{-1}$(这多半才是原意)。

〔9〕我们有 $A‘ = (J_i)_{ik}A_k$。当 $k \ne r$:若 $i = r$ 则 $(J_i)_{ik}A_k = 0$;若 $i \ne r$ 则 $= \bar{A}^{-1}$。于是我们有

$$A' = \begin{cases} A' + (J_i)_{ri}\bar{A}', & i \ne r,\\ (J_i)_{ri}\bar{A}'', & i = r,\end{cases}$$

也有 $A’; = (J_i)_{ri}\bar{A}'^{-1}$。把“A”处处换成“X”,这些结果仍真。令 $i \ne r$。取 $j = r$ 得 $A' = \bar{A}'' + (J_i)_{ir}A/\bar{r}^{-1}$,但因 $i \ne r$ 有 $A‘_r = 0$,故 $(J_i)_{ir} = -\bar{A}^{-1}/A_{r-1}^{-1}$,$i \ne r$。(多处残损。)

〔10〕此方程附带条件 $i \ne r$。

〔11〕我们来证 M 存在。因 A 非奇异,$\bar{A}^*A$ 正定,故 $\bar{A}^*A = LDU$(某组 L、D、U)。于是 $LDU = \bar{U}^*\bar{D}^*\bar{L}^*$,由唯一性 $\bar{L} = \bar{U}^*$。从而 $\bar{D} = \bar{N}^*\bar{A}^*A\bar{N}$,其中 $\bar{N} = \bar{U}^{-1}$。$\bar{D}$ 正定故其元素非负,可写 $\bar{D} = D'^2$。则 $M = ND'^{-1}$ 满足要求。

〔12〕令 $B = \bar{A}^*A$。由 (1,1) 元得 $m_{11}^2 = b_{11}$(原文如此),故知 $m_{11}$ 从而 M 的第一列。设已知 M 的前 r 列。则知 $\bar{M}^*$ 的前 r 行,从而 $M^*B$ 的前 r 行。由第 $(i, r+1)$ 元得 $\sum(M^*B)_{ix}M_{k,r+1} = 0$($i = 1, \ldots, r$),故 $M_{i,r+1}$($i = 1, \ldots, r+1$)在一个乘法因子范围内已知。第 $(r+1, r+1)$ 元给出确定该因子的方程。

〔13〕$N(XY)^2 = \sum_{ik}(\sum_k x_{ik}y_{kj})^2 \le \sum_{ik}\sum_k x^2y^2 = \sum_{jk}xy = N(X)^2N(Y)$,证明 (7.6)。方程 (7.7)、(7.8) 平凡。在 $B(A)$ 的定义中取 x 为单位矩阵的第 q 列,得 $(\sum_i a_{iq}^2)^{1/2} \le B(A)$。故 $|a_{pq}| \le B(A)$,(7.9) 随之得出。平方并对 q 求和得 $N(A)^2 \le nB(A)^2$,证明 (7.12)。其次,

$$|Ax|^2 = (\sum a_{ik}x_k)^2 \le (\sum a_{ik}^2)(\sum x_k^2),$$

故 $B(A)^2 \le \sum_{ik}a_{ik}^2 = N(A)$,证明 (7.11)。

〔14〕由 (7.7),$B(A) \le nM(A)$。这与 (7.10) 不是一回事,而 (7.10) 可由例子看出是错的(例矩阵在 OCR 中缺失)。在 $B(A)$ 定义中取 $x = (1\ 1)^T$,得 $\sqrt2 \le B(A)$。若 (7.10) 正确将有 $\sqrt2 \le \sqrt2$(原文如此,疑为不等号方向之误)。

〔15〕令 $B = A^{-1} + A^{-1}SA^{-1}$。由于在一阶近似下 $(A-S)B = I = B(A-S)$,可知 $(A-S)^{-1}$ 近似于 B。乘以 b 即见 x 近似于 $x_0 + A^{-1}Sx_0$。

〔16〕R.M.S. 指“均方根”即标准差。也可以作非统计论证:$|x-x_0|/|x_0| = |A^{-1}Sx_0|/|x_0| \le B(A^{-1}S)$,它不超过 $B(A)B(A^{-1})B(S)/B(A)$(或类似组合),这提示用 $B(A)B(A^{-1})$ 或 $N(A)N(A^{-1})$ 作度量。(一行倒置残损。)

〔17〕联系后文结果(§11、12、13),或许值得注意 $M(A^{-1}) = M(\overline{B - A^{-1}} + B) \le nM(B)M(E)/(1-nM(E)) + M(B) = M(B)/(1-nM(E))$,类似地 $M(A^{-1}) \le M(\bar{B})/(1-n^2\{M(E)\}^2)$。

〔18〕此表达式当 $i \ne r$ 时等于 A(原文如此);下面含 X 的表达式类似。

〔19〕(一行完全倒置残损,大意:由于 $I = X_rV$ 必须成立,可得 $X_r = \cdots$,从而得 (11.3)。)〔译注14〕

〔20〕考虑性质“在第 r 列之后的所有列上等于 I”。具有该性质的两矩阵之积仍具该性质。$J_1, \ldots, J_r$ 都有此性质,故 $X_r$ 亦然。

〔21〕(倒置残损,大意:)$X_{r+1}(A + S_{r+1}X_{r+1}^{-1}) = X_rD'_r + I_r = I_{r+1} = I$。

〔22〕右端的负号应删去;并且 (11.7) 中 $-S‘$ 应为 $+S’$。

〔23〕设 C 表示把前 r 列改为零后的 $A^{-1}$。则(倒置残损:)$M((A^{-1}, S'_r(I-D'_r))) \ge M(C)$。

〔24〕$|(I - I_r)X| = (x_{r+1}^2 + \cdots + x_n^2)^{1/2} \le |X|$,故 $B(I - I_r) \le 1$;同样 $B(I_r) \le 1$。现在 $B(S_r) \le nM(S_r) \le n\varepsilon$(见注〔14〕)且 $B(S‘) \le n\varepsilon’$。故 (11.9) 中 $n^{3/2}$ 应为 $n^2$。

〔25〕$(1-r)/2$ 应为 $(n-r)^{1/2}$。

〔26〕$\sum_{r=1}^{n}(n-r)/2 \le \sum n^{1/2} \le (n+1)^{3/2}$,且 $n(n+1)^{3/2} \le (n+1)^{5/2}$。

〔27〕写(分块矩阵显示式在 OCR 中缺失),其中 X 是 $r \times r$ 的,并把 (11.7) 中其余矩阵也写成类似的分块形式。则有

$$S_r = \begin{pmatrix} 0 & B \\ C & D \end{pmatrix},\qquad S‘ = \begin{pmatrix} \varepsilon & * \\ * & * \end{pmatrix}$$

(块内容残损)。例如 $I_rS_rA^{-1}$ 等于 $\begin{pmatrix} BZBT \\ 0 \end{pmatrix}$ 形的分块。由于 B 有 $n-r$ 列而 Z、T 有 $n-r$ 行,$M(D'_rS_rA^{-1}) \ge (n-r)\varepsilon M(A^{-1})$。照此进行即得 (11.11)。

〔28〕我们有:若 $l \le r$ 则 $(S_r)_{kl} = 0$。现在对满足 $l > r$ 的 r、k、l 求 $(S_r)_{kl}$ 系数的平方和,得 $\Sigma_1 + \Sigma_2$,其中 $\Sigma_1 = \sum(A^{-1})^2$(对使 $i \le r < l$ 的 r、k、l);$\Sigma_2 = \sum(A^{-1})(A^{-1})$(对使 $r < k$、$r < l$ 者)。故 $\Sigma_1 = \sum_{i<l}(A^{-1})_{li}^2$,而 $\Sigma_2 = \sum_{k,l>r}(A^{-1})_{ki}(A^{-1})_{li}\cdots$(后段残损)。这解释了头两个被加项,即图灵方程中 $n^2$ 的系数(不过那里是 K−1 而非 K)。$n‘^2$ 的系数是对满足 $r > j$ 的 r、k 求 $(S’)_ {kj}$ 系数的平方和 $= \sum[(I_r)_{ik} + (A^{-1})_{ik}(I-I_r)_{kk}]^2 = (n+1)-\max(i,j) + \sum_{k>j}(k-j)(A^{-1})_{kj}^2$,与正文表达式略有不同。但由于 $\sum\min(k-1, l-1) = O(n^3)$、$\sum(I-i) = O(n^2)$ 且 $\sum(k-j) = O(n^2)$,仍得 $(A^{-1})_{ij}$ 的 R.M.S. 误差首项为 $n\{M(A^{-1})\}^2E$,其中 $E = O(n^{3/2})$。〔译注14〕

〔29〕这是因为 $n^2$ 的系数是 $O(n^3)$,而 $n‘^2$ 的系数只有 $O(n^2)$;于是误差 $S_r$ 支配误差 $S’$。

〔30〕这来自不等式 (11.8),其中 $\varepsilon‘$ 换成 $\delta’M(A^{-1})$、ε 换成 δM(A)。

〔31〕要知道这一点,回忆 (11.8) 的证明即可。

〔32〕这里应为 $s'_1, s'_2, \ldots, s'_n$。

〔33〕$J_{n-1}\cdots J_2J_1A$ 是上三角(=DU)。定义 $J_n = I$。则 $J_n\cdots J_1A = DU$ 且 $X_r = J_n\cdots J_r = L^{-1}$。令 $J_n\cdots J_1b = c$,则 $(DU)^{-1}c = x$,$c = b + \sum X_r^{-1}(s'_r + S_rx)$(倒置行复原),且 $s'_1 + s_2 + \cdots = F$。误差是 $E^{-1}F - A^{-1}b$。现在 $X_r(A + \sum X_r^{-1}S_r) = E$,对 F 类似,故误差为 $(A+\sum X_r^{-1}S_r)^{-1}(b + \sum X_r^{-1}s'_r) - A^{-1}b$。若 G 小,$(A+G)^{-1} \approx A^{-1} - A^{-1}GA^{-1}$,故误差近似为

$$A^{-1}\sum X_r^{-1}(s'_r - S_rA^{-1}b), \tag{*}$$

它等于 $U^{-1}D^{-1}X_r\sum X_r^{-1}(s'_r - S_rU^{-1}D^{-1}x_rb)$。

〔34〕该方程用类似于注〔6〕的方法证明。由于 $M(J_i) = 1$($i = 1, \ldots, n$),有 $M(X_r) = 1$。

〔35〕这由注〔33〕的 (*) 得出。下一行缺括号。

〔36〕该不等式右端应除以 n。

〔37〕这里应为 $d_m^{-1}[(L^{-1}b)_m - \sum_{i>m}(DU)_{mi}x_i]$。

〔38〕设 $x_m$ 的算得值为 $x'_m$。则 $x‘_m = d_m^{-1}[(L^{-1}b)_m - \sum_{i>m}(DU)_{mi}x’_i] + t_m = d_m^{-1}[(L^{-1}b + Dt)_m - \sum_{i>m}(DU)_{mi}x‘_i]$。也就是说 $DUx’ = L^{-1}b + Dt$。故 $DU(x' - U^{-1}t) = L^{-1}b$,x 的误差是 $U^{-1}t$。

〔39〕$L = X_n^{-1}$ 故 $M(L) = 1$。现在 $(A^{-1}LDt)_{mn} = \sum_{k,p}(A^{-1})_{mk}L_{kp}d_{pp}t_p$,若 $|d_{pp}t_p| < \varepsilon$,其模至多 $\sum_{k,p}M(A^{-1})\varepsilon \le n^2\varepsilon M(A^{-1})$。

〔40〕(n,n) 元是 $d_{nn}\sum_i(A^{-1})_{ni}\sum_j(X_r^{-1}S_r)_{jn}$。现在 $(X_r^{-1}S_r)_{in} = \sum_k(X_r^{-1})_{ik}(S_r)_{kn} \le n\delta$,故 (n,n) 元绝对值不超过 $n^2d_{nn}M(A^{-1})\delta$(而非 $n^3$)。

〔41〕$(L^{-1})_{ij} = \sum(J_r^{-1})_{i,r_1}(J_2^{-1})_{r_1,r_2}\cdots(J_n^{-1})_{r_{n-1},j}$。每个 J 的每行至多有两个非零元。故 r₁ 至多两种选择;每种之下 r₂ 至多两种选择,依此类推。于是非零被加项至多 $2^{n-1}$ 个。因 $M(J_s^{-1}) = 1$,有 $|(L^{-1})_{ij}| \le 2^{n-1}$,即 $M(L^{-1}) \le 2^{n-1}$。

〔42〕给出的论证可以重述如下。设 L、W 的算得值为 $L^*, W^*$;$L^{*-1}, W^{*-1}$ 的算得值为 K、V;VK 的算得值为 J。则 $L^*W^* = A - S$、$L^*K = I - S'$、$VW^* = I - S''$ 且 $VK = J - S'''$。$A^{-1}$ 算得值的误差为

$$J - A^{-1} = (I-S''')(A-S)^{-1}(I-S') + S''' - A^{-1} = \ldots$$

(展开式一行倒置残损)到一阶为止。设 $M(S) < \varepsilon$、$M(S') < \varepsilon‘$、$M(S’‘) < \varepsilon’‘$、$M(S’'‘) < \varepsilon’''$。则误差至多

$$n^2\varepsilon M(A^{-1})^2 + 2n\varepsilon'M(A^{-1}) + \varepsilon'''。$$

## 具有消去律的半群中的字问题(1950)

### 摘要

**具有消去律的半群**是带结合乘法并满足消去律 $ab = ac \Rightarrow b = c$、$ba = ca \Rightarrow b = c$ 的集合。(原式一行倒置。)

设 Σ 是一个符号集。一个 **Σ-字**(简称**字**)是由 Σ 中符号组成的有限序列。两个字的积是把一者接在另一者之后写出。

一个**呈现**(presentation)由符号集 Σ 和 Σ-字的有序对之集 D 组成。称两个字 U、V **等价**,如果存在字的有序对的序列 $P_1, \ldots, P_N$,其中 $P_1 = (U, V)$,且每个 $P_i$ 或者 (i) 具有 $(W, W)$ 的形式、或属于 D、或由某个先前的 $P_j$ 经运算之一得出:

$$(A, B) \to (B, A),\qquad (A, B) \ne (As, Bs),\qquad (A, B) \ne (Sa, sB),$$

其中 $s \in \Sigma$,或者 (ii) 譬如是 $(A, C)$,而先前有两对 $(A, B)$、$(B, C)$(某 B)。

容易验证:全体字模此等价关系所得之集是一个具有消去律的半群,记作 $\operatorname{sc}(\Sigma, D)$。称 $(\Sigma, D)$ 的**字问题可解**,如果存在一个算法,能对任意两个字判定它们是否等价。(显然,两字等价当且仅当它们在 $\operatorname{sc}(\Sigma, D)$ 中对应的类相等。)

**定理 2.** 存在呈现 $(\Sigma, D)$,其中 Σ 与 D 都是有限集,其字问题不可解。

证明归结为以下已知结果:存在一台图灵机 B,使得没有算法能对任意初始完整构形判定 B 最终是否会停机并留下空白带。

构造一个有限呈现 $(\Sigma, D)$ 及映射

$$\Phi_1, \Phi_2\colon (\text{B 的完整构形 } C) \to \text{字},$$

并证明了下面的定理。

**定理 1.** $\Phi_1(C)$ 与 $\Phi_2(C)$ 是等价的字,当且仅当 B 以初始构形 C 出发最终停机且留下空白带。

定理 2 由定理 1 立即得出。

### 注释

〔1〕机器 B 的显式描述见 BOONE(1958)《对图灵〈具有消去律的半群中的字问题〉的分析》,该文重印于本卷。初次阅读图灵此文者,强烈建议在 Boone 文章的指引下阅读。

〔2〕在这些关系的每一个中,从 $O_m$ 到 $T_m$ 之间任何处都不应有逗号。每个逗号应换成附着于前一字母的撇号(prime/dash)。

〔3〕"'h,'" 应为 "'nn'"。

〔4〕"Φ₁" 应读作 "Φ₂"。

〔5〕"'v,'" 在此处及两行之后应为 "'r,'"。

〔6〕(一行完全残损,无法复原。)

〔7〕归纳步骤的另一论证如下。我们有 $\gamma(H_{r-1}) = C_{r-1} = AVB$。现在 U 具有 rs 或 sl 形式之一(下标省略)。故对某 X、Y,$H_{r-1}$ 分别是 $XuT_kY$ 或 $XjSuY$。这里 T 是 t 上的字,S 是 σ 上的字。又两种情形都有 $\gamma(X) = A$、$\gamma(Y) = B$。

不用关系 (C, D) 的记法,改写 C = D。由交换关系,

$$H_{p-1} = X\varphi_0(T)u_kY\ \text{或}\ Xju_t(S)Y,\quad\text{分别;} = X\varphi_0(T)\varphi_1(U)Y\ \text{或}\ X\varphi_1(U)t(S)Y,\ \text{分别。}$$

设 $H_r = X\alpha(T)o_mP_r(V)t_mY$ 或 $Xo_mP_r(V)t_mt(S)Y$(分别)。则两种情形都有 $H_{r-1} = H_r$,且

$$\gamma(H_r) = \gamma(X)V\gamma(Y) = AVB = C_r 。$$

又因 $H_{r-1}$ 正规,故 $H_r$ 亦正规。(细节多处残损。)

〔8〕从此处起不再给出任何非平凡的编者评注,因为本卷重印的 BOONE(1958)文章已提供一切所需(见注〔1〕)。

〔9〕关于这一记法及引理 5 的说明,见 Boone 的文章。

〔10〕"(AB)" 应读作 "(A,B)"。

〔11〕〔12〕〔13〕见 Boone 的文章。

〔14〕最后一处出现的 "G₆" 应为 "G₄"。

〔15〕"'G₄ G₅ G₆'" 应读作 "'G₄, G₅, G₆'"。

〔16〕"'G,F'" 应为 "'G₂F'"。

〔17〕〔18〕〔19〕〔20〕〔21〕见 Boone 的文章。

## 黎曼泽塔函数的一些计算(1953)

### 摘要

1950 年 6 月,曼彻斯特大学的计算机被用来考察黎曼泽塔函数 $\zeta(s)$($s = \sigma + it$)在

$$2\pi\cdot63^2 \le t \le 2\pi\cdot64^2$$

范围内的零点,希望找到临界线 $\sigma = \tfrac12$ 之外的(非平凡)零点。初步结论是:该区域内 $\zeta(s)$ 的所有零点都是临界线上的单零点。

区间 $1414 \le t \le 1608$ 也作了考察,试图扩展蒂奇马什的工作——他考察过 $0 < t \le 1468$(TITCHMARSH 1936)。由于一个计算错误,这里的结论只是:$0 < t < 1540$ 内临界线之外没有零点。

**第一部分 总论**

图灵首先陈述了蒂奇马什书第十五章一个结果的某个版本,即泽塔函数的一个方程:

**定理 1.** 设 $t \ge 64$,$m = [\sqrt{t}]$,$\sqrt{t} = m + \vartheta$,并令(诸定义式残损)

$$K(t) = \frac{1}{4\pi i}\log\frac{F(\tfrac14 + \pi it)}{F(\tfrac14 - \pi it)} - t\log\sqrt{t}\ (\text{符号残损}),\qquad Z(t) = (\tfrac14 + 2\pi it)\exp(2\pi ic(t)),$$

以及 $K_1(t) = t\log t - (\pi - \ldots)$,$h(\xi) = \dfrac{\cos 2\pi(\xi^2 - \xi - \ldots)}{\cos 2\pi\xi}$。〔译注15〕

则 Z(t) 为实,且

$$Z(t) = 2\sum_{n=1}^{\infty} n^{-1/2}\cos 2n\pi\{t\log n - K(t)\} + (-1)^{m+1}\vartheta^{-1/4}h(\vartheta) + O(1.09\,t^{-3/4}),$$

其中 $O(a)$ 表示绝对值至多为 a 的数。又有 $K(t) = K_1(t) + O(0.006t^{-1})$。

接下来,为便于计算 Z(t),作者想用二次表达式代替 $h(\vartheta)$,并把 m、ϑ 的定义放宽为:$|\sqrt{t} - m - \tfrac12| < 0.53$,$m \in \mathbb{Z}$。

**定理 2.** 若 $|\vartheta - \tfrac12| < \tfrac13$,则 $h(\vartheta) = 0.373 + 2.16(\vartheta - \tfrac12)^2 + O(0.0153)$。若 $|\vartheta - \tfrac12| < 0.53$,则 $h(\vartheta) = 0.373 + 2.16(\vartheta - \tfrac12)^2 + O(0.0243)$。

**定理 3.** 若改按 $|\sqrt{t} - m - \tfrac12| < 0.53$、$m \in \mathbb{Z}$ 定义 m、ϑ,则定理 1 仍成立,误差项换成 $O(1.15\,m^{-3/2})$。

现在设 $N(t)$ 是 $\zeta(\sigma + it)$ 当 $0 < \sigma \le 1$ 时零点的个数(原文如此〔译注15〕)。设 $S(t)$ 为 $\tfrac1\pi\arg\zeta(\tfrac12 + it)$ 的适当定义值。则 $N(t) = 2k(t/2\pi) + 1 + S(t)$(记号残损)。令 $S_1(t) = \int^t S(u)\,du$。

**定理 4.** 设 $t_2 > t_1 > 168\pi$。则

$$S(t_2) - S(t_1) = O\big(2.3 + 0.128\log\tfrac{t_2}{2\pi}\big)。$$

最后一个定理意味着,在某些情形可以精确求出 $N(2\pi t_0)$。

**定理 5.**(陈述中含一组关于 $t_{-R_1}, \ldots, t_0, \ldots, t_{R_2}$ 与常数 $c_r$、$\delta_r$ 的条件及一个双侧不等式;公式排印破碎,大意是:在若干符号条件与相邻点函数值异号的条件之下,$|N(2\pi t_0) - 2\kappa(t_0) - 1|$ 被形如 $\{0.184\log t_0 + 0.0103(\log t_0)^2\}$ 的量控制。)〔译注15〕

作为定理 5 用法的示例,图灵证明:存在 $|t - 551| < 0.05$ 内的数 $t_0$ 使 $N(2\pi t_0) = 1103$。

借助定理 5 可以找到各种数对 $(t_0, t_1)$,使 $\zeta(s)$ 在区域 $t_0 \le t \le t_1$ 中零点个数 $N(t_0) - N(t_1)$ 精确已知。要证明这样一个区域内的所有零点都是直线 $\sigma = \tfrac12$ 上的单零点,可如下进行:对区间内若干点计算 $Z(t/2\pi)$ 的符号,必要时加密取点,直到变号次数等于已知的零点数。若成功,所欲证的结果即得证。

**第二部分 计算**

作者简要描述了曼彻斯特计算机,并陈述了计算 Z(t) 所用的部分实际计算策略。所取的 t 值 $T_0, T_1, T_2, \ldots$ 由一个把 $T_{n+1}$ 用 $T_n$、$\kappa(T_n)$ 表示的简单公式自动给出。该定义保证 $\kappa(t_0)$ 接近整数 p,而 $\kappa(t_n)$ 接近整数 $p+n$。然后在那些使 $Z(t)\cos 2\pi\kappa(t) < 0$ 的点附近考察更多 t 值。

计算方法自然要求 t 不太大。所选范围为 $63^2 \le t \le 64^2$;对此类 t,$m = 63$,计算 Z(t) 的误差小于 0.02。

### 按

LEHMAN(1970)在其论文中沿图灵的方法,给出了定理 4 一个略微修改版本的阐述:

$$\text{若 } t_2 > t_1 > 168\pi,\ \text{则 } |S(t_2) - S(t_1)| \le 1.91 + 0.114\log\tfrac{t_2}{2\pi}。$$

其要点如下。(i) 对图灵的引理 3——确切说,对其略加修改的形式——提供了证明。(ii) 作者发现并改正了图灵引理 9 证明中交换极限次序的一处错误。

### 注释

〔1〕"'-½'" 应读作 "'-¼'"。(OCR 中两符号无法区分。)

〔2〕删去指数中的负号。

〔3〕"'-½'" 换成 "'-¼'"。(同上,OCR 无法区分。)

〔4〕除误差项外,Z(t) 与 κ(t) 的方程以及 Z(t) 为实这一事实,由 TITCHMARSH(1951)之 15.3 得出;图灵的 Z(t) 即 Titchmarsh 的 $Z(2\pi t)$(原文如此),而我们写 $\bar{t} = t/2\pi$。此外 κ(t) 为实。

〔5〕本文几乎完全把 Z(t) 当作实变量 t 的(实值)函数来对待。不过有一处考虑了复的 ζ;在区域 $\Re t > 0$、$|t| \le \tfrac12\pi$ 内 Z(t) 的零点与区域 $0 \le \sigma \le 1$、$t > 0$ 内 ζ 的零点之间有显然的一一对应。

〔6〕这条评语可以这样论证。在图灵的论文 (6) 中,对临界线上的 s 有

$$\zeta(s)\Gamma(s)\pi^{-s/2} = -2\,\Re\big(\Gamma(s)\pi^{-s/2}I(s)\big),$$

其中 $I(s) = -\sum_{n=1}^{m}1/n + \cdots$,而 m 近似于 $t^{1/2}$。令 $B(s) = \Gamma(\tfrac12s)\pi^{-s/2}$。则 $\exp 2\pi i\kappa(t) = lB(s)$,l 为实;这可以直接证明,或如下:$\zeta(s)B(s)$ 为实,$\zeta(s)\exp 2\pi i\kappa(t)$ 亦然,故其商为实。于是图灵 (6) 蕴含 $Z(t) = \zeta(s)/B(s) = -2\,\Re(\exp 2\pi i\kappa(t)(-\sum 1/n + \cdots)) = 2\sum n^{-1/2}\cos 2\pi(t\log n - K(t) + \cdots)$。我没有考察过图灵关于他的论文 (6) 的公式“更精确”的说法(在什么意义上?)。

〔7〕令 $J(\xi) = 0.373 + 2.16(\xi - \tfrac12)^2$,则 $f = h - J$。h 与 J 都关于 $\xi = \tfrac12$ 对称,故 f 亦然。当 $\xi = n$、$15 \le n \le 32$ 时 $f(\xi)$ 很小,从而 $-2 \le n \le 32$ 时亦然。设 $|\xi - \tfrac12| < 0.53$。则存在 n 使 $-2 \le n-1 < n \le 30 < n+1 < n+2 \le 32$(数字残损)。取 $\xi_i = (n + i - 2)$,$i = 1,2,3,4$。为证 $|P(\xi)|$ 小,进行如下:$P(\xi_i) = f(\xi_i) = \eta_i$。令 $d = \ldots$,则 P(ξ) 可写成带一、二、三阶差分 $u_1, u_2, u_3$ 的插值公式(式残损)。由于各 $\eta_i$ 小,各阶差分也小,故有 $|P(\xi)| < |\eta| + 2|u_1| + |u_2| + |u_3|$。

〔8〕"$(-1)^{m-1}$" 应为 "$(-1)^{m}$"(指数形式经 OCR 复原,存疑)。

〔9〕新误差是(公式残损)其中 $E = \xi^2 - 2\xi - \cdots$ 而 $\tfrac12e^2 \le (m-1)^2/(3m+3) + 0.006(m+1)^{-2}$。随后须分 m 偶、m 奇两种情形讨论。

〔10〕$N(t)$ 为奇或偶,视 $Z(t/2\pi)$ 为正或负而定;因为 $\arg Z(t) = \arg(\tfrac14 + 2\pi it) + 2\pi K(t) = \pi(S(2\pi t) + 2K(t)) = \pi(N(2t) - 1)$(记号残损)。故若对给定的 t 已知 $Z(t/2\pi)$ 的符号,则 $N(t)$ 从而 $S(t)$ 在模 2 意义下已知。

〔11〕(本注开头一行缺失:)……平行于 x 轴的线段以及以 $\zeta(s)$ 零点为心的小圆周的一部分。$\log\zeta(s)$ 沿 $y =$ 常数的线段的积分之实部与 log 分支无关,而沿小圆周的积分实部随半径趋于零。

〔12〕我们要用定理 1,故 $0 \le \alpha < 1$。若 $\alpha \ne 0$,则 $h(\xi) < 0.373 + (2.16) + 0.0153$,而 $h(0) = \cos\tfrac12\pi$。故 $h(\xi) < 0.95$,

$$|\zeta(\tfrac12 + 2\pi it)| = |Z(t)| < 2\sum r^{-1/2} + 0.95\,t^{1/4} + 1.09\,t^{-3/4}。$$

〔13〕(缺。)

〔14〕(a) 由级数展开知,若 $\sigma > 1$,则 $|\zeta(s)| \le \zeta(\sigma)$、$|\log\zeta(s)| \le \log\zeta(\sigma)$,但(两个比值式残损)。(b) 从 $1.25 + it$ 到 $\infty$ 的积分意指从 $1.25 + it$ 到 $\infty + it$。

〔15〕指数应为 '$-\sigma + \tfrac12s$'。

〔16〕由引理 2,若 $t \ge 128\pi$,则 $|\zeta(\alpha + it)| < 4(t/2\pi)^{1/4} < 4\cdot1^{1/4}$。故 $|\zeta(\tfrac12 + it)| < 4$。

〔17〕用 $\tan^{-1}x \le x$(对 $x \ge 0$)。

〔18〕对 $\alpha \ge \tfrac12$、$l \ge 1$,我们有 $|\ldots| < 9t^{1/2} = 9(128\pi)^{1/2}$。(左端残损。)

〔19〕Phragmén–Lindelöf 定理的一个适用版本是:若 $\varphi(s) \le M$ 在半直线 $\alpha = \pm c$、$t \ge 0$ 上及线段 $-c \le \alpha \le c$ 上成立,且 $|\varphi(s)| < A\exp(\exp t^\beta)$,其中 $0 < \beta < \pi/2c$、$A > 0$,则在两条半直线与线段围成的无限带形内处处 $|\varphi(s)| \le M$。我们的情形 $c = \tfrac12$;取 β = 1。

〔20〕这里用 $t > 168\pi$。

〔21〕这由 $|\Im\zeta(s)| \le 4(\exp 0.1)(t^2 + (\alpha - \tfrac12)^2)^{\cdots}$ 得出,其中 $a = \ldots$(残损)。

〔22〕需要 $a \ne 0$。

〔23〕作为证明第一部分(化归到实情形)的替代,有如下做法:

$$\int\log\frac{a-z}{a+z}\,dz = \int_0^\infty\log(\cdots)\,dz = F(\alpha, \beta)\ (\text{如此称呼}),$$

其中 $a = \alpha + i\beta$。然后证明 $F(\alpha, \beta) > F(\alpha, 0)$。当 $\alpha \ge \tfrac12$ 时容易,因 $(\alpha + x + \tfrac12)^2 \ge (\alpha - x)^2$。当 $0 < \alpha < \tfrac12$ 时置 $\mu = \tfrac12 - \alpha$,称新的被积函数为 E。把积分区间分成 $[-\tfrac12 - \alpha, 0]$ 两段,此处 $(-\mu)^2 \ge (\mu + \tfrac12)^2$,结果随之得出。

〔24〕在较大的解处,函数 $\psi(a) + k/a$(a 实)取最大值。当 $a \to 1+$ 或 $a \to 1-$ 时它趋于 $k - 2\log 2 > 0$;当 $a \to +\infty$ 时趋于 $\infty$。故只须证此函数在较小解处为正。

〔25〕积分前的符号应改变。

〔26〕设 $\mu > 1$、$x > 0$、$z = x - iux$。则 $\Re z > 0$,但被积函数在 $u = \mu x + ix$ 处有极点,它位于新旧两线之间。然而,若把引理 8 的假设改为 $\Re z > 0$、$\Im z > 0$,则该引理为真,且对后面的应用已经足够。

〔27〕(一行倒置残损,末句可辨:)第三项应换成 1。

〔28〕把 '$-\tfrac12\log\tfrac12t$' 换成 '$-\tfrac12\log\tfrac12t + c$',c 是适当的小数值常数。(见注〔27〕。)

〔29〕该积分等于 $\int w^{-g-1}\log(z/z+1)\,dz$(记号残损),其中 $w = \tfrac12 + it$。由于 $0 < \Re\omega < 1$,可用引理 7。由于 $\Re(k/e) > 0$ 并注意所得级数收敛,得(公式残损)

$$= e_2 - 1.49\big[\Phi_1(\Phi)(w) - \tfrac12\log\pi + \Phi_1(\Phi)(w+1)\big],$$

其中 $e_2 = -1.49\,\Re(-b_1 + 1/(w-1))$。e₂ “小”,因为据 INGHAM(1931)第 58 页 $b_1$ 近似于 $-0.023$,而 $t > 50$。于是由引理 8、引理 3 及不等式 $\tfrac12\log(\tfrac12t^2 + \tfrac12) < \log t/2\pi$ 得到(式残损),其中 $e_3 = (\pi^2\Im(\tfrac12t^2 - \tfrac12))^{-1}$。

〔30〕用这些引理我得到 $S_1(t_2) - S_1(t_1) = O(2.36 + 0.116\log t_2/2\pi)$。

〔31〕右端应是第一个表达式加上 $\tfrac1{2t}$ 乘该积分。

〔32〕假设应作如下改动:定义 $c_r = \kappa_1(t_r)$。(陈述 $\delta_{R_1} = -R_1 = 0$ 是假定而非定义。)把 $N(2\pi t_0) - 2c_0 - 1$ 换成 $N(2\pi t_0) - 2\kappa_1(t_0) - 1$。

〔33〕$2/R_1$ 应为 $2/R_2$(仅此行)。

〔34〕$R_2 - 1$ 应为 $R_2 - 2$。若 $Z(t_r)Z(t_{r+1}) < 0$,则 $Z(t) = 0$,即存在 T 使 $\zeta(\tfrac12 + 2\pi iT) = 0$、$t_r < T < t_{r+1}$;故 $N(2\pi t_{r+1}) \ge N(2\pi t_r) + 1$。

在区间 $(T_{R_2-1}, T_R)$ 内我们只有 $N(2\pi t) \ge N(2\pi T_{R_2-1}) \ge N(2\pi t_0) + (R_2 - 1)$。

证明的下一段中,R 指 $R_2$。

〔35〕右端应减去 $(c_r - C_{R-1})$。因此下一行的 $\sum\delta_r$ 应换成(公式残损)

$$(\textstyle\sum\delta)^{R_2-2} + d_{R_2} - \delta_{R_2-1} + \ldots$$

定理 5 的结论中也作同样替换。

〔36〕0.006 应为 0.012,下一行的 0.003 应为 0.006。若 $D(t) = \kappa(t) - K_1(t)$,则 $|D(t)| \le 0.006t^{-1}$。又 $C_R - c_0 = \tfrac12R_1$,因 $\delta_{R_1} = 0$。

〔37〕特别地,因 $C_8 - C_7 = c_0 + 4 - c_8 = 551 + \tfrac12 - 554.5 > 0$(残损),我们有 $t_8 > t_7$。

〔38〕对下文来说只需 $|N(2\pi t_0) - 2c_0 - 1| < 1.9$。

〔39〕回忆:N(2πt) 为奇或偶,视 Z(t) 为正或负而定。又 $\cos 2\pi\kappa(t_0) = \cos(2\pi(551)) = 1$。

〔40〕$\lambda = 2\kappa(t) - n$,$n \in \mathbb{Z}$(不是 $n - 2\kappa(t)$)。下一行把 κ(t) 换成 2κ(t),使 $|\lambda| < 0.125$。实际上,“$2\kappa(t‘)$ 与整数之差小于 0.125”这一结论只有在忽略一个非常小的量时才真。为使结论成立,把 0.125 换成 0.126(比如说)即可。

〔41〕(i) E 在后文定义。(ii) 这个判别法表述正确吗?$Z(t)$ 的算得值可能远小于 $-E$ 或远大于 $E$,而 H 可能正也可能负(并非分别对应)。四种情形中有两种判别法成立,另两种失效。我怀疑应为 $|Z(t)H(c)| > 0.31E$。(iii) 注意对所有 κ 有 $H(r)\cos 2\pi u\kappa < 0$。

〔42〕按注〔40〕的建议用 0.09 代替 0.1,就保证:若 $2\kappa(t)$ 的初值与整数之差小于 0.125,则其后所有值与整数之差都小于 0.12。现在若 $2\kappa = n + \varepsilon$($|\varepsilon| < 0.12$,$n \in \mathbb{Z}$),则 $K - \tfrac12 = \text{整数} + \lambda$,其中 $|\lambda| < \tfrac12 + \tfrac12(0.12) = 0.31$。另注意 $|H(x)| = |\lambda| > \tfrac12 - \tfrac12(0.12) = 0.19$。

## 图灵的泽塔函数工作
*(希思-布朗的评估)*

〔感谢 D. R. 希思-布朗博士为图灵关于泽塔函数的论文提供以下评估。〕

首先,图灵能做出这样的东西本身就说明了很多——这对他而言本是相当边缘的副业。1943 年那篇论文读起来实在谈不上愉快,即使与其他泽塔函数论文相比也是如此,但部分原因在于其工作的数值性。他所引用的蒂奇马什的论文风格类似。

至于该文的意义,1943 年的论文如今已被遗忘:它被蒂奇马什的方法取代了。后者至少结果更优雅,尽管证明更令人不快。人们有 $\zeta(\tfrac12 + it) = \text{和} + \text{误差}$ 型的公式,误差为 $O(t^{-c})$,c 为常数。典型地 $|\zeta(\tfrac12 + it)|$ 不会小于 $O(\exp(-\text{常数}\cdot\sqrt{\log t}))$。[事实上 $\log|\zeta(\tfrac12 + ic)|/(\log\log t)/2$ 在适当意义下服从标准 $N(0,1)$ 分布。] 所以一个误差项(一行倒置残损,大意:某误差项在数值上会淹没 Z(t))……问题在于对“小的” t(比如 ≤1000),O 项中的常数不太理想。不过如今计算已越过第 $1.5\times10^n$ 个零点,这类问题已不相干。图灵的方法并不稳妥,因为那个和是不连续的:应当代之以 $2\sum W(n/t^{1/2})\cdots$,其中 W(x) 是光滑权,例如 $e^{-x^2}$。事实上可以带着好的逼近这样做。这类方法不用于数值计算,原因有二:(i) 蒂奇马什公式的误差对多数实际目的已足够小;(ii) $W(n/t^{1/2})$ 是个不好算的多余量。

1953 年的论文明显更有意思。数论向来是计算机“数字捣弄”的热门领域,而这篇论文是泽塔函数方面的第一个实例。注意即使在本文中,计算 Z(t) 的方法也是蒂奇马什的。毫无疑问论文最精彩之处在定理 4 和定理 5:证明在临界线上找到的零点确实是截至该高度的全部零点。这比蒂奇马什用的技术容易得多也优雅得多(后者相当碰运气——新方法是保险起效的)。这是近来所有计算采用的方法。

罗杰·希思-布朗

## 可解与不可解问题(1954)

### 注释

〔1〕见 CROWELL 与 FOX(1977)。

〔2〕见注〔18〕。

〔3〕“替换谜题”(substitution puzzle)的另一个名字是“半图厄系统”(semi-Thue system)。

〔4〕这个说法需要稍加限定。按数学家通常理解的意义去证明群论中的定理,并不是谜题的例子;但如果限于在一级逻辑之内进行的证明,那就会是一个谜题的例子。

〔5〕文献为:CHURCH(1936A、B);KLEENE(1935/1936);POST(1936);TURING(1937A)。

〔6〕这个说法至今仍然有效。

〔7〕很少有人会不同意这一点,但确有有趣的问题。给定某判定问题存在算法,我们可以问,例如:是否存在多项式时间内可执行的算法?复杂性理论如今已是数学一个非常活跃的分支。

〔8〕GÖDEL(1931)。

〔9〕见注〔5〕。(Entscheidungsproblem 关心的是:是否存在算法,能判定一级语言的任意语句是否逻辑有效。“不存在这种算法”这一结果通称丘奇定理。)

〔10〕这不是深刻的结果,证明相当容易。

〔11〕例如图灵机的停机问题。

〔12〕这是丘奇定理的推论。因为若 A 是一级语句,则公理“非 A”导致矛盾当且仅当 A 逻辑有效。

〔13〕这是图灵证明的;他的证明收入本卷。

〔14〕“存在字问题不可解的有限呈现半群”由 MARKOV(1947)与 POST(1947)证明。相应的群的结果——“存在字问题不可解的有限呈现群”——由 NOVIKOV(1955)证明。这一重大结果常被并列归于布恩,他在 1954–1957 年间写了一系列论文;文献见 BOONE(1959)。诺维科夫 1952 年早先的通告中所概述的方法是不充分的(NOVIKOV(1952))。

**传记性附记**

诺维科夫 1952 年的通告发表时,纽曼把它译了出来,并宣称它不可能是对的。

(读了诺维科夫完整而正确的 1955 年证明之后再回头看,我研究了 1952 年的版本,结论是该法不充分(BRITTON(1958))。)

〔15〕准确的结果是:若 $n \ge 6$,存在由 102 个整系数 $n \times n$ 矩阵组成的集合,使得没有算法能判定任意整元素矩阵是否为以这些给定矩阵为因子的乘积(MARKOV(1951))。

〔16〕它的一个特化如下。如注〔14〕所述,存在字问题不可解的有限呈现群。由此产生问题:是否存在算法,能判定给定的有限呈现的字问题是否不可解?ADYAN(1957)证明不存在这种算法。

〔17〕马尔可夫证明了:不存在判定两个 4 维流形是否同胚的算法。证明归结到群同构问题的不可解性,即不存在算法判定群的任意两个有限呈现是否同构(ADYAN(1957);MARKOV(1958);RABIN(1958))。

〔18〕(a) Hemion 证明了纽结的判定问题可解,而且一大类 3 维流形的同胚问题可解(HEMION(1979))。

(b) 图灵或许还会列入的另一判定问题是希尔伯特第十问题:是否存在算法,对任意整系数多项式 $p(x_1, \ldots, x_n)$ 判定是否存在整数 $a_1, \ldots, a_n$ 使 $p(a_1, \ldots, a_n) = 0$?

MATIYASEVICH(1970)证明了它不可解;其证明基于 DAVIS、PUTNAM 与 ROBINSON(1961)的工作。

## 关于正规数的札记(未刊 I)

### 注释

〔1〕事实上,CHAMPERNOWNE(1933)已给出正规数的一个例子。

〔2〕更准确地说,γ 是 $u_1, \ldots, u_l$,其中 $0 \le u_i < t$($i = 1, \ldots, l'$),且 $u_1, \ldots, u_l$ 互不相同。

〔3〕第二个求和应从 0 到 R。右端应为 $(R - r + 1)t^{-l}$;不过后文并不需要这个公式。

〔4〕固定 R、T 与 r,把记号简化为 $N(\gamma, n)$、$S'(\alpha, \gamma)$。设 J 是 t 进制下所有 R 位整数之集;对 $\alpha \in (0,1)$,令 $\rho(\alpha) \in J$ 为 α 在 t 进制展开中小数点后的前 R 位数字。若 g 属于 J,令 $S'(g, \gamma)$ 为 γ 在 g 中出现的次数。我们有:$N(\gamma, n)$ 即 γ 恰出现 n 次的 J 中元素的个数。现在,

$$\text{使 } S'(g,\gamma) = x \text{ 的对 } (g,\gamma) \text{ 个数} = \sum_\gamma(\text{使 } S'(g,v) = x \text{ 的对数}) = \sum_\gamma N(\gamma, x)。$$

设 $k < 0.3$。使 $|S'(g,\gamma) - Rt^{-l}| > R/t'^{k/4}$(指数残损)的对数等于:对满足 $|x - Rt^{-l}| > R/t'$ 的 y、x 求和的 $\sum N(\gamma, x)$。此和小于 $2t^l\exp(-k^2t^l/4R)$。使 $\rho(\alpha)$ 等于给定 g 的全体 α 构成长度 $t^{-R}$ 的区间。又 $S(\alpha, \gamma) = S'(\rho(\alpha), \gamma)$。故 (0,1) 中使 $|S(\alpha,\gamma) - Rt^{-l}| > R/t'^{k/4}$ 的 α 之集的测度小于 $\ldots = 2\exp(-Rt^{-l}/4k^2)$(指数残损)。所需不等式随之得出。

〔5〕把 $T^{L+1}$ 换成 $2T^{L+1}$。

〔6〕$A_{k+n}$ 是区间的有限并(因每个 $B(\cdot, \gamma, t, R)$ 都是);这实质上是因为在注〔4〕的记号下,对每个属于 J 的 g,$\rho^{-1}(g)$ 是一个区间。此外这些区间的端点都是有理数。

〔7〕这里给出的该定理证明肯定不充分。我甚至怀疑定理是假的。

在定理中令 $\theta(p) = 0$(对所有 p),或更一般地设 θ 递归。则在证明的记号下可以递归枚举 $m_1, m_2, \ldots$;于是区间 $I_n = (m_n/2^n, (m_n+1)/2^n)$ 可递归枚举。假定这些区间的交是一个单点 x 并注意 $m(I_n) = 2^{-n}$,便知 x 不是 Martin-Löf 随机的(见 CHAITIN(1987))。

〔8〕构造这些区间的论证中似乎有一个严重缺口。非构造性地找出这种区间是平凡的,但我们必须构造性地进行。

注意给定 m 与 n 时我们可以计算 $a_{n,m}$ 与 $b_{n,m}$(见注〔9〕)。略去 n,$(a_m)$ 是极限为 $a \ge 0$(未知)的递减序列,$b_m \to b$(未知)。令 $c = a + b$,则 $c > 0$。设 $0 < c' \le c \le c''$,其中 c′、c″ 已知且 $c'' < 2c‘$。取 x、y 使 $0 < x < c’$、$0 < y < c‘$、$c'' < x + y$。则或者某个 $a_m < x$,或者某个 $b_m < x$,或者存在 m 使 $a_m < y$ 且 $b_m < y$;否则对一切 m 有 $a_m + b_m \ge x + y$,于是 $c \ge x + y > c''$。

第一种情形 $a < x$,故 $b > c - x \ge c’ - x > 0$;类似地在第三种情形 $a < y$、$b < y$,故 $a > c' - y > 0$ 且 $b > c' - y > 0$。(这一分析表明(一行残损)。)第一种情形选右半区间,第二种情形选左半区间,第三种情形作一个由 θ 决定的选择。

倘若上面这类做法就是作者从 $I_n$ 得到 $I_{n+1}$ 时心中所想,我看不出如何把 x、y、c′、c″ 定义成 n 的函数而得以构造出全部区间 $I_n$。

〔9〕左端的符号“m”显然指两集之交的测度。右端依赖于 n 和另一个不幸也叫 m 的变量,故显然 c(k,n) 应为 c(k,m)。

〔10〕有什么能排除“从某处起总是选左半区间”的情形?此时诸区间之交为空。(不过,若交集为空,则所有相应闭区间公共的那个点是有理数。)

假定交集非空,为什么该数是正规的?(考虑类似的情形:$I_n = (\tfrac12 - \tfrac1{2n}, \tfrac12 + \tfrac1{2n})$,$E = (0,\tfrac12)\cup(\tfrac12,1)$。则 $I_n \cap E$ 有正测度,但 $\tfrac12$ 不属于 E。)

〔11〕把 $2^{-n-1}$ 换成 $2^{-n}$(并把 $1 - 2/k$ 换成 $1 - 3/k$)?

〔12〕正文中有三个文献编号,却没有相应的文献条目。关于正规数的更多信息,见 KUIPERS 与 NIEDERREITER(1974)。

## 紧群中的字问题(未刊 II)

### 注释

〔1〕设 L 是带等词的一阶语言,含一个二元关系符号 < 与二元函数符号 −、×。L 的语句 A 称为**对 ℝ 真**,如果把它放到实数上(=、<、−、× 取通常含义)时为真。塔斯基定理可以这样表述:存在算法,对任意语句 A 判定 A 是否对 ℝ 为真。

为后文注意:y = 0 在 L 中可表达为 $y - y = y$。又有若干表达式分别表示 y = 1、加法与不等式(数行倒置残损,大意如此):例如 $z = x - ((x - x) - y)$ 表示 $z = x + y$;而"$x = z$ 不成立且……"表示 $x \ne z$。〔译注16〕

〔2〕要使程序 (a) 有意义,群 G 必须以生成元和定义关系给出,生成元之集须可递归枚举,定义关系之集也须可递归枚举。特别地 G 必须可数;这就排除了例如酉群 U(n)。

〔3〕"阶 r"当然指矩阵是 $r \times r$ 的。

〔4〕这意味着:若引号中的陈述记作 S,则存在注〔1〕的一阶语言中的语句 $A_S$,使 S 真当且仅当 $A_S$ 对 ℝ 真。(要看出这点,先把 $E_k$ 的第 $(p,q)$ 元写成 $\chi_{pqk} + i\eta_{pqk}$ 的形式,其中 χ、η 是变量。)

〔5〕注意:M 与 N 都必须有限,$A_{MN}$ 才是一级逻辑的语句。因此主定理实际上是:字问题在**有限呈现的**紧群中是可解的。

〔6〕TARSKI(1951)是该 RAND 报告的“第二版”。关于塔斯基工作的更多细节,见 DONER 与 HODGES(1988)。

## 论置换群(未刊 III)

### 摘要

考虑 T 个对象上的置换。记 S、A 分别为对称群与交错群。R 表示一个固定的 T-循环 $R = (a_1, a_2, \ldots, a_T)$。

对任意置换 U,$J(U)$ 或 J 表示由 R 与 U 生成的 S 的子群;$H(U)$ 或 H 表示 J 的、由所有形如

$$R^{t_1}UR^{t_2}\cdots UR^{t_k},\qquad \sum t_i = 0$$

的表达式组成的正规子群。我们关心的是 H 而非 J。在研究 J 与 H 时,置换 U 称为**直立者**(upright)。〔译注17〕

S 的子群若为 A 或 S,则称为**非例外的**(unexceptional)。

**定理 I.** 设 $U \ne 1$、$T \ne 4$。则 H 非例外当且仅当 J 非例外。

若 H 非例外,则称 U 非例外。所考虑的问题是找出所有例外的 H。

**定理 II.** 设 $T > 4$。若 m 与 T 互素,且 J 含有形如 $(\alpha, R^m\alpha)$ 或 $(\alpha, R^m\alpha, \beta)$ 或 $(\alpha, R^m\alpha)(\beta, \gamma)$ 的置换——第三种情形中若 T 为偶,还要求该置换不与 $R^{T/2}$ 交换——则 J 非例外:它含全部 3-循环,且在第一种情形下还含全部 2-循环。

**注.** 若 J 含有 $(\alpha, R^m\alpha)$ 而 m 不与 T 互素,则 H 是非传递群(从而是例外的)。若 J 含有 3-循环 $(\alpha, R^m\alpha, R^{m+p}\alpha)$ 且某个素数整除 m、p、T 全体,亦然。上面第三种情形中,若该置换确实与 $R^{T/2}$ 交换,则 H 的每个成员都与它交换,故 H 是例外的。

实践中我们把 U、UR、UR²、… 写成循环分解,希望找到其中某个的适当幂次满足定理假设。若成功,则 U 非例外,可以淘汰。

注意:

- 若 $U' = R^mUR^n$(某 m、n),则 $J(U') = J(U)$;
- 若 V 与群 $\langle R\rangle$ 交换,则 $H(VUV^{-1}) = H(U)$;
- 若 $U' = U^2$ 且 $U = U'''$,则 $H(U') = H(U)$。(此行残损,大意如此。)〔译注17〕

称 U **有“甲虫”**(beetle)〔原文如此〕,如果某个 $R^mUR^n$ 固定两个或更多对象。

如下定义向量 $(f(1), \ldots, f(T))$:令

$$R^{f(i)}Ua_i = Ua_{i+1},\qquad i = 1, \ldots, T,$$

其中 $a_{T+1}$ 指 $a_1$。

若数

$$f(1) + \cdots + f(n) - n,\qquad n = 0, 1, \ldots, T-1$$

两两不同,则 T 为奇数。若(通常如此)它们并非两两不同,则 U 有甲虫。

$R^mUR^n$ 的向量结果恰是 U 的向量的一个循环轮换。U 的向量的适当循环轮换称为 U 的**不变量**(invariant)。

若 U 有甲虫,可不失一般性设 U 固定某对象;(该固定对象的取法一行残损:)可取为 $R^ta_1\ (= a_{t+1})$,其中 t 整除 T 且 $1 < t < T$。

作者随后开始对例外群进行漫长、细致而费力的搜索,覆盖 $T = 1, 2, \ldots, 8$ 各情形。特别地当 T = 8 时发现:在 $8! = 40320$ 个可能的直立者中有 2144 个是例外的。在例外群之中有一个阶为 168 的群。(此句残损。)

论文最后几页转向另一个相关主题。设 H 是 h 阶有限群,生成元 $U_1, \ldots, U_k$ 互不相同。E 表 H 上全体实值函数之集。对 $\theta \in E$,令 $\|\theta\| = (h^{-1}\sum_a \theta(a)^2)^{1/2}$。$f \in E$ 定义如下:$f(a) = k^{-1}$ 若 a 是 $U_1, \ldots, U_k$ 之一;否则为 0。g 表 E 中满足 g(a) ≥ 0(一切 a)且 g(a) > 0(某个 a)的元素。$R_f$ 定义为

$$(R_fg)(a) = \frac{1}{h}\sum_b f(ab^{-1})g(b)。$$

**引理.** $\|R_fg\| \le \|g\|\cdot\ldots$(系数残损),等号成立仅当:对任何使 $f(a) \ne 0$、$f(b) \ne 0$ 的 a、b,$g(a^{-1}bx)/g(x)$ 与 x 无关。

若子序列 $g, R_fg, R_f^2g, \ldots$ 趋于极限 k,则 k 称为一个**极限分布**。

K(或 $H_1$)表示 H 的、由所有表达式 $U_1^{m_1}\cdots U_k^{m_k}(\sum m_i = 0)$ 组成的正规子群。

**定理 I.** 任一极限分布 k 在每个傍系上取常值。

$H/H_1$ 是循环群。若 g 取为 f,则 k 除一个傍系外处处为零。

**注.** 对任意 $n \ge 1$,$R_f^n f$ 在 $H_1$ 的各傍系上除一个(即 $H_1U^n$)外为零。(算子残损。)

**推论.** 若 H 是至少五个符号上的对称群 $S_n$ 或交错群 $A_n$,则:若 $U_1, \ldots, U_k$ 奇偶性全同,则 $H_1$ 为 A;否则为 S。

### 注释

〔1〕(本注开头残损:)……它整除 k,这与 $2k = 1$(T)矛盾。

〔2〕见 HALL(1959)§1.9 例 4。

〔3〕在“U 是所述形式的 2-循环”这一假设下,H 非传递因而例外。(H 的任一元素都是形如 $R^tUR^{-t}$ 的元素之积,每个这样的元素都保持所述的非传递性集。)

这是不是想要的假设?两行之后 “generator” 一词的用法提示是这样。

〔4〕故 H 例外。

〔5〕我们并不需要“距离 NF 为 8”这一事实;显然 $U_{22}$ 不与 $R_{13}$ 交换。

〔6〕若 $U = R$、m = 1、n = 0 且 T 为偶,则 $U‘ = RU = R^2$,故 $H(U) = \langle R\rangle$ 而 $H(U’) = \langle R^2\rangle$;于是 $H(U)$、$H(U')$ 不同构。不过总有 $J(U) = J(U')$。

〔7〕注意:若 U 是 R 的幂,则对所有 n 有 f(n) = 1。R 的幂必有甲虫,因为存在 m、n 使 $R^mUR^n = I$。

〔8〕设 $(VUV^{-1})R^{n+1}Z = R^{g(n)}(VUV^{-1})R^nZ$。则

$$VUR^{-n-1}V^{-1}Z = R^{g(n)}\,VUR^{-n}V^{-1}Z 。$$

我们有 $V^{-1}Z = R^kZ$(某 k)。故

$$R^{g(n)}UR^{-n-1+k}Z = UR^{-n+k}Z = R^{f(-n+k-1)}UR^{-n+k-1}Z,$$

所以 $g(n) = f(-n+k-1)$,其中 f 对一切 n 的定义约定是(倒置残损,大意:$f(n \pm T) = f(n)$)。〔译注17〕

〔9〕设诸对象为 $A_1, \ldots, A_T$。则 Z 即 $A_T$;把 $A_1$ 记作 A。我们求得 $R^{-n}UR^nA = R^SUA$,其中 $S = f(1)+\cdots+f(n)-n$($0 \le n \le T-1$)。若序列中两数模 T 相等,则有 $R^{-i}UR^iA = R^{-j}UR^jA$,其中 $i - j = p > 0$。于是 $UR^pR^jA = \cdots$。令 $UA_{j+1} = A_\alpha$,则

$$UA_{p+j+1} = R^pUA_{j+1} = A_{\alpha+d}$$

(下标残损)。于是 $U' = R^{i+j-d}U$ 固定 $A_{j+1}$ 与 $A_{j+p+i}$,故 U 有甲虫。

〔10〕短语“other than where U is a power of R”(“除非 U 是 R 的幂”)令人费解;见注〔7〕。

〔11〕设 $0 < t < T$ 且 T 与 t 的最大公因子为 d。只需 s = d 的情形。先证存在 k 使

$$0 < k < T,\qquad kd \equiv t\ (\operatorname{mod} T),\qquad (k, T) = 1 。$$

若 k 存在,则 $kd = t + hT$,于是 $k = t' + hT‘$,其中 $t = t’d$、$T = T'd$。下列各数

$$t',\ t'+T',\ \ldots,\ t'+(d-1)T'$$

都满足 k 所需性质的前两条。设无一满足第三条。则对每个 $h = 0, 1, \ldots, d-1$ 有素数 $p_h$ 同时整除 $t'+hT'$ 与 $T'd$。它不能整除 T′,否则也整除 t′;故它整除 d。若 $p_i = p_j = p$($i \ne j$),则 p 整除 $t'+iT'$ 与 $t'+jT'$,从而整除 t′ 与 T′。于是 $p_0, \ldots, p_{d-1}$ 互不相同且都整除 d。这给出矛盾:d ≥ 2^d(原文如此)。〔译注17〕

因 $R^k$ 与 R 同阶,存在置换 V 使 $VA = A_1$、$V^{-1}RV = R^k$。故 $V^{-1}R^dV = R^{kd} = R^t$,即 $VR^tV^{-1} = R^d$。又 $V^{-1}\langle R\rangle V = \langle R\rangle$,故 $V\langle R\rangle V^{-1} = \langle R\rangle$。最后,置换 $VUV^{-1}$ 固定 $A_1$ 与 $R^dA$,因为

$$VUV^{-1}R^dA = VUR^tV^{-1}A = VUR^tA = VR^tA = R^tVA = R^dA 。$$

〔12〕(a) 不变量为 22222 的置换有五个,33333、44444 类似。不变量为 11111 的置换构成循环群 $\langle R\rangle$。此处的 $\langle R\rangle$ 的“numatizer”看来由这 20 个置换组成。

(b) “These together prove the numatizer of ⟨R⟩”(“这些合起来证明了 ⟨R⟩ 的 numatizer”)这句话似乎没有意义。

〔13〕$R_f^{-1}g$?

〔14〕把 '$g(ab^{-1}x)$' 换成 '$g(a^{-1}bx)$'。

〔15〕这个和等于 $(\sum f(a)^2)\|g\|^2 = h^2F^2\|g\|^2$。所以我们真正需要的是 $F = h^{-1}$,即 $\sum f(a) = 1$,而不是 F = 1。

〔16〕首先注意

$$(R_f^n g)(a) = \sum f(aa_2^{-1})\cdots f(a_ma_{m+1})g(a_{m+1})。$$

现在令 $F = R_f^{m-1}f$。我们发现对任意 h 有 $R_fh = \cdots$(残损)。由 $\|R_f^{m-1}k\| = \|k\|$ 得 $\|R_fk\| = \|k\|$,故 $F(a) \ne 0$、$F(b) \ne 0$ 蕴含 $k(a^{-1}bx)/k(x)$ 与 x 无关(见引理)。现在 $H(c‘) = (pf - f)(c’)$?(倒置残损);而且若……非零,则存在生成元 $U_1, \ldots, U_m$ 其积为 a(因为 $f(b) \ne 0$ 当且仅当 b 是生成元),所以当 y 形如

$$(U_1\cdots U_m)^{-1}U_s\cdots U_{s'}\cdots$$

时,$k(yx)/k(x)$ 与 x 无关。〔译注17〕

〔17〕定义域 L 由形如 $(U_1\cdots U_m)^{-1}U_s\cdots U_{s'}$ 的元素生成,故 L 含于 $H_1$。又 L 是 $H_1$ 的正规子群:因为若 $h \in H_1$、$y \in L$,则 $h^{-1}yh \in L$,因为 h 可写成不含负指数的生成元字。现在用对长度的归纳易证:指数和为零的字属于 L。故 $L = H_1$。

〔18〕在本行及下一行把 g 换成 k。

〔19〕这一点显然,但需证定理 III 的最后一句随之得出。

设 $R_f^rf \to k$,即 $R_f^rf - k \to O$(r → ∞)。于是对每个 $a \in H$,$(R_f^rf)(a) \to k(a)$。但 $\sum(R_f^rf)(a) = 1$,故 $\sum k(a) = 1$。对每个 r,$(R_f^rf)(a) \ne 0$ 蕴含 a 属于 $H_1$ 的某个傍系 C(r)。取适当的子列可设 C(r) = C 与 r 无关。若 a 不属于 C,则对一切 r 有 $(R_f^rf)(a) = 0$,故 $k(a) = 0$。但 k 在傍系上取常值,故 k 在 C 上非零而在 C 外为零。

〔20〕$(R_f^{-1}f)(a) = \sum f(U_{i_1})f(U_{i_2})\cdots f(U_{i_n})$,对使 $a = U_{i_1}U_{i_2}\cdots U_{i_n}$ 的 $(i_1, \ldots, i_n)$ 求和。这等于 $k^{-n}$ 乘以这种 n 元组的个数。本情形 k = 2。n = 1、2 时得到表的第 1、2 行。然而 n = 3 时得

$$0000$$

故表的第 3 行看来有误。

〔21〕若所有生成元奇偶性相同,则由于置换与其逆奇偶性相同,$H_1$ 的任一元素都是偶数个同奇偶置换之积,故为偶置换,从而 $H_1 = A$。反之若 $U_1$、$U_2$ 奇偶相反,则 $U_1^{-1}U_2 \in H_1$ 且为奇置换;故 $H_1$ 是对称群。

## 差 ψ(x) − x(未刊 IV)

### 注释

〔1〕"'a'" 与 "'b'" 应分别换成 "'log a'" 与 "'log b'"。

〔2〕具体地,

$$\eta(t) = e^{-t/2}\big({-\tfrac12\log(1-e^{-t}) - \tfrac12S'(0)}\big)$$

(记号残损)。

〔3〕设 $b > a = nT$。则

$$\int_a^b w(v)\cos(\gamma v)\,dv = w(a)\int_a^{a+\pi/T}\cos(\gamma u)\,du$$

(公式破碎,大意如此),这是因为 w(v) 正且递减。右端等于 $w(a)\frac{T}{\gamma}(\sin(\gamma\xi/T) - \sin(\gamma a/T))$,至多为 $(2T/\gamma)w(nT)$。

〔4〕这里用到不等式

$$|a\cos\gamma\omega + b\sin\gamma\omega| \le (a^2 + b^2)^{1/2}。$$

〔5〕本行中是 $\omega + \ldots$,下一行是 $\omega + \ldots$(两个分数在 OCR 中丢失)。事实上二者应相等。似乎无论两者都取哪个都无妨。

〔6〕求导之后须证

$$\int_0^\infty \sin v\,f(v)\,dv = \frac{1}{2\sqrt{2\pi}}\exp(-\alpha^2),$$

其中 $f(v) = v\exp(-\tfrac12v^2/\alpha^2)$。令 $F(v) = \int f(u)\,du = -\alpha^2\exp(-\tfrac12u^2/\alpha^2)$(原文如此)。则 $\int \sin v\,f(v)\,dv = -\int\cos v\,F(v)\,dv$,后者可用恒等式

$$\int_0^\infty \cos(un)\,w(v)\,du = \exp(-n^2)$$

求值;它与正文前面陈述过的恒等式等价。

〔7〕右端应加上 $T/2n$。

〔8〕令 $c = 2\pi/137$ 并设 $\gamma < 125\pi$。则

$$\frac{\gamma(\omega + 2/3)}{2\pi} = N + \theta,$$

N 为整数且 $|\theta| < \ldots$。故 $-\sin\gamma\omega = \sin\ldots$(残损)。

现在用:由于 $|2\pi\theta| < c$,有 $\cos 2\pi\theta > \cos c$ 且 $|\sin 2\pi\theta| < c$。

〔9〕这由 S 的定义立即得到:当 $\gamma < 125\pi$ 时用刚得到的 $-\sin\gamma\omega$ 下界;当 $\gamma \ge 125\pi$ 时用 $-\sin\gamma\omega \ge -1$。

〔10〕把 25/137 换成 2π/137。

〔11〕积分区间应改为从 0 到 125π。

〔12〕左端的负号应换成正号。

〔13〕三处出现的 “135” 应改为 “137”。实际上该行大概应为:

$$= \cos\frac{2\pi}{137}\cdot\frac{1-\mathfrak{l}_2}{2\pi c} + \frac{2\pi}{137}\cdot\frac{\mathfrak{l}+\cos}{2\pi}\cdot\frac{\varepsilon_1+\varepsilon_2+\varepsilon_3}{137}+\cdots$$

(此式完全破碎,只可辨认出若干片段:分母 137 反复出现,以及 $\varepsilon_1 + \varepsilon_2 +$、$\varepsilon_3$ 等。)〔译注18〕

〔14〕$\nu^{-1}$ 左边的负号应删去;也就是说,运算应是乘法而非减法。

〔15〕$S(0) = -\tfrac12$。

〔16〕等号应换成正号。是否漏掉了项 $S(125\pi)/125\pi$?

*(科恩的评论)*

〔感谢 A. M. 科恩博士提供以下评论。〕

从文献看,这项工作在时间上很可能早于关于 $\pi(x) - \operatorname{li}x$ 的论文 (V),甚至很可能早于图灵 (1953) 用计算机扩展蒂奇马什对泽塔函数的计算。

手稿中的基本思想大概是健全的。但要整理这些结果还需相当多的工作。例如不等式 (i) 是错的,因为其左端的近似值为 0.011908,比图灵的数值 0.00851 大约大 40%。

## 论利特尔伍德的一个定理(S. 斯丘斯与 A. M. 图灵,未刊 V)

### 摘要

收于本卷的 COHEN 与 MAYHEW(1968)一文,实质上是这份未刊手稿主要部分——即 §1 至 §5,也就是直到并包含定理 2 的证明为止的部分——的一个经过大幅修正与扩充的版本。

这一部分的摘要,见 Cohen–Mayhew 论文首页。

在 §6 中,斯丘斯与图灵简要指出:假定计算给出泽塔函数的前 300 个非平凡零点到小数七位(所有这些零点都在临界线上),那么借助数字计算机应当能改进估计。随后给出一个统计论证,表明这种做法有一半机会给出某个 $x$($2 < x < \exp 220000$)使 $\pi(x) > \operatorname{li}x$。

最后,§7 考虑了在临界线之外找到一个非平凡零点的可能性。

**定理 3.** 设 $\beta_1 + i\gamma_1$($\beta_1 > \tfrac12$,$\gamma_1 > 0$)是泽塔函数的一个零点,而对每个其他非平凡零点 $\beta + i\gamma$,或者 $\beta = \tfrac12$,或者 $|\gamma - \gamma_1| > 14$。则存在某个 x,$2 < x < (16\gamma_1)^a$,$a = 1.12/(\beta_1 - \tfrac12)$,使 $\pi(x) > \operatorname{li}x$。

### 注释

〔1〕我未能找到原稿本身,但见到了它的复印件。

文章是打字体,数学符号均为手写。尽管是联名,笔迹与措辞表明它也许出自图灵一人之手。

稿上有另一人的手写批注,可能是 A. E. 英厄姆。这些批注在此以方括号 [ ] 括出。必要时用一个较早的 $ 号标出批注适用的正文位置;若批注针对正文中的符号或表达式,则相应的 $ 号紧放在该符号或表达式之前。

阅读本文时宜不断对照 COHEN 与 MAYHEW(1968),该文重印于本卷。

斯丘斯–图灵与 Cohen–Mayhew 的引理对应关系如下(S&T 的定理 1、2 分别对应 C&M 的定理 1、2):

| S&T | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10–12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C&M | 1 | 4 | 3 | 5(a) | 2 | 6 | 7(b) | 8–9 | | | |

((a):第 695 页;(b):第 708 页。)

〔2〕(本注开头残损:)……后接一个左括号和一个被划掉的表达式。

〔3〕注意 $\exp 220000$ 远大于 R. Sherman Lehman 在 1966 年得到的值 $1.65\times10^{1165}$;见 Cohen–Mayhew 文章末尾。不过我们可以说,图灵猜对了:确有某个 $x$($2 < x < \exp 220000$)使 $\pi(x) > \operatorname{li}x$。
