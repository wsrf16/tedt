from feature import ldapauth


def do():
    cfg_url = 'ldap://dc-01.qdingnet.cn:389'
    cfg_base = 'dc=qdingnet,dc=cn'
    cfg_username = 'itadmin'
    cfg_password = 'Aa123456789'
    ldap_config = ldapauth.LDAPConfig(cfg_url, cfg_base, cfg_username, cfg_password)

    conn = ldapauth.bind(ldap_config)
    base = ldap_config.base
    username = 'zhaoyu'
    password = 'Qd@2014'
    login_result = ldapauth.login(conn, username, password, base)