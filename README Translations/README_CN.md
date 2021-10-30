
<!-- Do not translate this -->
<details>
<summary>
<strong> Read this guide in other languages </strong>
</summary>
    <ul>
	    <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_AR.md"> Arabic </a></li>
		<li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_CN.md"> Chinese </a></li>
		<li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README.md"> English </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_FR.md"> French </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_DE.md"> German </a></li>
		<li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_HINDI.md"> Hindi </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_ID.md"> Indonesian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_IT.md"> Italian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_KR.md"> Korean </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_PT.md"> Portuguese </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_RO.md"> Romanian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_RU.md"> Russian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_ES.md"> Spanish </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_AF.md"> Afrikaans </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_EL.md"> Greek - Ελληνικά </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_JA.md"> Japanese - 日本語 </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_NL.md"> Dutch - Nederlands </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_SW.md"> Swahili - Kiswahili </a></li>
	</ul> 
</details>
<!-- Do not translate this -->

# 整数列表（Integer Sequences）

## 项目介绍

这是一个相对简单、初学者友好的开源项目。对于那些想要做出第一次开源贡献的人来说，这是一个很好的选择。
任何人都可以自由地做出贡献。

该项目的目的是使用您选择的编程语言创建一个算法数据库，其中每个算法将返回以下维基百科链接中列出的整数序列的第 n 个元素
https://en.wikipedia.org/wiki/List_of_integer_sequences

此维基百科链接包含许多著名整数序列的列表，例如质数、Kolakoski 序列、Motzkin 数、Lucas 数 等...

'n' 代表由用户输入的整数。例如，如果用户输入整数 '2'，那么你的算法应该返回序列的第三个元素（因为索引从 0 开始，序列的第一个元素是 n=0，第二个元素是 n = 1 ……）

如果有人需要在他们自己的程序中，实现维基百科页面上列出的一个更晦涩的整数序列，他们很可能需要从头开始开发自己的算法来找到序列的第 n 个元素，因为在于互联网上，暂时没有代码可以生成这些晦涩的数字序列。

我想在这个项目中完成算法的数据库，以便其他人可以简单地使用我数据库中的算法，而不是浪费时间开发自己的算法。因为本项目使用的是 Unlicense，任何人都可以在自己的软件中自由使用本项目中的代码，无需征得许可。

## 如何贡献

看看这个维基百科的链接： https://en.wikipedia.org/wiki/List_of_integer_sequences

查看整数序列中值得注意数字，并使用任何编程语言来开发一种算法，使其可以返回序列的第 n 个元素。索引从 0 开始，所以如果用户输入 n=0，这将返回序列的第一个元素，n=1 返回第二个元素等。

查看项目存储库，以确保您选择的整数序列的代码尚未添加到项目中

例如，如果有人用 Python 完成了贝尔数（Bell numbers）算法，并将其添加到项目中，您仍然可以使用任何其他语言（除了 python）为贝尔数创建算法

如果在项目存储库中，不存在特定整数序列的代码，您可以使用任何编程语言编写此整数序列

查看项目存储库中已经存在的代码，用它来指导并帮助您开发自己的算法。

在您对开发的代码感到满意后，使用拉取请求模板提交拉取请求，并更新跟踪列表。我将随后检查您的代码以确保它按预期工作，然后将其添加到项目存储库中。无论编码标准/代码质量如何，也无论代码速度如何，如果您的代码产生了正确的输出，它将被添加到项目存储库中。

您还可以修改和改进项目中的现有代码，提交拉取请求，我将审核您的更改。例如，您可以通过添加注释、空格、更改变量名称等来提高代码速度，或提高编码标准。

## 如何提交拉取请求

由于这是一个面向初学者的项目，我想为不知道的人简要解释一下最简单的提交拉取请求的方法。

打开我的存储库并单击“分叉”。这将创建存储库的分叉副本。

将您的代码添加到您的分叉副本中。

返回我的存储库并单击提交拉取请求。单击“跨叉比较”（compare across forks）。选择存储库的分叉副本作为头部，选择我的存储库作为基础。

单击提交拉取请求并留下有意义的注释，解释您尝试添加到项目中的代码。

1. 要在本地系统中克隆代码库，请使用

`git clone repo-link folder_name`

2. 要添加您刚刚更改的文件，请使用

`git add file-name`

3. 如果您更改了多个文件并希望一次将它们全部添加，请使用

`git add .`

4. 要提交这些更改，请使用

`git commit -m "Fixed Issue #issue_number"`

5. 要将改进放入主支，请使用

`git push origin Branch-name`
