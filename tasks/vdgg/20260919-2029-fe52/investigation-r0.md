## Root Cause Investigation
severity: medium。英語320pxで料金カードが右端318pxまで膨らみ、clientWidth305pxを13px超過。
## Pattern Analysis
nowrapの英語ボタンと左右25px余白・28px gapがグリッドの最小幅を押し広げる。
## Hypothesis
狭幅だけボタンのpadding/gap/fontを縮めればカード内に収まる。
## Implementation plan
既存モバイルmedia内相当の料金CTAルールを追加し、日英320/390/768/1440でscrollWidth<=clientWidthを検証する。
