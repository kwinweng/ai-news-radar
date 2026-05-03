import unittest

from scripts.update_news import classify_business_category


class BusinessCategoryTests(unittest.TestCase):
    def classify(self, title, source="Example Feed", site_name="Example", url="https://example.com/post"):
        return classify_business_category(
            {
                "title": title,
                "title_zh": title,
                "source": source,
                "site_name": site_name,
                "url": url,
            }
        )

    def test_models_platforms(self):
        result = self.classify("OpenAI 发布 GPT-5o 模型 API 和 Agent 平台更新")
        self.assertEqual(result["business_category"], "models_platforms")
        self.assertEqual(result["business_category_label"], "模型与平台")

    def test_models_platforms_llama_benchmark(self):
        result = self.classify("Meta 开源 LLaMA 3 权重，各大 benchmark 评测结果出炉")
        self.assertEqual(result["business_category"], "models_platforms")

    def test_models_platforms_diffusion_multimodal(self):
        result = self.classify("Stable Diffusion 3 发布，多模态扩散模型性能提升显著")
        self.assertEqual(result["business_category"], "models_platforms")

    def test_models_platforms_rag_embedding(self):
        result = self.classify("RAG 架构中 embedding 向量检索增强方案对比评测")
        self.assertEqual(result["business_category"], "models_platforms")

    def test_product_trends(self):
        result = self.classify("Perplexity 推出新的 AI 浏览器产品功能和订阅定价")
        self.assertEqual(result["business_category"], "product_trends")

    def test_product_trends_low_code(self):
        result = self.classify("低代码 AI 平台 Dify 发布 v2 版本，无代码迭代体验再升级")
        self.assertEqual(result["business_category"], "product_trends")

    def test_product_trends_vscode_ide(self):
        result = self.classify("Cursor 与 VSCode IDE 深度集成 integration，代码补全新功能上线")
        self.assertEqual(result["business_category"], "product_trends")

    def test_product_trends_canva_figma(self):
        result = self.classify("Canva 与 Figma 发布 AI 生成新功能，产品体验全面升级")
        self.assertEqual(result["business_category"], "product_trends")

    def test_growth_commercial(self):
        result = self.classify("AI 应用通过 PLG 增长策略提升付费转化和留存")
        self.assertEqual(result["business_category"], "growth_commercial")

    def test_growth_commercial_saas_arpu(self):
        result = self.classify("SaaS AI 产品提升 ARPU 的订阅制 freemium 定价策略拆解")
        self.assertEqual(result["business_category"], "growth_commercial")

    def test_growth_commercial_overseas(self):
        result = self.classify("国产 AI 工具出海全球化，海外市场 B2B 获客路径分析")
        self.assertEqual(result["business_category"], "growth_commercial")

    def test_growth_commercial_kol_seo(self):
        result = self.classify("KOL 内容营销 + SEO 双驱动为 AI 产品带来海量免费流量")
        self.assertEqual(result["business_category"], "growth_commercial")

    def test_industry_insight(self):
        result = self.classify("AI 创业公司完成融资，行业分析称企业采用正在加速")
        self.assertEqual(result["business_category"], "industry_insight")

    def test_industry_insight_regulation(self):
        result = self.classify("欧盟 AI Act 正式实施，各平台合规备案监管细则解读")
        self.assertEqual(result["business_category"], "industry_insight")

    def test_industry_insight_chip_gpu(self):
        result = self.classify("英伟达 H100 GPU 算力需求激增，数据中心能耗与碳排放问题引发关注")
        self.assertEqual(result["business_category"], "industry_insight")

    def test_industry_insight_ipo_ma(self):
        result = self.classify("AI 独角兽完成并购后估值重估，分析师预测年内 IPO 上市")
        self.assertEqual(result["business_category"], "industry_insight")

    def test_tooling_ops(self):
        result = self.classify("面向运营团队的 AI 自动化数据分析工具发布")
        self.assertEqual(result["business_category"], "tooling_ops")

    def test_case_playbooks(self):
        result = self.classify("品牌用 AI 营销案例打造可复用私域运营玩法")
        self.assertEqual(result["business_category"], "case_playbooks")

    def test_case_playbooks_tutorial(self):
        result = self.classify("手把手教程：如何用 AI 代码生成工具完成自动化测试实战")
        self.assertEqual(result["business_category"], "case_playbooks")

    def test_case_playbooks_vertical(self):
        result = self.classify("医疗AI 落地经验总结：金融AI 与教育AI 应用场景横向对比")
        self.assertEqual(result["business_category"], "case_playbooks")

    def test_case_playbooks_step_by_step(self):
        result = self.classify("Step by step guide: how to build a customer service chatbot with LLMs")
        self.assertEqual(result["business_category"], "models_platforms")

    def test_other_fallback(self):
        result = self.classify("一条相关但暂时无法归入业务分类的 AI 新闻")
        self.assertEqual(result["business_category"], "other")
        self.assertEqual(result["business_category_label"], "其他信号")


if __name__ == "__main__":
    unittest.main()
