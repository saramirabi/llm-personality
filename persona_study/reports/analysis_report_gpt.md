# gpt measurement report

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
| B1 | overall | 0.7840 | 0.7718 | 0.7966 | 0.1667 | 4824 |
| B1 | Early | 0.7718 | 0.7512 | 0.7917 | 0.1667 | 1608 |
| B1 | Middle | 0.8246 | 0.8047 | 0.8433 | 0.1667 | 1608 |
| B1 | Late | 0.7556 | 0.7332 | 0.7780 | 0.1667 | 1608 |
| B2 | overall | 0.5678 | 0.5543 | 0.5815 | 0.1667 | 4824 |
| B2 | Early | 0.5858 | 0.5628 | 0.6088 | 0.1667 | 1608 |
| B2 | Middle | 0.6014 | 0.5790 | 0.6244 | 0.1667 | 1608 |
| B2 | Late | 0.5162 | 0.4919 | 0.5386 | 0.1667 | 1608 |
| B3 | overall | 0.7796 | 0.7672 | 0.7931 | 0.1667 | 4824 |
| B3 | Early | 0.7606 | 0.7388 | 0.7811 | 0.1667 | 1608 |
| B3 | Middle | 0.8203 | 0.8010 | 0.8402 | 0.1667 | 1608 |
| B3 | Late | 0.7581 | 0.7351 | 0.7805 | 0.1667 | 1608 |
| B4 | overall | 0.6546 | 0.6412 | 0.6687 | 0.1667 | 4824 |
| B4 | Early | 0.6710 | 0.6474 | 0.6940 | 0.1667 | 1608 |
| B4 | Middle | 0.6716 | 0.6499 | 0.6934 | 0.1667 | 1608 |
| B4 | Late | 0.6213 | 0.5983 | 0.6437 | 0.1667 | 1608 |
| B5 | overall | 0.2828 | 0.2728 | 0.2931 | 0.1667 | 4824 |
| B5 | Early | 0.2886 | 0.2718 | 0.3047 | 0.1667 | 1608 |
| B5 | Middle | 0.3221 | 0.3035 | 0.3402 | 0.1667 | 1608 |
| B5 | Late | 0.2376 | 0.2233 | 0.2519 | 0.1667 | 1608 |
| B6 | overall | 0.8167 | 0.8042 | 0.8294 | 0.2000 | 4020 |
| B6 | Early | 0.8142 | 0.7933 | 0.8358 | 0.2000 | 1340 |
| B6 | Middle | 0.8418 | 0.8216 | 0.8604 | 0.2000 | 1340 |
| B6 | Late | 0.7940 | 0.7716 | 0.8149 | 0.2000 | 1340 |
| B7 | overall | 0.8522 | 0.8420 | 0.8628 | 0.2000 | 4824 |
| B7 | Early | 0.8514 | 0.8358 | 0.8669 | 0.2000 | 1608 |
| B7 | Middle | 0.8806 | 0.8638 | 0.8974 | 0.2000 | 1608 |
| B7 | Late | 0.8246 | 0.8041 | 0.8451 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.7562 | 0.7251 | 0.7861 | 0.1667 | 804 |
| B1 | overall | P1 | 0.7313 | 0.6978 | 0.7624 | 0.1667 | 804 |
| B1 | overall | P2 | 0.6443 | 0.6082 | 0.6791 | 0.1667 | 804 |
| B1 | overall | P3 | 0.8308 | 0.8035 | 0.8582 | 0.1667 | 804 |
| B1 | overall | P4 | 0.8545 | 0.8296 | 0.8781 | 0.1667 | 804 |
| B1 | overall | P5 | 0.8868 | 0.8632 | 0.9104 | 0.1667 | 804 |
| B1 | Early | P0 | 0.6269 | 0.5672 | 0.6828 | 0.1667 | 268 |
| B1 | Early | P1 | 0.7164 | 0.6604 | 0.7724 | 0.1667 | 268 |
| B1 | Early | P2 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 268 |
| B1 | Early | P3 | 0.8545 | 0.8097 | 0.8955 | 0.1667 | 268 |
| B1 | Early | P4 | 0.9478 | 0.9179 | 0.9739 | 0.1667 | 268 |
| B1 | Early | P5 | 0.8246 | 0.7761 | 0.8731 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.8284 | 0.7835 | 0.8731 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.7948 | 0.7463 | 0.8396 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.6754 | 0.6157 | 0.7313 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.8358 | 0.7910 | 0.8769 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.8769 | 0.8396 | 0.9142 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.9366 | 0.9067 | 0.9627 | 0.1667 | 268 |
| B1 | Late | P0 | 0.8134 | 0.7687 | 0.8582 | 0.1667 | 268 |
| B1 | Late | P1 | 0.6828 | 0.6269 | 0.7388 | 0.1667 | 268 |
| B1 | Late | P2 | 0.5970 | 0.5373 | 0.6531 | 0.1667 | 268 |
| B1 | Late | P3 | 0.8022 | 0.7537 | 0.8471 | 0.1667 | 268 |
| B1 | Late | P4 | 0.7388 | 0.6866 | 0.7910 | 0.1667 | 268 |
| B1 | Late | P5 | 0.8993 | 0.8619 | 0.9328 | 0.1667 | 268 |
| B2 | overall | P0 | 0.5261 | 0.4900 | 0.5609 | 0.1667 | 804 |
| B2 | overall | P1 | 0.6654 | 0.6306 | 0.6990 | 0.1667 | 804 |
| B2 | overall | P2 | 0.3259 | 0.2910 | 0.3595 | 0.1667 | 804 |
| B2 | overall | P3 | 0.5485 | 0.5124 | 0.5846 | 0.1667 | 804 |
| B2 | overall | P4 | 0.7214 | 0.6878 | 0.7537 | 0.1667 | 804 |
| B2 | overall | P5 | 0.6194 | 0.5871 | 0.6530 | 0.1667 | 804 |
| B2 | Early | P0 | 0.4179 | 0.3582 | 0.4776 | 0.1667 | 268 |
| B2 | Early | P1 | 0.7127 | 0.6604 | 0.7649 | 0.1667 | 268 |
| B2 | Early | P2 | 0.3433 | 0.2873 | 0.3993 | 0.1667 | 268 |
| B2 | Early | P3 | 0.5410 | 0.4776 | 0.6007 | 0.1667 | 268 |
| B2 | Early | P4 | 0.8060 | 0.7575 | 0.8545 | 0.1667 | 268 |
| B2 | Early | P5 | 0.6940 | 0.6418 | 0.7501 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.5970 | 0.5373 | 0.6604 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.7500 | 0.6978 | 0.8022 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.2985 | 0.2463 | 0.3545 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.5933 | 0.5336 | 0.6530 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.7313 | 0.6754 | 0.7836 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.6381 | 0.5784 | 0.6940 | 0.1667 | 268 |
| B2 | Late | P0 | 0.5634 | 0.5037 | 0.6231 | 0.1667 | 268 |
| B2 | Late | P1 | 0.5336 | 0.4701 | 0.5896 | 0.1667 | 268 |
| B2 | Late | P2 | 0.3358 | 0.2761 | 0.3918 | 0.1667 | 268 |
| B2 | Late | P3 | 0.5112 | 0.4515 | 0.5709 | 0.1667 | 268 |
| B2 | Late | P4 | 0.6269 | 0.5672 | 0.6828 | 0.1667 | 268 |
| B2 | Late | P5 | 0.5261 | 0.4664 | 0.5896 | 0.1667 | 268 |
| B3 | overall | P0 | 0.7500 | 0.7189 | 0.7811 | 0.1667 | 804 |
| B3 | overall | P1 | 0.7313 | 0.7002 | 0.7624 | 0.1667 | 804 |
| B3 | overall | P2 | 0.6430 | 0.6069 | 0.6803 | 0.1667 | 804 |
| B3 | overall | P3 | 0.8308 | 0.8035 | 0.8570 | 0.1667 | 804 |
| B3 | overall | P4 | 0.8483 | 0.8234 | 0.8731 | 0.1667 | 804 |
| B3 | overall | P5 | 0.8744 | 0.8507 | 0.8980 | 0.1667 | 804 |
| B3 | Early | P0 | 0.6194 | 0.5634 | 0.6754 | 0.1667 | 268 |
| B3 | Early | P1 | 0.7090 | 0.6530 | 0.7612 | 0.1667 | 268 |
| B3 | Early | P2 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 268 |
| B3 | Early | P3 | 0.8657 | 0.8246 | 0.9067 | 0.1667 | 268 |
| B3 | Early | P4 | 0.9403 | 0.9104 | 0.9664 | 0.1667 | 268 |
| B3 | Early | P5 | 0.7687 | 0.7163 | 0.8209 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.8209 | 0.7761 | 0.8657 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.7948 | 0.7463 | 0.8396 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.6679 | 0.6082 | 0.7239 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.8284 | 0.7836 | 0.8731 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.8731 | 0.8357 | 0.9104 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.9366 | 0.9067 | 0.9664 | 0.1667 | 268 |
| B3 | Late | P0 | 0.8097 | 0.7612 | 0.8545 | 0.1667 | 268 |
| B3 | Late | P1 | 0.6903 | 0.6342 | 0.7425 | 0.1667 | 268 |
| B3 | Late | P2 | 0.6007 | 0.5410 | 0.6604 | 0.1667 | 268 |
| B3 | Late | P3 | 0.7985 | 0.7536 | 0.8470 | 0.1667 | 268 |
| B3 | Late | P4 | 0.7313 | 0.6790 | 0.7836 | 0.1667 | 268 |
| B3 | Late | P5 | 0.9179 | 0.8843 | 0.9479 | 0.1667 | 268 |
| B4 | overall | P0 | 0.5871 | 0.5522 | 0.6219 | 0.1667 | 804 |
| B4 | overall | P1 | 0.6368 | 0.6032 | 0.6716 | 0.1667 | 804 |
| B4 | overall | P2 | 0.4913 | 0.4565 | 0.5261 | 0.1667 | 804 |
| B4 | overall | P3 | 0.7438 | 0.7114 | 0.7761 | 0.1667 | 804 |
| B4 | overall | P4 | 0.7699 | 0.7388 | 0.7985 | 0.1667 | 804 |
| B4 | overall | P5 | 0.6990 | 0.6667 | 0.7313 | 0.1667 | 804 |
| B4 | Early | P0 | 0.4963 | 0.4402 | 0.5522 | 0.1667 | 268 |
| B4 | Early | P1 | 0.7537 | 0.7015 | 0.8060 | 0.1667 | 268 |
| B4 | Early | P2 | 0.5933 | 0.5336 | 0.6530 | 0.1667 | 268 |
| B4 | Early | P3 | 0.8060 | 0.7612 | 0.8507 | 0.1667 | 268 |
| B4 | Early | P4 | 0.8881 | 0.8507 | 0.9254 | 0.1667 | 268 |
| B4 | Early | P5 | 0.4888 | 0.4254 | 0.5485 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.6231 | 0.5634 | 0.6792 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.6940 | 0.6343 | 0.7463 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.4478 | 0.3918 | 0.5075 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.7201 | 0.6679 | 0.7724 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.7463 | 0.6940 | 0.7985 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.7985 | 0.7500 | 0.8470 | 0.1667 | 268 |
| B4 | Late | P0 | 0.6418 | 0.5858 | 0.6978 | 0.1667 | 268 |
| B4 | Late | P1 | 0.4627 | 0.4030 | 0.5261 | 0.1667 | 268 |
| B4 | Late | P2 | 0.4328 | 0.3694 | 0.4925 | 0.1667 | 268 |
| B4 | Late | P3 | 0.7052 | 0.6493 | 0.7576 | 0.1667 | 268 |
| B4 | Late | P4 | 0.6754 | 0.6157 | 0.7276 | 0.1667 | 268 |
| B4 | Late | P5 | 0.8097 | 0.7612 | 0.8545 | 0.1667 | 268 |
| B5 | overall | P0 | 0.0908 | 0.0709 | 0.1119 | 0.1667 | 804 |
| B5 | overall | P1 | 0.6206 | 0.5883 | 0.6505 | 0.1667 | 804 |
| B5 | overall | P2 | 0.0137 | 0.0062 | 0.0224 | 0.1667 | 804 |
| B5 | overall | P3 | 0.6903 | 0.6580 | 0.7226 | 0.1667 | 804 |
| B5 | overall | P4 | 0.2015 | 0.1741 | 0.2301 | 0.1667 | 804 |
| B5 | overall | P5 | 0.0796 | 0.0622 | 0.0995 | 0.1667 | 804 |
| B5 | Early | P0 | 0.1007 | 0.0672 | 0.1381 | 0.1667 | 268 |
| B5 | Early | P1 | 0.8955 | 0.8582 | 0.9328 | 0.1667 | 268 |
| B5 | Early | P2 | 0.0373 | 0.0149 | 0.0597 | 0.1667 | 268 |
| B5 | Early | P3 | 0.4478 | 0.3881 | 0.5112 | 0.1667 | 268 |
| B5 | Early | P4 | 0.2090 | 0.1604 | 0.2575 | 0.1667 | 268 |
| B5 | Early | P5 | 0.0410 | 0.0187 | 0.0672 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.1082 | 0.0709 | 0.1455 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.6903 | 0.6343 | 0.7463 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.0037 | 0.0000 | 0.0112 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.8060 | 0.7575 | 0.8507 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.2164 | 0.1679 | 0.2687 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.1082 | 0.0746 | 0.1493 | 0.1667 | 268 |
| B5 | Late | P0 | 0.0634 | 0.0373 | 0.0933 | 0.1667 | 268 |
| B5 | Late | P1 | 0.2761 | 0.2239 | 0.3321 | 0.1667 | 268 |
| B5 | Late | P2 | 0.0000 | 0.0000 | 0.0000 | 0.1667 | 268 |
| B5 | Late | P3 | 0.8172 | 0.7687 | 0.8619 | 0.1667 | 268 |
| B5 | Late | P4 | 0.1791 | 0.1343 | 0.2276 | 0.1667 | 268 |
| B5 | Late | P5 | 0.0896 | 0.0560 | 0.1269 | 0.1667 | 268 |
| B6 | overall | P1 | 0.7537 | 0.7226 | 0.7836 | 0.2000 | 804 |
| B6 | overall | P2 | 0.7363 | 0.7040 | 0.7687 | 0.2000 | 804 |
| B6 | overall | P3 | 0.8408 | 0.8147 | 0.8669 | 0.2000 | 804 |
| B6 | overall | P4 | 0.8570 | 0.8321 | 0.8806 | 0.2000 | 804 |
| B6 | overall | P5 | 0.8955 | 0.8731 | 0.9179 | 0.2000 | 804 |
| B6 | Early | P1 | 0.7537 | 0.6978 | 0.8060 | 0.2000 | 268 |
| B6 | Early | P2 | 0.6828 | 0.6305 | 0.7351 | 0.2000 | 268 |
| B6 | Early | P3 | 0.8619 | 0.8172 | 0.9030 | 0.2000 | 268 |
| B6 | Early | P4 | 0.9478 | 0.9179 | 0.9739 | 0.2000 | 268 |
| B6 | Early | P5 | 0.8246 | 0.7761 | 0.8731 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.7985 | 0.7463 | 0.8433 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.7500 | 0.6940 | 0.8022 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.8396 | 0.7948 | 0.8806 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.8769 | 0.8396 | 0.9142 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.9440 | 0.9142 | 0.9701 | 0.2000 | 268 |
| B6 | Late | P1 | 0.7090 | 0.6530 | 0.7612 | 0.2000 | 268 |
| B6 | Late | P2 | 0.7761 | 0.7275 | 0.8284 | 0.2000 | 268 |
| B6 | Late | P3 | 0.8209 | 0.7761 | 0.8657 | 0.2000 | 268 |
| B6 | Late | P4 | 0.7463 | 0.6903 | 0.7949 | 0.2000 | 268 |
| B6 | Late | P5 | 0.9179 | 0.8806 | 0.9478 | 0.2000 | 268 |
| B7 | overall | P0 | 0.7139 | 0.6803 | 0.7463 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.9241 | 0.9104 | 0.9372 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.8321 | 0.8035 | 0.8595 | 0.2000 | 804 |
| B7 | overall | P4 | 0.8545 | 0.8296 | 0.8794 | 0.2000 | 804 |
| B7 | overall | P5 | 0.8644 | 0.8383 | 0.8893 | 0.2000 | 804 |
| B7 | Early | P0 | 0.5746 | 0.5149 | 0.6306 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.9608 | 0.9440 | 0.9757 | 0.2000 | 536 |
| B7 | Early | P3 | 0.8657 | 0.8209 | 0.9067 | 0.2000 | 268 |
| B7 | Early | P4 | 0.9478 | 0.9179 | 0.9739 | 0.2000 | 268 |
| B7 | Early | P5 | 0.7985 | 0.7500 | 0.8470 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.7873 | 0.7388 | 0.8358 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.9347 | 0.9123 | 0.9552 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.8321 | 0.7873 | 0.8769 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.8731 | 0.8321 | 0.9104 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.9216 | 0.8881 | 0.9515 | 0.2000 | 268 |
| B7 | Late | P0 | 0.7799 | 0.7313 | 0.8284 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.8769 | 0.8470 | 0.9067 | 0.2000 | 536 |
| B7 | Late | P3 | 0.7985 | 0.7500 | 0.8433 | 0.2000 | 268 |
| B7 | Late | P4 | 0.7425 | 0.6902 | 0.7948 | 0.2000 | 268 |
| B7 | Late | P5 | 0.8731 | 0.8321 | 0.9142 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | 1.0931 | 0.4892 | 0.0254 | 0.1343 | 2.0519 |
| C(position, Treatment(reference='Early'))[T.Late] | -0.1202 | 0.1359 | 0.3765 | -0.3864 | 0.1461 |
| C(position, Treatment(reference='Early'))[T.Middle] | 0.3089 | 0.1141 | 0.0068 | 0.0854 | 0.5325 |
| log_context | 0.0226 | 0.0866 | 0.7943 | -0.1472 | 0.1923 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1973 | -0.2936 | -0.1036 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1585 | -0.3121 | -0.0098 | 0.0350 | 0.1050 | 268 | confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1359 | -0.2986 | 0.0215 | 0.0940 | 0.1080 | 268 | not confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.2976 | -0.4998 | -0.1015 | 0.0030 | 0.0120 | 268 | confirmed |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | 2.8447 | 2.3394 | 3.3576 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | 1.3897 | 0.4132 | 2.3227 | 0.0080 | 0.0080 | 268 | confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | 4.1108 | 3.3202 | 4.8992 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | 3.0335 | 2.3736 | 3.7278 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | -0.2299 | -0.2765 | -0.1842 | 0.0000 | 0.0000 | 507 | confirmed |
| Early | P1 - P0 | share_open | lower | pre-specified | -0.0950 | -0.1573 | -0.0319 | 0.0010 | 0.0040 | 222 | confirmed |
| Middle | P1 - P0 | share_open | lower | pre-specified | -0.3214 | -0.3958 | -0.2411 | 0.0000 | 0.0000 | 168 | confirmed |
| Late | P1 - P0 | share_open | lower | pre-specified | -0.3547 | -0.4487 | -0.2650 | 0.0000 | 0.0000 | 117 | confirmed |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.2870 | 0.1866 | 0.3852 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.3169 | 0.1589 | 0.4814 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1524 | -0.0016 | 0.2950 | 0.0540 | 0.1080 | 268 | not confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.3917 | 0.1965 | 0.5870 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 3.6076 | 3.4033 | 3.8055 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 4.6368 | 4.3117 | 4.9414 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 3.4579 | 3.1684 | 3.7607 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 2.7280 | 2.4038 | 3.0650 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.1908 | 0.1447 | 0.2351 | 0.0000 | 0.0000 | 631 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.0703 | 0.0028 | 0.1378 | 0.0390 | 0.0540 | 205 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.1840 | 0.1061 | 0.2642 | 0.0000 | 0.0000 | 212 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.3131 | 0.2243 | 0.3988 | 0.0000 | 0.0000 | 214 | confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 5.7018 | 5.4594 | 5.9419 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 7.1236 | 6.7578 | 7.4779 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 5.2417 | 4.8499 | 5.6082 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 4.7400 | 4.3127 | 5.1660 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.2305 | 0.1836 | 0.2755 | 0.0000 | 0.0000 | 645 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.2395 | 0.1689 | 0.3078 | 0.0000 | 0.0000 | 222 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.2193 | 0.1392 | 0.3019 | 0.0000 | 0.0000 | 212 | confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | 0.2322 | 0.1493 | 0.3104 | 0.0000 | 0.0000 | 211 | confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -3.2202 | -3.6687 | -2.7897 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -5.3496 | -6.1829 | -4.5426 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -1.9533 | -2.5650 | -1.3429 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -2.3577 | -2.9768 | -1.7280 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.0942 | 1.8478 | 2.3260 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.4867 | 2.0902 | 2.8682 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.7838 | 1.3880 | 2.1376 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.0120 | 1.5598 | 2.4748 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -1.2978 | -1.6164 | -0.9651 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -1.6446 | -2.2230 | -1.0694 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -1.0512 | -1.6010 | -0.4840 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -1.1977 | -1.7057 | -0.6480 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3887 | 0.3314 | 0.4474 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.4095 | 0.3122 | 0.5059 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.4121 | 0.3333 | 0.4992 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.3445 | 0.2634 | 0.4286 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0361 | -0.0572 | -0.0163 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0514 | -0.0937 | -0.0170 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0229 | -0.0581 | 0.0119 | 0.1980 | 0.1980 | 268 | not confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0341 | -0.0743 | 0.0045 | 0.0920 | 0.1840 | 268 | not confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | -0.1322 | -0.1870 | -0.0768 | 0.0000 | 0.0000 | 198 | confirmed |
| Early | P5 - P0 | share_open | lower | pre-specified | -0.0777 | -0.1384 | -0.0184 | 0.0180 | 0.0540 | 118 | confirmed |
| Middle | P5 - P0 | share_open | lower | pre-specified | -0.1667 | -0.3114 | -0.0222 | 0.0220 | 0.0540 | 45 | confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | -0.2714 | -0.4146 | -0.1286 | 0.0000 | 0.0000 | 35 | confirmed |
| overall | P5 - P0 | has_question | lower | pre-specified | -0.5933 | -0.6306 | -0.5547 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | has_question | lower | pre-specified | -0.3881 | -0.4515 | -0.3209 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | has_question | lower | pre-specified | -0.6604 | -0.7164 | -0.6007 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | has_question | lower | pre-specified | -0.7313 | -0.7873 | -0.6754 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | plan_statement_present | higher | pre-specified | 0.4552 | 0.4179 | 0.4913 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | pre-specified | 0.2799 | 0.2164 | 0.3396 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | pre-specified | 0.5187 | 0.4478 | 0.5821 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | pre-specified | 0.5672 | 0.5075 | 0.6270 | 0.0000 | 0.0000 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1391 | -0.3965 | 0.1062 | 0.2870 | 0.5740 | not confirmed |
| P1 - P0 | med_per_100 | higher | pre-specified | 1.6438 | 0.5580 | 2.8148 | 0.0010 | 0.0020 | opposite |
| P1 - P0 | share_open | lower | pre-specified | -0.2597 | -0.3722 | -0.1541 | 0.0000 | 0.0000 | opposite |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.0748 | -0.1746 | 0.3169 | 0.5890 | 0.5890 | not confirmed |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | -1.9089 | -2.3474 | -1.4961 | 0.0000 | 0.0000 | confirmed |
| P3 - P0 | share_open | higher | pre-specified | 0.2428 | 0.1383 | 0.3435 | 0.0000 | 0.0000 | opposite |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -2.3836 | -2.9039 | -1.8437 | 0.0000 | 0.0000 | confirmed |
| P4 - P0 | share_open | higher | pre-specified | -0.0073 | -0.1153 | 0.0989 | 0.9050 | 0.9050 | not confirmed |
| P4 - P0 | med_per_100 | lower | pre-specified | 2.9918 | 1.9267 | 3.9969 | 0.0000 | 0.0000 | confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.4747 | -1.0639 | 0.1152 | 0.1100 | 0.3300 | not confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | 0.4468 | -0.2947 | 1.2324 | 0.2430 | 0.2430 | not confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | -0.0650 | -0.1848 | 0.0538 | 0.2880 | 0.2880 | not confirmed |
| P5 - P0 | n_leading | higher | pre-specified | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0174 | -0.0419 | 0.0769 | 0.5450 | 0.5450 | not confirmed |
| P5 - P0 | share_open | lower | pre-specified | -0.1937 | -0.3494 | -0.0439 | 0.0060 | 0.0120 | opposite |
| P5 - P0 | has_question | lower | pre-specified | -0.3433 | -0.4291 | -0.2575 | 0.0000 | 0.0000 | opposite |
| P5 - P0 | plan_statement_present | higher | pre-specified | 0.2873 | 0.2015 | 0.3731 | 0.0000 | 0.0000 | opposite |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.7313 | 0.6978 | 0.7624 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P2 | 0.6443 | 0.6082 | 0.6791 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.8308 | 0.8035 | 0.8582 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.8545 | 0.8296 | 0.8781 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.8868 | 0.8632 | 0.9104 | 0.1667 | 1 | 4 | 3 | 0 | not realised |
| Early | P1 | 0.7164 | 0.6604 | 0.7724 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P2 | 0.6604 | 0.6045 | 0.7164 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.8545 | 0.8097 | 0.8955 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.9478 | 0.9179 | 0.9739 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 0.8246 | 0.7761 | 0.8731 | 0.1667 | 1 | 4 | 3 | 0 | not realised |
| Middle | P1 | 0.7948 | 0.7463 | 0.8396 | 0.1667 | 1 | 3 | 2 | 0 | not realised |
| Middle | P2 | 0.6754 | 0.6157 | 0.7313 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.8358 | 0.7910 | 0.8769 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.8769 | 0.8396 | 0.9142 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Middle | P5 | 0.9366 | 0.9067 | 0.9627 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Late | P1 | 0.6828 | 0.6269 | 0.7388 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P2 | 0.5970 | 0.5373 | 0.6531 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.8022 | 0.7537 | 0.8471 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Late | P4 | 0.7388 | 0.6866 | 0.7910 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P5 | 0.8993 | 0.8619 | 0.9328 | 0.1667 | 1 | 4 | 2 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.8794 | 804 |
| P0 | overall | plan_statement_present | 0.1791 | 804 |
| P0 | overall | empathy_phrases_present | 0.3396 | 804 |
| P0 | overall | hedge_per_100 | 1.2722 | 804 |
| P0 | overall | n_words | 60.8172 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.9067 | 268 |
| P0 | Early | plan_statement_present | 0.1194 | 268 |
| P0 | Early | empathy_phrases_present | 0.2948 | 268 |
| P0 | Early | hedge_per_100 | 0.8031 | 268 |
| P0 | Early | n_words | 44.9925 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.8582 | 268 |
| P0 | Middle | plan_statement_present | 0.2015 | 268 |
| P0 | Middle | empathy_phrases_present | 0.2836 | 268 |
| P0 | Middle | hedge_per_100 | 1.5536 | 268 |
| P0 | Middle | n_words | 68.3657 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.8731 | 268 |
| P0 | Late | plan_statement_present | 0.2164 | 268 |
| P0 | Late | empathy_phrases_present | 0.4403 | 268 |
| P0 | Late | hedge_per_100 | 1.4598 | 268 |
| P0 | Late | n_words | 69.0933 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.7662 | 804 |
| P1 | overall | plan_statement_present | 0.1294 | 804 |
| P1 | overall | empathy_phrases_present | 0.0137 | 804 |
| P1 | overall | hedge_per_100 | 0.3434 | 804 |
| P1 | overall | n_words | 42.6517 | 804 |
| P1 | overall | persona_distance | 0.3998 | 804 |
| P1 | Early | has_question | 0.9888 | 268 |
| P1 | Early | plan_statement_present | 0.0037 | 268 |
| P1 | Early | empathy_phrases_present | 0.0000 | 268 |
| P1 | Early | hedge_per_100 | 0.0388 | 268 |
| P1 | Early | n_words | 26.7052 | 268 |
| P1 | Early | persona_distance | 0.4034 | 268 |
| P1 | Middle | has_question | 0.7873 | 268 |
| P1 | Middle | plan_statement_present | 0.1194 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0149 | 268 |
| P1 | Middle | hedge_per_100 | 0.3908 | 268 |
| P1 | Middle | n_words | 38.3060 | 268 |
| P1 | Middle | persona_distance | 0.4806 | 268 |
| P1 | Late | has_question | 0.5224 | 268 |
| P1 | Late | plan_statement_present | 0.2649 | 268 |
| P1 | Late | empathy_phrases_present | 0.0261 | 268 |
| P1 | Late | hedge_per_100 | 0.6005 | 268 |
| P1 | Late | n_words | 62.9440 | 268 |
| P1 | Late | persona_distance | 0.3153 | 268 |
| P2 | overall | has_question | 0.8470 | 804 |
| P2 | overall | plan_statement_present | 0.1430 | 804 |
| P2 | overall | empathy_phrases_present | 0.1343 | 804 |
| P2 | overall | hedge_per_100 | 0.7896 | 804 |
| P2 | overall | n_words | 70.3943 | 804 |
| P2 | overall | persona_distance | 0.3117 | 804 |
| P2 | Early | has_question | 0.9627 | 268 |
| P2 | Early | plan_statement_present | 0.0261 | 268 |
| P2 | Early | empathy_phrases_present | 0.1007 | 268 |
| P2 | Early | hedge_per_100 | 0.3265 | 268 |
| P2 | Early | n_words | 49.7985 | 268 |
| P2 | Early | persona_distance | 0.3459 | 268 |
| P2 | Middle | has_question | 0.8321 | 268 |
| P2 | Middle | plan_statement_present | 0.1604 | 268 |
| P2 | Middle | empathy_phrases_present | 0.1269 | 268 |
| P2 | Middle | hedge_per_100 | 1.0302 | 268 |
| P2 | Middle | n_words | 76.6567 | 268 |
| P2 | Middle | persona_distance | 0.3148 | 268 |
| P2 | Late | has_question | 0.7463 | 268 |
| P2 | Late | plan_statement_present | 0.2425 | 268 |
| P2 | Late | empathy_phrases_present | 0.1754 | 268 |
| P2 | Late | hedge_per_100 | 1.0120 | 268 |
| P2 | Late | n_words | 84.7276 | 268 |
| P2 | Late | persona_distance | 0.2744 | 268 |
| P3 | overall | has_question | 0.9913 | 804 |
| P3 | overall | plan_statement_present | 0.1256 | 804 |
| P3 | overall | empathy_phrases_present | 0.6206 | 804 |
| P3 | overall | hedge_per_100 | 1.1085 | 804 |
| P3 | overall | n_words | 96.7351 | 804 |
| P3 | overall | persona_distance | 0.3305 | 804 |
| P3 | Early | has_question | 0.9963 | 268 |
| P3 | Early | plan_statement_present | 0.0336 | 268 |
| P3 | Early | empathy_phrases_present | 0.5299 | 268 |
| P3 | Early | hedge_per_100 | 0.8580 | 268 |
| P3 | Early | n_words | 84.2201 | 268 |
| P3 | Early | persona_distance | 0.3623 | 268 |
| P3 | Middle | has_question | 0.9888 | 268 |
| P3 | Middle | plan_statement_present | 0.1642 | 268 |
| P3 | Middle | empathy_phrases_present | 0.6343 | 268 |
| P3 | Middle | hedge_per_100 | 1.2054 | 268 |
| P3 | Middle | n_words | 101.5485 | 268 |
| P3 | Middle | persona_distance | 0.3204 | 268 |
| P3 | Late | has_question | 0.9888 | 268 |
| P3 | Late | plan_statement_present | 0.1791 | 268 |
| P3 | Late | empathy_phrases_present | 0.6978 | 268 |
| P3 | Late | hedge_per_100 | 1.2622 | 268 |
| P3 | Late | n_words | 104.4366 | 268 |
| P3 | Late | persona_distance | 0.3086 | 268 |
| P4 | overall | has_question | 0.9813 | 804 |
| P4 | overall | plan_statement_present | 0.1182 | 804 |
| P4 | overall | empathy_phrases_present | 0.7873 | 804 |
| P4 | overall | hedge_per_100 | 0.8559 | 804 |
| P4 | overall | n_words | 77.1244 | 804 |
| P4 | overall | persona_distance | 0.4082 | 804 |
| P4 | Early | has_question | 0.9963 | 268 |
| P4 | Early | plan_statement_present | 0.0485 | 268 |
| P4 | Early | empathy_phrases_present | 0.8097 | 268 |
| P4 | Early | hedge_per_100 | 0.5476 | 268 |
| P4 | Early | n_words | 64.7873 | 268 |
| P4 | Early | persona_distance | 0.4737 | 268 |
| P4 | Middle | has_question | 0.9888 | 268 |
| P4 | Middle | plan_statement_present | 0.1231 | 268 |
| P4 | Middle | empathy_phrases_present | 0.7761 | 268 |
| P4 | Middle | hedge_per_100 | 1.0449 | 268 |
| P4 | Middle | n_words | 81.0746 | 268 |
| P4 | Middle | persona_distance | 0.3883 | 268 |
| P4 | Late | has_question | 0.9590 | 268 |
| P4 | Late | plan_statement_present | 0.1828 | 268 |
| P4 | Late | empathy_phrases_present | 0.7761 | 268 |
| P4 | Late | hedge_per_100 | 0.9753 | 268 |
| P4 | Late | n_words | 85.5112 | 268 |
| P4 | Late | persona_distance | 0.3627 | 268 |
| P5 | overall | has_question | 0.2861 | 804 |
| P5 | overall | plan_statement_present | 0.6343 | 804 |
| P5 | overall | empathy_phrases_present | 0.1045 | 804 |
| P5 | overall | hedge_per_100 | 0.4957 | 804 |
| P5 | overall | n_words | 72.0162 | 804 |
| P5 | overall | persona_distance | 0.2982 | 804 |
| P5 | Early | has_question | 0.5187 | 268 |
| P5 | Early | plan_statement_present | 0.3993 | 268 |
| P5 | Early | empathy_phrases_present | 0.1119 | 268 |
| P5 | Early | hedge_per_100 | 0.3556 | 268 |
| P5 | Early | n_words | 53.8769 | 268 |
| P5 | Early | persona_distance | 0.3339 | 268 |
| P5 | Middle | has_question | 0.1978 | 268 |
| P5 | Middle | plan_statement_present | 0.7201 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0858 | 268 |
| P5 | Middle | hedge_per_100 | 0.5638 | 268 |
| P5 | Middle | n_words | 79.0896 | 268 |
| P5 | Middle | persona_distance | 0.2951 | 268 |
| P5 | Late | has_question | 0.1418 | 268 |
| P5 | Late | plan_statement_present | 0.7836 | 268 |
| P5 | Late | empathy_phrases_present | 0.1157 | 268 |
| P5 | Late | hedge_per_100 | 0.5676 | 268 |
| P5 | Late | n_words | 83.0821 | 268 |
| P5 | Late | persona_distance | 0.2656 | 268 |

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
