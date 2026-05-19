#!/usr/bin/env python3
"""LinkedInt 自动冒烟测试（登录 + GraphQL 搜索 + 可选单页抓取）。"""
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

import configparser
import requests

import LinkedInt as LI

FAIL = 0
OK = 0


def check(name, cond, detail=''):
    global OK, FAIL
    if cond:
        OK += 1
        print('[PASS] %s' % name)
    else:
        FAIL += 1
        print('[FAIL] %s%s' % (name, (' — ' + detail) if detail else ''))


def main():
    print('=== LinkedInt 自动测试 ===\n')
    cfg = configparser.RawConfigParser()
    cfg.read(LI.CFG_PATH)
    raw = cfg.get('SESSION', 'cookie', fallback='')
    check('配置文件含 SESSION', bool(raw.strip()), 'path=%s' % LI.CFG_PATH)

    cookies = LI.login_from_config()
    check('读取 Cookie 会话', cookies is not None and cookies.get('li_at'))
    if not cookies:
        print('\n合计: %i 通过, %i 失败' % (OK, FAIL))
        sys.exit(1)

    ok, msg = LI._verify_session(cookies)
    check('Voyager /me 登录', ok, msg)
    print('       %s\n' % msg)

    js = cookies.get('JSESSIONID', 'ajax:0')
    headers = LI._voyager_headers(js)
    keywords = 'university of london'
    filters = LI._dash_search_filters()
    url = LI._dash_search_url(0, keywords, filters, count=10)
    r = requests.get(url, cookies=cookies, headers=headers, timeout=30)
    check('GraphQL HTTP 200', r.status_code == 200, 'status=%s' % r.status_code)
    content = LI._parse_json_or_exit(r, '自动测试 GraphQL')
    clusters = LI._dash_clusters_root(content)
    check('GraphQL 返回 clusters', clusters is not None)
    entities = list(LI._iter_dash_people_entities(content))
    check('解析到人员实体', len(entities) >= 1, 'count=%i' % len(entities))
    if entities:
        e = entities[0]
        name = LI._dash_text_field(e.get('title'))
        slug = LI._dash_public_id_from_entity(e)
        check('首条含姓名与 public_id', bool(name and slug), '%s / %s' % (name, slug))

    print('\n--- 端到端：单页抓取（--max-pages 1）---\n')
    rc = os.spawnlp(
        os.P_WAIT,
        sys.executable,
        sys.executable,
        os.path.join(BASE, 'LinkedInt.py'),
        '-y',
        '-u', keywords,
        '-o', '_autotest_london',
        '--email-domain', 'london.ac.uk',
        '--prefix', 'first.last',
        '--max-pages', '1',
        '--no-open-html',
    )
    check('LinkedInt.py 退出码 0', rc == 0, 'rc=%s' % rc)
    html_path = os.path.join(BASE, '_autotest_london.html')
    csv_path = os.path.join(BASE, '_autotest_london.csv')
    check('生成 HTML', os.path.isfile(html_path))
    check('生成 CSV', os.path.isfile(csv_path))
    if os.path.isfile(csv_path):
        with open(csv_path, 'r', encoding='utf-8', errors='replace') as f:
            lines = [ln for ln in f.readlines() if ln.strip()]
        check('CSV 含数据行', len(lines) > 1, 'lines=%i' % len(lines))

    print('\n=== 合计: %i 通过, %i 失败 ===' % (OK, FAIL))
    sys.exit(1 if FAIL else 0)


if __name__ == '__main__':
    main()
