from django.shortcuts import render
import random

# Create your views here.
def start_lotto(request):
    return render(request, 'lotto.html')

def result_lotto(request):
    # 로또 번호 생성기
    result_lotto = []

    # 게임 수 가져오기
    num_of_game = int(request.GET.get('num_of_game'))

    # 게임 수 만큼 생성
    for _ in range(num_of_game):
        lotto = []
        # 6개의 숫자 생성
        # 중복 방지
        while len(lotto) < 6:
            lotto.append(random.randint(1, 45))
            lotto = list(set(lotto))
        
        result_lotto.append(sorted(lotto))

    # 정렬 및 응답
    return render(request, 'lotto_result.html', {'num_of_game':num_of_game,'result':result_lotto})