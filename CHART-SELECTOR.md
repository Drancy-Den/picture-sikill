# 补充skill：根据数据自动选常规图或创新图

独立名称：`math-modeling-chart-selector`。原 `math-modeling-figures` 及原安装脚本保持不变。

提供26类数据路由、常规与创新选择条件、情境化软件建议、4条总/模式提示词和26条专用提示词。完整提示词保留在安装包 `references/prompts.md` 中。创新以信息增益和统计语义为前提，不保证每个数据集都适合创新图。

## 终端安装（Python 3.9+）

Windows PowerShell：

```powershell
curl.exe -fL https://raw.githubusercontent.com/Drancy-Den/picture-sikill/main/install-chart-selector.py -o install-chart-selector.py
python install-chart-selector.py
```

macOS/Linux：

```bash
curl -fL https://raw.githubusercontent.com/Drancy-Den/picture-sikill/main/install-chart-selector.py -o install-chart-selector.py
python3 install-chart-selector.py
```

先确认下载成功，再执行脚本。安装脚本下载[独立安装包](math-modeling-chart-selector.zip)并核对固定SHA-256；现有内容完全相同时仅核验，不同时停止，不覆盖修改。下载URL使用main而内容由固定校验值锁定；包更新后旧脚本将拒绝不匹配的包。也可把脚本和ZIP放在一起离线运行，或使用 `--archive` 指定ZIP、`--dest` 指定技能父目录。

默认安装到 `$CODEX_HOME/skills/math-modeling-chart-selector`，未设置时为 `~/.codex/skills/math-modeling-chart-selector`。不会修改原绘图skill。

## 使用

```text
使用 $math-modeling-chart-selector，检查我的数据，自动选一个常规图或创新图，
解释选择依据和最佳适用软件，并输出能直接给AI画图的提示词。先不要实际画图。
```

```text
先用 $math-modeling-chart-selector 选图，再用 $math-modeling-figures 按真实数据画图。
我已有Python代码，只交付PNG与代码；创新图没有信息增益时使用常规图。
```

本skill可独立使用；第二个例子只有原绘图skill已安装时才需要联用。下一轮可调用本机安装后的skill。
