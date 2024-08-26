#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kumari Sonali Singh
# DATE CREATED: 10/11/2023                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# Define get_pet_labels function with hardcoded image directory
def get_pet_labels():
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    
    Returns:
    results_dic - Dictionary with 'key' as image filename and 'value' as a 
                  List. The list contains for following item:
                  index 0 = pet image label (string)
    """
    # Hardcoded path to the "pet_images" directory
    image_dir = "pet_images"

    # creates an empty dictionary of the pet labels
    results_dic = {}

    # Retrieve the filenames of the pets from the specified directory
    filenames = listdir(image_dir)
    
    # Process each of the files to create a dictionary where the key is
    # the filename and the value is the pet label (formatted correctly)
    for idx in range(len(filenames)):
        # Skips file if starts with . (like .MArk pet store) because
        # this is not a pet name
        if filenames[idx][0] != ".":
            # Creates temporary label variable to hold pet label name extracted   
            pet_label = ""
            
            # Splits filename by _ to break into words
            pet_image = filenames[idx].split("_")
            
            # Loops to check if the word in pet name is only
            # alphabetic characters - also usually the image
            # extension
            for word in pet_image:
                if word.isalpha():
                    pet_label += word.lower() + " "
                    
            # Strips off trailing whitespaces
            pet_label = pet_label.strip()
                    
            # Adds pet label to dictionary using filename as key
            if filenames[idx] not in results_dic:
                results_dic[filenames[idx]] = [pet_label]
            else:
                print("** warning: Duplicate files exist in directory:", filenames[idx])

    # returns dictionary of labels
    return results_dic

# Call the function and print the results
print(get_pet_labels())
