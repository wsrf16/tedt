import ldap


class LDAPConfig(object):
    """
    LDAP配置信息（AD域）
    """
    def __init__(self, url, base, username, password):
        self.url = url
        self.base = base
        self.username = username
        self.password = password


def get_full_cn(cn, base):
    full = 'cn={0},ou=服务用户,{1}'.format(cn, base)
    return full


def get_full_ou(ou, base):
    full = 'ou={0},{1}'.format(ou, base)
    return full


def get_filter_by_sam_account_name(sam_account_name):
    filter = 'sAMAccountName={0}'.format(sam_account_name)
    return filter


def bind(ldap_config):
    url = ldap_config.url
    base = ldap_config.base
    username = ldap_config.username
    password = ldap_config.password
    conn = ldap.initialize(url)
    fullcn = get_full_cn(username, base)
    conn.simple_bind_s(fullcn, password)
    return conn


def login(conn, username, password, base):
    fullou = get_full_ou('千丁互联', base)
    scope = ldap.SCOPE_SUBTREE
    sam_filter = get_filter_by_sam_account_name(username)

    result = conn.search_s(fullou, scope, sam_filter, None)
    print(result)
    user_dict = result[0][1]
    cn = str(user_dict['cn'][0], 'utf8')
    dn = result[0][0]
    account = {'cn': cn, 'dn': dn, 'pwd' : password}

    b_result = conn.simple_bind_s(account['dn'], password)
    return b_result