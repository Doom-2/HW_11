from flask import Flask, render_template
from utils import load_candidates, get_candidate_by_id, get_candidates_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    """Главная страничка."""
    candidates: list[dict] = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Страничка кандидата по ключу id."""

    candidate: dict = get_candidate_by_id(uid)
    if not candidate:
        return '<br><h3> Кандидат не найден </h3>'
    return render_template('card.html', candidate=candidate)


@app.route('/search/<part_name>')
def search_by_name(part_name):
    """Страничка кандидатов у которых в имени содержится подстрока part_name."""

    candidates: list[dict] = get_candidates_by_name(part_name.lower())
    return render_template('search.html', candidates=candidates, part_name=part_name)


@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    """Страничка кандидатов у которых есть один из навыков по ключу skills."""

    candidates: list[dict] = get_candidate_by_skill(skill_name.lower())
    return render_template('skill.html', candidates=candidates, skill_name=skill_name)


if __name__ == "__main__":
    app.run()
