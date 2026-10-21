# gemini measurement report

Plan SHA-256: `c1747f993babaa05f8dd3c99543584d8555cb9212138a92e909972505a210450`
Erratum 1 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) plan SHA-256 before this erratum: `56679285fb538ddfe04723dfadca09a1a34418ff6ba766cc55fa559c86675cc6`
Prompt SHA-256: `5d91f7d1e52d4b6b3ec38d6b05ab9eef8d184113eb9597f52cd52de88bae7999`

No generation was run. Measurements use `analysis_text` only.

## Data

- Output rows: 4824
- Missing `analysis_text`: 0. Those rows stay in the feature file and are excluded from calculations.
- Rows in the calculations: 4824
- Contexts: 804
- Rows by condition: {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
- Rows by position: {'Early': 1608, 'Late': 1608, 'Middle': 1608}
- Rows with any format flag, among analysed rows: 26
- Persona content words removed for the echo controls: 55

## Part B accuracy

| variant | scope | accuracy | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | 0.4992 | 0.4842 | 0.5145 | 0.1667 | 4824 |
| B1 | Early | 0.4328 | 0.4073 | 0.4590 | 0.1667 | 1608 |
| B1 | Middle | 0.5386 | 0.5131 | 0.5634 | 0.1667 | 1608 |
| B1 | Late | 0.5261 | 0.5025 | 0.5516 | 0.1667 | 1608 |
| B2 | overall | 0.4635 | 0.4484 | 0.4789 | 0.1667 | 4824 |
| B2 | Early | 0.4136 | 0.3893 | 0.4372 | 0.1667 | 1608 |
| B2 | Middle | 0.4888 | 0.4658 | 0.5149 | 0.1667 | 1608 |
| B2 | Late | 0.4882 | 0.4627 | 0.5125 | 0.1667 | 1608 |
| B3 | overall | 0.4946 | 0.4801 | 0.5097 | 0.1667 | 4824 |
| B3 | Early | 0.4310 | 0.4055 | 0.4558 | 0.1667 | 1608 |
| B3 | Middle | 0.5361 | 0.5112 | 0.5603 | 0.1667 | 1608 |
| B3 | Late | 0.5168 | 0.4932 | 0.5423 | 0.1667 | 1608 |
| B4 | overall | 0.4216 | 0.4100 | 0.4341 | 0.1667 | 4824 |
| B4 | Early | 0.3601 | 0.3402 | 0.3800 | 0.1667 | 1608 |
| B4 | Middle | 0.4646 | 0.4428 | 0.4869 | 0.1667 | 1608 |
| B4 | Late | 0.4403 | 0.4198 | 0.4614 | 0.1667 | 1608 |
| B5 | overall | 0.2948 | 0.2844 | 0.3049 | 0.1667 | 4824 |
| B5 | Early | 0.2506 | 0.2332 | 0.2687 | 0.1667 | 1608 |
| B5 | Middle | 0.3389 | 0.3234 | 0.3551 | 0.1667 | 1608 |
| B5 | Late | 0.2948 | 0.2774 | 0.3116 | 0.1667 | 1608 |
| B6 | overall | 0.5821 | 0.5654 | 0.5985 | 0.2000 | 4020 |
| B6 | Early | 0.4985 | 0.4694 | 0.5269 | 0.2000 | 1340 |
| B6 | Middle | 0.6261 | 0.5978 | 0.6530 | 0.2000 | 1340 |
| B6 | Late | 0.6216 | 0.5948 | 0.6485 | 0.2000 | 1340 |
| B7 | overall | 0.6059 | 0.5918 | 0.6198 | 0.2000 | 4824 |
| B7 | Early | 0.5398 | 0.5143 | 0.5641 | 0.2000 | 1608 |
| B7 | Middle | 0.6412 | 0.6175 | 0.6642 | 0.2000 | 1608 |
| B7 | Late | 0.6368 | 0.6132 | 0.6604 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.3545 | 0.3221 | 0.3881 | 0.1667 | 804 |
| B1 | overall | P1 | 0.4440 | 0.4092 | 0.4789 | 0.1667 | 804 |
| B1 | overall | P2 | 0.3197 | 0.2873 | 0.3532 | 0.1667 | 804 |
| B1 | overall | P3 | 0.5137 | 0.4776 | 0.5460 | 0.1667 | 804 |
| B1 | overall | P4 | 0.7201 | 0.6891 | 0.7500 | 0.1667 | 804 |
| B1 | overall | P5 | 0.6430 | 0.6082 | 0.6754 | 0.1667 | 804 |
| B1 | Early | P0 | 0.3097 | 0.2537 | 0.3657 | 0.1667 | 268 |
| B1 | Early | P1 | 0.4366 | 0.3769 | 0.4963 | 0.1667 | 268 |
| B1 | Early | P2 | 0.2873 | 0.2351 | 0.3433 | 0.1667 | 268 |
| B1 | Early | P3 | 0.4664 | 0.4067 | 0.5261 | 0.1667 | 268 |
| B1 | Early | P4 | 0.6567 | 0.6007 | 0.7127 | 0.1667 | 268 |
| B1 | Early | P5 | 0.4403 | 0.3806 | 0.5000 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.3731 | 0.3172 | 0.4328 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.5000 | 0.4402 | 0.5597 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.3134 | 0.2575 | 0.3694 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.5261 | 0.4664 | 0.5821 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.7910 | 0.7425 | 0.8358 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.7276 | 0.6754 | 0.7799 | 0.1667 | 268 |
| B1 | Late | P0 | 0.3806 | 0.3246 | 0.4403 | 0.1667 | 268 |
| B1 | Late | P1 | 0.3955 | 0.3358 | 0.4590 | 0.1667 | 268 |
| B1 | Late | P2 | 0.3582 | 0.3022 | 0.4142 | 0.1667 | 268 |
| B1 | Late | P3 | 0.5485 | 0.4888 | 0.6119 | 0.1667 | 268 |
| B1 | Late | P4 | 0.7127 | 0.6567 | 0.7649 | 0.1667 | 268 |
| B1 | Late | P5 | 0.7612 | 0.7090 | 0.8134 | 0.1667 | 268 |
| B2 | overall | P0 | 0.3520 | 0.3197 | 0.3868 | 0.1667 | 804 |
| B2 | overall | P1 | 0.4378 | 0.4030 | 0.4714 | 0.1667 | 804 |
| B2 | overall | P2 | 0.3060 | 0.2736 | 0.3383 | 0.1667 | 804 |
| B2 | overall | P3 | 0.4042 | 0.3706 | 0.4391 | 0.1667 | 804 |
| B2 | overall | P4 | 0.6567 | 0.6194 | 0.6915 | 0.1667 | 804 |
| B2 | overall | P5 | 0.6244 | 0.5883 | 0.6580 | 0.1667 | 804 |
| B2 | Early | P0 | 0.3246 | 0.2687 | 0.3806 | 0.1667 | 268 |
| B2 | Early | P1 | 0.4776 | 0.4178 | 0.5373 | 0.1667 | 268 |
| B2 | Early | P2 | 0.2761 | 0.2239 | 0.3284 | 0.1667 | 268 |
| B2 | Early | P3 | 0.3470 | 0.2910 | 0.4030 | 0.1667 | 268 |
| B2 | Early | P4 | 0.6007 | 0.5410 | 0.6567 | 0.1667 | 268 |
| B2 | Early | P5 | 0.4552 | 0.3955 | 0.5149 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.3433 | 0.2873 | 0.4030 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.4664 | 0.4067 | 0.5261 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.2761 | 0.2239 | 0.3284 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.4291 | 0.3731 | 0.4888 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.7015 | 0.6455 | 0.7575 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.7164 | 0.6604 | 0.7687 | 0.1667 | 268 |
| B2 | Late | P0 | 0.3881 | 0.3321 | 0.4478 | 0.1667 | 268 |
| B2 | Late | P1 | 0.3694 | 0.3134 | 0.4254 | 0.1667 | 268 |
| B2 | Late | P2 | 0.3657 | 0.3097 | 0.4216 | 0.1667 | 268 |
| B2 | Late | P3 | 0.4366 | 0.3769 | 0.4963 | 0.1667 | 268 |
| B2 | Late | P4 | 0.6679 | 0.6082 | 0.7239 | 0.1667 | 268 |
| B2 | Late | P5 | 0.7015 | 0.6455 | 0.7537 | 0.1667 | 268 |
| B3 | overall | P0 | 0.3545 | 0.3234 | 0.3868 | 0.1667 | 804 |
| B3 | overall | P1 | 0.4328 | 0.3980 | 0.4677 | 0.1667 | 804 |
| B3 | overall | P2 | 0.3085 | 0.2774 | 0.3408 | 0.1667 | 804 |
| B3 | overall | P3 | 0.5162 | 0.4813 | 0.5485 | 0.1667 | 804 |
| B3 | overall | P4 | 0.7127 | 0.6816 | 0.7438 | 0.1667 | 804 |
| B3 | overall | P5 | 0.6430 | 0.6070 | 0.6766 | 0.1667 | 804 |
| B3 | Early | P0 | 0.3022 | 0.2463 | 0.3582 | 0.1667 | 268 |
| B3 | Early | P1 | 0.4291 | 0.3694 | 0.4888 | 0.1667 | 268 |
| B3 | Early | P2 | 0.2873 | 0.2351 | 0.3396 | 0.1667 | 268 |
| B3 | Early | P3 | 0.4701 | 0.4104 | 0.5299 | 0.1667 | 268 |
| B3 | Early | P4 | 0.6493 | 0.5933 | 0.7052 | 0.1667 | 268 |
| B3 | Early | P5 | 0.4478 | 0.3843 | 0.5075 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.3731 | 0.3172 | 0.4328 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.4888 | 0.4291 | 0.5485 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.3022 | 0.2500 | 0.3545 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.5299 | 0.4701 | 0.5896 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.7948 | 0.7462 | 0.8396 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.7276 | 0.6716 | 0.7799 | 0.1667 | 268 |
| B3 | Late | P0 | 0.3881 | 0.3321 | 0.4478 | 0.1667 | 268 |
| B3 | Late | P1 | 0.3806 | 0.3246 | 0.4403 | 0.1667 | 268 |
| B3 | Late | P2 | 0.3358 | 0.2836 | 0.3919 | 0.1667 | 268 |
| B3 | Late | P3 | 0.5485 | 0.4888 | 0.6082 | 0.1667 | 268 |
| B3 | Late | P4 | 0.6940 | 0.6381 | 0.7500 | 0.1667 | 268 |
| B3 | Late | P5 | 0.7537 | 0.7015 | 0.8060 | 0.1667 | 268 |
| B4 | overall | P0 | 0.0958 | 0.0759 | 0.1169 | 0.1667 | 804 |
| B4 | overall | P1 | 0.7450 | 0.7114 | 0.7786 | 0.1667 | 804 |
| B4 | overall | P2 | 0.1256 | 0.1020 | 0.1505 | 0.1667 | 804 |
| B4 | overall | P3 | 0.3905 | 0.3557 | 0.4254 | 0.1667 | 804 |
| B4 | overall | P4 | 0.6928 | 0.6604 | 0.7264 | 0.1667 | 804 |
| B4 | overall | P5 | 0.4801 | 0.4453 | 0.5149 | 0.1667 | 804 |
| B4 | Early | P0 | 0.0597 | 0.0336 | 0.0896 | 0.1667 | 268 |
| B4 | Early | P1 | 0.7425 | 0.6903 | 0.7948 | 0.1667 | 268 |
| B4 | Early | P2 | 0.1306 | 0.0896 | 0.1716 | 0.1667 | 268 |
| B4 | Early | P3 | 0.4179 | 0.3582 | 0.4776 | 0.1667 | 268 |
| B4 | Early | P4 | 0.5970 | 0.5373 | 0.6567 | 0.1667 | 268 |
| B4 | Early | P5 | 0.2127 | 0.1642 | 0.2649 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.0858 | 0.0522 | 0.1194 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.8321 | 0.7836 | 0.8769 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.1306 | 0.0933 | 0.1717 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.3881 | 0.3321 | 0.4478 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.7761 | 0.7239 | 0.8284 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.5746 | 0.5187 | 0.6343 | 0.1667 | 268 |
| B4 | Late | P0 | 0.1418 | 0.1045 | 0.1828 | 0.1667 | 268 |
| B4 | Late | P1 | 0.6604 | 0.6007 | 0.7127 | 0.1667 | 268 |
| B4 | Late | P2 | 0.1157 | 0.0784 | 0.1530 | 0.1667 | 268 |
| B4 | Late | P3 | 0.3657 | 0.3097 | 0.4216 | 0.1667 | 268 |
| B4 | Late | P4 | 0.7052 | 0.6493 | 0.7612 | 0.1667 | 268 |
| B4 | Late | P5 | 0.6530 | 0.5970 | 0.7090 | 0.1667 | 268 |
| B5 | overall | P0 | 0.0224 | 0.0124 | 0.0336 | 0.1667 | 804 |
| B5 | overall | P1 | 0.6729 | 0.6418 | 0.7065 | 0.1667 | 804 |
| B5 | overall | P2 | 0.0821 | 0.0647 | 0.1020 | 0.1667 | 804 |
| B5 | overall | P3 | 0.1119 | 0.0896 | 0.1356 | 0.1667 | 804 |
| B5 | overall | P4 | 0.6530 | 0.6219 | 0.6841 | 0.1667 | 804 |
| B5 | overall | P5 | 0.2264 | 0.1990 | 0.2537 | 0.1667 | 804 |
| B5 | Early | P0 | 0.0336 | 0.0149 | 0.0597 | 0.1667 | 268 |
| B5 | Early | P1 | 0.6940 | 0.6381 | 0.7463 | 0.1667 | 268 |
| B5 | Early | P2 | 0.1045 | 0.0672 | 0.1418 | 0.1667 | 268 |
| B5 | Early | P3 | 0.1343 | 0.0970 | 0.1791 | 0.1667 | 268 |
| B5 | Early | P4 | 0.3881 | 0.3284 | 0.4440 | 0.1667 | 268 |
| B5 | Early | P5 | 0.1493 | 0.1082 | 0.1940 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.0187 | 0.0037 | 0.0373 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.7500 | 0.7015 | 0.8022 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.0970 | 0.0634 | 0.1343 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.1269 | 0.0858 | 0.1642 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.7649 | 0.7127 | 0.8172 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.2761 | 0.2239 | 0.3321 | 0.1667 | 268 |
| B5 | Late | P0 | 0.0149 | 0.0037 | 0.0299 | 0.1667 | 268 |
| B5 | Late | P1 | 0.5746 | 0.5186 | 0.6306 | 0.1667 | 268 |
| B5 | Late | P2 | 0.0448 | 0.0224 | 0.0709 | 0.1667 | 268 |
| B5 | Late | P3 | 0.0746 | 0.0448 | 0.1082 | 0.1667 | 268 |
| B5 | Late | P4 | 0.8060 | 0.7575 | 0.8545 | 0.1667 | 268 |
| B5 | Late | P5 | 0.2537 | 0.2015 | 0.3060 | 0.1667 | 268 |
| B6 | overall | P1 | 0.5224 | 0.4851 | 0.5560 | 0.2000 | 804 |
| B6 | overall | P2 | 0.4478 | 0.4142 | 0.4826 | 0.2000 | 804 |
| B6 | overall | P3 | 0.5535 | 0.5174 | 0.5858 | 0.2000 | 804 |
| B6 | overall | P4 | 0.7239 | 0.6940 | 0.7537 | 0.2000 | 804 |
| B6 | overall | P5 | 0.6629 | 0.6281 | 0.6953 | 0.2000 | 804 |
| B6 | Early | P1 | 0.4963 | 0.4366 | 0.5560 | 0.2000 | 268 |
| B6 | Early | P2 | 0.3619 | 0.3060 | 0.4216 | 0.2000 | 268 |
| B6 | Early | P3 | 0.4963 | 0.4366 | 0.5560 | 0.2000 | 268 |
| B6 | Early | P4 | 0.6642 | 0.6082 | 0.7201 | 0.2000 | 268 |
| B6 | Early | P5 | 0.4739 | 0.4141 | 0.5336 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.5746 | 0.5149 | 0.6343 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.4478 | 0.3881 | 0.5075 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.5634 | 0.5075 | 0.6231 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.7985 | 0.7500 | 0.8433 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.7463 | 0.6940 | 0.7948 | 0.2000 | 268 |
| B6 | Late | P1 | 0.4963 | 0.4328 | 0.5560 | 0.2000 | 268 |
| B6 | Late | P2 | 0.5336 | 0.4776 | 0.5970 | 0.2000 | 268 |
| B6 | Late | P3 | 0.6007 | 0.5410 | 0.6604 | 0.2000 | 268 |
| B6 | Late | P4 | 0.7090 | 0.6530 | 0.7612 | 0.2000 | 268 |
| B6 | Late | P5 | 0.7687 | 0.7164 | 0.8172 | 0.2000 | 268 |
| B7 | overall | P0 | 0.2699 | 0.2400 | 0.3022 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.7674 | 0.7450 | 0.7892 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.4963 | 0.4614 | 0.5299 | 0.2000 | 804 |
| B7 | overall | P4 | 0.7177 | 0.6866 | 0.7475 | 0.2000 | 804 |
| B7 | overall | P5 | 0.6169 | 0.5821 | 0.6493 | 0.2000 | 804 |
| B7 | Early | P0 | 0.2052 | 0.1567 | 0.2537 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.7743 | 0.7369 | 0.8116 | 0.2000 | 536 |
| B7 | Early | P3 | 0.4291 | 0.3657 | 0.4888 | 0.2000 | 268 |
| B7 | Early | P4 | 0.6530 | 0.5970 | 0.7127 | 0.2000 | 268 |
| B7 | Early | P5 | 0.4030 | 0.3396 | 0.4627 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.2724 | 0.2238 | 0.3284 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.7761 | 0.7388 | 0.8116 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.5224 | 0.4664 | 0.5821 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.7910 | 0.7425 | 0.8358 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.7090 | 0.6567 | 0.7612 | 0.2000 | 268 |
| B7 | Late | P0 | 0.3321 | 0.2799 | 0.3918 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.7519 | 0.7146 | 0.7873 | 0.2000 | 536 |
| B7 | Late | P3 | 0.5373 | 0.4776 | 0.5970 | 0.2000 | 268 |
| B7 | Late | P4 | 0.7090 | 0.6530 | 0.7612 | 0.2000 | 268 |
| B7 | Late | P5 | 0.7388 | 0.6866 | 0.7910 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | -1.3667 | 0.3829 | 0.0004 | -2.1172 | -0.6161 |
| C(position, Treatment(reference='Early'))[T.Late] | 0.1092 | 0.1238 | 0.3778 | -0.1335 | 0.3519 |
| C(position, Treatment(reference='Early'))[T.Middle] | 0.2447 | 0.1031 | 0.0177 | 0.0425 | 0.4468 |
| log_context | 0.1975 | 0.0693 | 0.0044 | 0.0617 | 0.3334 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.4540 | -0.6629 | -0.2490 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.3579 | -0.6221 | -0.1081 | 0.0050 | 0.0250 | 268 | confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.4346 | -0.8071 | -0.0669 | 0.0200 | 0.0600 | 268 | confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.5694 | -0.9504 | -0.1730 | 0.0010 | 0.0060 | 268 | confirmed |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | 0.9479 | 0.1819 | 1.7332 | 0.0190 | 0.0190 | 804 | confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | 0.8643 | -0.5377 | 2.2426 | 0.2430 | 0.3120 | 268 | not confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | 1.1379 | -0.1554 | 2.3937 | 0.0860 | 0.2580 | 268 | not confirmed |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | 0.8416 | -0.2999 | 2.0378 | 0.1560 | 0.3120 | 268 | not confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | -0.0089 | -0.0397 | 0.0203 | 0.5420 | 0.7840 | 637 | not confirmed |
| Early | P1 - P0 | share_open | lower | pre-specified | -0.0411 | -0.0889 | 0.0090 | 0.1150 | 0.6900 | 223 | not confirmed |
| Middle | P1 - P0 | share_open | lower | pre-specified | 0.0357 | -0.0090 | 0.0871 | 0.1350 | 0.6900 | 224 | not confirmed |
| Late | P1 - P0 | share_open | lower | pre-specified | -0.0237 | -0.0816 | 0.0316 | 0.4270 | 1.0000 | 190 | not confirmed |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.3176 | 0.1414 | 0.4882 | 0.0010 | 0.0010 | 804 | confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1627 | -0.0704 | 0.3838 | 0.1730 | 0.2540 | 268 | not confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.2266 | -0.0665 | 0.5090 | 0.1270 | 0.2540 | 268 | not confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.5634 | 0.1861 | 0.9422 | 0.0050 | 0.0250 | 268 | confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.2341 | 0.9804 | 1.4918 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.0551 | 0.7207 | 1.3981 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.2188 | 0.7433 | 1.6666 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.4284 | 0.9834 | 1.9031 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.1637 | 0.1289 | 0.1985 | 0.0000 | 0.0000 | 612 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.1051 | 0.0474 | 0.1602 | 0.0010 | 0.0070 | 218 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.2110 | 0.1489 | 0.2689 | 0.0000 | 0.0000 | 207 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.1796 | 0.1101 | 0.2451 | 0.0000 | 0.0000 | 187 | confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 3.6824 | 3.3998 | 3.9866 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 3.6778 | 3.1809 | 4.2037 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 4.0073 | 3.5069 | 4.4883 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 3.3622 | 2.8863 | 3.8358 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.3907 | 0.3534 | 0.4326 | 0.0000 | 0.0000 | 610 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.2976 | 0.2366 | 0.3571 | 0.0000 | 0.0000 | 224 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.4909 | 0.4266 | 0.5545 | 0.0000 | 0.0000 | 202 | confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | 0.3940 | 0.3207 | 0.4665 | 0.0000 | 0.0000 | 184 | confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -7.0245 | -7.7202 | -6.3842 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -6.5596 | -7.7482 | -5.3846 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -8.4119 | -9.5679 | -7.2214 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -6.1019 | -7.1506 | -5.1018 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.4483 | 2.1540 | 2.7266 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.6227 | 2.1050 | 3.1827 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.7885 | 2.2822 | 3.2940 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.9338 | 1.4255 | 2.3958 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -2.9852 | -3.5301 | -2.4283 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -2.8507 | -3.8942 | -1.8708 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -3.1233 | -4.0213 | -2.2135 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -2.9814 | -3.8492 | -2.1197 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1595 | 0.1033 | 0.2247 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1220 | 0.0436 | 0.2308 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1710 | 0.0654 | 0.2936 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1855 | 0.0846 | 0.2974 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | -0.0100 | -0.0199 | 0.0000 | 0.0900 | 0.0900 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | -0.0075 | -0.0224 | 0.0075 | 0.4470 | 0.8940 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | -0.0149 | -0.0410 | 0.0075 | 0.2800 | 0.8400 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | -0.0075 | -0.0224 | 0.0075 | 0.4590 | 0.8940 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0068 | -0.0073 | 0.0257 | 0.4650 | 0.4650 | 804 | not confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0271 | -0.0138 | 0.0830 | 0.3310 | 0.7860 | 268 | not confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0068 | -0.0176 | 0.0000 | 0.2620 | 0.7860 | 268 | not confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | -0.0142 | -0.0476 | 0.0191 | 0.3920 | 0.7840 | 387 | not confirmed |
| Early | P5 - P0 | share_open | lower | pre-specified | -0.0125 | -0.0642 | 0.0383 | 0.6690 | 1.0000 | 187 | not confirmed |
| Middle | P5 - P0 | share_open | lower | pre-specified | -0.0182 | -0.0757 | 0.0378 | 0.5640 | 1.0000 | 119 | not confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | -0.0123 | -0.0802 | 0.0556 | 0.8160 | 1.0000 | 81 | not confirmed |
| overall | P5 - P0 | has_question | lower | exploratory | -0.3321 | -0.3682 | -0.2973 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | has_question | lower | exploratory | -0.1642 | -0.2164 | -0.1157 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | has_question | lower | exploratory | -0.3881 | -0.4478 | -0.3284 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | has_question | lower | exploratory | -0.4440 | -0.5112 | -0.3806 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | plan_statement_present | higher | exploratory | 0.2873 | 0.2562 | 0.3209 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | exploratory | 0.1119 | 0.0709 | 0.1568 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | exploratory | 0.3955 | 0.3395 | 0.4590 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | exploratory | 0.3545 | 0.2872 | 0.4217 | 0.0000 | 0.0000 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.2115 | -0.6585 | 0.2546 | 0.4000 | 0.7820 | not confirmed |
| P1 - P0 | med_per_100 | higher | pre-specified | -0.0227 | -1.7413 | 1.7709 | 0.9840 | 1.0000 | not confirmed |
| P1 - P0 | share_open | lower | pre-specified | 0.0174 | -0.0583 | 0.0907 | 0.6670 | 1.0000 | not confirmed |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.4007 | -0.0697 | 0.8395 | 0.0970 | 0.3880 | not confirmed |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.3733 | -0.1547 | 0.9147 | 0.1500 | 0.4500 | not confirmed |
| P3 - P0 | share_open | higher | pre-specified | 0.0745 | -0.0169 | 0.1580 | 0.1140 | 0.3420 | not confirmed |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -0.3156 | -1.0019 | 0.3437 | 0.3910 | 0.7820 | not confirmed |
| P4 - P0 | share_open | higher | pre-specified | 0.0964 | 0.0046 | 0.1867 | 0.0400 | 0.1600 | opposite |
| P4 - P0 | med_per_100 | lower | pre-specified | 0.4577 | -1.0495 | 2.0102 | 0.5490 | 1.0000 | not confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.6889 | -1.4321 | 0.0190 | 0.0620 | 0.3100 | not confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | -0.1307 | -1.5137 | 1.2443 | 0.8600 | 1.0000 | not confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | 0.0635 | -0.0802 | 0.2071 | 0.3810 | 0.3810 | not confirmed |
| P5 - P0 | n_leading | higher | pre-specified | 0.0000 | -0.0224 | 0.0224 | 1.0000 | 1.0000 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0338 | -0.0901 | 0.0071 | 0.1590 | 0.1590 | not confirmed |
| P5 - P0 | share_open | lower | pre-specified | 0.0001 | -0.0849 | 0.0885 | 1.0000 | 1.0000 | not confirmed |
| P5 - P0 | has_question | lower | exploratory | -0.2799 | -0.3619 | -0.1978 | 0.0000 | 0.0000 | opposite |
| P5 - P0 | plan_statement_present | higher | exploratory | 0.2425 | 0.1567 | 0.3284 | 0.0000 | 0.0000 | opposite |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.4440 | 0.4092 | 0.4789 | 0.1667 | 1 | 3 | 2 | 0 | not realised |
| overall | P2 | 0.3197 | 0.2873 | 0.3532 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.5137 | 0.4776 | 0.5460 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.7201 | 0.6891 | 0.7500 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.6430 | 0.6082 | 0.6754 | 0.1667 | 1 | 4 | 1 | 0 | not realised |
| Early | P1 | 0.4366 | 0.3769 | 0.4963 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Early | P2 | 0.2873 | 0.2351 | 0.3433 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.4664 | 0.4067 | 0.5261 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.6567 | 0.6007 | 0.7127 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 0.4403 | 0.3806 | 0.5000 | 0.1667 | 1 | 4 | 1 | 0 | not realised |
| Middle | P1 | 0.5000 | 0.4402 | 0.5597 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Middle | P2 | 0.3134 | 0.2575 | 0.3694 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.5261 | 0.4664 | 0.5821 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.7910 | 0.7425 | 0.8358 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Middle | P5 | 0.7276 | 0.6754 | 0.7799 | 0.1667 | 1 | 4 | 1 | 0 | not realised |
| Late | P1 | 0.3955 | 0.3358 | 0.4590 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Late | P2 | 0.3582 | 0.3022 | 0.4142 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.5485 | 0.4888 | 0.6119 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Late | P4 | 0.7127 | 0.6567 | 0.7649 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P5 | 0.7612 | 0.7090 | 0.8134 | 0.1667 | 1 | 4 | 1 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.9353 | 804 |
| P0 | overall | plan_statement_present | 0.1057 | 804 |
| P0 | overall | empathy_phrases_present | 0.0224 | 804 |
| P0 | overall | hedge_per_100 | 0.2037 | 804 |
| P0 | overall | n_words | 31.0274 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.9925 | 268 |
| P0 | Early | plan_statement_present | 0.0261 | 268 |
| P0 | Early | empathy_phrases_present | 0.0187 | 268 |
| P0 | Early | hedge_per_100 | 0.1757 | 268 |
| P0 | Early | n_words | 19.0299 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.9328 | 268 |
| P0 | Middle | plan_statement_present | 0.0970 | 268 |
| P0 | Middle | empathy_phrases_present | 0.0224 | 268 |
| P0 | Middle | hedge_per_100 | 0.1542 | 268 |
| P0 | Middle | n_words | 29.9216 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.8806 | 268 |
| P0 | Late | plan_statement_present | 0.1940 | 268 |
| P0 | Late | empathy_phrases_present | 0.0261 | 268 |
| P0 | Late | hedge_per_100 | 0.2812 | 268 |
| P0 | Late | n_words | 44.1306 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.9677 | 804 |
| P1 | overall | plan_statement_present | 0.0211 | 804 |
| P1 | overall | empathy_phrases_present | 0.0025 | 804 |
| P1 | overall | hedge_per_100 | 0.0680 | 804 |
| P1 | overall | n_words | 20.9490 | 804 |
| P1 | overall | persona_distance | 0.4794 | 804 |
| P1 | Early | has_question | 0.9963 | 268 |
| P1 | Early | plan_statement_present | 0.0000 | 268 |
| P1 | Early | empathy_phrases_present | 0.0037 | 268 |
| P1 | Early | hedge_per_100 | 0.0704 | 268 |
| P1 | Early | n_words | 14.6716 | 268 |
| P1 | Early | persona_distance | 0.4194 | 268 |
| P1 | Middle | has_question | 0.9925 | 268 |
| P1 | Middle | plan_statement_present | 0.0149 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P1 | Middle | hedge_per_100 | 0.0598 | 268 |
| P1 | Middle | n_words | 15.8470 | 268 |
| P1 | Middle | persona_distance | 0.4965 | 268 |
| P1 | Late | has_question | 0.9142 | 268 |
| P1 | Late | plan_statement_present | 0.0485 | 268 |
| P1 | Late | empathy_phrases_present | 0.0037 | 268 |
| P1 | Late | hedge_per_100 | 0.0738 | 268 |
| P1 | Late | n_words | 32.3284 | 268 |
| P1 | Late | persona_distance | 0.5223 | 268 |
| P2 | overall | has_question | 0.9677 | 804 |
| P2 | overall | plan_statement_present | 0.0336 | 804 |
| P2 | overall | empathy_phrases_present | 0.0286 | 804 |
| P2 | overall | hedge_per_100 | 0.1229 | 804 |
| P2 | overall | n_words | 28.6381 | 804 |
| P2 | overall | persona_distance | 0.4618 | 804 |
| P2 | Early | has_question | 1.0000 | 268 |
| P2 | Early | plan_statement_present | 0.0000 | 268 |
| P2 | Early | empathy_phrases_present | 0.0373 | 268 |
| P2 | Early | hedge_per_100 | 0.0000 | 268 |
| P2 | Early | n_words | 16.7201 | 268 |
| P2 | Early | persona_distance | 0.4198 | 268 |
| P2 | Middle | has_question | 0.9701 | 268 |
| P2 | Middle | plan_statement_present | 0.0373 | 268 |
| P2 | Middle | empathy_phrases_present | 0.0187 | 268 |
| P2 | Middle | hedge_per_100 | 0.1367 | 268 |
| P2 | Middle | n_words | 24.9552 | 268 |
| P2 | Middle | persona_distance | 0.4723 | 268 |
| P2 | Late | has_question | 0.9328 | 268 |
| P2 | Late | plan_statement_present | 0.0634 | 268 |
| P2 | Late | empathy_phrases_present | 0.0299 | 268 |
| P2 | Late | hedge_per_100 | 0.2319 | 268 |
| P2 | Late | n_words | 44.2388 | 268 |
| P2 | Late | persona_distance | 0.4931 | 268 |
| P3 | overall | has_question | 0.9751 | 804 |
| P3 | overall | plan_statement_present | 0.0609 | 804 |
| P3 | overall | empathy_phrases_present | 0.2488 | 804 |
| P3 | overall | hedge_per_100 | 0.5962 | 804 |
| P3 | overall | n_words | 52.3284 | 804 |
| P3 | overall | persona_distance | 0.4956 | 804 |
| P3 | Early | has_question | 0.9963 | 268 |
| P3 | Early | plan_statement_present | 0.0149 | 268 |
| P3 | Early | empathy_phrases_present | 0.1903 | 268 |
| P3 | Early | hedge_per_100 | 0.5541 | 268 |
| P3 | Early | n_words | 35.3694 | 268 |
| P3 | Early | persona_distance | 0.4719 | 268 |
| P3 | Middle | has_question | 0.9888 | 268 |
| P3 | Middle | plan_statement_present | 0.0410 | 268 |
| P3 | Middle | empathy_phrases_present | 0.2313 | 268 |
| P3 | Middle | hedge_per_100 | 0.6698 | 268 |
| P3 | Middle | n_words | 53.6604 | 268 |
| P3 | Middle | persona_distance | 0.5044 | 268 |
| P3 | Late | has_question | 0.9403 | 268 |
| P3 | Late | plan_statement_present | 0.1269 | 268 |
| P3 | Late | empathy_phrases_present | 0.3246 | 268 |
| P3 | Late | hedge_per_100 | 0.5648 | 268 |
| P3 | Late | n_words | 67.9552 | 268 |
| P3 | Late | persona_distance | 0.5105 | 268 |
| P4 | overall | has_question | 0.9577 | 804 |
| P4 | overall | plan_statement_present | 0.0560 | 804 |
| P4 | overall | empathy_phrases_present | 0.4229 | 804 |
| P4 | overall | hedge_per_100 | 0.7848 | 804 |
| P4 | overall | n_words | 52.6045 | 804 |
| P4 | overall | persona_distance | 0.5786 | 804 |
| P4 | Early | has_question | 0.9851 | 268 |
| P4 | Early | plan_statement_present | 0.0149 | 268 |
| P4 | Early | empathy_phrases_present | 0.3060 | 268 |
| P4 | Early | hedge_per_100 | 0.7139 | 268 |
| P4 | Early | n_words | 37.4179 | 268 |
| P4 | Early | persona_distance | 0.5611 | 268 |
| P4 | Middle | has_question | 0.9590 | 268 |
| P4 | Middle | plan_statement_present | 0.0448 | 268 |
| P4 | Middle | empathy_phrases_present | 0.4440 | 268 |
| P4 | Middle | hedge_per_100 | 0.8434 | 268 |
| P4 | Middle | n_words | 56.8134 | 268 |
| P4 | Middle | persona_distance | 0.5995 | 268 |
| P4 | Late | has_question | 0.9291 | 268 |
| P4 | Late | plan_statement_present | 0.1082 | 268 |
| P4 | Late | empathy_phrases_present | 0.5187 | 268 |
| P4 | Late | hedge_per_100 | 0.7973 | 268 |
| P4 | Late | n_words | 63.5821 | 268 |
| P4 | Late | persona_distance | 0.5751 | 268 |
| P5 | overall | has_question | 0.6032 | 804 |
| P5 | overall | plan_statement_present | 0.3930 | 804 |
| P5 | overall | empathy_phrases_present | 0.0473 | 804 |
| P5 | overall | hedge_per_100 | 0.0845 | 804 |
| P5 | overall | n_words | 26.9042 | 804 |
| P5 | overall | persona_distance | 0.5572 | 804 |
| P5 | Early | has_question | 0.8284 | 268 |
| P5 | Early | plan_statement_present | 0.1381 | 268 |
| P5 | Early | empathy_phrases_present | 0.0410 | 268 |
| P5 | Early | hedge_per_100 | 0.1108 | 268 |
| P5 | Early | n_words | 18.4776 | 268 |
| P5 | Early | persona_distance | 0.4550 | 268 |
| P5 | Middle | has_question | 0.5448 | 268 |
| P5 | Middle | plan_statement_present | 0.4925 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0634 | 268 |
| P5 | Middle | hedge_per_100 | 0.0811 | 268 |
| P5 | Middle | n_words | 27.6866 | 268 |
| P5 | Middle | persona_distance | 0.5950 | 268 |
| P5 | Late | has_question | 0.4366 | 268 |
| P5 | Late | plan_statement_present | 0.5485 | 268 |
| P5 | Late | empathy_phrases_present | 0.0373 | 268 |
| P5 | Late | hedge_per_100 | 0.0614 | 268 |
| P5 | Late | n_words | 34.5485 | 268 |
| P5 | Late | persona_distance | 0.6214 | 268 |

## Part D

Part D drops 26 analysed rows with any format flag, leaving 4798. Prediction verdicts changed in 0 of 68 rows. H2 verdicts changed in 0 of 17 rows. Realised flags changed in 0 of 20 rows.

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
