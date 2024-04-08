from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import User  직접 참조 안하고....
# 장고한테 너 지금 인증할 때 쓰는 User 클래스 내놔(get_user_model 함수 사용)....

# Accounts 관련 Form은 이미 다 만들어져 있는데...
# auth.User 기준으로 만들어져 있어서
# accounts.User를 사용해야 하니까....그냥은 사용못하고
class CustomUserCreationForm(UserCreationForm):
    # auth.User 사용하는 걸 accounts.User 사용하도록 변경
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    # auth.User 사용하는 걸 accounts.User 사용하도록 변경
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        #사용자가 직접 변경할 수 있는 fields만 보여주기
        fields = ('first_name','last_name','email')
        