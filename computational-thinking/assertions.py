# assert <expression boolean>, <message error>

def first_letter(list_of_words):
    first_letters = []
    
    for word in list_of_words:
      try:
        assert type(word) == str, f'{word} is not a str'
        assert len(word) > 0 , 'Empty are not allowed'
        first_letters.append(word[0])
      except AssertionError as e:
        print(e)

    return first_letters

def run():
  my_list = ['Angel', 5.5, '', 2, '43952353', 0.35]
  print('First valid letter are: ', first_letter(my_list))


if __name__ == '__main__':
  run()