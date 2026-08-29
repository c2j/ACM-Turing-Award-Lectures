# 计算泽塔函数的一种方法

**A Method for the Calculation of the Zeta-Function**

> 作者:艾伦·图灵(A. M. Turing)
> 原载 *Proceedings of the London Mathematical Society*, Series 2, Vol. 48(1943), pp. 180–197(1939 年 3 月 7 日收到,3 月 16 日宣读)
> 译自 `papers/Pure Mathematics. 2-North Holland $1992$.pdf`(个人学习用途)

## 引言(theta 函数动机)

黎曼找到了泽塔函数的一个渐近级数,西格尔\* 将它发表,蒂奇马什† 则用它计算了该函数若干零点的大致位置。这个渐近级数很难给出令人满意的余项估计——蒂奇马什上述两篇论文的第一篇即可为证——除非 \(t\) 非常大。本文将描述一种计算方法,它与渐近公式一样,以近似函数方程为基础;而且对一切 \(s\) 值都适用。这一方法很可能在如下的 \(t\) 范围内最有价值:\(t\) 既没有小到可以径直使用欧拉–麦克劳林求和法,也没有大到值得动用渐近公式(例如 \(t < 1000\))。〔译注1〕

粗略地说,本方法就是把泽塔函数近似函数方程中的余项表成一个积分,暂时记作 \(\int_{-\infty}^{\infty} h(x)\,dx\),然后用显而易见的和 \(\sum_{k=-K}^{K} h(k)\) 去逼近它。我们发现:只要对"主级数"作某些修改,这样得到的结果精度高得惊人;当所取项数为 \(T = 2K+1\) 时,误差的数量级为 \(e^{-\pi T}\)。〔译注2〕theta 函数给出了这种现象的另一个例子。我们有恒等式

$$\sum_{n=-\infty}^{\infty} e^{-\pi n^2 x} \;=\; x^{-1/2}\sum_{n=-\infty}^{\infty} e^{-\pi n^2/x} \qquad \text{(对任意正数 } x\text{)},$$

由此〔译注3〕

$$\frac{1}{k}\sum_{n=-\infty}^{\infty} e^{-\pi n^2/k^2} \;-\; \int_{-\infty}^{\infty} e^{-\pi u^2}\,du \;=\; 2\sum_{n=1}^{\infty} e^{-\pi n^2 k^2} \qquad (k \geq 1 \text{ 时}),$$

$$\Bigl|\, \frac{1}{k}\sum_{n=-K}^{K} e^{-\pi n^2/k^2} \;-\; \int_{-\infty}^{\infty} e^{-\pi u^2}\,du \,\Bigr| \;<\; \frac{2\,e^{-\pi K^2/k^2}}{1-e^{-2\pi}} \qquad (\text{若 } K = k^2).$$〔译注4〕

上面这个不等式的证明,完全依赖于 \(e^{-\pi u^2}\) 这一函数的特殊形式。但我们也可以换一种方式来证明它。沿顶点为 \(\pm R \pm i\kappa\)〔译注5〕的矩形积分,令 \(R \to \infty\),由留数定理得〔译注6〕

$$\int_{-\infty-i\kappa}^{\infty-i\kappa} \frac{e^{-\pi u^2}}{1-e^{-2\pi iu\kappa}}\,du \;=\; \sum_{k=-\infty}^{\infty} e^{-\pi k^2\kappa^2},$$

即〔译注6〕

$$\sum_{k=-\infty}^{\infty}\; \int_{\infty-i\kappa}^{-\infty-i\kappa} e^{-\pi u^2}\,e^{-2\pi iuk}\,du \;=\; \int_{\infty-i\kappa}^{-\infty-i\kappa} e^{-\pi u^2}\,du \;+\; \int_{\infty+i\kappa}^{-\infty+i\kappa} \frac{e^{-\pi u^2}\,e^{2\pi iu\kappa}}{1-e^{2\pi iu\kappa}}\,du.$$

左端各积分的积分路径都可以换成实轴,而右端按模小于〔译注7〕

$$\frac{2}{1-e^{-2\pi\kappa}} \int_{-\infty}^{\infty} \exp\,\bigl[-\pi(u-i\kappa)^2 - 2\pi i(u-i\kappa)\kappa\bigr]\,du \;=\; \frac{2 \int_{-\infty}^{\infty} \exp(-\pi u^2-\pi\kappa^2)\,du}{1-e^{-2\pi\kappa}} \;\le\; \frac{2\,e^{-\pi\kappa^2}}{1-e^{-2\pi}} \qquad (\kappa \geq 1 \text{ 时}).$$

这种论证可以用于更一般的情形;但在移动积分路径时,我们可能遇到被积函数的奇点,它们会使结果有所改变。

我们的计算以黎曼\* 给出的泽塔函数的一个积分表示为基础。

> \* 原注:C. L. Siegel, "Über Riemanns Nachlass zur analytischen Zahlentheorie", *Quellen und Studien zur Geschichte der Mathematik*, B, 2 (1931), 45–80.
> † 原注:E. C. Titchmarsh, *Proc. Roy. Soc. A*, 151 (1935), 234–255;又 157 (1936), 261–263.〔译注8〕
> \* 原注:Siegel, loc. cit., 24.

## §1 求一类定积分的值

**〔书页 25–26|PLMS pp. 181–182〕**

设

$$G(u) \;=\; \int_{0\nearrow 1} \frac{\exp(i\pi z^2 + 2\pi i u z)}{e^{i\pi z} - e^{-i\pi z}}\,dz,$$

其中 \(0\nearrow 1\) 表示积分沿一条从 \(-\varepsilon\infty\) 到 \(\varepsilon\infty\)、与实轴交于 0 与 1 之间的直线进行,且 \(\varepsilon = e^{\pi i/4}\)。〔译注9:ε 之值在源文本层中 OCR 识作近似 "etwi"(疑为 \(e^{3\pi i/4}\) 之残迹)。然而沿 135°/315° 方向 \(\exp(i\pi z^2)\) 的实部为 \(+\pi r^2\),积分发散;收敛要求 \(\varepsilon^2 = i\),即 \(\varepsilon = e^{\pi i/4}\)(或 \(e^{-3\pi i/4}\))。又据 §5 中 J 曲线之几何("J₁ 为从 \(-\varepsilon\infty\) 出发经 \(z_0\) 到 b 的直线",而 J 自第三象限走向第一象限),亦定 \(\varepsilon = e^{\pi i/4}\)。今按 \(e^{\pi i/4}\) 译出,存疑待图像复核。〕我们把 \(-1\nearrow 0\) 上的类似积分暂记作 \(G(u)\)。于是,经变量代换 **[1]**,得到

$$G(u) = G(u-1)\,e^{-2\pi i u},$$

再由留数定理,

$$G(u) = G(u-1)\,e^{-2\pi i u} + 1.$$

〔译注10:此式源文本层识作 "G(u) = G(u)-+ 1",中段因子为 OCR 所失;据两条平行线(交实轴于 (0,1) 与 (−1,0))间含极点 z = 0、留数 \(1/(2\pi i)\) 之围道计算复原为 \(G(u-1)e^{-2\pi iu}+1\)。注意左端 \(G(u)\) 为 \(0\nearrow 1\) 上的积分,而上一式左端暂记的 \(G(u)\) 为 \(-1\nearrow 0\) 上的积分,原书行文有此交叠。〕

把恒等式

$$\frac{1}{1-e^{2\pi i z}} + \frac{1}{1-e^{-2\pi i z}} = 1$$

乘以 \(\exp(i\pi z^2 + 2\pi i u z)\),并沿 \(0\nearrow 1\) 积分,得到 **[2]**

$$G(u) = e^{-i\pi(u-\frac12)^2 + i\pi/4} + G(u-1).$$

〔译注11:此式源文本层识作 "G(u) = ee-in(u-i)+G(u--1)";"ee" 之重叠提示指数前另有一因子,经推导 \(G(u+\frac12) - G(u-\frac12) = \int_{0\nearrow 1} e^{i\pi z^2+2\pi iuz}dz = e^{-i\pi u^2 + i\pi/4}\)(高斯型积分,配方后沿 45° 线为 \(e^{i\pi/4}\int e^{-\pi t^2}dt = e^{i\pi/4}\)),令 \(u \to u-\frac12\) 即得,故复原为含 \(e^{i\pi/4}\) 之形式。〕合并这些结果,得

$$G(u) \;=\; \frac{1 - e^{-i\pi(u+\frac12)^2 + i\pi/4}}{1 - e^{-2\pi i u}}. \qquad (1.1)$$

〔译注12:(1.1) 之排式在源文本层中残损(仅存碎片 "1 … e^{-iπu²} … (1.1)");上式系由 [1] 之两条函数方程消去 \(G(u-1)\) 而得的一致形式,存疑待图像复核。又按:本节诸式之编号 [1]、[2] 为原刊右边距之步骤标号,非公式编号;编号 [3] 未见于 OCR,疑在 §2 首个积分表示处,故 §2 起编号顺延为 [4]。〕

## §2 泽塔函数的一个积分表示

**〔书页 26–27|PLMS pp. 182–183〕**

我们把 \(z^{-s}/(1-e^{-2\pi i z})\) 沿一条曲线 \(L\) 积分;\(L\) 可取为由一条从 \(i\infty\) 到 \(\frac12\) 的直线、一条从 \(\frac12\) 到 \(-\frac12\)、位于下半平面的半圆、以及一条从 \(-\frac12\) 到 \(i\infty\) 的直线组成。我们这样定义 \(z^{-s}\):它在正实轴上取通常值,且除正虚轴外连续。以 0 为圆心的圆的任何一段弧上的积分,当弧趋向无穷远时都趋于零〔译注13:此处源文本层失一行,据上下文补足大意;原句当为"以 0 为圆心、半径趋于无穷的任何一段圆弧上的积分都趋于零"〕,只要 \(\Re s > 1\);因此在这一情形有

$$\int_L \frac{z^{-s}}{1-e^{-2\pi i z}}\,dz \;=\; 2\pi i \times (\text{在除 0 以外的整数处的留数和}),$$

$$\sum_{m=1}^{\infty}\bigl(m^{-s} + e^{i\pi s} m^{-s}\bigr) \;=\; \zeta(s)\,(1 + e^{i\pi s}).$$

〔译注14:此二式在源文本层中残损("278"、"((s)(1-+eins)" 等);左边表示按留数计算复原——\(L\) 之走向(右缘下行、下半圆、左缘上行)使其包围除 0 以外之一切整数,在 \(z = m\) 处留数为 \(m^{-s}/(2\pi i)\),在 \(z = -m\) 处按上文辐角分支(\(\arg(-m) = -\pi\),故 \((-m)^{-s} = e^{i\pi s}m^{-s}\))留数为 \(e^{i\pi s}m^{-s}/(2\pi i)\)。又,原文接云"这给出 ζ(s) 在全平面上除偶整数外可能的例外之外的解析延拓",而按 \(1+e^{i\pi s}\) 计,零点落在奇整数处;此矛盾("偶"或为"奇"之误排,或原文作 \(1-e^{i\pi s}\))存疑待图像复核。〕这给出 \(\zeta(s)\) 在全平面上除(可能的)偶整数之外的解析延拓。现在,由 (1.1) **[4]**

$$\int_L \frac{e^{-i\pi u^2}\,u^{-s}}{e^{i\pi u}-e^{-i\pi u}}\,du \;=\; \int_L \frac{u^{-s}e^{2\pi i u\mu}}{(\,.\,)}\,du \quad\text{〔译注15:此式排式在源文本层中严重残损,仅存 } e^{-i\pi u^2},\ \exp(i\pi z^2+2\pi iuz)\,dz,\ u^{-s}e^{2\pi iuz},\ e^{i\pi z}-e^{-i\pi z},\ \int_L,\ \int_{0\nearrow 1} \text{ 诸碎片,无法连缀,照残记录〕}$$

**[5]** 即

$$\int_L \frac{e^{i\pi z^2} z^{s-1}}{e^{i\pi z}-e^{-i\pi z}}\,dz \;=\; -2\,(2\pi)^{s-1}\,\sin\!\bigl(\tfrac12 s\pi\bigr)\,\Gamma(1-s)\,e^{i\pi s/4} \int_{0\nearrow 1} \frac{e^{i\pi z^2} z^{s-1}}{e^{i\pi z}-e^{-i\pi z}}\,dz.$$

〔译注16:[5] 之系数亦经复原:碎片 "= -- 2(2m)-1 sin s I(1 --s) etisr" 读作 \(-2(2\pi)^{s-1}\sin(\frac12 s\pi)\Gamma(1-s)e^{i\pi s/4}\);左端积分号下 \(e^{i\pi z^2}z^{s-1}\) 清晰,存疑处为末因子积分号下 \(z\) 之幂次。〕

**[6]** 在第一个积分中,可把 \(L\) 换成 \(0\nearrow 1\) 与 \(-1\nearrow 0\) 两条线,得〔译注17:此步之公式在源文本层中残损,碎片显示为两个沿 \(0\nearrow 1\) 与 \(-1\nearrow 0\) 的积分之和;按 [1] 之变量代换,后者可化为前者,系数 \(e^{-2\pi iu}\),存疑〕**[7]**

**[8]** 此时若改变符号,曲线可换成 \(0\nearrow 1\),于是得到

$$\zeta(s) \;=\; \frac{1}{1+e^{i\pi s}}\int_L \frac{e^{-i\pi u^2}\,u^{-s}}{e^{i\pi u}-e^{-i\pi u}}\,du \;=\; -2\,(2\pi)^{s-1}\sin\!\bigl(\tfrac12 s\pi\bigr)\Gamma(1-s)\,e^{i\pi s/4}\, I(s),\qquad (2.1)$$

其中

$$I(s) \;=\; \int_{0\nearrow 1} \frac{e^{i\pi z^2}\,z^{s-1}}{e^{i\pi z}-e^{-i\pi z}}\,dz.\qquad (2.2)$$

〔译注18:(2.1)(2.2) 之排式在源文本层中部分残损;碎片清晰可见 \(\zeta(s)\)、\(-2(2\pi)^{s-1}\sin(\frac12 s\pi)\Gamma(1-s)e^{i\pi s/4}\)、两个积分(沿 L 的 \(e^{-i\pi u^2}u^{-s}/(e^{i\pi u}-e^{-i\pi u})\) 与沿 \(0\nearrow 1\) 的 \(e^{i\pi z^2}z^{s-1}/(e^{i\pi z}-e^{-i\pi z})\))及编号 (2.1);中段"\(\frac{1}{1+e^{i\pi s}}\int_L\)"为按上下文复原,存疑。(2.2) 之编号亦未见于 OCR,按 §3 引用 "(2-2)" 之文义定位。原文接云:ζ(s) 的计算遂化为计算积分 (2.2)。〕于是 \(\zeta(s)\) 的计算化为积分 (2.2) 的计算。〔译注19:此句之后源文本层有 "[9]" 步骤标号及残句 "It remains to express the left side of (2·1) ..."(尚须把 (2.1) 左端表为……),其显示式残损,当为把 \(\int_L e^{-i\pi u^2}u^{-s}/(e^{i\pi u}-e^{-i\pi u})du\) 经变量代换 \(u \to 1/u\)(或类似)化为 \(I(s)\) 同型积分之步骤;据 §3 引用 "(2-3)"、"(2-4)" 文义,知本节末尾尚有 (2.3)(2.4) 两式,均残损,照缺录,待图像复核。〕


## §3 计算方法

**〔书页 26–28|PLMS pp. 182–184〕**

设 \(\mu\) 为介于整数 \(m\) 与 \(m+1\) 之间的一个正实数。于是〔译注20〕

$$I(s) \;=\; \int_{0\nearrow 1} h(z)\,dz \;=\; \int_{m\nearrow m+1} h(z)\,dz \;-\; \sum_{r=1}^{m} r^{s-1},$$

其中 \(h(z)=e^{i\pi z^2}z^{s-1}\big/\bigl(e^{i\pi z}-e^{-i\pi z}\bigr)\),即积分 (2.2) 的被积函数;\(\displaystyle\int_{m\nearrow m+1}\) 表示沿一条过 \(m\) 与 \(m+1\) 之间、与 \(0\nearrow 1\) 相平行的直线的积分。

今设 \(k\) 为一正实数,并令

$$g(z) \;=\; \frac{h(z)}{1-\exp\bigl[2\pi i k\varepsilon(z-\mu)\bigr]}\,.$$

函数 \(g\) 在除 0 以外的各个整点、以及在点 \(\rho_\kappa=\mu+\varepsilon\kappa/k\)(\(\kappa\) 为任一整数)处有单极点;除此之外,它在闭正虚轴之外处处正则。〔译注21〕它在非零整数 \(r\) 处的留数为

$$\frac{(-1)^r\,r^{s-1}}{2\pi i\,\bigl(1-\exp[2\pi i k\varepsilon(r-\mu)]\bigr)},$$

而在 \(\rho_\kappa\) 处则为

$$\frac{\varepsilon}{2\pi k}\,h(\rho_\kappa)\,.$$

诸极点 \(\rho\) 所在的那条直线(取从左到右的方向)称为 \(P\)。

设 \(J\)、\(J'\) 是两条曲线:\(J\) 自第三象限走向第一象限,\(J'\) 自第一象限走向第三象限;\(J\) 完全位于 \(P\) 之右侧,\(J'\) 完全位于 \(P\) 之左侧且在原点之右侧。再设有正实数 \(\alpha\),使得在离原点充分远处,两曲线落在区域 \(\alpha<\arg z<\pi-\alpha\) 或 \(\pi-\alpha>\arg z>-\pi+\alpha\) 之中,且两曲线介于 \(|z|<R\) 内的弧长为 \(O(R)\)。于是容易看出〔译注22〕

$$\int_{J+J'} g(z)\,dz \;=\; 2\pi i\left(\;\sum_r \frac{(-1)^r r^{s-1}}{2\pi i\bigl(1-E(r)\bigr)}\;+\;\text{(}g\text{ 在 }J,J'\text{ 之间诸极点处的留数和}\right),$$

其中第一个和式取遍位于 \(J\) 与 \(J'\) 之间的整数 \(r\)(此处及下文记 \(E(z)=\exp[2\pi ik\varepsilon(z-\mu)]\))。今

$$\int_{J+J'} g(z)\,dz \;=\; \int_{J+J'}\bigl(g(z)-h(z)\bigr)\,dz \;+\; \int h(x)\,dx \;+\; \int h(z)\,dz,$$

〔排式残损,末两项之分限不明,照残录〕而

$$g(z)-h(z) \;=\; \frac{\exp[2\pi i k\varepsilon(z-\mu)]}{1-\exp[2\pi i k\varepsilon(z-\mu)]}\;h(z)\,.$$

若曲线 \(J\)、\(J'\) 与直线 \(P\) 的距离恒大于 \(1/(4k)\),则在这两条曲线上有〔译注23〕

$$\frac{h(z)}{1-\exp[2\pi i k\varepsilon(z-\mu)]} \;=\; h(z)\,\bigl[\,1+\operatorname{sg}(z)\cdot\theta(z)\,\bigr],\qquad |\theta(z)| < 0.27\text{(约)},$$

其中 \(\operatorname{sg}(z)\) 当 \(z\) 位于 \(P\) 之左侧时取值 \(1\)、位于 \(P\) 之右侧时取值 \(-1\)。

现在可以把我们的结果汇总成〔译注24〕

$$I(s) \;=\; \sum_{\kappa} h(\rho_\kappa)\bigl(1+\cdots\bigr) \;-\; \sum_{r=1}^{m} r^{s-1}\,\theta_r \;+\; R_0\,,\qquad (3.1)$$

〔排式中段残损,骨架如上,\(\theta_r\) 因子之确切位置未能定出〕其中 \(\theta_r\):当 \(r\) 位于 \(J'\) 之左时取值 \(1\);当 \(r\) 介于 \(J\) 与 \(J'\) 之间时取值 \(\bigl\{1-\exp[2\pi ik\varepsilon(r-\mu)]\bigr\}^{-1}\);其余情形取值 \(0\)。余项 \(R_0\) 满足〔译注25〕

$$|R_0| \;<\; 1.27\!\!\int_{J+J'} \Bigl|\,\exp\bigl[-\sqrt{2}\,\pi k\mu\,\operatorname{sg}(z)\bigr]\;\frac{e^{i\pi z^2}}{e^{i\pi z}-e^{-i\pi z}}\,\Bigr|\,|dz|\,,\qquad (3.2)$$

其中

$$\Phi(z) \;=\; i\pi z^2 \;+\; 2\pi k\varepsilon z\operatorname{sg}(z) \;-\; it\log z\,.\qquad (3.3)$$

〔译注26〕我们也可以把 \(I(s)\) 的公式写成〔译注27〕

$$I(s) \;=\; \sum_{\kappa=-\infty}^{\infty} \frac{\varepsilon}{k}\cdot \frac{e^{i\pi\rho_\kappa^{\,2}}\,\rho_\kappa^{\,s-1}}{e^{i\pi\rho_\kappa}-e^{-i\pi\rho_\kappa}} \;+\; \sum_r (\cdots)\;+\;R\,,\qquad (3.4)$$

其中 \(R=R_0+R_1\),\(\rho_\kappa=\mu+\varepsilon\kappa/k\),而

$$|R_1| \;<\; 1.27\, \sum \exp\bigl[-\sqrt{2}\,\pi k\,|r-\mu|\bigr],$$

求和取遍不介于 \(J\) 与 \(J'\) 之间的正整数。把 \(I(s)\) 表成这一形式,我们便能在数值计算中完全摆脱对曲线 \(J\)、\(J'\) 位置的任何参照,而余项并无明显的增大。在 §5 中我们将选取曲线使 \(R_1=0\)。当然,在实际计算中,因子 \(\bigl\{1-\exp[2\pi ik\varepsilon(r-\mu)]\bigr\}^{-1}\) 将〔中句残损;按 §6 之用法,当为:除少数项外径以 \(0\) 或 \(1\) 代替〕各项。〔译注28〕在估计余项时,我们假定 \(\sigma\ge 0\),但这并不是必要的。

## §4 关于余项估计的一般评述

**〔书页 28–29|PLMS pp. 185–186〕**

设

$$U \;=\; \int_{C_0} e^{w(z)}\,k(z)\,dz\,.$$

那么,对任一条在 \(e^{w(z)}k(z)\) 的正则区域内可形变到 \(C_0\) 的曲线 \(C\),有

$$|U| \;\le\; \int_C \bigl|e^{w(z)}\bigr|\,|k(z)|\,|dz|\,.\qquad (4.1)$$

今设 \(\Re w(z)\) 具有大而急剧的变化,而 \(|k(z)|\) 相对平稳。此时 (4.1) 右端积分之值主要受 \(C\) 上 \(\Re w(z)\) 最大值的影响;将这一最大值极小化,即可得到 \(|U|\) 的一个良好不等式。容易看出:若存在一条使该最大值达到极小的曲线,且最大值于某点 \(z_0\) 处取得,则 \(w'(z_0)=0\),亦即 \(z_0\) 是 \(w\) 的一个“鞍点”。设在鞍点的邻域内曲线为 \(z=z_0+le^{i\alpha}\)(\(l\) 为弧长参数),则来自鞍点邻域的对积分的贡献近似为〔译注29〕

$$|k(z_0)|\,e^{\Re w(z_0)}\,\sqrt{\frac{-2\pi}{\Re\bigl[\,w''(z_0)\,e^{2i\alpha}\bigr]}}\,,$$

〔其后尚有一行,残损不可辨,照缺录。〕

在估计 \(R_0\) 时,\(w(z)\) 既可取为 \(\Phi(z)\),也可取为 \(\Phi(z)\pm i\pi z\)(后一情形中,两个符号分别用于两条曲线 \(J\)、\(J'\))。第一种形式的分析较为简单,第二种给出更好的结果;此处只讨论较简单的一种。

我们实际使用鞍点积分思想的方式如下。设有一条以弧长 \(l\) 为参数的曲线 \(C\),\(l\) 自 \(0\) 起算。则在曲线上有〔译注30〕

$$\bigl|\exp w[z(l)]\bigr| \;<\; e^{-al^2}\,e^{\Re w[z(0)]}\,,\qquad\text{(a)}$$

从而有

$$\Bigl|\int_C e^{w(z)}\,k(z)\,dz\Bigr| \;\le\; e^{\Re w[z(0)]}\,\max_C|k|\cdot\sqrt{\pi/a}\,.\qquad\text{(b)}$$

〔两式排式均残损(碎片 "\(e^{tw[a(l)]}<e^{-tal^2}e^{\Re w[\cdots]}\)" 等);按其在 §5 中被引用之方式复原为上述形状,原刊编号未详。〕这使我们得以估计来自鞍点邻域的对积分的贡献;对于其余部分,我们可以……〔句末排式仅存 "\(dz\)"、"a" 二碎片,照缺录。〕

## §5 余项的详细估计

**〔书页 29–35|PLMS pp. 186–192〕**

对于两条曲线 \(J\)、\(J'\),我们有两个不同的鞍点 \(z_0\)、\(z_0'\),它们是 \(\Phi'(z)\) 在直线 \(P\) 两侧的零点。我们可以令〔译注31〕

$$\Phi'(z)=2\pi iz+2\pi k\varepsilon-\frac{it}{z}=\frac{2\pi i}{z}\,(z-z_0)(z-z_1)\qquad\text{（在 }P\text{ 之左）},$$

以及

$$\Phi'(z)=2\pi iz-2\pi k\varepsilon-\frac{it}{z}=\frac{2\pi i}{z}\,(z-z_0')(z-z_1')\qquad\text{（在 }P\text{ 之右）};$$

点 \(z_0\)、\(z_0'\) 位于右半平面,\(z_1\)、\(z_1'\) 位于左半平面。若再令 \(\tau=t/2\pi\),\(\rho=k\tau^{-1/2}\),\(\xi=z\tau^{-1/2}\),则可将上二式写成

$$(\xi-\xi_0)(\xi-\xi_1)=\xi^2-i\varepsilon\rho\xi-1\,,\qquad (\xi-\xi_0')(\xi-\xi_1')=\xi^2+i\varepsilon\rho\xi-1\,.$$

诸根满足〔译注32〕

$$\eta_0+\eta_0'=0\,,\quad \eta_1+\eta_1'=0\,,\quad \arg\xi_0+\arg\xi_0'=0\,,\quad \pm\pi>\arg\xi_0'>0\,.$$

四根共处于一条与 \(\rho\) 无关的三次曲线上。我们还需要根的若干其他性质,将在用到时随时提出;它们大多是一些不等式,可以用直截了当然而繁琐的方法加以证明。

\(\rho\) 的若干函数的性态示于图 1。

> **图 1**:曲线图(横轴标至约 800,纵轴见 "0.5""1·5" 等刻度;可辨轴标注有 \(\arg\xi_0'\)、"\(2\theta_0\)"、"sin" 等碎片)。〔译注33〕

我们选取积分曲线 \(J\)、\(J'\) 如下。\(J\) 由三个直线段 \(J_1\)、\(J_2\)、\(J_3\) 组成:\(J_1\) 是从 \(-\varepsilon\infty\) 出发、经过 \(z_0\) 而到 \(b\) 的直线,其中 \(b=z_0-y_0(1+i)\);\(J_2\) 连接 \(b\) 与 \(b+\beta\),其中 \(\beta\) 为正实数;\(J_3\) 连接 \(b+\beta\) 与 \(\varepsilon\infty\),并经过一个半奇整数点。当 \(\beta\to\infty\) 时,\(J_3\) 对余项的贡献趋于零〔译注34〕;因此略去 \(J_3\),而设 \(J\) 由 \(J_1\) 连同取作延伸至无穷的 \(J_2\) 组成;此时 \(J\) 的右侧就没有对 \(R_1\) 有贡献的极点了。

> **图 2**:\(J\)、\(J'\) 两曲线构造之示意图。〔译注35〕

曲线 \(J'\) 由四个部分 \(J_1'\)、\(J_2'\)、\(J_3'\)、\(J_4'\) 组成,其中 \(J_2'\) 又分为 \(J_5'\) 与 \(J_6'\)。令 \(b'=z_0'-y_0'(1+i)\)。于是 \(J_1'\) 是从 \(\varepsilon\infty\) 出发、经过 \(z_0'\) 而到 \(b'\) 的直线;\(J_2'\) 是从 \(b'\) 到 \(c\) 的直线,其中 \(c/b'\) 为实数且 \(0<c/b'<1\),\(|c|=\min(\tau^{1/2},|z_1'|)\)〔译注36〕。曲线 \(J_3'\) 是位于半平面 \(\Im z>0\) 内的一段圆弧,连接 \(c\) 与 \(-ic\)。将 \(J_2'\) 与 \(J_3'\) 关于直线 \(\Re z=0\) 作反射并反转方向,即得 \(J_4'\)。我们把 \(J_2'\) 分成 \(J_5'\) 与 \(J_6'\),其中 \(J_5'\) 是满足 \(y>y_0'\) 的部分。这两段都有正的长度,\(J_5'\) 的长度至少为 \(|z_1'|\)。

在 \(J_1\) 与 \(J_4'\) 上我们有 \(|z|>\tau^{1/2}\)〔残〕及〔译注37〕

$$\bigl|e^{i\pi z}-e^{-i\pi z}\bigr|^{-1}\le \operatorname{cosech}|\pi y_0'|\,.$$

因此 \(J_1\) 对 \(R_0\) 的贡献至多为

$$\int_{J_1} (1.27)\,(2\pi k)^{-1}\exp\bigl[\sqrt{2}\,\pi k\mu\bigr]\operatorname{cosech}|\pi y_0'\,|\;\bigl|e^{\Phi(z)}\bigr|\,|dz|\,.\qquad (5.1)$$

〔译注38〕在 \(J_2\) 上,利用简单的事实:\(J_2\) 到 0 的距离大于 \(\sqrt{2}\,|z_1|\)〔残〕,且 \(\arg\xi_1<-2/\pi\)〔残〕;又有

$$\Bigl|\frac{2\pi(z-z_1)(z-z_0)}{z}\Bigr|>\pi|z-z_0|\,,$$

于是

$$\Re\Bigl[\frac{-2\pi iz}{(z-z_1)(z-z_0)}\Bigr]\,dl\;\cdots\;<\;\cdots$$

只要 \(l\) 在趋近 \(z_0\) 时总是减小。然后应用 §4 之 (a),得

$$\int_{J_2}\bigl|e^{\Phi(z)}\bigr|\,|dz| \;<\; \sqrt{\pi/(6\cdots)}\;e^{\Re\Phi(c)}\cdots\qquad (5.2)$$

又

$$\Re\Phi(b)<\Re\Phi(z_0)-\pi y_0^{\,2}\,.\qquad (5.3)$$

在 \(J_2\) 上 \(dz/dl=i\cdots\),而〔译注39〕

$$\frac{e^{\Phi(z)}}{\Phi'(z)}\;\cdots\;<\;\pi(\sqrt{2}\,\rho-2)\,y_0^{\,2}\;\cdots\;=\;-2\pi y_0^{\,2}\cdots\qquad (5.4)$$

但 \(\tau<\xi_0^{\,2}\),因为对一切 \(\rho\) 均有 \(\xi_0>1\);因此……〔中段残损〕于是由 §4 之 (b)、(5.3) 与 (5.4) 得

$$\int_{J_2}\bigl|e^{\Phi(z)}\bigr|\,|dz| \;<\; (2\pi y_0)^{-1}\exp\bigl[\Re\Phi(z_0)-\pi y_0^{\,2}\bigr]\,.\qquad (5.5)$$

现在转到 \(J'\)。若 \(z\) 是 \(J_3'+J_4'\) 上的一点,则 \(-iz\) 是 \(J_2'\) 上的对应点,且有〔译注40〕

$$\Re\Phi(-iz)=\Re\bigl[i\pi(-iz)^2+2k\varepsilon(-iz)-it\log z-it\log(-iz/z)\bigr]\,,$$

即

$$\Re\Phi(-iz)\le\Re\Phi(z)-\sigma t\,\pi\cdots\qquad\text{〔残〕}$$

又有 \(|-iz|=|z|\),且

$$|\operatorname{cosec}(-i\pi z)|<|\operatorname{cosec}\pi z|\,,$$

后者可以利用 sine 函数的无穷乘积表示、并注意 \(|\arg z|<\pi\) 来证明。从而

$$\Bigl|\int_{J_3'+J_4'} \frac{e^{i\pi z^2}z^{s-1}}{e^{i\pi z}-e^{-i\pi z}}\,dz\Bigr| < (1+e^{-\pi t})\int_{J_5'+J_6'} \Bigl|\frac{e^{i\pi z^2}z^{s-1}}{e^{i\pi z}-e^{-i\pi z}}\Bigr|\,|dz|\,.\qquad (5.6)$$

〔式右端曲线标号系按文义复原。〕在 \(J_1'\) 上,若 \(l\) 在从两侧任一侧趋近 \(z_0'\) 时总是减小,则〔同前法之估计式,残损〕;应用 §4 之 (a),得〔译注41〕

$$\int_{J_1'}\bigl|e^{\Phi(z)}\bigr|\,|dz| \;<\; (2\rho)^{-1}\cdots\,e^{\Re\Phi(z_0')}\cdots\qquad (5.7)$$

又

$$\Re\Phi(b')<\Re\Phi(z_0')-\pi y_0'^{\,2}\sin\gamma\,.\qquad (5.8)$$

在 \(J_6'\) 上〔译注42〕

$$\Bigl|\frac{-2\pi i}{(b'-z_0')(b'-z_1')}\Bigr|\;\cdots\;\qquad (5.9)$$

但 \(\arg(z_1'b')=-\pi\),且

$$0>\arg(b'-z_1')>\arg(-z_1')=\gamma-\tfrac14\pi\,,$$

于是

$$\pi\cdots<\arg\bigl[(b'-z_0')(b'-z_1')\bigr]<\pi\cdots$$

又有

$$\bigl|-2\pi i(b'-z_0')(b'-z_1')/b'\bigr|>\sqrt{2}\,\pi y_0'\,,$$

于是

$$\Re\Bigl[\frac{2\pi i}{(b'-z_0')(b'-z_1')}\Bigr]\;<\;-\sqrt{2}\,\pi y_0'\sin\gamma\,,\qquad (5.10)$$

应用 §4 之 (b),并用 (5.9)、(5.10) 与 (5.8),得

$$\int_{J_6'}\bigl|e^{\Phi(z)}\bigr|\,|dz| < \bigl(\sqrt{2}\,\pi y_0'\sin\gamma\bigr)^{-1}\exp\bigl[\Re\Phi(z_0')-\pi y_0'^{\,2}\sin\gamma\bigr]\,.\qquad (5.11)$$

又〔译注43〕

$$\Re\Phi(c')<\Re\Phi(z_0')-\pi y_0'^{\,2}\sin\gamma-\sqrt{2}\,\pi y_0'\,|z_1'|\sin\gamma\,.\qquad (5.12)$$

在 \(J_5'\) 上,

$$\Re\Bigl[\frac{-2\pi i}{(z-z_0')(z-z_1')}\Bigr]\cdot\frac{2\rho\cdots}{z}\;\cdots\;<\;2\sin^{-1}\cdots<\tfrac{\pi}{2}<\pi-\cdots$$

于是在 \(J_4'\) 与 \(J_5'\) 上皆有

$$\Re\Bigl[\frac{2\pi i}{(z-z_0')(z-z_1')}\Bigr]\cdot\frac{dz}{z}\;<\;-\sqrt{2}\,\pi y_0'\sin\gamma\,.$$

结合 (5.12) 即得

$$\int_{J_4'+J_5'}\bigl|e^{\Phi(z)}\bigr|\,|dz| < \bigl(\sqrt{2}\,\pi y_0'\sin\gamma\bigr)^{-1}\exp\bigl[\Re\Phi(z_0')-\pi y_0'^{\,2}\sin\gamma-\sqrt{2}\,\pi y_0'\,|z_1'|\sin\gamma\bigr]\,.\qquad (5.13)$$

在 \(J_5'\) 上我们有〔译注44〕

$$\Bigl|\frac{1}{e^{i\pi z}-e^{-i\pi z}}\Bigr|<\tfrac12\operatorname{cosech}|\pi y_0'|\,;\qquad (5.15)$$

在 \(J_6'\) 上

$$\Bigl|\frac{1}{e^{i\pi z}-e^{-i\pi z}}\Bigr|<\tfrac12\operatorname{cosech}|\pi y|\,;\qquad (5.16)$$

而在 \(J_3'\)、\(J_4'\) 上

$$\Bigl|\frac{1}{e^{i\pi z}-e^{-i\pi z}}\Bigr|\le\bigl[\min(\tau^{1/2},\tau|\xi_0'|)\bigr]^{-1}\operatorname{cosec}\arg\xi_0'\,.\qquad (5.17)$$

〔原刊编号无 (5.14),OCR 亦未见其式,当系编号跳越或该式排版残失。〕

现在可以把诸结果汇总起来,给出一个关于 \(|R|\) 的不等式。我们使用 (5.1)、(5.2)、(5.5)、(5.6)、(5.7)、(5.11)、(5.13)、(5.15)、(5.16) 与 (5.17),并利用关系 \(z_0z_1=z_0'z_1'=-\tau\) 把指数 \(\Re\Phi(z_0)+\sqrt{2}\,\pi k\mu\) 与 \(\Re\Phi(z_0')-\sqrt{2}\,\pi k\mu\) 写得更显豁〔译注45〕:

$$
\begin{aligned}
|R|=|R_0| \;&<\; 0.635\,(\Re\varepsilon)^{-1}\,\operatorname{cosech}|\pi y_0|\,\bigl\{2.45+\cdots\bigr\}\\
&\quad\times\exp\bigl[-\pi k\Re\varepsilon(z_0-2\mu)+2\pi\tau\arg z_0\bigr]\\
&\quad+0.635\,(1+e^{-\pi t})\,|z_1'|\,\Bigl\{(\sin\gamma)^{-1}\cdot 2\operatorname{cosech}|\pi y_0'|+(\sqrt{2}\,\pi y_0'\sin\gamma)^{-1}\exp[-\pi y_0'^{\,2}\sin\gamma]\\
&\qquad\times 3\operatorname{cosech}|\pi y_0'|+|z_1'|\,[\min(\cdots)]^{-1}\operatorname{cosec}\arg\xi_0'\times\exp[-\sqrt{2}\,\pi y_0'\sin\gamma/(2\xi_0')\,]\Bigr\}\\
&\quad\times\exp\bigl[-\pi\Re\varepsilon(2\mu-z_0')+2\pi\tau\arg z_0'\bigr].
\end{aligned}
\qquad (5.18)
$$

此处宜把上述不等式右端出现的各个量用 \(s\)、\(k\) 复述一遍〔译注46〕:

$$\sigma=\Re s\,,\quad t=\Im s\,,\quad \tau=t/2\pi\,,\quad \rho=k\tau^{-1/2}\,,\quad \varepsilon=e^{i\pi/4}\,.$$

复数 \(\xi_0'\)、\(\xi_1'\)、\(\xi_1\)、\(\xi_0\) 是方程

$$(\xi^2-1)^2=-\varepsilon\rho^2\xi^2$$

的根,分别位于第一、二、三、四象限;而〔译注46 续〕

$$z_0'=\tau^{1/2}\xi_0'\,,\qquad z_0=\tau^{1/2}\xi_0=x_0+iy_0\,,\qquad y_0=\tfrac{\pi}{4}-\arg z_1\,,$$

其中 \(\xi\)、\(\eta\)、\(x\)、\(y\) 均为实数。(5.18) 所给的 \(R\) 的估计颇为繁复;当 \(\rho\) 不很大时,它可以大大简化。我对 \(\rho\le\frac14\) 的情形给出一个估计;此时我们有〔译注47〕

$$\sqrt{2}\,\xi_1'>1\,,\qquad \Re\bigl(1-z_0'^{\,2}\bigr)>0.45\rho\,,\qquad \sin\gamma>0.55\,,$$

$$\xi_1'>\rho/2\sqrt{2}\,,\qquad \eta_0'>0.29\rho\,,\qquad |z_1'|>0.81\,.\qquad (5.19)$$

结果是:当 \(\rho\le\frac14\)、\(t\ge 250\)〔数字残,末位存疑〕时,

$$
|R|=|R_0|<0.76\cdot 2^{\cdots}\,\operatorname{cosech}\,0.78\,(k/\sqrt{2})\times\bigl[\text{含 }e^{-A}\text{ 之项(残)}\bigr]
\times\Bigl[1.91\cdot 2^{\cdots}\operatorname{cosech}\,0.64\,(k/\sqrt{2})+1.00\,(k/\sqrt{2})^{-1}\exp\bigl(-0.14\,(k/\sqrt{2})^2\bigr)\times 1.74\cdot 3^{\cdots}\operatorname{cosech}\,0.42\,(k/\sqrt{2})+1.7\,(1.62)^{-\cdots}+\cdots\Bigr],
$$

其中

$$A=\pi\Re\varepsilon(z_0-2\mu)+2\pi\tau\arg z_0'\,,\qquad B=\pi\Re\varepsilon(2\mu-z_0')-2\pi\tau\arg z_0'\,.$$

在 \(\rho\ge\frac14\) 的情形,利用下面这组对一切正 \(\rho\) 都成立的不等式,可使由 (5.18) 所作的余项估计变得容易些〔译注48〕:

$$\Box\;>\;1-\frac{1}{0.65\rho}\,,\qquad \Box\;>\;1-\frac{1}{\rho^2+2}\,.$$

## §6 参数的选取与具有限级数时的余项

**〔书页 36–38|PLMS pp. 193–195〕**

由 (5.18) 所给的余项 \(R\) 是两项之和,其二者的主因子分别为 \(e^{-A}\) 与 \(e^{-B}\)。参数 \(\mu\) 的最有利选择,大约就是使这两个因子相等的那种选择。称该值为 \(\mu_0\),则有〔译注49〕

$$\mu_0=\frac{2\sqrt{2}}{\log\{\cdots\}+\cdots}\qquad\text{〔排式大部残损,仅此可辨〕}$$

当 \(\rho\) 趋于无穷时,\(\mu_0\sim\tau\rho/2\sqrt{2}\);而当 \(\rho\) 趋于 \(0\) 时,\(\mu_0\sim\tau^{1/2}\)。〔两处渐近式均残损,按文义复原,存疑〕又有〔残式:\(\{1/(¼+\cdots)+\arg\cdots\}\) 之类碎片〕:当 \(\rho\to 0\) 时,因子〔残式〕趋于 \(1\);当 \(\rho\to\infty\) 时,该因子趋于 \(\frac12\)(约);对一切正的 \(\rho\),它都大于 \(\frac12\)(约);因此〔译注50〕

$$\Re\varepsilon(\mu_0-2z_0)>K\,.$$

又〔残式〕,而有

$$\Re\varepsilon(2\mu_0-z_0')>K\,.$$

〔上二式中常数 \(K\) 之义未能辨明,或系 \(k\) 或某一显式常数之误排。〕若取 \(\mu=\mu_0\pm\delta\)(\(\delta>0\)),则指数因子 \(e^{-A}\)、\(e^{-B}\) 中较大者为

$$\exp[-\pi k^2+\sqrt{2}\,\pi k\delta\,].$$

可选的 \(\mu\) 值所受的限制只有一条:曲线 \(J\)、\(J'\) 必须与 \(P\) 相距至少 \(1/(4k)\)。若 \(k\ge\sqrt{2}\),我们便可在区间 \((\mu_0,\ \mu_0+\delta)\) 内选取 \(\mu\);若 \(k\ge 2\),则可在区间 \((\mu_0-\delta,\ \mu_0+\delta)\) 内选取〔区间端点符号残损,以 \(\delta\) 试读;译注51〕。不过,对这样小的 \(k\) 值,把 \(\mu\) 选得相当接近 \(\mu_0\) 大概仍是最好的做法。至于 \(k\) 比 \(2\) 更小的情形则无须考虑,因为(下文可见)即便只从级数 \(\sum h(\rho_\kappa)\) 中取一项,取这么小的 \(k\) 值也无好处可言。

当 \(\rho\) 小时,\(\mu_0\) 接近 \(\tau^{1/2}\);因此最简单的做法大概是径直选一个接近 \(\tau^{1/2}\) 的 \(\mu\) 值而不去实际计算 \(\mu_0\)。这时下面这个不等式应当有用〔译注52〕:

$$\text{〔一个含 }0<\delta<1\text{ 的初等不等式,排式全残,照缺录〕}$$

对大的 \(k\) 值(例如 \(k>3\)),把 \(\mu\) 取为整数或半奇整数是上策。当 \(\mu\) 为整数时,函数 \(g\) 在 \(\mu\) 处有一个二阶极点;此时我们须以下式在 0 处的留数

$$2\pi i\,(\varepsilon/k)\,(z+\mu)^{s-1}\exp[i\pi(z+\mu)^2]\;\big/\;\bigl(1-e^{-2\pi iz}\bigr)\bigl(1-e^{-2\pi ik\varepsilon(z-\mu)}\bigr)$$

来代替

$$\frac{(\varepsilon/k)\,h(\mu)}{1-\exp[2\pi ik\varepsilon(\mu-\mu)]}$$

各项,而这一留数等于〔其值之排式整行失落于 OCR,照缺录〕。〔译注53〕

在实际应用中,当然只从级数 \(\sum(\varepsilon/k)h(\rho_\kappa)\) 中取有限多项。因此我们需要估计由此产生的误差。设我们先行确定结果中所容许的最大总误差为 \(\eta\)(符号残,以 \(\eta\) 试读),则可如下进行:先选 \(k\) 使 \(|R|<\eta\),再从级数中取足够多的项,使这第二个误差来源不超过 \(\frac12\eta\)。现在来估计这第二个余项。为此我们证明下面的〔译注54〕

**引理。** 函数 \(|e^{i\pi z^2}z^{s-1}|\) 在直线 \(P\) 上只有一个最大值。

证:令 \(\zeta=\mu+\Box\,(1+\theta)(1+i)\)〔系数残〕,\(a=t/(2\pi\mu)\);则 \(\theta\) 为实数,且有〔排式残损:\(|e^{i\pi\zeta^2}\zeta^{s-1}|\le\cdots\) 型不等式〕。把右端缩记为 \(H(\theta)\)。则〔译注55〕

$$H'(\theta)=\frac{D(\theta)}{(1+\theta)^2+\theta^3}\quad\text{〔分子 }D(\theta)\text{ 之式残〕}$$

今〔式残:形如 \(\bigl((1+\theta)^2+\theta^2\bigr)(1+2\theta)^{-a}\)〕不可能对多于一个 \(\theta\) 值为零;而它显然至少对一个值为零。于是 \(H(\theta)\) 只有一个驻点,而易见其为最大值。引理得证。若 \(a<1\),给出最大值的 \(\theta\) 满足〔不等式残,似为 \(1>\theta>a-1\) 一类〕。

令 \(u_K=\sum_{\kappa=-K}^{K}|h(\rho_\kappa)|\);则当 \(\sigma\ge 0\) 时,有〔译注56〕

$$u_K\;\le\;\frac{(\mu/\sqrt{2})^{\sigma-1}}{\pi k}\;M\cdot\Bigl(\exp\text{-型求和},\ \kappa=-K\ldots K\Bigr)\quad\text{〔排式残损,骨架试读;}M\text{ 为式中最大值因子〕}$$

如果我们假定 \(\sum(\rho_\kappa^{\sigma-1})\) 小于 \(|e^{i\pi z^2}z^{s-1}|\) 取最大值处之相应参量值〔原文字母残,所指未详〕,且 \(k>K+1\),则〔式残〕,因而

$$\sum_{\text{尾部}}\;\le\;\exp\bigl[-(K+1)^2/K\sqrt{2}\cdots\bigr]\times(\cdots)(\cdots)\quad\text{〔残〕}$$

同样,若(当 \(K'\ge 0\) 且 \(a\le 1\) 时情形总是如此)\(\sum(\rho_{\kappa'}{}^{\sigma+1})\) 大于最大值出现处之相应值,则〔式残〕,于是〔译注57〕

$$|R^*|\;\le\;\frac{2\,|h(\rho_{-K-1})|+|h(\rho_{K'+1})|}{\bigl(1-e^{-\cdots}\bigr)\bigl(1-e^{-\cdots}\bigr)}\,,\qquad K^*=\min(K,K')$$

〔分母中的衰减比按几何级数尾项之常例复原,具体形式残损。〕

当 \(k\) 与 \(\tau^{1/2}\) 相比为小时,对给定的精度我们可以容易地得到所需项数的粗略估计。因为此时 \(K\)、\(K'\) 满足 \(\rho_{-K}/\mu-1\) 与 \(\rho_{K'}/\mu-1\) 都很小,而 \(u_K\) 近似为 \(\exp[-2\pi(K+1)^2/k^2]\)。若余项 \(R\) 与 \(R^*\) 同数量级,则近似地有〔译注58〕

$$2\pi(K+1)^2/k^2=\pi k^2\cdots\,,\qquad\text{即}\quad K+1\approx\tfrac12 k^2\ \text{〔残,试读〕}.$$

我们所取的项数 \(T=2K+1\),即近似为 \(k^2\),而总误差的数量级为 \(e^{-\pi T}\)。若要把这一陈述表成确切的形式,须这样说:若 \(\mu\) 与 \(k\) 作为 \(t\)、\(\eta\) 的函数适当选取,\(\sigma\) 位于区间 \(0\le\sigma\le 1\) 内,且 \(\eta\to 0\)、\(t\to\infty\) 的方式使 \(k^{-1}\)、\(k\tau^{-1/2}\) 亦趋于 \(0\),则误差不超过 \(\eta\),而且 \(T^{-1}\log\eta^{-1}\) 趋于 \(\pi\);对任何大于 \(\pi\) 的数此结论不成立。

当 \(k\tau^{-1/2}\) 为 1 的数量级时,我们得不到如此简单的所需项数估计;但在极限情形 \(k\tau^{-1/2}\to\infty\) 下可以得到一个估计。此时可以略去 \(u_K\) 中除 \(|e^{i\pi\rho_\kappa^{\,2}}\rho_\kappa^{\,s-1}/k|\) 之外的一切因子。令 \(\mu+\varepsilon\nu=\rho_\kappa\)(试读),则近似地有〔译注59〕

$$\bigl|e^{i\pi(\mu+\varepsilon\nu)^2}\bigr|=e^{-\pi\sqrt{2}\,\mu\nu-\pi\nu^2}\cdots$$

只要 \(R\) 与 \(R^*\) 同数量级;亦即

$$\sqrt{2}\,\pi\mu\nu+\pi\nu^2=\pi K^2\,.$$

但对大的 \(\mu\) 值,近似地有 \(\mu=k/2\sqrt{2}\)〔残,"\(x\)" 当为 \(k\) 之误识〕;于是近似地得到

$$2\nu^2-\nu\tau\sqrt{2}\cdots-k^2\cdots=0\quad\text{〔排式残损,照残录〕}$$

这一方程的两个根近似为 \((\rho_{-K}-\mu)\) 与 \((\rho_K-\mu)\),而误差的数量级为 \(e^{-\pi T}\)。

有可能通过把 \(\mu\) 取得不同于 \(\mu_0\) 来改进这一点:因为若把 \(\mu\) 取得更接近 \(\tau^{1/2}\),则对给定的 \(T\) 而言余项 \(R^*\) 会变小。这样的改进必然十分有限;笔者未曾考察沿此路线是否真能获得改进〔中句残失一行,按文义补足〕。〔译注60〕

在 \(T=3\) 的情形,可取 \(k=1.6/\sqrt{2}\)(或 \(1.6\sqrt{2}\),数字排式存疑);于是,若 \(\sigma=\frac12\)、\(\mu=\tau^{1/2}\)、\(t>350\),并且把因子 \((1-\exp[2\pi i\kappa\varepsilon(r-\mu)])^{-1}\) 除主级数中的两项外一律代之以 \(0\) 或 \(1\),则来自一切来源的误差不超过 \(0.0044\,\tau^{-1/2}\)〔指数残,试读〕。〔译注61〕

## §7 一个类似的方法

**〔书页 39–40|PLMS pp. 196–197〕**

泽塔函数还有一个可供我们计算之基的、而且更为人熟知的积分表示,即〔译注62〕

$$\zeta(s)=\tfrac12+\sum_{n=1}^{m} n^{-s}\;+\;2(2\pi)^{s-1}\sin\tfrac12\pi s\;\Gamma(1-s)\int_{\Omega_m}\frac{e^{2\pi imz}\,z^{-s}}{1-e^{-2\pi iz}}\,dz$$

〔排式大部残损:可辨碎片有 "\(\frac12+\)"、"\(2(2\pi)^{s-1}\sin\frac12\pi s\,\Gamma(1-s)\)"、"\(e^{2\pi imz}z^{-s}dz\)" 及三个 \(\Sigma_{n=1}\) 型下限;按 Hermite 型表示之常例连缀如上,结构存疑待图像复核。〕

此处 \(\Omega_m\) 是一条自第一象限无穷远处来的曲线,在 \(m\) 与 \(m+1\) 之间穿过实轴一次,又在 \(-m\) 与 \(-m-1\) 之间穿过一次,然后走向第二象限的无穷远处;\(z^{-s}\) 按 §2 的方式定义。若取 \(m=m'=\lfloor\tau\rfloor\),并令 \(\Omega_m\) 在正实轴附近的部分是一条在 \(\mu\) 处以 \(\frac{\pi}{4}\) 角穿过实轴的直线〔原文作 "negatively directed real axis"(负向实轴),与 \(\mu>0\) 不合,疑为排版之误或指曲线走向,照录待核〕,则当 \(t\) 很大时,对积分的唯一可观贡献来自正实轴的邻域。

我们可以用与前文相同的方式逼近这一积分,所得 \(\zeta(s)\) 的近似值为〔译注63〕

$$
\sum_{n=1}^{?} n^{-s}\Bigl\{1-\bigl(1+e^{i\pi s}\bigr)^{-1}\bigl(1-\exp[-2\pi ik\varepsilon(n-\mu)]\bigr)^{-1}\Bigr\}
+2(2\pi)^{s-1}\sin\tfrac12\pi s\,\Gamma(1-s)\sum_{n=1}^{\infty}(\cdots)
$$

$$
+\sum_{\kappa=-K}^{K}\frac{\bigl(\mu+\varepsilon\kappa/k\bigr)^{-s}\exp\bigl[2\pi i m(\mu+\varepsilon\kappa/k)\bigr]}{k\,(1+\cdots)}
+\int\bigl[(z/\cdots)+\cdots\bigr]^{-s}dx\cdots
$$

〔上二行系按碎片连缀之骨架:首行诸因子清晰;\(\Sigma_{n=1}^{\infty}\) 后之中段、第三行之分母 \(k(1+\cdots)\)("k(1+er8)" 碎片)及末项积分均残损。〕

整数 \(K\) 不可取得太大;通常取 \(K<k\tau^{1/2}\)〔符号残,试读〕即已足够小。此方法的优点是:对不在临界线上的点,只须计算两个实积分而非四个。这对计算不在临界线上的零点可能有其价值。不过,在其原有形式下此法仅适用于大的 \(t\) 值〔残句,按文义补足〕;然而,沿一条抛物线积分即可消除这一限制,例如抛物线

$$x^2=2\mu y+\mu^2\qquad([\tau]\le\mu\le[\tau]+1).$$

保形映射 \(u^2=z\) 把这条抛物线变成一条直线,于是

$$\int_{\Omega_m}\frac{e^{2\pi imz}\,z^{-s}}{1-e^{-2\pi iz}}\,dz=\int\frac{e^{2\pi imu^2}\,u^{-2s+1}}{1-e^{-2\pi iu^2}}\,du\,.$$

积分直线在虚轴上介于 \(-im^{1/2}\) 与 \(-i(m+1)^{1/2}\) 之间穿过〔幂指数残,试读〕。

**King's College, Cambridge.**(剑桥,国王学院)〔全文完〕

---

> **整理附记**:本篇译文(引言及 §1–§7)至此完整。原刊为无文本层扫描件,§3 以下公式排式多有 OCR 残损;凡属复原之处均已随文以〔译注N〕标明存疑,完全无法辨识者照缺录或照残录。图 1(函数性态曲线图)与图 2($J$、$J'$ 曲线构造图)细节无法辨读,仅记其存在与大貌,待图像复核后修订。
