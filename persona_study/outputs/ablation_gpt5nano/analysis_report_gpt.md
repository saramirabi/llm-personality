# gpt measurement report

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
| B1 | overall | 0.8605 | 0.8501 | 0.8700 | 0.1667 | 4824 |
| B1 | Early | 0.8961 | 0.8818 | 0.9098 | 0.1667 | 1608 |
| B1 | Middle | 0.8632 | 0.8458 | 0.8794 | 0.1667 | 1608 |
| B1 | Late | 0.8221 | 0.8035 | 0.8396 | 0.1667 | 1608 |
| B2 | overall | 0.6196 | 0.6066 | 0.6331 | 0.1667 | 4824 |
| B2 | Early | 0.6493 | 0.6287 | 0.6685 | 0.1667 | 1608 |
| B2 | Middle | 0.6455 | 0.6238 | 0.6679 | 0.1667 | 1608 |
| B2 | Late | 0.5641 | 0.5417 | 0.5877 | 0.1667 | 1608 |
| B3 | overall | 0.8576 | 0.8472 | 0.8671 | 0.1667 | 4824 |
| B3 | Early | 0.8924 | 0.8775 | 0.9073 | 0.1667 | 1608 |
| B3 | Middle | 0.8588 | 0.8414 | 0.8756 | 0.1667 | 1608 |
| B3 | Late | 0.8215 | 0.8028 | 0.8396 | 0.1667 | 1608 |
| B4 | overall | 0.6951 | 0.6826 | 0.7069 | 0.1667 | 4824 |
| B4 | Early | 0.7463 | 0.7257 | 0.7668 | 0.1667 | 1608 |
| B4 | Middle | 0.6766 | 0.6542 | 0.6990 | 0.1667 | 1608 |
| B4 | Late | 0.6623 | 0.6418 | 0.6841 | 0.1667 | 1608 |
| B5 | overall | 0.3373 | 0.3252 | 0.3487 | 0.1667 | 4824 |
| B5 | Early | 0.3451 | 0.3265 | 0.3650 | 0.1667 | 1608 |
| B5 | Middle | 0.3364 | 0.3159 | 0.3570 | 0.1667 | 1608 |
| B5 | Late | 0.3302 | 0.3097 | 0.3507 | 0.1667 | 1608 |
| B6 | overall | 0.9152 | 0.9062 | 0.9246 | 0.2000 | 4020 |
| B6 | Early | 0.9313 | 0.9179 | 0.9448 | 0.2000 | 1340 |
| B6 | Middle | 0.9216 | 0.9067 | 0.9358 | 0.2000 | 1340 |
| B6 | Late | 0.8925 | 0.8761 | 0.9097 | 0.2000 | 1340 |
| B7 | overall | 0.8779 | 0.8688 | 0.8866 | 0.2000 | 4824 |
| B7 | Early | 0.9192 | 0.9073 | 0.9316 | 0.2000 | 1608 |
| B7 | Middle | 0.8719 | 0.8563 | 0.8868 | 0.2000 | 1608 |
| B7 | Late | 0.8427 | 0.8259 | 0.8595 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.7637 | 0.7313 | 0.7960 | 0.1667 | 804 |
| B1 | overall | P1 | 0.9378 | 0.9204 | 0.9552 | 0.1667 | 804 |
| B1 | overall | P2 | 0.7749 | 0.7450 | 0.8060 | 0.1667 | 804 |
| B1 | overall | P3 | 0.8246 | 0.7985 | 0.8495 | 0.1667 | 804 |
| B1 | overall | P4 | 0.8731 | 0.8495 | 0.8968 | 0.1667 | 804 |
| B1 | overall | P5 | 0.9888 | 0.9813 | 0.9950 | 0.1667 | 804 |
| B1 | Early | P0 | 0.7948 | 0.7463 | 0.8433 | 0.1667 | 268 |
| B1 | Early | P1 | 0.9515 | 0.9254 | 0.9739 | 0.1667 | 268 |
| B1 | Early | P2 | 0.8172 | 0.7687 | 0.8619 | 0.1667 | 268 |
| B1 | Early | P3 | 0.8619 | 0.8208 | 0.9030 | 0.1667 | 268 |
| B1 | Early | P4 | 0.9515 | 0.9254 | 0.9739 | 0.1667 | 268 |
| B1 | Early | P5 | 1.0000 | 1.0000 | 1.0000 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.7612 | 0.7090 | 0.8097 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.9328 | 0.9030 | 0.9627 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.8022 | 0.7500 | 0.8507 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.8246 | 0.7761 | 0.8694 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.8694 | 0.8284 | 0.9067 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.9888 | 0.9739 | 1.0000 | 0.1667 | 268 |
| B1 | Late | P0 | 0.7351 | 0.6791 | 0.7836 | 0.1667 | 268 |
| B1 | Late | P1 | 0.9291 | 0.8955 | 0.9590 | 0.1667 | 268 |
| B1 | Late | P2 | 0.7052 | 0.6530 | 0.7575 | 0.1667 | 268 |
| B1 | Late | P3 | 0.7873 | 0.7351 | 0.8321 | 0.1667 | 268 |
| B1 | Late | P4 | 0.7985 | 0.7500 | 0.8433 | 0.1667 | 268 |
| B1 | Late | P5 | 0.9776 | 0.9590 | 0.9925 | 0.1667 | 268 |
| B2 | overall | P0 | 0.4067 | 0.3719 | 0.4440 | 0.1667 | 804 |
| B2 | overall | P1 | 0.7960 | 0.7662 | 0.8271 | 0.1667 | 804 |
| B2 | overall | P2 | 0.4639 | 0.4279 | 0.5012 | 0.1667 | 804 |
| B2 | overall | P3 | 0.5896 | 0.5547 | 0.6231 | 0.1667 | 804 |
| B2 | overall | P4 | 0.8147 | 0.7873 | 0.8420 | 0.1667 | 804 |
| B2 | overall | P5 | 0.6468 | 0.6082 | 0.6828 | 0.1667 | 804 |
| B2 | Early | P0 | 0.4142 | 0.3545 | 0.4740 | 0.1667 | 268 |
| B2 | Early | P1 | 0.8619 | 0.8172 | 0.9030 | 0.1667 | 268 |
| B2 | Early | P2 | 0.4776 | 0.4216 | 0.5374 | 0.1667 | 268 |
| B2 | Early | P3 | 0.5373 | 0.4776 | 0.5970 | 0.1667 | 268 |
| B2 | Early | P4 | 0.8955 | 0.8545 | 0.9328 | 0.1667 | 268 |
| B2 | Early | P5 | 0.7090 | 0.6530 | 0.7612 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.4216 | 0.3619 | 0.4776 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.8134 | 0.7649 | 0.8583 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.5075 | 0.4478 | 0.5672 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.6679 | 0.6119 | 0.7202 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.8321 | 0.7836 | 0.8769 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.6306 | 0.5709 | 0.6903 | 0.1667 | 268 |
| B2 | Late | P0 | 0.3843 | 0.3209 | 0.4440 | 0.1667 | 268 |
| B2 | Late | P1 | 0.7127 | 0.6604 | 0.7687 | 0.1667 | 268 |
| B2 | Late | P2 | 0.4067 | 0.3470 | 0.4701 | 0.1667 | 268 |
| B2 | Late | P3 | 0.5634 | 0.5075 | 0.6231 | 0.1667 | 268 |
| B2 | Late | P4 | 0.7164 | 0.6604 | 0.7687 | 0.1667 | 268 |
| B2 | Late | P5 | 0.6007 | 0.5410 | 0.6604 | 0.1667 | 268 |
| B3 | overall | P0 | 0.7562 | 0.7239 | 0.7886 | 0.1667 | 804 |
| B3 | overall | P1 | 0.9403 | 0.9241 | 0.9565 | 0.1667 | 804 |
| B3 | overall | P2 | 0.7736 | 0.7425 | 0.8035 | 0.1667 | 804 |
| B3 | overall | P3 | 0.8134 | 0.7861 | 0.8396 | 0.1667 | 804 |
| B3 | overall | P4 | 0.8756 | 0.8532 | 0.8980 | 0.1667 | 804 |
| B3 | overall | P5 | 0.9863 | 0.9789 | 0.9938 | 0.1667 | 804 |
| B3 | Early | P0 | 0.7836 | 0.7351 | 0.8321 | 0.1667 | 268 |
| B3 | Early | P1 | 0.9664 | 0.9440 | 0.9851 | 0.1667 | 268 |
| B3 | Early | P2 | 0.8209 | 0.7761 | 0.8657 | 0.1667 | 268 |
| B3 | Early | P3 | 0.8321 | 0.7836 | 0.8769 | 0.1667 | 268 |
| B3 | Early | P4 | 0.9552 | 0.9291 | 0.9776 | 0.1667 | 268 |
| B3 | Early | P5 | 0.9963 | 0.9888 | 1.0000 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.7612 | 0.7090 | 0.8097 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.9328 | 0.8993 | 0.9590 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.7873 | 0.7351 | 0.8358 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.8209 | 0.7724 | 0.8657 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.8657 | 0.8209 | 0.9030 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.9851 | 0.9701 | 0.9963 | 0.1667 | 268 |
| B3 | Late | P0 | 0.7239 | 0.6715 | 0.7724 | 0.1667 | 268 |
| B3 | Late | P1 | 0.9216 | 0.8881 | 0.9515 | 0.1667 | 268 |
| B3 | Late | P2 | 0.7127 | 0.6604 | 0.7649 | 0.1667 | 268 |
| B3 | Late | P3 | 0.7873 | 0.7388 | 0.8321 | 0.1667 | 268 |
| B3 | Late | P4 | 0.8060 | 0.7612 | 0.8545 | 0.1667 | 268 |
| B3 | Late | P5 | 0.9776 | 0.9590 | 0.9925 | 0.1667 | 268 |
| B4 | overall | P0 | 0.5709 | 0.5323 | 0.6082 | 0.1667 | 804 |
| B4 | overall | P1 | 0.8296 | 0.8047 | 0.8545 | 0.1667 | 804 |
| B4 | overall | P2 | 0.5746 | 0.5398 | 0.6095 | 0.1667 | 804 |
| B4 | overall | P3 | 0.5858 | 0.5498 | 0.6194 | 0.1667 | 804 |
| B4 | overall | P4 | 0.7077 | 0.6741 | 0.7413 | 0.1667 | 804 |
| B4 | overall | P5 | 0.9017 | 0.8818 | 0.9204 | 0.1667 | 804 |
| B4 | Early | P0 | 0.5970 | 0.5410 | 0.6567 | 0.1667 | 268 |
| B4 | Early | P1 | 0.8806 | 0.8396 | 0.9179 | 0.1667 | 268 |
| B4 | Early | P2 | 0.6791 | 0.6231 | 0.7351 | 0.1667 | 268 |
| B4 | Early | P3 | 0.6567 | 0.6007 | 0.7164 | 0.1667 | 268 |
| B4 | Early | P4 | 0.7239 | 0.6716 | 0.7761 | 0.1667 | 268 |
| B4 | Early | P5 | 0.9403 | 0.9104 | 0.9664 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.5746 | 0.5149 | 0.6343 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.8097 | 0.7649 | 0.8582 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.5149 | 0.4552 | 0.5746 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.5299 | 0.4664 | 0.5896 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.7575 | 0.7052 | 0.8060 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.8731 | 0.8321 | 0.9104 | 0.1667 | 268 |
| B4 | Late | P0 | 0.5410 | 0.4851 | 0.6007 | 0.1667 | 268 |
| B4 | Late | P1 | 0.7985 | 0.7500 | 0.8470 | 0.1667 | 268 |
| B4 | Late | P2 | 0.5299 | 0.4738 | 0.5896 | 0.1667 | 268 |
| B4 | Late | P3 | 0.5709 | 0.5112 | 0.6270 | 0.1667 | 268 |
| B4 | Late | P4 | 0.6418 | 0.5857 | 0.7015 | 0.1667 | 268 |
| B4 | Late | P5 | 0.8918 | 0.8545 | 0.9291 | 0.1667 | 268 |
| B5 | overall | P0 | 0.3470 | 0.3147 | 0.3769 | 0.1667 | 804 |
| B5 | overall | P1 | 0.6468 | 0.6119 | 0.6816 | 0.1667 | 804 |
| B5 | overall | P2 | 0.2450 | 0.2152 | 0.2736 | 0.1667 | 804 |
| B5 | overall | P3 | 0.5945 | 0.5535 | 0.6294 | 0.1667 | 804 |
| B5 | overall | P4 | 0.1119 | 0.0896 | 0.1343 | 0.1667 | 804 |
| B5 | overall | P5 | 0.0784 | 0.0609 | 0.0970 | 0.1667 | 804 |
| B5 | Early | P0 | 0.3881 | 0.3284 | 0.4478 | 0.1667 | 268 |
| B5 | Early | P1 | 0.7164 | 0.6604 | 0.7687 | 0.1667 | 268 |
| B5 | Early | P2 | 0.2201 | 0.1716 | 0.2687 | 0.1667 | 268 |
| B5 | Early | P3 | 0.5597 | 0.5000 | 0.6157 | 0.1667 | 268 |
| B5 | Early | P4 | 0.1082 | 0.0709 | 0.1455 | 0.1667 | 268 |
| B5 | Early | P5 | 0.0784 | 0.0485 | 0.1119 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.3097 | 0.2575 | 0.3657 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.6716 | 0.6156 | 0.7239 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.2724 | 0.2201 | 0.3246 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.5821 | 0.5224 | 0.6381 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.1082 | 0.0709 | 0.1455 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.0746 | 0.0448 | 0.1082 | 0.1667 | 268 |
| B5 | Late | P0 | 0.3433 | 0.2836 | 0.4030 | 0.1667 | 268 |
| B5 | Late | P1 | 0.5522 | 0.4925 | 0.6082 | 0.1667 | 268 |
| B5 | Late | P2 | 0.2425 | 0.1940 | 0.2948 | 0.1667 | 268 |
| B5 | Late | P3 | 0.6418 | 0.5858 | 0.6978 | 0.1667 | 268 |
| B5 | Late | P4 | 0.1194 | 0.0821 | 0.1604 | 0.1667 | 268 |
| B5 | Late | P5 | 0.0821 | 0.0522 | 0.1157 | 0.1667 | 268 |
| B6 | overall | P1 | 0.9440 | 0.9279 | 0.9602 | 0.2000 | 804 |
| B6 | overall | P2 | 0.9117 | 0.8868 | 0.9341 | 0.2000 | 804 |
| B6 | overall | P3 | 0.8595 | 0.8358 | 0.8818 | 0.2000 | 804 |
| B6 | overall | P4 | 0.8682 | 0.8433 | 0.8930 | 0.2000 | 804 |
| B6 | overall | P5 | 0.9925 | 0.9863 | 0.9975 | 0.2000 | 804 |
| B6 | Early | P1 | 0.9590 | 0.9328 | 0.9813 | 0.2000 | 268 |
| B6 | Early | P2 | 0.8993 | 0.8619 | 0.9366 | 0.2000 | 268 |
| B6 | Early | P3 | 0.8582 | 0.8134 | 0.8993 | 0.2000 | 268 |
| B6 | Early | P4 | 0.9403 | 0.9104 | 0.9664 | 0.2000 | 268 |
| B6 | Early | P5 | 1.0000 | 1.0000 | 1.0000 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.9366 | 0.9066 | 0.9627 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.9366 | 0.9030 | 0.9627 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.8731 | 0.8321 | 0.9104 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.8694 | 0.8284 | 0.9067 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.9925 | 0.9813 | 1.0000 | 0.2000 | 268 |
| B6 | Late | P1 | 0.9366 | 0.9067 | 0.9627 | 0.2000 | 268 |
| B6 | Late | P2 | 0.8993 | 0.8619 | 0.9328 | 0.2000 | 268 |
| B6 | Late | P3 | 0.8470 | 0.8060 | 0.8881 | 0.2000 | 268 |
| B6 | Late | P4 | 0.7948 | 0.7463 | 0.8433 | 0.2000 | 268 |
| B6 | Late | P5 | 0.9851 | 0.9701 | 0.9963 | 0.2000 | 268 |
| B7 | overall | P0 | 0.7090 | 0.6741 | 0.7438 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.9403 | 0.9291 | 0.9521 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.8271 | 0.8010 | 0.8520 | 0.2000 | 804 |
| B7 | overall | P4 | 0.8781 | 0.8557 | 0.9005 | 0.2000 | 804 |
| B7 | overall | P5 | 0.9726 | 0.9614 | 0.9838 | 0.2000 | 804 |
| B7 | Early | P0 | 0.7463 | 0.6940 | 0.7949 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.9739 | 0.9608 | 0.9869 | 0.2000 | 536 |
| B7 | Early | P3 | 0.8731 | 0.8321 | 0.9104 | 0.2000 | 268 |
| B7 | Early | P4 | 0.9552 | 0.9291 | 0.9776 | 0.2000 | 268 |
| B7 | Early | P5 | 0.9925 | 0.9813 | 1.0000 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.7052 | 0.6493 | 0.7613 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.9366 | 0.9179 | 0.9552 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.8209 | 0.7724 | 0.8619 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.8694 | 0.8284 | 0.9067 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.9627 | 0.9403 | 0.9851 | 0.2000 | 268 |
| B7 | Late | P0 | 0.6754 | 0.6194 | 0.7313 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.9104 | 0.8862 | 0.9328 | 0.2000 | 536 |
| B7 | Late | P3 | 0.7873 | 0.7388 | 0.8358 | 0.2000 | 268 |
| B7 | Late | P4 | 0.8097 | 0.7649 | 0.8545 | 0.2000 | 268 |
| B7 | Late | P5 | 0.9627 | 0.9402 | 0.9813 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | 2.5753 | 0.6693 | 0.0001 | 1.2634 | 3.8871 |
| C(position, Treatment(reference='Early'))[T.Late] | -0.5227 | 0.1757 | 0.0029 | -0.8671 | -0.1784 |
| C(position, Treatment(reference='Early'))[T.Middle] | -0.2443 | 0.1314 | 0.0630 | -0.5019 | 0.0133 |
| log_context | -0.0756 | 0.1175 | 0.5198 | -0.3059 | 0.1547 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1682 | -0.2201 | -0.1133 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.2138 | -0.2996 | -0.1301 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1444 | -0.2302 | -0.0576 | 0.0020 | 0.0040 | 268 | confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1462 | -0.2340 | -0.0543 | 0.0010 | 0.0040 | 268 | confirmed |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | 5.7231 | 5.4009 | 6.0780 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | 6.9524 | 6.3473 | 7.5279 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | 5.1739 | 4.6466 | 5.7561 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | 5.0430 | 4.5374 | 5.5465 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | -0.0399 | -0.0614 | -0.0214 | 0.0000 | 0.0000 | 339 | confirmed |
| Early | P1 - P0 | share_open | lower | pre-specified | -0.0244 | -0.0480 | -0.0038 | 0.0180 | 0.0900 | 152 | confirmed |
| Middle | P1 - P0 | share_open | lower | pre-specified | -0.0229 | -0.0574 | 0.0029 | 0.1040 | 0.3120 | 97 | not confirmed |
| Late | P1 - P0 | share_open | lower | pre-specified | -0.0843 | -0.1408 | -0.0342 | 0.0000 | 0.0000 | 90 | confirmed |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1594 | 0.1120 | 0.2055 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1982 | 0.1247 | 0.2714 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1135 | 0.0377 | 0.1880 | 0.0020 | 0.0040 | 268 | confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1666 | 0.0811 | 0.2475 | 0.0010 | 0.0040 | 268 | confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.8415 | 0.7732 | 0.9106 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.0225 | 0.9018 | 1.1493 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.7439 | 0.6352 | 0.8563 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.7580 | 0.6501 | 0.8662 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.1524 | 0.1285 | 0.1765 | 0.0000 | 0.0000 | 661 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.1113 | 0.0822 | 0.1428 | 0.0000 | 0.0000 | 239 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.1390 | 0.0992 | 0.1824 | 0.0000 | 0.0000 | 210 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.2120 | 0.1607 | 0.2636 | 0.0000 | 0.0000 | 212 | confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 1.6603 | 1.5417 | 1.7787 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 1.8949 | 1.6764 | 2.1103 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 1.6685 | 1.5000 | 1.8466 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 1.4174 | 1.2808 | 1.5612 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.2233 | 0.1985 | 0.2489 | 0.0000 | 0.0000 | 656 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.2060 | 0.1686 | 0.2443 | 0.0000 | 0.0000 | 240 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.2269 | 0.1779 | 0.2732 | 0.0000 | 0.0000 | 206 | confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | 0.2396 | 0.1875 | 0.2951 | 0.0000 | 0.0000 | 210 | confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -3.7639 | -4.0201 | -3.4878 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -3.4998 | -3.9230 | -3.0975 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -4.0865 | -4.5398 | -3.6257 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -3.7053 | -4.1214 | -3.2695 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.8188 | 0.7067 | 0.9314 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.8723 | 0.6651 | 1.1009 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.9246 | 0.7371 | 1.1050 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.6594 | 0.5151 | 0.8165 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -2.1343 | -2.3436 | -1.9151 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -2.2892 | -2.6354 | -1.9233 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -2.2615 | -2.6380 | -1.8997 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -1.8521 | -2.1919 | -1.5061 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3572 | 0.3308 | 0.3841 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.4280 | 0.3856 | 0.4725 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3291 | 0.2870 | 0.3710 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3143 | 0.2763 | 0.3546 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | 0.0012 | 0.0000 | 0.0037 | 0.7460 | 0.7460 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | 0.0037 | 0.0000 | 0.0112 | 0.7460 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1135 | -0.1321 | -0.0963 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1168 | -0.1437 | -0.0932 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1071 | -0.1381 | -0.0774 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1167 | -0.1494 | -0.0883 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | -0.0269 | -0.0490 | -0.0065 | 0.0120 | 0.0120 | 348 | confirmed |
| Early | P5 - P0 | share_open | lower | pre-specified | -0.0047 | -0.0279 | 0.0212 | 0.6640 | 0.6640 | 149 | not confirmed |
| Middle | P5 - P0 | share_open | lower | pre-specified | -0.0267 | -0.0674 | 0.0049 | 0.1340 | 0.3120 | 95 | not confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | -0.0590 | -0.1152 | -0.0069 | 0.0240 | 0.0960 | 104 | confirmed |
| overall | P5 - P0 | has_question | lower | pre-specified | -0.3520 | -0.3893 | -0.3134 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | has_question | lower | pre-specified | -0.3097 | -0.3731 | -0.2463 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | has_question | lower | pre-specified | -0.3619 | -0.4328 | -0.2873 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | has_question | lower | pre-specified | -0.3843 | -0.4515 | -0.3172 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | plan_statement_present | higher | pre-specified | 0.3122 | 0.2749 | 0.3507 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | pre-specified | 0.3284 | 0.2724 | 0.3918 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | pre-specified | 0.3470 | 0.2873 | 0.4104 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | pre-specified | 0.2612 | 0.2052 | 0.3172 | 0.0000 | 0.0000 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | 0.0676 | -0.0550 | 0.1860 | 0.2630 | 0.5260 | not confirmed |
| P1 - P0 | med_per_100 | higher | pre-specified | -1.9094 | -2.6668 | -1.1214 | 0.0000 | 0.0000 | confirmed |
| P1 - P0 | share_open | lower | pre-specified | -0.0598 | -0.1261 | -0.0028 | 0.0350 | 0.1050 | opposite |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | -0.0315 | -0.1393 | 0.0686 | 0.5550 | 0.5550 | not confirmed |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | -0.2645 | -0.4184 | -0.1047 | 0.0010 | 0.0040 | confirmed |
| P3 - P0 | share_open | higher | pre-specified | 0.1007 | 0.0413 | 0.1591 | 0.0000 | 0.0000 | opposite |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -0.4775 | -0.7214 | -0.2556 | 0.0000 | 0.0000 | confirmed |
| P4 - P0 | share_open | higher | pre-specified | 0.0336 | -0.0323 | 0.1002 | 0.3050 | 0.3050 | not confirmed |
| P4 - P0 | med_per_100 | lower | pre-specified | -0.2055 | -0.7438 | 0.3780 | 0.4990 | 0.4990 | not confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.2129 | -0.4756 | 0.0239 | 0.0880 | 0.2640 | not confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | 0.4372 | -0.0500 | 0.9363 | 0.0720 | 0.1440 | not confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | -0.1137 | -0.1712 | -0.0569 | 0.0000 | 0.0000 | confirmed |
| P5 - P0 | n_leading | higher | pre-specified | -0.0037 | -0.0112 | 0.0000 | 0.7460 | 0.7460 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0001 | -0.0405 | 0.0376 | 0.9970 | 0.9970 | not confirmed |
| P5 - P0 | share_open | lower | pre-specified | -0.0544 | -0.1130 | 0.0019 | 0.0630 | 0.1260 | not confirmed |
| P5 - P0 | has_question | lower | pre-specified | -0.0746 | -0.1791 | 0.0224 | 0.1620 | 0.1620 | not confirmed |
| P5 - P0 | plan_statement_present | higher | pre-specified | -0.0672 | -0.1455 | 0.0075 | 0.0930 | 0.0930 | not confirmed |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.9378 | 0.9204 | 0.9552 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P2 | 0.7749 | 0.7450 | 0.8060 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.8246 | 0.7985 | 0.8495 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.8731 | 0.8495 | 0.8968 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.9888 | 0.9813 | 0.9950 | 0.1667 | 1 | 4 | 3 | 0 | not realised |
| Early | P1 | 0.9515 | 0.9254 | 0.9739 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P2 | 0.8172 | 0.7687 | 0.8619 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.8619 | 0.8208 | 0.9030 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.9515 | 0.9254 | 0.9739 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 1.0000 | 1.0000 | 1.0000 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Middle | P1 | 0.9328 | 0.9030 | 0.9627 | 0.1667 | 1 | 3 | 2 | 0 | not realised |
| Middle | P2 | 0.8022 | 0.7500 | 0.8507 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.8246 | 0.7761 | 0.8694 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.8694 | 0.8284 | 0.9067 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Middle | P5 | 0.9888 | 0.9739 | 1.0000 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Late | P1 | 0.9291 | 0.8955 | 0.9590 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P2 | 0.7052 | 0.6530 | 0.7575 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.7873 | 0.7351 | 0.8321 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Late | P4 | 0.7985 | 0.7500 | 0.8433 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P5 | 0.9776 | 0.9590 | 0.9925 | 0.1667 | 1 | 4 | 3 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.8818 | 804 |
| P0 | overall | plan_statement_present | 0.6580 | 804 |
| P0 | overall | empathy_phrases_present | 0.1007 | 804 |
| P0 | overall | hedge_per_100 | 0.4076 | 804 |
| P0 | overall | n_words | 228.0784 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.9328 | 268 |
| P0 | Early | plan_statement_present | 0.6455 | 268 |
| P0 | Early | empathy_phrases_present | 0.1045 | 268 |
| P0 | Early | hedge_per_100 | 0.4242 | 268 |
| P0 | Early | n_words | 222.1119 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.8433 | 268 |
| P0 | Middle | plan_statement_present | 0.6194 | 268 |
| P0 | Middle | empathy_phrases_present | 0.0970 | 268 |
| P0 | Middle | hedge_per_100 | 0.4114 | 268 |
| P0 | Middle | n_words | 228.3843 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.8694 | 268 |
| P0 | Late | plan_statement_present | 0.7090 | 268 |
| P0 | Late | empathy_phrases_present | 0.1007 | 268 |
| P0 | Late | hedge_per_100 | 0.3872 | 268 |
| P0 | Late | n_words | 233.7388 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.5075 | 804 |
| P1 | overall | plan_statement_present | 0.5522 | 804 |
| P1 | overall | empathy_phrases_present | 0.0000 | 804 |
| P1 | overall | hedge_per_100 | 0.1740 | 804 |
| P1 | overall | n_words | 166.3346 | 804 |
| P1 | overall | persona_distance | 0.2220 | 804 |
| P1 | Early | has_question | 0.6604 | 268 |
| P1 | Early | plan_statement_present | 0.4366 | 268 |
| P1 | Early | empathy_phrases_present | 0.0000 | 268 |
| P1 | Early | hedge_per_100 | 0.1553 | 268 |
| P1 | Early | n_words | 150.6828 | 268 |
| P1 | Early | persona_distance | 0.2370 | 268 |
| P1 | Middle | has_question | 0.4403 | 268 |
| P1 | Middle | plan_statement_present | 0.6082 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P1 | Middle | hedge_per_100 | 0.2015 | 268 |
| P1 | Middle | n_words | 164.2761 | 268 |
| P1 | Middle | persona_distance | 0.2211 | 268 |
| P1 | Late | has_question | 0.4216 | 268 |
| P1 | Late | plan_statement_present | 0.6119 | 268 |
| P1 | Late | empathy_phrases_present | 0.0000 | 268 |
| P1 | Late | hedge_per_100 | 0.1653 | 268 |
| P1 | Late | n_words | 184.0448 | 268 |
| P1 | Late | persona_distance | 0.2080 | 268 |
| P2 | overall | has_question | 0.8831 | 804 |
| P2 | overall | plan_statement_present | 0.5398 | 804 |
| P2 | overall | empathy_phrases_present | 0.0423 | 804 |
| P2 | overall | hedge_per_100 | 0.2878 | 804 |
| P2 | overall | n_words | 282.9017 | 804 |
| P2 | overall | persona_distance | 0.1810 | 804 |
| P2 | Early | has_question | 0.9515 | 268 |
| P2 | Early | plan_statement_present | 0.4813 | 268 |
| P2 | Early | empathy_phrases_present | 0.0485 | 268 |
| P2 | Early | hedge_per_100 | 0.2661 | 268 |
| P2 | Early | n_words | 285.0522 | 268 |
| P2 | Early | persona_distance | 0.1902 | 268 |
| P2 | Middle | has_question | 0.8582 | 268 |
| P2 | Middle | plan_statement_present | 0.5075 | 268 |
| P2 | Middle | empathy_phrases_present | 0.0336 | 268 |
| P2 | Middle | hedge_per_100 | 0.3082 | 268 |
| P2 | Middle | n_words | 286.0075 | 268 |
| P2 | Middle | persona_distance | 0.1774 | 268 |
| P2 | Late | has_question | 0.8396 | 268 |
| P2 | Late | plan_statement_present | 0.6306 | 268 |
| P2 | Late | empathy_phrases_present | 0.0448 | 268 |
| P2 | Late | hedge_per_100 | 0.2892 | 268 |
| P2 | Late | n_words | 277.6455 | 268 |
| P2 | Late | persona_distance | 0.1753 | 268 |
| P3 | overall | has_question | 0.9900 | 804 |
| P3 | overall | plan_statement_present | 0.7823 | 804 |
| P3 | overall | empathy_phrases_present | 0.1754 | 804 |
| P3 | overall | hedge_per_100 | 0.4316 | 804 |
| P3 | overall | n_words | 341.1381 | 804 |
| P3 | overall | persona_distance | 0.1813 | 804 |
| P3 | Early | has_question | 0.9963 | 268 |
| P3 | Early | plan_statement_present | 0.7463 | 268 |
| P3 | Early | empathy_phrases_present | 0.1455 | 268 |
| P3 | Early | hedge_per_100 | 0.4299 | 268 |
| P3 | Early | n_words | 330.1530 | 268 |
| P3 | Early | persona_distance | 0.1801 | 268 |
| P3 | Middle | has_question | 0.9851 | 268 |
| P3 | Middle | plan_statement_present | 0.7500 | 268 |
| P3 | Middle | empathy_phrases_present | 0.1791 | 268 |
| P3 | Middle | hedge_per_100 | 0.4060 | 268 |
| P3 | Middle | n_words | 342.9328 | 268 |
| P3 | Middle | persona_distance | 0.1805 | 268 |
| P3 | Late | has_question | 0.9888 | 268 |
| P3 | Late | plan_statement_present | 0.8507 | 268 |
| P3 | Late | empathy_phrases_present | 0.2015 | 268 |
| P3 | Late | hedge_per_100 | 0.4589 | 268 |
| P3 | Late | n_words | 350.3284 | 268 |
| P3 | Late | persona_distance | 0.1835 | 268 |
| P4 | overall | has_question | 0.9888 | 804 |
| P4 | overall | plan_statement_present | 0.6505 | 804 |
| P4 | overall | empathy_phrases_present | 0.1642 | 804 |
| P4 | overall | hedge_per_100 | 0.4749 | 804 |
| P4 | overall | n_words | 312.2239 | 804 |
| P4 | overall | persona_distance | 0.2123 | 804 |
| P4 | Early | has_question | 1.0000 | 268 |
| P4 | Early | plan_statement_present | 0.5597 | 268 |
| P4 | Early | empathy_phrases_present | 0.1866 | 268 |
| P4 | Early | hedge_per_100 | 0.4948 | 268 |
| P4 | Early | n_words | 278.0187 | 268 |
| P4 | Early | persona_distance | 0.2137 | 268 |
| P4 | Middle | has_question | 0.9813 | 268 |
| P4 | Middle | plan_statement_present | 0.6791 | 268 |
| P4 | Middle | empathy_phrases_present | 0.1455 | 268 |
| P4 | Middle | hedge_per_100 | 0.4562 | 268 |
| P4 | Middle | n_words | 319.3881 | 268 |
| P4 | Middle | persona_distance | 0.2097 | 268 |
| P4 | Late | has_question | 0.9851 | 268 |
| P4 | Late | plan_statement_present | 0.7127 | 268 |
| P4 | Late | empathy_phrases_present | 0.1604 | 268 |
| P4 | Late | hedge_per_100 | 0.4736 | 268 |
| P4 | Late | n_words | 339.2649 | 268 |
| P4 | Late | persona_distance | 0.2135 | 268 |
| P5 | overall | has_question | 0.5299 | 804 |
| P5 | overall | plan_statement_present | 0.9701 | 804 |
| P5 | overall | empathy_phrases_present | 0.0112 | 804 |
| P5 | overall | hedge_per_100 | 0.1519 | 804 |
| P5 | overall | n_words | 328.3831 | 804 |
| P5 | overall | persona_distance | 0.2085 | 804 |
| P5 | Early | has_question | 0.6231 | 268 |
| P5 | Early | plan_statement_present | 0.9739 | 268 |
| P5 | Early | empathy_phrases_present | 0.0149 | 268 |
| P5 | Early | hedge_per_100 | 0.1354 | 268 |
| P5 | Early | n_words | 339.9739 | 268 |
| P5 | Early | persona_distance | 0.2204 | 268 |
| P5 | Middle | has_question | 0.4813 | 268 |
| P5 | Middle | plan_statement_present | 0.9664 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0075 | 268 |
| P5 | Middle | hedge_per_100 | 0.1597 | 268 |
| P5 | Middle | n_words | 318.0634 | 268 |
| P5 | Middle | persona_distance | 0.2060 | 268 |
| P5 | Late | has_question | 0.4851 | 268 |
| P5 | Late | plan_statement_present | 0.9701 | 268 |
| P5 | Late | empathy_phrases_present | 0.0112 | 268 |
| P5 | Late | hedge_per_100 | 0.1605 | 268 |
| P5 | Late | n_words | 327.1119 | 268 |
| P5 | Late | persona_distance | 0.1992 | 268 |

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
