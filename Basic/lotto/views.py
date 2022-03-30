from django.shortcuts import render
import random

# Create your views here.
def create_lotto(request):
    # 로또 번호 생성기
    result_lotto = []

    # 6개의 숫자 생성
    # 중복 방지
    while len(result_lotto) < 6:
        result_lotto.append(random.randint(1, 45))
        result_lotto = list(set(result_lotto))

    # 정렬 및 응답
    return render(request, 'lotto.html', {'result':sorted(result_lotto)})