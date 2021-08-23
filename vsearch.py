def search_for_vowels(phrase:str) -> set:
    """Возвращает булево значение в зависимости от присутствия любых гласных."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search_for_letters(phrase:set, letters:str='aeiou') -> set:
    """Находит множество букв из 'letters', найденных в указанном слове"""
    return set(letters).intersection(set(phrase))
