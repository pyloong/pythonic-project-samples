# pyspark-etl-template

---

[![python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![pyspark](https://img.shields.io/badge/pyspark-3.3.0-brightgreen)](https://spark.apache.org/docs/latest/api/python/)

pyspark etl项目工程化模板, 可参考文档：[Pyspark-etl-doc](https://pyloong.github.io/pythonic-project-guidelines/bigdata/basis/init/)

## 使用方式

### 1. 开发前准备
- Install python 3.9/3.10
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
- Install [poetry](https://python-poetry.org/docs/)
    ```bash
    pip install poetry
    ```
- Install [cookiecutter](https://github.com/cookiecutter/cookiecutter)
    ```bash
    # 安装或升级 cookiecutter
    pip install -U cookiecutter
    ```

### 2. 创建项目骨架

使用 [cookiecutter](https://github.com/cookiecutter/cookiecutter) 加载项目模板。通过交互操作，可以选择使用的功能。

在终端运行命令：

```bash
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-bigdata
```

### 3. 初始化环境
```bash
pyspark-project-template> poetry install
```

## 项目结构
```angular2html
├─src
│  │  __init__.py
│  │
│  └─pyspark_etl_template
│     │  cmdline.py
│     │  executor.py
│     │  constants.py
│     │  __init__.py
│     │
│     ├─configs
│     │  │  dev.toml
│     │  │  global.toml
│     │  │  prod.toml
│     │  └─ test.toml
│     │
│     ├─dependecies
│     │  │  log.py
│     │  │  config.py
│     │  └─ __init__.py
│     │
│     ├─tasks
│     │  │  __init__.py
│     │  │
│     │  └─abstract
│     │     │  task.py
│     │     │  transform.py
│     │     └─ __init__.py
│     │
│     └─utils
│        │  exception.py
│        └─ __init__.py
|
└─tests
    │  conftest.py
    │  test_version.py
    └─ __init__.py
```