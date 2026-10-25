# 三遍论文阅读技能

[English](README.md) | **简体中文**

面向科研新手的论文阅读技能，依据 **S. Keshav 于2007年发表的《How to Read a Paper》**，把“三遍阅读法”整理成可执行、可检查的工作流程：先建立全貌，再理解证据，最后重建方法、审视假设。

仓库提供可复用的skill、阅读笔记模板、两篇实际试读报告，以及对应的数值复算和自检记录。

## 从这里开始

- **使用技能：**[SKILL.md](skills/three-pass-paper-reading/SKILL.md)
- **看实际成果：**[PCB缺陷检测精读](examples/pcb-defect-detection.zh-CN.md) · [农业目标检测精读](examples/agricultural-detection.zh-CN.md)
- **看执行与自检：**[完整中文自检报告](examples/self-check.zh-CN.md) · [发布检查](validation/SELF-CHECK.md)
- **自己做阅读笔记：**[阅读模板](templates/reading-notes.md)
- **检查计算：**[36项数值复算](examples/numeric-checks.json) · [复算脚本](examples/numeric_checks.py)

## 三遍分别做什么

| 阶段 | 阅读动作 | 应该留下的成果 |
|---|---|---|
| **第一遍：建立全貌** | 读题名、摘要、引言、各级标题、结论，浏览参考文献。 | 回答五个C，决定停止、稍后再读或继续。 |
| **第二遍：理解内容与证据** | 理解论证，检查图表，把研究主张与实验/分析对应起来，标记需要补读的背景。 | 能用具体证据向别人解释这篇论文。 |
| **第三遍：重建与质疑** | 尝试重建方法或推理，再与原文核对；复算关键数字、审查假设。 | 方法重建、修正记录、优缺点与最值得补做的验证。 |

五个C分别是：**Category（类型）、Context（背景）、Correctness（假设是否初步合理）、Contributions（贡献）、Clarity（表达是否清楚）**。第一遍的Correctness是初判，后续仍需检查证据。

原方法强调的是“**最多三遍**”。和研究关系较远的论文可以第一遍后停止；对自己研究重要的论文，再投入更深的阅读。

## 在Codex中使用

先让内置技能安装器安装仓库中的技能目录：

```text
$skill-installer 安装这个技能：
https://github.com/jiangyuhan0318-July/three-pass-paper-reading/tree/main/skills/three-pass-paper-reading
```

下一轮对话即可这样使用：

```text
$three-pass-paper-reading 请按三遍法阅读附件论文。
用中文输出五个C、带PDF页码的主张—证据表、方法重建、
尚未解决的问题和最终自检，区分作者报告与独立核验。
```

只想先判断值不值得读时：

```text
$three-pass-paper-reading 对这篇论文做第一遍阅读，
说明是否值得继续，以及我需要补哪些背景知识。
```

也可以把 `skills/three-pass-paper-reading/` 整个目录复制到Codex的技能目录：`$CODEX_HOME/skills`，未设置时为 `~/.codex/skills`。保留其中的 `references/` 子目录。其他助手也可读取 `SKILL.md` 执行，具体调用语法取决于应用。

自己读论文时，可以直接打开[阅读模板](templates/reading-notes.md)，逐项记录判断。

## 我们增加了什么

三遍阅读、五个C、停止/继续决策、虚拟重实现和综述检索思路来自Keshav原文。本项目增加了便于AI执行与人工检查的做法：

- 用页码记录主张与证据，回看原始图表、公式和页面。
- 先写方法重建，再核对原文并记录修正。
- 复算增量，区分百分点、相对百分比和不同基线。
- 分清作者主张、已确认的内部不一致和待验证风险。
- 留下实际使用情况与自检记录。

具体对应关系见[方法溯源](skills/three-pass-paper-reading/references/method-origin.md)。

## 两篇实际试读

首次应用阅读了两篇视觉检测论文及两页方法文章，共 **31页PDF**；两篇研究论文均完成三遍阅读，对关键图表进行了视觉核查，并留下 **36项数值复算**。

| 试读对象 | 一个值得学习的阅读发现 | 成果 |
|---|---|---|
| YOLOv8 + CBAM的PCB缺陷检测 | 同一个“提升幅度”必须对应明确基线：表3支持+9.5个百分点，表4支持+3.3个百分点。 | [完整报告](examples/pcb-defect-detection.zh-CN.md) |
| STN + TPS + CBAM的农业目标检测 | 接受显著性结论前，需要重建空间坐标链路，核对实验口径与统计样本单位。 | [完整报告](examples/agricultural-detection.zh-CN.md) |

试读完成了内容审查、方法重建和算术复算，没有训练作者模型或独立验证其精度/速度。两篇论文的数据、任务和指标口径不同，不直接比较数值高低。[英文示例导读](examples/README.md)概括了两篇成果及验证范围。

复跑算术检查只需要Python 3标准库：

```bash
python examples/numeric_checks.py
```

脚本写入 `examples/numeric-checks.json`。输入数字来自人工转录、原表视觉核对；脚本不自动抽表，也不运行检测模型。

## 原文与致谢

**S. Keshav，《How to Read a Paper》，ACM SIGCOMM Computer Communication Review，37(3)，83–84，2007年7月。** 本次使用的2007年版本署名单位为**滑铁卢大学（University of Waterloo）**。

- [滑铁卢大学托管的2007年原文](https://cs.uwaterloo.ca/~Brecht/courses/856/readings/how-to-read/keshav-paper-reading.pdf)
- [作者维护的文章页面：后续版本与多语言翻译](https://svr-sk818-web.cl.cam.ac.uk/keshav/publications/htrap.html)

这是[July](https://github.com/jiangyuhan0318-July)与Codex共同整理的独立实践版本。阅读方法归功于Keshav；本项目贡献是技能化执行、记录和示例。试读报告为AI辅助学习成果，保留页码证据与核验边界。欢迎通过GitHub issue提交附有论文版本和页码/表号的修正。

## 许可

仓库自行撰写的技能指令、模板、脚本和分析文字采用[MIT许可](LICENSE)。参考论文保留各自权利与许可；本仓库提供来源链接和我们的阅读笔记，不附带原始PDF、全文抽取文本或整页截图。
