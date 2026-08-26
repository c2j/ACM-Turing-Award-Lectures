# 论差 π(x)−li x

**On the Difference π(x)−li x**

> 作者:A. 科恩(A. M. Cohen)、M. J. E. 梅休(M. J. E. Mayhew)
> 原载 *Proceedings of the London Mathematical Society* (3) 18 (1968),pp. 691–713(1965 年 9 月 21 日收到,1967 年 1 月 4 日修回);后收入《图灵文集·纯数学》卷(J. L. Britton 编,North-Holland,1992)"相关论文"部分〔译注1〕
> 译自 `papers/Pure Mathematics. 2-North Holland (1992).pdf` 第 205–227 页(书页 183–205;即期刊页 691–713)(个人学习用途)

## 1 引言

本文基于 A. M. 图灵的想法;这些想法记录在一部未发表、且个别处并不准确的手稿之中。我们复述了图灵导言的一部分,并就实质内容沿用他的最初几条引理,但在引理 6 处与他的做法有所分歧。

"设 π(x) 为小于 x 的素数个数,li x 为 x 的'对数积分',定义为

$$\operatorname{li}x=\lim_{\varepsilon\to+0}\Bigl\{\int_0^{1-\varepsilon}+\int_{1+\varepsilon}^{\infty}\Bigr\}\frac{du}{\log u}.$$

在这一问题(如同在其他记号问题)上,我们遵循英厄姆(Ingham)(文献 1)。我们打算考察 π(x)−li x 在何处为正。当 x 小于约 1.42 时该量为正,从这里直到 10³ 它都是负的〔译注2〕。数据暗示

$$\pi(x)-\operatorname{li}x\sim -c/\log x\qquad(x\to\infty),$$

不过常有例外。论证按黎曼假设之真伪分情形进行。若黎曼假设成立,斯克斯(Skewes)〔译注3〕已证明(文献 3)

$$\pi(x)-\operatorname{li}x>0\quad\text{对某个 }x,\ 2<x<10^{10^{10^{34}}};$$

而当黎曼假设不成立时,他也证明了(文献 4)

$$\pi(x)-\operatorname{li}x>0\quad\text{对某个 }x,\ 2<x<10^{10^{10^{963}}}.$$

† 这一结果是图灵所不知道的,它发表于图灵去世之后。图灵在手稿中只引用了较早的那个结果。
‡ 我们的数字。图灵用的是 exp exp(661)。

在本文中,我们打算建立:**存在某个 x 使 π(x)>li x,且 2<x<exp exp(1236)**‡——无须以黎曼假设为前提。我们还将为进一步借助大规模计算改进这一界做好准备;对整个方法至关重要的是这样一个事实:黎曼假设已在区域

[184]

|γ|<1468(蒂奇马什 Titchmarsh,文献 5)内得到检验〔译注4〕。本文作者们还利用了如今关于黎曼 ζ 函数早期零点的更多知识(见哈塞尔格罗夫与米勒 Haselgrove and Miller,文献 9)。哈塞尔格罗夫计算的零点,其精度几乎比哈塞尔格罗夫–米勒表格提高了一倍;后续计算采用的就是这批零点。

图灵在其导言的后文把方法概述如下:

"必须使用函数 Π(x)〔译注5〕与 log ζ(s) 这一点使论证略显复杂。方法的总体轮廓,可以通过处理一个类似的问题来说明,即求 ϑ(x)>x 成立的位置。由于

$$\psi(x)=\vartheta(x)+\vartheta(x^{1/2})+\vartheta(x^{1/3})+\vartheta(x^{1/4})+\cdots,$$

以及 ψ(x)∼x,这实质上等价于问 ψ(x)>x+x^{1/2} 在何处成立。现在

$$G(t)=-\sum_\rho \frac{e^{(\rho-1/2)t}}{\rho}\sim\log(1-1/t^2)\ \text{之类的和},$$

于是问题实质上化为:对什么样的 t,不等式

$$G(t)=-\sum_\rho \frac{e^{(\rho-1/2)t}}{\rho}>1$$

成立,求和遍及复零点?

'可以考虑形如下式的各种表达式

$$I=\int_{-\infty}^{\infty}G(t)f(t-t_0)\,dt.$$

令 F 为 f 的傅里叶变换,则有〔译注6〕

$$I=\int G(t)f(t-t_0)\,dt=\int F(\gamma)\widehat{f}(\gamma)\,d\gamma$$

一类的表示。若 f(t) 当 t 为正时恒正,并足够快地递减到零,便可以反过来由 I 的值推知不等式 G(t)>1。例如,只须有

$$\int_{-\infty}^{\infty}G(t)f(t-t_0)\,dt>\text{某一正常数},$$

即可推断存在满足 0<t<A 的某个 t 使 G(t)>1。使 I 充分大且为正的那个 t,须用丢番图逼近求得。作逼近时,我们力图调整具有小 γ 的那些项的相位使之达到最大,并安排其余未加调整的项都很小。因此我们希望 F(u) 在较大的 γ 处很小。英厄姆(文献 6)取

$$f(t)=\{(\sin\beta t)/t\}^2,$$

从而保证:当黎曼假设成立时,只有有限多项不为零。本文改用

$$f(t)=\{(\sin\beta t)/t\}^4\exp(-\alpha^2t^2).$$

这一函数并不具有使某些项恰好消失的性质;但只要 α 很小,靠后的项便极其微小。现行函数还有若干优点(它促使积分迅速收敛,便于由 I 的值推断关于 G(t) 的不等式):因子 exp(−α²t²) 还使 F(u) 成为整函数(否则它将只在两个方块与两个直角形区域上正则);使用 (sin βt)/t 的更高次幂会使 f 从大值到小值的过渡相当更陡,带来可观的数值改进。'

谨向已故的 C. B. 哈塞尔格罗夫博士致谢,是他向我们中的一位提出了这个问题;感谢利特尔伍德(Littlewood)教授对本文写作的帮助与不断的鼓励;感谢英厄姆先生与斯坦因(P. Stein)教授对图灵手稿所作的若干实质性订正;最后感谢审稿人指出初稿中的一处严重失误并提出许多宝贵建议。"

[185]

## 2 一般引理

设 f(t) 为偶函数,在带域 $|\Im t|\le\lambda$ 内正则,且对每个正数 $\varepsilon$ 满足增长条件

$$f(t)=\begin{cases}O(e^{-(\mu-\varepsilon)s)},&s\to+\infty,\\ O(e^{-(\lambda-\varepsilon)s}),&s\to-\infty,\end{cases}$$

其中 $\lambda>0$,$\mu>0$,$s=\Re t$〔译注7〕。定义

$$F(u)=\int_{-\infty}^{\infty}e^{-iut}f(t)\,dt.\tag{2.1}$$

再设 h(x) 在每个有限区间 $(0,X)$ 上是有界变差函数,s=σ+iτ,且下列条件满足:

(i) φ(s) 正则,并在 0≤σ≤2 上一致地为 O(e^{−δ|τ|}),其中 δ>0 固定;
(ii) 当 x→0 与 x→∞ 时 h(x)=o(x^θ)(θ 为某固定数);
(iii) 积分 ∫₀^∞ x^{−3/2}|h(x)|dx 收敛。

〔条件 (i)–(iii) 的文字此处 OCR 有缺损,系按上下文复原,见译注7。〕于是,若 t₀ 为实数,则有

**引理 1.**

$$\int_0^\infty h(e^t)f(t-t_0)\,dt=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}\phi(s)\,F(s-1)\,e^{(s-1)t_0}\,ds,$$

其中 $\phi(s)=\displaystyle\int_0^\infty x^{-s}\,dh(x)$。

证. 当 σ=2 时,对 (2.1) 分部积分并利用条件 (i),可得

$$\phi(s)=s\int_0^\infty h(x)\,x^{-s-1}\,dx.$$

把它代入引理右端,得到一个二重积分。由条件 (i) 与 (iii),该二重积分绝对收敛,故可交换积分次序;积分遂化为

$$\int_0^\infty x^{-1}h(x)\chi(x)\,dx,$$

其中

$$\chi(x)=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}x^{s-1}F(s-1)e^{(s-1)t_0}\,ds.$$

现在写 x=e^u,则依据 (2.1) 与条件 (i) 所含的 s 增长性限制,可以把积分直线移到 σ=0 处,再用傅里叶反演公式得到 χ(x)=f(t−t₀),引理 1 得证。□

我们用关系式

$$f(t)=f_1(t)f_2(t),\tag{2.3}$$

定义 f,其中

$$f_1(t)=\{(\sin\mu t)/\mu t\}^4,\qquad f_2(t)=\exp(-\alpha^2t^2),\tag{2.4}$$

而 μ>0,α>0。于是

$$F(u)=(2\pi)^{-1/2}\int F_1(\xi)F_2(u-\xi)\,d\xi,\tag{2.5}$$

其中

$$F_j(\xi)=(2\pi)^{-1/2}\int e^{i\xi t}f_j(t)\,dt\qquad(j=1,2),$$

以及

$$K(x)=\begin{cases}\dfrac23-\bigl(1-|x|\bigr)^2+\dfrac12\bigl(1-|x|\bigr)^3,&0\le|x|\le1,\\[4pt]\dfrac16\bigl(2-|x|\bigr)^3,&1\le|x|\le2,\\[4pt]0,&2\le|x|.\end{cases}\tag{2.6}$$

结果 (2.5) 及 F₂ 的显式公式可在蒂奇马什的书中找到(文献 7,§51、177),K(x) 的公式则可通过沿一条在原点处凹进的半圆围道积分求得〔译注8〕。我们注意 K(x)≥0,K(x) 在 x=0 处取得最大值。这意味着 F₁(ξ)≥0,其最大值为 F₁(0)。我们还需要 |F₂(u−ξ)| 当 ξ 变动时的最大值,即

$$\alpha^{-1}\exp(y^2/2\alpha^2)=M,\quad\text{其中 }u=\sigma+iy.$$

下面我们对 F(u) 与 F(iu) 推出几个不等式;下文中的 f、F 均指上文所定义的函数。

**引理 2.** 若 u=σ+iy,则

1. |F(u)|≤α⁻¹exp(y²/2α²);
2. |F(u)|≤√(2π)·exp(y²/2α²)/2μ;
3. |F′(u)|≤(αμ)⁻¹exp(y²/2α²);
4. $\Bigl|\displaystyle\int_{c-i\infty}^{c+i\infty}F(u)\,du\Bigr|\le\sqrt{2\pi}\,\exp(c^2/2\alpha^2)$(c 为实数);
5. |F(u)|≤α⁻¹exp[{y²−(|u|−4μ)²/2α²}](当 |u|>4μ)。

证. 由 (2.5),

$$|F(u)|=(2\pi)^{-1/2}\Bigl|\int F_1(\xi)F_2(u-\xi)\,d\xi\Bigr|\le(2\pi)^{-1/2}M\int|F_1(\xi)|\,d\xi=Mf_1(0).$$

因 f₁(0)=1,得 (i)。

其次仍由 (2.5),

$$|F(u)|\le(2\pi)^{-1/2}\int|F_1(\xi)|\,|F_2(u-\xi)|\,d\xi\le(2\pi)^{-1/2}M\int|F_1(\xi)|\exp\{-(\sigma-y)^2/2\alpha^2\}\,d\xi=\sqrt{2\pi}\exp(y^2/2\alpha^2)/2\mu,$$

这就证明了 (ii)。

在 (2.5) 中令 ξ=u−ξ′ 并对 u 求导,得

$$F'(u)=(2\pi)^{-1/2}\int F_2'(u-\xi)F_1(\xi)\,d\xi,$$

从而

$$|F'(u)|\le(2\pi)^{-1/2}\int|F_2'(u-\xi)|\,|F_1(\xi)|\,d\xi\le(\alpha\mu)^{-1}\exp(y^2/2\alpha^2),$$

这是因为 $|F_2'|$ 可由 $-F_2'$ 的绝对值的积分控制,故得 (iii)。

对于 (iv),我们有

$$\Bigl|\int_{c-i\infty}^{c+i\infty}F(u)\,du\Bigr|=(2\pi)^{-1/2}\Bigl|\int_{c-i\infty}^{c+i\infty}\Bigl(\int F_2(iu-\xi)F_1(\xi)\,d\xi\Bigr)du\Bigr|.$$

利用 F₁(ξ)≥0 恒成立这一事实,左端的积分至多为

$$(2\pi)^{-1/2}\int_{c-i\infty}^{c+i\infty}\Bigl\{\int|F_2(iu-\xi)|\,|F_1(\xi)|\,d\xi\Bigr\}|du|,$$

而此处允许交换积分次序,故它等于

$$(2\pi)^{-1/2}\int|F_1(\xi)|\Bigl\{\int_{c-i\infty}^{c+i\infty}|F_2(iu-\xi)|\,|du|\Bigr\}d\xi.$$

现在在直线 (c−i∞,c+i∞) 上,

$$|F_2(iu-\xi)|=\alpha^{-1}\exp(Q),\qquad Q=\{c^2-(\tau+t)^2\}/2\alpha^2,\ u=c+it,$$

其中 τ 为 ξ 的虚部。于是沿该直线的内层积分恰为 exp(c²/2α²) 的一个不依赖于 ξ 的倍数,(iv) 随之成立。

再由 (2.5),

$$|F(u)|\le(2\pi)^{-1/2}\Bigl\{\int_{|\xi|\le4\mu}+\int_{|\xi|>4\mu}\Bigr\}|F_1(\xi)|\,|F_2(u-\xi)|\,d\xi\le(2\pi)^{-1/2}M_1\int|F_1(\xi)|\,d\xi=M_1,$$

其中 M₁ 是 |F₂(u−ξ)| 在 |ξ|≤4μ 上的最大值。由于 |u|>4μ,

$$M_1=\alpha^{-1}\exp\bigl[\{y^2-(|u|-4\mu)^2\}/2\alpha^2\bigr],$$

即得 (v)。引理 2 证毕。□

我们可以立即声明 μ、α、t₀ 满足

$$\mu=175,\qquad t_0>2500,\qquad \alpha^2t_0=400.\tag{2.7}$$

最后一个方程把 α 与 t₀ 联系起来;而 t₀ 与"π(x)>li x 对某个 x<X 成立"中的那个 X 密切相关,它要到最后一刻才确定。

[186]

## 3 函数 g(s)

定义

$$g(s)=\int_{a(s-1)}^{\infty}\frac{e^{-t}}{t}\,dt,\tag{3.1}$$

其中 s=σ+iτ,而 a=1/log 2。函数 g(s) 除实轴上 σ≤1 的部分外处处有定义;对 σ<1 的实轴部分,我们用

$$g(\sigma)=\tfrac12\{g_+(\sigma)+g_-(\sigma)\}$$

来定义 g(σ),其中 g₊(σ)、g₋(σ) 分别是 τ→±0 时 g(σ+iτ) 的极限;如此定义后,g(s) 除 s=1 外处处连续〔译注9〕。往后我们需要 g(s) 的下述不等式:

**引理 3.**

$$|g(s)|\le\{\pi|\tau|+10/(|s-1|)\}\exp(a-a\sigma).$$

证. 对除 s=1 左侧实轴之外的一切 s,把函数 exp{−a(z−1)}/(z−1) 沿围道 Γ=Γ₁+Γ₂+Γ₃+Γ₄ 积分,其中 Γ₁、Γ₂、Γ₃ 是联结 s 到 s+R、s+R 到 s₀+R、s₀+R 到 s₀ 的直线段,取 s₀=1+½|s−1| 并令 R→∞;Γ₄ 是以 1 为圆心、|s−1| 为半径、联结 s 与 s₀ 且不穿过 s=1 左侧实轴的圆弧。

由于该函数在 Γ 所围区域内正则,

$$\int_\Gamma \frac{\exp\{-a(z-1)\}}{z-1}\,dz=0,$$

又因沿 Γ₂ 的积分当 R→∞ 时趋于零,我们有

$$g(s)=g(s_0)-\int_{\Gamma_4}\frac{\exp\{-a(z-1)\}}{z-1}\,dz.$$

如果把"对数"理解为主值,便得到 (3.1) 之外 g(s) 的另一个定义:

$$g(s)=\log(s-1)+\bigl\{\text{整函数}\bigr\},$$

并且注意到 **g(s)+log(s−1) 在整个平面上正则**。现在,

$$0<g(s_0)=\int_{a(\sigma_0-1)}^{\infty}\frac{e^{-t}}{t}\,dt<\int_{a(\sigma_0-1)}^{\infty}\frac{e^{-t}}{a(\sigma_0-1)}\,dt=\frac{e^{-a(\sigma_0-1)}}{a(\sigma_0-1)},$$

而由于 $a|s-1|\ge a(\sigma_0-1)$,遂有

$$|g(s_0)|\le 10\exp\{a(1-\sigma)\}/|s-1|.$$

其次,对 Γ₄ 上的 z,写 z−1=|s−1|e^{iθ}。此时

$$|\exp\{-a(z-1)\}|\le e^{-a(\sigma-1)},\qquad |dz/(z-1)|=d\theta,$$

于是

$$\Bigl|\int_{\Gamma_4}\frac{e^{-a(z-1)}}{z-1}\,dz\Bigr|\le\pi\exp\{a(1-\sigma)\},$$

合并以上诸结果即得引理 3。

当 s 位于 s=1 左侧的实轴上时,我们求助于定义 g(σ)=½{g₊(σ)+g₋(σ)}。由于在极限意义下

$$|g_+(\sigma)|\le\{\pi+10/(|\sigma-1|)\}\exp(a-a\sigma),\qquad |g_-(\sigma)|\le\{\pi+10/(|\sigma-1|)\}\exp(a-a\sigma),$$

可知引理 3 的不等式对一切实数 s<1 也成立。□

[187]

## 4 函数 Π(x) 与 M(x)

用公式

$$\Pi(x)=\sum_{m\le[\log x/\log 2]}\frac{1}{m}\,\pi\bigl(x^{1/m}\bigr)$$

定义 Π(x)(黎曼的素数计数函数),并用一个显式积分定义 M(x)。〔M(x) 的原始定义此处 OCR 全部残损,无法逐字复原;就本文用法而言只须知道:M(x) 是由显式积分给出的、与 li x 相差极小的量,其梅林–斯蒂尔杰斯变换在引理 4 的证明中给出为 (s−1)^{−1}g(s)·(s−1)=g(s) 型的表达,且当 x 大时 M(x)≥li x。详见译注10。〕于是我们有

**引理 4.**

$$\int_0^\infty\{\Pi(e^t)-M(e^t)\}f(t-t_0)\,dt=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}(s-1)^{-1}\{\log\zeta(s)-g(s)\}(s-\tfrac12)\exp\{(s-\tfrac12)t_0\}\,ds,$$

其中 f 与 F 由 (2.1)、(2.3)、(2.4) 定义,t₀ 是满足 (2.7) 的一个数,将于稍后选定。

证. 先取 h(x)=Π(x)。此时 h(x) 有界变差,满足 §2 的条件 (ii) 与 (iii),而且

$$\int_0^\infty x^{-s-1}\Pi(x)\,dx=\frac{1}{s}\log\zeta(s),$$

故由引理 1,

$$\int_0^\infty \Pi(e^t)f(t-t_0)\,dt=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}(s-1)^{-1}\log\zeta(s)\,(s-\tfrac12)\exp\{(s-\tfrac12)t_0\}\,ds.$$

再取 h(x)=M(log x)。此时 h(x) 同样有界变差且满足 §2 的条件 (ii) 与 (iii),经变量代换可得

$$(s-1)^{-1}\int_{a(s-1)}^{\infty}\frac{e^{-t}}{t}\,dt.$$

由于 σ=2 时三角形围道 [a(s−1), R(s−1), a(s−1)+R] 内部无奇性,且沿 R(s−1) 到 a(s−1)+R 一边的积分当 R→∞ 时趋于零,我们有

$$\phi(s)=(s-1)^{-1}\int_{a(s-1)}^{\infty}\frac{e^{-t}}{t}\,dt=g(s).$$

因此

$$\int_0^\infty M(e^t)f(t-t_0)\,dt=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}(s-1)^{-1}g(s)\,(s-\tfrac12)\exp\{(s-\tfrac12)t_0\}\,ds,$$

两式相减,引理 4 得证。□

[188]

## 5 基本积分表示与引理 5

设 ρ 为 ζ(s) 的一个非平凡零点,并定义

$$I_1=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}\frac{1}{s-1}\log\frac{(s-1)\zeta(s)}{(s+1)(s+2)\zeta(s+2)}\,(s-\tfrac12)\exp\{(s-\tfrac12)t_0\}\,ds,\tag{5.1}$$

$$I_2=\frac{1}{2\pi i}\int_{-\Delta-i\infty}^{-\Delta+i\infty}\frac{1}{s-1}\Bigl[\log\frac{\zeta(s)}{(s+1)(s+2)\zeta(s+2)}-g(s)\Bigr](s-\tfrac12)\exp\{(s-\tfrac12)t_0\}\,ds,\tag{5.2}$$

其中在 I₁ 中对数于 s=2 处取实值并沿 σ=2 连续延拓;在 I₂ 中对数沿直线 σ=−Δ 自实轴负侧跨到正侧、此外处处连续。Δ 稍后取为 400。再定义

$$I_\rho=\frac{1}{2\pi i}\int_{2-i\infty}^{2+i\infty}\frac{1}{s-1}\,g(s-\rho)\exp\{(s-\tfrac12)t_0\}\,ds,\tag{5.3}$$

$$J=(2\pi\mu)^{1/2}\bigl(\log(|\zeta(0)|/2\zeta(2))-g(0)\bigr)g(-\tfrac12)\exp(-t_0/2);\tag{5.4}$$

〔(5.4) 的常数因子按上下文复原,见译注10。〕于是有

**引理 5.**

$$\int_0^\infty\{\Pi(e^t)-M(e^t)\}f(t-t_0)\,dt=I_1+I_2+J-\sum_\rho I_\rho,$$

其中 f 与 F 由 (2.1)、(2.3)、(2.4) 定义,g(s) 由 (3.1) 定义,t₀ 是满足 (2.7) 的数,要到最后一刻才确定。

证. 我们需要英厄姆书中的下列结果(文献 1,第 71 页以下):

(A) 存在一列数 T₂,T₃,…,T_r,…,使得

$$r<T_r<r+1\qquad(r=2,3,\dots)$$

且

$$|\zeta'(s)/\zeta(s)|<A\log^2T\qquad(-1\le\sigma\le2,\ t=T_r),$$

其中 A 为常数。

(B) 在从半平面 σ≤−1 中挖去以 s=−2,−4,−6,… 为圆心、半径 ½ 的一组圆的内部之后所得的区域,即由

$$\sigma\le-1,\qquad |s-n|\ge\tfrac12\quad(n=-2,-4,-6,\dots)$$

定义的区域中,

$$|\zeta'(s)/\zeta(s)|<A\log(|s|+1),$$

其中 A 为常数。

若现在 Δ≥½,则在线段 −Δ+½≤σ≤−1、t=T_r 上有

$$|\zeta'(s)/\zeta(s)|<A\log(|\sigma+iT_r|+1)<A'\log T_r.$$

该结果与 (A) 合并给出

$$|\zeta'(s)/\zeta(s)|<A_1\log^2T\qquad(-\Delta+\tfrac12\le\sigma\le2),$$

其中 A₁ 是适当的常数。从 σ+iT_r 积分到 2+iT_r,得

$$|\log\zeta(\sigma+iT_r)-\log\zeta(2+iT_r)|<(2-\sigma)A\log^2T\le(\Delta+\tfrac12)A_1\log^2T,$$

[189]

其中对 σ<2 我们把 log ζ(s) 定义为

$$\log\zeta(s)=\log|\zeta(s)|+\arg\zeta(s),\qquad -\pi<\arg\zeta(s)<\pi,\ \sigma\ge2,$$

沿直线段 (σ+iT_r, 2+iT_r) 的解析延拓——只要 ζ(s) 在该线段上无零点。于是

$$|\log\zeta(\sigma+iT_r)|<1+(\Delta+\tfrac12)A_1\log^2T<A_2\log^2T,$$

其中上述 A′、A₁、A₂ 均依赖于 Δ。

现在定义

$$\chi(s)=\Bigl(\frac{s}{2\pi}\Bigr)\Bigl[\log\frac{\zeta(s)}{(s+1)(s+2)\zeta(s+2)}-g(s)\Bigr](s-\tfrac12)\exp((s-\tfrac12)t_0).\tag{5.5}$$

〔前因子按 OCR 与上下文复原,见译注10。〕我们把 χ(s) 沿以

$$(2-iT_r,\ 2+iT_r,\ -\Delta+\tfrac12+iT_r,\ -\Delta+\tfrac12-iT_r)\qquad(r=2,3,4,\dots)$$

为顶点的矩形积分。记 I₃、I₄ 为两条竖边上的积分:

$$I_3=\int_{2-iT_r}^{-\Delta+\tfrac12-iT_r}\chi(s)\,ds,\qquad I_4=\int_{-\Delta+\tfrac12+iT_r}^{2+iT_r}\chi(s)\,ds,$$

则由上面的估计可知,I₃、I₄ 的模小于

$$T_r^{-1}(2\pi)^{-1}\bigl[2A_1\log^2T_r+A_2\log T_r+(\pi+10T_r^{-1})\exp\{a(\Delta+\tfrac12)\}\bigr]M_2(\Delta+\tfrac12)e^{t_0},$$

从而当 T_r→∞ 时 I₃、I₄→0。

接下来考察 χ(s) 的奇性。把它改写为

$$\chi(s)=(s-\tfrac12)e^{(s-\tfrac12)t_0}\Bigl(\frac{s}{2\pi}\Bigr)\{\chi_1(s)-\chi_2(s)\},$$

其中

$$\chi_1(s)=\log\Bigl[\frac{(s-1)\zeta(s)}{(s+1)(s+2)\zeta(s+2)}\Bigr],\qquad \chi_2(s)=g(s)+\log(s-1).$$

由 (3.2)(即"g(s)+log(s−1) 为整函数"这一事实)可知 χ₂(s) 处处有定义且无奇性;而 χ₁(s) 在每个 ρ 与每个 ρ−2 处有对数奇性。于是 χ(s) 在 ρ 与 ρ−2 处有对数奇性,并在 s=½ 处有一个极点。沿给定矩形积分时,前者贡献 −∑I_ρ;这一点可以通过把利特尔伍德(文献 8)的定理 1 中的 log ζ(s) 换成 χ₁(s)=χ(s)·log ζ(s) 型的修改而推得。

为求极点的贡献,需要 s=0 处的留数。在矩形 (2, 2+iT_r, −Δ+½+iT_r, −Δ+½) 的内部,当 Δ>½ 时,ζ(s) 的每一个零点都对应 ζ(s+2) 的一个零点。因此当沿矩形绕行一周时,

$$\frac{(s-1)\zeta(s)}{(s+1)(s+2)\zeta(s+2)}$$

的对数回到其原值。注意:由于因子 (s+1)(s+2),上述表达式沿整条实轴是实的、正的、正则的。我们取其在 s=2 处的对数为实值。又该表达式在 s=0 处为正,故可取其对数为 log(|ζ(0)|/2ζ(2))。χ₂(s) 对留数的贡献为

$$\chi_2(0)=\{\log 1+g_-(0)+g_+(0)\}=g(0).$$

于是

$$-I_3+\int_{-\Delta+\tfrac12-iT_r}^{-\Delta+\tfrac12+iT_r}\chi(s)\,ds=J-\sum_\rho I_\rho.$$

现在把 I₃ 加到两边并整理,得

$$\int_{-\Delta+\tfrac12-iT_r}^{2+iT_r}\chi(s)\,ds=J-\sum_\rho I_\rho+I_3,$$

再结合 I₃、I₄→0 与引理 4,引理 5 得证。□

[190]

## 6 引理 6

令 △=400=α²t₀ 且 t₀>2500。我们有

**引理 6.**

$$\sum' F(\gamma)e^{i\gamma t_0}>e^{-t_0}\Bigl(\frac{0.93}{12}\Bigr)-\frac{0.051}{|\gamma|+\rho t_0},$$

〔上式右端排版此处 OCR 严重残损;按上下文,引理给出的是和式 ∑′F(γ)e^{iγt₀} 的一个下界,其中含 e^{−t₀} 阶的主项与 0.051、0.93 两个数值系数控制的余项,详见译注11。〕其中 ∑′ 表示对所有满足 |γ|≤4μ+50 的零点求和,这里 10≤μ≤250;f 与 F 由 (2.1)、(2.3)、(2.4) 定义,Π(x) 与 M(x) 定义于引理 4 之前。后文将取 μ=175 并确定 t₀ 的值。

这正是我们较多偏离图灵手稿之处:我们的右端比图灵的稍大。不过,主要的偏离在第 9 节。

证. 回到引理 5,先证明

$$|I_1|,\ |I_2|,\ |J|<\sqrt{2\pi}\exp(-t_0).\tag{6.1}$$

我们注意到 I₁ 的被积函数在带域 1≤σ≤2 中正则,且当 T→±∞ 时在 σ 上一致趋于零。于是沿矩形 (2−iR, 2+iR, ½+iR, ½−iR) 积分并令 R→∞,得

$$I_1=\frac{1}{2\pi i}\int_{\tfrac12-i\infty}^{\tfrac12+i\infty}(s-1)^{-1}\log\Bigl[\frac{(s-1)\zeta(s)}{(s+1)(s+2)\zeta(s+2)}\Bigr](s-\tfrac12)e^{(s-\tfrac12)t_0}ds.$$

现在对 σ≥4:

$$|(s-1)^{-1}\log[(s+1)(s+2)\zeta(s+2)]|\\ \le \log\{(|s|+1)(|s|+2)|\zeta(\sigma+2)|\},$$

以及

$$\log|s+a|\le\log(|s|+a-1)\le (4a-3)^{-1}|s|\quad(a=1,2),$$

并且 |log ζ(s+2)|≤log ζ(σ+2),因为 log ζ(s) 的狄利克雷级数系数均非负。于是

$$\int_{\tfrac12-i\infty}^{\tfrac12+i\infty}\Bigl|(s-1)^{-1}\log[(s+1)(s+2)\zeta(s+2)]\Bigr|\,|ds|<\infty.\tag{6.2}$$

由引理 2(iv),

$$\Bigl|\int_{\tfrac12-i\infty}^{\tfrac12+i\infty}(s-\tfrac12)\exp((s-\tfrac12)t_0)ds\Bigr|\le\sqrt{2\pi}\,\exp(t_0/12800).$$

〔指数中常数按上下文复原,见译注11。〕结合 (6.2),

$$|I_1|\le 22(2\pi)^{-1}\exp(-t_0/2)\cdot(2\pi)^{1/2}\exp(t_0/12800)<(2\pi)^{1/2}\exp(-t_0),$$

这是因为 t₀>2500。

现在利用 ζ(s) 与 ζ(1−s) 的函数关系,它给出

$$\log\frac{\zeta(s)}{(s+1)(s+2)\zeta(s+2)}=\log\frac{\zeta(1-s)}{(\ldots)\zeta(\ldots)}+\text{(初等因子)},$$

故当 σ<−3 时,

$$\Bigl|\log\frac{\zeta(s)}{(s+1)(s+2)\zeta(s+2)}\Bigr|\le\pi+2\log 2\pi+\log|s/(s+2)|\\ +|\log\zeta(1-s)|+|\log\zeta(-1-s)|\\ <\pi+2\log 2\pi+\log 3+2\log\zeta(2)<12,$$

这是因为当 σ<−3 时 $1<|s/(s+2)|<3$,且如上有

$$|\log\zeta(\pm1-s)|\le\log\zeta(\pm1-\sigma)\le\log\zeta(2).$$

沿积分直线 s=−△+½+iτ 用引理 3,

$$|g(s)|\le(\pi+10/|\!-\!\triangle|)\exp\{a(\triangle+\sigma)\}<e^{40},$$

这里 △=400、a≈1.44 取整估计;于是

$$\bigl|\log\frac{\zeta(s)}{(s+1)(s+2)\zeta(s+2)}-g(s)\bigr|\le12+e^{40}<4e^{40}.\tag{6.3}$$

再由引理 2(iv),

$$\Bigl|\int_{-\triangle-i\infty}^{-\triangle+i\infty}(s-\tfrac12)\exp((s-\tfrac12)t_0)ds\Bigr|\le\sqrt{2\pi}\,\exp(\triangle^2/2\alpha^2).$$

由 (6.3),

$$|I_2|<(2\pi)^{-1}(\triangle-\tfrac12)^{-1}\cdot 4e^{40}\exp(-\triangle t_0)\cdot(2\pi)^{1/2}\exp(\triangle t_0/2)\\ =6(\triangle-\tfrac12)^{-1}\exp(40-200t_0)\\ <\sqrt{2\pi}\exp(-t_0),$$

因为 △=400=α²t₀ 且 t₀>2500。

[191]

由 (5.4),

$$|J|=(2\pi\mu)^{1/2}\Bigl|\bigl(\log(|\zeta(0)|/2\zeta(2))-g(0)\bigr)g(-\tfrac12)\exp(-t_0/2)\Bigr|.$$

现在

$$|\log(|\zeta(0)|/2\zeta(2))|=|\log(\pi^2/12)|<3,$$

而引理 3 给出

$$|g(0)|\le\tfrac12(\pi+10)\exp(a)<15.$$

〔此处系数按上下文复原。〕于是由引理 2(ii),

$$|J|<(2\pi\mu)^{1/2}(3+15)\sqrt{2\pi}\,(2\mu)^{-1}\exp\{(a^2)-t_0\}\\ <\pi\exp\{t_0(\tfrac{1}{400}-1)\}<\sqrt{2\pi}\exp(-t_0).$$

这就完成了 (6.1) 的证明。

引理 5 右端唯一尚未估计的项是 (5.3) 定义的 ∑I_ρ。对每个 |γ|≤4μ+50 的零点,我们如下逐个估计 I_ρ。写

$$K_\rho=\int F(s-\rho)\exp\{(s-\tfrac12)t_0\}\,ds,\tag{6.4}$$

$$L_\rho=\int\rho^{-1}\{(s-\tfrac12)F(s-\rho)-F(-\gamma)\}\exp\{(s-\tfrac12)t_0\}\,ds,\tag{6.5}$$

$$M_\rho=\int\rho^{-1}F(-\gamma)\exp(s-\tfrac12)t_0\,ds,\tag{6.6}$$

$$N_\rho=\int\rho^{-1}F(-\gamma)\exp(s-\tfrac12)t_0\,ds.\tag{6.7}$$

〔以上四式中的积分路径各不相同——分别过点 ρ 附近的水平/斜线段等;OCR 残损,路径细节按上下文复原,见译注11。〕由于 ρ=½+iγ 且 |γ|≤4μ+50≤10⁵⁰,对该范围内的每个 ρ 有恒等式

$$(2\pi)^{-1/2}I_\rho=K_\rho+L_\rho+M_\rho-N_\rho.\tag{6.8}$$

我们将证明

$$|K_\rho|\le0.93\,\gamma^{-2}/(\mu t_0),\qquad |L_\rho|<0.051\,t_0^{-1}/(\mu|\gamma|),\tag{6.9}$$

$$M_\rho=F(\gamma)\exp(i\gamma t_0)/t_0(\tfrac12+i\gamma),\qquad |N_\rho|<N^{-1}\exp(-\tfrac12 t_0),$$

其中 N 是满足 |γ|≤4μ+50 的共轭零点对的数目,即 25≤N≤690。

由 (6.4),

$$|K_\rho|=\Bigl|\int (s-\rho)^{\cdot}(s-\tfrac12)\exp\{(s-\tfrac12)t_0\}\,ds\Bigr|.$$

此处 s=ρ−it,其中 0≤t≤2,且有

$$|\rho/s|\le1/\gamma^2;\qquad |\exp\{(s-\tfrac12)t_0\}|=\exp(-ct_0);$$

$$|(s-\tfrac12)^{\cdot}ds|\le\sqrt{2\pi}\,\mu^{-1}\exp(c^2/2\alpha^2),\qquad\text{由引理 2(ii)}.$$

[192]

因此

$$|K_\rho|\le\sqrt{2\pi}\,\mu^{-1}\gamma^{-2}\int_0^2 \exp\{(c^2/2\alpha^2)-ct_0\}\,dc.$$

在 0≤c≤2 中,$(c^2/2\alpha^2)-ct_0\le -ct_0(1-c/800)$,而

$$c\exp\{-ct_0(1-c/800)\}$$

在 c=800^{−1}t₀^{−1}(1−c/800)^{−1}·… 处取最大值,故有

$$|K_\rho|\le1.005/(2\pi)e^{-1}\gamma^{-2}/(\mu t_0)\le0.93\,\gamma^{-2}/(\mu t_0).$$

由 (6.5),

$$L_\rho=\int\rho^{-1}\{(s-\tfrac12)F(s-\rho)-F(-\gamma)\}\exp\{(s-\tfrac12)t_0\}\,ds.$$

分部积分,得

$$|L_\rho|\le T_1+T_2,\ \text{记之},$$

其中

$$T_1=\Bigl|\int \frac{d}{ds}\{\rho^{-1}((s-\tfrac12)F(s-\rho)-F(-\gamma))\}\Bigr|\\ <\exp(-\tfrac52 t_0)\bigl[\sqrt{2\pi}\,\mu^{-1}\{\exp(2/\alpha^2)+1\}\bigr]/|\gamma|t_0\\ <0.00075\,t_0^{-1}/\mu|\gamma|,$$

以及

$$T_2=\Bigl|\int_{\rho-2}^{\rho}\exp\{(s-\tfrac12)t_0\}F'(s-\rho)\,ds\Bigr|.$$

令 α=p−s 作代换,由引理 2(i) 可见

$$T_2\le(|\gamma|\,t_0\alpha\mu)^{-1}\int_0^2\exp\{(c^2/2\alpha^2)-ct_0\}\,da,$$

其中内层积分满足

$$\int_0^2\exp\{-(c-I)/2\alpha^2\}\,dc<\exp(c/\alpha^2)\theta,$$

于是(因 α²=400/t₀)得 T₂<0.05025·t₀^{−1}/μ|γ|。故

$$|L_\rho|\le T_1+T_2<0.051\,t_0^{-1}/\mu|\gamma|.$$

对 (6.6) 积分,有

$$M_\rho=F(-\gamma)\exp(i\gamma t_0)/\rho t_0=F(\gamma)\exp(iy t_0)/t_0(\tfrac12+i\gamma).$$

类似地,对 (6.7) 积分,有

$$|N_\rho|=\bigl|\rho^{-1}F(\gamma)\exp\{(\tfrac12-\gamma)t_0\}/\rho t_0\bigr|<|F(\gamma)\exp(-\tfrac12 t_0)/t_0|\cdot N^{-1}<N^{-1}\exp(-t_0),$$

这里用到引理 2(ii)。这就完成了 (6.9) 的证明。

为完成引理 6 的证明,还须证明:当 ∑₂ 表示对 |γ|>4μ+50 的零点求和时,该和收敛到很小的量。事实上我们证明

$$\sum\nolimits_2|I_\rho|<\sqrt{2\pi}\exp(-t_0).\tag{6.10}$$

[193]

若 ρ=β+iγ 且 |γ|>4μ+50,则 0<β<1,且

$$I_\rho=(2\pi)^{-1}\int (s-1)^{-1}g(s-\rho)\exp\{(s-\tfrac12)t_0\}\,ds,$$

其中 s=ρ−it;由引理 2(v),

$$|(2\pi)^{-1}I_\rho|\le \alpha^{-1}|\gamma|^{-1}\exp[\{(c+\alpha)^2-(|\gamma|-4\mu)^2\}/2\alpha^2].$$

方括号内的项小于

$$\{(c+\alpha)^2-(|\gamma|-4\mu)^2\}/2\alpha^2,$$

而另一指数项小于 (½−c)t₀,于是

$$|(2\pi)^{-1}I_\rho|<3\alpha^{-1}|\gamma|^{-1}\exp[t_0(\tfrac12-c)-(|\gamma|-4\mu)^2/800].$$

现在

$$\tfrac12-c=\frac{\beta-\tfrac12}{?},\qquad\text{即}\quad \exp\{t_0(\tfrac12-c)\}\le e^{-t_0/2},$$

〔此行 OCR 残损;按上下文,β−½ 的因子被吸收进指数估计。〕故

$$|(2\pi)^{-1}I_\rho|<3\alpha^{-1}|\gamma|^{-1}\exp[-t_0\{1+(|\gamma|-4\mu)\}].$$

而当 |γ|>4μ+50 时,

$$\bigl||\gamma|-4\mu\bigr|>|\gamma|/24,\tag{6.11}$$

于是

$$(2\pi)^{-1}|I_\rho|<\sqrt{2\pi}\,|\gamma|^{-2}\exp(-t_0)\cdot\varepsilon.$$

花括号中的项小于 ε,且 α⁻¹<exp(εt₀),从而给出

$$|I_\rho|<\sqrt{2\pi}\,\gamma^{-2}\exp(-\tfrac12 t_0).$$

因此

$$\sum\nolimits_2|I_\rho|<\sqrt{2\pi}\exp(-\tfrac12 t_0)\sum 1/\gamma^2<(2\pi)\exp(-t_0),$$

因为由文献 (4)(引理 1(ii))有 ∑(1/γ²)≤0.0466。

[194]

由 (6.8) 与引理 5,

$$\int_0^\infty\{\Pi(e^t)-M(e^t)\}f(t-t_0)\,dt\\ =I_1+I_2+J-\sqrt{2\pi}\sum\nolimits_1(K_\rho+L_\rho-N_\rho)-\sum\nolimits_2 I_\rho,$$

从而

$$(2\pi)^{-1/2}\int_0^\infty\{\Pi(e^t)-M(e^t)\}f(t-t_0)\,dt\\ \le(2\pi)^{-1/2}(|I_1|+|I_2|+|J|+\sum\nolimits_2|I_\rho|)+\sum\nolimits_1(|K_\rho|+|L_\rho|+|N_\rho|).$$

把这里与 (6.1)、(6.9)、(6.10) 的结果合并,即得引理 6 的结论。□

[195]

## 7 引理 7

**引理 7.** 若

$$\int_0^\infty\{\Pi(e^t)-M(e^t)\}\exp\{-\alpha^2(t-t_0)^2\}\Bigl(\frac{\sin\mu(t-t_0)}{\mu(t-t_0)}\Bigr)^4 dt>\frac{1.0001\,\pi}{\mu t_0},\tag{7.1}$$

〔阈值数字 OCR 残损;按定理 1 的推导该下界约为 1.0025π/(μt₀),此处系数按上下文复原。〕则存在满足 0.950t₀≤t₁≤1.052t₀ 的数 t₁,使

$$\Pi(e^{t_1})-\operatorname{li}(e^{t_1})>1.002\,t_1^{-1}\exp(t_1),$$

其中 Π(x) 与 M(x) 定义于引理 4 之前,f 由 (2.1)、(2.3)、(2.4) 定义,μ 与 t₀ 满足 (2.7)。

证. 由于

$$\int_{-\infty}^{\infty}\Bigl(\frac{\sin\mu t}{\mu t}\Bigr)^4dt=\frac{2}{3\mu},$$

若 (7.1) 成立,则

$$\int_0^\infty\{\Pi(e^t)-M(e^t)\}\\ \times\exp\{-\alpha^2(t-t_0)^2\}\Bigl(\frac{\sin\mu(t-t_0)}{\mu(t-t_0)}\Bigr)^4 dt>0.0001\,\pi/\mu t_0.$$

这意味着对某个 t(记作 t₁),有

$$\{\Pi(e^{t_1})-M(e^{t_1})\}\cdot(\text{权函数的规范化})\\ >\exp\{t_1+200t_0^{-1}(t_1-t_0)^2-0.01t_0\},$$

因为当 t₀>2500 时 1.0024·t₁⁻¹>exp(−0.01t₀)。若 t₁<0.950t₀,则

$$200t_0^{-1}(t_1-t_0)^2-0.01t_0>0.5t_1,$$

这将推出 Π(e^{t₁})>e^{t₁},与平凡事实 Π(x)≤x 矛盾。类似地,t₁>1.052t₀ 也导致矛盾。于是存在满足 0.950t₀≤t₁≤1.052t₀ 的某个 t₁,使得

$$\Pi(e^{t_1})-M(e^{t_1})>1.0024\,t_1^{-1}\exp\{t_1+200t_1^{-1}(t_1-t_0)^2\}.$$

然而 M(t)≥li(e^t),且在上述 t₁ 的范围内,

$$1.0024\,t_1^{-2}\exp\{200t_1^{-1}(t_1-t_0)^2\}>1.002\,t_1^{-1},$$

故引理 7 得证。□

[196]

## 8 引理 8 与定理 1

**引理 8.** 若 {Π(x)−li x}·x^{−1/2}/log x ≥ 1.002 且 x>exp(2000),则

$$\pi(x)>\operatorname{li}x\quad\text{或}\quad \pi(\sqrt{x})>\operatorname{li}\sqrt{x}.$$

证. 记

$$E=\Pi(x)-\pi(x)-\tfrac12\pi(\sqrt{x})=\sum_{r=3}\frac{1}{r}\,\pi(x^{1/r}).$$

若 r>log_e x,则 x^{1/r}<e,故 π(x^{1/r})<2,且

$$E<\sum_{r=3}^{[\log_e x]}\frac{\pi(x^{1/r})}{r}+2\sum_{r=[\log_e x]+1}^{\infty}\frac{1}{r}.$$

[197]

然而对所有 x 有 π(x)<2+x^{1/2},于是

$$E<\sum_{r=3}^{n}\Bigl(2+\frac{1}{m}\Bigr)\frac{1}{r},$$

其中 m=[log_e x],n=[log₂ x]。由于对 r≥3 有 x^{1/r}<√x 且 x>exp(2000),我们有

$$\sum_{r=3}\frac{1}{r}<\log(m)+2\log(n)\\ <x^{-1/2}\log\log+2\log\log.\tag{8.1}$$

〔此行 OCR 残损;按上下文为 E 的上界中两个对数型余项的估计。〕现在

$$\{\Pi(x)-\operatorname{li}x\}x^{-1/2}/\log x=\{E+\pi(x)+\tfrac12\pi(\sqrt{x})-\operatorname{li}x\}x^{-1/2}/\log x,$$

若假定 π(x)≤li x 且 π(√x)≤li √x,则

$$\{\Pi(x)-\operatorname{li}x\}x^{-1/2}/\log x\le\{E+\tfrac12\operatorname{li}(\sqrt{x})\}x^{-1/2}/\log x\\ \le x^{-1/2}\log x\log\log x+2x^{-1/2}\log x\log\log x+\tfrac12(\operatorname{li}\sqrt{x})x^{-1/2}/\log x,$$

这里用到 (8.1)。对函数

$$\{x/\log x-1.5\}-\operatorname{li}x$$

求导可知它在 x>1000 时为正(且递增)。于是

$$\{\Pi(x)-\operatorname{li}x\}x^{-1/2}/\log x\le(\sqrt{x}+2x^{-1/2})^{-1}\log x\log\log x+\log x/(\tfrac12\log x-3)\\ <1.002,\qquad\text{当 }x>\exp(2000).$$

〔中间步骤按上下文复原。〕因此,若 {Π(x)−li x}x^{−1/2}/log x>1.002 且 x>exp(2000),则前提必有假者:即 π(x)>li x 或 π(√x)>li √x。引理 8 得证。□

合并引理 6、7、8 即得

**定理 1.** 若存在数 t₀>2500 使得

$$\sum' F(\gamma)e^{i\gamma t_0}>0.521\sqrt{2\pi}/\mu,\tag{8.2}$$

则存在数 t 满足 0.950t₀≤t≤1.052t₀,使得 π(e^t)>li e^t 或 π(e^{t/2})>li e^{t/2};其中 F 满足 (2.1) 与 (2.5),μ 与 t₀ 满足 (2.7),∑′ 表示对所有满足 |γ|≤4μ+50 的零点求和。

证. 在引理 6 中应用条件 (8.2),得

$$\int_0^\infty\{\Pi(e^t)-M(e^t)\}f(t-t_0)\,dt>1.042\,\pi/\mu t_0-\sqrt{2\pi}\exp(-t_0)\\ -0.051-0.93.$$

〔后两项实为分别带 1/(μt₀) 型因子的余项;排版此处 OCR 残损,按下一节的数值合并复原。〕现在,对给定范围内的 t₀,

$$\sqrt{2\pi}\exp(-t_0)<0.0001\,\pi/\mu t_0,$$

而由直接枚举

$$\sum 1/\gamma^2<0.0466,\qquad \sum 1/|\gamma|<5,$$

于是

$$\{\Pi(e^t)-M(e^t)\}\text{ 的加权积分}> \pi\mu^{-1}t_0^{-1}(1.042-0.0001-0.0042-0.0346)\\ >1.0025\,\pi/\mu t_0,$$

定理便由引理 7 与引理 8 得出。□

[198]

## 9 t₀ 的确定(数值部分)

我们现在的任务是寻找满足 (8.2) 的适当的 t₀。由于 F(γ)=F(−γ),而 ζ(s) 在 s=½ 上的零点成对共轭出现,(8.2) 左端的和可以表示为

$$\sum' F(\gamma)e^{i\gamma t_0}=2\sum_{|\rho|}'\frac{F(\gamma)}{|\rho|}\sin(\gamma t_0+\theta+\pi),$$

其中 ∑′ 表示对 0<γ≤4μ+50 求和,且 tan θ=γ⁻¹〔OCR 残损,θ 的定义按 1/ρ 的辐角复原,见译注12〕。若把零点排序为 γ₁<γ₂<…,该表达式可写作

$$2\sum_n \frac{F(\gamma_n)}{|\rho_n|}\sin(\gamma_nt_0+\theta_n+\pi),\tag{9.1}$$

其中 θ_n=arctan(γ_n²)·? 而 0<γ_n≤4μ+50。

为求值 (9.1),需要对 F(γ_n) 有所了解。由 (2.5) 与 (2.6),

$$F(\gamma_n)=(2\mu)^{-1}\alpha^{-1}\Bigl(\int\Phi_1(u)\,du+\int\Phi_2(u)\,du+\int\Phi_3(u)\,du\Bigr),$$

其中被积函数形如 (2−|u|/2μ)²exp{−(γ_n−u)²/2α²},即

$$F(\gamma_n)=\mu^{-1}\alpha^{-1}\int(2-u/2\mu)^4\Phi(u)\,du,$$

而

$$\Phi(u)=\exp\{-(\gamma_n-u)^2/2\alpha^2\}+\exp\{-(\gamma_n+u)^2/2\alpha^2\}.$$

经适当的变量代换,这给出

$$F(\gamma_n)=X_n+Y_n+Z_n+T_n,$$

其中

$$X_n\sim\int e^{-x^2}(a-qx)\,da,\qquad Y_n\sim\int e^{-x^2}(b-qc)^2\,da,\qquad Z_n\sim\int e^{-x^2}(c-qx)^3\,dx,\qquad T_n\sim\int e^{-x^2}(d-qx)^2\,dx,$$

〔各项的积分限与幂次此处 OCR 残损;结构为形如 ∫e^{−½x²}(a−qx)^r dx 的线性组合,见译注12。〕这里 a、b、c、d、q 分别表示 2−γ_n/2μ、2+γ_n/2μ、1−γ_n/2μ、1+γ_n/2μ、α/2μ 诸量,而 a′、b′、c′、d′、e′ 分别表示 α⁻¹(4μ−γ_n)、α⁻¹(4μ+γ_n)、α⁻¹(2μ−γ_n)、α⁻¹(2μ+γ_n)、α⁻¹γ_n。

当 t₀>2500 时,α⁻¹>2.5,e′>2.5γ_n>30。借助形如

$$\int_A^\infty e^{-hx^2}\,dx$$

的积分表,我们发现 |Y_n|、|T_n|<10^{−10}μ^{−1}。在此我们说明:把 F(γ_n) 表为 X_n、Y_n、Z_n、T_n,是为了便于数值计算。这些项涉及 x^r·e^{−tx²}(r=0,1,2,3) 的线性组合;r=1,3 时 x·e^{−tx²} 可直接积出,r=0,2 时只要积分上限足够大(例如取到 7),便可得到渐近展开。我们要特别提到一个使用极多、非常有用的展开式:

$$\int_A^\infty e^{-x^2}\,dx=\frac{e^{-A^2}}{A}\Bigl(1-\frac{1}{2A^2}+\frac{1\cdot3}{(2A^2)^2}-\cdots+(-1)^n\frac{(2n-1)!!}{(2A^2)^n}\cdots\Bigr).$$

〔展开式细节按标准渐近展开复原,原式 OCR 残损。〕在积分上限 a′ 与 c′ 接近零的情形,我们发现 a、c、q 碰巧都非常小。于是若取 μ=175,便发现 X_n 与 Z_n 分别与

$$X_n'= (8\mu)^{-1}\int_{-2.5\gamma_n}^{2+5(4\mu-\gamma_n)}e^{-\tfrac12x^2}(a-qc)^3\,dc$$

以及

$$Z_n'=(2\mu)^{-1}\int_{-2.5\gamma_n}^{2+5(2\mu-\gamma_n)}e^{-\tfrac12x^2}(c-qa)\,da$$

相差可忽略地小。更确切地说,可以证明

$$|X_n-X_n'|<10^{-8}\mu^{-1},\qquad |Z_n-Z_n'|<10^{-8}\mu^{-1}.$$

[199]

在对 (9.1) 的各项作进一步求值之前,先证明下面的引理。

**引理 9.** 给定实数 a₁,…,a_k、一个正实数 T 以及正整数 m₁,…,m_k,则可以找到 T 的整数倍 t,满足 T≤t≤T·m₁⋯m_k,使得对每个 n(1≤n≤k),ta_n 与某整数之差不超过 1/m_n。

〔"ta_n 与整数之差"的确切归一此处 OCR 残损;按狄利克雷抽屉原理的标准形式复原。〕

证. 证明基本上与狄利克雷定理相同(英厄姆,文献 1,定理 J,第 94 页),只是把"单位立方体"分割成 ∏m_n 个"长方体",第 n 条棱的长度为 1/m_n。□

由该引理,存在 t 属于范围

$$2500\le t\le 2500\prod\bigl(1+2R\gamma_n/\nu\bigr),$$

其中 R=60、N=100、ν=236.524…,使得

$$||nt||\le 1/m_n,\qquad n=1,2,\dots,241,$$

其中 m_n=[2Rν/γ_n]+1,而 ||α|| 表示 α 到最近整数的非负距离。现在取

$$t_0=2\pi t-\pi/2N.$$

则

$$|n(t_0+\pi/2N)/2\pi|\le 1/m_n,$$

且

$$\bigl|\gamma_n\{t_0+(\theta_n/\gamma_n)+(\pi/2n)\}/2\pi\bigr|\le\bigl|\gamma_n(t+\pi/2N)/2\pi\bigr|+|X_n|,$$

其中

$$X_n=\theta_n/\gamma_n-\pi/2N\cdot?$$

〔X_n 的定义式 OCR 残损,按上下文为 θ_n/γ_n 与 π/2N 之差的某个组合。〕由于

$$(\pi/2)(\theta)<\theta<\ldots,$$

对 1≤n≤241 我们有

$$-\tfrac12+1/m_n<X_n<\tfrac12-1/m_n,\qquad n=1,\dots,241,$$

从而

$$|X_n|<\tfrac12-1/m_n.$$

R 正是特意选来达成这一结果的;它保证 (9.1) 的前 241 项为正。这是因为对所选的 t₀,现在有

$$|\gamma_nt_0+\theta_n+\pi)/2\pi\bigr|<1/m_n+(\tfrac12-1/m_n)=\tfrac12,$$

因而 γ_nt₀+θ_n+π 与 2π 的整数倍相差不超过 π/2·?——即对所选的 t₀,

$$\sin(\gamma_nt_0+\theta_n+\pi)>0,\qquad n=1,2,\dots,241.$$

[200]

此外,

$$\sin(\gamma_nt_0+\theta_n+\pi)\begin{cases}\ge\sin\{(\pi\gamma_n/N)-(2\pi/m_n)-\theta_n\},&X>0,\\ \ge\sin\{(\pi\gamma_n/N)+(2\pi/m_n)-\theta_n\},&X<0,\end{cases}$$

而 X=0 的情形已由 X 的构造方式排除。取 μ=175 时,(9.1) 中共使用了 ζ 函数的 452 个零点,于是该和大于

$$2\sum_{n=1}^{241}\frac{(X_n+Z_n)}{|\rho_n|}\cdot\frac{\text{符号}}{}\sin(\pi\gamma_n/N+(2\pi/m_n)-\theta_n)+2\sum_{n=242}^{452}\frac{F(\gamma_n)}{|\rho_n|}\sin(\gamma_nt_0+\theta_n+\pi)+\text{小项},$$

其中第一项里:当 X<0 时取加号、当 X>0 时取减号。小项的模小于 10^{−6}μ^{−1},故 (9.1) 大于

$$2\sum_{n=1}^{241}\frac{(X_n+Z_n)}{|\rho_n|}\sin(\pi\gamma_n/N+(2\pi/m_n)-\theta_n)\\ -2\sum_{n=242}^{452}\Bigl|\frac{F(\gamma_n)}{|\rho_n|}\Bigr|-10^{-6}\mu^{-1}.$$

对这些和作数值求值(读者或许有兴趣知道:上述计算在一台 Elliott 803 计算机上耗时约 20 分钟,当然还应加上编程与纸带准备所需的一两个小时),并对舍入误差作必要的修正之后,我们发现 (9.1) 大于 (8.2) 所要求的界 0.521√(2π)/μ。〔该数值不等式的原行 OCR 全毁;由定理 2 的推导可知它必须超过 (8.2) 的右端,见译注12。〕

于是我们证明了存在 t₀ 满足

$$2\pi\cdot 2500\le t_0+\pi/2N\le 2\pi\cdot 2500\prod_{n=1}^{241}\bigl(1+2R\gamma_n/n\bigr),$$

使得 (8.2) 成立。由直接计算,

$$\sum_{n=1}^{241}\log\{1+(2R\gamma_n/n)\}<1207,$$

即

$$2\pi\cdot2500\le t_0+\pi/2N\le 2\pi\cdot2500\cdot\exp(1207),$$

亦即

$$2500<t_0<10^{530}.$$

[201]

由定理 1 可知,存在数 t₁(t₁≤1.052t₀)使得 π(e^{t₁})>li e^{t₁} 或 π(e^{t₁/2})>li e^{t₁/2}。于是我们得到

**定理 2.** 存在数 x 满足 2≤x≤10^{10^{530}},使 π(x)>li x。

**附记(1967 年 6 月 26 日增).** 审稿人提请我们注意 R. Sherman Lehman 的一篇论文(Acta Arithmetica 11 (1966) 397–410),文中证明:在范围

$$1.53\times10^{1165}<x<1.65\times10^{1165}$$

之内,有超过 10⁵⁰⁰ 个相继整数 x 使 π(x)>li x。

[202]

## 参考文献

1. A. E. Ingham, *The distribution of prime numbers*(Cambridge Mathematical Tracts,No. 30,1932).
2. J. E. Littlewood,'Sur la distribution des nombres premiers',*Comptes Rendus* 158 (1914) 1869–72.
3. S. Skewes,'On the difference π(x)−li(x)(I)',*J. London Math. Soc.* 8 (1933) 277–83.
4. S. Skewes,'On the difference π(x)−li(x)(II)',*Proc. London Math. Soc.*(3) 5 (1955) 48–70.
5. E. C. Titchmarsh,'The zeros of the zeta-function',*Proc. Royal Soc.*(A) 157 (1936) 261–63.
6. A. E. Ingham,'A note on the distribution of primes',*Acta Arithmetica* 1 (1936) 201–11.
7. E. C. Titchmarsh,*Introduction to the theory of Fourier integrals*(Oxford,1937).
8. J. E. Littlewood,'On the zeros of the Riemann zeta-function',*Proc. Cambridge Phil. Soc.* 22 (1924) 295–318.
9. C. B. Haselgrove and J. C. P. Miller,*Tables of the Riemann zeta function*,Roy. Soc. Math. Tables, Vol. 6 (1960).

(威尔士大学科学技术学院,加的夫;拉格比工程技术学院,拉格比)

[205]

## 译注

### 一、出处与背景

**〔译注1〕出处。** 本文原刊于 *Proc. London Math. Soc.*(3)18(1968)691–713;1992 年经 J. L. Britton 编《图灵文集·纯数学》卷(North-Holland,"Collected Works of A. M. Turing"第 2 卷)重印于其"相关论文"部分(pp. 183–205),紧随图灵未完成手稿《差 ψ(x)−x》与斯克斯–图灵合著《论利特尔伍德的一个定理》之后——本文正是对这两份遗稿中思路的继承与完成。作者单位分别为威尔士大学科学技术学院(科恩)与拉格比工程技术学院(梅休)。

**〔译注2〕"直到 10³ 为负"。** 原文上标在扫描件中残损("10?"仅存底数)。π(x)−li x 在 x 极小处为正(li x 在 x<1.45… 时为负),随后转负;此处具体幂次按上下文复原为 10³,不影响论证。又,正文所引"π(x)−li x ∼ −c/log x"是图灵手稿中的经验性猜测,并非严格结论。

**〔译注3〕斯克斯(S. Skewes)。** 南非数学家,以关于 π(x)>li x 首个出现位置的两大界著称:(I)1933 年在黎曼假设下证明该位置 x<e^e^e^79≈10^{10^{10^34}};(II)1955 年无条件地证明 x<10^{10^{10^963}} 一类(常引作 e^e^e^e^7.705)。原文两处指数的末位数字均因 OCR 丢失,译文按文献记载复原;"发表于图灵去世之后"指 (II)(图灵卒于 1954 年)。

**〔译注4〕|γ|<1468。** γ 记 ζ(s) 零点的虚部。蒂奇马什 1936 年证明临界线上 |γ|≤1464(原文作 1468)内无零点偏离直线,即黎曼假设在该高度以下成立;这是后文数值方法可用的前提。

**〔译注5〕Π(x)。** 黎曼引入的素数计数函数 Π(x)=∑_{m≥1}(1/m)π(x^{1/m}),与 π(x) 的关系为 π(x)=Π(x)−½Π(x^{1/2})−⅓Π(x^{1/3})−…(默比乌斯反演);本文引理 8 正是用这一关系从 Π 的下界推出 π 的下界。

### 二、OCR 残损与公式复原

**〔译注6〕引言中图灵方法概要的公式。** 引言系图灵手稿原文的转录,其中若干公式(如 I 与傅里叶变换乘积的关系、"只须有……即可推断 G(t)>1"处的显式条件)在扫描件中严重破碎,译文按 §2–§7 的正式表述回填,行文顺序亦按上下文理顺(原件此段有明显的排版错位)。

**〔译注7〕§2 的函数类与条件。** f 的增长条件、φ(s) 的定义及 h(x) 的条件 (i)–(iii) 文字均有缺损。按引理 1 的证明所需复原:f 在竖直带域内正则并沿两个水平方向指数衰减;φ(s)=∫₀^∞ x^{−s}dh(x);条件保证佩龙积分可交换次序。个别记号(如带域半宽 λ 与参数 μ 的分工)可能与原书略有出入。

**〔译注8〕K(x) 公式。** K(x) 即 sinc⁴ 的傅里叶变换(三次 B 样条)。OCR 显示分段二次式且常数丢失,译文按标准公式

$$K(x)=\frac23-(1-|x|)^2+\frac12(1-|x|^3)\ (0\le|x|\le1),\quad \frac16(2-|x|)^3\ (1\le|x|\le2)$$

复原;K(0)=2/3 与"最大值在 x=0 处取得"相符。

**〔译注9〕g(s) 与引理 3。** g(s) 定义 (3.1) 中是否含 1/(a(s−1)) 前因子,OCR 无法判定;按"g(s)+log(s−1) 在全平面正则"(§5 用于 χ₂ 无奇性)及 g(s₀) 的估计式,取 g(s)=∫_{a(s−1)}^∞ e^{−t}dt/t(E₁ 函数)。引理 3 右端指数 exp(a−aσ) 的准确形式同样按上下文复原。g(σ) 的实轴定义式中另有一小句完全不可读,已略去。

**〔译注10〕M(x)、(5.4) 与 χ(s)。** M(x) 的显式定义、(5.4) 的常数因子、χ(s)(5.5) 的前因子三处在扫描件中无法逐字复原,均按其在引理 4–6 中的用法回填:M(x) 是与 li x 相差极小的显式积分量,大 x 时 M(x)≥li x(引理 7 所需);J 含归一化因子 (2πμ)^{1/2} 与 e^{−t₀/2};χ(s) 含 (s/2π) 型前因子(源自 ζ 函数方程)。如需精确引用,请核对原书页 [190] 附近版面。

**〔译注11〕§6 的数值不等式。** 引理 6 的主不等式、(6.2)(6.9) 系列中的若干常数(22、1.005/(2π)e^{-1}、exp(t₀/12800)、T₂<0.05025 等)以及 (6.10)–(6.11) 附近的推导行,OCR 均有不同程度的破损;译文保留了可读的系数(0.93、0.051、0.00075、25≤N≤690、∑1/γ²≤0.0466 等),断裂处用文字概述补足。引理 6 结论的确切形态应以原书为准;其用途(代入定理 1 后得加权积分 >1.0025π/(μt₀))不受影响。

**〔译注12〕§9 的相位与数值结果。** θ_n 的定义(原文排作 arctan(γ_n²),疑为 arctan(1/γ_n) 或 1/ρ 辐角之误)、X_n 的构造式、sin 下界的两种情形、最终数值不等式一整行(含 452 个零点求和的结果)均有残损或疑似误植;译文按逻辑链复原:X 的取法保证前 241 项 sin>0,数值计算给出 (9.1)>0.521√(2π)/μ,从而满足 (8.2)。Elliott 803 是英国埃利奥特兄弟公司 1960 年代的晶体管计算机,主频约 1 MHz——以今日眼光看,20 分钟算完 452 项正弦和堪称"手工时代"的计算。

### 三、术语与译名

**〔译注13〕人名与术语对照。** 英厄姆=A. E. Ingham;利特尔伍德=J. E. Littlewood;蒂奇马什=E. C. Titchmarsh;哈塞尔格罗夫=C. B. Haselgrove;米勒=J. C. P. Miller;斯克斯=S. Skewes;斯坦因=P. Stein。ϑ(x)、ψ(x) 为切比雪夫函数;ρ=β+iγ 记 ζ 的非平凡零点;"整函数"(integral function)系英国旧称,今译"整函数"(entire function);"方块"(square)与"直角形区域"(right-angle segment)指复平面上以两条线段围成的标准区域。"丢番图逼近"指用有理/整数参数逼近相位以使三角和极大化的技术(引理 9 即其抽屉原理形式的推广)。
