# pyspark-etl-template

---

[![python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![pyspark](https://img.shields.io/badge/pyspark-3.3.0-brightgreen)](https://spark.apache.org/docs/latest/api/python/)

pyspark etl项目工程化模板, 可参考文档：[Pyspark-etl-doc](https://jingyuanr.github.io/pyspark-etl-project-specification/)

## 使用方式

### 1. 开发前准备
- Install python 3.10
    ```angular2html
    https://www.python.org/downloads/
    ```
- Install Java 8
    ```angular2html
    https://www.oracle.com/java/technologies/downloads/#java8
    ```
- Install hadoop 3.0+
    ```bash
    # https://archive.apache.org/dist/hadoop/common/
    tar -zxvf hadoop-3.1.1.tar.gz
    ```
- Install [pipenv](https://pypi.org/project/pipenv/)
    ```bash
    pip install pipenv
    ```
- Install pyspark
    ```bash
    pip install pyspark
    ```
### 2. 克隆项目
```bash
git clone https://github.com/JingyuanR/pyspark-project-template.git
```

### 3. 初始化环境
```bash
pyspark-project-template> pipenv install
```

## 项目结构
```angular2html
├─src
│  │  __init__.py
│  │
│  ├─etl_project
│  │  │  app.py
│  │  │  executor.py
│  │  │  constants.py
│  │  │  __init__.py
│  │  │
│  │  ├─configs
│  │  │  │  dev.toml
│  │  │  │  global.toml
│  │  │  │  prod.toml
│  │  │  └─ test.toml
│  │  │
│  │  ├─dependecies
│  │  │  │  log.py
│  │  │  │  config.py
│  │  │  │  spark.py
│  │  │  └─ __init__.py
│  │  │
│  │  ├─tasks
│  │  │  │  __init__.py
│  │  │  │
│  │  │  └─abstract
│  │  │     │  task.py
│  │  │     │  transform.py
│  │  │     └─ __init__.py
│  │  │
│  │  └─utils
│  │         join.py
│  │         schema.py
│  │         exception.py
│  │         __init__.py
│  │
│  └─etl_project.egg-info
│         dependency_links.txt
│         PKG-INFO
│         requires.txt
│         SOURCES.txt
│         top_level.txt
│
└─tests
    │  conftest.py
    │  tests.py
    ├─ __init__.py
    │
    └─data

```