## Findings
既存LPは静的HTML、style.cssを法務ページと共有。作業開始時worktree clean。アセットは520x909の実機画像とMP4、アイコン。ChatGPTはWebCodex経由で対象パスを読み取り済み。
現在のアプリソースSettingsManager.swiftにはClaude、Codex、各API、Apple Intelligence、MLX、LM Studio、Ollama等が存在する。READMEだけでプロバイダの有無を判断しない。
LicenseConfig.swift trialDays=7、LicenseManager.freeSlots=[.one]。旧LPは14日・slot9無料と記載。日数はユーザー回答待ち、無料対象は誤字修正のみを記載する。価格は既存表記を維持し購入処理は実行しない。購入URLのソースコメントにテストモードとあるがコメントの鮮度は未確認。
## Lessons applied
none applicable
## Unknowns
配布中バイナリとローカルソースの一致、販売設定の現在の本番状態は未確認。公開せずドラフトPRでレビューに回す。
