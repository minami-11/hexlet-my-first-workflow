from  hexlet_my_first_workflow.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH', ('Алярм! Хекслет не перевернулся'
                                           'как надо')


def test_reverse_for_empty_string():
    assert reverse('') == '', ('Алярм! Упало на пустой строке')
