from load_scores import load_scores
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_빈_줄은_건너뛴다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

import pytest
def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError): # 예상한 에러가 일어나면 테스트 통과함.
        load_scores("없는파일.csv")

def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []

@pytest.mark.parametrize("점수, 유효한가", [
    (-1,  False),   # 경계 바로 아래
    (0,   True),    # ★ 아래쪽 경계
    (1,   True),
    (99,  True),
    (100, True),    # ★ 위쪽 경계
    (101, False),   # 경계 바로 위
])
def test_점수_경계값(점수, 유효한가):
    with open("임시.csv", "w", encoding="utf-8") as f:
        f.write(f"name,score\n학생,{점수}\n")
    kept, skipped = load_scores("임시.csv")
    assert (len(kept) == 1) == 유효한가
