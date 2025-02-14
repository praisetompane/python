# Python

**objective**: an in-depth study of Python, its implementation and ecosystem.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Language details: 
  - [language reference](https://docs.python.org/3.11/reference/index.html#reference*index)
  - [base modules index](https://docs.python.org/3/py-modindex.html)
  - [standard library reference](https://docs.python.org/3.11/library/index.html)
  - package management:
    - [packaging](https://packaging.python.org/en/latest/)
    - tools:
      - [pip](https://pypi.org/project/pip/)
      - [pipenv](https://pipenv.pypa.io/en/latest/)
      - [editors](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)
      - [performance benchmark](https://github.com/psf/pyperf)
    - structuring projects:
      - [python-packaging](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure%3E)
      - [src layout](https://stackoverflow.com/questions/50155464/using-pytest-with-a-src-layer)
  - [package index](https://pypi.org)
  - [extending and embedding](https://docs.python.org/3.11/extending/index.html)
  - [developer contribution guide](https://devguide.python.org/)
  - [compiler/interpreter](https://github.com/python/cpython)
  - memory model:
    - [computational complexity cost model](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/readings/python-cost-model/)
  - history:
    - [The Story of Python, by Its Creator, Guido van Rossum](https://www.youtube.com/watch?v=J0Aq44Pze-w)

## Testing:
  - [pytest](https://docs.pytest.org/en/latest/explanation/pythonpath.html#pytest-vs-python-m-pytest):
    - [goodpractices](https://docs.pytest.org/en/latest/explanation/goodpractices.html#which-import-mode)

## Use Cases:
  - [Applications for Python](https://www.python.org/about/apps/)
  - Large Implementations:
        - https://github.com/praisetompane/posthog
  - Database Integration:
      - SQLAlchemy
      - alembic
          - op reference: https://alembic.sqlalchemy.org/en/latest/ops.html#ops
          - mako templates: https://www.makotemplates.org
          - commands:
              - create a migration: alembic revision -m "create account table"
              - run migrations forward: 
                - update database to latest: alembic upgrade head
                - update database by 1 script: alembic upgrade head +1
                - alembic upgrade head --sql
              - run migrations backwards: 
                - rollback database to start state: alembic downgrade base
                - rollback database ny 1 script: alembic downgrade -1
              - get history: alembic history
                  extra flag: --verbose
              - alembic current
              - alembic heads
              - alembic branches
              - view slices of history:
                  - alembic history -r[start]:[end]
                      where [start]:[end] can be revisions, numbers
                      - example:
                          - alembic history -r1975ea:ae1027
                          - alembic history -r-3:current
                  - alembic history --rev-range=-3:current
              - view applied migrations: SELECT * FROM public.alembic_version;
      - Flask-SQLAlchemy: https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/
      - Flask-Migrate: https://flask-migrate.readthedocs.io/en/latest/
      - https://medium.com/@johnid0ouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a
      - pure SQL:
          - http://allan-simon.github.io/blog/posts/alembic-use-sql-statement-instead-of-sqlalchemy/
          - https://stackoverflow.com/questions/23206562/sqlalchemy-executing-raw-sql-with-parameter-bindings
      - handling large migrations/revisions: https://alembic.sqlalchemy.org/en/latest/cookbook.html#building-uptodate

    - Web Development:
        - frameworks:
          - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
            - https://flask.palletsprojects.com/en/stable/deploying/
            - https://developers.redhat.com/articles/2023/08/17/how-deploy-flask-application-python-gunicorn#the_application
          - [FastAPI]()
          - [Django]()
          - Flask vs FastAPI vs Django REST:
             - https://python.land/create-a-python-rest-api#google_vignette
             - https://www.turing.com/kb/fastapi-vs-flask-a-detailed-comparison

        - [WSGI](https://wsgi.readthedocs.io/en/latest/index.html)
          - gunicorn
        - [ASGI](https://asgi.readthedocs.io/en/latest/)
  - Data Science:
      - courses:
          - MITx: Introduction to Computational Thinking and Data Science: https://www.edx.org/learn/computer-science/massachusetts-institute-of-technology-introduction-to-computational-thinking-and-data-science
  
  - Machine Learning:
      - https://github.com/praisetompane/computation_and_information/tree/main/6_computing_methodologies/artificial_intelligence
      - numpy: https://github.com/numpy/numpy
      - courses:
          - MITx: Machine Learning with Python: from Linear Models to Deep Learning: https://www.edx.org/learn/machine-learning/massachusetts-institute-of-technology-machine-learning-with-python-from-linear-models-to-deep-learning?utm_source=mitopenlearning-mit-open-learning&utm_medium=affiliate_partner
          - HarvardX: CS50's Introduction to Artificial Intelligence with Python: https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python?utm_source=lms_catalog_service_user&utm_medium=affiliate_partner&_gl=1*hmq9pu*_gcl_au*MTgxMTI5NzM0NC4xNzM2MzA2MDEz*_ga*MTYyMjc3MDcxMy4xNzM2MzA2MDAy*_ga_D3KS4KMDT0*MTczNjMwNjAwMS4xLjEuMTczNjMwNjQ0OS40NS4wLjA.

## Learning Resources:
  - [roadmap](https://roadmap.sh/python)
  - [practice problems](ttps://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=python)
  - HarvardX: CS50's Web Programming with Python and JavaScript: https://www.edx.org/learn/web-development/harvard-university-cs50-s-web-programming-with-python-and-javascript?utm_source=lms_catalog_service_user&utm_medium=affiliate_partner&_gl=1*hmq9pu*_gcl_au*MTgxMTI5NzM0NC4xNzM2MzA2MDEz*_ga*MTYyMjc3MDcxMy4xNzM2MzA2MDAy*_ga_D3KS4KMDT0*MTczNjMwNjAwMS4xLjEuMTczNjMwNjQ0OS40NS4wLjA.
  - [How to Think Like a Computer Scientist: Interactive Edition](https://runestone.academy/ns/books/published/thinkcspy/index.html)
  - Dr. Ana Bell.Prof. Eric Grimson. Prof. John Guttag. 2016. Introduction To Computer Science And Programming In Python
  - MITx: Introduction to Computer Science and Programming Using Python: https://www.edx.org/learn/computer-science/massachusetts-institute-of-technology-introduction-to-computer-science-and-programming-using-python?utm_source=mitopenlearning-mit-open-learning&utm_medium=affiliate_partner
  - HarvardX: CS50'S Introduction To Programming With Python: https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python?utm_source=lms_catalog_service_user&utm_medium=affiliate_partner&_gl=1*gei9xp*_gcl_au*MTgxMTI5NzM0NC4xNzM2MzA2MDEz*_ga*MTYyMjc3MDcxMy4xNzM2MzA2MDAy*_ga_D3KS4KMDT0*MTczNjMwNjAwMS4xLjEuMTczNjMwNjQ4Ny43LjAuMA.

# References:
  - Johni Douglas Marangon. Using migrations in Python — SQLAlchemy with Alembic + Docker solution. https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a

**Disclaimer**: This is an ongoing and incomplete project to unpack these concepts and serve as my distributed memory.
