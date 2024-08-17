#!/usr/bin/env python3
# Author Gaurav
# date 2024-6-27
from pathlib import Path
import pandas as pd
from shiny import reactive
from shiny.express import render, ui
from htmltools import HTML, div
import subprocess

app_ui = ui.page_fixed(
    ui.h1("Sequencing service pacbiohifi read summarizer")
    ui.h2("a single page application summary post pacbio hifi sequencing runs"),
        ui.markdown(" use the pacbiohifisequencing reads files and generate a single page deploayable summary"),
        ui.markdown("Developed by Gaurav Sablok")
        ui.output_image("image")
        ui.markdown("Sequencing sample done by ----------")
        ui.output_table("realengthbeforecutoff"),
        ui.output_table("readlengthaftercutoff")
        ui.output_dataframe("readdataframebeforecutoff")
        ui.output_dataframe("readdataframeaftercutoff")
        ui.output_plot("readplot")
        ui.output_text("writefasta")
        ui.output_text("parsebam")
        ui.output_text("PacBiohifi")
)
def server(input, output, session):
    @output
    @render.text
    def PacBiohifi():
        div(HTML("<iframe src =  https://pacbiohifi.streamlit.app/ > PacbioHifi Streamlit </iframe>"))
   
    @output
    @render.image
    def image():
           img: ImgData = {"src": "https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", "width": "100px"}
        return img
   
    @output
    @render.dataframe
    def readdataframebeforecutoff():
        infile = Path(__file__).parent / "reads.fastq"
        fastqreads = {}
        with open(infile) as fastqfile:
        fastqread = fastqfile.readlines()
        for line in range(len(fastqread)):
            if fastqread[line].startswith("@"):
                fastqreads[fastqread[line].strip().split()[0]] = fastqread[line+1]
        fastqheaders = list(fastqreads.keys())
        fastqsequences = list(fastqreads.values())
        fastqlength = list(map(len,list(fastqreads.values())))
        dataframe = pd.concat([pd.DataFrame([fastqheaders], columns = ["headers"]), pd.DataFrame([fastqsequences], columns = ["sequence"]), pd.DataFrame([fastqlength], columns = ["length"])], axis =1)
        return dataframe

    @output
    @render.dataframe
    def readdataframeaftercutoff():
        infile = Path(__file__).parent / "reads.fastq"
        fastqreads = {}
        with open(infile) as fastqfile:
        fastqread = fastqfile.readlines()
        for line in range(len(fastqread)):
            if fastqread[line].startswith("@"):
                fastqreads[fastqread[line].strip().split()[0]] = fastqread[line+1]
        fastqheaders = list(fastqreads.keys())
        fastqsequences = list(fastqreads.values())
        fastqlength = list(map(len,list(fastqreads.values())))
        lenghtcutoff = int(lengthcut)
        afterlengthcut = {}
        for i in range(len(fastaheaders)):
            if fastqlength[i] >= lengthcutoff:
                afterlengthcut[fastqheaders[i]] = [fastqsequences[i], fastqlength[i]]
        afterlengthdatakeys = list(afterlengthcut.keys())
        afterlengthdataseq = [i[0] for i in list(afterlengthcut.values())]
        afterlengthdatalen = [i[1] for i in list(afterlengthcut.values())]
        dataframe = pd.concat([pd.DataFrame([afterlengthdatakeys], columns = ["headers"]), pd.DataFrame([afterlengthdataseq], columns = ["sequence"]), pd.DataFrame([afterlengthdatalen], columns = ["length"])], axis =1)
        return dataframe

    @output
    @render.table
    def readlengthaftercutoff():
        infile = Path(__file__).parent / "reads.fastq"
        fastqreads = {}
        with open(infile) as fastqfile:
        fastqread = fastqfile.readlines()
        for line in range(len(fastqread)):
            if fastqread[line].startswith("@"):
                fastqreads[fastqread[line].strip().split()[0]] = fastqread[line+1]
        fastqheaders = list(fastqreads.keys())
        fastqsequences = list(fastqreads.values())
        fastqlength = list(map(len,list(fastqreads.values())))
        dataframeheaderslength = pd.concat([pd.DataFrame([fastqheaders], columns = ["headers"]), pd.DataFrame([fastqsequences], columns = ["sequence"]), pd.DataFrame([fastqlength], columns = ["length"])], axis =1)
        return dataframe[["fastqheaders", "fastalength"]]

    @output
    @render.table
    def realengthbeforecutoff():
        infile = Path(__file__).parent / "reads.fastq"
        fastqreads = {}
        with open(infile) as fastqfile:
        fastqread = fastqfile.readlines()
        for line in range(len(fastqread)):
            if fastqread[line].startswith("@"):
                fastqreads[fastqread[line].strip().split()[0]] = fastqread[line+1]
        fastqheaders = list(fastqreads.keys())
        fastqsequences = list(fastqreads.values())
        fastqlength = list(map(len,list(fastqreads.values())))
        lenghtcutoff = int(lengthcut)
        afterlengthcut = {}
        for i in range(len(fastaheaders)):
            if fastqlength[i] >= lengthcutoff:
                afterlengthcut[fastqheaders[i]] = [fastqsequences[i], fastqlength[i]]
        afterlengthdatakeys = list(afterlengthcut.keys())
        afterlengthdataseq = [i[0] for i in list(afterlengthcut.values())]
        afterlengthdatalen = [i[1] for i in list(afterlengthcut.values())]
        dataframe = pd.concat([pd.DataFrame([afterlengthdatakeys], columns = ["headers"]), pd.DataFrame([afterlengthdataseq], columns = ["sequence"]), pd.DataFrame([afterlengthdatalen], columns = ["length"])], axis =1)
        return dataframe[["headers", "length"]]

    @output
    @render.plot
    def readplot():
        infile = Path(__file__).parent / "reads.fastq"
        fastqreads = {}
        with open(infile) as fastqfile:
        fastqread = fastqfile.readlines()
        for line in range(len(fastqread)):
            if fastqread[line].startswith("@"):
                fastqreads[fastqread[line].strip().split()[0]] = fastqread[line+1]
        fastqheaders = list(fastqreads.keys())
        fastqsequences = list(fastqreads.values())
        fastqlength = list(map(len,list(fastqreads.values())))
        dataframeheaderslength = pd.concat([pd.DataFrame([fastqheaders], columns = ["headers"]), pd.DataFrame([fastqsequences], columns = ["sequence"]), pd.DataFrame([fastqlength], columns = ["length"])], axis =1)
        lenghtcutoff = int(lengthcut)
        afterlengthcut = {}
        for i in range(len(fastaheaders)):
            if fastqlength[i] >= lengthcutoff:
                afterlengthcut[fastqheaders[i]] = [fastqsequences[i], fastqlength[i]]
        afterlengthdatakeys = list(afterlengthcut.keys())
        afterlengthdataseq = [i[0] for i in list(afterlengthcut.values())]
        afterlengthdatalen = [i[1] for i in list(afterlengthcut.values())]
        afterdataframe = pd.concat([pd.DataFrame([afterlengthdatakeys], columns = ["headers"]), pd.DataFrame([afterlengthdataseq], columns = ["sequence"]), pd.DataFrame([afterlengthdatalen], columns = ["length"])], axis =1)
        return dataframeheaderslength.length.plot.bar(), afterdataframe.length.plot.bar()
        
    @output
    @render.text
    def writefasta():
        infile = Path(__file__).parent / "reads.fastq"
        fastqreads = {}
        with open(infile) as fastqfile:
        fastqread = fastqfile.readlines()
        for line in range(len(fastqread)):
            if fastqread[line].startswith("@"):
                fastqreads[fastqread[line].strip().split()[0]] = fastqread[line+1]
        fastqheaders = list(fastqreads.keys())
        fastqsequences = list(fastqreads.values())
        outfile = Path(__file__).parent / "sequencingreads.fasta"
        with open(outfile, "w") as filetowrite:
            for i in range(len(fastqheaders)):
                outfile.write(f">{fastaqheaders[i]}\n{fastasequences[i]}")
            filetowrite.close()
            
     @output
     @render.parsebam
     infile = Path(__file__).parent / "reads.bam"
     infilepbi = Path(__file__).parent / "reads.pbi"
     oufile = Path(__file__).parent / "reads.fastq"
     if infile and not infilepbi:
         print(f"the pbi file are required for the read conversion")
         return
     if infile and infilepbi:
         subprocess.run(["bam2fastq", infile, "-o", "reads.fastq"]
                    
app = App(app_ui, server)
