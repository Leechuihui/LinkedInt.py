#!/usr/bin/env python3
"""从本机 Chrome 同步 LinkedIn Cookie 与账户信息到 LinkedInt.cfg。"""
import configparser
import json
import os
import sys

try:
    import browser_cookie3
    import requests
except ImportError:
    sys.exit('请先安装: python3.12 -m pip install browser-cookie3 requests')

BASE = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep
CFG = BASE + 'LinkedInt.cfg'

NAMES = ('li_at', 'JSESSIONID', 'bcookie', 'bscookie', 'lang', 'liap', 'lidc', 'li_rm')


def _parse_cookies(raw):
    out = {}
    for part in raw.split(';'):
        part = part.strip()
        if '=' not in part:
            continue
        k, v = part.split('=', 1)
        k, v = k.strip(), v.strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        out[k] = v
    return out


def _fetch_profile(cookies):
    js = cookies.get('JSESSIONID', 'ajax:0')
    headers = {
        'Csrf-Token': js,
        'X-RestLi-Protocol-Version': '2.0.0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'Referer': 'https://www.linkedin.com/feed/',
    }
    r = requests.get(
        'https://www.linkedin.com/voyager/api/me',
        cookies=cookies,
        headers=headers,
        timeout=25,
    )
    data = json.loads(r.text)
    for item in data.get('included') or []:
        if isinstance(item, dict) and item.get('firstName'):
            pid = item.get('publicIdentifier', '')
            return {
                'name': '%s %s' % (item.get('firstName', ''), item.get('lastName', '')).strip(),
                'public_id': pid,
                'profile_url': 'https://www.linkedin.com/in/%s' % pid if pid else '',
            }
    return {}


def main():
    cj = browser_cookie3.chrome(domain_name='linkedin.com')
    wanted = {c.name: c.value for c in cj if c.name in NAMES}
    if not wanted.get('li_at'):
        sys.exit('[!] Chrome 中未找到 linkedin.com 的 li_at，请先在 Chrome 登录 LinkedIn')

    cookie_str = '; '.join('%s=%s' % (k, v) for k, v in wanted.items())
    config = configparser.RawConfigParser()
    config.read(CFG)

    hunter = config.get('API_KEYS', 'hunter').strip() if config.has_section('API_KEYS') else ''
    email = ''
    password = ''
    if config.has_section('ACCOUNT'):
        email = config.get('ACCOUNT', 'email', fallback='').strip()
        password = config.get('ACCOUNT', 'password', fallback='').strip()
    if not email and config.has_section('CREDS'):
        email = config.get('CREDS', 'linkedin_username', fallback='').strip()
        password = config.get('CREDS', 'linkedin_password', fallback='').strip()

    email_domain = config.get('DEFAULTS', 'email_domain', fallback='').strip() if config.has_section('DEFAULTS') else ''
    email_prefix = config.get('DEFAULTS', 'email_prefix', fallback='auto').strip() if config.has_section('DEFAULTS') else 'auto'
    filter_company = config.get('DEFAULTS', 'filter_company', fallback='n').strip() if config.has_section('DEFAULTS') else 'n'
    company_id = config.get('DEFAULTS', 'company_id', fallback='').strip() if config.has_section('DEFAULTS') else ''
    open_html = config.get('DEFAULTS', 'open_html', fallback='n').strip() if config.has_section('DEFAULTS') else 'n'

    profile = _fetch_profile(_parse_cookies(cookie_str))
    name = profile.get('name', '')
    public_id = profile.get('public_id', '')
    profile_url = profile.get('profile_url', '')

    lines = [
        '[API_KEYS]',
        '# Hunter.io：邮箱前缀选 auto 时使用。在 https://hunter.io/api-keys 获取',
        'hunter = %s' % hunter,
        '',
        '[ACCOUNT]',
        '# LinkedIn 登录账户（密码仅本地保存，脚本实际用 [SESSION] Cookie 登录）',
        'email = %s' % email,
        'password = %s' % password,
        'name = %s' % name,
        'public_id = %s' % public_id,
        'profile_url = %s' % profile_url,
        '',
        '[CREDS]',
        '# 与 [ACCOUNT] 保持一致，兼容旧版字段名',
        'linkedin_username = %s' % email,
        'linkedin_password = %s' % password,
        '',
        '[DEFAULTS]',
        'email_domain = %s' % email_domain,
        'email_prefix = %s' % email_prefix,
        'filter_company = %s' % filter_company,
        'company_id = %s' % company_id,
        'open_html = %s' % open_html,
        '',
        '[SESSION]',
        '# LinkedIn 会话。过期后重新执行本脚本',
        'cookie = %s' % cookie_str,
        'li_at = %s' % wanted['li_at'],
        '',
    ]
    with open(CFG, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print('[+] 已写入 %s' % CFG)
    print('    账户: %s (%s)' % (name or '—', email or '—'))


if __name__ == '__main__':
    main()
