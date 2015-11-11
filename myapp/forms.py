from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _


class UserChangeFormNoPassword(UserChangeForm):
    password = ReadOnlyPasswordHashField(label=_("Password"))
