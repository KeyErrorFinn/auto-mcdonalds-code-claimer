<h1 align="center">
  Automatic Mcdonalds Code Claimer <br>
  (NO LONGER MAINTAINED)
</h1>

<p align="center">
  <a href="https://github.com/KeyErrorFinn/auto-mcdonalds-code-claimer/commits/main/"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KeyErrorFinn/auto-mcdonalds-code-claimer" /></a>
  <a href="https://github.com/KeyErrorFinn/auto-mcdonalds-code-claimer/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/KeyErrorFinn/auto-mcdonalds-code-claimer" /></a>
</p>
<p align="center">
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" /></a>
</p>

This project is for getting mcdonalds codes from the <s>Bossman's Bargains discord server</s> and redeem them on the official mcdonalds page.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [How the program works](#how-the-program-works)
  - [TO-DO](#to-do)


## About the Project
> [!WARNING]
> This project is not finished and has been put on hold. The server has not also been checked in a while so it could not work at all.

The python script uses selenium to retrieve the code from the <s>Bossman's Bargains discord server</s> and uses that code on the official mcdonalds page which returns a code that can be used in the mcdonalds app.

### How the program works:
1) Creates chrome window with selenium
2) Goes to discord and logs in using a token
3) Goes to the discord server channel and generates a code
4) Gets the code and goes to the mcdonalds food-for-thought website
5) uses the code to automatically input the information using the url parameters
6) <s>Automatically Goes through all the pages and fills in the forms</s>
7) <s>Finishes and retrieves the code</s>

### TO-DO:
- [x] <s>Start Program</s>
- [x] <s>Gather Code</s>
- [x] <s>Use the code on website</s>
- [x] <s>Go through the form pages</s>
- [ ] Try using a mobile view due to form errors
- [ ] Retrieve final code from website
- [ ] Look into automatically using the code for the app.
