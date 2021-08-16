# 정수형 수열

## 프로젝트 소개 

이 프로젝트는 처음으로 오픈소스에 컨트리뷰트 하고 싶은 사람에게 가장좋은 선택이자 상대적으로 간단한 입문자용 오프소스 프로젝트 입니다. 누구나 자유롭게 프로젝트에 기여할 수 있습니다.

이 프로젝트의 목적은 당신이 선택한 프로그래밍의 언어로 만들어진 알고리즘 데이터베이스르 제공하는 것입니다. 각각의 알고리즘은 다음의 위키피티아 주소에 리스트된 유명한 수열에서 n번쨰 숫자를 반환할 것입니다. https://en.wikipedia.org/wiki/List_of_integer_sequences

위의 위키피디아 주소는 소수, 콜라코스키 수열, 모츠키 수, 루카스 수, 기타등등과 같은 유명한 정수형 수열들을 포함하고 있습니다. 

'n'은 사용자의 의해 입력된 정수를 나타냅니다. 예를 들어, 만약에 유저가 2를 입력하였다면, 당신의 알고리즘은 해당 수열의 3번째 원소를 반환해야 합니다. (그 이유는 인덱싱이 0에서 시작하기 떄문에, n=0 은 첫번쨰 원소, n=1 은 두번째 원소를 의미합니다.)

만약에 누군가가 해당 위키피디아 페이지에 있는 난해한 정수형 수열들 중 하나를 코드로 실현하고자 한다면, 인터넷에 이 수열들을 생성하는 코드가 존재하지 않기 떄문에, 그 사람은 수열에서 n번째 숫자를 찾기 위해서 자기만의 알고리즘을 처음부터 끝까지 만들어야 할 것입니다. 

나는 프로젝트내에서 순열 알고리즘 데이터베이스를 완성하여 누군가가 자기만의 알고리즘을 만드는 데 시간으 낭비하지 않고 간단하게 내가 만든 데이타 베이스를 사용하였으면 좋겠습니다. 이 프로젝트는 Unlicense를 사용하기 때문에 누구나 자신의 소프트웨어에서 자유롭게 이 프로젝트 내의 코드를 사용하 수 있으며, 허락을 구할 필요가 없습니다.

## 프로젝트에 컨트리뷰트 하는 방법

해당 위키피디아 주소르 봐주시기 바랍니다.  https://en.wikipedia.org/wiki/List_of_integer_sequences

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



Alternatively, you can use the following git commands:

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

