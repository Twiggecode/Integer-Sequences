<!-- Do not translate this -->
<details>
<summary>
<strong> Read this guide in other languages </strong>
</summary>
    <ul>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README.md"> English </a></li>
        <li><a href="./README Translations\README_KR.md"> Korean </a></li>
        <li><a href="./README Translations\README_ES.md"> Spanish </a></li>
        <li><a href="./README Translations\README_RO.md"> Romanian </a></li>
        <li><a href="./README Translations\README_PT.md"> Portuguese </a></li>
        <li><a href="./README Translations\README_ID.md"> Indonesian </a></li>
        <li><a href="./README Translations\README_RU.md"> Russian </a></li>
    </ul>
</details>
<!-- Do not translate this -->

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

유명한 정수형 수열 리스트를 보시고 특정 프로그래밍 언어로 그 수열에서 n번째 원소를 반환하는 알고리즘을 만들어 주세요. 인덱싱은 0에서 시작하기 떄문에, 사용자 입력값이 n=0일 때 첫번째 원소를 반환하도록 해야하고, 사용자 입력값이 n=1일 때, 두번째 원소를 반환하도록 해야 합니다. 프로젝트 레포짓을 보시고 당신이 선택한 프로그래밍 언어로 만들어진 수열에 관한 코드가 프로젝트에 이미 있는지 확인해 주시기 바랍니다.

예를 들어, 만약 누군가가 이미 벨 숫자에 관한 파이썬 알고리즘을 만들어서 프로젝트에 추가하였다면, 당신은 얼마든지 파이썬이 아닌 다른 언어로 벨 숫자에 관한 알고리즘을 만들어서 프로젝트에 추가할 수 있습니다. 

만약 프로젝트 레포짓에 특정 수열에 관한 코드가 존재하지 않는다면, 당신은 당신이 원하는 아무 프로그래밍 언어로 수열에 관한 코드를 만들 수 있습니다.

프로젝트 레포짓에 이미 만들어진 코드를 보시고, 당신만의 알고리즘으 만드는데 참고 하시기 바랍니다.

당신이 만든 코드에 만족한다면, pull request template 을 사용하여 코드를 제출해 주세요. 제가 당신의 코드를 리뷰하여 예상대로 작동하는지 확인하 다음 프로젝트 레포짓에 추가하여 드립니다. 만약 당신이 만든 코드가 정확한 결과를 도출 한다면, 코드의 실행 속도, 코드의 가치와 관계없이, 당신의 코드는 항상 프로젝트 레포짓에 추가될 것입니다. 

당신은 프로젝트내에 이미 존재하는 코드를 변경하거나 향상 시킬 수 있습니다. pull request 를 통해 코드를 제출 하시면 제가 변경사항을 확인할 것입니다. 예를 들어, 당신은 코드의 속도를 향상 시킬 수 있습니다, 또한 코멘트, 스페이스를 추가하고, 변수의 이름을 변경하여 코드의 형식적인 부분을 향상 시킬 수 있습니다.



## Pull Request 하는 방법

이 프로그램이 초보자를 위한 것이기에, 이것을 모르는 사람으 위해 저는 pull request를 하느 가장 간단한 방법을 간력하게 설명하고자 합니다.

제 레포짓을 열고 "Fork"를 클릭해 주세요. 이것은 복사된 레포짓을 만들 것입니다.

복사된 파일에 당신의 코드를 추가해 주세요.

제 레포짓으로 돌와오셔셔 "submit pull request"을 클릭해주세요. "compare across forks"을 클릭해주세요. 당신의 레포짓에 있는 복삽본을 head로 선택하시고 제 레포짓을 base로 선택하여 주세요.

"submit a pull request"을 클릭하신 후 당신이 프로젝트에 추가하려느 코드를 설명하는 의미있는 코멘트를 남겨주세요.


대안으로, 당신은 다음의 git 커맨드를 사용할 수도 있습니다:

1. 로컬 시스템에서 사용하기 위해 레포짓으로 복사하는 경우

```git clone repo-link folder_name```

2. 당신이 바꾼 파일을 stage 하기 위한 경우

```git add file-name```
   
3. 당신의 여러개의 파일을 변경 한 후 여러개의 파일을 한번에 stage 하려느 경우

```git add .``` 

4. 당신이 변경한 사항을 commit 하려는 경우

```git commit -m "Fixed Issue #issue_number"```

5. 변경사항을 레포짓에 push 하려는 경우

```git push origin Branch-name```
