# 软件选择：在当前任务下最佳，而非普遍最佳

先遵守用户指定软件、已存在的模型代码、许可证和输出要求；更换工具的收益必须大于转换成本。以下为工作流建议，不是软件速度基准或原作者使用证明。

|任务|默认首选|何时选备选|
|---|---|---|
|论文静态定量图、复杂子图、局部放大|Python Matplotlib|已有MATLAB仿真可直接沿用，避免迁移模型输出|
|统计分布、雨云、联合图、相关矩阵|Seaborn+Matplotlib|已有R统计管线可沿用ggplot2；小样本不用密度装饰|
|交互探索、桑基、层级构成|Plotly|论文最终需要静态导出时验证导出依赖和小字清晰度；静态组合也可转Matplotlib|
|制图投影、比例尺、空间图层排版|QGIS|模型批量生成地图选GeoPandas+Matplotlib；已有ArcGIS许可与项目可沿用ArcGIS|
|真实SHAP解释图|SHAP及现有模型环境|不把普通特征重要性改名SHAP；没有解释值先计算或改图|
|生存曲线和风险表|已有R流程选survival/survminer|Python现有流程选lifelines；事件、删失定义优先于视觉效果|
|无需编程的常规科研图|已有Origin工作流|批量、可复现、复杂图版需求优先代码方案；先确认许可证|
|机制框架与非定量注释|draw.io或已有PowerPoint|规则复杂或需自动重排时选Graphviz；公式/文字保持可编辑|

原始数值图不使用生成式图片模型自由绘制。图形美化和拼版不能改写统计量；输出用户要求的格式，不强制增加多种格式。论文静态图和交互探索是不同交付，选软件时先明确。

## 官方能力资料（2026-09-09核对）

- [Matplotlib示例库](https://matplotlib.org/stable/gallery/index.html)：线、条、场、误差棒、布局与局部放大等能力。
- [Seaborn示例库](https://seaborn.pydata.org/examples/index.html)：分布、联合图、分面及矩阵等能力。
- [Plotly桑基说明](https://plotly.com/python/sankey-diagram/)：source、target、value结构。
- [QGIS排版手册](https://docs.qgis.org/latest/en/docs/user_manual/print_composer/index.html)：地图版面相关资料入口。

这些资料支撑绘图能力；“首选”的判断来自任务适配，不是官方优劣排名。实际调用前核对当前环境中的版本、导出依赖及工具可用性。
