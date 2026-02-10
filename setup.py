from setuptools import setup,find_packages
setup(name="nullsec-payload-authflood",version="2.0.0",author="bad-antics",description="WiFi authentication flood detection and defense",packages=find_packages(where="src"),package_dir={"":"src"},python_requires=">=3.8")
