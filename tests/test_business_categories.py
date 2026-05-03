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

    def test_product_trends(self):
        result = self.classify("Perplexity 推出新的 AI 浏览器产品功能和订阅定价")
        self.assertEqual(result["business_category"], "product_trends")

    def test_growth_commercial(self):
        result = self.classify("AI 应用通过 PLG 增长策略提升付费转化和留存")
        self.assertEqual(result["business_category"], "growth_commercial")

    def test_industry_insight(self):
        result = self.classify("AI 创业公司完成融资，行业分析称企业采用正在加速")
        self.assertEqual(result["business_category"], "industry_insight")

    def test_tooling_ops(self):
        result = self.classify("面向运营团队的 AI 自动化数据分析工具发布")
        self.assertEqual(result["business_category"], "tooling_ops")

    def test_case_playbooks(self):
        result = self.classify("品牌用 AI 营销案例打造可复用私域运营玩法")
        self.assertEqual(result["business_category"], "case_playbooks")

    def test_other_fallback(self):
        result = self.classify("一条相关但暂时无法归入业务分类的 AI 新闻")
        self.assertEqual(result["business_category"], "other")
        self.assertEqual(result["business_category_label"], "其他信号")


if __name__ == "__main__":
    unittest.main()
