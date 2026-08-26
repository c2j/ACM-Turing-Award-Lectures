# 群的扩张

**The Extensions of a Group**

> 作者:艾伦·图灵(A. M. Turing)〔译注1〕,剑桥,英格兰
> 原载 *Compositio Mathematica*, Vol. 5(1937 年 3 月 22 日收到,1938 年刊出),pp. 357–367
> 译自 `papers/Pure Mathematics. 2-North Holland (1992).pdf` 第 33–43 页(书页 11–21)(个人学习用途)

设 $\mathfrak{M}$ 是群 $\mathfrak{G}$ 的自共轭子群〔译注2〕且 $\mathfrak{G}/\mathfrak{M} \cong \mathfrak{G}'$,则称群 $\mathfrak{G}$ 是 $\mathfrak{M}$ 经 $\mathfrak{G}'$ 的一个**扩张**(extension)。求 $\mathfrak{M}$ 经 $\mathfrak{G}'$ 的扩张这一问题,施赖埃尔¹)和贝尔²)〔译注3〕都研究过。

设 $\Omega$ 是 $\mathfrak{M}$ 的自同构群,$S$ 是内自同构子群。那么,$\mathfrak{G}$ 中 $\mathfrak{M}$ 的每个陪集 $\gamma$ 都对应着 $\Omega$ 中 $S$ 的一个陪集 $X(\gamma)$:若 $c$ 属于 $\gamma$,则 $c$ 在 $\mathfrak{M}$ 中诱导的自同构属于 $X(\gamma)$。$X(\gamma)$ 是 $\mathfrak{G}'$ 到 $\Omega/S$ 里的一个同态。〔译注4〕贝尔的研究着眼于:在 $\mathfrak{M}$、$\mathfrak{G}'$ 和同态 $X(\gamma)$ 都给定时,找出所有可能的群 $\mathfrak{G}$。作为解决这个问题的第一步,要先弄清 $\mathfrak{G}/\mathfrak{z}(\mathfrak{M})$ 可能有的结构,这里 $\mathfrak{z}(\mathfrak{M})$ 表示 $\mathfrak{M}$ 的中心;〔译注5〕于是只剩下在 $\mathfrak{M}$ 为阿贝尔群的情形求解原问题。这一情形的处理方式截然不同。本文要说明的是:贝尔的方法——它只适用于 $\mathfrak{M}$ 为阿贝尔群的情形——如何能用于任意群 $\mathfrak{M}$。

在具体判定具有给定示性数据(特征)的所有扩张时,必须弄清商群 $\mathfrak{G}'$ 的关系群的结构。即使 $\mathfrak{M}$ 是阿贝尔群也是如此。这个问题在本文后半部分讨论。作为例示,文中把这套理论应用于任意群经循环群的扩张。

## § 1. 带给定自同构的扩张

求一个群经另一个给定群的、诱导出给定自同构类的扩张,这一问题最好化归为下述另一个问题来处理;该问题既在其陈述中、也在下述定理中得到解决。

**定理 1.** 设 $\mathfrak{M}$、$\mathfrak{E}$ 是给定的群,〔译注6〕$R$ 是 $\mathfrak{E}$ 的自共轭子群;$\chi_a$ 是 $\mathfrak{E}$ 到 $\mathfrak{M}$ 的自同构群里的一个同态(即 $\chi_a(\mathfrak{b})$ 作为 $\mathfrak{b}$ 的函数是 $\mathfrak{M}$ 的自同构,且满足

$$\chi_{ab}(\mathfrak{b}) = \chi_b(\chi_a(\mathfrak{b})) \qquad (1;\ I,\ b,\ a,\ \mathfrak{b})$$

对所有 $b, a$ 属于 $\mathfrak{E}$ 及 $\mathfrak{b}$ 属于 $\mathfrak{M}$ 成立),而 $a(r)$ 是 $R$ 到 $\mathfrak{M}$ 里的同态。那么,存在一个群 $\mathfrak{G}$,$\mathfrak{M}$ 是它的自共轭子群,并且存在 $\mathfrak{E}$ 到 $\mathfrak{G}$ 里的一个同态 $m(a)$,满足:

- a) $\chi_a(\mathfrak{b}) = (m(a))^{-1}\,\mathfrak{b}\, m(a) \qquad (2,\ I,\ a,\ \mathfrak{b})$;
- b) $\mathfrak{M}$ 在 $\mathfrak{G}$ 中的每个陪集都含有 $m(\mathfrak{E})$ 的一个元素;
- c) $m(r) = a(r) \qquad (2,\ II,\ r)$,

**当且仅当**

$$\chi_a(a(r)) = a(a^{-1}ra) \qquad (3,\ I,\ a,\ r), \tag{3}$$
$$\chi_r(\mathfrak{b}) = (a(r))^{-1}\,\mathfrak{b}\, a(r) \qquad (3,\ II,\ r,\ \mathfrak{b})$$

(对 $R$ 中所有 $r$ 及 $\mathfrak{M}$ 中所有 $\mathfrak{b}$)。

本定理与原扩张问题的关联可见于

**推论.** 设 $\mathfrak{E}$ 是自由群⁴),带自共轭子群 $R$(记 $\mathfrak{E}/R \cong \mathfrak{G}'$),$X(\gamma)$ 是 $\mathfrak{E}/R$ 到某给定群 $\mathfrak{M}$ 的自同构类里的同态。取 $\chi_a$ 为 $\mathfrak{E}$ 到 $\mathfrak{M}$ 的自同构里的任一同态,使得每当 $a$ 属于 $R$ 在 $\mathfrak{E}$ 中的陪集 $\alpha$ 时,$\chi_a$ 属于类 $X(\alpha)$。那么,存在 $\mathfrak{M}$ 经 $\mathfrak{G}'$ 的一个扩张 $\mathfrak{G}$,使 $\mathfrak{M}$ 的陪集 $\alpha$ 诱导出自同构类 $X(\alpha)$,其充要条件是:存在 $R$ 到 $\mathfrak{M}$ 里的同态 $a(r)$ 满足 (3)。

**定理的证明.** 诸条件的必要性是显然的。$(3, I, a, r)$ 由 $(2, I, a, a(r))$、$(2, II, r)$、$(2, II, a^{-1}ra)$ 及 $m$ 是同态这一事实推出;$(3, II, r, \mathfrak{b})$ 由 $(2, I, r, \mathfrak{b})$ 与 $(2, II, r)$ 立即推出。

充分性的证明须构造群 $\mathfrak{G}$。这个群的元素取为所有等价对 $(a, \mathfrak{a})$ 所成的类($a$ 属于 $\mathfrak{E}$,$\mathfrak{a}$ 属于 $\mathfrak{M}$),$(a', \mathfrak{a}')$ 等价于 $(a, \mathfrak{a})$ 当且仅当 $a^{-1}a'$ 属于 $R$ 且 $a(a^{-1}a') = \mathfrak{a}\mathfrak{a}'^{-1}$。这是一个等价关系,因为:

1) 若 $a^{-1}a' \in R$ 且 $a(a^{-1}a') = \mathfrak{a}\mathfrak{a}'^{-1}$,则

$$a'^{-1}a \in R \quad\text{且}\quad a(a'^{-1}a) = \mathfrak{a}'\mathfrak{a}^{-1},$$

即关系是对称的;

2) $a^{-1}a = e \in R$,$a(a^{-1}a) = \mathfrak{e} = \mathfrak{a}\mathfrak{a}^{-1}$,

即关系是自反的;

3) 若 $a^{-1}a' \in R$、$a'^{-1}a'' \in R$,

$$a(a^{-1}a') = \mathfrak{a}\mathfrak{a}'^{-1} \quad\text{且}\quad a(a'^{-1}a'') = \mathfrak{a}'\mathfrak{a}''^{-1},$$

则

$$a^{-1}a'' = (a^{-1}a')(a'^{-1}a'') \in R$$

〔且 $a(a^{-1}a'') = \mathfrak{a}\mathfrak{a}''^{-1}$〕,

即关系是传递的。

两个对的乘积定义为

$$(a, \mathfrak{a})(b, \mathfrak{b}) = (ab,\, \chi_b(\mathfrak{a})\mathfrak{b}).$$

要使这确实给出类的乘法,须证:若 $(a', \mathfrak{a}')$ 等价于 $(a, \mathfrak{a})$、$(b', \mathfrak{b}')$ 等价于 $(b, \mathfrak{b})$,则 $(a', \mathfrak{a}')(b', \mathfrak{b}')$ 等价于 $(a, \mathfrak{a})(b, \mathfrak{b})$,即:若

$$a^{-1}a' \in R,\quad b^{-1}b' \in R,\quad a(a^{-1}a') = \mathfrak{a}\mathfrak{a}'^{-1} \quad\text{且}\quad a(b^{-1}b') = \mathfrak{b}\mathfrak{b}'^{-1}, \tag{4}$$

则

$$(ab)^{-1}(a'b') \in R \quad\text{且}\quad a\bigl((ab)^{-1}(a'b')\bigr) = (\chi_b(\mathfrak{a})\mathfrak{b})(\chi_{b'}(\mathfrak{a}')\mathfrak{b}')^{-1}.$$

现在

$$(ab)^{-1}(a'b') = \bigl(b^{-1}(a^{-1}a')b\bigr)(b^{-1}b')$$

〔属于 $R$,因为 $R$ 自共轭〕,并且

$$a\bigl((ab)^{-1}(a'b')\bigr) = \chi_b(\mathfrak{a}\mathfrak{a}'^{-1})\,\mathfrak{b}\mathfrak{b}'^{-1}$$
$$= \chi_b(\mathfrak{a})\,\mathfrak{b}\,\mathfrak{b}'^{-1}\,\mathfrak{b}'\,\chi_{b'}(\mathfrak{a}'^{-1})\,\mathfrak{b}'^{-1} = (\chi_b(\mathfrak{a})\mathfrak{b})(\chi_{b'}(\mathfrak{a}')\mathfrak{b}')^{-1},$$

这是由 (4)、$(3,\ II,\ b^{-1}b',\ \chi_b(\mathfrak{a}'))$ 与 (1) 得到的。乘法还是结合的,因为

$$\bigl((a, \mathfrak{a})(b, \mathfrak{b})\bigr)(c, \mathfrak{c}) = (ab, \chi_b(\mathfrak{a})\mathfrak{b})(c, \mathfrak{c}) = (abc,\, \chi_c(\chi_b(\mathfrak{a})\mathfrak{b})\mathfrak{c}),$$
$$(a, \mathfrak{a})\bigl((b, \mathfrak{b})(c, \mathfrak{c})\bigr) = (a, \mathfrak{a})(bc, \chi_c(\mathfrak{b})\mathfrak{c}) = (abc,\, \chi_{bc}(\mathfrak{a})\chi_c(\mathfrak{b})\mathfrak{c}),$$

〔两式右端相等,由 (1) 及 $\chi_c$ 是自同构即得〕。$(\mathfrak{e}, \mathfrak{e})$ 是单位元,而 $(a^{-1}, \chi_{a^{-1}}(\mathfrak{a}^{-1}))$ 是 $(a, \mathfrak{a})$ 的逆。于是,带此乘法的对类构成一个群。

$m(a)$ 定义为

$$m(a) = (a, \mathfrak{e}),$$

显然是同态。要证 $(2, II)$ 满足,只需验证 $(r, \mathfrak{e})$ 等价于 $(\mathfrak{e}, a(r))$。至于 $(2, I)$,我们有

$$(m(a))^{-1}\mathfrak{b}\,m(a) = (a^{-1}, \mathfrak{e})\,\mathfrak{b}\,(a, \mathfrak{e}) = (a^{-1}, \mathfrak{e})(a, \chi_a(\mathfrak{b})) = (\mathfrak{e}, \chi_a(\mathfrak{b})) = \chi_a(\mathfrak{b}).$$

既然

$$(a, \mathfrak{a}) = (a, \mathfrak{e})(\mathfrak{e}, \mathfrak{a}) = m(a)\,\mathfrak{a},$$

条件 b 便满足。$\mathfrak{M}$ 的元素 $\mathfrak{b}$ 同时落在 $m(\mathfrak{E})$ 中的条件是:$(\mathfrak{e}, \mathfrak{b})$ 与某个对 $(a, \mathfrak{e})$ 等价。这意味着 $a$ 属于 $R$ 且 $a(a) = \mathfrak{b}$。于是 $\mathfrak{M} \cap m(\mathfrak{E}) \le m(R)$。由于 $m(r) = a(r)$,有 $m(R) \le \mathfrak{M}$,故前述条件满足。

**推论的证明.** 设 $\mathfrak{E}$ 是具有所需性质的群,$e_1, e_2, \ldots, e_n$ 是 $\mathfrak{E}$ 的一组自由生成元,$w$ 是确定 $\mathfrak{E}$ 到 $\mathfrak{G}'$ 上同态的函数。取 $\mathfrak{e}_1, \mathfrak{e}_2, \ldots, \mathfrak{e}_n$ 为 $\mathfrak{G}$ 中具有下述性质的元素:$\mathfrak{e}_i$ 属于 $\mathfrak{M}$ 的陪集 $w(e_i)$,且

$$\chi_{e_i}(\mathfrak{b}) = \mathfrak{e}_i^{-1}\mathfrak{b}\,\mathfrak{e}_i \qquad \text{对 } \mathfrak{M} \text{ 中所有 } \mathfrak{b}.$$

那么,若 $m$ 是 $\mathfrak{E}$ 到 $\mathfrak{G}$ 里的同态且对所有 $i$ 满足 $m(e_i) = \mathfrak{e}_i$,则将有

$$\chi_a(\mathfrak{b}) = (m(a))^{-1}\mathfrak{b}\,m(a) \qquad \text{对 } \mathfrak{M} \text{ 中所有 } \mathfrak{b}.$$

若对 $R$ 中的元素 $r$ 令 $m(r) = a(r)$,则由定理 1 的前一半(其证明未用到 b、c)知条件 (3) 必成立。反之,若有满足 (3) 的函数 $a(r)$,就可以构造定理 1 的群 $\mathfrak{G}$;容易看出它具有所需的性质。

具体应用时,定理 1 的推论以下述形式更合用:

**定理 2.** $\mathfrak{M}$ 是给定群。$\mathfrak{E}$ 是带生成元 $e_1, e_2, \ldots, e_n$ 的自由群。$R$ 是 $\mathfrak{E}$ 的含 $r_1, r_2, \ldots, r_l$ 的最小自共轭子群。$w$ 把 $\mathfrak{E}$ 同态地映到 $\mathfrak{G}'$ 上,映到单位元的元素恰是 $R$ 中的元素。$\chi_a$ 是 $\mathfrak{E}$ 到 $\mathfrak{M}$ 的自同构里的同态,而 $X(w(a))$ 是含 $\chi_a$ 的自同构类。$\mathfrak{r}_1^*, \mathfrak{r}_2^*, \ldots, \mathfrak{r}_l^*$ 是 $\mathfrak{M}$ 中满足

$$\chi_{r_i}(\mathfrak{b}) = (\mathfrak{r}_i^*)^{-1}\,\mathfrak{b}\,\mathfrak{r}_i^* \qquad \text{对 } \mathfrak{M} \text{ 中所有 } \mathfrak{b} \tag{5}$$

的元素。那么,存在 $\mathfrak{M}$ 经 $\mathfrak{G}'$ 的、实现自同构类 $X(\alpha)$ 的扩张 $\mathfrak{G}$,当且仅当⁵)存在 $\mathfrak{M}$ 的中心的元素 $\mathfrak{b}_1, \mathfrak{b}_2, \ldots, \mathfrak{b}_l$,使得:每当对应方程

$$\prod_{i=1}^{N} c_i^{-1} r_{j_i}^{\varepsilon_i} c_i = e \tag{7}$$

在 $\mathfrak{E}$ 中成立时,方程

$$\prod_{i=1}^{N} \chi_{c_i}(\mathfrak{b}_{j_i})^{\varepsilon_i} = \mathfrak{e} \tag{6}$$

也成立。〔译注7〕

若扩张 $\mathfrak{G}$ 存在,则由定理 1 的推论,存在 $R$ 到 $\mathfrak{M}$ 里的同态 $a(r)$ 满足 (3)。这个同态由它在 $\mathfrak{r}_1, \mathfrak{r}_2, \ldots, \mathfrak{r}_l$〔此处 $\mathfrak{r}_1, \mathfrak{r}_2, \ldots, \mathfrak{r}_l$ 是 $\mathfrak{M}$ 中诱导出诸自同构 $\chi_{r_i}$ 的元素〕处的值完全确定。令 $a(r_i) = \mathfrak{r}_i$ 并令 $\mathfrak{b}_i = (\mathfrak{r}_i^*)^{-1}\mathfrak{r}_i$。$\mathfrak{b}_i$ 当然在中心里,因为 $\mathfrak{r}_i$ 与 $\mathfrak{r}_i^*$ 诱导同一个自同构。把 (7) 左端的表达式记作 $\rho$,则必有 $a(\rho) = a(e) = \mathfrak{e}$。但若利用 $(3, I)$ 以及 $a(r)$ 是同态这一事实,便得

$$\prod_{i=1}^{N} \chi_{c_i}(\mathfrak{r}_{j_i})^{\varepsilon_i} = \mathfrak{e}, \tag{8}$$

它等价于 (6)。〔译注7〕

反过来,设给定了元素 $\mathfrak{b}_i$,即给定了诱导自同构 $\chi_{r_i}$ 且满足 (8) 的诸 $\mathfrak{r}_i$。那么,若令

$$a(r) = \prod_{i=1}^{N} \chi_{c_i}(\mathfrak{b}_{j_i})^{\varepsilon_i}, \qquad \text{其中 } r = \prod_{i=1}^{N} c_i^{-1} r_{j_i}^{\varepsilon_i} c_i,$$

便得到 $a(r)$ 的一个定义;由 (8) 可见它是唯一的,而且是 $R$ 到 $\mathfrak{M}$ 里的同态。若

$$r = \prod_{i=1}^{N} c_i^{-1} r_{j_i}^{\varepsilon_i} c_i,$$

则

$$a(a^{-1}ra) = a\Bigl(\, \prod_{i=1}^{N} (c_i a)^{-1} r_{j_i}^{\varepsilon_i} (c_i a) \Bigr) = \chi_a(a(r)),$$

即 $(3, I)$ 满足。又有

$$\chi_{a^{-1}r_i a}(\mathfrak{b}) = \chi_a\bigl(\chi_{r_i}(\chi_{a^{-1}}(\mathfrak{b}))\bigr) = \chi_a(\mathfrak{r}_i^*)^{-1}\,\mathfrak{b}\,\chi_a(\mathfrak{r}_i^*),$$

故 $(3,\ II,\ a^{-1}r_i a,\ \mathfrak{b})$ 满足。但若 $(3, II, r, \mathfrak{b})$ 与 $(3, II, s, \mathfrak{b})$ 对所有 $\mathfrak{b}$ 满足,则 $(3, II, rs, \mathfrak{b})$ 对所有 $\mathfrak{b}$ 满足。于是 $(3, II)$ 满足〔因为形如 $a^{-1}r_i a$ 的元素生成 $R$〕,从而可以应用定理 1 的推论。

当 $\mathfrak{M}$ 的中心或只含单位元、或为整个群时,方程组 (6) 总有解。这些方程右端的表达式总代表中心元素,所以在中心只含单位元的情形,取每个 $\mathfrak{b}_i = \mathfrak{e}$ 即得解。若 $\mathfrak{M}$ 是阿贝尔群,取 $\mathfrak{b}_i = \mathfrak{r}_i^*$。对一般情形,我们必须能够求出全部关系 (7)。

## § 2. 一个群的诸关系之间的关系

设 $\mathfrak{E}$ 是带生成元 $e_1, \ldots, e_n$ 的自由群,$R$ 是含某些元素 $r_1, r_2, \ldots, r_l$ 的最小自共轭子群。商群将称为 $\mathfrak{G}'$。如前所示,在扩张问题中,重要的是能用关系 $r_1, r_2, \ldots, r_l$ 的共轭元之间的关系来表达 $\mathfrak{G}'$ 的结构。这个问题已被赖德迈斯特⁶)解决。〔译注8〕为得到另一个扩张定理(定理 4),有必要重述他的结论。

确切地说,问题可陈述如下。$R$ 由 $\mathfrak{E}$ 中所有形如 $a^{-1}r_i a$ 的元素生成;因此可以把 $R$ 看作自由群 $\Phi$($\Phi$ 带生成元 $E_{i,a}$)对某个自共轭子群 $P$ 的商群 $\Phi/P$。问题在于找出 $\Phi$ 中一组元素,使它们的共轭元生成 $P$。例如,$P$ 包含所有形如

$$E_{i,ab}^{-1}\, E_{i,a}\, E_{i,b} \tag{9}$$

的元素。〔译注9〕

我们这种求关系群 $P$ 的方法若要是能行的,就必须已知原群 $\mathfrak{G}'$ 的结构,或者等价地,有某种能行方法判定 $\mathfrak{E}$ 中给定元素是否属于 $R$。若这一点成立,就可以找到一个对 $\mathfrak{E}$ 中所有 $a$ 都有定义的能行函数 $v_a$:它在 $R$ 的每个陪集上取常值,取值在该陪集中,且满足 $v_e = e$。这些元素是各陪集的一组代表。若令 $r_a = v_a^{-1}a$,则对每个 $a$,$r_a$ 是一个关系($R$ 的成员)。

我们用条件

$$v_{a e_i} = v_a\, e_i\, r_{a, e_i}^{-1}$$

来定义 $r_{a, e_i}$。〔译注10〕那么,$R$ 由诸关系 $b^{-1} r_{a, e_i} b$ 生成。因为,设 $R'$ 是由这些关系生成的群,且它含 $r_c$,则由

$$r_{c e_i} = r_{c, e_i}\, e_i^{-1} r_c\, e_i,$$
$$r_{c e_i^{-1}} = r_{c, e_i^{-1}}\, e_i\, r_c\, e_i^{-1}, \tag{10}$$

〔$R'$ 便含 $r_{c e_i}$ 与 $r_{c e_i^{-1}}$〕。但 $R'$ 含 $r_e = e$;因此它含每个 $r_c$。对每个 $c$,我们已在同态 $t$($\Phi$ 到 $R$ 上)下为它选取了 $\Phi$ 中对应的元素,并定义自同构 $\chi_a$ 如下:

$$\chi_a(E_{i,b}) = E_{i,ba}. \tag{11}$$

于是可以用方程组

$$R_e = E,$$
$$R_{c e_i} = R_{c, e_i}\,\chi_{e_i}(R_c),$$
$$R_{c e_i^{-1}} = R_{c, e_i^{-1}}\,\chi_{e_i^{-1}}(R_c), \tag{12}$$

递归地定义 $R_c$;这样,不论 $k = e_i$ 还是 $k = e_i^{-1}$,都有

$$R_{ck} = R_{c,k}\,\chi_k(R_c). \tag{13}$$

我们的定义合法,当且仅当恒有

$$R_{(c e_i) e_i^{-1}} = R_{(c e_i^{-1}) e_i} = R_c.$$

这一点容易验证为真。〔译注11〕

既然每当 $k$ 是生成元或其逆时 (13) 与

$$r_{ck} = r_{c,k}\; k^{-1} r_c\, k \tag{14}$$

都成立,$R_c$ 在 $t$ 下就必须对应于 $r_c$。现在,对所有 $b, i$,元素 $t(E_{i,v_b}) = v_b^{-1} r_i v_b$ 与 $r_{v_b^{-1} r_i v_b}$ 位于 $P$ 的同一陪集。也就是说,

$$R_{v_b^{-1} r_i v_b}\, E_{i, v_b}^{-1} \tag{15}$$

〔译注12〕必须属于 $P$。用自同构 $\chi_a$ 作用,便看到所有形如

$$\chi_a(R_{v_b^{-1} r_i v_b}\, E_{i, v_b}^{-1}) \tag{16}$$

的元素都属于 $P$。$P$ 的结构现在可以由

**定理 3.** $R$ 的关系群 $P$ 是 $\Phi$ 的含所有形如 (9) 与 (16) 的元素的最小自共轭子群。

来描述。本定理只给出证明梗概。第一步是证明:对所有 $c, a$ 有

$$R_{a^{-1} c a} = \chi_a(R_c) \quad (\text{模 } P). \tag{17}$$

〔译注13〕为此,考虑使 (17) 对所有 $a$ 成立的那些 $\alpha$ 组成的集 $\mathcal{E}$。可以证明:若 $\alpha, \gamma$ 属于 $\mathcal{E}$,则 $\alpha\gamma$ 属于 $\mathcal{E}$。而由 (13),生成元 $e_i, e_i^{-1}$ 属于 $\mathcal{E}$。

现在令 $P_1$ 是 $\Phi$ 的由 (9)、(16) 生成的自共轭子群。我们证明 $R_c$ 在模 $P_1$ 的意义下与 $a$ 的选取无关,并且,若让 $K(r)$ 表示含 $R_c$ 的 $P_1$-陪集,则 $K(r)$ 给出 $R$ 到 $\Phi/P_1$ 上的一个同态。但显然存在由 $t$ 决定的、$\Phi/P_1$ 到 $R$ 上的同态 $t'$,满足 $t'(K(r)) = r$。这只可能在 $t'$ 与 $K$ 都是同构且 $P_1 = P$ 时发生。

为证明 $K$ 的这些性质,把使 $R_c$ 模 $P_1$ 与 $a$ 无关的那些关系 $r$ 的全体记作 $H$,并依次证明:

- I) 若 $r, s$ 属于 $H$,则 $R_{rs} \in K(r)K(s)$;
- II) 若 $r$ 属于 $H$,则 $R_{r^{-1}} \in K(r)^{-1}$;
- III) 若 $r$ 属于 $H$ 且 $k$ 是生成元或其逆,则 $R_{k^{-1} r k} = \chi_k(K(r))$(其中 $\chi_k$ 的意义经明显改写后沿用)。

I)、II)、III) 的证明都要用到 (17),也要用到 $P$ 在自同构 $\chi_a$ 下的不变性。〔译注13〕

现在回到扩张问题。对此,只有由 (15) 给出的那些关系是重要的。事实上我们有

**定理 4.** 在定理 2 中,可以把条件 (6) 换成下述条件:若 $\Phi$ 到 $R$ 上的同态 $\theta$ 由

$$\theta(E_{i,a}) = \chi_a(\mathfrak{r}_i^*) \tag{18}$$

确定,则对 $P$ 中每个元素 $Z$ 都必须有 $\theta(Z) = \mathfrak{e}$。〔译注14〕

同态 $\theta$ 把 § 2 的自同构 $\chi_a$ 变换为 § 1 的自同构 $\chi_a$,即

$$\theta(\chi_a(X)) = \chi_a(\theta(X)).$$

特别地,若 $\theta(X) = \mathfrak{e}$,则有

$$\theta(\chi_a(X)) = \chi_a(\mathfrak{e}) = \mathfrak{e},$$

于是形如 (16) 的元素都被 $\theta$ 映到单位元。剩下的只须证明 $\theta(Z) = \mathfrak{e}$ 对所有形如 (9) 的 $Z$ 成立:

$$\theta(E_{i,ab}^{-1} E_{i,a} E_{i,b}) = \chi_{ab}(\mathfrak{r}_i^*)^{-1}\, \chi_a(\mathfrak{r}_i^*)\, \chi_b(\mathfrak{r}_i^*)$$
$$= \chi_b\bigl(\, \chi_{ab^{-1}}(\mathfrak{r}_i^*)\; \mathfrak{r}_i^*\; \chi_{ab^{-1}}(\mathfrak{r}_i^*)^{-1} \;\cdots\, \bigr) = \chi_b(\mathfrak{e}),$$

后者由 (5) 得到。〔译注15〕我们已取 $\mathfrak{r}_i^* \mathfrak{b}_i = \mathfrak{r}_i$。这样,$\theta$ 把整个 $P$ 映到单位元,定理 2 的条件便得到满足。

## § 3. 循环扩张

当 $\mathfrak{G}'$ 是 $n$ 阶循环群时,我们取 $\mathfrak{E}$ 为带单个生成元 $a$ 的自由群,取 $R$ 为由 $\rho = a^n$ 生成的子群。代表元素 $v$ 可取为

$$\mathfrak{e},\ a,\ a^2,\ \ldots,\ a^{n-1}.$$

我们容易求得

$$r_{a^p, a} = e \quad \text{若 } p \ne -1 \ (\mathrm{mod}\ n), \qquad r_{a^{n-1}, a} = \rho.$$

若 $Q_{a^p}$ 是 $\Phi$ 中对应于 $a^{-p} \rho a^p$ 的元素,则

$$R_{a^p, a} = E \quad \text{若 } p \ne -1 \ (\mathrm{mod}\ n), \qquad R_{a^{-1}, a} = Q,$$

并且由方程组 (12) 得

$$R_{a^p} = E \qquad (0 \le p \le n-1),$$
$$R_{a^{n+p}} = Q_{a^p}.$$

因此表达式 (15) 就是

$$Q_{a^p}\, Q^{-1} \qquad (p = 0, 1, \ldots, n-1). \tag{19}$$

若 $\theta$ 是 $\Phi$ 的同态且 $\theta(Q_{a^p} Q^{-1}) = \mathfrak{e}$,则

$$\theta(Q_a) = \theta(Q_{a^2}) = \cdots = \theta(Q). \tag{20}$$

现在利用 (19)、(20),关于循环扩张的定理 4 变成

**定理 5.** $A$ 是群 $\mathfrak{M}$ 的一个自同构类。$A^n$ 是 $A$ 的第一个成为内自同构类的幂,$\phi$ 是 $A$ 中任一自同构。$\mathfrak{r}^*$ 是 $\mathfrak{M}$ 中诱导出内自同构 $\phi^n$ 的元素。那么,存在 $\mathfrak{M}$ 经 $n$ 阶循环群、实现自同构类 $A, A^2, \ldots$ 的扩张,当且仅当存在 $\mathfrak{M}$ 的中心的元素 $\mathfrak{b}$ 满足

$$\phi(\mathfrak{b})\, \mathfrak{b}^{-1} = \phi(\mathfrak{r}^*)\, \mathfrak{r}^{*-1}. \tag{21}$$

我们已取

$$\theta(Q) = \mathfrak{r}^* \mathfrak{b}^{-1}, \qquad \theta(Q_a) = \phi(\mathfrak{r}^* \mathfrak{b}^{-1}).$$

若令 $\phi(\mathfrak{b})\mathfrak{b}^{-1} = \pi(\mathfrak{b})$,则 $\pi$ 是 $\mathfrak{M}$ 的中心 $\mathfrak{z}$ 的一个(可能退化的,即未必真为自同构的)映射。对某些群,所有这样的 $\pi$ 都是退化的。所有阶为 2 的幂的循环群都是这种情形。在这些情形,若 $\phi(\mathfrak{r}^*) \mathfrak{r}^{*-1}$ 不在 $\pi(\mathfrak{z})$ 中,就会有不可实现的自同构类。

例如,设 $\mathfrak{M}$ 是 20 阶二面体群 $D_{10}$,由 $a, b$ 生成,带关系

$$a^{10} = b^2 = (ab)^2 = \mathfrak{e}.$$

这个群的中心由 $\mathfrak{e}$ 和 $a^5$ 组成。用

$$\phi(a) = a^3, \qquad \phi(b) = ba^5$$

定义自同构 $\phi$,〔译注17〕则

$$\phi^2(a) = a^{-1} = b^{-1}ab, \qquad \phi^2(b) = b = b^{-1}bb,$$

故 $\mathfrak{r}^*$ 可以取为 $b$。这时方程 (21) 成为

$$\phi(\mathfrak{b})\, \mathfrak{b}^{-1} = \phi(b)\, b^{-1} = a^5,$$

但对两个中心元素都有 $\phi(\mathfrak{b})\, \mathfrak{b}^{-1} = \mathfrak{e}$。

(1937 年 3 月 22 日收到。)

---

1) O. Schreier, *Über die Erweiterung von Gruppen* [Monats. f. Math. u. Phys. 34 (1926), 165–180].

2) R. Baer, *Erweiterung von Gruppen und ihren Isomorphismen* [Math. Zeitschr. 38 (1934), 375–416].

3) $\mathfrak{E}$ 的元素用斜体字母表示,$\mathfrak{M}$ 与 $\mathfrak{G}$ 的元素用德文(哥特)字母表示,$\mathfrak{G}/\mathfrak{M}$ 的元素用希腊字母表示。$\mathfrak{e}$、$\mathfrak{c}$、$\varepsilon$ 分别是这些群的单位元,$E$ 是 § 2 中 $\Phi$ 的单位元。

4) 若要诸条件是必要的,$\mathfrak{E}$ 为自由群这一点必不可少。一个平凡的例子表明:若要求 $a(r)$ 与定理中的函数 $m(a)$ 相关联,则 $\mathfrak{E}$ 至少不能任意取。设 $\mathfrak{G}$ 是 4 阶循环群 $\{b\}$,$\mathfrak{M}$ 是 2 阶循环群 $\{g\}$,取 $R$ 为 $\{b^2\}$ 且 $\chi_g(b^2) = b^2$。〔译注18〕那么本应有 $a(\mathfrak{e}) = \mathfrak{c}$。但 $a(\mathfrak{e}) = a(g^2) = b^2$。

5) 元素 $\mathfrak{b}_i$ 并非总存在,这一点可由贝尔给出的一个例子看出(引文同前,415 页)。§ 3 中将给出另一个例子。

6) K. Reidemeister, *Knoten und Gruppen* [Hamb. Abhandl. 5 (1926), 8–23].

## 译注

### 文本与翻译说明

1. 原文为纯扫描图像(无文本层),全文经 150–1200 dpi 分档渲染后由 RapidOCR 逐页识别;定理、公式的关键部位另以 600–1200 dpi 局部放大与词框逐字核对。数学式依 OCR 碎片加数学重构复原,凡不确定处在下节逐条标明。
2. 论文的交叉引用体系独特:公式按 (1)、(2)、… 编号,另附"(型别,变元)"式限定表,如 $(2, I, a, \mathfrak{b})$ 表示"公式 (2) 的 I 型,对变元 $a, \mathfrak{b}$ 成立";正文证明中即以 "$(3, I, a, r)$ 由 $(2, I, a, a(r))$、$(2, II, r)$……推出"的方式引用。译文完整保留这一体系,并在首次出现处于括号内照录原文标记。
3. 原书编者在翻印页右缘加有方括号行号标记([1]–[33] 之类),系编者批注之用,非论文内容,未予翻译;原刊页眉(The extensions of a group / A. M. Turing 及页码 357–367)亦不再出现。
4. 原文用 "shew"(show 的旧式英国拼法)、"self conjugate subgroup"(即正规子群)等旧术语,译文分别按现代通行语"证明/表明"、"自共轭子群(正规子群)"处理;"characteristics" 在引言中指扩张的示性数据(诱导自同构类等),译作"示性数据"。

### 背景与文化注

〔译注1〕本文 1937 年 3 月 22 日收到,刊于《组合数学》(Compositio Mathematica)第 5 卷(1938)。该刊 1934 年创刊于荷兰,是当时少数以群论、拓扑等"组合"学科为主战场的国际期刊。图灵署名"Cambridge, England"——此时他已自普林斯顿返回剑桥。

〔译注2〕"自共轭子群"(self conjugate subgroup)即今之正规子群(normal subgroup),译文保留旧称并于首次出现处加注。本篇术语沿用本卷《导论》译法:扩张(extension)、自同构、内自同构、中心、自由群、关系(即定义关系)。

〔译注3〕奥托·施赖埃尔(Otto Schreier,1901–1929),奥地利群论学家,1926 年在《月报》上奠定群的扩张理论(脚注 1),又与赖德迈斯特同创群的提升(lifting)方法;不幸英年早逝。莱因霍尔德·贝尔(Reinhold Baer,1902–1979),扩张理论的集大成者,脚注 2 所引 1934 年《数学杂志》论文系统研究了带给定诱导自同构的扩张。库尔特·赖德迈斯特(Kurt Reidemeister,1893–1971)以组合纽结理论闻名,脚注 6 所引《结与群》建立了"关系之间的关系"(即今所谓关系模 relation module 与佩弗恒等式)的理论;§ 2 的展开正是其方法的翻版,今称赖德迈斯特–施赖埃尔方法。

〔译注4〕$X(\gamma)$ 即扩张的经典不变量:对每个陪集 $\gamma \in \mathfrak{G}/\mathfrak{M}$,取其元素在 $\mathfrak{M}$ 上诱导的自同构所成的类(模去内自同构),得同态 $\mathfrak{G}/\mathfrak{M} \to \operatorname{Aut}(\mathfrak{M})/\operatorname{Inn}(\mathfrak{M})$。本卷《导论》中布里顿以 $\theta\colon G/N \to A/I$ 记之,含义相同。

〔译注5〕$\mathfrak{z}(\mathfrak{M})$ 表示 $\mathfrak{M}$ 的中心(原文以哥特字母排印,OCR 读作 "8(M)"、"3")。第一步先确定 $\mathfrak{G}/\mathfrak{z}(\mathfrak{M})$ 的可能结构,源自贝尔把一般情形化归为阿贝尔情形的纲领。

〔译注6〕$\mathfrak{E}$ 为自由群(脚注 4 强调:若要条件必要,自由性必不可少)。原文以哥特字母排印此群名,形近 "&",按德文花体 E 复原为 $\mathfrak{E}$;若原刊实为其他哥特字母,以原刊为准。

〔译注7〕(6)、(7)、(8) 的精确排印形式(指数、共轭方向、乘积限)未能自扫描件完全复原,译文按下述数学依据重构:$E_{i,a} \mapsto a^{-1} r_i a$(见 § 2 首段"R 由形如 $a^{-1}r_i a$ 的元素生成"及 (18) 的 $\theta(E_{i,a}) = \chi_a(\mathfrak{r}_i^*)$);(1) 的复合规则 $\chi_{ab} = \chi_b \circ \chi_a$;以及 (3, I) 的验证所需的方向匹配。详见"OCR 与印刷勘误"第 3 条。

〔译注8〕即"关系之间的关系"(relations between the relations):把 $R$ 写成自由群 $\Phi$(以 $E_{i,a}$ 为生成元,$E_{i,a}$ 对应共轭元 $a^{-1}r_i a$)模 $P$ 的商,则 $P$ 的生成元刻画了诸定义关系的全部相容性——这正是后来同调代数中"二阶同调"观念的先声。

〔译注9〕(9) 的形式 $E_{i,ab}^{-1}E_{i,a}E_{i,b}$ 系由定理 4 证明中对 $\theta(E_{i,ab}^{-1}E_{i,a}E_{i,b})$ 的计算(原刊 365 页,即本书第 19 页)反推确认,原文 (9) 行本身的 OCR 只有残片。

〔译注10〕即"因子集"式的定义:代表函数 $v$ 满足 $v_{ae_i} = v_a e_i r_{a,e_i}^{-1}$,偏差 $r_{a,e_i}$ 落在 $R$ 中。递推式 (10) 与 $\S 3$ 循环情形的实例($r_{a^p,a} = \mathfrak{e}$,$r_{a^{n-1},a} = \rho$)互相印证。

〔译注11〕此句判定递归定义的合法性(两种约化路径给出同一 $R_c$),原文仅称"容易验证为真"。

〔译注12〕(15) 的下标结构未能完全复原,此处按定理 4 的用法($\theta$ 须把 (15)、(16) 型元素映到单位元,而 $\theta(E_{i,a}) = \chi_a(\mathfrak{r}_i^*)$)与 § 3 实例 (19)(即 $Q_{a^p}Q^{-1}$)重构为 $R_{v_b^{-1} r_i v_b} E_{i,v_b}^{-1}$ 一类;若原刊下标不同,以原刊为准。

〔译注13〕(17) 的原印形式仅有 OCR 碎片 "Rax = Rx Xa(Ra)";按 III) 的模式 $R_{k^{-1}rk} = \chi_k(K(r))$ 与上下文重构为 $R_{a^{-1}ca} = \chi_a(R_c)$(模 $P$)。同理,$P$ 在 $\chi_a$ 下的不变性与 $K$-同态部分照数学脉络直译,细节请核对原刊 363–365 页。

〔译注14〕定理 4 陈述中"对 $P$ 中每个 $Z$ 都有 $\theta(Z) = \mathfrak{e}$"一句,原文该行为镜像乱码,按定理的用法与随后的证明("这样,$\theta$ 把整个 $P$ 映到单位元")复原。

〔译注15〕这一计算的中行在扫描件上无法辨认(含一个大括号与若干 $\chi$ 复合),译文以 "$\cdots$" 保留缺口;首行与末行("$= \chi_b(\mathfrak{e})$,由 (5) 得到")为 OCR 可辨部分。其数学内容是:把 $\chi_{ab}(\mathfrak{r}_i^*)^{-1}\chi_a(\mathfrak{r}_i^*)\chi_b(\mathfrak{r}_i^*)$ 归并成 $\chi_b(\ \cdots\ )$ 后,括号内由 (5)($\chi_{r_i}(\mathfrak{b}) = \mathfrak{r}_i^{*-1}\mathfrak{b}\mathfrak{r}_i^*$ 型的共轭关系)化为单位元。

〔译注16〕$\theta(Q)$ 两行的 OCR 仅余 "$\theta(Q) = \mathfrak{r}^{*-1}$"、"θ(Q_a) = ϕ(𝔯*𝔟^{-1})" 碎片;按 $\theta(E_{i,a}) = \chi_a(\mathfrak{r}_i^*)$ 应有 $\theta(Q_{a^p}) = \phi^p(\mathfrak{r}^*\mathfrak{b}^{-1})$ 之形,译文据此复原,与 (19)、(20)、(21) 的相容性已核对,但确切排印以原刊为准。

〔译注17〕$\phi(a) = a^3$、$\phi(b) = ba^5$ 两式原文扫描无法辨认(仅 $\phi(b)$ 行尾部可辨一个 "5")。指数依下述数学条件反推:$\phi^2 = b$-共轭(即 $\phi^2(a) = a^{-1}$,$\phi^2(b) = b$)要求 $\phi(a) = a^k$,$k^2 \equiv -1 \pmod{10}$($k = 3$ 或 $7$);$\phi(b)b^{-1}$ 须为中心元(等于 $a^5$)且 $(ba^5)^2 = \mathfrak{e}$。所取值使全文自洽,若原刊取 $k = 7$,道理相同。

〔译注18〕脚注 4 的例子:原文此处 OCR 混乱("Let β be the cyclic group {b} of order 4, the cyclic group {g} of order 2, and let be {b²} and xg(b²) = b²"),按文意应为:设(扩张的)$\mathfrak{M}$(或相应群)为 4 阶循环群 $\{b\}$ 之子群结构、$\mathfrak{M}$ 为 2 阶循环群 $\{g\}$、$R$ 对应 $\{b^2\}$,而 $\chi$ 把 $g$(或 $g$ 所在生成元)映到平凡作用;于是本应有 $a(\mathfrak{e}) = \mathfrak{c}$(把单位映到单位),但同态性强迫 $a(\mathfrak{e}) = a(g^2) = b^2 \ne \mathfrak{c}$——矛盾。具体字母归属请以原刊为准,此处仅保意。

### OCR 与印刷勘误

1. **记号复原总则** —— 原文的哥特字母($\mathfrak{G}, \mathfrak{M}, \mathfrak{E}, \mathfrak{r}, \mathfrak{b}, \mathfrak{e}, \mathfrak{z}$,及 $\S 2$ 的 $\Phi$)OCR 一律误读为 "③"、"@"、"M"、"≥"、"&"、"y"、"3"、"8" 等;希腊字母 $\chi$、$\phi$、$\rho$、$\pi$、$\Omega$ 常与 x、5、q、p、W 混淆;$\mathfrak{r}^*$ 的星号时隐时现。均按论文脚注 3) 所述的记号约定(斜体 = $\mathfrak{E}$ 的元素,德文花体 = $\mathfrak{M}, \mathfrak{G}$ 的元素,希腊文 = $\mathfrak{G}/\mathfrak{M}$ 的元素)复原。
2. **定理 1 的限定表** —— "(1; I, b, a, 𝔟)""(2, I, a, 𝔟)""(2, II, r)""(3, I, a, r)""(3, II, r, 𝔟)" 各标记系多次放大核对;b) 原文经 600 dpi 放大确认为 "every coset of 𝔐 in 𝔊 contains an element of m(𝔈)"(OCR 曾误作 "of R in ?")。
3. **(6)、(7)、(8) 的形式(不确定度:中)** —— 原印两式仅有乘积号与限 "N"、"i=1" 可辨;译文形式 $\prod c_i^{-1} r_{j_i}^{\varepsilon_i} c_i = e$(7)与 $\prod \chi_{c_i}(\mathfrak{b}_{j_i})^{\varepsilon_i} = \mathfrak{e}$(6)按 $E_{i,a} \leftrightarrow a^{-1}r_i a$ 对应及 (3, I) 验证所需方向重构;(8) 的 χ-作用对象 OCR 作 "xa()",按 $\mathfrak{r}_i = \mathfrak{r}_i^*\mathfrak{b}_i$ 之关系取 $\mathfrak{r}_{j_i}$(与 (6) 等价)。指数 $\varepsilon_i$、下标 $j_i$ 为依惯例补入。
4. **(9)–(17) 的 § 2 公式** —— (10) 的两行递推按 $v_{ae} = v_a e r_{a,e}^{-1}$ 推导复原(OCR 残片 "rce; = rc,e;e1reeie" 与之一致);(12)、(13) 中的 $R_{c,e_i}$-型因子(OCR 作 "Rvk")与 χ-下标经 § 3 实例反推;(14) 原印 OCR 作 "rck = rkk-1rck",按与 (13) 的对应及 (10) 的推导复原为 $r_{ck} = r_{c,k}\,k^{-1}r_c k$;(15) 见译注 12;(17) 见译注 13。
5. **定理 5 及其后的 $\phi$、$\mathfrak{b}$ 记号** —— OCR 把 $\phi$ 读作 "5"、"§",把 𝔟 读作 "3";"A is a class of automorphisms" 中 $A$ 的第一个成为内自同构类的幂印作 "$4w$",应为 $A^n$。正文"我们已取 $\mathfrak{r}_i^* \mathfrak{b}_i = \mathfrak{r}_i$"一句 OCR 作 "We have put r*1 = r",按定理 2 证明中 $\mathfrak{b}_i = (\mathfrak{r}_i^*)^{-1}\mathfrak{r}_i$ 的关系复原。
6. **二面体群例子** —— "ϕ(a) = a³"、"ϕ(b) = ba⁵"、"(21) 成为 … = a⁵" 的指数均为扫描所失、按数学反推(见译注 17);"a¹⁰ = b² = (ab)² = e" 与 "中心由 e 和 a⁵ 组成" 可自 OCR 直接确认(后者 "a" 处放大可见指数)。
7. **首页缺行** —— 原刊 357 页第 15–17 行在一次识别中整行丢失,经 600 dpi 逐行重扫补全("This case is treated entirely differently. In the present paper it is proposed to shew how Baer's method … can be used for any group M")。
8. **镜像乱码** —— 个别行被 OCR 自右向左读出(如 "( u g pup & u & ug p 1no .of)" 实为 "(for all r of R and 𝔟 of 𝔐)"),均已按语义复原。
9. **脚注 4 例子的字母** —— 见译注 18;此为全文唯一整句无法完全复原处。
