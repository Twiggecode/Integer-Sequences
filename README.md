<!-- Do not translate this -->
<details>
<summary>
<strong> Read this guide in other languages </strong>
</summary>
    <ul>
        <li><a href="./README.md"> English </a></li>
    </ul>
</details>
<!-- Do not translate this -->

# Integer Sequences

## Project Introduction

This is a relatively simple, beginner friendly open source project that is an excellent choice to contribute to for those who want to make their first open source contributions. However, anyone is free to contribute.

The purpose of this project is to create a database of algorithms using your choice of programming language, where each algorithm will return the nth element of one of the notable integer sequences listed on the following wikipedia link. https://en.wikipedia.org/wiki/List_of_integer_sequences

This wikipedia link contains a list of many notable integer sequences, such as the prime numbers, the Kolakoski sequence, Motzkin numbers, Lucas numbers etc...

'n' Represents an integer input by the user. For example, if the user inputs the integer '2', then your algorithm should return the third element of the sequence (because the indexing starts at 0, the first element of the sequence is for n=0, the second element is for n=1, etc).

If someone needs to implement one of the more obscure integer sequences listed on the wikipedia page within their own program, it is likely that they will have to develop their own algorithm from scratch to find the nth element of the sequence, as no code to generate these obscure sequences will exist on the internet. 

I want to complete the database of algorithms within this project so that others can simply use the algorithms within my database instead of wasting time developing their own algorithms. Anyone is free to use the code within this project in their own software, there is no need to ask for permission because this project uses the Unlicense.

## How to Contribute

Have a look at the wikipedia link https://en.wikipedia.org/wiki/List_of_integer_sequences

Look at the list of notable integer sequences and develop an algorithm in any programming language to return the nth element of the sequence. The indexing starts at 0, so if the user inputs n=0, this will return the first element of the sequence, n=1 returns the second element etc. Look at the project repository to ensure that code for your integer sequence of choice has not already been added to the project in your programming language of choice.

For example, if someone has created a Python algorithm for the Bell numbers and added it to the project, you can still create an algorithm for the Bell numbers in any other language, just not with Python.

If no code for a specific integer sequence exists in the project repository, you can create code for this integer sequence in any programming language you want.

Look at code that already exists within the project repository, use this to guide you and help you develop your own algorithm.

After you are happy with the code you have developed, submit a pull request using the pull request template. I will then review your code to ensure that it works as expected, and then add it to the project repository. If your code produces the correct outputs, it will be always be added to the project repository, regardless of the coding standards/code quality, and regardless of the speed of the code.

You can also modify and improve existing code within the project, submit a pull request and I will review your changes. For example, you can improve the speed of code, or improve the coding standards by adding comments, spaces, changing variable names, etc.




## How to Submit a Pull Request

As this is a project aimed at beginners, I want to briefly explain the most simple way to submit a pull request for those who don't know.

Open my repository and click "Fork". This creates a forked copy of the repository.

Add your code to your forked copy.

Return to my repository and click submit pull request. Click "compare across forks". Select your forked copy of the repository as the head and my repository as the base.

Click submit a pull request and leave a meaningful comment explaining the code you are attempting to add to the project.



Alternatively, you can use the following git commands -

1. To clone the repository in your local system use

```git clone repo-link folder_name```

2. To stage the file you just changed use

```git add file-name```
   
3. In case you have changed multiple files and want to stage them all at once use

```git add .``` 

4. To commit those changes use

```git commit -m "Fixed Issue #issue_number"```

5. To push these changes use

```git push origin Branch-name```


