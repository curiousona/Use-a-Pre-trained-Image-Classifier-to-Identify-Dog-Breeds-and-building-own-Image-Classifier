#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Kumari Sonali Singh
# DATE CREATED: 10/11/23                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# Define a list of available CNN model architectures
available_architectures = ['alexnet', 'vgg', 'resnet']

# TODO: 1a. EDIT parse.add_argument statements BELOW to add type & help for:
#          --arch - the CNN model architecture
#          --dogfile - text file of names of dog breeds
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    # Creates parser 
    parser = argparse.ArgumentParser("./pet_images, AlexNet, ./dognames.txt")

    # Creates 3 command line arguments args.dir for path to images files,
    # args.arch which CNN model to use for classification, args.labels path to
    # text file with names of dogs.
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='./pet_images')

    # TODO: 1a. EDIT parse.add_argument statements BELOW to add type & help for:
    #          --arch - the CNN model architecture
    #          --dogfile - text file of names of dog breeds
    parser.add_argument('--arch', type=str, default='vgg',
                        help='ALexNet {}'.format(available_architectures))
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='./dognames.txt')

    # TODO: 1b. Replace None with parser.parse_args() parsed argument 
    # collection that you created with this function 
    return parser.parse_args()

# Example usage:
# This block is just for testing purposes, it would not be included in your final code.
if __name__ == "__main__":
    # Call the function and print the parsed arguments
    args = get_input_args()
    print(args)
