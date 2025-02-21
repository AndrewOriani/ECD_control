from setuptools import setup, find_packages

setup(
    name='ECD_control',
    version='1.0',
    description='ECD control is a fast, echoed, gate-based approach to the quantum control of an oscillator with weak dispersive coupling to a qubit.',
    author='Alec Eickbusch',
    author_email='alec.eickbusch@yale.edu',
    url='https://github.com/alec-eickbusch/ECD_control/branches',
    packages=find_packages(),
    install_requires=[
        'qutip', 'tensorflow', 'h5py', 'tqdm', 'scikit-learn'
    ],
)