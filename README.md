# 数学建模论文绘图 Skill

[下载完整 Skill 安装包](math-modeling-figures.zip)

安装包包含 `math-modeling-figures/SKILL.md`、15份参考文档及使用说明，共17个文件。解压后将完整 `math-modeling-figures` 文件夹复制到工具的技能目录，例如 Codex 的 `~/.codex/skills/`，保持 references 子目录完整。

## 终端安装（Python 3.9+，无需第三方依赖）

Windows PowerShell：

```powershell
curl.exe -fL https://raw.githubusercontent.com/Drancy-Den/picture-sikill/main/install.py -o install-math-modeling.py
python install-math-modeling.py
```

macOS / Linux：

```bash
curl -fL https://raw.githubusercontent.com/Drancy-Den/picture-sikill/main/install.py -o install-math-modeling.py
python3 install-math-modeling.py
```

先确认下载命令成功，再运行脚本；也可先阅读 [install.py](install.py)。脚本下载固定提交版本的ZIP并校验SHA-256，默认安装到 `$CODEX_HOME/skills/math-modeling-figures`，未设置CODEX_HOME时使用 `~/.codex/skills/math-modeling-figures`。同版本重复安装只核验，不覆盖；已有目录内容不同时停止，保留原文件。

离线安装：先下载 [ZIP](math-modeling-figures.zip) 和 [install.py](install.py) 放在同一目录，运行 `python install.py`。也可用 `python install.py --archive /path/to/math-modeling-figures.zip` 指定已下载的安装包，使用 `--dest /path/to/skills` 指定技能父目录。

安装成功后下一轮即可使用 `$math-modeling-figures`。此脚本安装Codex技能，不是Python包，不使用 `pip install`。

## 内容

- 48类图形与版式提示词，按10个图形家族按需读取。
- 选图规则、数据要求、配色与版式建议、质量检查。
- 2021–2025年196份论文的可视化阅读索引及软件证据。

## 调用示例

```text
使用 $math-modeling-figures，为我的数学建模论文制作预测对比图。
数据字段：year、actual、forecast、lower_95、upper_95。
上下界为95%预测区间。使用Python，只输出PNG和绘图代码。
```

也可以只请求某种图的提示词，不必实际生成图像。

## 研究边界

检查聚焦本地资料集196份PDF（4,923页）的可视化，未审核全部数学推导；其中两份2022年文件名标注F奖和M奖，因此不把全部样本称为O奖。48类包含复合版式，并非互斥频率统计。

原作者软件与复现建议已分开标注。仓库发布原创总结和提示词，不分发论文PDF或截图。技能已通过结构、48类覆盖及相对链接校验，尚未在所有客户端和全部绘图软件中端到端验证。
