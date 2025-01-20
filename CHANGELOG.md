# Changelog

## [1.1.0](https://github.com/devopsarr/whisparr-py/compare/v1.0.1...v1.1.0) (2025-01-20)


### Features

* remove broken root api path ([a9d269f](https://github.com/devopsarr/whisparr-py/commit/a9d269f401389c9743b887c96071d2abba04f489))


### Bug Fixes

* **deps:** update openapitools/openapi-generator-cli docker tag to v7.10.0 ([17001c9](https://github.com/devopsarr/whisparr-py/commit/17001c9fc94f5281f8cabc307a84fddee4103721))
* **deps:** update openapitools/openapi-generator-cli docker tag to v7.11.0 ([b7d9d5b](https://github.com/devopsarr/whisparr-py/commit/b7d9d5ba46f612e07bf09d0f7d85a7b975add471))
* **deps:** update openapitools/openapi-generator-cli docker tag to v7.9.0 ([8492a80](https://github.com/devopsarr/whisparr-py/commit/8492a8000726a2d3b724130fee3eb5a3e7b9504f))

## [1.0.1](https://github.com/devopsarr/whisparr-py/compare/v1.0.0...v1.0.1) (2024-02-21)


### Bug Fixes

* map Field to ContractField to avoid pydantic issue ([0caf78d](https://github.com/devopsarr/whisparr-py/commit/0caf78dc929f4aa1b637db981ec1110b0ab2fe0b))

## [1.0.0](https://github.com/devopsarr/whisparr-py/compare/v1.0.0...v1.0.0) (2024-02-20)


### ⚠ BREAKING CHANGES

* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x

### Features

* **devopsarr/prowlarr-py#11:** add request timeout to config ([cb0192b](https://github.com/devopsarr/whisparr-py/commit/cb0192b3f2d2a37d234087e9e07bf75d206277ab))
* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x ([bad01c0](https://github.com/devopsarr/whisparr-py/commit/bad01c0566c91648ab269116b65946df8d61879e))
* first configuration ([860d8a6](https://github.com/devopsarr/whisparr-py/commit/860d8a664b59eca475cd3500bbc4336cd44bb2c6))
* inject api version into readme ([4ed74b5](https://github.com/devopsarr/whisparr-py/commit/4ed74b5671066d7df81109abca345c6921a7d35d))
* pin openapi version and add version management ([fb7b738](https://github.com/devopsarr/whisparr-py/commit/fb7b738a198279f650c3f3423ea8cf1e47b331be))
* sdk generation alignment ([051e4f7](https://github.com/devopsarr/whisparr-py/commit/051e4f77dced7ec2068bb09b424eecdaeeff2c60))


### Bug Fixes

* **devopsarr/radarr-py#6:** indentation error on config ([6b6bae0](https://github.com/devopsarr/whisparr-py/commit/6b6bae0d3cd87ed719c8dbecc75e276e5f063eeb))
* **devopsarr/sonarr-py#6:** remove timespan validator ([9548251](https://github.com/devopsarr/whisparr-py/commit/95482519420631326be4af2f9f245a5c98b7a40b))
* **python:** wrong release versioning on configuration.py ([93c4bbb](https://github.com/devopsarr/whisparr-py/commit/93c4bbb6d1789b388267ffc65740bc67e7dc6a27))
* release please commented lines ([ab2f862](https://github.com/devopsarr/whisparr-py/commit/ab2f86214ef6603d2bc8b38570339956d32ebe6e))
* remove middle elements from method name ([29b0adc](https://github.com/devopsarr/whisparr-py/commit/29b0adc1753d0722eeb7800745e70df62710e7db))
* set pydantic version ([da77da5](https://github.com/devopsarr/whisparr-py/commit/da77da59560b4ae1ce364cebfad549c4377233a0))
* **whisparr:** use radarr swagger for now ([ae6e154](https://github.com/devopsarr/whisparr-py/commit/ae6e15461ae0c6c3c53397001bb68922b7be4d42))


### Miscellaneous Chores

* release 1.0.0 ([37fa212](https://github.com/devopsarr/whisparr-py/commit/37fa2121fdedcc30660fa1a1841f26dfe0c8a64c))

## [1.0.0](https://github.com/devopsarr/whisparr-py/compare/v0.3.0...v1.0.0) (2024-02-15)


### ⚠ BREAKING CHANGES

* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x

### Features

* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x ([bad01c0](https://github.com/devopsarr/whisparr-py/commit/bad01c0566c91648ab269116b65946df8d61879e))
* inject api version into readme ([4ed74b5](https://github.com/devopsarr/whisparr-py/commit/4ed74b5671066d7df81109abca345c6921a7d35d))


### Bug Fixes

* **python:** wrong release versioning on configuration.py ([93c4bbb](https://github.com/devopsarr/whisparr-py/commit/93c4bbb6d1789b388267ffc65740bc67e7dc6a27))
* release please commented lines ([ab2f862](https://github.com/devopsarr/whisparr-py/commit/ab2f86214ef6603d2bc8b38570339956d32ebe6e))
* remove middle elements from method name ([29b0adc](https://github.com/devopsarr/whisparr-py/commit/29b0adc1753d0722eeb7800745e70df62710e7db))

## [0.3.0](https://github.com/devopsarr/whisparr-py/compare/v0.2.2...v0.3.0) (2023-07-21)


### Features

* **devopsarr/prowlarr-py#11:** add request timeout to config ([cb0192b](https://github.com/devopsarr/whisparr-py/commit/cb0192b3f2d2a37d234087e9e07bf75d206277ab))
* pin openapi version and add version management ([fb7b738](https://github.com/devopsarr/whisparr-py/commit/fb7b738a198279f650c3f3423ea8cf1e47b331be))


### Bug Fixes

* set pydantic version ([da77da5](https://github.com/devopsarr/whisparr-py/commit/da77da59560b4ae1ce364cebfad549c4377233a0))

## [0.2.2](https://github.com/devopsarr/whisparr-py/compare/v0.2.1...v0.2.2) (2023-03-27)


### Bug Fixes

* **devopsarr/sonarr-py#6:** remove timespan validator ([9548251](https://github.com/devopsarr/whisparr-py/commit/95482519420631326be4af2f9f245a5c98b7a40b))

## [0.2.1](https://github.com/devopsarr/whisparr-py/compare/v0.2.0...v0.2.1) (2023-03-24)


### Bug Fixes

* **devopsarr/radarr-py#6:** indentation error on config ([6b6bae0](https://github.com/devopsarr/whisparr-py/commit/6b6bae0d3cd87ed719c8dbecc75e276e5f063eeb))

## [0.2.0](https://github.com/devopsarr/whisparr-py/compare/v0.1.0...v0.2.0) (2023-03-24)


### Features

* sdk generation alignment ([051e4f7](https://github.com/devopsarr/whisparr-py/commit/051e4f77dced7ec2068bb09b424eecdaeeff2c60))


### Bug Fixes

* **whisparr:** use radarr swagger for now ([ae6e154](https://github.com/devopsarr/whisparr-py/commit/ae6e15461ae0c6c3c53397001bb68922b7be4d42))

## 0.1.0 (2023-01-24)


### Features

* first configuration ([860d8a6](https://github.com/devopsarr/whisparr-py/commit/860d8a664b59eca475cd3500bbc4336cd44bb2c6))
