# Foondamate_task

This is the solution for a data engineering role [task](https://careers.foondamate.com/data-engineer-remote/foondamate-software-engineer-coding-challenge-001) at Foondamate. This allows a company visualize the growth of their users from the Command line.

## Repository Structure
* main.py: This python script fetches the data and plots the desires graph.
* images: This contains the image of the graph gotten after running the script.

## Steps to tun the script
1. Clone this repository into your local computer.
2. Open your desired terminal and navigate to the directory holding the main.py and requirements.txt files.
3. Create a virtual environment using :
    * virtualenv foonda   (N.B "foonda" is the name of the virtual environment. You can use your desired name)
4. Activate the virtual environment using :
    * .\foonda\Scripts\activate
5. Run " pip install -r requirements.txt " to get the necessary package(s)
6. To plot the graph, use the following command:
    * python main.py 01-01-2022 11-01-2022   (N.B You can enter your desired start and end date)
  

## Graph plotted

![Graph plotted](https://github.com/Oluwadurotimi10/CLI_APP/blob/main/graph1.PNG)
