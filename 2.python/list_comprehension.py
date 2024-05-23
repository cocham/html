#-*- coding: euc-kr -*-

# 2. ���ڿ��� ���� �� ����
words = ["apple", "banana", "cherry", "dragonfruit"]
words_lengths = [len(n) for n in words]
print(words_lengths)

# 4. ���ڿ� ����Ʈ���� ���̰� 3 ������ �ܾ�鸸 �����ϱ�
words = ["apple", "banana", "cherry", "dragonfruit","egg"]
short_words = [x for x in words if len(x)<=3]
print(short_words)

# 5. ��ø ����Ʈ ��ġ��
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#flattened_list = [y for x in nested_list for y in x]
flattened_list = [x[i] for x in nested_list for i in range(len(x))]
print(flattened_list)

# 6. Ư�� ����(5���� ū��)�� �����ϴ� ��� ���͸�
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = [x for x in numbers if x>5]
print(greater_than_five)

# 7. ���ڿ� ����Ʈ���� ù ���ڰ� ������ �ܾ�� �����ϱ�
words = ["apple", "banana", "cherry", "apricot", "egg"]
vowel_starting_words = [x for x in words if x[0] in "aeiou"]
print(vowel_starting_words)

