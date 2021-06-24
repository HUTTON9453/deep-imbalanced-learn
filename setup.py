from setuptools import setup


setup(
    name='deepimblearn',
    version='0.0.1',
    description='Deep Imbalanced Learning in Python',
    packages=[
        'deepimblearn',
        'deepimblearn.strategy',
        'deepimblearn.net',
        'deepimblearn.loss',
        'deepimblearn.dataset',
        'deepimblearn.utils',
    ],
    package_dir={
        'deepimblearn': 'deepimblearn',
        'deepimblearn.strategy': 'deepimblearn/strategy',
        'deepimblearn.net': 'deepimblearn/net',
        'deepimblearn.loss': 'deepimblearn/loss',
        'deepimblearn.dataset': 'deepimblearn/dataset',
        'deepimblearn.utils': 'deepimblearn/utils',
    },
)
