from django import template
register = template.Library()

@register.simple_tag(takes_context=False)
def set_page_title(current_path):
    match current_path:
        case "/user/register/":
            return "Nest | Register"
        case "/user/login/":
            return "Nest | Login"
        case _:
            return "Nest | Multivendor Ecommerce"