# 李群的有限逼近

**Finite Approximations to Lie Groups**

> 作者:艾伦·图灵(A. M. Turing)〔译注1〕
> 原载 *Annals of Mathematics*, Second Series, Vol. 39, No. 1(1938 年 1 月),pp. 105–111(1937 年 4 月 28 日收到,1937 年 9 月 29 日修订)
> 译自 `papers/Pure Mathematics. 2-North Holland $1992$.pdf` 第 25–31 页(书页 3–9)(个人学习用途)

我们将讨论"一个有限群可以在某种意义上逼近一个度量群的结构"这句话的一种确切含义。〔译注2〕由于有限线性变换群的若尔当定理¹,〔译注3〕很明显,我们不能指望用有限子群去逼近一般的李群。我将证明:甚至连"近似子群"("approximately subgroups")也无法用来逼近——事实上,可逼近的李群只有紧致阿贝尔群。解决问题的关键仍是若尔当定理,但它不能直接应用,必须为逼近群找到那样的表示,其次数只依赖于被逼近的群。

## 度量群的可逼近性

设 \(G\) 是带度量 \(D\) 的群,\(D\) 在左平移下不变,即对 \(G\) 中所有 \(x, y, \alpha\) 有 \(D(\alpha x, \alpha y) = D(x, y)\)。设 \(H_\varepsilon\) 是 \(G\) 的一个有限子集,其上定义了第二种乘法,使它对此构成一个群(若 \(a\)、\(b\) 属于 \(H_\varepsilon\),则它们作为 \(G\) 中元素的乘积记作 \(ab\);作为 \(H_\varepsilon\) 中元素的乘积记作 \(a \circ b\);\(a\) 作为 \(H_\varepsilon\) 中元素的逆记作 \([a]^{-1}\);\(G\) 与 \(H_\varepsilon\) 的单位元分别记作 \(e\)、\(e_\varepsilon\)),并设 \(G\) 的每个元素 \(x\) 与 \(H_\varepsilon\) 的某个元素 \(r(x)\) 相距不超过 \(\varepsilon\),且对 \(H_\varepsilon\) 中每对 \(a, b\) 有 \(D(a \circ b, ab) < \varepsilon\)。这时称 \(H_\varepsilon\) 是 \(G\) 的一个 **\(\varepsilon\)-逼近**(ε-approximation)。

一个群,若对每个 \(\varepsilon > 0\) 都有一个 \(\varepsilon\)-逼近,就称它是**可逼近的**(approximable)。

由定义立即可见,可逼近的群是全有界的,即条件紧的。〔译注4〕因此可以找到一个既左不变又右不变、且与原度量等价的度量(等价的意义是两种度量决定同一开集类)。今后我们总假定所取的度量是双向不变的,并把 \(x\) 与 \(y\) 的距离记作 \(D(x, y)\)。

J. v. 诺依曼²已证明:对一个条件紧的群,可以为群上每个(复值)连续函数定义一种平均值,使得(把 \(f(x)\) 的平均值记作 \(\int f(x)\,dx\))

$$\int (f(x) + g(x))\,dx = \int f(x)\,dx + \int g(x)\,dx, \qquad \int f(ax)\,dx = \int f(xa)\,dx = \int f(x)\,dx,$$

并且使得:若 \(\varepsilon > 0\)(且 \(f(x)\) 连续),则存在 \(G\) 中有限个元素 \(a_1, a_2, \ldots, a_\nu\),使

$$\Bigl|\, \frac{1}{\nu}\sum_{i=1}^{\nu} f(xa_i) - \int f(x)\,dx \,\Bigr| < \varepsilon \tag{1}$$

对 \(G\) 的每个元素 \(x\) 成立。〔译注5〕

在着手证明主要定理之前,我们先建立两个初等不等式。设函数 \(r(x)\) 属于 \(G\) 的某个 \(\varepsilon\)-逼近 \(H_\varepsilon\),则

$$D(r(x) \circ r(y),\, xy) \le D(r(x) \circ r(y),\, r(x)r(y)) + D(r(x)r(y),\, xr(y)) + D(xr(y),\, xy) < 3\varepsilon, \tag{2}$$

而对 \(H_\varepsilon\) 中任意 \(a, c\) 有

$$D(c \circ a \circ [c]^{-1},\, cac^{-1}) < 4\varepsilon, \tag{3}$$

因为

$$D(c \circ a \circ [c]^{-1},\, cac^{-1}) < D(ca[c]^{-1},\, cac^{-1}) + 2\varepsilon = D([c]^{-1}c,\, e) + 2\varepsilon$$
$$\le D([c]^{-1} \circ c,\, [c]^{-1}c) + D(e_\varepsilon,\, e) + 2\varepsilon \le D(e_\varepsilon,\, e) + 3\varepsilon$$
$$= D(e_\varepsilon^2,\, e_\varepsilon) + 3\varepsilon \le D(e_\varepsilon \circ e_\varepsilon,\, e_\varepsilon) + 4\varepsilon = 4\varepsilon.$$

**定理 1.** 设 \(G\) 是可逼近的群,并有一个次数为 \(n\) 的忠实连续矩阵表示。〔译注6〕则它可以用带同样次数 \(n\) 的忠实表示的有限群来逼近。

**引理.** 设 \(H_\eta\) 是群 \(G\) 的一个 \(\eta\)-逼近(其阶为 \(h_\eta\)),\(f(x)\) 是 \(G\) 上满足下述条件的连续函数:

$$|f(x) - f(x')| < \Delta \qquad \text{当 } D(x, x') < \eta \text{ 时},$$

则

$$\Bigl|\, \frac{1}{h_\eta}\sum_{h \in H_\eta} f(h) - \int f(x)\,dx \,\Bigr| \le 2\Delta. \tag{4}$$

我们令

$$\frac{1}{h_\eta}\sum_{h \in H_\eta} f(h) = B, \qquad \int f(x)\,dx = A,$$

那么给定 \(\varepsilon > 0\),存在 \(a_1, a_2, \ldots, a_\nu\) 使

$$\Bigl|\, \frac{1}{\nu}\sum_{i=1}^{\nu} f(xa_i) - A \,\Bigr| < \varepsilon \tag{5}$$

对 \(G\) 的每个元素 \(x\) 成立。在 (5) 中依次取 \(x\) 为 \(H_\eta\) 的每个元素,并把所得各不等式合并,便得

$$\Bigl|\, \frac{1}{\nu}\sum_{i=1}^{\nu} f(ca_i) - A \,\Bigr| < \varepsilon;$$

但 \(D(ca_i,\, c \circ r(a_i)) < 2\eta\),故 \(|f(ca_i) - f(c \circ r(a_i))| < 2\Delta\),因此

$$\Bigl|\, \frac{1}{h_\eta}\sum_{c \in H_\eta} \frac{1}{\nu}\sum_{i=1}^{\nu} f(c \circ r(a_i)) - A \,\Bigr| < \varepsilon + 2\Delta; \tag{6}$$

然而

$$\frac{1}{h_\eta}\sum_{c \in H_\eta} f(c \circ r(a_i)) = B,$$

于是 (6) 便给出 (4),因为 \(\varepsilon\) 是任意的。

## 定理的证明

不妨设所给表示不包含任何多于一次的不可约成分。令 \(\chi(x)\) 为该表示的特征标。这个函数将满足

$$\chi(x) = \int_G \chi(xy)\bar{\chi}(y)\,dy, \tag{7}$$
$$\chi(x) = \chi(cxc^{-1}), \tag{8}$$
$$|\chi(x)| \le n, \tag{9}$$

又由于它是忠实表示的特征标,当 \(x \ne e\) 时

$$\chi(x) \ne \chi(e) = n.$$

取 \(\varepsilon > 0\)。则存在某个 \(\alpha\),\(1 > \alpha > 0\),使当 \(D(x, e) \ge \varepsilon\) 时 \(|\chi(x) - n| > \alpha\)。〔译注7〕再取 \(\eta\) 满足 \(\varepsilon/16 > \eta > 0\),并使

$$|\chi(x) - \chi(x')| < \frac{\alpha}{50n^2} \qquad \text{当 } D(x, x') < 4\eta \text{ 时}, \tag{10}$$
$$|\chi(ay)\bar{\chi}(y) - \chi(ay')\bar{\chi}(y')| < \frac{\alpha}{50n} \qquad \text{对一切 } a,\ \text{当 } D(y, y') < 2\eta \text{ 时}, \tag{11}$$

然后取一个相应的 \(\eta\)-逼近 \(H_\eta\)。若令

$$\varphi(a) = \frac{1}{h_\eta}\sum_{c \in H_\eta} \chi(c \circ a \circ [c]^{-1}), \tag{12}$$

则

$$\frac{1}{h_\eta}\sum_{c \in H_\eta} \bigl|\, \chi(c \circ a \circ [c]^{-1}) - \chi(cac^{-1}) \,\bigr| < \frac{\alpha}{50n^2}, \tag{13}$$

因为由 (3) 有 \(D(c \circ a \circ [c]^{-1},\, cac^{-1}) < 4\eta\),从而每一被加项都小于 \(\alpha/(50n^2)\)。我们有

$$\frac{1}{h_\eta}\sum_{b \in H_\eta} \varphi(a \circ b)\bar{\varphi}(b) - \chi(a)$$
$$= \frac{1}{h_\eta}\sum_{b \in H_\eta} \bigl(\varphi(a \circ b)\bar{\varphi}(b) - \chi(a \circ b)\bar{\chi}(b)\bigr) + \frac{1}{h_\eta}\sum_{b \in H_\eta} \bigl(\chi(a \circ b) - \chi(ab)\bigr)\bar{\chi}(b)$$
$$+ \Bigl[\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \chi(ab)\bar{\chi}(b) - \int \chi(ay)\bar{\chi}(y)\,dy \Bigr] + \Bigl[\, \int \chi(ay)\bar{\chi}(y)\,dy - \chi(a) \Bigr]. \tag{14}$$

对 \(\chi(ay)\bar{\chi}(y)\) 应用引理并利用 (11),得

$$\Bigl|\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \chi(ab)\bar{\chi}(b) - \int \chi(ay)\bar{\chi}(y)\,dy \,\Bigr| \le \frac{2\alpha}{50n}; \tag{15}$$

而由 (9)、(10) 得

$$\Bigl|\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \bigl(\chi(a \circ b) - \chi(ab)\bigr)\bar{\chi}(b) \,\Bigr| \le \frac{\alpha}{50n}; \tag{16}$$

又〔由 (13) 及 \(|\varphi| \le n\)〕

$$\Bigl|\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \bigl(\varphi(a \circ b)\bar{\varphi}(b) - \chi(a \circ b)\bar{\chi}(b)\bigr) \,\Bigr| \le \frac{2\alpha}{50n}; \tag{17}$$

把 (14)、(15)、(16)、(17) 结合起来,便有

$$\Bigl|\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \varphi(a \circ b)\bar{\varphi}(b) - \chi(a) \,\Bigr| \le \frac{\alpha}{10n}. \tag{18}$$

$$\Bigl|\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \varphi(a \circ b)\bar{\varphi}(b) - \varphi(a) \,\Bigr| \le \frac{\alpha}{8n}. \tag{19}$$

现在,对 \(H_\eta\) 中每对 \(a, c\) 有 \(\varphi(a) = \varphi(c \circ a \circ [c]^{-1})\)。〔译注8〕因此这个函数可以写成特征标之和

$$\varphi(a) = \sum_{\lambda=1}^{M} \alpha_\lambda \chi_\lambda(a),$$

其中 \(\chi_\lambda\) 取遍 \(H_\eta\) 的不可约表示的特征标。由有限群表示的一般理论,

$$\frac{1}{h_\eta}\sum_{b \in H_\eta} \chi_\lambda(ab)\bar{\chi}_\lambda(b) = \mu_\lambda \chi_\lambda(a),$$

其中 \(\mu_\lambda\) 为常数。〔译注8〕于是 (19) 便成为

$$\Bigl|\, \sum_{\lambda=1}^{M} \alpha_\lambda(\bar{\alpha}_\lambda \mu_\lambda - 1)\chi_\lambda(a) \,\Bigr| \le \frac{\alpha}{8n}.$$

把不等式两边平方并对 \(H_\eta\) 求和,得

$$\sum_{\lambda=1}^{M} |\alpha_\lambda|^2\,|\bar{\alpha}_\lambda \mu_\lambda - 1|^2 \le \frac{\alpha^2}{64n^2}.$$

若用下式定义 \(\psi(a)\):〔译注9〕

$$\psi(a) = \sum_{\lambda=1}^{M} \beta_\lambda \chi_\lambda(a),$$

则它满足

$$\frac{1}{h_\eta}\sum_{b \in H_\eta} \psi(a \circ b)\bar{\psi}(b) = \psi(a), \tag{20}$$

并且

$$|\psi(a) - \varphi(a)|^2 \le \frac{4}{16n^2} \sum_{\lambda=1}^{M} |\alpha_\lambda|^2\,|1 - \alpha_\lambda|. \tag{21}$$

我们现在想从不等式 (21) 推出:函数 \(\psi(a)\) 与 \(\varphi(a)\) 在 \(H_\eta\) 的每一点上都相差很小。这要靠关系式 (19)、(20) 才能做到。事实上

$$\Bigl|\, \frac{1}{h_\eta}\sum_{b \in H_\eta} \bigl(\psi(a \circ b)\bar{\psi}(b) - \varphi(a \circ b)\bar{\varphi}(b)\bigr) \,\Bigr| \le \frac{1}{4n}\Bigl(\frac{\alpha}{8n} + \frac{\alpha}{10n}\Bigr), \tag{22}$$

因为对 \(H_\eta\) 中每个 \(b\) 有 \(|\psi(b)| \le n\)、\(|\varphi(b)| \le n\)。现在把 (18)、(20)、(22) 结合起来,便得

$$|\psi(a) - \chi(a)| < \frac{\alpha}{10n}.$$

这就蕴涵 \(\psi(e_\eta) = \chi(e) = n\),并且当 \(D(a, e) \ge \varepsilon\) 时 \(\psi(a) \ne \chi(e) = \psi(e_\eta)\)。〔译注10〕于是 \(\psi(a) = \psi(e_\eta)\) 只对某个自共轭(正规)子群 \(N\) 中的元素成立,而 \(N\) 整个落在离 \(G\) 的单位元不超过 \(\varepsilon\) 的范围内。商群有一个次数为 \(n\) 的忠实表示,我将证明它可取为 \(G\) 的一个 \(\varepsilon\)-逼近。我们在 \(N\) 的每个陪集中各选一个元素作为该陪集的代表,并定义函数 \(v(a)\)(\(a\) 属于 \(H_\eta\))为 \(a\) 所在陪集的代表。元素 \(v(a)\) 的全体称为 \(K\)。令 \(v(a) \otimes v(b) = v(a \circ b)\),\(K\) 关于乘法 \(\otimes\) 构成一个群。对 \(H_\eta\) 中每个 \(a\),存在 \(N\) 中元素 \(m\) 使 \(v(a) = a \circ m\),因此

$$D(a, v(a)) \le D(a, am) + D(am, a \circ m) < \varepsilon + \eta.$$

从而若令 \(R(x) = v(r(x))\),便有

$$D(R(x), x) \le D(v(r(x)), r(x)) + D(r(x), x) < (\varepsilon + \eta) + \eta < \varepsilon,$$

并且

$$D(v(a) \otimes v(b),\, v(a)v(b)) \le D(v(a \circ b), a \circ b) + D(a \circ b, ab) + D(ab, v(a)v(b)) < 3(\varepsilon + \eta) + \eta < \varepsilon,$$

这就表明 \(K\) 是 \(G\) 的一个 \(\varepsilon\)-逼近。

**定理 2.** 可逼近的李群是紧致且阿贝尔的。

**引理.** 连通群的闭子群其指数不能大于 1。

设 \(H\) 是 \(G\) 的闭子群且指数为 \(i\),\(1 < i < \infty\)。则 \(G - H\) 非空且是闭的,因为它是有限个闭集(即 \(H\) 的各陪集)之和。于是 \(G\) 是两个不相交的非空闭集之和,因此不连通。

若 \(G\) 是紧李群,它就不能有异于全群的正测度闭子群。

**定理的证明.** 可逼近的李群是完备且条件紧的,即它是紧致的,因此〔由 v. 诺依曼³〕它是一个线性变换群,设其次数为 \(n\)。由定理 1,我们可以用带 \(n\) 次线性变换表示的有限群 \(H_\eta\) 逼近它。但由若尔当定理⁴,〔译注3〕每个有限线性变换群都有一个阿贝尔子群,其指数不超过某个只依赖于次数的界 \(Z(n)\)。令 \(A_\eta\) 是 \(H_\eta\) 中的这个阿贝尔子群。那么存在 \(H_\eta\) 中有限个元素 \(c_1, c_2, \ldots, c_N\)(\(N \le Z(n)\)),使 \(H_\eta\) 的每个元素都形如 \(c_i \circ a\),其中 \(a\) 属于 \(A_\eta\)。对 \(G\) 中任意 \(x\),我们有

$$D(x, r(x)) < \eta,$$
$$r(x) = c_i \circ a, \qquad a \in A_\eta,\ i \le N,$$
$$D(c_i a, c_i \circ a) < \eta.$$

因此 \(G\) 的每个元素都形如 \(c_i a d\),其中 \(d\) 与 \(G\) 的单位元相距不超过 \(2\eta\),且 \(i \le N\)。这些点 \(ad\) 必定构成一个测度至少为 \(1/Z(n)\) 的集 \(E_\eta\)。现在取 \(x = ad\)、\(y = a'd'\):

$$D(xy, yx) = D(ada'd', a'd'ad)$$
$$\le 2D(d, d') + D(a \circ a', aa') + D(aa', a \circ a') + D(aa', a'a) < 6\eta. \tag{23}$$

于是在乘积群 \(G \times G\) 中,我们有一个测度至少为 \(1/(Z(n))^2\) 的点对 \((x, y)\) 的集 \(E_\eta \times E_\eta\),在其中 \(D(xy, yx) < 6\eta\)。现在取趋于 0 的序列 \(\eta_i\),并令 \(F_i = E_{\eta_i} \times E_{\eta_i}\)、\(E = \bigcap_i F_i\)。由于诸 \(F_i\) 是递降序列,故 \(mE \ge 1/(Z(n))^2\)。若 \((x, y)\) 属于 \(E\),则对每个 \(i\) 有 \(D(xy, yx) < 6\eta_i\);但 \(i\) 是任意的,所以 \(D(xy, yx) = 0\),即 \(xy = yx\)。

现在令 \(N_x\) 为使 \(xy = yx\) 的那些 \(y\) 组成的集,即 \(x\) 的正规化子。则

$$mN_x = \int_{N_x} dc \ge mE \ge \frac{1}{(Z(n))^2}.$$

因而在一个正测度的 \(x\)-集上 \(mN_x > 0\)。但若 \(mN_x > 0\),由引理便有 \(N_x = G\),因为 \(N_x\) 显然是闭的。这表明 \(G\) 的中心具有正测度;再次应用引理,便知 \(G\) 是阿贝尔的。

PRINCETON UNIVERSITY.

---

1 这条定理是说:有限线性变换群有一个自共轭的阿贝尔子群,其指数不超过某个只依赖于次数的界。

2 J. v. Neumann, *Zum Haarschen Mass in topologischen Gruppen*, Compositio Mathematica, vol. 1 (1934), pp. 106–114;或者,J. v. Neumann, *Almost periodic functions in a group*, Transactions of the American Mathematical Society, vol. 36 (1934), pp. 445–492(请记住:条件紧群上的每个连续函数都是 a.p. 的)。若读者愿意以某种方式限制群并使用别的平均值,则只需验证不等式 (1)。

3 J. v. Neumann, *Die Einführung analytischer Parameter in topologischen Gruppen*, Annals of Mathematics, vol. 34 (1933), pp. 170–190.

4 A. Speiser, *Theorie der Gruppen von endlicher Ordnung*, (Berlin 1927) 2nd ed., p. 215.

## 译注

### 文本与翻译说明

1. 原文为纯扫描图像(无文本层),全文经 150–1200 dpi 分档渲染后由 RapidOCR 逐页识别;公式密集段落(引理证明、特征标演算 (12)–(22))另以 300–1200 dpi 局部放大逐词框核对。数学式依 OCR 碎片加数学重构复原,不确定处在下节逐条标明。
2. 原文定理、引理、公式编号 (1)–(23) 一一保留;节标题"Approximability of metrical groups""Proof of the theorem"均照原样设节。表示论术语按本卷《导论》译法:特征标(character)、忠实表示(true representation)、不可约成分(irreducible component)、共轭、自共轭子群(正规子群)。
3. 原书编者在翻印页右缘加有方括号行号标记([1]–[33] 之类),系编者批注之用,非论文内容,未予翻译;原刊页眉(ANNALS OF MATHEMATICS / FINITE APPROXIMATIONS TO LIE GROUPS / A. M. TURING 及页码 105–111)亦不再出现。
4. "条件紧"(conditionally compact)即全有界;原文两种说法并用("totally bounded i.e. conditionally compact")。

### 背景与文化注

〔译注1〕本文写作时图灵正在普林斯顿大学随阿隆佐·丘奇攻读博士学位(1936–1938 年),文末署名 PRINCETON UNIVERSITY;1937 年 4 月投稿、9 月修订,1938 年 1 月刊于《数学年刊》(Annals of Mathematics)第二系列 39 卷 1 期。

〔译注2〕"哪种群可以用有限群逼近"是 S. 乌拉姆(Stanisław Ulam)提出的问题(见本卷布里顿《导论》)。图灵的答案出人意料:对李群而言,只有紧致阿贝尔群可逼近——非交换性哪怕"近似地"也不可能。这一"有限群近似"思想在二十世纪末以"sofic 群""超有限积"等名义重新活跃,图灵 1938 年的此文常被引为该方向的先声。

〔译注3〕若尔当定理(Camille Jordan,1878):有限线性变换群必有指数受限于次数的阿贝尔正规子群。论文脚注 1 转述了它,脚注 4 指出的施派泽(A. Speiser)《有限阶群论》第 215 页则是当时的标准出处。文中量 $Z(n)$ 即这个只依赖次数 $n$ 的指数界。

〔译注4〕"条件紧"与完备性合用即得紧性——定理 2 证明的第一步("An approximable Lie group is complete and conditionally compact, i.e. it is compact")用的正是这一点;度量群的完备化与双向不变度量的替换是 v. 诺依曼拓扑群理论的标准手段。

〔译注5〕这里引述的是 v. 诺依曼为条件紧群上的连续函数构造的不变平均值(脚注 2 所引两文),亦即紧群上规范化哈尔测度的先声;不等式 (1) 是"有限平均一致逼近平均值"这一性质的离散化身,整篇证明的引擎。图灵特别提醒:读者若不愿引用 v. 诺依曼的平均值,只需直接验证 (1)。

〔译注6〕"true representation"直译"真表示",即忠实(一一)表示;为免与"真"字的其他含义混淆,译文作"忠实表示"并于首次出现处保留原词。定理 1 的内容:逼近有限群不仅自身要存在,还须带上次数不变($n$ 次)的忠实表示——这正是若尔当定理得以应用的接口。

〔译注7〕这一步用到 $|\chi(x)| \le n$($n$ 为表示次数)、$\chi(e) = n$、忠实性($x \ne e$ 时 $\chi(x) \ne n$)以及紧性,故可在紧集 $\{x: D(x,e) \ge \varepsilon\}$ 上取到与 $n$ 的正间隔 $\alpha$。

〔译注8〕此两句(φ 为 $H_\eta$ 上类函数、可展开为不可约特征标之和;以及 $\mu_\lambda$-常数关系)为按 OCR 碎片与有限群特征标正交关系复原,原文排印细节未能完全辨认:按标准理论 $\mu_\lambda$ 应等于相应不可约表示次数的倒数。见勘误第 4 条。

〔译注9〕$\psi$ 的构造意在把 $\varphi$ 的特征标展开式系数 $\alpha_\lambda$ "舍入"为使 (20) 严格成立的取值(由 (19) 的平方和估计,诸 $\alpha_\lambda$ 已接近所需值)。原文此处的定义式、以及 (20)、(21) 的精确排印形式未能自扫描件复原,译文按数学上下文重构,见勘误第 5 条。

〔译注10〕证明收尾的机制:$|\psi - \chi| < \alpha/10n$ 且 $\chi$ 在 $\{D(a,e) \ge \varepsilon\}$ 上与 $n$ 相差至少 $\alpha$,故 $\psi(a) = n$ 只可能发生在离单位元 $\varepsilon$ 之内;使 $\psi$ 取平凡值的元素组成正规子群 $N$,商群 $K = H_\eta/N$(以陪集代表实现)既继承 $n$ 次忠实表示,又是 $G$ 的 $\varepsilon$-逼近。

### OCR 与印刷勘误

1. **定义中 $D(a \circ b, ab)$ 的不等号(不确定度:低)** —— OCR 读作 "D(aob, ab) > ε";按定义之意及 (2)、(3) 中该式的用法,应为 "$<$",译文已改。
2. **平均值公式的归一化(不确定度:低)** —— $B$ 的定义式、(4)、(6) 中求和号前的 $\frac{1}{h_\eta}$(或 $\frac{1}{\nu}$)在 OCR 中屡屡丢失,依引理叙述"(of order $h_\eta$)"及证明的逻辑复原;均值公式的第二个等式组($\int f(ax)dx = \int f(xa)dx = \int f(x)dx$)在图像上成两行排印,积分号下标 $G$ 仅在一处可辨,译文统一写作不带下标的 $\int$(与正文 "denoting the mean of f(x) by ∫f(x)dx" 一致)。
3. **(1) 与 (5) 的平移方向(不确定度:中)** —— (1) 行 OCR 仅余碎片 "(cai)"、"f(x) dx"、"ε";由引理证明中代入 $x = c \in H_\eta$ 后出现的项 $f(ca_i)$、$D(ca_i, c \circ r(a_i))$ 判定,(1)、(5) 中的平移为右平移 $xa_i$。若原刊实为 $a_ix$,不影响证明的正确性,但请以原刊为准。
4. **(7) 的归一化因子(不确定度:高,敬请留意)** —— (7) 在图像上清晰可辨为 "$\chi(x) = \int_G \chi(xy)\bar{\chi}(y)dy$",无可见的因子。但按紧群规范化正交关系,$n$ 次不可约表示的特征标满足 $\int \chi(xy)\bar{\chi}(y)dy = \chi(x)/n$;要与原式一致,须平均值的归一化与 $n$ 相抵(或原刊在 $\int$ 前有因子 $n$ 为扫描所失)。因 (14) 的最后一项方括号正是靠 (7) 消去,此式在证明中按字面使用,译文照录原形并注明疑点。复共轭记号 $\bar{\chi}$ 在扫描中不可见,系按正交关系的惯例恢复。
5. **特征标演算段 (14)–(22)(不确定度:高)** —— 这一段各显示式的内部结构(诸 $\alpha_\lambda$、$\mu_\lambda$、$\beta_\lambda$ 的上下标、极小记号 min 的用法)在扫描件上无法逐字辨认。译文中的处理:(14) 按"四项分解 + 分别由 (17)、(16)、(15)、(7) 控制"重构,右端常数经数学核算与 (15) $2\alpha/50n$、(16) $\alpha/50n$、(17) $2\alpha/50n$ 之和恰为 (18) 的 $\alpha/10n$ 吻合;(19) 的转化式与平方和式按有限群特征标正交性重构((19)-转化式中 OCR 可辨 "α_λ(α_λ−1)χ_λ(a)",译文作 $\alpha_\lambda(\bar{\alpha}_\lambda\mu_\lambda - 1)$,两者相差的共轭号与 $\mu_\lambda$ 为扫描所失);(21) 的 OCR 碎片为 "Min(|α_λ|, |1−α_λ|)" 与 "≤ 4Σ|α_λ|²|1−α_λ| / 16n²",已按此拼合并注明;(22) 右端的最终数值化简(OCR 碎片 "…= …/20…")未能确认,译文保留未化简形式。需要精确引用者请对照《数学年刊》原刊 39 卷 108–109 页。
6. **结尾两式的不等号(照录存疑)** —— "$D(R(x), x) < (\varepsilon + \eta) + \eta < \varepsilon$" 与 "$\cdots < 3(\varepsilon + \eta) + \eta < \varepsilon$" 系 OCR 原样($\varepsilon/16 > \eta$ 时数值上不可能严格小于 $\varepsilon$);疑原刊此处 $\varepsilon$ 为字号相近的另一记号或有系数为扫描所失。译文照录,并以〔 〕不加改动,读者引用时请核对原刊 110 页。
7. **$\psi(e_\eta) = \chi(e) = n$ 一句** —— OCR 原文 "This implies that &(en) = x(e) = n and that if D(a, e) ≥ e then &(a) ≠ x(e) = &(e,)",其中 "&"、"§" 均为 $\psi$ 的误读,"(e,)" 为 $e_\eta$ 的误读;已按上下文复原。
8. **度量群定义行** —— "D(ac, ay) = D(c, y) for all α, y, α" 中变量名有 OCR 混乱,应为 $D(\alpha x, \alpha y) = D(x, y)$ 对所有 $x, y, \alpha$。
9. **脚注 2、3 的德文题名** —— "Zum Haarschen Mass"、"Die Einfuhrung analytischer Parameter" 中 "Mass"、"Einfuhrung" 为原文省略元音变音符的排印(马赫 Haarsch/哈尔 Haar),译文照录 "Haarschen";"Einfuhrung" 应读作 "Einführung"。
10. **若干名词的 OCR 噪声** —— "approsimated byfinitegroups"(approximated by finite groups)、"cani defne"(can define)、"gcnerated"(generated)、"cquations"(equations)、"porwer"(power)、"rcducing"(reducing)、"shew/shcw"(show 的旧式拼法)等,均按正确拼写翻译,不再一一出注。
