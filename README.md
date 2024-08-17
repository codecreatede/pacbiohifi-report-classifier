# pacbiohifi-seq-app

- a single page shiny express pacbiohifi-seq-app for profiling of the pacbiohifi sequencing reads sequencing facility or startups.
- shiny API reference is located at [python API](https://shiny.posit.co/py/api/) and also here [express API](https://shiny.posit.co/py/docs/express-in-depth.html)
- You can also host on tapyr template [template](https://github.com/Appsilon/tapyr-template)
- parameters to set: fastq file path, readfiltercutoff, provide the name and the address of the sequencing facility, provide the name and the person responsible for sequencing.
- installation dependencies
```
# First install htmltools, then shiny
pip install https://github.com/posit-dev/py-htmltools/tarball/main
pip install https://github.com/posit-dev/py-shiny/tarball/main
pip install shiny
pip install shinywidgets
pip install shinylive
pip install shinyswatch
```
- to use and build a dashboard will be build for the complete analysis including the name of the sequencing facility or center and the person
```
git clone https://github.com/gauravcodepro/pacbiohifi-seq-app.git
cd pacbiohifi-seq-app
# put the fastq reads files there. provide the parameters and run as 
shiny run pacbiohifi-seq-app.py app.py --reload
```
- **To do today: bin according to the struger rule, bug check**

Gaurav Sablok

