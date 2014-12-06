########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.05.December.2014
# v1.0
########################################################################
#
#
#
########################################################################
### Introduction
#
# Command and control module for the entire pyrprocessing system (eventually).
# This file will set up all the input/output directories and allow for input parameter editing (eventually).
#
########################################################################
#
#
#
####### imports
import os
import shutil
########################################################################
#
#
#
####### set the simulation directory
simulation_dir=raw_input('set the simulation directory:')
#######
#
####### set the home directory
home_dir='C:\\ftp\git\\pyroprocessing_discrete.event.simulation\\src\\command.and.control'
#######
#
#
#
########################################################################
#
# functions
#
########################################################################
#
#
#
####### make simulation directories for input, output 
def make_simulation_dir(subsystem,simulation_dir):
###
#
### current directory is /src/command.and.control
#
    input_dir='..\\..\\input\\'+subsystem+'\\'+simulation_dir 
    output_dir='..\\..\\output\\'+subsystem+'\\'+simulation_dir 
###
#
### make simulation directories
    os.makedirs(input_dir)
    os.makedirs(output_dir)
###
#
### make data and figure output directories
    os.chdir(output_dir)
    os.makedirs('data')
    os.makedirs('figures')
###
    return(input_dir,output_dir)
#######
#
#
#
####### copy files from default directory to simulation directory
def copy_input_files(subsystem,simulation_dir):
###
#
### move to default directory
    default_dir_change='..\\..\\input\\'+subsystem+'\\'+'default'
    os.chdir(default_dir_change)
    default_dir=os.getcwd()
###
#
### set destination directory
    destination_dir='..\\'+simulation_dir
###
#
    for files in os.listdir(default_dir):
	if files.endswith('.inp'): # default readme.md file not to be copied
	    shutil.copy(files,destination_dir)
# end for
#
###
    return()
#######
#
#
#
####### make read me file for the simulation
def make_readme(input_dir):
###
#
### move to simulation directory
    os.chdir(input_dir)
###
#
### open file
    readme_information=open('readme.md','w+')
###
#
### add statement
    readme_statement=raw_input('enter a readme statement for the simulation:')
###
#
### write to file
    readme_information.write(readme_statement)
#
### close file
    readme_information.close()
###
    return()
#######
#
#
#
####### write imput and output directories
def write_simulation_dir(input_dir,output_dir):
###
#
### move up a level
# this file needs to be stored outside of the simulation_dir so the module file knows where to look in the first place
    os.chdir('..\\')
###
#
### open file
    simulation_dir_file=open('simulation.dir.inp','w+')
###
#
### write directories
    simulation_dir_file.write(input_dir+'\n'+output_dir+'\\data'+'\n'+output_dir+'\\figures')
###
#
### close file
    simulation_dir_file.close()
###
#
###
    return()
########################################################################
#
#
#
########################################################################
#
# end functions
#
########################################################################
#
#
#
########################################################################
#
# fuel fabrication module
#
########################################################################
#
#
#
### set the file trees
input_dir,output_dir=make_simulation_dir('fuel.fabrication',simulation_dir)
###
#
### reset home directory
os.chdir(home_dir)
#
### copy default input files to new simulation directory
copy_input_files('fuel.fabrication',simulation_dir)
###
#
### reset home directory
os.chdir(home_dir)
###
#
### make readme file
make_readme(input_dir)
###
#
### write input and output directories
write_simulation_dir(input_dir,output_dir)
###
#
### make readme file
os.chdir(home_dir)
###
#
#
#
########################################################################
#
# end modules
#
########################################################################
#
#
#
########################################################################
#
# EOF
#
########################################################################