# llama3instruct measurement report

Plan SHA-256: `c742158d7ae455ffa11d0551922fbdf5321b0c49504fcba19ac92c71d3c810f2`
Erratum 1 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) plan SHA-256 before this erratum: `56679285fb538ddfe04723dfadca09a1a34418ff6ba766cc55fa559c86675cc6`
Erratum 4 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 4 (2026-10-02) plan SHA-256 before this erratum: `c1747f993babaa05f8dd3c99543584d8555cb9212138a92e909972505a210450`
Erratum 5 (2026-10-05) plan SHA-256 before this erratum: `7b85c86fc37013b4e42e3a46c77bdef4cf6073171add570ca9879b7f7c896455`
Erratum 6 (2026-10-05) plan SHA-256 before this erratum: `01f67a5b0a8fa45deb692ceaea5f1420b7778b9cdfffc9808a6b91cde966e322`
Erratum 7 (2026-10-08) plan SHA-256 before this erratum: `e33bdf0004f1e97aa30a4e8dd1a124f1bc20586c4104f7eeb9d3434654cfff73`
Prompt SHA-256: `2314d1cccef40ae12b89bf36a09508adf2122cc25e49b606faa65b8f9bda3d19`

No generation was run. Measurements use `analysis_text` only.

## Data

- Output rows: 4824
- Missing `analysis_text`: 0. Those rows stay in the feature file and are excluded from calculations.
- Rows in the calculations: 4824
- Contexts: 804
- Rows by condition: {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
- Rows by position: {'Early': 1608, 'Late': 1608, 'Middle': 1608}
- Rows with any format flag, among analysed rows: 0
- Persona content words removed for the echo controls: 55

## Part B accuracy

| variant | scope | accuracy | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | 0.5479 | 0.5334 | 0.5628 | 0.1667 | 4824 |
| B1 | Early | 0.5404 | 0.5143 | 0.5653 | 0.1667 | 1608 |
| B1 | Middle | 0.5790 | 0.5553 | 0.6020 | 0.1667 | 1608 |
| B1 | Late | 0.5243 | 0.4994 | 0.5479 | 0.1667 | 1608 |
| B2 | overall | 0.5075 | 0.4940 | 0.5205 | 0.1667 | 4824 |
| B2 | Early | 0.4857 | 0.4639 | 0.5087 | 0.1667 | 1608 |
| B2 | Middle | 0.5379 | 0.5143 | 0.5622 | 0.1667 | 1608 |
| B2 | Late | 0.4988 | 0.4726 | 0.5230 | 0.1667 | 1608 |
| B3 | overall | 0.5435 | 0.5294 | 0.5587 | 0.1667 | 4824 |
| B3 | Early | 0.5410 | 0.5162 | 0.5659 | 0.1667 | 1608 |
| B3 | Middle | 0.5746 | 0.5510 | 0.5977 | 0.1667 | 1608 |
| B3 | Late | 0.5149 | 0.4907 | 0.5386 | 0.1667 | 1608 |
| B4 | overall | 0.4664 | 0.4534 | 0.4795 | 0.1667 | 4824 |
| B4 | Early | 0.4515 | 0.4297 | 0.4720 | 0.1667 | 1608 |
| B4 | Middle | 0.5081 | 0.4851 | 0.5317 | 0.1667 | 1608 |
| B4 | Late | 0.4397 | 0.4154 | 0.4646 | 0.1667 | 1608 |
| B5 | overall | 0.2411 | 0.2307 | 0.2519 | 0.1667 | 4824 |
| B5 | Early | 0.2450 | 0.2270 | 0.2625 | 0.1667 | 1608 |
| B5 | Middle | 0.2450 | 0.2270 | 0.2631 | 0.1667 | 1608 |
| B5 | Late | 0.2332 | 0.2152 | 0.2519 | 0.1667 | 1608 |
| B6 | overall | 0.6137 | 0.5983 | 0.6294 | 0.2000 | 4020 |
| B6 | Early | 0.6112 | 0.5843 | 0.6373 | 0.2000 | 1340 |
| B6 | Middle | 0.6336 | 0.6090 | 0.6582 | 0.2000 | 1340 |
| B6 | Late | 0.5963 | 0.5709 | 0.6209 | 0.2000 | 1340 |
| B7 | overall | 0.6428 | 0.6296 | 0.6567 | 0.2000 | 4824 |
| B7 | Early | 0.6430 | 0.6231 | 0.6642 | 0.2000 | 1608 |
| B7 | Middle | 0.6772 | 0.6567 | 0.6984 | 0.2000 | 1608 |
| B7 | Late | 0.6082 | 0.5840 | 0.6325 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.4490 | 0.4167 | 0.4838 | 0.1667 | 804 |
| B1 | overall | P1 | 0.5983 | 0.5622 | 0.6368 | 0.1667 | 804 |
| B1 | overall | P2 | 0.3458 | 0.3159 | 0.3769 | 0.1667 | 804 |
| B1 | overall | P3 | 0.4925 | 0.4590 | 0.5274 | 0.1667 | 804 |
| B1 | overall | P4 | 0.6716 | 0.6405 | 0.7002 | 0.1667 | 804 |
| B1 | overall | P5 | 0.7301 | 0.6990 | 0.7587 | 0.1667 | 804 |
| B1 | Early | P0 | 0.3918 | 0.3358 | 0.4515 | 0.1667 | 268 |
| B1 | Early | P1 | 0.6231 | 0.5671 | 0.6791 | 0.1667 | 268 |
| B1 | Early | P2 | 0.3507 | 0.2947 | 0.4067 | 0.1667 | 268 |
| B1 | Early | P3 | 0.4851 | 0.4254 | 0.5411 | 0.1667 | 268 |
| B1 | Early | P4 | 0.7425 | 0.6940 | 0.7948 | 0.1667 | 268 |
| B1 | Early | P5 | 0.6493 | 0.5896 | 0.7052 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.4888 | 0.4327 | 0.5485 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.6119 | 0.5522 | 0.6716 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.3731 | 0.3172 | 0.4291 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.4664 | 0.4030 | 0.5224 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.6940 | 0.6381 | 0.7425 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.8396 | 0.7948 | 0.8806 | 0.1667 | 268 |
| B1 | Late | P0 | 0.4664 | 0.4067 | 0.5261 | 0.1667 | 268 |
| B1 | Late | P1 | 0.5597 | 0.5000 | 0.6194 | 0.1667 | 268 |
| B1 | Late | P2 | 0.3134 | 0.2575 | 0.3694 | 0.1667 | 268 |
| B1 | Late | P3 | 0.5261 | 0.4627 | 0.5858 | 0.1667 | 268 |
| B1 | Late | P4 | 0.5784 | 0.5149 | 0.6343 | 0.1667 | 268 |
| B1 | Late | P5 | 0.7015 | 0.6455 | 0.7575 | 0.1667 | 268 |
| B2 | overall | P0 | 0.4204 | 0.3868 | 0.4527 | 0.1667 | 804 |
| B2 | overall | P1 | 0.5734 | 0.5386 | 0.6070 | 0.1667 | 804 |
| B2 | overall | P2 | 0.2873 | 0.2575 | 0.3197 | 0.1667 | 804 |
| B2 | overall | P3 | 0.4303 | 0.3943 | 0.4652 | 0.1667 | 804 |
| B2 | overall | P4 | 0.6542 | 0.6219 | 0.6878 | 0.1667 | 804 |
| B2 | overall | P5 | 0.6791 | 0.6493 | 0.7090 | 0.1667 | 804 |
| B2 | Early | P0 | 0.3507 | 0.2948 | 0.4067 | 0.1667 | 268 |
| B2 | Early | P1 | 0.5970 | 0.5373 | 0.6567 | 0.1667 | 268 |
| B2 | Early | P2 | 0.2649 | 0.2127 | 0.3209 | 0.1667 | 268 |
| B2 | Early | P3 | 0.3694 | 0.3134 | 0.4291 | 0.1667 | 268 |
| B2 | Early | P4 | 0.7239 | 0.6679 | 0.7761 | 0.1667 | 268 |
| B2 | Early | P5 | 0.6082 | 0.5485 | 0.6642 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.4590 | 0.3993 | 0.5187 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.5858 | 0.5299 | 0.6418 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.3022 | 0.2463 | 0.3583 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.4254 | 0.3731 | 0.4888 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.6978 | 0.6455 | 0.7537 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.7575 | 0.7052 | 0.8060 | 0.1667 | 268 |
| B2 | Late | P0 | 0.4515 | 0.3918 | 0.5112 | 0.1667 | 268 |
| B2 | Late | P1 | 0.5373 | 0.4813 | 0.5970 | 0.1667 | 268 |
| B2 | Late | P2 | 0.2948 | 0.2425 | 0.3507 | 0.1667 | 268 |
| B2 | Late | P3 | 0.4963 | 0.4366 | 0.5560 | 0.1667 | 268 |
| B2 | Late | P4 | 0.5410 | 0.4776 | 0.6007 | 0.1667 | 268 |
| B2 | Late | P5 | 0.6716 | 0.6157 | 0.7240 | 0.1667 | 268 |
| B3 | overall | P0 | 0.4341 | 0.4005 | 0.4677 | 0.1667 | 804 |
| B3 | overall | P1 | 0.6119 | 0.5771 | 0.6480 | 0.1667 | 804 |
| B3 | overall | P2 | 0.3408 | 0.3072 | 0.3707 | 0.1667 | 804 |
| B3 | overall | P3 | 0.4925 | 0.4590 | 0.5274 | 0.1667 | 804 |
| B3 | overall | P4 | 0.6592 | 0.6281 | 0.6903 | 0.1667 | 804 |
| B3 | overall | P5 | 0.7226 | 0.6915 | 0.7525 | 0.1667 | 804 |
| B3 | Early | P0 | 0.3769 | 0.3209 | 0.4328 | 0.1667 | 268 |
| B3 | Early | P1 | 0.6343 | 0.5746 | 0.6940 | 0.1667 | 268 |
| B3 | Early | P2 | 0.3396 | 0.2835 | 0.3993 | 0.1667 | 268 |
| B3 | Early | P3 | 0.5149 | 0.4552 | 0.5746 | 0.1667 | 268 |
| B3 | Early | P4 | 0.7388 | 0.6903 | 0.7910 | 0.1667 | 268 |
| B3 | Early | P5 | 0.6418 | 0.5821 | 0.6978 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.4701 | 0.4104 | 0.5299 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.6343 | 0.5746 | 0.6903 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.3881 | 0.3321 | 0.4440 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.4515 | 0.3955 | 0.5075 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.6716 | 0.6157 | 0.7239 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.8321 | 0.7873 | 0.8731 | 0.1667 | 268 |
| B3 | Late | P0 | 0.4552 | 0.3955 | 0.5112 | 0.1667 | 268 |
| B3 | Late | P1 | 0.5672 | 0.5075 | 0.6269 | 0.1667 | 268 |
| B3 | Late | P2 | 0.2948 | 0.2388 | 0.3507 | 0.1667 | 268 |
| B3 | Late | P3 | 0.5112 | 0.4515 | 0.5709 | 0.1667 | 268 |
| B3 | Late | P4 | 0.5672 | 0.5037 | 0.6231 | 0.1667 | 268 |
| B3 | Late | P5 | 0.6940 | 0.6381 | 0.7500 | 0.1667 | 268 |
| B4 | overall | P0 | 0.3632 | 0.3284 | 0.3968 | 0.1667 | 804 |
| B4 | overall | P1 | 0.6306 | 0.5970 | 0.6642 | 0.1667 | 804 |
| B4 | overall | P2 | 0.2264 | 0.1965 | 0.2587 | 0.1667 | 804 |
| B4 | overall | P3 | 0.3557 | 0.3234 | 0.3905 | 0.1667 | 804 |
| B4 | overall | P4 | 0.6331 | 0.6007 | 0.6642 | 0.1667 | 804 |
| B4 | overall | P5 | 0.5896 | 0.5572 | 0.6219 | 0.1667 | 804 |
| B4 | Early | P0 | 0.2761 | 0.2239 | 0.3284 | 0.1667 | 268 |
| B4 | Early | P1 | 0.6716 | 0.6119 | 0.7239 | 0.1667 | 268 |
| B4 | Early | P2 | 0.2276 | 0.1791 | 0.2799 | 0.1667 | 268 |
| B4 | Early | P3 | 0.3657 | 0.3097 | 0.4254 | 0.1667 | 268 |
| B4 | Early | P4 | 0.6604 | 0.6007 | 0.7164 | 0.1667 | 268 |
| B4 | Early | P5 | 0.5075 | 0.4478 | 0.5634 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.4403 | 0.3806 | 0.5037 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.6716 | 0.6119 | 0.7276 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.2313 | 0.1828 | 0.2836 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.3694 | 0.3097 | 0.4254 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.6903 | 0.6343 | 0.7425 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.6455 | 0.5858 | 0.7016 | 0.1667 | 268 |
| B4 | Late | P0 | 0.3731 | 0.3172 | 0.4254 | 0.1667 | 268 |
| B4 | Late | P1 | 0.5485 | 0.4851 | 0.6082 | 0.1667 | 268 |
| B4 | Late | P2 | 0.2201 | 0.1716 | 0.2724 | 0.1667 | 268 |
| B4 | Late | P3 | 0.3321 | 0.2761 | 0.3881 | 0.1667 | 268 |
| B4 | Late | P4 | 0.5485 | 0.4925 | 0.6082 | 0.1667 | 268 |
| B4 | Late | P5 | 0.6157 | 0.5560 | 0.6754 | 0.1667 | 268 |
| B5 | overall | P0 | 0.1182 | 0.0958 | 0.1418 | 0.1667 | 804 |
| B5 | overall | P1 | 0.5547 | 0.5224 | 0.5859 | 0.1667 | 804 |
| B5 | overall | P2 | 0.0995 | 0.0784 | 0.1219 | 0.1667 | 804 |
| B5 | overall | P3 | 0.4826 | 0.4502 | 0.5162 | 0.1667 | 804 |
| B5 | overall | P4 | 0.0821 | 0.0622 | 0.1032 | 0.1667 | 804 |
| B5 | overall | P5 | 0.1095 | 0.0858 | 0.1318 | 0.1667 | 804 |
| B5 | Early | P0 | 0.1381 | 0.0970 | 0.1791 | 0.1667 | 268 |
| B5 | Early | P1 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 268 |
| B5 | Early | P2 | 0.1194 | 0.0821 | 0.1604 | 0.1667 | 268 |
| B5 | Early | P3 | 0.3619 | 0.3096 | 0.4216 | 0.1667 | 268 |
| B5 | Early | P4 | 0.0821 | 0.0485 | 0.1194 | 0.1667 | 268 |
| B5 | Early | P5 | 0.1082 | 0.0709 | 0.1455 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.0896 | 0.0560 | 0.1231 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.5784 | 0.5187 | 0.6381 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.0821 | 0.0522 | 0.1158 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.5299 | 0.4701 | 0.5858 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.0970 | 0.0634 | 0.1306 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.0933 | 0.0597 | 0.1306 | 0.1667 | 268 |
| B5 | Late | P0 | 0.1269 | 0.0896 | 0.1680 | 0.1667 | 268 |
| B5 | Late | P1 | 0.4254 | 0.3657 | 0.4888 | 0.1667 | 268 |
| B5 | Late | P2 | 0.0970 | 0.0672 | 0.1343 | 0.1667 | 268 |
| B5 | Late | P3 | 0.5560 | 0.5000 | 0.6157 | 0.1667 | 268 |
| B5 | Late | P4 | 0.0672 | 0.0410 | 0.0970 | 0.1667 | 268 |
| B5 | Late | P5 | 0.1269 | 0.0896 | 0.1679 | 0.1667 | 268 |
| B6 | overall | P1 | 0.6493 | 0.6157 | 0.6828 | 0.2000 | 804 |
| B6 | overall | P2 | 0.4316 | 0.3980 | 0.4652 | 0.2000 | 804 |
| B6 | overall | P3 | 0.5187 | 0.4851 | 0.5535 | 0.2000 | 804 |
| B6 | overall | P4 | 0.6716 | 0.6405 | 0.7002 | 0.2000 | 804 |
| B6 | overall | P5 | 0.7973 | 0.7687 | 0.8234 | 0.2000 | 804 |
| B6 | Early | P1 | 0.6642 | 0.6119 | 0.7165 | 0.2000 | 268 |
| B6 | Early | P2 | 0.4179 | 0.3582 | 0.4739 | 0.2000 | 268 |
| B6 | Early | P3 | 0.5224 | 0.4627 | 0.5821 | 0.2000 | 268 |
| B6 | Early | P4 | 0.7425 | 0.6940 | 0.7948 | 0.2000 | 268 |
| B6 | Early | P5 | 0.7090 | 0.6493 | 0.7612 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.6679 | 0.6119 | 0.7239 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.4291 | 0.3693 | 0.4851 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.4701 | 0.4104 | 0.5299 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.6978 | 0.6418 | 0.7463 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.9030 | 0.8657 | 0.9366 | 0.2000 | 268 |
| B6 | Late | P1 | 0.6157 | 0.5560 | 0.6716 | 0.2000 | 268 |
| B6 | Late | P2 | 0.4478 | 0.3881 | 0.5075 | 0.2000 | 268 |
| B6 | Late | P3 | 0.5634 | 0.5000 | 0.6194 | 0.2000 | 268 |
| B6 | Late | P4 | 0.5746 | 0.5112 | 0.6306 | 0.2000 | 268 |
| B6 | Late | P5 | 0.7799 | 0.7276 | 0.8284 | 0.2000 | 268 |
| B7 | overall | P0 | 0.3980 | 0.3657 | 0.4328 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.8029 | 0.7823 | 0.8240 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.4776 | 0.4428 | 0.5124 | 0.2000 | 804 |
| B7 | overall | P4 | 0.6704 | 0.6381 | 0.6990 | 0.2000 | 804 |
| B7 | overall | P5 | 0.7052 | 0.6716 | 0.7363 | 0.2000 | 804 |
| B7 | Early | P0 | 0.3358 | 0.2835 | 0.3955 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.8601 | 0.8302 | 0.8899 | 0.2000 | 536 |
| B7 | Early | P3 | 0.4664 | 0.4067 | 0.5261 | 0.2000 | 268 |
| B7 | Early | P4 | 0.7388 | 0.6902 | 0.7910 | 0.2000 | 268 |
| B7 | Early | P5 | 0.5970 | 0.5336 | 0.6530 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.4440 | 0.3881 | 0.5000 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.8172 | 0.7854 | 0.8489 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.4627 | 0.4030 | 0.5224 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.6978 | 0.6418 | 0.7464 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.8246 | 0.7761 | 0.8694 | 0.2000 | 268 |
| B7 | Late | P0 | 0.4142 | 0.3545 | 0.4739 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.7313 | 0.6959 | 0.7687 | 0.2000 | 536 |
| B7 | Late | P3 | 0.5037 | 0.4403 | 0.5634 | 0.2000 | 268 |
| B7 | Late | P4 | 0.5746 | 0.5112 | 0.6306 | 0.2000 | 268 |
| B7 | Late | P5 | 0.6940 | 0.6380 | 0.7500 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | -0.8160 | 0.4186 | 0.0513 | -1.6366 | 0.0045 |
| C(position, Treatment(reference='Early'))[T.Late] | -0.3035 | 0.1155 | 0.0086 | -0.5299 | -0.0771 |
| C(position, Treatment(reference='Early'))[T.Middle] | -0.0056 | 0.0855 | 0.9476 | -0.1733 | 0.1621 |
| log_context | 0.1764 | 0.0739 | 0.0170 | 0.0316 | 0.3213 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.5040 | -0.6947 | -0.3171 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1609 | -0.3902 | 0.0663 | 0.1820 | 0.1820 | 268 | not confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.5721 | -0.8825 | -0.2517 | 0.0010 | 0.0030 | 268 | confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.7790 | -1.2085 | -0.3712 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | -0.4638 | -1.0084 | 0.0312 | 0.0620 | 0.0620 | 804 | not confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | -0.0890 | -1.0316 | 0.8380 | 0.8570 | 1.0000 | 268 | not confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | -1.1623 | -2.0429 | -0.3097 | 0.0080 | 0.0360 | 268 | opposite |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | -0.1401 | -0.9853 | 0.6405 | 0.7330 | 1.0000 | 268 | not confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | 0.1710 | 0.1276 | 0.2128 | 0.0000 | 0.0000 | 554 | opposite |
| Early | P1 - P0 | share_open | lower | pre-specified | 0.1019 | 0.0332 | 0.1698 | 0.0040 | 0.0080 | 238 | opposite |
| Middle | P1 - P0 | share_open | lower | pre-specified | 0.2540 | 0.1807 | 0.3323 | 0.0000 | 0.0000 | 166 | opposite |
| Late | P1 - P0 | share_open | lower | pre-specified | 0.1889 | 0.1217 | 0.2589 | 0.0000 | 0.0000 | 150 | opposite |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.7979 | 0.5928 | 1.0127 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.3075 | 0.0258 | 0.6198 | 0.0300 | 0.0600 | 268 | confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.9078 | 0.5303 | 1.3231 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 1.1784 | 0.7954 | 1.6175 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 5.0462 | 4.6461 | 5.4555 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 6.0809 | 5.4509 | 6.7413 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 5.1888 | 4.4489 | 5.8592 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 3.8688 | 3.1849 | 4.5420 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.2848 | 0.2429 | 0.3294 | 0.0000 | 0.0000 | 539 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.2436 | 0.1770 | 0.3084 | 0.0000 | 0.0000 | 234 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.2678 | 0.1976 | 0.3339 | 0.0000 | 0.0000 | 159 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.3693 | 0.2934 | 0.4458 | 0.0000 | 0.0000 | 146 | confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 7.0399 | 6.7215 | 7.3696 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 7.8802 | 7.3714 | 8.3895 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 7.5753 | 6.9649 | 8.1528 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 5.6642 | 5.0281 | 6.3039 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.3417 | 0.3031 | 0.3817 | 0.0000 | 0.0000 | 559 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.2899 | 0.2293 | 0.3498 | 0.0000 | 0.0000 | 238 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.3843 | 0.3142 | 0.4490 | 0.0000 | 0.0000 | 170 | confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | 0.3753 | 0.2980 | 0.4492 | 0.0000 | 0.0000 | 151 | confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -3.2690 | -3.7365 | -2.8086 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -3.4564 | -4.4250 | -2.5386 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -3.5965 | -4.2703 | -2.9279 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -2.7541 | -3.4617 | -2.0482 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.9937 | 1.6101 | 2.3988 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.7993 | 1.1194 | 2.5357 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.3865 | 1.6523 | 3.1245 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.7953 | 1.0694 | 2.5738 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -0.8120 | -1.2325 | -0.4289 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -0.9490 | -1.6013 | -0.2822 | 0.0060 | 0.0360 | 268 | confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -0.5315 | -1.2524 | 0.1818 | 0.1440 | 0.4320 | 268 | not confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -0.9555 | -1.6495 | -0.2830 | 0.0070 | 0.0360 | 268 | confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1621 | 0.1246 | 0.2036 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1165 | 0.0679 | 0.1735 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.2325 | 0.1624 | 0.3034 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1373 | 0.0827 | 0.2018 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | 0.0012 | 0.0000 | 0.0037 | 0.7090 | 0.7090 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | 0.0037 | 0.0000 | 0.0112 | 0.7090 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.3021 | -0.4013 | -0.2121 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.4563 | -0.6259 | -0.2835 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.3092 | -0.4508 | -0.1694 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1407 | -0.2745 | -0.0166 | 0.0260 | 0.0260 | 268 | confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | -0.1200 | -0.1635 | -0.0766 | 0.0000 | 0.0000 | 402 | confirmed |
| Early | P5 - P0 | share_open | lower | pre-specified | -0.1052 | -0.1727 | -0.0395 | 0.0010 | 0.0030 | 194 | confirmed |
| Middle | P5 - P0 | share_open | lower | pre-specified | -0.1615 | -0.2515 | -0.0670 | 0.0000 | 0.0000 | 112 | confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | -0.1016 | -0.1884 | -0.0174 | 0.0190 | 0.0190 | 96 | confirmed |
| overall | P5 - P0 | has_question | lower | pre-specified | -0.0386 | -0.0771 | -0.0012 | 0.0470 | 0.0470 | 804 | confirmed |
| Early | P5 - P0 | has_question | lower | pre-specified | -0.0784 | -0.1269 | -0.0299 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | has_question | lower | pre-specified | -0.0261 | -0.1045 | 0.0448 | 0.4980 | 0.9960 | 268 | not confirmed |
| Late | P5 - P0 | has_question | lower | pre-specified | -0.0112 | -0.0896 | 0.0635 | 0.7790 | 0.9960 | 268 | not confirmed |
| overall | P5 - P0 | plan_statement_present | higher | pre-specified | 0.2363 | 0.1990 | 0.2762 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | pre-specified | 0.2761 | 0.2090 | 0.3433 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | pre-specified | 0.2687 | 0.1977 | 0.3470 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | pre-specified | 0.1642 | 0.0932 | 0.2388 | 0.0000 | 0.0000 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.6181 | -1.1113 | -0.1544 | 0.0110 | 0.0220 | opposite |
| P1 - P0 | med_per_100 | higher | pre-specified | -0.0511 | -1.3230 | 1.1635 | 0.8880 | 1.0000 | not confirmed |
| P1 - P0 | share_open | lower | pre-specified | 0.0870 | -0.0109 | 0.1844 | 0.0920 | 0.2220 | not confirmed |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.8709 | 0.3631 | 1.3943 | 0.0000 | 0.0000 | opposite |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | -2.2120 | -3.1246 | -1.2891 | 0.0000 | 0.0000 | confirmed |
| P3 - P0 | share_open | higher | pre-specified | 0.1257 | 0.0152 | 0.2378 | 0.0240 | 0.0960 | opposite |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -2.2160 | -3.0861 | -1.3802 | 0.0000 | 0.0000 | confirmed |
| P4 - P0 | share_open | higher | pre-specified | 0.0854 | -0.0073 | 0.1782 | 0.0740 | 0.2220 | not confirmed |
| P4 - P0 | med_per_100 | lower | pre-specified | 0.7024 | -0.4686 | 1.8969 | 0.2470 | 0.7410 | not confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.0040 | -1.0380 | 1.0407 | 0.9920 | 0.9920 | not confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | -0.0065 | -1.0023 | 1.0053 | 0.9900 | 1.0000 | not confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | 0.0209 | -0.0588 | 0.1035 | 0.5790 | 0.5790 | not confirmed |
| P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | 0.3155 | 0.1001 | 0.5151 | 0.0080 | 0.0080 | confirmed |
| P5 - P0 | share_open | lower | pre-specified | 0.0037 | -0.1008 | 0.1037 | 0.9030 | 0.9030 | not confirmed |
| P5 - P0 | has_question | lower | pre-specified | 0.0672 | -0.0299 | 0.1642 | 0.1920 | 0.1920 | not confirmed |
| P5 - P0 | plan_statement_present | higher | pre-specified | -0.1119 | -0.2164 | -0.0112 | 0.0300 | 0.0300 | confirmed |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.5983 | 0.5622 | 0.6368 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| overall | P2 | 0.3458 | 0.3159 | 0.3769 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.4925 | 0.4590 | 0.5274 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.6716 | 0.6405 | 0.7002 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.7301 | 0.6990 | 0.7587 | 0.1667 | 1 | 4 | 3 | 0 | not realised |
| Early | P1 | 0.6231 | 0.5671 | 0.6791 | 0.1667 | 1 | 3 | 0 | 0 | not realised |
| Early | P2 | 0.3507 | 0.2947 | 0.4067 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.4851 | 0.4254 | 0.5411 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.7425 | 0.6940 | 0.7948 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 0.6493 | 0.5896 | 0.7052 | 0.1667 | 1 | 4 | 3 | 0 | not realised |
| Middle | P1 | 0.6119 | 0.5522 | 0.6716 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Middle | P2 | 0.3731 | 0.3172 | 0.4291 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.4664 | 0.4030 | 0.5224 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.6940 | 0.6381 | 0.7425 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Middle | P5 | 0.8396 | 0.7948 | 0.8806 | 0.1667 | 1 | 4 | 3 | 0 | not realised |
| Late | P1 | 0.5597 | 0.5000 | 0.6194 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Late | P2 | 0.3134 | 0.2575 | 0.3694 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.5261 | 0.4627 | 0.5858 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Late | P4 | 0.5784 | 0.5149 | 0.6343 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P5 | 0.7015 | 0.6455 | 0.7575 | 0.1667 | 1 | 4 | 3 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.7438 | 804 |
| P0 | overall | plan_statement_present | 0.3669 | 804 |
| P0 | overall | empathy_phrases_present | 0.0037 | 804 |
| P0 | overall | hedge_per_100 | 0.6801 | 804 |
| P0 | overall | n_words | 40.3396 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.9328 | 268 |
| P0 | Early | plan_statement_present | 0.1530 | 268 |
| P0 | Early | empathy_phrases_present | 0.0037 | 268 |
| P0 | Early | hedge_per_100 | 0.6055 | 268 |
| P0 | Early | n_words | 32.6231 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.6940 | 268 |
| P0 | Middle | plan_statement_present | 0.4254 | 268 |
| P0 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P0 | Middle | hedge_per_100 | 0.8470 | 268 |
| P0 | Middle | n_words | 41.5000 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.6045 | 268 |
| P0 | Late | plan_statement_present | 0.5224 | 268 |
| P0 | Late | empathy_phrases_present | 0.0075 | 268 |
| P0 | Late | hedge_per_100 | 0.5877 | 268 |
| P0 | Late | n_words | 46.8955 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.9677 | 804 |
| P1 | overall | plan_statement_present | 0.0373 | 804 |
| P1 | overall | empathy_phrases_present | 0.0000 | 804 |
| P1 | overall | hedge_per_100 | 0.4162 | 804 |
| P1 | overall | n_words | 33.5037 | 804 |
| P1 | overall | persona_distance | 0.5812 | 804 |
| P1 | Early | has_question | 0.9851 | 268 |
| P1 | Early | plan_statement_present | 0.0261 | 268 |
| P1 | Early | empathy_phrases_present | 0.0000 | 268 |
| P1 | Early | hedge_per_100 | 0.5097 | 268 |
| P1 | Early | n_words | 30.2090 | 268 |
| P1 | Early | persona_distance | 0.5059 | 268 |
| P1 | Middle | has_question | 0.9739 | 268 |
| P1 | Middle | plan_statement_present | 0.0299 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P1 | Middle | hedge_per_100 | 0.3540 | 268 |
| P1 | Middle | n_words | 31.9216 | 268 |
| P1 | Middle | persona_distance | 0.6093 | 268 |
| P1 | Late | has_question | 0.9440 | 268 |
| P1 | Late | plan_statement_present | 0.0560 | 268 |
| P1 | Late | empathy_phrases_present | 0.0000 | 268 |
| P1 | Late | hedge_per_100 | 0.3849 | 268 |
| P1 | Late | n_words | 38.3806 | 268 |
| P1 | Late | persona_distance | 0.6283 | 268 |
| P2 | overall | has_question | 0.8669 | 804 |
| P2 | overall | plan_statement_present | 0.1940 | 804 |
| P2 | overall | empathy_phrases_present | 0.0000 | 804 |
| P2 | overall | hedge_per_100 | 0.7858 | 804 |
| P2 | overall | n_words | 43.9602 | 804 |
| P2 | overall | persona_distance | 0.5336 | 804 |
| P2 | Early | has_question | 0.9664 | 268 |
| P2 | Early | plan_statement_present | 0.0784 | 268 |
| P2 | Early | empathy_phrases_present | 0.0000 | 268 |
| P2 | Early | hedge_per_100 | 0.7242 | 268 |
| P2 | Early | n_words | 38.0522 | 268 |
| P2 | Early | persona_distance | 0.4887 | 268 |
| P2 | Middle | has_question | 0.8470 | 268 |
| P2 | Middle | plan_statement_present | 0.2015 | 268 |
| P2 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P2 | Middle | hedge_per_100 | 0.8560 | 268 |
| P2 | Middle | n_words | 43.2761 | 268 |
| P2 | Middle | persona_distance | 0.5543 | 268 |
| P2 | Late | has_question | 0.7873 | 268 |
| P2 | Late | plan_statement_present | 0.3022 | 268 |
| P2 | Late | empathy_phrases_present | 0.0000 | 268 |
| P2 | Late | hedge_per_100 | 0.7773 | 268 |
| P2 | Late | n_words | 50.5522 | 268 |
| P2 | Late | persona_distance | 0.5577 | 268 |
| P3 | overall | has_question | 0.9515 | 804 |
| P3 | overall | plan_statement_present | 0.1405 | 804 |
| P3 | overall | empathy_phrases_present | 0.0174 | 804 |
| P3 | overall | hedge_per_100 | 1.7660 | 804 |
| P3 | overall | n_words | 55.5448 | 804 |
| P3 | overall | persona_distance | 0.5770 | 804 |
| P3 | Early | has_question | 0.9925 | 268 |
| P3 | Early | plan_statement_present | 0.0597 | 268 |
| P3 | Early | empathy_phrases_present | 0.0149 | 268 |
| P3 | Early | hedge_per_100 | 2.2042 | 268 |
| P3 | Early | n_words | 48.0597 | 268 |
| P3 | Early | persona_distance | 0.5548 | 268 |
| P3 | Middle | has_question | 0.9328 | 268 |
| P3 | Middle | plan_statement_present | 0.1791 | 268 |
| P3 | Middle | empathy_phrases_present | 0.0112 | 268 |
| P3 | Middle | hedge_per_100 | 1.7914 | 268 |
| P3 | Middle | n_words | 57.6119 | 268 |
| P3 | Middle | persona_distance | 0.5958 | 268 |
| P3 | Late | has_question | 0.9291 | 268 |
| P3 | Late | plan_statement_present | 0.1828 | 268 |
| P3 | Late | empathy_phrases_present | 0.0261 | 268 |
| P3 | Late | hedge_per_100 | 1.3023 | 268 |
| P3 | Late | n_words | 60.9627 | 268 |
| P3 | Late | persona_distance | 0.5804 | 268 |
| P4 | overall | has_question | 0.9838 | 804 |
| P4 | overall | plan_statement_present | 0.0995 | 804 |
| P4 | overall | empathy_phrases_present | 0.0958 | 804 |
| P4 | overall | hedge_per_100 | 1.6095 | 804 |
| P4 | overall | n_words | 53.1741 | 804 |
| P4 | overall | persona_distance | 0.6048 | 804 |
| P4 | Early | has_question | 1.0000 | 268 |
| P4 | Early | plan_statement_present | 0.0410 | 268 |
| P4 | Early | empathy_phrases_present | 0.1418 | 268 |
| P4 | Early | hedge_per_100 | 1.8437 | 268 |
| P4 | Early | n_words | 49.0672 | 268 |
| P4 | Early | persona_distance | 0.5821 | 268 |
| P4 | Middle | has_question | 0.9851 | 268 |
| P4 | Middle | plan_statement_present | 0.1269 | 268 |
| P4 | Middle | empathy_phrases_present | 0.0858 | 268 |
| P4 | Middle | hedge_per_100 | 1.6668 | 268 |
| P4 | Middle | n_words | 52.9328 | 268 |
| P4 | Middle | persona_distance | 0.6261 | 268 |
| P4 | Late | has_question | 0.9664 | 268 |
| P4 | Late | plan_statement_present | 0.1306 | 268 |
| P4 | Late | empathy_phrases_present | 0.0597 | 268 |
| P4 | Late | hedge_per_100 | 1.3180 | 268 |
| P4 | Late | n_words | 57.5224 | 268 |
| P4 | Late | persona_distance | 0.6061 | 268 |
| P5 | overall | has_question | 0.7052 | 804 |
| P5 | overall | plan_statement_present | 0.6032 | 804 |
| P5 | overall | empathy_phrases_present | 0.0050 | 804 |
| P5 | overall | hedge_per_100 | 0.3213 | 804 |
| P5 | overall | n_words | 48.6828 | 804 |
| P5 | overall | persona_distance | 0.5477 | 804 |
| P5 | Early | has_question | 0.8545 | 268 |
| P5 | Early | plan_statement_present | 0.4291 | 268 |
| P5 | Early | empathy_phrases_present | 0.0037 | 268 |
| P5 | Early | hedge_per_100 | 0.3214 | 268 |
| P5 | Early | n_words | 42.5224 | 268 |
| P5 | Early | persona_distance | 0.5519 | 268 |
| P5 | Middle | has_question | 0.6679 | 268 |
| P5 | Middle | plan_statement_present | 0.6940 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0037 | 268 |
| P5 | Middle | hedge_per_100 | 0.2777 | 268 |
| P5 | Middle | n_words | 50.8022 | 268 |
| P5 | Middle | persona_distance | 0.5496 | 268 |
| P5 | Late | has_question | 0.5933 | 268 |
| P5 | Late | plan_statement_present | 0.6866 | 268 |
| P5 | Late | empathy_phrases_present | 0.0075 | 268 |
| P5 | Late | hedge_per_100 | 0.3648 | 268 |
| P5 | Late | n_words | 52.7239 | 268 |
| P5 | Late | persona_distance | 0.5417 | 268 |

## Part D

Part D drops 0 analysed rows with any format flag, leaving 4824. Prediction verdicts changed in 0 of 68 rows. H2 verdicts changed in 0 of 17 rows. Realised flags changed in 0 of 20 rows.

## Problems and assumptions

- The leading-question rule that looks for a sentence starting with "so you" is applied after filler stripping. "so" is itself a filler, so that clause cannot match. It was not changed.
- A6, the distance to the P0 response, is stored as a feature and is excluded from the B4 classifier because it is computed from the labelled P0 output.
- In B4, `share_open` is median-imputed inside each training fold. The imputer is not tuned.
- Sentences are splits on `.`, `!`, and `?`. `n_questions` counts question marks. `n_words` counts the same tokens used for lexicon matching.
- Stopwords are scikit-learn's English list. Echo words are the remaining tokens in the P1-P5 persona texts, not the shared base instruction.
- A lexicon hit is dropped in the echo-free psychosocial score when the matched word is one of those persona content words. Separate phrases can each add a count when they overlap.
- Accuracy and recall intervals resample dialogues on the fixed out-of-fold predictions. They do not refit the classifier.
- Each bootstrap uses NumPy `default_rng(20261002)` on its own.
- Cosine distance is 1 minus the cosine similarity of L2-normalised MiniLM embeddings.
- Package pins are in the plan: scispaCy 0.5.5 with `en_core_sci_sm` 0.5.4, sentence-transformers 3.4.1, and NumPy 1.26.4. The scispaCy build needed that NumPy version.
- Erratum 2 (2026-10-02) adds P5 versus P0 predictions for lower `has_question` and higher `plan_statement_present`. For Gemini and Claude these are exploratory. They are excluded from the realised count.
- Cross-model generalisation is reported in `persona_study/reports/analysis_report_all_models.md`.
- Confusion matrices are in `persona_study/analysis/results/b_confusion.csv` and the figures under `persona_study/analysis/results/figures/`.
