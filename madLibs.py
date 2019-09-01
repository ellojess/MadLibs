def intro():
    print('Welcome to MadLibs! MadLibs are short, silly stories based on your words. ')
    #definition of madLibs: https://www.glowwordbooks.com/blog/category/kids-online-mad-libs/

    print('''
    a proper noun is the name of a person, place or thing: e.g., Alaska, Phillip, Tahoe
    \n a noun is a person, place, or thing: e.g.
    \n an adjective is a describing word: e.g., beautiful, warm, cold
    \n an adverb is word that modifies another word: e.g., gently, quitly
    \n a verb is a word that describes an action: e.g., hear, run, fly
    \n a number is an arithmetical value: e.g., 1, 200, 38
    ''')

#story 1: random story
random_story = '''
    Once upon a time in a town called {} where
    \n there was a bird named {},
    \n who felt {} and liked to {}
    \n {}. Sometime the bird would feel {} and eat {}.
    \n But when the bird would try to eat {},
    \n they would see their friend, the {}
    \n {}. Together, they would {} see {}
    \n {} for {} hours.
    '''


def main():

    proper_noun = []
    proper_noun.append(input('Enter a proper noun: '))
    proper_noun.append(input('Enter another proper noun: '))

    noun = []
    noun.append(input('Enter a noun: '))
    noun.append(input('Enter a noun: '))
    noun.append(input('Enter a noun: '))
    noun.append(input('Enter a noun: '))

    adjective = []
    adjective.append(input('Enter an adjective: '))
    adjective.append(input('Enter an adjective: '))
    adjective.append(input('Enter an adjective: '))
    adjective.append(input('Enter an adjective: '))

    adverb = []
    adverb.append(input('Enter an adverb: '))
    adverb.append(input('Enter an adverb: '))

    verb = input('Enter a verb: ')

    number = input('Enter a number: ')

    mad_lib = random_story.format(proper_noun[0],
                                proper_noun[1],
                                adjective[0],
                                adverb[0],
                                verb,
                                adjective[1],
                                noun[0],
                                noun[1],
                                adjective[2],
                                noun[2],
                                adverb[1],
                                adjective[3],
                                noun[3],
                                number)

    print(mad_lib)

intro()
main()
