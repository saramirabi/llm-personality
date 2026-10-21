# medgemma measurement report

Plan SHA-256: `7b85c86fc37013b4e42e3a46c77bdef4cf6073171add570ca9879b7f7c896455`
Erratum 1 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 2 (2026-10-02) plan SHA-256 before this erratum: `56679285fb538ddfe04723dfadca09a1a34418ff6ba766cc55fa559c86675cc6`
Erratum 4 (2026-10-02) original plan SHA-256: `2fde5453edf8a2674b83db5a74d26b22e7dae48edd3ac45cea70819112df5cf4`
Erratum 4 (2026-10-02) plan SHA-256 before this erratum: `c1747f993babaa05f8dd3c99543584d8555cb9212138a92e909972505a210450`
Prompt SHA-256: `2314d1cccef40ae12b89bf36a09508adf2122cc25e49b606faa65b8f9bda3d19`

No generation was run. Measurements use `analysis_text` only.

## Data

- Output rows: 4824
- Missing `analysis_text`: 0. Those rows stay in the feature file and are excluded from calculations.
- Rows in the calculations: 4824
- Contexts: 804
- Rows by condition: {'P0': 804, 'P1': 804, 'P2': 804, 'P3': 804, 'P4': 804, 'P5': 804}
- Rows by position: {'Early': 1608, 'Late': 1608, 'Middle': 1608}
- Rows with any format flag, among analysed rows: 3
- Persona content words removed for the echo controls: 55

## Part B accuracy

| variant | scope | accuracy | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | 0.4743 | 0.4610 | 0.4876 | 0.1667 | 4824 |
| B1 | Early | 0.4925 | 0.4720 | 0.5124 | 0.1667 | 1608 |
| B1 | Middle | 0.5000 | 0.4770 | 0.5224 | 0.1667 | 1608 |
| B1 | Late | 0.4303 | 0.4073 | 0.4527 | 0.1667 | 1608 |
| B2 | overall | 0.4343 | 0.4206 | 0.4473 | 0.1667 | 4824 |
| B2 | Early | 0.4577 | 0.4366 | 0.4782 | 0.1667 | 1608 |
| B2 | Middle | 0.4577 | 0.4366 | 0.4789 | 0.1667 | 1608 |
| B2 | Late | 0.3874 | 0.3663 | 0.4086 | 0.1667 | 1608 |
| B3 | overall | 0.4739 | 0.4610 | 0.4869 | 0.1667 | 4824 |
| B3 | Early | 0.4938 | 0.4726 | 0.5137 | 0.1667 | 1608 |
| B3 | Middle | 0.5000 | 0.4789 | 0.5205 | 0.1667 | 1608 |
| B3 | Late | 0.4279 | 0.4061 | 0.4496 | 0.1667 | 1608 |
| B4 | overall | 0.3794 | 0.3667 | 0.3916 | 0.1667 | 4824 |
| B4 | Early | 0.3775 | 0.3588 | 0.3968 | 0.1667 | 1608 |
| B4 | Middle | 0.4136 | 0.3924 | 0.4347 | 0.1667 | 1608 |
| B4 | Late | 0.3470 | 0.3252 | 0.3688 | 0.1667 | 1608 |
| B5 | overall | 0.2305 | 0.2218 | 0.2388 | 0.1667 | 4824 |
| B5 | Early | 0.2382 | 0.2245 | 0.2512 | 0.1667 | 1608 |
| B5 | Middle | 0.2463 | 0.2320 | 0.2612 | 0.1667 | 1608 |
| B5 | Late | 0.2071 | 0.1947 | 0.2195 | 0.1667 | 1608 |
| B6 | overall | 0.5460 | 0.5308 | 0.5609 | 0.2000 | 4020 |
| B6 | Early | 0.5597 | 0.5366 | 0.5828 | 0.2000 | 1340 |
| B6 | Middle | 0.5716 | 0.5470 | 0.5955 | 0.2000 | 1340 |
| B6 | Late | 0.5067 | 0.4799 | 0.5343 | 0.2000 | 1340 |
| B7 | overall | 0.5794 | 0.5655 | 0.5925 | 0.2000 | 4824 |
| B7 | Early | 0.6051 | 0.5821 | 0.6269 | 0.2000 | 1608 |
| B7 | Middle | 0.6007 | 0.5790 | 0.6213 | 0.2000 | 1608 |
| B7 | Late | 0.5323 | 0.5081 | 0.5560 | 0.2000 | 1608 |

## Part B recall

| variant | scope | condition | recall | ci_low | ci_high | chance | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | overall | P0 | 0.3246 | 0.2910 | 0.3582 | 0.1667 | 804 |
| B1 | overall | P1 | 0.5236 | 0.4851 | 0.5597 | 0.1667 | 804 |
| B1 | overall | P2 | 0.2935 | 0.2600 | 0.3259 | 0.1667 | 804 |
| B1 | overall | P3 | 0.4540 | 0.4141 | 0.4938 | 0.1667 | 804 |
| B1 | overall | P4 | 0.7475 | 0.7127 | 0.7799 | 0.1667 | 804 |
| B1 | overall | P5 | 0.5025 | 0.4627 | 0.5410 | 0.1667 | 804 |
| B1 | Early | P0 | 0.3619 | 0.3060 | 0.4179 | 0.1667 | 268 |
| B1 | Early | P1 | 0.5037 | 0.4440 | 0.5634 | 0.1667 | 268 |
| B1 | Early | P2 | 0.2873 | 0.2313 | 0.3470 | 0.1667 | 268 |
| B1 | Early | P3 | 0.5448 | 0.4851 | 0.6045 | 0.1667 | 268 |
| B1 | Early | P4 | 0.8545 | 0.8097 | 0.8955 | 0.1667 | 268 |
| B1 | Early | P5 | 0.4030 | 0.3433 | 0.4590 | 0.1667 | 268 |
| B1 | Middle | P0 | 0.3246 | 0.2687 | 0.3806 | 0.1667 | 268 |
| B1 | Middle | P1 | 0.5821 | 0.5187 | 0.6418 | 0.1667 | 268 |
| B1 | Middle | P2 | 0.3433 | 0.2910 | 0.3993 | 0.1667 | 268 |
| B1 | Middle | P3 | 0.4254 | 0.3657 | 0.4851 | 0.1667 | 268 |
| B1 | Middle | P4 | 0.7873 | 0.7351 | 0.8358 | 0.1667 | 268 |
| B1 | Middle | P5 | 0.5373 | 0.4776 | 0.5970 | 0.1667 | 268 |
| B1 | Late | P0 | 0.2873 | 0.2351 | 0.3433 | 0.1667 | 268 |
| B1 | Late | P1 | 0.4851 | 0.4216 | 0.5448 | 0.1667 | 268 |
| B1 | Late | P2 | 0.2500 | 0.1978 | 0.2986 | 0.1667 | 268 |
| B1 | Late | P3 | 0.3918 | 0.3358 | 0.4515 | 0.1667 | 268 |
| B1 | Late | P4 | 0.6007 | 0.5373 | 0.6604 | 0.1667 | 268 |
| B1 | Late | P5 | 0.5672 | 0.5075 | 0.6231 | 0.1667 | 268 |
| B2 | overall | P0 | 0.2736 | 0.2425 | 0.3047 | 0.1667 | 804 |
| B2 | overall | P1 | 0.4913 | 0.4540 | 0.5261 | 0.1667 | 804 |
| B2 | overall | P2 | 0.2351 | 0.2052 | 0.2649 | 0.1667 | 804 |
| B2 | overall | P3 | 0.4104 | 0.3756 | 0.4453 | 0.1667 | 804 |
| B2 | overall | P4 | 0.8047 | 0.7724 | 0.8334 | 0.1667 | 804 |
| B2 | overall | P5 | 0.3905 | 0.3545 | 0.4279 | 0.1667 | 804 |
| B2 | Early | P0 | 0.3060 | 0.2500 | 0.3619 | 0.1667 | 268 |
| B2 | Early | P1 | 0.4925 | 0.4328 | 0.5522 | 0.1667 | 268 |
| B2 | Early | P2 | 0.2313 | 0.1828 | 0.2836 | 0.1667 | 268 |
| B2 | Early | P3 | 0.5187 | 0.4627 | 0.5784 | 0.1667 | 268 |
| B2 | Early | P4 | 0.8657 | 0.8245 | 0.9067 | 0.1667 | 268 |
| B2 | Early | P5 | 0.3321 | 0.2761 | 0.3881 | 0.1667 | 268 |
| B2 | Middle | P0 | 0.2687 | 0.2127 | 0.3246 | 0.1667 | 268 |
| B2 | Middle | P1 | 0.5634 | 0.5037 | 0.6194 | 0.1667 | 268 |
| B2 | Middle | P2 | 0.2537 | 0.2015 | 0.3060 | 0.1667 | 268 |
| B2 | Middle | P3 | 0.3881 | 0.3284 | 0.4478 | 0.1667 | 268 |
| B2 | Middle | P4 | 0.8507 | 0.8022 | 0.8881 | 0.1667 | 268 |
| B2 | Middle | P5 | 0.4216 | 0.3619 | 0.4776 | 0.1667 | 268 |
| B2 | Late | P0 | 0.2463 | 0.1978 | 0.2948 | 0.1667 | 268 |
| B2 | Late | P1 | 0.4179 | 0.3545 | 0.4740 | 0.1667 | 268 |
| B2 | Late | P2 | 0.2201 | 0.1679 | 0.2687 | 0.1667 | 268 |
| B2 | Late | P3 | 0.3246 | 0.2724 | 0.3806 | 0.1667 | 268 |
| B2 | Late | P4 | 0.6978 | 0.6418 | 0.7500 | 0.1667 | 268 |
| B2 | Late | P5 | 0.4179 | 0.3582 | 0.4776 | 0.1667 | 268 |
| B3 | overall | P0 | 0.3371 | 0.3035 | 0.3707 | 0.1667 | 804 |
| B3 | overall | P1 | 0.5162 | 0.4764 | 0.5522 | 0.1667 | 804 |
| B3 | overall | P2 | 0.2861 | 0.2537 | 0.3172 | 0.1667 | 804 |
| B3 | overall | P3 | 0.4478 | 0.4080 | 0.4851 | 0.1667 | 804 |
| B3 | overall | P4 | 0.7587 | 0.7251 | 0.7898 | 0.1667 | 804 |
| B3 | overall | P5 | 0.4975 | 0.4577 | 0.5361 | 0.1667 | 804 |
| B3 | Early | P0 | 0.3694 | 0.3134 | 0.4254 | 0.1667 | 268 |
| B3 | Early | P1 | 0.4963 | 0.4402 | 0.5560 | 0.1667 | 268 |
| B3 | Early | P2 | 0.2873 | 0.2313 | 0.3433 | 0.1667 | 268 |
| B3 | Early | P3 | 0.5448 | 0.4851 | 0.6008 | 0.1667 | 268 |
| B3 | Early | P4 | 0.8582 | 0.8134 | 0.8993 | 0.1667 | 268 |
| B3 | Early | P5 | 0.4067 | 0.3470 | 0.4664 | 0.1667 | 268 |
| B3 | Middle | P0 | 0.3396 | 0.2836 | 0.3955 | 0.1667 | 268 |
| B3 | Middle | P1 | 0.5858 | 0.5261 | 0.6455 | 0.1667 | 268 |
| B3 | Middle | P2 | 0.3358 | 0.2836 | 0.3918 | 0.1667 | 268 |
| B3 | Middle | P3 | 0.4291 | 0.3731 | 0.4888 | 0.1667 | 268 |
| B3 | Middle | P4 | 0.7948 | 0.7463 | 0.8470 | 0.1667 | 268 |
| B3 | Middle | P5 | 0.5149 | 0.4552 | 0.5746 | 0.1667 | 268 |
| B3 | Late | P0 | 0.3022 | 0.2463 | 0.3582 | 0.1667 | 268 |
| B3 | Late | P1 | 0.4664 | 0.4030 | 0.5261 | 0.1667 | 268 |
| B3 | Late | P2 | 0.2351 | 0.1828 | 0.2836 | 0.1667 | 268 |
| B3 | Late | P3 | 0.3694 | 0.3134 | 0.4255 | 0.1667 | 268 |
| B3 | Late | P4 | 0.6231 | 0.5597 | 0.6792 | 0.1667 | 268 |
| B3 | Late | P5 | 0.5709 | 0.5111 | 0.6269 | 0.1667 | 268 |
| B4 | overall | P0 | 0.2251 | 0.1965 | 0.2537 | 0.1667 | 804 |
| B4 | overall | P1 | 0.6915 | 0.6567 | 0.7239 | 0.1667 | 804 |
| B4 | overall | P2 | 0.1057 | 0.0858 | 0.1256 | 0.1667 | 804 |
| B4 | overall | P3 | 0.3047 | 0.2748 | 0.3396 | 0.1667 | 804 |
| B4 | overall | P4 | 0.6455 | 0.6107 | 0.6791 | 0.1667 | 804 |
| B4 | overall | P5 | 0.3035 | 0.2687 | 0.3383 | 0.1667 | 804 |
| B4 | Early | P0 | 0.1381 | 0.0970 | 0.1828 | 0.1667 | 268 |
| B4 | Early | P1 | 0.8172 | 0.7687 | 0.8619 | 0.1667 | 268 |
| B4 | Early | P2 | 0.0522 | 0.0261 | 0.0821 | 0.1667 | 268 |
| B4 | Early | P3 | 0.3358 | 0.2799 | 0.3955 | 0.1667 | 268 |
| B4 | Early | P4 | 0.7500 | 0.6978 | 0.8022 | 0.1667 | 268 |
| B4 | Early | P5 | 0.1716 | 0.1269 | 0.2201 | 0.1667 | 268 |
| B4 | Middle | P0 | 0.3022 | 0.2500 | 0.3582 | 0.1667 | 268 |
| B4 | Middle | P1 | 0.7201 | 0.6642 | 0.7725 | 0.1667 | 268 |
| B4 | Middle | P2 | 0.1231 | 0.0858 | 0.1642 | 0.1667 | 268 |
| B4 | Middle | P3 | 0.3284 | 0.2724 | 0.3843 | 0.1667 | 268 |
| B4 | Middle | P4 | 0.7090 | 0.6493 | 0.7687 | 0.1667 | 268 |
| B4 | Middle | P5 | 0.2985 | 0.2425 | 0.3545 | 0.1667 | 268 |
| B4 | Late | P0 | 0.2351 | 0.1866 | 0.2873 | 0.1667 | 268 |
| B4 | Late | P1 | 0.5373 | 0.4776 | 0.5970 | 0.1667 | 268 |
| B4 | Late | P2 | 0.1418 | 0.0970 | 0.1828 | 0.1667 | 268 |
| B4 | Late | P3 | 0.2500 | 0.1978 | 0.3022 | 0.1667 | 268 |
| B4 | Late | P4 | 0.4776 | 0.4179 | 0.5373 | 0.1667 | 268 |
| B4 | Late | P5 | 0.4403 | 0.3806 | 0.5000 | 0.1667 | 268 |
| B5 | overall | P0 | 0.0286 | 0.0187 | 0.0410 | 0.1667 | 804 |
| B5 | overall | P1 | 0.5709 | 0.5348 | 0.6057 | 0.1667 | 804 |
| B5 | overall | P2 | 0.0485 | 0.0348 | 0.0634 | 0.1667 | 804 |
| B5 | overall | P3 | 0.6294 | 0.5970 | 0.6617 | 0.1667 | 804 |
| B5 | overall | P4 | 0.0771 | 0.0585 | 0.0970 | 0.1667 | 804 |
| B5 | overall | P5 | 0.0286 | 0.0187 | 0.0410 | 0.1667 | 804 |
| B5 | Early | P0 | 0.0299 | 0.0112 | 0.0522 | 0.1667 | 268 |
| B5 | Early | P1 | 0.8582 | 0.8134 | 0.8993 | 0.1667 | 268 |
| B5 | Early | P2 | 0.0485 | 0.0224 | 0.0746 | 0.1667 | 268 |
| B5 | Early | P3 | 0.3619 | 0.3022 | 0.4216 | 0.1667 | 268 |
| B5 | Early | P4 | 0.0821 | 0.0522 | 0.1157 | 0.1667 | 268 |
| B5 | Early | P5 | 0.0485 | 0.0261 | 0.0784 | 0.1667 | 268 |
| B5 | Middle | P0 | 0.0373 | 0.0149 | 0.0597 | 0.1667 | 268 |
| B5 | Middle | P1 | 0.5709 | 0.5112 | 0.6306 | 0.1667 | 268 |
| B5 | Middle | P2 | 0.0672 | 0.0373 | 0.0970 | 0.1667 | 268 |
| B5 | Middle | P3 | 0.6978 | 0.6455 | 0.7537 | 0.1667 | 268 |
| B5 | Middle | P4 | 0.0821 | 0.0522 | 0.1157 | 0.1667 | 268 |
| B5 | Middle | P5 | 0.0224 | 0.0075 | 0.0410 | 0.1667 | 268 |
| B5 | Late | P0 | 0.0187 | 0.0037 | 0.0373 | 0.1667 | 268 |
| B5 | Late | P1 | 0.2836 | 0.2313 | 0.3358 | 0.1667 | 268 |
| B5 | Late | P2 | 0.0299 | 0.0112 | 0.0522 | 0.1667 | 268 |
| B5 | Late | P3 | 0.8284 | 0.7836 | 0.8731 | 0.1667 | 268 |
| B5 | Late | P4 | 0.0672 | 0.0373 | 0.1007 | 0.1667 | 268 |
| B5 | Late | P5 | 0.0149 | 0.0037 | 0.0299 | 0.1667 | 268 |
| B6 | overall | P1 | 0.5485 | 0.5112 | 0.5858 | 0.2000 | 804 |
| B6 | overall | P2 | 0.3383 | 0.3047 | 0.3731 | 0.2000 | 804 |
| B6 | overall | P3 | 0.5410 | 0.5025 | 0.5796 | 0.2000 | 804 |
| B6 | overall | P4 | 0.7525 | 0.7177 | 0.7848 | 0.2000 | 804 |
| B6 | overall | P5 | 0.5498 | 0.5124 | 0.5871 | 0.2000 | 804 |
| B6 | Early | P1 | 0.5336 | 0.4739 | 0.5896 | 0.2000 | 268 |
| B6 | Early | P2 | 0.3246 | 0.2687 | 0.3806 | 0.2000 | 268 |
| B6 | Early | P3 | 0.6231 | 0.5634 | 0.6791 | 0.2000 | 268 |
| B6 | Early | P4 | 0.8619 | 0.8172 | 0.9030 | 0.2000 | 268 |
| B6 | Early | P5 | 0.4552 | 0.3992 | 0.5112 | 0.2000 | 268 |
| B6 | Middle | P1 | 0.5970 | 0.5373 | 0.6567 | 0.2000 | 268 |
| B6 | Middle | P2 | 0.3731 | 0.3209 | 0.4328 | 0.2000 | 268 |
| B6 | Middle | P3 | 0.5336 | 0.4739 | 0.5933 | 0.2000 | 268 |
| B6 | Middle | P4 | 0.7761 | 0.7239 | 0.8246 | 0.2000 | 268 |
| B6 | Middle | P5 | 0.5784 | 0.5187 | 0.6381 | 0.2000 | 268 |
| B6 | Late | P1 | 0.5149 | 0.4552 | 0.5746 | 0.2000 | 268 |
| B6 | Late | P2 | 0.3172 | 0.2612 | 0.3769 | 0.2000 | 268 |
| B6 | Late | P3 | 0.4664 | 0.4067 | 0.5261 | 0.2000 | 268 |
| B6 | Late | P4 | 0.6194 | 0.5597 | 0.6791 | 0.2000 | 268 |
| B6 | Late | P5 | 0.6157 | 0.5597 | 0.6716 | 0.2000 | 268 |
| B7 | overall | P0 | 0.2811 | 0.2512 | 0.3122 | 0.2000 | 804 |
| B7 | overall | P1P2 | 0.7711 | 0.7469 | 0.7948 | 0.2000 | 1608 |
| B7 | overall | P3 | 0.4328 | 0.3918 | 0.4726 | 0.2000 | 804 |
| B7 | overall | P4 | 0.7450 | 0.7102 | 0.7774 | 0.2000 | 804 |
| B7 | overall | P5 | 0.4751 | 0.4366 | 0.5124 | 0.2000 | 804 |
| B7 | Early | P0 | 0.3358 | 0.2799 | 0.3918 | 0.2000 | 268 |
| B7 | Early | P1P2 | 0.7705 | 0.7276 | 0.8097 | 0.2000 | 536 |
| B7 | Early | P3 | 0.5261 | 0.4664 | 0.5858 | 0.2000 | 268 |
| B7 | Early | P4 | 0.8507 | 0.8060 | 0.8955 | 0.2000 | 268 |
| B7 | Early | P5 | 0.3769 | 0.3172 | 0.4328 | 0.2000 | 268 |
| B7 | Middle | P0 | 0.2761 | 0.2201 | 0.3284 | 0.2000 | 268 |
| B7 | Middle | P1P2 | 0.8190 | 0.7836 | 0.8526 | 0.2000 | 536 |
| B7 | Middle | P3 | 0.4104 | 0.3507 | 0.4701 | 0.2000 | 268 |
| B7 | Middle | P4 | 0.7836 | 0.7313 | 0.8321 | 0.2000 | 268 |
| B7 | Middle | P5 | 0.4963 | 0.4366 | 0.5597 | 0.2000 | 268 |
| B7 | Late | P0 | 0.2313 | 0.1791 | 0.2799 | 0.2000 | 268 |
| B7 | Late | P1P2 | 0.7239 | 0.6810 | 0.7631 | 0.2000 | 536 |
| B7 | Late | P3 | 0.3619 | 0.3060 | 0.4216 | 0.2000 | 268 |
| B7 | Late | P4 | 0.6007 | 0.5373 | 0.6604 | 0.2000 | 268 |
| B7 | Late | P5 | 0.5522 | 0.4925 | 0.6082 | 0.2000 | 268 |

## Part B1 GEE

Logistic GEE of out-of-fold correctness, clustered by dialogue: `correct ~ position + log(context_word_count)`. Working correlation: exchangeable. Position reference: Early.

| term | coef | std_err | p_value | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| Intercept | 0.0208 | 0.3351 | 0.9505 | -0.6360 | 0.6776 |
| C(position, Treatment(reference='Early'))[T.Late] | -0.2382 | 0.1013 | 0.0186 | -0.4367 | -0.0398 |
| C(position, Treatment(reference='Early'))[T.Middle] | 0.0382 | 0.0773 | 0.6210 | -0.1133 | 0.1898 |
| log_context | -0.0091 | 0.0604 | 0.8797 | -0.1275 | 0.1092 |

## Part C predictions

Verdicts use the pre-specified interval rule. Holm p-values are within each marker and do not change the verdict. Erratum 2 predictions are exploratory for Gemini and Claude, and pre-specified for any model run after 2026-10-02. They are not part of the realised rule.

| scope | contrast | marker | direction | specification | estimate | ci_low | ci_high | p_value | p_holm | n_pairs | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1649 | -0.2874 | -0.0381 | 0.0120 | 0.0120 | 804 | confirmed |
| Early | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.1901 | -0.3322 | -0.0564 | 0.0050 | 0.0350 | 268 | confirmed |
| Middle | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.2428 | -0.4428 | -0.0315 | 0.0190 | 0.0950 | 268 | confirmed |
| Late | P1 - P0 | psychosocial_per_100 | lower | pre-specified | -0.0620 | -0.3058 | 0.2077 | 0.6470 | 1.0000 | 268 | not confirmed |
| overall | P1 - P0 | med_per_100 | higher | pre-specified | 0.3298 | -0.4208 | 1.0442 | 0.3750 | 0.3750 | 804 | not confirmed |
| Early | P1 - P0 | med_per_100 | higher | pre-specified | -1.2013 | -2.4876 | 0.1106 | 0.0780 | 0.1560 | 268 | not confirmed |
| Middle | P1 - P0 | med_per_100 | higher | pre-specified | -0.2071 | -1.4885 | 1.0011 | 0.7110 | 0.7110 | 268 | not confirmed |
| Late | P1 - P0 | med_per_100 | higher | pre-specified | 2.3978 | 1.2484 | 3.7362 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P1 - P0 | share_open | lower | pre-specified | 0.0120 | -0.0184 | 0.0411 | 0.4210 | 0.4210 | 348 | not confirmed |
| Early | P1 - P0 | share_open | lower | pre-specified | -0.0009 | -0.0315 | 0.0289 | 0.9860 | 1.0000 | 196 | not confirmed |
| Middle | P1 - P0 | share_open | lower | pre-specified | 0.0446 | -0.0099 | 0.1089 | 0.1300 | 0.7800 | 101 | not confirmed |
| Late | P1 - P0 | share_open | lower | pre-specified | -0.0033 | -0.1275 | 0.1242 | 0.9910 | 1.0000 | 51 | not confirmed |
| overall | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1613 | 0.0626 | 0.2666 | 0.0010 | 0.0020 | 804 | confirmed |
| Early | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.2604 | 0.0943 | 0.4419 | 0.0020 | 0.0160 | 268 | confirmed |
| Middle | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.1930 | 0.0442 | 0.3531 | 0.0070 | 0.0420 | 268 | confirmed |
| Late | P2 - P1 | psychosocial_per_100 | higher | pre-specified | 0.0304 | -0.1634 | 0.2273 | 0.7890 | 1.0000 | 268 | not confirmed |
| overall | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.2600 | 0.1164 | 0.4078 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.5281 | 0.2887 | 0.7901 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.2338 | 0.0111 | 0.4494 | 0.0400 | 0.1600 | 268 | confirmed |
| Late | P3 - P0 | psychosocial_per_100 | higher | pre-specified | 0.0181 | -0.2505 | 0.3084 | 0.9450 | 1.0000 | 268 | not confirmed |
| overall | P3 - P0 | share_open | higher | pre-specified | 0.1025 | 0.0717 | 0.1338 | 0.0000 | 0.0000 | 348 | confirmed |
| Early | P3 - P0 | share_open | higher | pre-specified | 0.1102 | 0.0701 | 0.1512 | 0.0000 | 0.0000 | 183 | confirmed |
| Middle | P3 - P0 | share_open | higher | pre-specified | 0.1250 | 0.0694 | 0.1883 | 0.0000 | 0.0000 | 108 | confirmed |
| Late | P3 - P0 | share_open | higher | pre-specified | 0.0351 | -0.0526 | 0.1170 | 0.4300 | 1.0000 | 57 | not confirmed |
| overall | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 2.4966 | 2.1964 | 2.8004 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 4.5671 | 3.9803 | 5.1740 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 2.1808 | 1.7296 | 2.6207 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | psychosocial_per_100 | higher | pre-specified | 0.7420 | 0.4216 | 1.0724 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P0 | share_open | higher | pre-specified | 0.4726 | 0.4263 | 0.5187 | 0.0000 | 0.0000 | 341 | confirmed |
| Early | P4 - P0 | share_open | higher | pre-specified | 0.4842 | 0.4236 | 0.5400 | 0.0000 | 0.0000 | 179 | confirmed |
| Middle | P4 - P0 | share_open | higher | pre-specified | 0.5236 | 0.4340 | 0.6085 | 0.0000 | 0.0000 | 106 | confirmed |
| Late | P4 - P0 | share_open | higher | pre-specified | 0.3393 | 0.2053 | 0.4732 | 0.0000 | 0.0000 | 56 | confirmed |
| overall | P4 - P0 | med_per_100 | lower | pre-specified | -5.6364 | -6.2331 | -5.0852 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P0 | med_per_100 | lower | pre-specified | -5.8811 | -6.8635 | -4.9240 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P0 | med_per_100 | lower | pre-specified | -6.7328 | -7.5858 | -5.9231 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P0 | med_per_100 | lower | pre-specified | -4.2953 | -5.1555 | -3.4178 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 2.2366 | 1.9417 | 2.5459 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 4.0390 | 3.4536 | 4.6712 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 1.9470 | 1.4840 | 2.4143 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | psychosocial_per_100 | higher | pre-specified | 0.7238 | 0.3834 | 1.0672 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P4 - P3 | med_per_100 | lower | pre-specified | -4.0318 | -4.5228 | -3.5553 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P4 - P3 | med_per_100 | lower | pre-specified | -4.4014 | -5.2623 | -3.5689 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P4 - P3 | med_per_100 | lower | pre-specified | -5.1196 | -5.8931 | -4.3528 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P4 - P3 | med_per_100 | lower | pre-specified | -2.5743 | -3.3360 | -1.7788 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.0940 | 0.0636 | 0.1289 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.0925 | 0.0399 | 0.1550 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.0848 | 0.0349 | 0.1436 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | instruction_per_100 | higher | pre-specified | 0.1046 | 0.0634 | 0.1512 | 0.0000 | 0.0000 | 268 | confirmed |
| overall | P5 - P0 | n_leading | higher | pre-specified | -0.0025 | -0.0124 | 0.0062 | 0.7280 | 0.7280 | 804 | not confirmed |
| Early | P5 - P0 | n_leading | higher | pre-specified | 0.0112 | -0.0037 | 0.0261 | 0.2400 | 0.7200 | 268 | not confirmed |
| Middle | P5 - P0 | n_leading | higher | pre-specified | -0.0112 | -0.0336 | 0.0075 | 0.4200 | 0.7200 | 268 | not confirmed |
| Late | P5 - P0 | n_leading | higher | pre-specified | -0.0075 | -0.0187 | 0.0000 | 0.2840 | 0.7200 | 268 | not confirmed |
| overall | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.2281 | -0.3034 | -0.1539 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.3621 | -0.5287 | -0.2134 | 0.0000 | 0.0000 | 268 | confirmed |
| Middle | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.2203 | -0.3393 | -0.0958 | 0.0010 | 0.0020 | 268 | confirmed |
| Late | P5 - P0 | invitation_per_100 | lower | pre-specified | -0.1020 | -0.2405 | 0.0240 | 0.1390 | 0.1390 | 268 | not confirmed |
| overall | P5 - P0 | share_open | lower | pre-specified | 0.0270 | 0.0010 | 0.0534 | 0.0440 | 0.0880 | 327 | opposite |
| Early | P5 - P0 | share_open | lower | pre-specified | 0.0414 | 0.0135 | 0.0742 | 0.0030 | 0.0210 | 173 | opposite |
| Middle | P5 - P0 | share_open | lower | pre-specified | -0.0067 | -0.0455 | 0.0303 | 0.7270 | 1.0000 | 99 | not confirmed |
| Late | P5 - P0 | share_open | lower | pre-specified | 0.0424 | -0.0515 | 0.1364 | 0.3470 | 1.0000 | 55 | not confirmed |
| overall | P5 - P0 | has_question | lower | pre-specified | 0.0187 | -0.0212 | 0.0585 | 0.4100 | 0.4100 | 804 | not confirmed |
| Early | P5 - P0 | has_question | lower | pre-specified | 0.0075 | -0.0448 | 0.0597 | 0.8470 | 1.0000 | 268 | not confirmed |
| Middle | P5 - P0 | has_question | lower | pre-specified | -0.0037 | -0.0784 | 0.0709 | 0.9660 | 1.0000 | 268 | not confirmed |
| Late | P5 - P0 | has_question | lower | pre-specified | 0.0522 | -0.0187 | 0.1269 | 0.1800 | 0.5400 | 268 | not confirmed |
| overall | P5 - P0 | plan_statement_present | higher | pre-specified | 0.1455 | 0.1119 | 0.1791 | 0.0000 | 0.0000 | 804 | confirmed |
| Early | P5 - P0 | plan_statement_present | higher | pre-specified | 0.0448 | 0.0037 | 0.0858 | 0.0400 | 0.0400 | 268 | confirmed |
| Middle | P5 - P0 | plan_statement_present | higher | pre-specified | 0.1828 | 0.1306 | 0.2388 | 0.0000 | 0.0000 | 268 | confirmed |
| Late | P5 - P0 | plan_statement_present | higher | pre-specified | 0.2090 | 0.1417 | 0.2761 | 0.0000 | 0.0000 | 268 | confirmed |

## H2 position tests

The estimate is the Late paired difference minus the Early paired difference. H2 predicts that this move is toward zero: positive when the main prediction is lower, and negative when the main prediction is higher.

| contrast | marker | prediction_direction | specification | estimate_late_minus_early | ci_low | ci_high | p_value | p_holm | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 - P0 | psychosocial_per_100 | lower | pre-specified | 0.1281 | -0.1438 | 0.4245 | 0.3840 | 0.3840 | not confirmed |
| P1 - P0 | med_per_100 | higher | pre-specified | 3.5990 | 1.7409 | 5.5188 | 0.0000 | 0.0000 | opposite |
| P1 - P0 | share_open | lower | pre-specified | -0.0024 | -0.1192 | 0.1216 | 0.9950 | 1.0000 | not confirmed |
| P2 - P1 | psychosocial_per_100 | higher | pre-specified | -0.2299 | -0.4932 | 0.0232 | 0.0760 | 0.1520 | not confirmed |
| P3 - P0 | psychosocial_per_100 | higher | pre-specified | -0.5100 | -0.8747 | -0.1204 | 0.0100 | 0.0300 | confirmed |
| P3 - P0 | share_open | higher | pre-specified | -0.0751 | -0.1789 | 0.0255 | 0.1320 | 0.3960 | not confirmed |
| P4 - P0 | psychosocial_per_100 | higher | pre-specified | -3.8251 | -4.5054 | -3.1764 | 0.0000 | 0.0000 | confirmed |
| P4 - P0 | share_open | higher | pre-specified | -0.1449 | -0.3023 | 0.0054 | 0.0620 | 0.2480 | not confirmed |
| P4 - P0 | med_per_100 | lower | pre-specified | 1.5858 | 0.3983 | 2.8229 | 0.0120 | 0.0120 | confirmed |
| P4 - P3 | psychosocial_per_100 | higher | pre-specified | -3.3152 | -4.0150 | -2.6220 | 0.0000 | 0.0000 | confirmed |
| P4 - P3 | med_per_100 | lower | pre-specified | 1.8271 | 0.7253 | 3.0243 | 0.0000 | 0.0000 | confirmed |
| P5 - P0 | instruction_per_100 | higher | pre-specified | 0.0121 | -0.0587 | 0.0761 | 0.7300 | 0.7300 | not confirmed |
| P5 - P0 | n_leading | higher | pre-specified | -0.0187 | -0.0410 | 0.0000 | 0.0780 | 0.0780 | not confirmed |
| P5 - P0 | invitation_per_100 | lower | pre-specified | 0.2600 | 0.0483 | 0.4683 | 0.0120 | 0.0120 | confirmed |
| P5 - P0 | share_open | lower | pre-specified | 0.0010 | -0.0954 | 0.1010 | 0.9850 | 1.0000 | not confirmed |
| P5 - P0 | has_question | lower | pre-specified | 0.0448 | -0.0448 | 0.1306 | 0.3320 | 0.3320 | not confirmed |
| P5 - P0 | plan_statement_present | higher | pre-specified | 0.1642 | 0.0821 | 0.2388 | 0.0000 | 0.0000 | opposite |

## Realised personas

A persona is realised when its B1 recall interval lies entirely above chance and every pre-specified prediction against P0 is confirmed. A persona with no prediction against P0 is not assessed. Erratum 1, 2026-10-02. The two erratum 2 P5 predictions are excluded from this count.

| scope | persona | recall | ci_low | ci_high | chance | recall_above_chance | n_predictions_vs_p0 | n_confirmed_vs_p0 | realised | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | P1 | 0.5236 | 0.4851 | 0.5597 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| overall | P2 | 0.2935 | 0.2600 | 0.3259 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| overall | P3 | 0.4540 | 0.4141 | 0.4938 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| overall | P4 | 0.7475 | 0.7127 | 0.7799 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| overall | P5 | 0.5025 | 0.4627 | 0.5410 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Early | P1 | 0.5037 | 0.4440 | 0.5634 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Early | P2 | 0.2873 | 0.2313 | 0.3470 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Early | P3 | 0.5448 | 0.4851 | 0.6045 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Early | P4 | 0.8545 | 0.8097 | 0.8955 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Early | P5 | 0.4030 | 0.3433 | 0.4590 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Middle | P1 | 0.5821 | 0.5187 | 0.6418 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Middle | P2 | 0.3433 | 0.2910 | 0.3993 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Middle | P3 | 0.4254 | 0.3657 | 0.4851 | 0.1667 | 1 | 2 | 2 | 1 | realised |
| Middle | P4 | 0.7873 | 0.7351 | 0.8358 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Middle | P5 | 0.5373 | 0.4776 | 0.5970 | 0.1667 | 1 | 4 | 2 | 0 | not realised |
| Late | P1 | 0.4851 | 0.4216 | 0.5448 | 0.1667 | 1 | 3 | 1 | 0 | not realised |
| Late | P2 | 0.2500 | 0.1978 | 0.2986 | 0.1667 | 1 | 0 | 0 |  | not assessed |
| Late | P3 | 0.3918 | 0.3358 | 0.4515 | 0.1667 | 1 | 2 | 0 | 0 | not realised |
| Late | P4 | 0.6007 | 0.5373 | 0.6604 | 0.1667 | 1 | 3 | 3 | 1 | realised |
| Late | P5 | 0.5672 | 0.5075 | 0.6231 | 0.1667 | 1 | 4 | 1 | 0 | not realised |

## Descriptive means

| condition | scope | marker | mean | n |
| --- | --- | --- | --- | --- |
| P0 | overall | has_question | 0.6045 | 804 |
| P0 | overall | plan_statement_present | 0.0945 | 804 |
| P0 | overall | empathy_phrases_present | 0.0274 | 804 |
| P0 | overall | hedge_per_100 | 0.3186 | 804 |
| P0 | overall | n_words | 57.6343 | 804 |
| P0 | overall | persona_distance | -0.0000 | 804 |
| P0 | Early | has_question | 0.8022 | 268 |
| P0 | Early | plan_statement_present | 0.0634 | 268 |
| P0 | Early | empathy_phrases_present | 0.0672 | 268 |
| P0 | Early | hedge_per_100 | 0.3440 | 268 |
| P0 | Early | n_words | 33.9440 | 268 |
| P0 | Early | persona_distance | -0.0000 | 268 |
| P0 | Middle | has_question | 0.5970 | 268 |
| P0 | Middle | plan_statement_present | 0.0634 | 268 |
| P0 | Middle | empathy_phrases_present | 0.0075 | 268 |
| P0 | Middle | hedge_per_100 | 0.2682 | 268 |
| P0 | Middle | n_words | 57.5746 | 268 |
| P0 | Middle | persona_distance | -0.0000 | 268 |
| P0 | Late | has_question | 0.4142 | 268 |
| P0 | Late | plan_statement_present | 0.1567 | 268 |
| P0 | Late | empathy_phrases_present | 0.0075 | 268 |
| P0 | Late | hedge_per_100 | 0.3438 | 268 |
| P0 | Late | n_words | 81.3843 | 268 |
| P0 | Late | persona_distance | -0.0000 | 268 |
| P1 | overall | has_question | 0.6443 | 804 |
| P1 | overall | plan_statement_present | 0.0249 | 804 |
| P1 | overall | empathy_phrases_present | 0.0012 | 804 |
| P1 | overall | hedge_per_100 | 0.1273 | 804 |
| P1 | overall | n_words | 39.1007 | 804 |
| P1 | overall | persona_distance | 0.4136 | 804 |
| P1 | Early | has_question | 0.9216 | 268 |
| P1 | Early | plan_statement_present | 0.0000 | 268 |
| P1 | Early | empathy_phrases_present | 0.0000 | 268 |
| P1 | Early | hedge_per_100 | 0.1971 | 268 |
| P1 | Early | n_words | 17.0149 | 268 |
| P1 | Early | persona_distance | 0.4623 | 268 |
| P1 | Middle | has_question | 0.6306 | 268 |
| P1 | Middle | plan_statement_present | 0.0112 | 268 |
| P1 | Middle | empathy_phrases_present | 0.0000 | 268 |
| P1 | Middle | hedge_per_100 | 0.0937 | 268 |
| P1 | Middle | n_words | 35.1940 | 268 |
| P1 | Middle | persona_distance | 0.4279 | 268 |
| P1 | Late | has_question | 0.3806 | 268 |
| P1 | Late | plan_statement_present | 0.0634 | 268 |
| P1 | Late | empathy_phrases_present | 0.0037 | 268 |
| P1 | Late | hedge_per_100 | 0.0910 | 268 |
| P1 | Late | n_words | 65.0933 | 268 |
| P1 | Late | persona_distance | 0.3506 | 268 |
| P2 | overall | has_question | 0.6530 | 804 |
| P2 | overall | plan_statement_present | 0.0398 | 804 |
| P2 | overall | empathy_phrases_present | 0.0050 | 804 |
| P2 | overall | hedge_per_100 | 0.2082 | 804 |
| P2 | overall | n_words | 49.3035 | 804 |
| P2 | overall | persona_distance | 0.3456 | 804 |
| P2 | Early | has_question | 0.9104 | 268 |
| P2 | Early | plan_statement_present | 0.0112 | 268 |
| P2 | Early | empathy_phrases_present | 0.0112 | 268 |
| P2 | Early | hedge_per_100 | 0.2066 | 268 |
| P2 | Early | n_words | 23.5485 | 268 |
| P2 | Early | persona_distance | 0.4116 | 268 |
| P2 | Middle | has_question | 0.6418 | 268 |
| P2 | Middle | plan_statement_present | 0.0112 | 268 |
| P2 | Middle | empathy_phrases_present | 0.0037 | 268 |
| P2 | Middle | hedge_per_100 | 0.1880 | 268 |
| P2 | Middle | n_words | 44.6306 | 268 |
| P2 | Middle | persona_distance | 0.3371 | 268 |
| P2 | Late | has_question | 0.4067 | 268 |
| P2 | Late | plan_statement_present | 0.0970 | 268 |
| P2 | Late | empathy_phrases_present | 0.0000 | 268 |
| P2 | Late | hedge_per_100 | 0.2299 | 268 |
| P2 | Late | n_words | 79.7313 | 268 |
| P2 | Late | persona_distance | 0.2880 | 268 |
| P3 | overall | has_question | 0.6443 | 804 |
| P3 | overall | plan_statement_present | 0.1107 | 804 |
| P3 | overall | empathy_phrases_present | 0.0498 | 804 |
| P3 | overall | hedge_per_100 | 0.5458 | 804 |
| P3 | overall | n_words | 65.1654 | 804 |
| P3 | overall | persona_distance | 0.2914 | 804 |
| P3 | Early | has_question | 0.8619 | 268 |
| P3 | Early | plan_statement_present | 0.0299 | 268 |
| P3 | Early | empathy_phrases_present | 0.1082 | 268 |
| P3 | Early | hedge_per_100 | 0.4262 | 268 |
| P3 | Early | n_words | 42.9552 | 268 |
| P3 | Early | persona_distance | 0.3281 | 268 |
| P3 | Middle | has_question | 0.6455 | 268 |
| P3 | Middle | plan_statement_present | 0.0933 | 268 |
| P3 | Middle | empathy_phrases_present | 0.0261 | 268 |
| P3 | Middle | hedge_per_100 | 0.5040 | 268 |
| P3 | Middle | n_words | 66.0373 | 268 |
| P3 | Middle | persona_distance | 0.2683 | 268 |
| P3 | Late | has_question | 0.4254 | 268 |
| P3 | Late | plan_statement_present | 0.2090 | 268 |
| P3 | Late | empathy_phrases_present | 0.0149 | 268 |
| P3 | Late | hedge_per_100 | 0.7073 | 268 |
| P3 | Late | n_words | 86.5037 | 268 |
| P3 | Late | persona_distance | 0.2778 | 268 |
| P4 | overall | has_question | 0.6803 | 804 |
| P4 | overall | plan_statement_present | 0.0771 | 804 |
| P4 | overall | empathy_phrases_present | 0.1455 | 804 |
| P4 | overall | hedge_per_100 | 0.6130 | 804 |
| P4 | overall | n_words | 54.6256 | 804 |
| P4 | overall | persona_distance | 0.3724 | 804 |
| P4 | Early | has_question | 0.9030 | 268 |
| P4 | Early | plan_statement_present | 0.0112 | 268 |
| P4 | Early | empathy_phrases_present | 0.1940 | 268 |
| P4 | Early | hedge_per_100 | 0.3765 | 268 |
| P4 | Early | n_words | 39.3769 | 268 |
| P4 | Early | persona_distance | 0.4499 | 268 |
| P4 | Middle | has_question | 0.6567 | 268 |
| P4 | Middle | plan_statement_present | 0.0485 | 268 |
| P4 | Middle | empathy_phrases_present | 0.1418 | 268 |
| P4 | Middle | hedge_per_100 | 0.6965 | 268 |
| P4 | Middle | n_words | 53.8060 | 268 |
| P4 | Middle | persona_distance | 0.3496 | 268 |
| P4 | Late | has_question | 0.4813 | 268 |
| P4 | Late | plan_statement_present | 0.1716 | 268 |
| P4 | Late | empathy_phrases_present | 0.1007 | 268 |
| P4 | Late | hedge_per_100 | 0.7659 | 268 |
| P4 | Late | n_words | 70.6940 | 268 |
| P4 | Late | persona_distance | 0.3178 | 268 |
| P5 | overall | has_question | 0.6231 | 804 |
| P5 | overall | plan_statement_present | 0.2400 | 804 |
| P5 | overall | empathy_phrases_present | 0.0137 | 804 |
| P5 | overall | hedge_per_100 | 0.3430 | 804 |
| P5 | overall | n_words | 63.2699 | 804 |
| P5 | overall | persona_distance | 0.3113 | 804 |
| P5 | Early | has_question | 0.8097 | 268 |
| P5 | Early | plan_statement_present | 0.1082 | 268 |
| P5 | Early | empathy_phrases_present | 0.0149 | 268 |
| P5 | Early | hedge_per_100 | 0.2765 | 268 |
| P5 | Early | n_words | 33.0037 | 268 |
| P5 | Early | persona_distance | 0.3394 | 268 |
| P5 | Middle | has_question | 0.5933 | 268 |
| P5 | Middle | plan_statement_present | 0.2463 | 268 |
| P5 | Middle | empathy_phrases_present | 0.0149 | 268 |
| P5 | Middle | hedge_per_100 | 0.2922 | 268 |
| P5 | Middle | n_words | 63.5000 | 268 |
| P5 | Middle | persona_distance | 0.3094 | 268 |
| P5 | Late | has_question | 0.4664 | 268 |
| P5 | Late | plan_statement_present | 0.3657 | 268 |
| P5 | Late | empathy_phrases_present | 0.0112 | 268 |
| P5 | Late | hedge_per_100 | 0.4604 | 268 |
| P5 | Late | n_words | 93.3060 | 268 |
| P5 | Late | persona_distance | 0.2850 | 268 |

## Part D

Part D drops 3 analysed rows with any format flag, leaving 4821. Prediction verdicts changed in 0 of 68 rows. H2 verdicts changed in 0 of 17 rows. Realised flags changed in 0 of 20 rows.

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
