from headhunter import HeadHunter
from db import db
from models.headhunter import meta

meta.create_all(db)

if __name__ == '__main__':
    parser = HeadHunter(search_word="Python", is_max_size=False)
    parser.run()