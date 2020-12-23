from django import template


register = template.Library()

def parse_int(value):
    alphabet = "abcdef"
    final_list = []
    for i in range(value):
        final_list.append(alphabet[i])
    return final_list

register.filter('parse_int', parse_int)