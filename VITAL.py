from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # 주어진 데이터
    data = {
        'woo_fe_real': '승',
        'smleell': '승',
        'jooneim18': '패',
        'viva_mini7': '승',
        'huiya._.a': '승',
        'ikju.cha': '승',
        '073._.kt_': '승',
        'jeong_uk_26': '무',
        'jinhyo4112': '승',
        'sywon27': '승',
        '0_39694613': '승',
        '01h_m320': '승',
        'ishowjunu': '승',
        'c0ld._.water': '승',
        's_hyuni221': '승',
        'igangseon94': '승',
        '_yxn_9': '승',
        'jiho5696': '승',
        'c.s.hoon_05': '승',
        'seonujunyeong4': '승',
        'marilv4386': '패',
        'munchinbro': '승',
        'mickeymousy6': '승',
        'chemi_jin': '무',
        'k_seo_04': '승'
    }

    # 패인 사람들은 모두 당첨
    winners = [name for name, result in data.items() if result == '패']

    # 나머지에서 3명을 무작위로 선택하여 당첨자에 추가
    other_candidates = [name for name, result in data.items() if result != '패']
    winners.extend(random.sample(other_candidates, min(3, len(other_candidates))))
    
    # 당첨자를 무작위로 섞은 후 상위 5명을 추출하여 상금 순위를 부여
    random.shuffle(winners)
    top_5 = winners[:5]
    prize = ["1등", "2등", "3등", "4등", "5등"]

    # 결과를 튜플 리스트로 묶어서 반환
    result = list(zip(prize, top_5))    

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)