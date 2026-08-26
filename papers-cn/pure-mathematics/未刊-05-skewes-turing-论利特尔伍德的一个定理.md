# 论利特尔伍德的一个定理

**On a Theorem of Littlewood**

> 作者:S. 斯基夫斯(S. Skewes)、A. M. 图灵(A. M. Turing);未刊手稿(1955 年前后;本篇系两人合作论文的未完成稿,由布里顿整理),译自《图灵文集·纯数学》卷 pp. 153–174(个人学习用途)


## § 1. 引言

本文拟考察 π(x) − li x 在何处取正值¹。当 x 小于约 1.42 时该量为正,由此直至 10⁷?〔原稿此处数字带问号〕为止它一直为负。数值证据提示,当 x→∞ 时 π(x) − li x 大致 behaves 如 x^{1/2}/log x;但利特尔伍德(Littlewood)(2)已经证明 π(x) − li x 会无穷多次变号。论证按黎曼假设成立与不成立两种情形分别进行。我们中的一人(Skewes(3))曾宣布:在黎曼假设成立的情形下,存在某个 x,2<x<10^{10^a},使 π(x) − li x > 0,其中 a=10^b,b=10^{34}。〔译注1:此行 OCR 严重残缺("2<x<10", where a= 10°, b= 1034"),指数塔结构系按文献中著名的 Skewes 数 10^{10^{10^{34}}} 的量级恢复。〕本文拟在不附加黎曼假设的前提下证明:存在某个 x,2<x<exp(exp 661),使 π(x)>li x。〔图灵手写批注:661 应为 686?〕

我们还将为进一步的改进做铺垫:借助大规模计算,有可能把上述界改进到约 10^a(其中 a=10^c)〔原句指数 OCR 残缺:"improving the bound to about 10", a= 10^"〕的量级;同时我们也将考察,一旦在临界线之外发现零点,会对整个局面产生何种影响。

> ¹ 这里的 π(x) 是小于 x 的素数个数,li x 是 x 的对数积分,即 $\int_0^x \mathrm{d}t/\log t$ 的柯西主值。在这一点以及其他记号问题上,我们均遵循英厄姆(Ingham)(1)。

## § 2. 方法的概要

不得不使用函数 li(x) 与 log ζ(s),这使得论证略显繁复。方法的总体思路可以通过处理下面这个类似问题来加以说明:求 θ(x)>x 在何处成立。由于

$$\psi(x)=\theta(x)+\theta(x^{1/2})+\theta(x^{1/3})+\cdots,$$

而 θ(x)∼x,这实质上就是问 ψ(x)>x+x^{1/2} 在何处成立。现在〔下式 OCR 严重残缺,按上下文恢复〕

$$\psi(x)-x=(\theta(x)-x)+\theta(x^{1/2})+\theta(x^{1/3})+\cdots,$$

于是问题实质上化归为:对哪些 t 值,不等式

$$G(t)=-\sum_{\rho}\rho^{-1}\exp\bigl((\rho-\tfrac12)t\bigr)>1$$

成立?其中求和取遍全部复零点〔译注2:指 ζ(s) 的非平凡零点,下同〕。

我们可以考虑形如 $\int G(t)f(t)\,\mathrm{d}t$ 的各种表达式。令

$$\frac{1}{\sqrt{2\pi}}\int f(t)e^{iut}\,\mathrm{d}t=F(u),$$

则有〔下式 OCR 残缺,系按傅里叶变换逐项代入恢复〕

$$\int G(t)f(t)\,\mathrm{d}t=-\sqrt{2\pi}\sum_{\rho}\rho^{-1}F\bigl(-i(\rho-\tfrac12)\bigr).$$

若 f(t) 当 t 为正时取正值,并且足够快地递减到零,那么就有可能从积分值反推出不等式 G(t)>1。例如,只要〔下列条件中的具体常数 OCR 不清,兹按可辨轮廓示意〕

$$\int_0^A f(t)\,\mathrm{d}t=1,\quad f(t)>0,$$

同时 I 充分大且为正,而 $\int_0^A G(t)f(t)\,\mathrm{d}t$ 充分小,便可推断对某个 t,0<t<A,有 G(t)>1。那个使 I 充分大且为正的 t 值,将通过丢番图逼近来求得。在进行逼近时,我们设法把 |ρ| 较小的那些项的相位调到恰当的数值,并设法使其余未经调整的项很小。因此我们希望:对 |ρ| 的大值,$F\bigl((\rho-\tfrac12)/i\bigr)$ 很小。英厄姆通过取 $f(t)=(\sin\beta t/t)^2$〔译注3:OCR 仅见 "((sin βt)/t)",幂次系按其论证(核为平方型 Fejér 核)及本文"更高次幂"之说补全〕保证了:若黎曼假设成立,则只有有限多项异于零。本文改用函数

$$f(t)=\Bigl(\frac{\sin\beta t}{t}\Bigr)^{4}\exp\bigl(-\tfrac12\alpha^2t^2\bigr),$$

它在很大程度上是受英厄姆论证启发的。这并不会使任何一项恰好为零,但只要 α 小,靠后的各项就极为微小。就当前目的而言,这个函数比英厄姆所用者有若干优点:因子 $\exp(-\tfrac12\alpha^2t^2)$ 促使积分 $\int G(t)f(t)\,\mathrm{d}t$ 迅速收敛,从而便于由 I 的值推出关于 G(t) 的不等式;这一因子还使 F(u) 成为整函数(否则它只会在两个正方形与两个直角扇形内正则)。使用 (sin βt)/t 的较高次幂,则使 F(u)〔OCR 作 f(u),疑为 F(u)〕由大变小的过渡陡峭得多,带来可观的数值上的改进。

对整个方法至关重要的一点是:黎曼假设已在区域 |γ|<1468 内经过检验(Titchmarsh(4))。

## § 3. 形式化的预备工作

**引理 1.** 设〔本句及下式 OCR 残损较重,按可辨片段与标准傅里叶–梅林反演格式恢复〕

$$F(u)=\frac{1}{\sqrt{2\pi}}\int f(t)e^{iut}\,\mathrm{d}t,\qquad \varphi(s)=\int_0^\infty h(x)x^{-s}\,\mathrm{d}x,$$

且积分 $\int_{3/2-i\infty}^{3/2+i\infty}|F(is)|\,|\mathrm{d}s|$ 与 $\int_0^\infty h(x)x^{3/2}\,\mathrm{d}x$ 收敛,又 $h(x)=o(x^{3/2})$(当 $x\to\infty$ 及 $x\to 0$ 时)〔OCR 作 $o(x^2)$,指数存疑〕,则

$$\int_{-\infty}^{\infty}h(e^t)e^{-t/2}f(t-t_0)\,\mathrm{d}t=\frac{1}{i\sqrt{2\pi}}\int_{2-i\infty}^{2+i\infty}\varphi(s)\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s.$$

证:若 $\sigma=2$,则由分部积分 $\varphi(s)=s\int h(x)x^{-s-1}\,\mathrm{d}x$,于是〔中间推导链 OCR 有损,兹按原文轮廓照录〕

$$\frac{1}{i\sqrt{2\pi}}\int_{2-i\infty}^{2+i\infty}\varphi(s)\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s$$
$$=\frac{1}{i\sqrt{2\pi}}\int h(x)\int x^{-s+1/2}\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s\,\mathrm{d}x$$
$$=\int x^{-3/2}h(x)f(\log x-t_0)\,\mathrm{d}x .$$

由于二重积分绝对收敛,交换积分次序是允许的。〔图灵手写批注若干:$t_0-\log x$ 抑或 $t-t_0$?对 f 还需什么条件?指数处应为 $+i(s-\tfrac12)$ 与 $+is$ 否?〕

**引理 2.** 若函数 f、F 受引理 1 的诸条件约束,则

$$\int e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,\mathrm{d}t=\frac{1}{i\sqrt{2\pi}}\int_{2-i\infty}^{2+i\infty}s^{-1}\bigl(\log\zeta(s)-g(s)\bigr)\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s,$$

其中

$$M(t)=\int u^{-1}e^{u}\,\mathrm{d}u,\quad\text{积分自 }0.1\text{ 至 }\max(t,0.1),$$

而〔定义式两处 OCR 互相矛盾,按下文"当 $\Re s>1$ 时亦可写作"一句及引理 3 反推取此形式,见译注4〕

$$g(s)=\int_{0.1}^{\infty}t^{-1}\exp\bigl((1-s)t\bigr)\,\mathrm{d}t,$$

积分沿一条平行于实轴的路径进行。〔原稿批注:s 为实数且 <1 时如何定义?〕

我们先以 h(x)=Π(x)、再以 h(x)=M(log x) 应用引理 1,并把两个结果合并。注意当 $\Re s>1$ 时 g(s) 亦可写成上述实轴积分形式。

**引理 3.**
(a) 若对数取主值,则函数 $g(s)+\log(s-1)$ 无奇点。
(b) 对任意 s,$|g(s)|<\pi+\bigl|\tfrac{1}{2(s-1)}\bigr|\exp\bigl(\tfrac12-0.1(1-\sigma)\bigr)$。〔译注5:此不等式右端 OCR 含混("π + $1 exp($ -- 0.1(1 - o))"),系数、分母与符号均存疑;原稿旁另有批注:"[1/|s−1|;但 g 含混][负号?][log sin φ?]"〕

证:(a) $g(s)+\log(s-1)$ 可定义为正则函数 $\bigl(1-\exp(-0.1(s-1))\bigr)/(s-1)$ 的不定积分。
(b) 该不等式可通过沿一段圆弧及正实轴的一部分积分来证明。

**引理 4.** 若函数 f 与 F 如引理 1 所述互为傅里叶变换,g 为引理所定义之函数,且 F(is) 在任一条带形 $\alpha\le\sigma\le 2$ 内有界〔原稿于此处标 "?"〕,则

$$\int e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,\mathrm{d}t=I_1+I_2+\sum_{\rho}I_{3,\rho}+J\quad[\text{负号?}]$$

其中求和取遍 ζ 函数的非平凡零点,$\alpha>\tfrac12$〔原稿标 "?"〕,而〔以下四式的具体形状 OCR 严重残缺,仅能辨认骨架;兹按第 157 页所述柯西定理移线论证(积分直线自 σ=2 移至 $\sigma=\tfrac12-4\Delta$,在零点处得留数 $I_{3,\rho}$、在 s=0 处得留数 J)恢复其大意,见译注6〕

$$I_1=\frac{1}{i\sqrt{2\pi}}\int_{2-i\infty}^{2+i\infty}s^{-1}\Bigl(\log\frac{\zeta(s)}{(s+1)(s+2)(s+2)}\Bigr)\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s,$$

$$I_2=\frac{1}{i\sqrt{2\pi}}\int_{-\Delta-i\infty}^{-\Delta+i\infty}s^{-1}\Bigl(\log\frac{\zeta(s)}{(s+1)(s+2)(s+2)}-g(s)\Bigr)\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s,$$

积分自 $-\Delta-i\infty$ 至 $-\Delta+i\infty$;

$$I_{3,\rho}=\sqrt{2\pi}\int_{\mathcal{C}_\rho}s^{-1}\frac{\zeta'(s)}{\zeta(s)}\,F\bigl(\sigma-i(s-\tfrac12)\bigr)\exp\bigl((s-\tfrac12)t_0\bigr)\,\mathrm{d}s,$$

$$J=(\text{s=0 处之留数,含 }\zeta(0)\text{ 与 }g(0))F(\tfrac{i}{?})\cdots\quad(\text{无法辨认}).$$

〔原稿批注:"[负号?][log 与 g(0) 均含混]"〕

形式上,这一结果可由柯西定理得到:把 I₂ 之被积函数的积分直线从 σ=2 移到 $\sigma=\tfrac12-4\Delta$。被积函数在这两条直线上都绝对收敛,于是〔此处一句 OCR 完全乱码("...n s s e si r e d o ssu o s"),大意应为水平边上的积分当 $T_r\to\infty$ 时可忽略〕,且 $I_{4,r}\to 0$,其中

$$I_{4,r}=\frac{1}{i\sqrt{2\pi}}\int s^{-1}\Bigl(\log\frac{\zeta(s)}{(s+1)(s+2)(s+2)}-g(s)\Bigr)\exp\bigl((s-\tfrac12)t_0\bigr)F\bigl(-i(s-\tfrac12)\bigr)\,\mathrm{d}s,$$

积分自 $\tfrac12-4\Delta+iT_r$ 至 $2+iT_r$;另有一个类似的序列取 $T_r\to-\infty$。下面我们只考虑前一情形。

〔手写段落:〕被积函数的奇点是……直线 σ 到 σ−2 上的那些点,可能还有若干别的奇点……然而〔公式无法辨认,似为 $\zeta(s)(s+1)(s+2)^2/(2\pi)^2$ 一类表达式〕在任何整数点都没有极点,而且显然在其他任何实点也没有。因此唯一的实奇点就是 O 点,由它产生留数 J。

〔打字稿续:〕序列 T_r 可按英厄姆《素数分布》(1932)之定理 26 选取。此时将存在 A,使得当 $\tfrac12-4\Delta\le\sigma\le 2$ 时

$$\bigl|(\zeta'/\zeta)(\sigma+iT_r)\bigr|<A(\log T_r)^2 .$$

量 A 只依赖于 Δ。于是

$$\bigl|\log\zeta(\sigma+iT_r)\bigr|\le\bigl|\log\zeta(2+iT_r)\bigr|+(1.5+4\Delta)A(\log T_r)^2<1+(1.5+4\Delta)A(\log T_r)^2,$$

从而

$$|I_{4,r}|<T_r^{-1}\bigl(1+(1.5+4\Delta)A(\log T_r)^2\bigr)(1.5+4\Delta)M\exp(1.5\,t_0),$$

其中 M 是 $|F(-i(s-\tfrac12))|$ 在区域 $\tfrac12-4\Delta\le\sigma\le 2$ 内的上界。显然当 r→∞ 时 $I_{4,r}\to 0$。〔原稿批注:自"从而"至"r→∞"一段细节?另:s、s+1、s+2 与 −g(s) 各处?〕

## § 4. 具有特殊核的结果

到目前为止,函数 f 所受的限制还比较宽泛;现在我们令 f(t)=f₁(t)f₂(t),其中

$$f_1(t)=\frac{\sin\mu t}{\mu t},\qquad f_2(t)=\exp\bigl(-\tfrac12\alpha^2t^2\bigr),$$

〔f₁ 的分母 OCR 仅余 "sinμt" 于分式上方,归一化按惯例补全;见译注7〕并且我们还将取

$$\alpha^2 t_0=4\Delta=400,$$

尽管这些代换并不总是代入使用。μ 与 t₀ 的具体数值眼下尚不选定,但我们暂设 $50<\mu<250$ 且 $10^4<t_0$。函数 F、F₁、F₂ 将如同引理 1 那样分别表示 f、f₁、f₂ 的傅里叶变换。

**引理 5.** 我们有

$$F_1(z)=\sqrt{2\pi}\,(2\mu)^{-1}K(z/2\mu)\quad(z\ \text{为实数}),$$
$$F_2(z)=\alpha^{-1}\exp(-z^2/2\alpha^2),$$
$$F(z)=\frac{1}{\sqrt{2\pi}}\int F_2(z-u)F_1(u)\,\mathrm{d}u,$$

其中

$$K(x)=\begin{cases}1-|x|^2, & 0\le|x|\le 1,\\ (2-|x|)^2, & 1\le |x|\le 2,\\ 0, & 2\le |x|.\end{cases}$$

〔原稿于 K 的前两支旁注有 "[−(1−|x|)²+(2−|x|)²]"、"[（2−|x|)²]" 等疑问记号〕这些是傅里叶变换理论中若干著名结果的直接应用。

**引理 6.** 设 z=x+iy,x、y 为实数,则

(a) $|F(z)|\le\alpha^{-1}\exp(\cdots)$ 〔右端指数因子在 OCR 中丢失〕;
(b) 当 $|x|\ge 4\mu$ 时,$|F(z)|\le\alpha^{-1}\exp(\cdots)$;
(c) $\displaystyle\int_{c-i\infty}^{c+i\infty}\bigl|F(iz)\bigr|\,|\mathrm{d}z|\le\sqrt{2\pi}\alpha\exp(\cdots)$〔c 为实数〕;
(d) 若 z 为实数,则 $|F(z)-\tilde F(z)|\le\sqrt{2\pi}\alpha(4\mu^2)^{-1}$〔原稿批注:"$\sqrt{2\pi}\alpha^2(16\mu^2)^{-1}$?"〕;
(e) $|F'(z)|\le(\alpha\mu)^{-1}$〔原稿批注:"[是否还应乘以某因子?]"〕。

证:(a)、(b) 的证明用不等式

$$|F(z)|\le\frac{1}{\sqrt{2\pi}}\int\bigl|F_2(z-u)\bigr|\,\bigl|F_1(u)\bigr|\,\mathrm{d}u,$$

并注意由于 $F_1(u)\ge 0$,有

$$\frac{1}{\sqrt{2\pi}}\int\bigl|F_1(u)\bigr|\,\mathrm{d}u=\frac{1}{\sqrt{2\pi}}\int F_1(u)\,\mathrm{d}u=f(0),$$

又被积函数在 $|u|<4\mu$ 之外为零,故 $|F(z)|<M$〔原稿标 "?"≤"〕,这里 M 是 $|F_2(z-u)|$ 在此范围内的最大值。
(c) 的证明:

$$\int_{c-i\infty}^{c+i\infty}\bigl|F(iz)\bigr|\,|\mathrm{d}z|\le\iint\bigl|F_2(iz-u)\bigr|\,\bigl|F_1(u)\bigr|\,\mathrm{d}u\,|\mathrm{d}z|=f(0)\int_{c-i\infty}^{c+i\infty}\bigl|F_2(iz)\bigr|\,|\mathrm{d}z|=\sqrt{2\pi}\alpha\exp(\cdots).$$

〔原稿批注:"correct but obscure"(正确但费解)。〕
(d):$|F(z)-\tilde F(z)|=\Bigl|\int\bigl(F_1(z-u)-F_1(z)+uF_1'(z)\bigr)F_2(u)\,\mathrm{d}u\Bigr|$〔原稿批注 "[+]"〕,因为 F₁ 是偶函数;

$$\le\frac{1}{4\tfrac12\mu^2}\int u^2|F_2(u)|\,\mathrm{d}u\quad[\text{实为 }u^2][\text{乘数?}],$$

因为 $|F_1''(z)|\le\sqrt{2\pi}/4\tfrac12\mu^2$〔原稿批注 "[μ²]"〕$=\sqrt{2\pi}\cdots/4\mu^2$(无法辨认)。〔原稿批注:"4μ² 应为 16μ³?"〕
(e):(此证明在本份打字稿副本中缺失,参见 COHEN 与 MAYHEW 1968,p. 695,引理 2 之 (i)。)

**引理 7.** 若〔题设条件 OCR 残损:对满足 $|y|\le 4\mu+50$ 的每一零点纵坐标 y 均有

$$\bigl|(\tfrac12+iy)^{-1}-F(y)\exp(iyt_0)\bigr|\le(\text{某小量}),$$

则〕当 $t_0>10^4$、$50<\mu<250$ 时,

$$\int e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,\mathrm{d}t\ \text{与主项之差小于}\ \mu^{-1}t_0^{-3/2}.[\text{原稿批注:"[?+]"}]$$

我们将证明:按引理 4 的记号,

- (a) $|J|<10^{-8}t_0^{-3/2}$;
- (b) $|I_1|<10^{-8}t_0^{-3/2}$;
- (c) $|I_2|<10^{-8}t_0^{-3/2}$;
- (d) $\Bigl|\sum_{|y|<4\mu+50} I_{3,\rho}\Bigr|<\dfrac{1}{\sqrt{2\pi}}\cdot\dfrac{0.02}{\mu}\,t_0^{-3/2}$ 与 $\dfrac{0.052}{?}\cdots$,求和范围 $|y|<4\mu+50$;〔此式 OCR 残损:"[左端括号左右存疑][右端存疑]"〕
- (e) 当 $|y|\ge 4\mu+50$ 时,$\sum|I_{3,\rho}|<10^{-8}t_0^{-3/2}$。

证:由引理 3 有 $|g(0)|<\tfrac12\pi$〔原稿标 "?"〕。又 ζ(0)=−½,ζ(2)=π²⁄6,故 $|J|<16$〔原稿批注:"正确但无用;是否应有 $|J|<2\exp(-\tfrac12 t_0)$?"〕,于是由 $t_0>10^4$ 得 (a)。

为证 (b),把积分直线移到 σ=½ 上,并注意在该直线上 $\bigl|s^{-1}\log\bigl(\zeta(s)/((s+1)(s+2)(s+2))\bigr)\bigr|<10$。于是

$$|I_1|<10e^{-\frac14 t_0}\int_{1/4-i\infty}^{1/4+i\infty}\bigl|F\bigl(\sigma-i(s-\tfrac12)\bigr)\bigr|\,|\mathrm{d}s|<10\alpha\exp(-\tfrac12 t_0+\alpha^2)\quad[\text{由引理 6(e)}]$$
$$=\tfrac12\,t_0^{1/2}\exp\bigl(t_0(\tfrac12+\alpha^2/?))<10^{-8}t_0^{-3/2}.[\text{原稿批注:"[200]"}]$$

〔此链末端 OCR 残损("= $tg1/2 exp(to(↓+ zx))"),常数与指数结构均存疑。〕

为估计 I₂,先考察 log(ζ(s)/((s+1)(s+2)(s+2))) 的性态。利用函数方程〔下式 OCR 严重残缺,仅能辨出 $(2\pi)^{s-1}$、$\sin\pi s/2$、$\Gamma(?-s)$ 等片段,兹不强行复原〕可得:当 $\Re s\le -1$〔原稿批注:"[应为 −3?]"〕时,

$$\Bigl|\log\frac{\zeta(s)}{(s+1)(s+2)(s+2)}\Bigr|\le\pi+2\cdot\tfrac12\log\tfrac12\pi+2+\log\Bigl|\frac{s+2}{s+2}\Bigr|<11.\ [\text{原稿批注:"[?2]"}]$$

又由引理 3(b) 有 $|g(s)|<\tfrac12\pi$〔原稿旁有插入记号 "[caret]"〕,于是再用引理 6(c):

$$|I_2|<15\tfrac12\alpha\exp(-i\Delta t_0)\bigl[\exp(0.1(1-\sigma)),\text{凡两处}\bigr]=300\,t_0^{-1/2}\exp(-200\,t_0).$$

〔原稿批注:"[less than?](是"小于"吗?)";并注明 "'200' 中的 '2' 亦被质疑"。此式 OCR 残损较重。〕

余下的是估计 I₃,ρ。由于当 $|\gamma_0|<4\Delta$? 时 $\Re\rho=\tfrac12$〔OCR:"Since Ro=↓ for ↓@ol<4",Δ 与条件存疑〕,我们可以把含 $F(-\gamma)$ 的主项分离出来($F(-\gamma)=F(\gamma)$,因 F 为偶函数)〔原稿标 "?"〕,写成 $I_{3,\rho}=($主项$)+M_{3,\rho}$,其中〔M₃,ρ 之定义式无法辨认〕

$$M_{3,\rho}=\int F\bigl(-i(s-\tfrac12)\bigr)\cdots\exp\bigl((s-\tfrac12)t_0\bigr)\,\mathrm{d}s.\ (\text{无法辨认})$$

于是〔以下诸估计式中 γ、α、μ 诸常数的归属多处被原稿质疑,兹照录轮廓〕

$$|I_{3,\rho}|\le\gamma^{-1}\exp(-\tfrac12 t_0)\,|F(\gamma)|\le(20\gamma t_0^{1/2})^{-1}\exp(-\tfrac12 t_0)<0.001\,\gamma^{-1}t_0^{-3/2}\mu^{-1},$$

〔原稿批注:此处三处符号 γ 均被质疑(并非 F(γ))〕且

$$|M_{3,\rho}|\le\gamma^{-2}\,2\alpha^{-1}\mu^{-1}\int_0^{t_0^2}\cdots\exp\bigl(-x/t_0\bigr)\,\mathrm{d}x<\frac{0.4}{\gamma^2\mu}t_0^{-3/2},$$

〔原稿批注:"成立,但非由 L₃ 所证;见 INGHAM 1932,注 22、23……";积分外之 "2" 与 "μ⁻¹" 亦被质疑〕从而由 $\sum\gamma^{-2}<\infty$,

$$\sum_{|y|<4\mu+50}|M_{3,\rho}|<\mu^{-1}\,0.02\,t_0^{-3/2}.$$

用分部积分,若 $|\gamma|<4\mu+50$,则

$$|I_{3,\rho}|=(t_0|\gamma|)^{-1}\exp(\tfrac12-\alpha^2/2)\bigl(F(-\gamma)-F(-\gamma+2i)\bigr)\cdots\int F'\bigl(-i(s-\tfrac12)\bigr)\exp\bigl((s-\tfrac12)t_0\bigr)\,\mathrm{d}s$$
$$\le(t_0\alpha\gamma)^{-1}\Bigl(2\exp\bigl(t_0(-\tfrac12+\tfrac{1.01}{\mu^2 t_0})\bigr)+\cdots\Bigr)\le 0.051\,\gamma^{-1}t_0^{-3/2}\mu^{-1}.$$

〔中间若干行("[（iy−2)t₀][-?][-?][+]""(½)≥…+α…y" 等)OCR 无法成句,已按首尾轮廓衔接。〕

(d) 由以上结果归并即得。

对情形 $|\gamma|\ge 4\mu+50$:由引理 6(b),

$$|I_{3,\rho}|\le 2\sqrt{2\pi}\alpha\,\gamma^{-1}\exp\bigl(\tfrac12 t_0+(2\alpha^2)^{-1}((?)^2-(|\gamma|-4\mu)^2)\bigr),$$

而由于〔一句倒置乱码 "ay am os<n pue os+t souss 1ng",大意:"但 |γ|>4μ+50,故 σ<½"?〕

$$(|\gamma|-4\mu)^2>50(|\gamma|-4\mu)>1250+25(|\gamma|-4\mu),$$

于是〔求和估计 OCR 残损:"≤(24μ/…)exp(−t₀)"〕

$$\sum_{|\gamma|\ge 4\mu+50}|I_{3,\rho}|\le\frac{24\mu}{?}\exp(-t_0)\cdots,$$

因为 $\gamma\exp(-t_0\gamma^2/32)$ 当 $\gamma>32/t_0$ 时是递减函数,而 $4\mu\ge 200>32/t_0$〔OCR 作 ">3/to",疑为 ">32/t₀"〕。于是

$$\sum_{|\gamma|\ge 4\mu+50}I_{3,\rho}<1.2\,\mu\alpha^{-1}\exp(-t_0)<0.01\,t_0^{-3/2},\quad(\mu<250).$$

〔原稿批注:"[(e) 写的是 10⁻⁸(就其本身而言无误);但与题设没有关联]"〕

**引理 8.** 若 $t_0>10^4$,且

$$\int e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,\mathrm{d}t>1.0025-\frac{1}{\mu t_0},$$

其中,如前所述,

$$f(t)=\Bigl(\frac{\sin\mu t}{\mu t}\Bigr)^4\exp\bigl(-\tfrac12\alpha^2t^2\bigr),\quad 50<\mu<250,$$

$$M(t)=\int u^{-1}e^{u}\,\mathrm{d}u,\quad\text{自 }0.1\text{ 至 }\max(t,0.1),$$

则存在某个 $t_1$,$0.974\,t_0<t_1<1.053\,t_0$,使得

$$\Pi(\exp t_1)-\mathrm{li}\exp t_1>1.002\,t_1^{-1}\exp(t_1).$$

〔译注8:结论右端按 OCR 直录("1.002 t-' exp(t)"),其量纲与上下文不尽吻合,存疑。〕

证:我们有〔一组傅里叶积分计算,OCR 大部残损:∫ sinμt/(μt) 之各阶矩、√(2π)、(2μ)³ 等片段可辨;"[4μ³?]" 为原稿批注〕,从而〔由主积分超过 $1.0025-1/(\mu t_0)$ 之假设〕

$$\int\frac{\sin^4(\mu(t-t_0))}{(\mu(t-t_0))^4}\exp\bigl(-\tfrac12\alpha^2(t-t_0)^2\bigr)\Bigl(1-\bigl(1-\tfrac{t}{t_0}\bigr)^3\Bigr)\,\mathrm{d}t>\frac{1.0025}{?}\cdots\quad(\text{无法辨认}).$$

于是对某个 t₁:

$$\Pi(\exp t_1)-M(t_1)>0.0025\,t_1\exp\bigl(J+\tfrac12\alpha^2(t_1-t_0)^2\bigr),$$

其中 $\alpha=\tfrac12(1.005)\,[?]$〔原稿批注:"[]"内不明〕且 $J=\tfrac12 t_1+200(t_1-t_0)^2/t_0$。

现在肯定有 $t_1>0.1$,否则 Π(exp t₁)=0 且 M(t₁)=0。但此时

$$\Pi(\exp t_1)=\cdots(\text{无法辨认})<\exp t_1+t_1\exp(t_1)<2\exp t_1;$$

因此

$$\frac{200(t_1-t_0)^2}{t_0}<\tfrac12 t_1+\log(3t_0).$$

若 $t_1>t_0$,则 $\log(3t_0)<0.01\,t_0<0.01\,t_1$,故

$$200\bigl(0.1275(t_1-t_0)^2\bigr)<0.1275(t_1+t_0)^2,\qquad t_1<1.053\,t_0 .$$

而若 $t_1\le t_0$,则

$$200(t_1-t_0)^2<0.051\,t_1^2,\qquad t_1>0.974\,t_0 .$$

〔此二行 OCR 数字结构存疑,照录。〕只剩下要证 M(t₁) ≤ li eᵗ¹〔原文作 "M(t)$<lie'"〕;而这只要 li e^{0.1}<0 即可推出〔原稿标 "[?>]"〕。但是

$$\mathrm{li}\,e^{0.1}=\int_{0.1}^{e^{0.1}}\frac{\sinh t}{?}\cdots+\int_0^{0.2}\cdots\le\int_{-0.2}^{0.1}t^{-1}\sinh t\,\mathrm{d}t+\tfrac12\sinh 0.1<0\quad[\text{凡两处须插入 2}].$$

〔此段公式 OCR 残损较重("c0.1 $ sinh t … t-'dt+ … P1 … 0. … t-' dt + $ sinh 0.1 <0"),仅能辨出被积函数含 sinh t 与 t⁻¹、积分限涉及 −0.2 与 0.1。大意:M(t₁) 在 $t_1\le 0.1$ 时为零,而 li(e^{0.1})<0,故 M(t₁)≤li eᵗ¹ 自动成立;兹按大意衔接。〕

**引理 9.** 若 $x\ge e^8$,则

$$\mathrm{li}\,x<\frac{x}{\log x-1.5}.$$

证:我们有〔本证明诸式 OCR 残损甚重,轮廓如下〕

$$e^{-a}\,\mathrm{li}\,e^{a}=R\int\frac{(1-t/a)?}{?}\cdots$$

只要积分沿一条避开 a 的围道进行,而 a 为实数〔且为正〕;被积函数形如 $\dfrac{t^2e^{-t}}{a^2(a-t)}$(无法完全辨认)。取围道 $t=u(1+\tfrac12 i)$(u 为实数),得〔若干中间界:"6.25"、"(±√5a)^{?}e^{−a}"、"a³" 等片段〕

$$e^{-a}\,\mathrm{li}\,e^a<\frac{6.25}{a^3}\quad\text{若 } a\ge 8 .$$

〔原稿批注:"{−(S'I−D)>}" 等无法辨认。〕

**引理 10.** 若下列两条件之一成立:

(a) $(\Pi(x)-\mathrm{li}\,x)\,x^{-1/2}\log x>1.002$ 且 $x>e^{2000}$;

或

(b) $(\Pi(x)-\mathrm{li}\,x)\,x^{-1/2}\log x>1.6$ 且 $16\le x<e^{16}$;〔译注9:(b) 行 OCR 为镜像倒置("91s<x pun 9'1 <x801z/-x(x-(x)1"),阈值 1.6 与区间端点系翻转恢复;"[16 存疑]" 为原稿批注〕

则或者 π(x)>li x,或者 π(x^{1/2})>li x^{1/2}。

证:先对 x>16 估计 Π(x) − π(x) − π(x^{1/2}):

$$\Pi(x)-\pi(x)-\pi(x^{1/2})=\tfrac13\pi(x^{1/3})+\sum_{r\ge4}\frac{1}{r}\,\pi(x^{1/r})$$
$$\le x^{1/3}+\sum_{r=4}^{\log_2 x}\frac{x^{1/r}}{3r},$$

求和自 r=4 至 log₂x(因为当 0<u<e 时 π(u)<2,而当 e<u 时 π(u)<2+½u)。〔原稿批注:"正确但费解;π(u)<2 用于 log x<r≤log₂x 的那些项"〕

$$\le x^{1/3}+2\log(\tfrac12\log_2 x)+x^{1/4}\sum_{r=4}^{\infty}r^{-2}$$

(因为 rx^{1/r} 在范围 4≤r≤log x 内随 r 递增而递减)

$$\le x^{1/3}+2\log\log x+0.4\,x^{1/4}.$$

于是,若 π(x) ≯ li x 且 π(x^{1/2}) ≯ li x^{1/2}〔原稿批注:"[?≤]"〕,则

$$(\Pi(x)-\mathrm{li}\,x)x^{-1/2}\log x<x^{-1/2}\,\mathrm{li}\,x^{1/2}\log x+x^{-1/6}\log x+0.4\,x^{-1/4}\log x+\frac{2\log\log x}{\log x}$$
$$\le\tfrac12\,x^{-1/2}\,\mathrm{li}\,x^{1/2}\log x\qquad[x\ge e^{16},\ \text{由引理 }9],$$

而这与 (a)、(b) 两者都矛盾。

**定理 1.** 设 50<μ<250、10⁴<t₀,且〔题设总括句 OCR 残损:"Zlxl<4u+s0 v~1<3",疑为"对每一零点纵坐标 y,|y|<4μ+50 且 y⁻¹<3"一类条件〕若

$$\sum_{0<y<4\mu+50}K(y)\,\Bigl|\Bigl(\frac{1}{\tfrac12+iy}\Bigr)-F(y)\exp(iyt_0)\Bigr|>0.502\,\mu^{-1}\Bigl(\frac{\tfrac12\log?}{2}\Bigr),$$

〔此式 OCR 严重残损("R$. exp(iyto)$ > 0.502 μ-(↓π)/2");左端括号与负号均被原稿质疑;右端指数结构无法确定,见译注10〕则存在某个 t₁,$0.974\,t_0<t_1<1.053\,t_0$,使得

$$\pi(\exp t_1)>\mathrm{li}\,\exp t_1\quad\text{或}\quad\pi(\exp(\tfrac12 t_1))>\mathrm{li}\,\exp(\tfrac12 t_1),$$

〔此行 OCR 为倒置乱码(" dxa!1 <(dx) o 1 dx!<(1 dx"),按引理 8 + 引理 10 的推理链恢复〕并且此时

$$\frac{t_1}{0.021+0.052\sum y^{-2}}<0.177\,t_1^{-1/2}<0.00177 .$$

〔末行求和范围 OCR 残损("|>|<4μ+50",应为 |y|<4μ+50)。〕

---



于是

$$\int_0^\infty e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,dt>1.004-0.00177>1.00,$$

引理 8 的条件得到满足，从而引理 10 的条件 (a) 也随之满足。

## 5. 丢番图逼近

直到现在，我们还没有太多用到对泽塔函数的大量计算所得到的结果。我们只用了"$|\gamma|<1468$ 时非平凡零点全部位于临界线上"这一事实——其实即便不用它也完全可以。现在我们要再进一步，利用关于这一范围内零点位置的若干信息。蒂奇马什(Titchmarsh)曾提到过〔编者原注：where?（出处待查）〕：若 $t_n$ 由条件 $\arg\zeta(\tfrac12+\tfrac12 i t_n)=n\pi$ 定义〔编者原注建议改为：定义 $\theta(t)=\pi-\arg\bigl(\pi^{-1/2}\zeta(\tfrac12+it)\bigr)$，$\theta(t_n)=n\pi$，$t_n>0$，$n=1,2,\dots$〕，那么当 $0<t_n<1468$ 时有 $N(t_n)-n=-1$、$0$ 或 $1$；而且若 $N(t_n)-n\neq0$，则 $N(t_{n+1})=n+1$ 且 $N(t_{n-1})=n-1$。此外 $\arg\zeta(\tfrac12+it)$〔即 $\theta(t)$〕是单调的〔对 $t>\dots$〕。由这些事实容易看出：当 $0<t<1468$ 时，$\pi^{-1}\arg\zeta(\tfrac12+it)<2$。我们还有：当 $t>51$ 时

$$\bigl|\pi^{-1}\arg\zeta(\tfrac12+it)-\tfrac{t}{2\pi}\log\tfrac{t}{2\pi}+1\bigr|<\tfrac14,$$

而当 $t\le51$ 时 $|S^*(t)|<2\tfrac14$，故对 $0<t<1468$ 总有 $|S^*(t)|<2\tfrac14$。〔编者原注：上界 $\tfrac14$ 可以换成一个小得多的常数，参见 TITCHMARSH 1935，第 238 页 (i)；又"$2\tfrac14$"处原稿本身即标有疑问〕这里 $S^*(t)=N(t)-\dfrac{t}{2\pi}\log\dfrac{t}{2\pi}-1$。〔译注1〕

**引理 12．** 若 $1\le h\le220$，则

$$\Bigl|\sum_{2\pi<\gamma<2\pi h}K(\gamma)\log\gamma\Bigr|<2\tfrac14\bigl(f(h)+\operatorname{var}f\bigr),$$

其中求和取遍 $2\pi<\gamma<2\pi h$。〔译注2〕

我们利用上面证得的不等式 $|S^*(t)|<2\tfrac14$（$0<t<1468$），并注意到 $S^*(2\pi)=0$。于是

$$\sum_{2\pi<\gamma<2\pi h}K(\gamma)\log\bigl|\zeta(\tfrac12+i\gamma)\bigr|
<\int_{2\pi}^{2\pi h}\log\bigl|\zeta(\tfrac12+iu)\bigr|\,df(u)
=f(h)\,S^*(2\pi h)-\int_{2\pi}^{2\pi h}S^*(2\pi u)\,df(u)
\le 2\bigl(f(h)+\operatorname{var}f\bigr).$$

为了得到一个稍好一点的结果，我们将使用狄利克雷定理的一个变形。

**引理 13．** 给定实数 $\alpha_1,\dots,\alpha_m$、一个正实数 $T$ 以及正整数 $N_1,\dots,N_m$，则可以找到整数 $r$，$1\le r<N_1N_2\cdots N_m$，使得对每个 $i$（$1\le i\le m$），$rT\alpha_i$ 与某个整数之差不超过 $1/N_i$。

证明与狄利克雷定理（INGHAM 1932，定理 J）的证明非常相似，细节留给读者。

**引理 14．** 若在函数 $f$、$F$ 中取 $\mu=60\pi$，则可以找到 $t_0$，使得

$$e^{20}<t_0<e^{60.9}$$

且

$$2S\equiv\sum_{0<y<4\mu+50}\Bigl(\tfrac14+y^2\Bigr)^{-1}F(y)\Bigl(\tfrac14-y\sin(yt_0)+i\cos(yt_0)\Bigr)>1.004.\quad\text{〔编者原注:?minus（是否应为负号？）〕}$$

〔译注3〕我们有

$$2S=\sum_{0<y<4\mu+50}\Bigl(\tfrac14+y^2\Bigr)^{-1}F(y)\Bigl(\tfrac14-y\sin(yt_0)+i\cos(yt_0)\Bigr)$$
〔编者原注在此式旁标有 "?minus"、"plus" 两条疑问〕，

并将它拆为

$$S_1=-\sum_{0<y<4\mu+50}\Bigl(y^2+\tfrac14\Bigr)^{-1}y\sin(yt_0),$$

$$S_2=\sum_{0<y<4\mu+50}\Bigl(y^2+\tfrac14\Bigr)^{-1}\cos(yt_0)\quad\text{〔编者原注：?minus〕},$$

$$S_3=\sum_{0<y<4\mu+50}\sin(yt_0).$$

那么

$$|S_3-S_1|\le\sum_{0<y<4\mu+50}\Bigl|\frac{\tfrac14}{y^2+\tfrac14}-\frac{y}{y^2+\tfrac14}\Bigr|\,|\sin(yt_0)|
\le\sum_{0<y<4\mu+50}\frac{1}{4y^3}<0.0004,$$

以及

$$|S-S_1-S_2|\le\sum\bigl|F(y)-F(\dots)\bigr|\;\mu\;\text{〔求和范围？——编者原注〕}\le\frac{\alpha}{2\mu}\cdot\frac{600}{120\pi}<0.0035,\qquad t_0\ge e^{20}-1.$$

且 $e^{20}-1<\tau<e^{20}$。然后我们按引理 13 选取 $t_0$，使得 $t_0$〔编者原注：query〕是 $\tau$ 的倍数，并且对每个 $\gamma$（$0<\gamma<120\pi$），$\dfrac{\gamma}{2\pi}t_0$ 与某个整数之差不超过 $\dfrac{\gamma}{1920\pi}$。

这样的 $t_0$ 可以在下述范围内找到：

$$e^{20}+1<t_0+\frac{\tau}{2\beta}<\bigl(e^{20}+2\bigr)\prod_{\gamma_0<\gamma<120\pi}\bigl(1+1920\,\gamma^{-1}\pi\bigr).$$
〔编者原注：should π/(2β) be …?（$\pi/2\beta$ 是否应为别的什么？）〕

现在

$$\log\prod_{2\pi<\gamma<120\pi}\bigl(1+1920\,\gamma^{-1}\pi\bigr)
<\sum_{2\pi<\gamma<120\pi}\log 1920\,\gamma^{-1}\pi
<\dots=960\log\frac{1800\pi}{900}-\log u+\frac{\dots}{900}\quad\text{〔数值 }647[\?672]\text{，字迹难辨〕},$$

从而 $\log\prod_{2\pi<\gamma<120\pi}(1+1920\,\gamma^{-1}\pi)>6.01$，$e^{20}<t_0<e^{60.9}$。〔译注5〕

我们有

$$S\ge S_1-\sum_{\substack{0<y<120\pi\\ 120\pi/y<1/8}}\min\sin\frac{(1+n)y}{120\pi}\;(\dots)-\sum_{120\pi<y<240\pi}(\dots)\quad\text{〔符号存疑——编者原注〕},$$

而若记〔译注6〕

$$\varphi(\nu)=
\begin{cases}
\dfrac{(2\pi\nu)^{-1}}{\pi\nu(1+n)}\min\sin(\dots), & 0<\nu<60,\\[3mm]
(2\pi\nu)^{-2}\ \ (<\tfrac18), & 60\le\nu\le120\quad\text{〔编者原注：应为 }\le\text{〕},
\end{cases}$$

则由引理 12 将有

$$S_3\ge\sum_{0<y<240\pi}(\dots)\ge 120\int_1^{120}\varphi(\nu)\log\nu\,d\nu+(\operatorname{var}\varphi)\cdot20
\gtrless \int_1^{120}\varphi(\nu)\log\nu\,d\nu+0.0097.\quad\text{〔符号存疑——编者原注〕}$$

但通过直接计算我们求得

$$\int_1^{120}\varphi(\nu)\log\nu\,d\nu>0.5080.$$
〔原稿此处有一条边注，大意为 "…else with…correct…p..)"，字迹无法完全辨认。〕

又有

$$S_2\ge 0.49\sum_{0<y<120\pi}y^{-2}c(y)-\sum_{120\pi<y<240\pi}y^{-2}\varphi(y)
-(240\pi)^{-2}\sum K(y)\max_{0<y<120\pi}\frac{\sin\bigl((1+n)y\bigr)}{\dots}>0.008,$$
〔极大号下的分式原稿字迹难辨（illegible）。〕

于是

$$S>0.5080+0.003-0.0097-0.0004-0.0035=0.5026.\quad\text{〔原稿带问号；见译注7〕}$$

现在我们可以陈述最终结果了。

**定理 2．** 存在 $x$，……，使得 $\pi(x)>\operatorname{li}x$。

（这里"……"代表两个条件之一，二者在手稿中都被划掉了。它们是

$$2<x<\exp\exp a<10^b,\qquad b=10^c,$$

其中 $(a,c)=(697,303)$ 或 $(661,287)$。）这由定理 1 与引理 14 推出。〔译注8〕

到此为止，我们的结果还有一个共同特点，就是余项的极度微小，我们的主要精力一直放在获得〔……〕上。〔原文此句与下文之间似有脱漏〕然而从今以后，我们将提出严格得多的要求。

## 6. 计算性的丢番图逼近

如果能得到相当精确的各个 $\gamma$ 的数值，那么应当有可能用数字计算机通过直接计算求出一个 $t_0$ 的值。这首先需要把头三百个左右的零点算到比如说小数点后七位，这可能需要十到二十小时的计算时间。然后我们取 $\mu=200$（比如说），使我们的和式延伸到 $800$。由于 $700$ 以上〔原稿此处符号缺失——编者原注 "(symbol missing)"〕的值很小，我们不必计算那一带的零点。一个合理的做法是系统地遍历所有使第一个零点满足 $\sin(\gamma_1 t_0)=1$ 的 $t_0$ 值。〔原文此处疑脱一动词〕让我们粗略估计一下，在运气不算太坏的前提下，按这一方案大约在何处可以指望找到解。

假设除第一项以外的各项之和是相互独立且服从正态分布的。容易算出 $S$ 的分布的标准差为

$$\Bigl(\sum_y K(y)^2\bigl(\tfrac14+y^2\bigr)^{-1}\Bigr)^{1/2}\quad\text{〔字迹难辨，式子按残迹重构；见译注11〕},$$

即约为 $0.0091$。当该和超过 $\tfrac12-1/\gamma_1$（即 $0.43$）时我们就得到一个解。按正态分布算，这件事的概率约为 $1.3\times10^{-6}$，由此可以得出：按这个方法在前 500 000 次试验（即 $t_0<220\,000$）内找到合适值的可能性约为对半开，也就是说，有约一半的机会确立"存在某个 $x$，$2<x<\exp(220\,000)$，使 $\pi(x)>\operatorname{li}x$"。

## 7. 黎曼假设不成立（正实部零点？）的情形

为了完成整个研究，最好还能得到一些在黎曼假设被发现不成立时可以套用的结果……（字迹难辨）不在临界线上。如果只给定"在某个大矩形内存在一个零点、该矩形不与临界线相交"（例如 $\sigma>0.53$，$0<t<10^4$），那就不容易对 $\pi(x)>\operatorname{li}x$ 的那些 $x$ 值证明任何非常令人满意的结果。原因在于：给定的那个零点附近可能还有许多别的零点；它们可能近得足以造成很大的麻烦，却又不够近，因而不能给出与重零点本质上相同的效果。本研究干脆绕开所有这些困难：假定有一个离群零点 $\beta+i\gamma_1$ 位于临界线之外，并且与任何其他此类零点都相距甚远。看起来非常可能的是，最先被计算出来的临界线外零点就会满足所要求的条件。我们将再次使用引理 4，但这次取

$$f(t)=\alpha\cdot\tfrac12\bigl(1+\cos(\gamma_1 t)\bigr)\exp(-\alpha^2 t^2),\qquad \alpha^2=100,$$
〔原稿作 "4 = 100"，缺失符号按后文补为 $\alpha^2$；见译注12〕

于是我们有

$$F(u)=\exp\Bigl(-\frac{(u-\gamma_1)^2}{2\alpha^2}\Bigr)+\exp\Bigl(-\frac{(u+\gamma_1)^2}{2\alpha^2}\Bigr)+\exp\Bigl(-\frac{u^2}{2\alpha^2}\Bigr).$$
〔第三项的系数与指数细节存疑；见译注13〕

我们需要对给定 $t$ 范围内的零点个数有个上界。

**引理 15．** 〔公式严重残损，仅可辨认为关于 $\bigl(\mathrm{d}^2/\mathrm{d}z^2\bigr)\log\Gamma(z)$ 型量（或泽塔函数相应量）的一个上界不等式，其中 $z=x+iy$；见译注14〕我们先求 $\bigl(\mathrm{d}^2/\mathrm{d}z^2\bigr)\log \Gamma(z)$（$z=x+iy$）的不等式：

$$I_1=\int_{-\infty}^{\infty}(\dots)\,\bigl(y^2+u^2\bigr)^{-1}\,du.$$

那么

$$\Bigl|\Bigl(\frac{d^2}{dz^2}\Bigr)\log\Gamma(x+iy+t)-(\dots)\log\Gamma(x+iy)\Bigr|
=\Bigl|(\dots)\Bigr|\le\max(\dots)\le\frac{\pi^3}{\dots}.$$
〔整段公式残损，只能照录可辨认的骨架。〕

**引理 16．** 以 $N(t)$ 记泽塔函数正虚部小于 $t$ 的零点个数，则

$$N(t+\delta)-N(t-\delta)\le 1.6\,\frac{\log\dfrac{\delta+1}{2\pi}}{\delta-3}+1.7.$$
〔分母"$\delta-3$"等处字迹残损；见译注15〕

利用 $\zeta'/\zeta$ 的积分表示〔中间一行公式残损，涉及 $(\tfrac{s+1}{s-1})^{\dots}$、$\zeta'(s)/\zeta(s)+R(s-1)-1$ 等可辨片段〕，取 $\sigma=2$、$t>10$，我们有 $(\zeta'/\zeta)(2)<0.53$，因此

$$\frac{\sigma-\beta}{(t-\gamma)^2+(\sigma-\beta)^2}\le\log\frac{t+\delta}{2\pi}+0.53.$$

现在，若 $\beta=\tfrac12$、$|t-\gamma|>\delta$，则 $\dfrac{\sigma-\beta}{(t-\gamma)^2+(\sigma-\beta)^2}<\dfrac12$；而若 $\beta+\beta'=1$、$|t-\gamma|<\delta$，则

$$\frac{\sigma-\beta}{(t-\gamma)^2+(\sigma-\beta)^2}+\frac{\sigma-\beta'}{(t-\gamma')^2+(\sigma-\beta')^2}\le\frac{32}{t^2}.\quad\text{〔右端照录，存疑〕}$$

于是

$$N(t+\delta)-N(t-\delta)\le \frac{32\,\delta}{10^2}\log\frac{t+\delta}{2\pi}+0.53+1.7.$$
〔编者原注对式中 "$2t-1$" 的 "2" 标有疑问〕这个不等式显然对 $0<t<10$ 也成立，因为左端是……（句子其余部分缺失）。

**定理 3．** 设 $\beta_1+i\gamma_1$（$\beta_1>\tfrac12$，$\gamma_1>0$）是泽塔函数的一个零点，且对每一个其他零点 $\beta+i\gamma$，或者 $\beta=\tfrac12$，或者 $|\gamma-\gamma_1|>14$。那么存在某个 $x$，$2<x<(16\gamma_1)^a$，其中 $a=1.12/(\beta_1-\tfrac12)$，使得 $\pi(x)>\operatorname{li}x$。

$f$、$F$ 按上面的定义取定，我们有

$$|F(x+iy)|<\exp(\dots),\qquad \int_{c-i\infty}^{c+i\infty}|F(is)|\,|ds|\le(2\pi)^{\dots},$$
〔两处指数均残损〕

并且，用引理 4 的记号，可以证明 $|J|$、$|I_1|$、$|I_2|$ 各不超过 $I_{3,0}$。〔下标记法按字迹推测〕若 $\rho=\beta+i\gamma$ 且 $0<\operatorname{Re}\rho<1$，则

$$I_3=\int(\rho-\alpha)^{-1}\exp\bigl((s-\tfrac12)t_0\bigr)\exp\Bigl(-\frac{(\sigma-\alpha)^2}{2\alpha^2}\Bigr)\,ds$$

$$\le\int_0^\infty v^{-1}\exp\bigl((\beta-\tfrac12)t_0+(2\alpha^2)^{-1}\operatorname{Re}(\rho-\alpha)^2\bigr)\exp\bigl(-(ut_0)+u^2/(2\alpha^2)+\operatorname{Re}(\rho-\alpha)+\dots\bigr)\,du$$

$$\le\exp\bigl((\beta-\tfrac12)t_0+\tfrac14 t_0\operatorname{Re}(\rho-\alpha)^2\bigr)\,\gamma_1^{-(t_0+\dots)-1}\cdot\frac{1.02}{\gamma_1 t_0}\,\exp\bigl((\beta-\tfrac12)t_0+2t_0(\sigma-\alpha)^2\bigr).$$
〔此链式不等式按残迹拼合，细节不可靠；见译注17〕

我们将把靠近 $\beta_1+i\gamma_1$ 的零点与相对较远的零点分开处理。若 $\bigl||\gamma|-|\gamma_1|\bigr|>14$，则（因为无论如何都有 $|\gamma|>14$）

$$\bigl(|\gamma|-\tfrac12\bigr)^2>182+\bigl||\gamma|-|\gamma_1|\bigr|,\qquad |\gamma|^2>182+|\gamma_1|^2,$$

因此

$$\sum|I_{3,\gamma}|<1.02\,(\gamma_1 t_0)^{-1}e^{\dots/2}\Bigl(\tfrac14\exp(-2t_0\nu^2)+\exp\bigl(-t_0(\nu-\tfrac12)^2\bigr)+\exp\bigl(-t_0(\gamma+\gamma_1)^2\bigr)\Bigr)$$

$$<1.02\,(\gamma_1 t_0)^{-1}\exp(-0.405\,t_0)\bigl(\exp(-t_0\gamma)+\exp(-t_0\,|1-\gamma|)\bigr).$$

现在我们设 $t_0>20$。

〔编者注：本文其余三页为手写。〕

那么

$$\sum_\gamma \gamma^{-1}\exp\bigl(-t_0\bigl||\gamma|-|\gamma_1|\bigr|\bigr)\le\sum_\gamma \gamma^{-1}\exp\bigl(-0.1\bigl||\gamma|-|\gamma_1|\bigr|\bigr)$$

$$\le\sum_n 1.6\log\bigl(\tfrac12(3n+8)\bigr)\exp\bigl(-0.1(\tfrac32 n-\gamma_1-\dots)\bigr)\qquad\text{由引理 15}$$

$$\le 2\log\bigl(\tfrac12(\nu+8)\bigr)\bigl(1-\exp(-0.3)\bigr)^{-1}$$

$$+\ 2\sum_{\dots<n<\dots}\exp(-0.15\,|n-\nu|)\max\log\bigl(\tfrac12(3n+8)\bigr)\exp(-0.15\,(\dots))$$

$$\le 2\log\bigl(\tfrac12(\gamma_1+8)\bigr),$$

以及

$$\sum_\gamma \gamma^{-1}\exp(-t_0\nu)\le\max_\nu\Bigl(\nu\exp\bigl(-\tfrac14 t_0\nu\bigr)\Bigr)\sum_\gamma\gamma^{-2}<\dots,$$

从而

$$\sum|I_{3,\gamma}|<1.02\exp(-0.405\,t_0)\Bigl(\tfrac14 t^2+12\,t_0^{-1}\log\bigl(\tfrac12(\gamma_1+8)\bigr)\Bigr)\qquad\text{（对 }|\gamma|-|\gamma_1|>14\text{ 求和）},$$

$$\sum|I_{3,\gamma}|<2\cdot\frac{1.03}{\gamma_1 t_0}\Bigl(\sum 1\Bigr)\qquad\text{因 }\gamma_1>1100$$
（第一个和取遍 $\bigl||\gamma|-|\gamma_1|\bigr|\le14$，第二个和取遍 $|\gamma-\gamma_1|<14$），合计

$$\le\frac{33}{\gamma_1 t_0}\cdot\log\bigl(\tfrac12(\gamma_1+22)\bigr).$$

若 $\rho=\beta+i\gamma$，则

$$J_3=\operatorname{Re}\int_0^\infty \Bigl(\tfrac14(\rho+u)^{-1}\Bigr)\exp\bigl((\rho_1-\tfrac12+u)t_0+\dots-2\alpha^{-2}(\beta-\tfrac12+u)^2\bigr)\,du.$$
〔被积表达式残损，按可辨片段重构。〕

若 $\sin(\gamma_1 t_0)=1$ 且 $\gamma_1>40$，则

$$\bigl|\arg\bigl((\rho+u)^{-1}\exp((\rho-\tfrac12)t_0)\bigr)\bigr|<\frac{\pi}{4},\qquad
\cos\arg\bigl((\rho+u)^{-1}\exp((\rho-\tfrac12)t_0)\bigr)\ge\frac{1}{4.05}\ \text{（逐级放缩：} 4.05,\ 4.1,\dots\text{）},$$

于是

$$J_3\ge(4.1\,\gamma_1)^{-1}\exp\bigl((\beta_1-\tfrac12)t_0\bigr)\int_0^\infty \exp\bigl(u t_0+2(\beta_1-\tfrac12+u)^2 t_0\bigr)\,du$$

$$\ge(4.1\,\gamma_1)^{-1}\exp\bigl((\beta_1-\tfrac12)t_0\bigr)\int_0^\infty \exp\bigl(2t_0(\beta_1-\tfrac12)^2+u(t_0+2(\beta_1-\tfrac12))\bigr)\,du$$

$$=\exp\bigl(t_0(\beta_1-\tfrac12+(\beta_1-\tfrac12)^2)\bigr)\times\bigl(1-\exp(-2(t_0+2(\beta_1-\tfrac12)))\bigr)\bigl(4.1\,\gamma_1(t_0+2(\beta_1-\tfrac12))\bigr)^{-1}$$

$$\ge(4.2\,\gamma_1 t_0)^{-1}\exp\bigl(t_0(\beta_1-\tfrac12+(\beta_1-\tfrac12)^2)\bigr),\qquad\text{当 } t_0>5.$$

汇总各结果：

$$\int_0^\infty e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,dt$$

$$\ge -3\cdot10^{-8}\,t_0^{-1/2}-1.02\exp(-0.405\,t_0)(t'+12\log\dots)-\frac{33}{\gamma_1 t_0}\log\bigl(\tfrac12(\gamma_1+22)\bigr)+(4.2\,\gamma_1)^{-1}\exp(t_0 A),$$

其中

$$A=\beta_1-\tfrac12+\bigl(\beta_1-\tfrac12\bigr)^2.$$

现在我们选取 $t_0$，使得 $\sin(\gamma_1 t_0)=1$ 且

$$0<t_0-(\beta_1-\tfrac12)^{-1}\log(16\gamma_1)<\frac{2\pi}{\gamma_1}.$$

由于 $\gamma_1>1468$，条件 $t_0>5$ 自动满足，实际上 $t_0>20$。于是 $\exp\bigl(t_0(\beta_1-\tfrac12)\bigr)>16\gamma_1$，从而

$$\int_0^\infty e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)f(t-t_0)\,dt$$

$$\ge -10^{-8}-13\log\bigl(\tfrac12(\gamma_1+3)\bigr)(16\gamma_1)^{-0.81}-\log\bigl(\tfrac12(1490)+\dots\bigr)+3.8\ \ge\ 3.5,$$
〔中间数值步骤残损，数字照录；见译注17〕

$$\int_0^\infty\Bigl(e^{-t/2}\bigl(\Pi(e^t)-M(t)\bigr)t_0-0.9\exp\bigl(0.4\alpha^2(t-t_0)^2\bigr)\Bigr)\exp\bigl(-\tfrac14\alpha^2(t-t_0)^2\bigr)\bigl(1+\cos(\gamma_1(t-t_0))\bigr)\,dt$$

$$\ge 3.5-0.9\Bigl(\frac{\pi}{\dots}\Bigr)\cdot\frac{\gamma_1^2}{1468^2\,t_0}>0,$$

因为 $\dfrac{10\alpha^2}{1000}>10$〔数字照录〕。

于是存在某个 $t_1$，使

$$t_0\,\bigl(e^{-t_1/2}\bigr)\bigl(\Pi(\exp t_1)-M(t_1)\bigr)>0.9\exp\bigl(0.4\alpha^2(t_1-t_0)^2\dots\bigr)
=0.9\exp\bigl(\tfrac{(t_1-t_0)^2}{40}\cdot\dots\bigr),$$

且 $40(t_1-t_0)^2<t_0+t_0\log(3t_0)$，由此可得

$$0.8\,t_0<t_1<1.12\,t_0,\qquad e^{-t_1/2}\bigl(\Pi(\exp t_1)-M(t_1)\bigr)>0.8.$$
〔末处 ">0.8" 后原稿尚有一难以辨认的字符〕

应用引理 10：

$$\pi(\exp t_1)>\operatorname{li}\exp t_1\quad\text{或}\quad \pi\bigl(\exp(\tfrac12 t_1)\bigr)>\operatorname{li}\exp\bigl(\tfrac12 t_1\bigr),$$

也就是说，存在 $x$，$2<x<(16\gamma_1)^A$，其中 $A=1.12/(\beta_1-\tfrac12)$，使得 $\pi(x)>\operatorname{li}x$。

## 参考文献

1. A. E. INGHAM, *The distribution of prime numbers*, Cambridge Mathematical Tracts, No. 30, 1932.
2. J. E. LITTLEWOOD, Sur la distribution des nombres premiers, *Comptes Rendus* **158** (1914) 1869–1872.
3. S. SKEWES, On the difference π(x) − li x, *Proc. London Math. Soc.* 〔这是图灵论文中所给出的出处。想来即同题论文，*J. London Math. Soc.* **8** (1933) 277–283。——编者注〕
4. E. C. TITCHMARSH, The zeros of the zeta-function, *Proc. Roy. Soc. (A)* **157** (1936) 261–263.

〔书页 174。全文至此为止——手稿无签名、无日期，正文在定理 3 的证明结束后径直以参考文献收束。〕


---
## 译注
〔说明〕原稿分两部分翻译合并而成,译注编号在两部分内各自连续:第一部分(PDF 页 175–186)之注见下节,第二部分(PDF 页 187–196)之注见再下节。

### 第一部分之译注

1. Skewes 数一行原文 OCR 作 "2<x<10", where a= 10°, b= 1034"。按 Skewes 1933 年(在黎曼假设下)给出的著名界 10^{10^{10^{34}}},指数塔应读作 10^{10^a} 而 a=10^b、b=10^{34};译文据此恢复,原稿确切排布无法核验。
2. 文中 "复零点"、"零点 ρ"、"γ(=Im ρ)" 均指黎曼 ζ 函数的非平凡零点及其虚部;记号遵从 Ingham《The Distribution of Prime Numbers》(1932)。
3. Ingham 所用核 f(t)=(sin βt/t)² 之幂次为译者所补;OCR 仅存 "((sin βt)/t)"。
4. g(s) 的定义在 OCR 中出现两种互相矛盾的形状(p.155 定义式与 p.156 "亦可写作"句)。译文取与引理 3(a)(即 g(s)+log(s−1) 无奇点,可由 (1−e^{−0.1(s−1)})/(s−1) 的不定积分定义)相容的形式 g(s)=∫_{0.1}^∞ t^{−1}exp((1−s)t)dt。
5. 引理 3(b) 的不等式右端各常数(π、½、指数 ½−0.1(1−σ))均为最佳努力复原;原稿旁批注本身即标注"g ambiguous""minus sign?""log sin φ?"。
6. 引理 4 中 I₁、I₂、I₃,ρ、J 四式的完整形状在扫描件中交错错位、大量字符丢失。I₁/I₂ 中因子 log(ζ(s)/((s+1)(s+2)(s+2))) 与积分限 σ=2、σ=−Δ 系据 p.157 的移线论证文字恢复;I₃,ρ 只能给出骨架;J(留数项)完全无法辨认。请勿引用任何具体公式。
7. §4 开头 f₁(t)=sin μt/(μt) 的分母归一化系补全(OCR 仅存分子 sin μt);后文引理 5 的 F₁(z)=√(2π)(2μ)^{−1}K(z/2μ) 与此一致。"α²t₀=4Δ=400" 的等式分组亦无法确证。
8. 引理 8 结论 "Π(exp t₁)−li exp t₁>1.002 t₁^{−1}exp(t₁)" 按 OCR 直录;从量纲看右端疑有缺失因子(或应为某种相对小量),待与第二部分及 Cohen–Mayhev(1968)的转述核对。
9. 引理 10(b) 整行在扫描页上为镜像印刷,OCR 按倒置录入;"1.6" 与 "16≤x<e^{16}" 由翻转恢复,原稿批注明言 "[16 queried]"。
10. 定理 1 的题设不等式右端 "> 0.502 μ^{−1}(…)/2" 无法完整复原(对照第二部分 p.167 处数值 S>0.5026 及引理 8 阈值 1.0025,该常数链大致衔接,但精确表达式待考)。

〔格式说明〕文中方括号内以"图灵手写批注/原稿批注"标出者,是 Britton 编本转录的图灵手迹疑问记号([? …] 等),属原始文献的一部分,非译者添加。所有以〔译注N〕标出的复原均为最佳努力猜测,数学内容未作独立验证。

### 第二部分之译注

本篇为《论利特尔伍德的一个定理》下半部分（PDF 第 187–196 页，书页 165–174）。手稿后三页为手写，公式残损较多；凡不能确认之处均按上下文作最优重构并以译注标明。编者（原书编者注/图灵自批注）插入语以"编者原注"标出，与译者注区分。

1. 原扫描件中分数符号大量脱落为一个形如"↓"的字形，无法判定是 $\tfrac14$ 还是 $\tfrac12$。本篇按上下文分别复原（如 $|S^*(t)|<2\tfrac14$、和超过 $\tfrac12-1/\gamma_1=0.43$ 等），不能确定处已随文说明。
2. 引理 12 的陈述与证明中的显示式均按残迹重构：求和号下限 "$2\pi<\gamma<2\pi h$"、"var f"（总变差，系编者补记）及右端常数可以辨认，其余细节不可靠。
3. 引理 14 中 $2S$ 的定义式里，括号内首项"$\tfrac14-y\sin(yt_0)$"的负号处原稿标有"?minus"，$S_2$ 处亦然；照录并存疑。
4. （并入译注3所在段落）$|S-S_1-S_2|$ 的估计式中 $F(y)$ 与何者相减、中间因子均不可辨，只照录首尾数值。
5. $t_0$ 所在范围的乘积估计一行严重残损："1800π""960""900"、"[?672]"等数字系照录；末行 "$e^{20}<t_0<e^{60.9}$" 的 "60.9" 在另一处倒序扫描作 "609"，也可能读作 "$e^{6.09}$"，存疑。
6. 函数 $\varphi(\nu)$ 的分段定义只能给出示意性重构；原稿在该段多处标注"signs queried"（符号存疑），积分限 $1$ 至 $120$ 系按上下文补。
7. 按所列算术 $0.5080+0.003-0.0097-0.0004-0.0035\approx0.4974$，与原文印出的 $0.5026$ 不合；原稿此处本身即带问号，照录不改。
8. 定理 2 中被划掉的两个条件，其印刷形式 "$2<x<\exp\exp a<10$，$b=10$" 有缺损；按给出的两对数 $(697,303)$、$(661,287)$ 补足为 $b=10^c$（因 $\exp\exp 697\approx10^{10^{302.5}}$）。
9. §5 末段 "our chief concern has been to obtain ……" 之后至 "onward, however" 之间疑有一行脱漏，中译以"〔……〕"标示。
10. §6 中 "(symbol missing)" 为编者原注照录；"A reasonable method of progressively all values…" 一句缺谓语动词，疑漏排或字迹缺失。
11. 标准差显示式的被求和项按残迹 "$K(y)^2/(¼+y²)$" 重构，其后 "(illegible)" 为编者原注。
12. §7 标题 "(positively?)" 为作者自问语气（指零点实部为正的情形？）；$f(t)$ 定义中 "$4 = 100$" 缺失的符号按后文 $\alpha^2$ 反推补为 $\alpha^2=100$。
13. $F(u)$ 的三项指数式中，分母 "$2\alpha^2$" 三次均可辨，但第三项分子及整体系数无法确认。
14. 引理 15 的不等式本体已不可恢复，仅能辨认为对 $(\mathrm{d}^2/\mathrm{d}z^2)\log\Gamma(z)$ 型量的上界；正文随后 "$I_1=\int_{-\infty}^{\infty}(y^2+u^2)^{-1}du$" 型积分可辨。p.192 顶部的推导链同理，只照录骨架。
15. 引理 16 右端 "$1.6\log\frac{\delta+1}{2\pi}/(\delta-3)+1.7$" 中分母 "$\delta-3$" 存疑；随后取 $\sigma=2$ 的推导中 "$(32/t^2)$""$\frac{32\delta}{10^2}$" 等数值均照录。
16. 编者注"本文其余三页为手写"置于 p.193 正文之中，位置照录。
17. pp.193–195 各条不等式链（$I_3$ 上界、$J_3$ 下界、最终积分下界）残损最重，本译文按可辨认的首尾数值与结构拼合；凡照录的数字（如 $-3\cdot10^{-8}$、$13\log(\tfrac12(\gamma_1+3))(16\gamma_1)^{-0.81}$、$3.5$、$3.8$、$\frac{10\alpha^2}{1000}>10$、$0.8$ 等）不代表已核验，仅供参照原文。
