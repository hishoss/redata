from setuptools import find_packages, setup

setup(
    version="0.0.5",
    author="redata-team",
    description="Monitoring system for data teams",
    name="redata",
    install_requires=[
        "apache-airflow",
        "psycopg2-binary",
        "grafana-api",
        "cattrs==1.0.0",
        "marshmallow-sqlalchemy==0.23.1",
        "marshmallow<3.0.0,>=2.18.0",
        "pyexasol",
        "pymysql",
        "cryptography",
        "pybigquery<0.6.0",
        "alembic",
        "scipy",
        "flask",
        "flask_admin",
        "Flask-Login",
        "waitress",
        "sqlalchemy-redshift",
        "snowflake-sqlalchemy",
        "pymssql",
    ],
    extras_require={"dev": ["isort", "black", "pre-commit"]},
    entry_points={
        "console_scripts": ["redata=redata.command_line:main"],
    },
    packages=find_packages(),
)
