import secrets
import string
pass_key_length = 32

# Generates a pass_key
def generate_pass_key():
    pass_key = ''
    alphabet = string.ascii_letters + string.digits

    # Generate pass_key_length number of random letters from the alphabet
    for i in range(pass_key_length):
        pass_key += ''.join(secrets.choice(alphabet))

    return pass_key

# Returns the javascript to store the pass_key in window session data
def pass_key_js(pass_key):
    return '<script>window.sessionStorage.setItem(\"avalon_pass\",\"' + pass_key + '\")</script>'

# Returns the javascript to retrieve information with pass_key stored in local windo session data
def retrieve_info_with_pass_key_js():
    with open('lib/pass_key_info.js', 'r') as f:
        return '<script>' + f.read() + '</script>'
