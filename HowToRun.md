Replit官方使用的是Poetry做环境管理，我们可以通过下面的方式自己管理venv:

1. python -m venv .venv
2. source .venv/bin/activate
3. python -m pip install --upgrade pip setuptools wheel
ERROR: Can not perform a '--user' install. User site-packages are not visible in this virtualenv.
5. printf "[install]\nuser = false\n" > "$VIRTUAL_ENV/pip.conf"
6. python -m pip install --upgrade pip setuptools wheel
7. 或者python -m pip install --upgrade pip setuptools wheel --no-user
8. which python && which pip
/home/runner/workspace/.venv/bin/python
/home/runner/workspace/.venv/bin/pip
9. 安装依赖：pip install agno duckduckgo-search yfinance openai matplotlib pandas
10. 或者 pip install -r requirements.txt
11. python -m agno_practices.04-multi-agent-team，而不是python agno_practices/04-multi-agent-team.py：
> replit中的包管理：https://chatgpt.com/share/6852517f-5cac-8001-be53-d056c199e894
> https://chatgpt.com/c/68524a1a-3dc0-8001-8a37-593925d78172



