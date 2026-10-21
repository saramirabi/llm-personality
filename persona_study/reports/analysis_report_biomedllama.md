# biomedllama measurement report

Plan SHA-256: `e33bdf0004f1e97aa30a4e8dd1a124f1bc20586c4104f7eeb9d3434654cfff73`
Erratum 1 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) plan SHA-256 before this erratum: `56679285fb538ddfe04723dfadca09a1a34418ff6ba766cc55fa559c86675cc6`
Erratum 4 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 4 (2026-10-02) plan SHA-256 before this erratum: `c1747f993babaa05f8dd3c99543584d8555cb9212138a92e909972505a210450`
Erratum 5 (2026-10-05) plan SHA-256 before this erratum: `7b85c86fc37013b4e42e3a46c77bdef4cf6073171add570ca9879b7f7c896455`
Erratum 6 (2026-10-05) plan SHA-256 before this erratum: `01f67a5b0a8fa45deb692ceaea5f1420b7778b9cdfffc9808a6b91cde966e322`
Prompt SHA-256: `2314d1cccef40ae12b89bf36a09508adf2122cc25e49b606faa65b8f9bda3d19`

No generation was run. Measurements use `analysis_text` only.

## Data

- Output rows: 4824
- Missing `analysis_text`: 0. Those rows stay in the feature file and are excluded from calculations.
- Rows in the calculations: 4824
- Contexts: 804
- Rows by condition: {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
- Rows by position: {'Early': 1608, 'Late': 1608, 'Middle': 1608}
- Rows with any format flag, among analysed rows: 46
- Persona content words removed for the echo controls: 55

## Part B accuracy

| variant | scope | accuracy | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | 0.3646 | 0.3514 | 0.3785 | 0.1667 | 4824 |
| B1 | Early | 0.3818 | 0.3570 | 0.4042 | 0.1667 | 1608 |
| B1 | Middle | 0.3588 | 0.3358 | 0.3812 | 0.1667 | 1608 |
| B1 | Late | 0.3532 | 0.3315 | 0.3769 | 0.1667 | 1608 |
| B2 | overall | 0.2525 | 0.2398 | 0.2645 | 0.1667 | 4824 |
| B2 | Early | 0.2736 | 0.2519 | 0.2954 | 0.1667 | 1608 |
| B2 | Middle | 0.2456 | 0.2239 | 0.2680 | 0.1667 | 1608 |
| B2 | Late | 0.2382 | 0.2183 | 0.2575 | 0.1667 | 1608 |
| B3 | overall | 0.3599 | 0.3462 | 0.3738 | 0.1667 | 4824 |
| B3 | Early | 0.3706 | 0.3470 | 0.3943 | 0.1667 | 1608 |
| B3 | Middle | 0.3613 | 0.3377 | 0.3843 | 0.1667 | 1608 |
| B3 | Late | 0.3476 | 0.3265 | 0.3706 | 0.1667 | 1608 |
| B4 | overall | 0.3016 | 0.2894 | 0.3136 | 0.1667 | 4824 |
| B4 | Early | 0.3184 | 0.2979 | 0.3389 | 0.1667 | 1608 |
| B4 | Middle | 0.3072 | 0.2867 | 0.3265 | 0.1667 | 1608 |
| B4 | Late | 0.2792 | 0.2562 | 0.3004 | 0.1667 | 1608 |
| B5 | overall | 0.2085 | 0.2002 | 0.2164 | 0.1667 | 4824 |
| B5 | Early | 0.2077 | 0.1928 | 0.2226 | 0.1667 | 1608 |
| B5 | Middle | 0.2158 | 0.2002 | 0.2320 | 0.1667 | 1608 |
| B5 | Late | 0.2021 | 0.1878 | 0.2158 | 0.1667 | 1608 |
| B6 | overall | 0.4204 | 0.4055 | 0.4353 | 0.2000 | 4020 |
| B6 | Early | 0.4403 | 0.4157 | 0.4657 | 0.2000 | 1340 |
| B6 | Middle | 0.4269 | 0.4015 | 0.4515 | 0.2000 | 1340 |
| B6 | Late | 0.3940 | 0.3701 | 0.4201 | 0.2000 | 1340 |
| B7 | overall | 0.4536 | 0.4407 | 0.4664 | 0.2000 | 4824 |
| B7 | Early | 0.4757 | 0.4521 | 0.4981 | 0.2000 | 1608 |
| B7 | Middle | 0.4527 | 0.4297 | 0.4739 | 0.2000 | 1608 |
| B7 | Late | 0.4322 | 0.4086 | 0.4559 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.3010 | 0.2674 | 0.3321 | 0.1667 | 804 |
| B1 | overall | P1 | 0.3134 | 0.2836 | 0.3433 | 0.1667 | 804 |
| B1 | overall | P2 | 0.2450 | 0.2152 | 0.2774 | 0.1667 | 804 |
| B1 | overall | P3 | 0.3694 | 0.3346 | 0.4018 | 0.1667 | 804 |
| B1 | overall | P4 | 0.3905 | 0.3582 | 0.4241 | 0.1667 | 804 |
| B1 | overall | P5 | 0.5684 | 0.5336 | 0.6032 | 0.1667 | 804 |
| B1 | Early | P0 | 0.2948 | 0.2388 | 0.3507 | 0.1667 | 268 |
| B1 | Early | P1 | 0.3769 | 0.3208 | 0.4328 | 0.1667 | 268 |
| B1 | Early | P2 | 0.2201 | 0.1716 | 0.2724 | 0.1667 | 268 |
| B1 | Early | P3 | 0.3731 | 0.3172 | 0.4291 | 0.1667 | 268 |
| B1 | Early | P4 | 0.4925 | 0.4366 | 0.5522 | 0.1667 | 268 |
| B1 | Early | P5 | 0.5336 | 0.4739 | 0.5896 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.2687 | 0.2164 | 0.3209 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.3097 | 0.2574 | 0.3619 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.2500 | 0.1978 | 0.3060 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.3284 | 0.2687 | 0.3807 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.3993 | 0.3432 | 0.4590 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.5970 | 0.5410 | 0.6493 | 0.1667 | 268 |
| B1 | Late | P0 | 0.3396 | 0.2836 | 0.3919 | 0.1667 | 268 |
| B1 | Late | P1 | 0.2537 | 0.2015 | 0.3060 | 0.1667 | 268 |
| B1 | Late | P2 | 0.2649 | 0.2164 | 0.3172 | 0.1667 | 268 |
| B1 | Late | P3 | 0.4067 | 0.3470 | 0.4628 | 0.1667 | 268 |
| B1 | Late | P4 | 0.2799 | 0.2276 | 0.3321 | 0.1667 | 268 |
| B1 | Late | P5 | 0.5746 | 0.5187 | 0.6343 | 0.1667 | 268 |
| B2 | overall | P0 | 0.2463 | 0.2152 | 0.2761 | 0.1667 | 804 |
| B2 | overall | P1 | 0.2326 | 0.2052 | 0.2624 | 0.1667 | 804 |
| B2 | overall | P2 | 0.1828 | 0.1567 | 0.2090 | 0.1667 | 804 |
| B2 | overall | P3 | 0.2612 | 0.2301 | 0.2948 | 0.1667 | 804 |
| B2 | overall | P4 | 0.2823 | 0.2500 | 0.3159 | 0.1667 | 804 |
| B2 | overall | P5 | 0.3097 | 0.2761 | 0.3408 | 0.1667 | 804 |
| B2 | Early | P0 | 0.2537 | 0.2052 | 0.3060 | 0.1667 | 268 |
| B2 | Early | P1 | 0.2612 | 0.2090 | 0.3134 | 0.1667 | 268 |
| B2 | Early | P2 | 0.1791 | 0.1343 | 0.2276 | 0.1667 | 268 |
| B2 | Early | P3 | 0.2761 | 0.2239 | 0.3321 | 0.1667 | 268 |
| B2 | Early | P4 | 0.3433 | 0.2873 | 0.3993 | 0.1667 | 268 |
| B2 | Early | P5 | 0.3284 | 0.2724 | 0.3843 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.2388 | 0.1903 | 0.2873 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.2388 | 0.1866 | 0.2910 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.1791 | 0.1343 | 0.2276 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.2276 | 0.1791 | 0.2799 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.2948 | 0.2388 | 0.3507 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.2948 | 0.2425 | 0.3507 | 0.1667 | 268 |
| B2 | Late | P0 | 0.2463 | 0.1940 | 0.2985 | 0.1667 | 268 |
| B2 | Late | P1 | 0.1978 | 0.1530 | 0.2500 | 0.1667 | 268 |
| B2 | Late | P2 | 0.1903 | 0.1455 | 0.2388 | 0.1667 | 268 |
| B2 | Late | P3 | 0.2799 | 0.2275 | 0.3358 | 0.1667 | 268 |
| B2 | Late | P4 | 0.2090 | 0.1604 | 0.2576 | 0.1667 | 268 |
| B2 | Late | P5 | 0.3060 | 0.2537 | 0.3619 | 0.1667 | 268 |
| B3 | overall | P0 | 0.2985 | 0.2662 | 0.3296 | 0.1667 | 804 |
| B3 | overall | P1 | 0.3085 | 0.2786 | 0.3383 | 0.1667 | 804 |
| B3 | overall | P2 | 0.2376 | 0.2077 | 0.2699 | 0.1667 | 804 |
| B3 | overall | P3 | 0.3719 | 0.3371 | 0.4055 | 0.1667 | 804 |
| B3 | overall | P4 | 0.3794 | 0.3470 | 0.4117 | 0.1667 | 804 |
| B3 | overall | P5 | 0.5634 | 0.5274 | 0.5995 | 0.1667 | 804 |
| B3 | Early | P0 | 0.2985 | 0.2463 | 0.3545 | 0.1667 | 268 |
| B3 | Early | P1 | 0.3694 | 0.3133 | 0.4291 | 0.1667 | 268 |
| B3 | Early | P2 | 0.2164 | 0.1716 | 0.2687 | 0.1667 | 268 |
| B3 | Early | P3 | 0.3582 | 0.3022 | 0.4142 | 0.1667 | 268 |
| B3 | Early | P4 | 0.4739 | 0.4179 | 0.5373 | 0.1667 | 268 |
| B3 | Early | P5 | 0.5075 | 0.4478 | 0.5672 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.2612 | 0.2090 | 0.3134 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.3134 | 0.2611 | 0.3657 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.2388 | 0.1903 | 0.2948 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.3433 | 0.2873 | 0.3993 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.4104 | 0.3545 | 0.4701 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.6007 | 0.5410 | 0.6567 | 0.1667 | 268 |
| B3 | Late | P0 | 0.3358 | 0.2799 | 0.3918 | 0.1667 | 268 |
| B3 | Late | P1 | 0.2425 | 0.1940 | 0.2949 | 0.1667 | 268 |
| B3 | Late | P2 | 0.2575 | 0.2090 | 0.3097 | 0.1667 | 268 |
| B3 | Late | P3 | 0.4142 | 0.3582 | 0.4739 | 0.1667 | 268 |
| B3 | Late | P4 | 0.2537 | 0.2015 | 0.3060 | 0.1667 | 268 |
| B3 | Late | P5 | 0.5821 | 0.5261 | 0.6418 | 0.1667 | 268 |
| B4 | overall | P0 | 0.2923 | 0.2624 | 0.3221 | 0.1667 | 804 |
| B4 | overall | P1 | 0.3905 | 0.3557 | 0.4241 | 0.1667 | 804 |
| B4 | overall | P2 | 0.1381 | 0.1169 | 0.1604 | 0.1667 | 804 |
| B4 | overall | P3 | 0.2637 | 0.2338 | 0.2935 | 0.1667 | 804 |
| B4 | overall | P4 | 0.3321 | 0.2998 | 0.3632 | 0.1667 | 804 |
| B4 | overall | P5 | 0.3930 | 0.3595 | 0.4266 | 0.1667 | 804 |
| B4 | Early | P0 | 0.2799 | 0.2239 | 0.3321 | 0.1667 | 268 |
| B4 | Early | P1 | 0.5187 | 0.4552 | 0.5821 | 0.1667 | 268 |
| B4 | Early | P2 | 0.0746 | 0.0448 | 0.1082 | 0.1667 | 268 |
| B4 | Early | P3 | 0.2425 | 0.1903 | 0.2910 | 0.1667 | 268 |
| B4 | Early | P4 | 0.4515 | 0.3918 | 0.5112 | 0.1667 | 268 |
| B4 | Early | P5 | 0.3433 | 0.2873 | 0.3993 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.3246 | 0.2724 | 0.3806 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.3881 | 0.3284 | 0.4440 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.1791 | 0.1343 | 0.2276 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.2537 | 0.2052 | 0.3097 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.2836 | 0.2276 | 0.3358 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.4142 | 0.3545 | 0.4701 | 0.1667 | 268 |
| B4 | Late | P0 | 0.2724 | 0.2201 | 0.3246 | 0.1667 | 268 |
| B4 | Late | P1 | 0.2649 | 0.2127 | 0.3209 | 0.1667 | 268 |
| B4 | Late | P2 | 0.1604 | 0.1194 | 0.2052 | 0.1667 | 268 |
| B4 | Late | P3 | 0.2948 | 0.2388 | 0.3470 | 0.1667 | 268 |
| B4 | Late | P4 | 0.2612 | 0.2127 | 0.3172 | 0.1667 | 268 |
| B4 | Late | P5 | 0.4216 | 0.3656 | 0.4777 | 0.1667 | 268 |
| B5 | overall | P0 | 0.1244 | 0.1020 | 0.1468 | 0.1667 | 804 |
| B5 | overall | P1 | 0.4826 | 0.4515 | 0.5149 | 0.1667 | 804 |
| B5 | overall | P2 | 0.0336 | 0.0211 | 0.0461 | 0.1667 | 804 |
| B5 | overall | P3 | 0.5522 | 0.5211 | 0.5846 | 0.1667 | 804 |
| B5 | overall | P4 | 0.0299 | 0.0187 | 0.0410 | 0.1667 | 804 |
| B5 | overall | P5 | 0.0286 | 0.0186 | 0.0398 | 0.1667 | 804 |
| B5 | Early | P0 | 0.1306 | 0.0933 | 0.1716 | 0.1667 | 268 |
| B5 | Early | P1 | 0.7052 | 0.6493 | 0.7612 | 0.1667 | 268 |
| B5 | Early | P2 | 0.0373 | 0.0187 | 0.0634 | 0.1667 | 268 |
| B5 | Early | P3 | 0.2948 | 0.2425 | 0.3507 | 0.1667 | 268 |
| B5 | Early | P4 | 0.0448 | 0.0224 | 0.0709 | 0.1667 | 268 |
| B5 | Early | P5 | 0.0336 | 0.0149 | 0.0560 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.1343 | 0.0933 | 0.1755 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.4254 | 0.3657 | 0.4851 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.0410 | 0.0187 | 0.0672 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.6306 | 0.5746 | 0.6866 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.0299 | 0.0112 | 0.0522 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.0336 | 0.0149 | 0.0560 | 0.1667 | 268 |
| B5 | Late | P0 | 0.1082 | 0.0709 | 0.1455 | 0.1667 | 268 |
| B5 | Late | P1 | 0.3172 | 0.2612 | 0.3769 | 0.1667 | 268 |
| B5 | Late | P2 | 0.0224 | 0.0075 | 0.0410 | 0.1667 | 268 |
| B5 | Late | P3 | 0.7313 | 0.6791 | 0.7836 | 0.1667 | 268 |
| B5 | Late | P4 | 0.0149 | 0.0037 | 0.0299 | 0.1667 | 268 |
| B5 | Late | P5 | 0.0187 | 0.0037 | 0.0373 | 0.1667 | 268 |
| B6 | overall | P1 | 0.3794 | 0.3445 | 0.4117 | 0.2000 | 804 |
| B6 | overall | P2 | 0.3047 | 0.2711 | 0.3371 | 0.2000 | 804 |
| B6 | overall | P3 | 0.3980 | 0.3644 | 0.4304 | 0.2000 | 804 |
| B6 | overall | P4 | 0.4017 | 0.3706 | 0.4353 | 0.2000 | 804 |
| B6 | overall | P5 | 0.6182 | 0.5833 | 0.6542 | 0.2000 | 804 |
| B6 | Early | P1 | 0.4440 | 0.3881 | 0.5001 | 0.2000 | 268 |
| B6 | Early | P2 | 0.2799 | 0.2276 | 0.3358 | 0.2000 | 268 |
| B6 | Early | P3 | 0.3769 | 0.3209 | 0.4366 | 0.2000 | 268 |
| B6 | Early | P4 | 0.4925 | 0.4328 | 0.5522 | 0.2000 | 268 |
| B6 | Early | P5 | 0.6082 | 0.5485 | 0.6642 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.3918 | 0.3321 | 0.4515 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.2985 | 0.2425 | 0.3545 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.3731 | 0.3134 | 0.4291 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.4328 | 0.3731 | 0.4925 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.6381 | 0.5821 | 0.6940 | 0.2000 | 268 |
| B6 | Late | P1 | 0.3022 | 0.2463 | 0.3545 | 0.2000 | 268 |
| B6 | Late | P2 | 0.3358 | 0.2799 | 0.3918 | 0.2000 | 268 |
| B6 | Late | P3 | 0.4440 | 0.3843 | 0.5037 | 0.2000 | 268 |
| B6 | Late | P4 | 0.2799 | 0.2276 | 0.3358 | 0.2000 | 268 |
| B6 | Late | P5 | 0.6082 | 0.5522 | 0.6679 | 0.2000 | 268 |
| B7 | overall | P0 | 0.2201 | 0.1928 | 0.2475 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.6648 | 0.6412 | 0.6884 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.3296 | 0.2973 | 0.3607 | 0.2000 | 804 |
| B7 | overall | P4 | 0.3445 | 0.3122 | 0.3769 | 0.2000 | 804 |
| B7 | overall | P5 | 0.4975 | 0.4627 | 0.5336 | 0.2000 | 804 |
| B7 | Early | P0 | 0.2276 | 0.1791 | 0.2799 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.7164 | 0.6772 | 0.7556 | 0.2000 | 536 |
| B7 | Early | P3 | 0.3172 | 0.2612 | 0.3731 | 0.2000 | 268 |
| B7 | Early | P4 | 0.4254 | 0.3657 | 0.4851 | 0.2000 | 268 |
| B7 | Early | P5 | 0.4515 | 0.3955 | 0.5112 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.1978 | 0.1493 | 0.2425 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.6549 | 0.6138 | 0.6940 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.2948 | 0.2351 | 0.3507 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.3694 | 0.3134 | 0.4291 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.5448 | 0.4888 | 0.6045 | 0.2000 | 268 |
| B7 | Late | P0 | 0.2351 | 0.1828 | 0.2836 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.6231 | 0.5858 | 0.6605 | 0.2000 | 536 |
| B7 | Late | P3 | 0.3769 | 0.3209 | 0.4366 | 0.2000 | 268 |
| B7 | Late | P4 | 0.2388 | 0.1903 | 0.2910 | 0.2000 | 268 |
| B7 | Late | P5 | 0.4963 | 0.4403 | 0.5560 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | 0.0523 | 0.3775 | 0.8898 | -0.6877 | 0.7923 |
| C(position, Treatment(reference='Early'))[T.Late] | 0.0073 | 0.1191 | 0.9511 | -0.2261 | 0.2407 |
| C(position, Treatment(reference='Early'))[T.Middle] | -0.0100 | 0.0944 | 0.9158 | -0.1950 | 0.1750 |
| log_context | -0.0964 | 0.0678 | 0.1551 | -0.2292 | 0.0365 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.0776 | -0.2042 | 0.0403 | 0.2160 | 0.4320 | 804 | not confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1008 | -0.3168 | 0.1068 | 0.3380 | 1.0000 | 268 | not confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.0210 | -0.1640 | 0.1234 | 0.7470 | 1.0000 | 268 | not confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1110 | -0.3724 | 0.1546 | 0.3780 | 1.0000 | 268 | not confirmed |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | 1.2290 | 0.8028 | 1.6649 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | 1.2349 | 0.4378 | 2.0525 | 0.0060 | 0.0300 | 268 | confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | 1.5979 | 0.8806 | 2.3793 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | 0.8542 | 0.1853 | 1.5370 | 0.0140 | 0.0560 | 268 | confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | -0.0069 | -0.0475 | 0.0309 | 0.7250 | 1.0000 | 189 | not confirmed |
| Early | P1 - P0 | share_open | lower | pre-specified | -0.0324 | -0.0874 | 0.0178 | 0.2050 | 1.0000 | 103 | not confirmed |
| Middle | P1 - P0 | share_open | lower | pre-specified | -0.0109 | -0.0761 | 0.0435 | 0.8960 | 1.0000 | 46 | not confirmed |
| Late | P1 - P0 | share_open | lower | pre-specified | 0.0633 | -0.0409 | 0.1717 | 0.2240 | 1.0000 | 40 | not confirmed |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1731 | 0.0501 | 0.2964 | 0.0100 | 0.0300 | 804 | confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1528 | -0.0316 | 0.3430 | 0.1120 | 0.7840 | 268 | not confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.3243 | 0.1009 | 0.5765 | 0.0040 | 0.0360 | 268 | confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.0422 | -0.1575 | 0.2424 | 0.6570 | 1.0000 | 268 | not confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.8680 | 0.7172 | 1.0329 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 1.2297 | 0.8731 | 1.6261 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.9248 | 0.6832 | 1.1836 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.4497 | 0.2016 | 0.6883 | 0.0030 | 0.0300 | 268 | confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.0855 | 0.0427 | 0.1305 | 0.0000 | 0.0000 | 230 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.0778 | 0.0097 | 0.1500 | 0.0270 | 0.2700 | 120 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.1384 | 0.0537 | 0.2316 | 0.0020 | 0.0220 | 59 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.0425 | -0.0196 | 0.1209 | 0.2360 | 1.0000 | 51 | not confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 0.9918 | 0.8063 | 1.1838 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 1.8037 | 1.4139 | 2.2241 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 0.7865 | 0.5298 | 1.0658 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 0.3853 | 0.1314 | 0.6359 | 0.0010 | 0.0110 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.0844 | 0.0415 | 0.1274 | 0.0000 | 0.0000 | 232 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.1566 | 0.0833 | 0.2298 | 0.0000 | 0.0000 | 124 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.0119 | -0.0358 | 0.0595 | 0.6440 | 1.0000 | 56 | not confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | -0.0096 | -0.0577 | 0.0385 | 0.9090 | 1.0000 | 52 | not confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -1.3222 | -1.7940 | -0.8630 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -1.1878 | -2.0131 | -0.3718 | 0.0020 | 0.0120 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -1.4671 | -2.1451 | -0.7408 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -1.3115 | -1.9907 | -0.6311 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.1238 | -0.0934 | 0.3362 | 0.2680 | 0.4320 | 804 | not confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.5740 | 0.0713 | 1.0710 | 0.0230 | 0.1840 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.1383 | -0.4788 | 0.1961 | 0.3790 | 1.0000 | 268 | not confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.0644 | -0.2973 | 0.1985 | 0.5850 | 1.0000 | 268 | not confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -0.2715 | -0.6446 | 0.1228 | 0.1910 | 0.1910 | 804 | not confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -0.4215 | -1.2014 | 0.3150 | 0.2680 | 0.8040 | 268 | not confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -0.3021 | -0.9492 | 0.3491 | 0.3760 | 0.8040 | 268 | not confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -0.0910 | -0.7455 | 0.5883 | 0.8140 | 0.8140 | 268 | not confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.2339 | 0.1906 | 0.2787 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.2408 | 0.1698 | 0.3155 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.2712 | 0.1993 | 0.3503 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1898 | 0.1232 | 0.2589 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | -0.0100 | 0.0112 | 1.0000 | 1.0000 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | 0.0000 | -0.0224 | 0.0224 | 1.0000 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | -0.0037 | -0.0150 | 0.0075 | 0.8020 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | 0.0037 | -0.0112 | 0.0261 | 0.8900 | 1.0000 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0907 | -0.1300 | -0.0497 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0881 | -0.1684 | -0.0110 | 0.0260 | 0.0520 | 268 | confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1204 | -0.1879 | -0.0562 | 0.0010 | 0.0030 | 268 | confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.0637 | -0.1241 | 0.0007 | 0.0520 | 0.0520 | 268 | not confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | -0.0024 | -0.0644 | 0.0540 | 0.9060 | 1.0000 | 137 | not confirmed |
| Early | P5 - P0 | share_open | lower | pre-specified | -0.0142 | -0.1057 | 0.0711 | 0.7480 | 1.0000 | 82 | not confirmed |
| Middle | P5 - P0 | share_open | lower | pre-specified | 0.0000 | -0.0652 | 0.0652 | 1.0000 | 1.0000 | 23 | not confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | 0.0260 | -0.0312 | 0.1042 | 0.5980 | 1.0000 | 32 | not confirmed |
| overall | P5 - P0 | has_question | lower | pre-specified | -0.0821 | -0.1269 | -0.0386 | 0.0010 | 0.0010 | 804 | confirmed |
| Early | P5 - P0 | has_question | lower | pre-specified | -0.1306 | -0.2015 | -0.0597 | 0.0010 | 0.0030 | 268 | confirmed |
| Middle | P5 - P0 | has_question | lower | pre-specified | -0.0821 | -0.1567 | 0.0037 | 0.0650 | 0.1300 | 268 | not confirmed |
| Late | P5 - P0 | has_question | lower | pre-specified | -0.0336 | -0.1119 | 0.0448 | 0.4580 | 0.4580 | 268 | not confirmed |
| overall | P5 - P0 | plan_statement_present | higher | pre-specified | 0.0958 | 0.0510 | 0.1405 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | pre-specified | 0.0821 | 0.0037 | 0.1604 | 0.0350 | 0.0700 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | pre-specified | 0.1306 | 0.0560 | 0.2052 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | pre-specified | 0.0746 | 0.0075 | 0.1455 | 0.0360 | 0.0700 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.0102 | -0.3586 | 0.3328 | 0.9330 | 0.9330 | not confirmed |
| P1 - P0 | med_per_100 | higher | pre-specified | -0.3807 | -1.4494 | 0.7031 | 0.4830 | 1.0000 | not confirmed |
| P1 - P0 | share_open | lower | pre-specified | 0.0957 | -0.0260 | 0.2168 | 0.1240 | 0.3720 | not confirmed |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | -0.1106 | -0.3721 | 0.1523 | 0.4250 | 0.8500 | not confirmed |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | -0.7800 | -1.2659 | -0.3288 | 0.0010 | 0.0040 | confirmed |
| P3 - P0 | share_open | higher | pre-specified | -0.0353 | -0.1307 | 0.0616 | 0.4560 | 0.9120 | not confirmed |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -1.4184 | -1.8888 | -0.9350 | 0.0000 | 0.0000 | confirmed |
| P4 - P0 | share_open | higher | pre-specified | -0.1662 | -0.2590 | -0.0762 | 0.0000 | 0.0000 | confirmed |
| P4 - P0 | med_per_100 | lower | pre-specified | -0.1238 | -1.0955 | 0.9086 | 0.8120 | 1.0000 | not confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -0.6384 | -1.2123 | -0.0610 | 0.0360 | 0.1080 | confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | 0.3304 | -0.6763 | 1.3701 | 0.4970 | 1.0000 | not confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | -0.0510 | -0.1456 | 0.0431 | 0.3050 | 0.3050 | not confirmed |
| P5 - P0 | n_leading | higher | pre-specified | 0.0037 | -0.0261 | 0.0373 | 0.9030 | 0.9030 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | 0.0243 | -0.0765 | 0.1261 | 0.6530 | 0.6530 | not confirmed |
| P5 - P0 | share_open | lower | pre-specified | 0.0403 | -0.0685 | 0.1567 | 0.4900 | 0.9120 | not confirmed |
| P5 - P0 | has_question | lower | pre-specified | 0.0970 | -0.0038 | 0.1978 | 0.0700 | 0.0700 | not confirmed |
| P5 - P0 | plan_statement_present | higher | pre-specified | -0.0075 | -0.1082 | 0.0970 | 0.9140 | 0.9140 | not confirmed |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.3134 | 0.2836 | 0.3433 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| overall | P2 | 0.2450 | 0.2152 | 0.2774 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.3694 | 0.3346 | 0.4018 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.3905 | 0.3582 | 0.4241 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.5684 | 0.5336 | 0.6032 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Early | P1 | 0.3769 | 0.3208 | 0.4328 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Early | P2 | 0.2201 | 0.1716 | 0.2724 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.3731 | 0.3172 | 0.4291 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.4925 | 0.4366 | 0.5522 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 0.5336 | 0.4739 | 0.5896 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Middle | P1 | 0.3097 | 0.2574 | 0.3619 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Middle | P2 | 0.2500 | 0.1978 | 0.3060 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.3284 | 0.2687 | 0.3807 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.3993 | 0.3432 | 0.4590 | 0.1667 | 1 | 3 | 2 | 0 | not realised |
| Middle | P5 | 0.5970 | 0.5410 | 0.6493 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Late | P1 | 0.2537 | 0.2015 | 0.3060 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Late | P2 | 0.2649 | 0.2164 | 0.3172 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.4067 | 0.3470 | 0.4628 | 0.1667 | 1 | 2 | 1 | 0 | not realised |
| Late | P4 | 0.2799 | 0.2276 | 0.3321 | 0.1667 | 1 | 3 | 2 | 0 | not realised |
| Late | P5 | 0.5746 | 0.5187 | 0.6343 | 0.1667 | 1 | 4 | 1 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.4677 | 804 |
| P0 | overall | plan_statement_present | 0.6206 | 804 |
| P0 | overall | empathy_phrases_present | 0.1020 | 804 |
| P0 | overall | hedge_per_100 | 1.2797 | 804 |
| P0 | overall | n_words | 85.2376 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.6119 | 268 |
| P0 | Early | plan_statement_present | 0.4925 | 268 |
| P0 | Early | empathy_phrases_present | 0.1381 | 268 |
| P0 | Early | hedge_per_100 | 1.0957 | 268 |
| P0 | Early | n_words | 63.4515 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.3993 | 268 |
| P0 | Middle | plan_statement_present | 0.6604 | 268 |
| P0 | Middle | empathy_phrases_present | 0.0896 | 268 |
| P0 | Middle | hedge_per_100 | 1.3989 | 268 |
| P0 | Middle | n_words | 88.9888 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.3918 | 268 |
| P0 | Late | plan_statement_present | 0.7090 | 268 |
| P0 | Late | empathy_phrases_present | 0.0784 | 268 |
| P0 | Late | hedge_per_100 | 1.3444 | 268 |
| P0 | Late | n_words | 103.2724 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.5012 | 804 |
| P1 | overall | plan_statement_present | 0.4664 | 804 |
| P1 | overall | empathy_phrases_present | 0.0585 | 804 |
| P1 | overall | hedge_per_100 | 1.0488 | 804 |
| P1 | overall | n_words | 78.3483 | 804 |
| P1 | overall | persona_distance | 0.3716 | 804 |
| P1 | Early | has_question | 0.6642 | 268 |
| P1 | Early | plan_statement_present | 0.2910 | 268 |
| P1 | Early | empathy_phrases_present | 0.0597 | 268 |
| P1 | Early | hedge_per_100 | 0.8494 | 268 |
| P1 | Early | n_words | 55.3284 | 268 |
| P1 | Early | persona_distance | 0.3839 | 268 |
| P1 | Middle | has_question | 0.4366 | 268 |
| P1 | Middle | plan_statement_present | 0.4963 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0448 | 268 |
| P1 | Middle | hedge_per_100 | 1.1874 | 268 |
| P1 | Middle | n_words | 82.4627 | 268 |
| P1 | Middle | persona_distance | 0.3671 | 268 |
| P1 | Late | has_question | 0.4030 | 268 |
| P1 | Late | plan_statement_present | 0.6119 | 268 |
| P1 | Late | empathy_phrases_present | 0.0709 | 268 |
| P1 | Late | hedge_per_100 | 1.1098 | 268 |
| P1 | Late | n_words | 97.2537 | 268 |
| P1 | Late | persona_distance | 0.3639 | 268 |
| P2 | overall | has_question | 0.4764 | 804 |
| P2 | overall | plan_statement_present | 0.5883 | 804 |
| P2 | overall | empathy_phrases_present | 0.0709 | 804 |
| P2 | overall | hedge_per_100 | 1.2246 | 804 |
| P2 | overall | n_words | 96.1244 | 804 |
| P2 | overall | persona_distance | 0.3524 | 804 |
| P2 | Early | has_question | 0.6493 | 268 |
| P2 | Early | plan_statement_present | 0.3769 | 268 |
| P2 | Early | empathy_phrases_present | 0.0896 | 268 |
| P2 | Early | hedge_per_100 | 0.9876 | 268 |
| P2 | Early | n_words | 69.8843 | 268 |
| P2 | Early | persona_distance | 0.3637 | 268 |
| P2 | Middle | has_question | 0.3993 | 268 |
| P2 | Middle | plan_statement_present | 0.6679 | 268 |
| P2 | Middle | empathy_phrases_present | 0.0560 | 268 |
| P2 | Middle | hedge_per_100 | 1.2913 | 268 |
| P2 | Middle | n_words | 101.8657 | 268 |
| P2 | Middle | persona_distance | 0.3500 | 268 |
| P2 | Late | has_question | 0.3806 | 268 |
| P2 | Late | plan_statement_present | 0.7201 | 268 |
| P2 | Late | empathy_phrases_present | 0.0672 | 268 |
| P2 | Late | hedge_per_100 | 1.3948 | 268 |
| P2 | Late | n_words | 116.6231 | 268 |
| P2 | Late | persona_distance | 0.3435 | 268 |
| P3 | overall | has_question | 0.6480 | 804 |
| P3 | overall | plan_statement_present | 0.5560 | 804 |
| P3 | overall | empathy_phrases_present | 0.1555 | 804 |
| P3 | overall | hedge_per_100 | 1.2938 | 804 |
| P3 | overall | n_words | 106.3383 | 804 |
| P3 | overall | persona_distance | 0.3614 | 804 |
| P3 | Early | has_question | 0.7799 | 268 |
| P3 | Early | plan_statement_present | 0.3731 | 268 |
| P3 | Early | empathy_phrases_present | 0.2090 | 268 |
| P3 | Early | hedge_per_100 | 1.1486 | 268 |
| P3 | Early | n_words | 74.2164 | 268 |
| P3 | Early | persona_distance | 0.3801 | 268 |
| P3 | Middle | has_question | 0.6119 | 268 |
| P3 | Middle | plan_statement_present | 0.5746 | 268 |
| P3 | Middle | empathy_phrases_present | 0.1567 | 268 |
| P3 | Middle | hedge_per_100 | 1.3942 | 268 |
| P3 | Middle | n_words | 110.4925 | 268 |
| P3 | Middle | persona_distance | 0.3604 | 268 |
| P3 | Late | has_question | 0.5522 | 268 |
| P3 | Late | plan_statement_present | 0.7201 | 268 |
| P3 | Late | empathy_phrases_present | 0.1007 | 268 |
| P3 | Late | hedge_per_100 | 1.3386 | 268 |
| P3 | Late | n_words | 134.3060 | 268 |
| P3 | Late | persona_distance | 0.3436 | 268 |
| P4 | overall | has_question | 0.6517 | 804 |
| P4 | overall | plan_statement_present | 0.5261 | 804 |
| P4 | overall | empathy_phrases_present | 0.1667 | 804 |
| P4 | overall | hedge_per_100 | 1.4611 | 804 |
| P4 | overall | n_words | 98.7289 | 804 |
| P4 | overall | persona_distance | 0.3679 | 804 |
| P4 | Early | has_question | 0.8097 | 268 |
| P4 | Early | plan_statement_present | 0.3134 | 268 |
| P4 | Early | empathy_phrases_present | 0.2649 | 268 |
| P4 | Early | hedge_per_100 | 1.3399 | 268 |
| P4 | Early | n_words | 70.3993 | 268 |
| P4 | Early | persona_distance | 0.3895 | 268 |
| P4 | Middle | has_question | 0.6530 | 268 |
| P4 | Middle | plan_statement_present | 0.5709 | 268 |
| P4 | Middle | empathy_phrases_present | 0.1306 | 268 |
| P4 | Middle | hedge_per_100 | 1.5257 | 268 |
| P4 | Middle | n_words | 106.2537 | 268 |
| P4 | Middle | persona_distance | 0.3664 | 268 |
| P4 | Late | has_question | 0.4925 | 268 |
| P4 | Late | plan_statement_present | 0.6940 | 268 |
| P4 | Late | empathy_phrases_present | 0.1045 | 268 |
| P4 | Late | hedge_per_100 | 1.5176 | 268 |
| P4 | Late | n_words | 119.5336 | 268 |
| P4 | Late | persona_distance | 0.3478 | 268 |
| P5 | overall | has_question | 0.3856 | 804 |
| P5 | overall | plan_statement_present | 0.7164 | 804 |
| P5 | overall | empathy_phrases_present | 0.0510 | 804 |
| P5 | overall | hedge_per_100 | 0.9359 | 804 |
| P5 | overall | n_words | 97.9664 | 804 |
| P5 | overall | persona_distance | 0.3618 | 804 |
| P5 | Early | has_question | 0.4813 | 268 |
| P5 | Early | plan_statement_present | 0.5746 | 268 |
| P5 | Early | empathy_phrases_present | 0.0448 | 268 |
| P5 | Early | hedge_per_100 | 0.8854 | 268 |
| P5 | Early | n_words | 73.3022 | 268 |
| P5 | Early | persona_distance | 0.3753 | 268 |
| P5 | Middle | has_question | 0.3172 | 268 |
| P5 | Middle | plan_statement_present | 0.7910 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0597 | 268 |
| P5 | Middle | hedge_per_100 | 0.9421 | 268 |
| P5 | Middle | n_words | 105.7313 | 268 |
| P5 | Middle | persona_distance | 0.3529 | 268 |
| P5 | Late | has_question | 0.3582 | 268 |
| P5 | Late | plan_statement_present | 0.7836 | 268 |
| P5 | Late | empathy_phrases_present | 0.0485 | 268 |
| P5 | Late | hedge_per_100 | 0.9802 | 268 |
| P5 | Late | n_words | 114.8657 | 268 |
| P5 | Late | persona_distance | 0.3573 | 268 |

## Part D

Part D drops 46 analysed rows with any format flag, leaving 4778. Prediction verdicts changed in 4 of 68 rows. H2 verdicts changed in 1 of 17 rows. Realised flags changed in 0 of 20 rows.

Changed prediction verdicts:

| scope | contrast | marker | verdict_main | verdict_sensitivity |
| --- | --- | --- | --- | --- |
| Early | P5 - P0 | plan_statement_present | confirmed | not confirmed |
| Late | P1 - P0 | share_open | not confirmed | opposite |
| Late | P5 - P0 | invitation_per_100 | not confirmed | confirmed |
| Middle | P5 - P0 | has_question | not confirmed | confirmed |

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
