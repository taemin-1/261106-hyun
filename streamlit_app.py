from html import escape
from textwrap import dedent

import streamlit as st


st.set_page_config(page_title="자기소개 | 나의 정글 노트", page_icon="🌿", layout="wide")

PROFILE = {
        "name": "이름을 입력하세요",
        "affiliation": "소속을 입력하세요",
        "role": "관심 분야나 역할을 입력하세요",
        "introduction": "나를 잘 보여주는 소개 문장을 여기에 적어주세요.",
        "goal": "앞으로 이루고 싶은 목표를 적어주세요.",
}

INTERESTS = ["관심사 1", "관심사 2", "관심사 3", "관심사 4"]

BOOKS = [
        {
                "title": "읽은 책 제목",
                "author": "저자 이름",
                "note": "기억에 남은 생각이나 문장을 적어주세요.",
        },
        {
                "title": "읽은 책 제목",
                "author": "저자 이름",
                "note": "이 책을 읽고 느낀 점을 적어주세요.",
        },
        {
                "title": "읽은 책 제목",
                "author": "저자 이름",
                "note": "다른 사람에게 추천하고 싶은 이유를 적어주세요.",
        },
]

interests_html = "".join(
        f'<li><span class="interest-number">0{index}</span>{escape(interest)}</li>'
        for index, interest in enumerate(INTERESTS, start=1)
)

books_html = "".join(
        f"""
        <article class="book-row">
            <span class="book-number">{index:02}</span>
            <div class="book-title-group">
                <h3>{escape(book["title"])}</h3>
                <p>{escape(book["author"])}</p>
            </div>
            <p class="book-note">{escape(book["note"])}</p>
        </article>
        """
        for index, book in enumerate(BOOKS, start=1)
)

st.html(
    dedent("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Gowun+Batang:wght@400;700&family=Manrope:wght@400;500;600;700&display=swap');

        :root {
            --forest: #173c2b;
            --forest-deep: #10291f;
            --leaf: #d3ef75;
            --paper: #eeeedf;
            --ink: #20362a;
            --muted: #667366;
            --clay: #c97755;
        }

        .stApp { background: var(--paper); color: var(--ink); }
        header[data-testid="stHeader"], #MainMenu, footer { display: none; }
        .block-container { max-width: 1360px; padding: 18px 42px 72px; }
        .jungle-page { font-family: 'Manrope', 'Noto Sans KR', sans-serif; }
        .topbar {
            min-height: 68px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            border-bottom: 1px solid rgba(32, 54, 42, .2);
            color: var(--forest);
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 11px;
            color: inherit;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
        }
        .brand-mark {
            width: 23px;
            height: 23px;
            display: inline-block;
            background: var(--forest);
            position: relative;
        }
        .brand-mark::after {
            content: '';
            position: absolute;
            width: 8px;
            height: 13px;
            left: 8px;
            top: 5px;
            border-left: 1px solid var(--leaf);
            border-radius: 100% 0;
            transform: rotate(25deg);
        }
        .topnav { display: flex; align-items: center; gap: 27px; }
        .topnav a {
            color: var(--forest);
            font-size: 12px;
            text-decoration: none;
        }
        .topnav a:hover { color: var(--clay); }

        .hero {
            min-height: 510px;
            margin-top: 18px;
            display: flex;
            align-items: flex-end;
            position: relative;
            overflow: hidden;
            background: var(--forest-deep);
            color: #fffef2;
        }
        .hero-photo {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 54%;
        }
        .hero-shade {
            position: absolute;
            inset: 0;
            background: rgba(8, 29, 19, .56);
        }
        .hero-content {
            position: relative;
            z-index: 1;
            width: 100%;
            padding: 54px 58px 49px;
        }
        .eyebrow, .section-index {
            margin: 0;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }
        .hero .eyebrow { color: var(--leaf); }
        .hero h1 {
            max-width: 900px;
            margin: 21px 0 15px;
            font-family: 'Gowun Batang', serif;
            font-size: 64px;
            font-weight: 400;
            line-height: 1.22;
            overflow-wrap: anywhere;
        }
        .hero h1 span { color: var(--leaf); }
        .hero-meta { margin: 0; color: #f0f0df; font-size: 14px; }
        .hero-meta span { margin: 0 9px; color: var(--leaf); }
        .hero-caption {
            position: absolute;
            right: 28px;
            top: 28px;
            z-index: 1;
            color: #fffef2;
            font-size: 10px;
            writing-mode: vertical-rl;
        }

        .content-section { padding: 83px 0; border-bottom: 1px solid rgba(32, 54, 42, .2); }
        .section-index { color: var(--clay); }
        .section-heading {
            margin: 13px 0 35px;
            color: var(--forest);
            font-family: 'Gowun Batang', serif;
            font-size: 39px;
            font-weight: 400;
            line-height: 1.35;
        }
        .about-grid { display: grid; grid-template-columns: 1.1fr .9fr; gap: 64px; }
        .intro-copy {
            margin: 0;
            max-width: 620px;
            color: var(--forest);
            font-family: 'Gowun Batang', serif;
            font-size: 28px;
            line-height: 1.75;
            overflow-wrap: anywhere;
        }
        .profile-facts { border-left: 1px solid rgba(32, 54, 42, .25); padding-left: 32px; }
        .fact { padding: 0 0 18px; margin: 0 0 18px; border-bottom: 1px solid rgba(32, 54, 42, .16); }
        .fact:last-child { margin-bottom: 0; }
        .fact-label { display: block; margin-bottom: 6px; color: var(--muted); font-size: 11px; }
        .fact-value { color: var(--forest); font-size: 16px; font-weight: 600; overflow-wrap: anywhere; }

        .goal-section {
            margin: 0 -42px;
            padding: 62px 58px 67px;
            background: var(--forest);
            color: #fffef2;
        }
        .goal-section .section-index { color: var(--leaf); }
        .goal-section .section-heading { max-width: 800px; margin-bottom: 18px; color: #fffef2; }
        .goal-copy { max-width: 800px; margin: 0; color: #e4e9dc; font-size: 17px; line-height: 1.9; overflow-wrap: anywhere; }

        .interest-list { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); padding: 0; margin: 0; list-style: none; }
        .interest-list li {
            min-height: 92px;
            padding: 20px 16px 16px 0;
            border-top: 1px solid var(--forest);
            color: var(--forest);
            font-family: 'Gowun Batang', serif;
            font-size: 19px;
            overflow-wrap: anywhere;
        }
        .interest-number { display: block; margin-bottom: 13px; color: var(--clay); font: 700 10px 'Manrope', sans-serif; }
        .book-list { border-top: 1px solid var(--forest); }
        .book-row {
            display: grid;
            grid-template-columns: 54px 1fr 1.2fr;
            align-items: center;
            gap: 20px;
            padding: 24px 0;
            border-bottom: 1px solid rgba(32, 54, 42, .22);
        }
        .book-number { color: var(--clay); font-size: 12px; font-weight: 700; }
        .book-title-group h3 { margin: 0 0 5px; color: var(--forest); font: 400 21px 'Gowun Batang', serif; overflow-wrap: anywhere; }
        .book-title-group p, .book-note { margin: 0; color: var(--muted); font-size: 12px; line-height: 1.7; overflow-wrap: anywhere; }
        .book-note { justify-self: end; max-width: 440px; text-align: right; }
        .page-footer { display: flex; justify-content: space-between; gap: 18px; padding-top: 24px; color: var(--muted); font-size: 11px; }

        @media (max-width: 760px) {
            .block-container { padding: 8px 18px 44px; }
            .topbar { min-height: 58px; gap: 12px; }
            .brand { font-size: 10px; }
            .topnav { gap: 13px; }
            .topnav a { font-size: 10px; }
            .hero { min-height: 480px; margin-top: 12px; }
            .hero-content { padding: 36px 25px; }
            .hero h1 { font-size: 43px; }
            .hero-caption { right: 14px; top: 15px; }
            .content-section { padding: 58px 0; }
            .section-heading { font-size: 32px; }
            .about-grid { grid-template-columns: 1fr; gap: 32px; }
            .intro-copy { font-size: 23px; }
            .profile-facts { padding-left: 18px; }
            .goal-section { margin: 0 -18px; padding: 48px 25px 52px; }
            .goal-copy { font-size: 15px; }
            .interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 18px; }
            .interest-list li { font-size: 17px; }
            .book-row { grid-template-columns: 34px 1fr; gap: 12px; }
            .book-note { grid-column: 2; justify-self: start; text-align: left; }
            .page-footer { flex-direction: column; }
        }
        @media (max-width: 390px) {
            .topnav { gap: 9px; }
            .topnav a { font-size: 9px; }
            .hero h1 { font-size: 36px; }
            .hero-meta { font-size: 12px; }
        }
        </style>
        """),
)

st.html(
    dedent(f"""
        <div class="jungle-page" id="top">
            <nav class="topbar" aria-label="페이지 메뉴">
                <a class="brand" href="#top"><span class="brand-mark"></span>MY FIELD NOTES</a>
                <div class="topnav">
                    <a href="#profile">소개</a>
                    <a href="#goal">목표</a>
                    <a href="#interests">관심사</a>
                    <a href="#books">읽은 책</a>
                </div>
            </nav>

            <section class="hero" aria-label="자기소개">
                <img class="hero-photo" src="https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=2200&q=85" alt="초록빛 나무가 우거진 숲길">
                <div class="hero-shade"></div>
                <span class="hero-caption">A LITTLE CLOSER TO THE WILD</span>
                <div class="hero-content">
                    <p class="eyebrow">PERSONAL FIELD GUIDE &nbsp; / &nbsp; 01</p>
                    <h1>안녕하세요,<br><span>{escape(PROFILE["name"])}</span>입니다.</h1>
                    <p class="hero-meta">{escape(PROFILE["affiliation"])}<span>·</span>{escape(PROFILE["role"])}</p>
                </div>
            </section>

            <section class="content-section" id="profile">
                <p class="section-index">01 &nbsp; / &nbsp; ABOUT ME</p>
                <h2 class="section-heading">나를 소개합니다</h2>
                <div class="about-grid">
                    <p class="intro-copy">“{escape(PROFILE["introduction"])}”</p>
                    <div class="profile-facts">
                        <p class="fact"><span class="fact-label">이름</span><span class="fact-value">{escape(PROFILE["name"])}</span></p>
                        <p class="fact"><span class="fact-label">소속</span><span class="fact-value">{escape(PROFILE["affiliation"])}</span></p>
                        <p class="fact"><span class="fact-label">관심 분야 / 역할</span><span class="fact-value">{escape(PROFILE["role"])}</span></p>
                    </div>
                </div>
            </section>

            <section class="goal-section" id="goal">
                <p class="section-index">02 &nbsp; / &nbsp; MY NORTH STAR</p>
                <h2 class="section-heading">지향하는 곳</h2>
                <p class="goal-copy">{escape(PROFILE["goal"])}</p>
            </section>

            <section class="content-section" id="interests">
                <p class="section-index">03 &nbsp; / &nbsp; CURIOSITY</p>
                <h2 class="section-heading">요즘 마음이 향하는 것</h2>
                <ul class="interest-list">{interests_html}</ul>
            </section>

            <section class="content-section" id="books">
                <p class="section-index">04 &nbsp; / &nbsp; READING LOG</p>
                <h2 class="section-heading">내가 읽은 책</h2>
                <div class="book-list">{books_html}</div>
            </section>

            <footer class="page-footer">
                <span>조금씩 배우고, 나답게 자라는 중.</span>
                <span>MY FIELD NOTES &nbsp; · &nbsp; 2026</span>
            </footer>
        </div>
        """),
)
