# claude measurement report

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
- Rows with any format flag, among analysed rows: 0
- Persona content words removed for the echo controls: 55

## Part B accuracy

| variant | scope | accuracy | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | 0.5659 | 0.5514 | 0.5800 | 0.1667 | 4824 |
| B1 | Early | 0.5535 | 0.5305 | 0.5771 | 0.1667 | 1608 |
| B1 | Middle | 0.5852 | 0.5616 | 0.6095 | 0.1667 | 1608 |
| B1 | Late | 0.5591 | 0.5317 | 0.5852 | 0.1667 | 1608 |
| B2 | overall | 0.4934 | 0.4791 | 0.5066 | 0.1667 | 4824 |
| B2 | Early | 0.4795 | 0.4577 | 0.5019 | 0.1667 | 1608 |
| B2 | Middle | 0.5274 | 0.5037 | 0.5516 | 0.1667 | 1608 |
| B2 | Late | 0.4733 | 0.4478 | 0.4969 | 0.1667 | 1608 |
| B3 | overall | 0.5595 | 0.5450 | 0.5740 | 0.1667 | 4824 |
| B3 | Early | 0.5454 | 0.5224 | 0.5697 | 0.1667 | 1608 |
| B3 | Middle | 0.5802 | 0.5572 | 0.6039 | 0.1667 | 1608 |
| B3 | Late | 0.5529 | 0.5255 | 0.5790 | 0.1667 | 1608 |
| B4 | overall | 0.4233 | 0.4100 | 0.4362 | 0.1667 | 4824 |
| B4 | Early | 0.4117 | 0.3887 | 0.4347 | 0.1667 | 1608 |
| B4 | Middle | 0.4440 | 0.4235 | 0.4646 | 0.1667 | 1608 |
| B4 | Late | 0.4142 | 0.3924 | 0.4378 | 0.1667 | 1608 |
| B5 | overall | 0.3027 | 0.2921 | 0.3132 | 0.1667 | 4824 |
| B5 | Early | 0.2873 | 0.2693 | 0.3066 | 0.1667 | 1608 |
| B5 | Middle | 0.3420 | 0.3240 | 0.3601 | 0.1667 | 1608 |
| B5 | Late | 0.2786 | 0.2631 | 0.2942 | 0.1667 | 1608 |
| B6 | overall | 0.6351 | 0.6194 | 0.6500 | 0.2000 | 4020 |
| B6 | Early | 0.6231 | 0.5970 | 0.6470 | 0.2000 | 1340 |
| B6 | Middle | 0.6657 | 0.6425 | 0.6896 | 0.2000 | 1340 |
| B6 | Late | 0.6164 | 0.5896 | 0.6440 | 0.2000 | 1340 |
| B7 | overall | 0.6335 | 0.6190 | 0.6484 | 0.2000 | 4824 |
| B7 | Early | 0.6269 | 0.6057 | 0.6474 | 0.2000 | 1608 |
| B7 | Middle | 0.6567 | 0.6325 | 0.6810 | 0.2000 | 1608 |
| B7 | Late | 0.6169 | 0.5896 | 0.6437 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.4540 | 0.4166 | 0.4888 | 0.1667 | 804 |
| B1 | overall | P1 | 0.6169 | 0.5808 | 0.6505 | 0.1667 | 804 |
| B1 | overall | P2 | 0.3296 | 0.2973 | 0.3632 | 0.1667 | 804 |
| B1 | overall | P3 | 0.5908 | 0.5597 | 0.6219 | 0.1667 | 804 |
| B1 | overall | P4 | 0.7488 | 0.7164 | 0.7799 | 0.1667 | 804 |
| B1 | overall | P5 | 0.6555 | 0.6219 | 0.6915 | 0.1667 | 804 |
| B1 | Early | P0 | 0.3619 | 0.3022 | 0.4216 | 0.1667 | 268 |
| B1 | Early | P1 | 0.6940 | 0.6381 | 0.7463 | 0.1667 | 268 |
| B1 | Early | P2 | 0.3284 | 0.2724 | 0.3843 | 0.1667 | 268 |
| B1 | Early | P3 | 0.5709 | 0.5112 | 0.6306 | 0.1667 | 268 |
| B1 | Early | P4 | 0.7724 | 0.7201 | 0.8209 | 0.1667 | 268 |
| B1 | Early | P5 | 0.5933 | 0.5336 | 0.6530 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.4590 | 0.3993 | 0.5187 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.6381 | 0.5784 | 0.6940 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.2985 | 0.2463 | 0.3545 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.6530 | 0.5970 | 0.7090 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.8022 | 0.7537 | 0.8470 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 268 |
| B1 | Late | P0 | 0.5410 | 0.4813 | 0.6007 | 0.1667 | 268 |
| B1 | Late | P1 | 0.5187 | 0.4552 | 0.5784 | 0.1667 | 268 |
| B1 | Late | P2 | 0.3619 | 0.3060 | 0.4179 | 0.1667 | 268 |
| B1 | Late | P3 | 0.5485 | 0.4888 | 0.6082 | 0.1667 | 268 |
| B1 | Late | P4 | 0.6716 | 0.6157 | 0.7276 | 0.1667 | 268 |
| B1 | Late | P5 | 0.7127 | 0.6567 | 0.7687 | 0.1667 | 268 |
| B2 | overall | P0 | 0.4055 | 0.3731 | 0.4391 | 0.1667 | 804 |
| B2 | overall | P1 | 0.6095 | 0.5734 | 0.6443 | 0.1667 | 804 |
| B2 | overall | P2 | 0.2575 | 0.2276 | 0.2873 | 0.1667 | 804 |
| B2 | overall | P3 | 0.4378 | 0.4030 | 0.4726 | 0.1667 | 804 |
| B2 | overall | P4 | 0.6617 | 0.6294 | 0.6953 | 0.1667 | 804 |
| B2 | overall | P5 | 0.5883 | 0.5547 | 0.6231 | 0.1667 | 804 |
| B2 | Early | P0 | 0.3619 | 0.3060 | 0.4216 | 0.1667 | 268 |
| B2 | Early | P1 | 0.6754 | 0.6194 | 0.7313 | 0.1667 | 268 |
| B2 | Early | P2 | 0.2239 | 0.1754 | 0.2761 | 0.1667 | 268 |
| B2 | Early | P3 | 0.3619 | 0.3060 | 0.4216 | 0.1667 | 268 |
| B2 | Early | P4 | 0.6567 | 0.6007 | 0.7127 | 0.1667 | 268 |
| B2 | Early | P5 | 0.5970 | 0.5373 | 0.6567 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.4030 | 0.3433 | 0.4627 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.6381 | 0.5821 | 0.6940 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.2836 | 0.2313 | 0.3396 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.4925 | 0.4291 | 0.5522 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.7351 | 0.6828 | 0.7910 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.6119 | 0.5560 | 0.6716 | 0.1667 | 268 |
| B2 | Late | P0 | 0.4515 | 0.3918 | 0.5112 | 0.1667 | 268 |
| B2 | Late | P1 | 0.5149 | 0.4515 | 0.5746 | 0.1667 | 268 |
| B2 | Late | P2 | 0.2649 | 0.2127 | 0.3209 | 0.1667 | 268 |
| B2 | Late | P3 | 0.4590 | 0.4030 | 0.5224 | 0.1667 | 268 |
| B2 | Late | P4 | 0.5933 | 0.5336 | 0.6493 | 0.1667 | 268 |
| B2 | Late | P5 | 0.5560 | 0.4963 | 0.6194 | 0.1667 | 268 |
| B3 | overall | P0 | 0.4478 | 0.4104 | 0.4838 | 0.1667 | 804 |
| B3 | overall | P1 | 0.5970 | 0.5609 | 0.6294 | 0.1667 | 804 |
| B3 | overall | P2 | 0.3308 | 0.2985 | 0.3669 | 0.1667 | 804 |
| B3 | overall | P3 | 0.5808 | 0.5498 | 0.6119 | 0.1667 | 804 |
| B3 | overall | P4 | 0.7550 | 0.7214 | 0.7861 | 0.1667 | 804 |
| B3 | overall | P5 | 0.6455 | 0.6132 | 0.6828 | 0.1667 | 804 |
| B3 | Early | P0 | 0.3657 | 0.3060 | 0.4254 | 0.1667 | 268 |
| B3 | Early | P1 | 0.6903 | 0.6343 | 0.7425 | 0.1667 | 268 |
| B3 | Early | P2 | 0.3172 | 0.2612 | 0.3731 | 0.1667 | 268 |
| B3 | Early | P3 | 0.5560 | 0.4925 | 0.6157 | 0.1667 | 268 |
| B3 | Early | P4 | 0.7761 | 0.7239 | 0.8246 | 0.1667 | 268 |
| B3 | Early | P5 | 0.5672 | 0.5075 | 0.6269 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.4552 | 0.3993 | 0.5149 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.6082 | 0.5485 | 0.6642 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.3097 | 0.2575 | 0.3657 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.6418 | 0.5821 | 0.6978 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.8022 | 0.7537 | 0.8470 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.6642 | 0.6082 | 0.7239 | 0.1667 | 268 |
| B3 | Late | P0 | 0.5224 | 0.4626 | 0.5821 | 0.1667 | 268 |
| B3 | Late | P1 | 0.4925 | 0.4291 | 0.5522 | 0.1667 | 268 |
| B3 | Late | P2 | 0.3657 | 0.3097 | 0.4216 | 0.1667 | 268 |
| B3 | Late | P3 | 0.5448 | 0.4851 | 0.6045 | 0.1667 | 268 |
| B3 | Late | P4 | 0.6866 | 0.6306 | 0.7425 | 0.1667 | 268 |
| B3 | Late | P5 | 0.7052 | 0.6493 | 0.7612 | 0.1667 | 268 |
| B4 | overall | P0 | 0.1940 | 0.1667 | 0.2226 | 0.1667 | 804 |
| B4 | overall | P1 | 0.7363 | 0.7027 | 0.7662 | 0.1667 | 804 |
| B4 | overall | P2 | 0.1604 | 0.1356 | 0.1866 | 0.1667 | 804 |
| B4 | overall | P3 | 0.4129 | 0.3769 | 0.4478 | 0.1667 | 804 |
| B4 | overall | P4 | 0.6368 | 0.6020 | 0.6716 | 0.1667 | 804 |
| B4 | overall | P5 | 0.3993 | 0.3644 | 0.4378 | 0.1667 | 804 |
| B4 | Early | P0 | 0.1642 | 0.1194 | 0.2090 | 0.1667 | 268 |
| B4 | Early | P1 | 0.7201 | 0.6642 | 0.7724 | 0.1667 | 268 |
| B4 | Early | P2 | 0.2388 | 0.1866 | 0.2948 | 0.1667 | 268 |
| B4 | Early | P3 | 0.4216 | 0.3619 | 0.4813 | 0.1667 | 268 |
| B4 | Early | P4 | 0.6493 | 0.5933 | 0.7052 | 0.1667 | 268 |
| B4 | Early | P5 | 0.2761 | 0.2239 | 0.3284 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.2388 | 0.1903 | 0.2910 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.7948 | 0.7425 | 0.8433 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.1194 | 0.0821 | 0.1604 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.4291 | 0.3694 | 0.4888 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.6903 | 0.6381 | 0.7463 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.3918 | 0.3321 | 0.4515 | 0.1667 | 268 |
| B4 | Late | P0 | 0.1791 | 0.1343 | 0.2239 | 0.1667 | 268 |
| B4 | Late | P1 | 0.6940 | 0.6381 | 0.7463 | 0.1667 | 268 |
| B4 | Late | P2 | 0.1231 | 0.0858 | 0.1642 | 0.1667 | 268 |
| B4 | Late | P3 | 0.3881 | 0.3284 | 0.4441 | 0.1667 | 268 |
| B4 | Late | P4 | 0.5709 | 0.5112 | 0.6306 | 0.1667 | 268 |
| B4 | Late | P5 | 0.5299 | 0.4701 | 0.5896 | 0.1667 | 268 |
| B5 | overall | P0 | 0.1928 | 0.1654 | 0.2214 | 0.1667 | 804 |
| B5 | overall | P1 | 0.6853 | 0.6493 | 0.7177 | 0.1667 | 804 |
| B5 | overall | P2 | 0.0672 | 0.0498 | 0.0846 | 0.1667 | 804 |
| B5 | overall | P3 | 0.1381 | 0.1144 | 0.1617 | 0.1667 | 804 |
| B5 | overall | P4 | 0.6107 | 0.5784 | 0.6455 | 0.1667 | 804 |
| B5 | overall | P5 | 0.1219 | 0.0970 | 0.1468 | 0.1667 | 804 |
| B5 | Early | P0 | 0.2201 | 0.1716 | 0.2724 | 0.1667 | 268 |
| B5 | Early | P1 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 268 |
| B5 | Early | P2 | 0.0896 | 0.0597 | 0.1231 | 0.1667 | 268 |
| B5 | Early | P3 | 0.1940 | 0.1493 | 0.2425 | 0.1667 | 268 |
| B5 | Early | P4 | 0.4067 | 0.3507 | 0.4664 | 0.1667 | 268 |
| B5 | Early | P5 | 0.1530 | 0.1119 | 0.1941 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.2351 | 0.1866 | 0.2873 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.7239 | 0.6715 | 0.7761 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.0784 | 0.0485 | 0.1119 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.1418 | 0.1007 | 0.1828 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.7537 | 0.7052 | 0.8060 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.1194 | 0.0821 | 0.1567 | 0.1667 | 268 |
| B5 | Late | P0 | 0.1231 | 0.0858 | 0.1679 | 0.1667 | 268 |
| B5 | Late | P1 | 0.6716 | 0.6157 | 0.7276 | 0.1667 | 268 |
| B5 | Late | P2 | 0.0336 | 0.0149 | 0.0560 | 0.1667 | 268 |
| B5 | Late | P3 | 0.0784 | 0.0485 | 0.1119 | 0.1667 | 268 |
| B5 | Late | P4 | 0.6716 | 0.6157 | 0.7276 | 0.1667 | 268 |
| B5 | Late | P5 | 0.0933 | 0.0597 | 0.1306 | 0.1667 | 268 |
| B6 | overall | P1 | 0.6729 | 0.6356 | 0.7052 | 0.2000 | 804 |
| B6 | overall | P2 | 0.4813 | 0.4465 | 0.5174 | 0.2000 | 804 |
| B6 | overall | P3 | 0.6032 | 0.5697 | 0.6356 | 0.2000 | 804 |
| B6 | overall | P4 | 0.7525 | 0.7189 | 0.7848 | 0.2000 | 804 |
| B6 | overall | P5 | 0.6654 | 0.6318 | 0.7015 | 0.2000 | 804 |
| B6 | Early | P1 | 0.7463 | 0.6940 | 0.7948 | 0.2000 | 268 |
| B6 | Early | P2 | 0.4142 | 0.3545 | 0.4739 | 0.2000 | 268 |
| B6 | Early | P3 | 0.5858 | 0.5261 | 0.6455 | 0.2000 | 268 |
| B6 | Early | P4 | 0.7687 | 0.7164 | 0.8172 | 0.2000 | 268 |
| B6 | Early | P5 | 0.6007 | 0.5410 | 0.6604 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.6978 | 0.6418 | 0.7500 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.4963 | 0.4365 | 0.5560 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.6530 | 0.5970 | 0.7090 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.8097 | 0.7612 | 0.8545 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.6716 | 0.6157 | 0.7276 | 0.2000 | 268 |
| B6 | Late | P1 | 0.5746 | 0.5149 | 0.6343 | 0.2000 | 268 |
| B6 | Late | P2 | 0.5336 | 0.4701 | 0.5933 | 0.2000 | 268 |
| B6 | Late | P3 | 0.5709 | 0.5112 | 0.6306 | 0.2000 | 268 |
| B6 | Late | P4 | 0.6791 | 0.6231 | 0.7352 | 0.2000 | 268 |
| B6 | Late | P5 | 0.7239 | 0.6716 | 0.7799 | 0.2000 | 268 |
| B7 | overall | P0 | 0.3669 | 0.3321 | 0.4017 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.7494 | 0.7251 | 0.7730 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.5622 | 0.5323 | 0.5945 | 0.2000 | 804 |
| B7 | overall | P4 | 0.7438 | 0.7090 | 0.7749 | 0.2000 | 804 |
| B7 | overall | P5 | 0.6294 | 0.5933 | 0.6654 | 0.2000 | 804 |
| B7 | Early | P0 | 0.2836 | 0.2276 | 0.3396 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.8041 | 0.7687 | 0.8358 | 0.2000 | 536 |
| B7 | Early | P3 | 0.5149 | 0.4552 | 0.5709 | 0.2000 | 268 |
| B7 | Early | P4 | 0.7687 | 0.7201 | 0.8172 | 0.2000 | 268 |
| B7 | Early | P5 | 0.5858 | 0.5261 | 0.6493 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.3918 | 0.3321 | 0.4515 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.7444 | 0.7034 | 0.7817 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.6418 | 0.5858 | 0.6978 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.7985 | 0.7500 | 0.8433 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.6194 | 0.5633 | 0.6754 | 0.2000 | 268 |
| B7 | Late | P0 | 0.4254 | 0.3657 | 0.4814 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.6996 | 0.6567 | 0.7407 | 0.2000 | 536 |
| B7 | Late | P3 | 0.5299 | 0.4701 | 0.5896 | 0.2000 | 268 |
| B7 | Late | P4 | 0.6642 | 0.6082 | 0.7201 | 0.2000 | 268 |
| B7 | Late | P5 | 0.6828 | 0.6305 | 0.7425 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | -0.2239 | 0.4065 | 0.5818 | -1.0205 | 0.5728 |
| C(position, Treatment(reference='Early'))[T.Late] | -0.0842 | 0.1207 | 0.4851 | -0.3208 | 0.1523 |
| C(position, Treatment(reference='Early'))[T.Middle] | 0.0567 | 0.0948 | 0.5497 | -0.1291 | 0.2426 |
| log_context | 0.0791 | 0.0729 | 0.2781 | -0.0639 | 0.2221 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.0901 | -0.2876 | 0.0967 | 0.3350 | 0.3350 | 804 | not confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.4566 | -0.7109 | -0.2159 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.2234 | -0.4852 | 0.0426 | 0.0970 | 0.2910 | 268 | not confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | 0.4098 | 0.0009 | 0.8177 | 0.0470 | 0.1880 | 268 | opposite |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | 1.0872 | 0.4730 | 1.6484 | 0.0020 | 0.0020 | 804 | confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | 0.6881 | -0.4165 | 1.7433 | 0.2080 | 0.4160 | 268 | not confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | 1.3132 | 0.3099 | 2.2908 | 0.0100 | 0.0300 | 268 | confirmed |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | 1.2603 | 0.3867 | 2.0960 | 0.0040 | 0.0200 | 268 | confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | -0.0030 | -0.0187 | 0.0128 | 0.7470 | 1.0000 | 553 | not confirmed |
| Early | P1 - P0 | share_open | lower | pre-specified | -0.0052 | -0.0336 | 0.0224 | 0.7370 | 1.0000 | 223 | not confirmed |
| Middle | P1 - P0 | share_open | lower | pre-specified | 0.0079 | -0.0237 | 0.0395 | 0.6740 | 1.0000 | 190 | not confirmed |
| Late | P1 - P0 | share_open | lower | pre-specified | -0.0143 | -0.0357 | 0.0000 | 0.2630 | 1.0000 | 140 | not confirmed |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1289 | -0.0461 | 0.3022 | 0.1440 | 0.2880 | 804 | not confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.3771 | 0.1454 | 0.6081 | 0.0030 | 0.0150 | 268 | confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1824 | -0.0398 | 0.3967 | 0.1060 | 0.2910 | 268 | not confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | -0.1727 | -0.5801 | 0.2126 | 0.4060 | 0.4060 | 268 | not confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.0572 | 0.8578 | 1.2434 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.9207 | 0.6131 | 1.2417 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.0406 | 0.7269 | 1.3687 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.2103 | 0.8760 | 1.5233 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.1096 | 0.0844 | 0.1365 | 0.0000 | 0.0000 | 467 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.0867 | 0.0434 | 0.1301 | 0.0000 | 0.0000 | 196 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.0833 | 0.0423 | 0.1268 | 0.0000 | 0.0000 | 142 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.1731 | 0.1189 | 0.2390 | 0.0000 | 0.0000 | 129 | confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 3.1336 | 2.8631 | 3.4140 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 3.3571 | 2.9366 | 3.7933 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 3.3988 | 3.0132 | 3.7860 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 2.6450 | 2.2218 | 3.0607 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.2951 | 0.2568 | 0.3369 | 0.0000 | 0.0000 | 462 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.3070 | 0.2439 | 0.3675 | 0.0000 | 0.0000 | 190 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.3069 | 0.2379 | 0.3759 | 0.0000 | 0.0000 | 145 | confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | 0.2638 | 0.1928 | 0.3386 | 0.0000 | 0.0000 | 127 | confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -3.6624 | -4.2575 | -3.1082 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -4.4384 | -5.4412 | -3.4496 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -3.3969 | -4.3275 | -2.4247 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -3.1520 | -3.9708 | -2.3316 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.0764 | 1.8453 | 2.3156 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.4364 | 2.0461 | 2.8242 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.3582 | 1.9875 | 2.7410 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.4346 | 1.0158 | 1.8785 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -1.3518 | -1.7782 | -0.9308 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -2.6415 | -3.4214 | -1.8582 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -1.0836 | -1.8720 | -0.3126 | 0.0040 | 0.0200 | 268 | confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -0.3302 | -1.0408 | 0.4189 | 0.3950 | 0.4160 | 268 | not confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3517 | 0.2849 | 0.4210 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3007 | 0.1916 | 0.4083 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3228 | 0.2281 | 0.4252 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.4316 | 0.3260 | 0.5407 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | -0.0037 | -0.0112 | 0.0050 | 0.4270 | 0.4270 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | -0.0075 | -0.0224 | 0.0075 | 0.4430 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | -0.0037 | -0.0224 | 0.0149 | 0.8580 | 1.0000 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0041 | -0.0235 | 0.0086 | 0.7330 | 0.7330 | 804 | not confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0059 | -0.0178 | 0.0000 | 0.7380 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0067 | -0.0037 | 0.0182 | 0.2130 | 0.6390 | 268 | not confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0131 | -0.0698 | 0.0201 | 0.7260 | 1.0000 | 268 | not confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | -0.0038 | -0.0191 | 0.0115 | 0.7280 | 1.0000 | 395 | not confirmed |
| Early | P5 - P0 | share_open | lower | pre-specified | -0.0029 | -0.0257 | 0.0171 | 0.9170 | 1.0000 | 175 | not confirmed |
| Middle | P5 - P0 | share_open | lower | pre-specified | -0.0037 | -0.0370 | 0.0296 | 0.9300 | 1.0000 | 135 | not confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | -0.0059 | -0.0353 | 0.0118 | 0.9140 | 1.0000 | 85 | not confirmed |
| overall | P5 - P0 | has_question | lower | exploratory | -0.2326 | -0.2674 | -0.1990 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | has_question | lower | exploratory | -0.1157 | -0.1567 | -0.0746 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | has_question | lower | exploratory | -0.2313 | -0.2873 | -0.1791 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | has_question | lower | exploratory | -0.3507 | -0.4179 | -0.2836 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | plan_statement_present | higher | exploratory | 0.2326 | 0.2002 | 0.2674 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | exploratory | 0.1642 | 0.1157 | 0.2164 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | exploratory | 0.2276 | 0.1791 | 0.2836 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | exploratory | 0.3060 | 0.2463 | 0.3694 | 0.0000 | 0.0000 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | 0.8664 | 0.3999 | 1.3311 | 0.0000 | 0.0000 | confirmed |
| P1 - P0 | med_per_100 | higher | pre-specified | 0.5722 | -0.8342 | 1.9770 | 0.4240 | 0.4240 | not confirmed |
| P1 - P0 | share_open | lower | pre-specified | -0.0091 | -0.0458 | 0.0243 | 0.5970 | 1.0000 | not confirmed |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | -0.5498 | -0.9887 | -0.1075 | 0.0140 | 0.0420 | confirmed |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.2896 | -0.1662 | 0.7257 | 0.2190 | 0.2190 | not confirmed |
| P3 - P0 | share_open | higher | pre-specified | 0.0864 | 0.0126 | 0.1650 | 0.0270 | 0.1080 | opposite |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -0.7122 | -1.3123 | -0.0989 | 0.0240 | 0.0480 | confirmed |
| P4 - P0 | share_open | higher | pre-specified | -0.0432 | -0.1370 | 0.0543 | 0.3610 | 1.0000 | not confirmed |
| P4 - P0 | med_per_100 | lower | pre-specified | 1.2864 | 0.0492 | 2.4906 | 0.0460 | 0.0920 | confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -1.0018 | -1.6112 | -0.3699 | 0.0020 | 0.0080 | confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | 2.3113 | 1.2657 | 3.3895 | 0.0000 | 0.0000 | confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1309 | -0.0205 | 0.2762 | 0.0970 | 0.0970 | not confirmed |
| P5 - P0 | n_leading | higher | pre-specified | -0.0037 | -0.0224 | 0.0149 | 0.8580 | 0.8580 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0072 | -0.0683 | 0.0304 | 0.8760 | 0.8760 | not confirmed |
| P5 - P0 | share_open | lower | pre-specified | -0.0030 | -0.0381 | 0.0284 | 0.9090 | 1.0000 | not confirmed |
| P5 - P0 | has_question | lower | exploratory | -0.2351 | -0.3061 | -0.1642 | 0.0000 | 0.0000 | opposite |
| P5 - P0 | plan_statement_present | higher | exploratory | 0.1418 | 0.0709 | 0.2127 | 0.0000 | 0.0000 | opposite |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.6169 | 0.5808 | 0.6505 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| overall | P2 | 0.3296 | 0.2973 | 0.3632 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.5908 | 0.5597 | 0.6219 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.7488 | 0.7164 | 0.7799 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.6555 | 0.6219 | 0.6915 | 0.1667 | 1 | 4 | 1 | 0 | not realised |
| Early | P1 | 0.6940 | 0.6381 | 0.7463 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Early | P2 | 0.3284 | 0.2724 | 0.3843 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.5709 | 0.5112 | 0.6306 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.7724 | 0.7201 | 0.8209 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 0.5933 | 0.5336 | 0.6530 | 0.1667 | 1 | 4 | 1 | 0 | not realised |
| Middle | P1 | 0.6381 | 0.5784 | 0.6940 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Middle | P2 | 0.2985 | 0.2463 | 0.3545 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.6530 | 0.5970 | 0.7090 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.8022 | 0.7537 | 0.8470 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Middle | P5 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 1 | 4 | 1 | 0 | not realised |
| Late | P1 | 0.5187 | 0.4552 | 0.5784 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Late | P2 | 0.3619 | 0.3060 | 0.4179 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.5485 | 0.4888 | 0.6082 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Late | P4 | 0.6716 | 0.6157 | 0.7276 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P5 | 0.7127 | 0.6567 | 0.7687 | 0.1667 | 1 | 4 | 1 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.8893 | 804 |
| P0 | overall | plan_statement_present | 0.1667 | 804 |
| P0 | overall | empathy_phrases_present | 0.0174 | 804 |
| P0 | overall | hedge_per_100 | 0.3072 | 804 |
| P0 | overall | n_words | 33.4701 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.9590 | 268 |
| P0 | Early | plan_statement_present | 0.0560 | 268 |
| P0 | Early | empathy_phrases_present | 0.0187 | 268 |
| P0 | Early | hedge_per_100 | 0.1913 | 268 |
| P0 | Early | n_words | 27.1828 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.9179 | 268 |
| P0 | Middle | plan_statement_present | 0.1455 | 268 |
| P0 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P0 | Middle | hedge_per_100 | 0.3117 | 268 |
| P0 | Middle | n_words | 33.1082 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.7910 | 268 |
| P0 | Late | plan_statement_present | 0.2985 | 268 |
| P0 | Late | empathy_phrases_present | 0.0336 | 268 |
| P0 | Late | hedge_per_100 | 0.4187 | 268 |
| P0 | Late | n_words | 40.1194 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.9453 | 804 |
| P1 | overall | plan_statement_present | 0.0547 | 804 |
| P1 | overall | empathy_phrases_present | 0.0012 | 804 |
| P1 | overall | hedge_per_100 | 0.0736 | 804 |
| P1 | overall | n_words | 20.0697 | 804 |
| P1 | overall | persona_distance | 0.3923 | 804 |
| P1 | Early | has_question | 1.0000 | 268 |
| P1 | Early | plan_statement_present | 0.0000 | 268 |
| P1 | Early | empathy_phrases_present | 0.0000 | 268 |
| P1 | Early | hedge_per_100 | 0.0663 | 268 |
| P1 | Early | n_words | 19.3769 | 268 |
| P1 | Early | persona_distance | 0.3307 | 268 |
| P1 | Middle | has_question | 0.9739 | 268 |
| P1 | Middle | plan_statement_present | 0.0299 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P1 | Middle | hedge_per_100 | 0.0228 | 268 |
| P1 | Middle | n_words | 18.2463 | 268 |
| P1 | Middle | persona_distance | 0.4163 | 268 |
| P1 | Late | has_question | 0.8619 | 268 |
| P1 | Late | plan_statement_present | 0.1343 | 268 |
| P1 | Late | empathy_phrases_present | 0.0037 | 268 |
| P1 | Late | hedge_per_100 | 0.1317 | 268 |
| P1 | Late | n_words | 22.5858 | 268 |
| P1 | Late | persona_distance | 0.4299 | 268 |
| P2 | overall | has_question | 0.8843 | 804 |
| P2 | overall | plan_statement_present | 0.1281 | 804 |
| P2 | overall | empathy_phrases_present | 0.0100 | 804 |
| P2 | overall | hedge_per_100 | 0.1936 | 804 |
| P2 | overall | n_words | 36.2898 | 804 |
| P2 | overall | persona_distance | 0.3396 | 804 |
| P2 | Early | has_question | 0.9963 | 268 |
| P2 | Early | plan_statement_present | 0.0112 | 268 |
| P2 | Early | empathy_phrases_present | 0.0187 | 268 |
| P2 | Early | hedge_per_100 | 0.1353 | 268 |
| P2 | Early | n_words | 30.4590 | 268 |
| P2 | Early | persona_distance | 0.3188 | 268 |
| P2 | Middle | has_question | 0.9142 | 268 |
| P2 | Middle | plan_statement_present | 0.0858 | 268 |
| P2 | Middle | empathy_phrases_present | 0.0037 | 268 |
| P2 | Middle | hedge_per_100 | 0.1650 | 268 |
| P2 | Middle | n_words | 31.3993 | 268 |
| P2 | Middle | persona_distance | 0.3538 | 268 |
| P2 | Late | has_question | 0.7425 | 268 |
| P2 | Late | plan_statement_present | 0.2873 | 268 |
| P2 | Late | empathy_phrases_present | 0.0075 | 268 |
| P2 | Late | hedge_per_100 | 0.2804 | 268 |
| P2 | Late | n_words | 47.0112 | 268 |
| P2 | Late | persona_distance | 0.3462 | 268 |
| P3 | overall | has_question | 0.9515 | 804 |
| P3 | overall | plan_statement_present | 0.1331 | 804 |
| P3 | overall | empathy_phrases_present | 0.0647 | 804 |
| P3 | overall | hedge_per_100 | 0.7177 | 804 |
| P3 | overall | n_words | 61.5647 | 804 |
| P3 | overall | persona_distance | 0.3895 | 804 |
| P3 | Early | has_question | 0.9963 | 268 |
| P3 | Early | plan_statement_present | 0.0485 | 268 |
| P3 | Early | empathy_phrases_present | 0.0597 | 268 |
| P3 | Early | hedge_per_100 | 0.5226 | 268 |
| P3 | Early | n_words | 47.8582 | 268 |
| P3 | Early | persona_distance | 0.3491 | 268 |
| P3 | Middle | has_question | 0.9851 | 268 |
| P3 | Middle | plan_statement_present | 0.0672 | 268 |
| P3 | Middle | empathy_phrases_present | 0.0634 | 268 |
| P3 | Middle | hedge_per_100 | 0.9276 | 268 |
| P3 | Middle | n_words | 60.7537 | 268 |
| P3 | Middle | persona_distance | 0.4131 | 268 |
| P3 | Late | has_question | 0.8731 | 268 |
| P3 | Late | plan_statement_present | 0.2836 | 268 |
| P3 | Late | empathy_phrases_present | 0.0709 | 268 |
| P3 | Late | hedge_per_100 | 0.7028 | 268 |
| P3 | Late | n_words | 76.0821 | 268 |
| P3 | Late | persona_distance | 0.4064 | 268 |
| P4 | overall | has_question | 0.9664 | 804 |
| P4 | overall | plan_statement_present | 0.0597 | 804 |
| P4 | overall | empathy_phrases_present | 0.2736 | 804 |
| P4 | overall | hedge_per_100 | 0.7483 | 804 |
| P4 | overall | n_words | 62.5995 | 804 |
| P4 | overall | persona_distance | 0.5293 | 804 |
| P4 | Early | has_question | 0.9963 | 268 |
| P4 | Early | plan_statement_present | 0.0187 | 268 |
| P4 | Early | empathy_phrases_present | 0.2575 | 268 |
| P4 | Early | hedge_per_100 | 0.6143 | 268 |
| P4 | Early | n_words | 49.8619 | 268 |
| P4 | Early | persona_distance | 0.5225 | 268 |
| P4 | Middle | has_question | 0.9701 | 268 |
| P4 | Middle | plan_statement_present | 0.0597 | 268 |
| P4 | Middle | empathy_phrases_present | 0.2985 | 268 |
| P4 | Middle | hedge_per_100 | 0.8874 | 268 |
| P4 | Middle | n_words | 68.9366 | 268 |
| P4 | Middle | persona_distance | 0.5493 | 268 |
| P4 | Late | has_question | 0.9328 | 268 |
| P4 | Late | plan_statement_present | 0.1007 | 268 |
| P4 | Late | empathy_phrases_present | 0.2649 | 268 |
| P4 | Late | hedge_per_100 | 0.7433 | 268 |
| P4 | Late | n_words | 69.0000 | 268 |
| P4 | Late | persona_distance | 0.5162 | 268 |
| P5 | overall | has_question | 0.6567 | 804 |
| P5 | overall | plan_statement_present | 0.3993 | 804 |
| P5 | overall | empathy_phrases_present | 0.0274 | 804 |
| P5 | overall | hedge_per_100 | 0.0883 | 804 |
| P5 | overall | n_words | 42.2699 | 804 |
| P5 | overall | persona_distance | 0.3805 | 804 |
| P5 | Early | has_question | 0.8433 | 268 |
| P5 | Early | plan_statement_present | 0.2201 | 268 |
| P5 | Early | empathy_phrases_present | 0.0261 | 268 |
| P5 | Early | hedge_per_100 | 0.0644 | 268 |
| P5 | Early | n_words | 33.5299 | 268 |
| P5 | Early | persona_distance | 0.3544 | 268 |
| P5 | Middle | has_question | 0.6866 | 268 |
| P5 | Middle | plan_statement_present | 0.3731 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0410 | 268 |
| P5 | Middle | hedge_per_100 | 0.0590 | 268 |
| P5 | Middle | n_words | 43.0896 | 268 |
| P5 | Middle | persona_distance | 0.3966 | 268 |
| P5 | Late | has_question | 0.4403 | 268 |
| P5 | Late | plan_statement_present | 0.6045 | 268 |
| P5 | Late | empathy_phrases_present | 0.0149 | 268 |
| P5 | Late | hedge_per_100 | 0.1415 | 268 |
| P5 | Late | n_words | 50.1903 | 268 |
| P5 | Late | persona_distance | 0.3905 | 268 |

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
